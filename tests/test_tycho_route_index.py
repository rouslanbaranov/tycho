"""E04-04 routing fixtures; no external network access or book enrichment."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import route_index as route  # noqa: E402
import frontmatter_generate as front  # noqa: E402

try:
    import yaml  # noqa: F401
    import jsonschema  # noqa: F401
    HAS_DEPS = True
except ImportError:
    HAS_DEPS = False


class PureRouteTests(unittest.TestCase):
    def test_score_and_budget_without_dependencies(self):
        data = {
            "snapshot_sha256": "snapshot-example", "coverage": "partial",
            "unannotated_paths": ["book/missing.md"], "documents": [
                {"id": "tycho.page.01h9abcdef", "title": "Queueing and latency",
                 "questions": ["What causes queue delay?"],
                 "summary": "Conditional queueing law", "topics": ["queueing"],
                 "keywords": ["latency"], "kind": "page", "path": "book/a.md",
                 "evidence_status": "unknown"},
                {"id": "tycho.page.02h9abcdef", "title": "Caching",
                 "questions": ["How does caching work?"],
                 "summary": "Cache freshness and correctness", "topics": ["caching"],
                 "keywords": ["cache"], "kind": "page", "path": "book/b.md",
                 "evidence_status": "unknown"}
            ]
        }
        result = route.route(data, "queueing latency", limit=1)
        self.assertEqual(result["returned"], 1)
        self.assertTrue(result["truncated"] is False)
        self.assertEqual(result["results"][0]["id"], "tycho.page.01h9abcdef")
        self.assertEqual(result["coverage"], "partial")
        self.assertEqual(result["unannotated_pages"], 1)
        with self.assertRaises(ValueError):
            route.route(data, "queueing", limit=1000)


@unittest.skipUnless(HAS_DEPS, "requires jsonschema and PyYAML routing dependencies")
class SnapshotRoutingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root/"book").mkdir()
        (self.root/"book/performance").mkdir()
        (self.root/"schemas").mkdir()
        shutil.copy(ROOT/"schemas/document-metadata.v1.schema.json",
                    self.root/"schemas/document-metadata.v1.schema.json")
        self.book = json.loads((ROOT/"fixtures/metadata-valid-book.v1.json").read_text())
        self.page = json.loads((ROOT/"fixtures/metadata-valid-page.v1.json").read_text())
        self.page["parent_id"] = self.book["id"]
        self.write(self.book, "# Synthetic book root\n")
        self.write(self.page, "# Queueing explanation\nSynthetic fixture.\n")

    def write(self, metadata, body):
        file = self.root / metadata["canonical_path"]
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(front.render(metadata)+"\n"+body)

    def test_stable_full_index(self):
        first = route.canonical_scan(self.root)
        second = route.canonical_scan(self.root)
        self.assertEqual(first, second)
        self.assertEqual(first["coverage"], "complete")
        self.assertEqual(len(first["documents"]), 2)

    def test_generated_route_and_exact_snapshot_read(self):
        data = route.canonical_scan(self.root)
        out = route.route(data, "queueing capacity", limit=1)
        self.assertEqual(out["results"][0]["id"], self.page["id"])
        node, body = route.selected(self.root, data, self.page["id"])
        self.assertEqual(node["path"], self.page["canonical_path"])
        self.assertIn("Synthetic fixture", body)

    def test_partial_coverage_is_explicit_not_silent(self):
        (self.root/"book/extra.md").write_text("# No metadata\n")
        with self.assertRaisesRegex(ValueError, "unannotated"):
            route.canonical_scan(self.root)
        data = route.canonical_scan(self.root, allow_partial=True)
        self.assertEqual(data["coverage"], "partial")
        self.assertEqual(data["unannotated_paths"], ["book/extra.md"])

    def test_cli_partial_check_requires_explicit_disposition(self):
        (self.root/"book/extra.md").write_text("# No metadata\n")
        data = route.canonical_scan(self.root, allow_partial=True)
        index = self.root/"route-index.json"
        index.write_text(json.dumps(data))
        command = [sys.executable, str(ROOT/"scripts/route_index.py"), "check",
                   "--root", str(self.root), "--index", str(index)]
        denied = subprocess.run(command, text=True, capture_output=True)
        self.assertNotEqual(denied.returncode, 0)
        self.assertIn("partial routing coverage", denied.stderr)
        allowed = subprocess.run(command + ["--allow-partial"], text=True, capture_output=True)
        self.assertEqual(allowed.returncode, 0, allowed.stderr)

    def test_dangling_related_reference_rejected(self):
        self.page["route_hints"]["related_ids"] = ["tycho.page.unknown1"]
        self.write(self.page, "# Synthetic page\n")
        with self.assertRaisesRegex(ValueError, "dangling related"):
            route.canonical_scan(self.root)

    def test_parent_cycle_rejected(self):
        self.page["parent_id"] = self.page["id"]
        self.write(self.page, "# Synthetic page\n")
        with self.assertRaisesRegex(ValueError, "cycle"):
            route.canonical_scan(self.root)

    def test_duplicate_ids_detected(self):
        duplicated = deepcopy(self.page)
        duplicated["canonical_path"] = "book/performance/duplicate.md"
        self.write(duplicated, "# Duplicate identity\n")
        with self.assertRaisesRegex(ValueError, "duplicate ID"):
            route.canonical_scan(self.root)

    def test_changed_document_invalidates_snapshot(self):
        data = route.canonical_scan(self.root)
        path = self.root / self.page["canonical_path"]
        path.write_text(path.read_text()+"\nA later change.")
        with self.assertRaisesRegex(ValueError, "since index"):
            route.selected(self.root, data, self.page["id"])

    def test_file_content_and_index_freshness(self):
        data = route.canonical_scan(self.root)
        index = self.root/"route-index.json"
        index.write_text(json.dumps(data))
        self.assertEqual(route.load_fresh(self.root,index), data)
        path = self.root / self.page["canonical_path"]
        path.write_text(path.read_text()+"\nEdit changes snapshot.")
        with self.assertRaisesRegex(ValueError, "stale"):
            route.load_fresh(self.root,index)


if __name__ == "__main__":
    unittest.main()

"""Offline tests for V12 search facets and artifact lookup."""
import hashlib
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import route_index  # noqa: E402
import section_fts_index  # noqa: E402
import section_search  # noqa: E402

PAGE = (
    "---\nid: tycho.page.v12alpha\nkind: page\ntitle: V12 alpha\n---\n"
    "# V12 alpha\n\nModel scope discusses timeout and simulation evidence.\n\n"
    "## Timeout boundary {#timeout-boundary}\nTimeout detail with token quasar.\n"
)


class V12SearchFacetTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="tycho-v12-facets-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "book/volumes/v12-modeling-simulation-and-decision-validation").mkdir(
            parents=True)
        (self.root / "generated").mkdir()
        (self.root / "edition/v12/models").mkdir(parents=True)
        self.page = (self.root / "book/volumes/v12-modeling-simulation-and-decision-validation/"
                     "v12-alpha.md")
        self.page.write_text(PAGE, encoding="utf-8")
        (self.root / "edition/v12/models/checkout.json").write_text(
            json.dumps({"id": "tycho.model.checkout"}), encoding="utf-8")
        self.write_indexes()

    def path(self):
        return self.page.relative_to(self.root).as_posix()

    def write_indexes(self):
        (self.root / "generated/v12-index.v1.json").write_text(json.dumps({
            "documents": [
                {"id": "tycho.page.v12alpha", "path": self.path(),
                 "title": "V12 alpha", "artifact_type": "document",
                 "volume": "v12", "pattern_ids": ["tycho.pattern.timeout"],
                 "evidence_status": "source-linked", "summary": "V12 alpha"},
                {"id": "tycho.model.checkout",
                 "path": "edition/v12/models/checkout.json",
                 "title": "Checkout model", "artifact_type": "model",
                 "volume": "v12", "pattern_ids": ["tycho.pattern.timeout"],
                 "evidence_status": "model-verified", "summary": "Checkout"},
            ]
        }), encoding="utf-8")
        (self.root / "edition/v12/reverse-index.v1.json").write_text(json.dumps({
            "patterns": {"tycho.pattern.timeout": [
                {"artifact_type": "model", "id": "tycho.model.checkout",
                 "path": "edition/v12/models/checkout.json"}
            ]}
        }), encoding="utf-8")

    def docs(self):
        text = self.page.read_text(encoding="utf-8")
        return [{
            "id": "tycho.page.v12alpha", "path": self.path(),
            "title": "V12 alpha", "kind": "page", "topics": ["simulation"],
            "evidence_status": "source-linked",
            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        }]

    def fake_scan(self, root, allow_partial):
        docs = self.docs()
        snapshot = hashlib.sha256(
            "|".join(d["id"] + d["sha256"] for d in docs).encode()).hexdigest()
        return {"snapshot_sha256": snapshot, "coverage": "complete",
                "unannotated_paths": [], "documents": docs}

    def build(self):
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            return section_fts_index.publish(self.root, full=True)

    def test_schema_and_search_return_v12_facets(self):
        self.build()
        db_path = self.root / "generated" / section_fts_index.INDEX_NAME
        with sqlite3.connect(db_path) as db:
            columns = {row[1] for row in db.execute("PRAGMA table_info(sections)")}
            self.assertIn("artifact_type", columns)
            self.assertIn("volume", columns)
            patterns = db.execute(
                "SELECT pattern_id FROM section_patterns").fetchall()
            self.assertEqual(set(patterns), {("tycho.pattern.timeout",)})
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            result = section_search.search(
                self.root, "quasar", volume="v12",
                pattern_ids=["tycho.pattern.timeout"], include_artifacts=True,
                abstain=False)
        self.assertEqual(result["status"], "ok")
        top = result["results"][0]
        self.assertEqual(top["section_id"], "timeout-boundary")
        self.assertEqual(top["artifact_type"], "document")
        self.assertEqual(top["volume"], "v12")
        self.assertEqual(top["pattern_ids"], ["tycho.pattern.timeout"])
        self.assertEqual(result["facets"]["volume"], {"v12": 1})
        self.assertEqual(result["facets"]["pattern_id"],
                         {"tycho.pattern.timeout": 1})
        self.assertEqual(result["artifact_total"], 1)
        self.assertEqual({item["artifact_type"] for item in result["artifacts"]},
                         {"model"})

    def test_artifact_type_intent_priority(self):
        self.assertEqual(
            section_search._artifact_type_intent(["input"]), "scenario")
        self.assertEqual(
            section_search._artifact_type_intent(["result"]), "run")
        self.assertEqual(
            section_search._artifact_type_intent(["input", "run"]), "run")
        self.assertEqual(
            section_search._artifact_type_intent(["decision", "runs"]),
            "decision")

    def test_include_artifacts_filters_by_query(self):
        self.build()
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            matched = section_search.search(
                self.root, "checkout model", volume="v12",
                include_artifacts=True, abstain=False)
            unmatched = section_search.search(
                self.root, "zebra", volume="v12",
                include_artifacts=True, abstain=False)
            volume_only = section_search.search(
                self.root, "zebra", volume="v12", abstain=False)
        self.assertEqual([item["id"] for item in matched["artifacts"]],
                         ["tycho.model.checkout"])
        self.assertEqual(unmatched["artifacts"], [])
        self.assertEqual(volume_only["artifacts"], [])

    def test_changed_v12_index_invalidates_search(self):
        self.build()
        payload = json.loads((self.root / "generated/v12-index.v1.json").read_text())
        payload["documents"][0]["pattern_ids"] = []
        (self.root / "generated/v12-index.v1.json").write_text(
            json.dumps(payload), encoding="utf-8")
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            with self.assertRaises(section_search.SearchError):
                section_search.search(self.root, "quasar", volume="v12",
                                      abstain=False)

    def test_v12_artifact_lookup_filters_pattern_and_type(self):
        payload = section_search.v12_artifacts(
            self.root, pattern_ids=["tycho.pattern.timeout"],
            artifact_type="model", volume="v12")
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["returned"], 1)
        self.assertEqual(payload["artifacts"][0]["id"], "tycho.model.checkout")
        self.assertEqual(payload["artifacts"][0]["pattern_ids"],
                         ["tycho.pattern.timeout"])


if __name__ == "__main__":
    unittest.main()

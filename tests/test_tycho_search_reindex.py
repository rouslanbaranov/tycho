"""Tests for the pre-enrichment search snapshot harness."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ROOT / "scripts"))
import search_reindex  # noqa: E402


class SearchReindexTests(unittest.TestCase):
    def test_content_digest_is_deterministic_and_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "book").mkdir()
            (root / "book/a.md").write_text("# A\n", encoding="utf-8")
            first = search_reindex.content_digest(root)
            second = search_reindex.content_digest(root)
            self.assertEqual(first, second)
            (root / "book/a.md").write_text("# B\n", encoding="utf-8")
            self.assertNotEqual(first, search_reindex.content_digest(root))

    def test_manifest_has_qrels_and_snapshot_metadata(self):
        manifest = json.loads(
            (ROOT / "edition/patterns/search-pre-enrichment.v1.json")
            .read_text(encoding="utf-8"))
        self.assertEqual(manifest["kind"], "pre-enrichment-search-snapshot")
        self.assertEqual(manifest["content"]["files"], 423)
        self.assertGreaterEqual(manifest["section_index"]["sections"], 1)
        self.assertGreaterEqual(manifest["section_index"]["passages"], 1)
        self.assertTrue(manifest["qrels"])
        self.assertIn("quality_claims", manifest)

    def test_check_is_fail_closed_on_stale_qrels(self):
        report = search_reindex.check(ROOT)
        self.assertIn(report["status"],
                      {"current", "current-with-stale-qrels", "stale"})
        self.assertEqual(report["content_files"], 423)
        if report["status"] == "current-with-stale-qrels":
            self.assertIn("qrels-stale", report["issues"])
            self.assertTrue(report["qrels_stale"])

    def test_check_reports_content_change(self):
        with patch.object(search_reindex, "content_digest",
                          return_value=("0" * 64, 423)):
            report = search_reindex.check(ROOT)
        self.assertIn("content-changed", report["issues"])
        self.assertEqual(report["status"], "stale")

    def test_check_reports_stale_index(self):
        stale = {"snapshot": "f" * 64, "coverage": "complete",
                 "documents": 423, "sections": 1, "passages": 0,
                 "bytes": 1}
        with patch.object(search_reindex.section_fts_index, "stats",
                          return_value=stale):
            report = search_reindex.check(ROOT)
        self.assertIn("index-stale", report["issues"])

    def test_check_reports_changed_qrels_file(self):
        original = search_reindex.sha

        def fake(path):
            if str(path).endswith("corpus-qrels.v2.json"):
                return "0" * 64
            return original(path)

        with patch.object(search_reindex, "sha", side_effect=fake):
            report = search_reindex.check(ROOT)
        self.assertIn("qrels-stale", report["issues"])


if __name__ == "__main__":
    unittest.main()

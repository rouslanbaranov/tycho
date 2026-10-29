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

    def test_diff_reports_page_and_qrels_changes(self):
        old = {"content": {"files_sha256": {"a": "1", "b": "2"}},
               "qrels": [{"path": "q", "sha256": "x"}],
               "section_index": {"sections": 2, "passages": 1,
                                 "sections_by_path": {"a": ["a#1"]}}}
        new = {"content": {"files_sha256": {"a": "1", "c": "3"}},
               "qrels": [{"path": "q", "sha256": "y"}],
               "section_index": {"sections": 3, "passages": 2,
                                 "sections_by_path": {
                                     "a": ["a#1", "a#2"]}}}
        report = search_reindex.diff_manifests(old, new)
        self.assertEqual(report["added_pages"], ["c"])
        self.assertEqual(report["removed_pages"], ["b"])
        self.assertEqual(report["qrels_changed"], ["q"])
        self.assertEqual(report["added_sections"], ["a#2"])
        self.assertEqual(report["section_changed_pages"], ["a"])
        self.assertEqual(report["status"], "changed")

    def test_reindex_lock_excludes_concurrent_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            with search_reindex.reindex_lock(tmp):
                with self.assertRaises(RuntimeError):
                    with search_reindex.reindex_lock(tmp):
                        pass

    def test_verify_wraps_deep_index_verification(self):
        deep = {"outcome": "verified", "snapshot": "s" * 64}
        with patch.object(search_reindex.section_fts_index, "verify",
                          return_value=deep), \
             patch.object(search_reindex, "check",
                          return_value={"qrels_stale": ["q"]}):
            report = search_reindex.verify(ROOT)
        self.assertEqual(report["status"], "verified")
        self.assertEqual(report["qrels_stale"], ["q"])

    def test_build_forwards_full_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            route = {"snapshot_sha256": "r" * 64, "documents": [],
                     "coverage": "complete"}
            result = {"snapshot": "s" * 64, "reused_documents": 3}
            stats = {"sections": 1, "passages": 0, "bytes": 1}
            with patch.object(search_reindex, "ROUTE_INDEX",
                              root / "generated/route.json"), \
                 patch.object(search_reindex.route_index, "canonical_scan",
                              return_value=route), \
                 patch.object(search_reindex.section_fts_index, "publish",
                              return_value=result) as publish, \
                 patch.object(search_reindex.section_fts_index, "stats",
                              return_value=stats):
                search_reindex.build(root, full=False)
                self.assertFalse(publish.call_args.kwargs["full"])
                search_reindex.build(root, full=True)
                self.assertTrue(publish.call_args.kwargs["full"])

    def test_check_reports_missing_or_corrupt_index(self):
        for exc in (RuntimeError("missing"),
                    search_reindex.sqlite3.DatabaseError("corrupt")):
            with patch.object(search_reindex.section_fts_index, "stats",
                              side_effect=exc):
                report = search_reindex.check(ROOT)
            self.assertIn("index-missing", report["issues"])


if __name__ == "__main__":
    unittest.main()

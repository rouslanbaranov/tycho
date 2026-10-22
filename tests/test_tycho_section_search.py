"""Offline search/read tests over a synthetic section snapshot.

No external corpus, network, YAML/schema dependency or book rewriting.
"""
import hashlib
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

PAGE_A = (
    "---\nid: tycho.page.alpha\nkind: page\ntitle: Alpha search page\n---\n"
    "# Alpha search page\n\nOverview discusses bounded retrieval and snapshots.\n\n"
    "## Retry budget {#retry-budget}\nRetry budget detail with token zebra.\n\n"
    "### Nested detail\nNested text stays in its parent section.\n\n"
    "## Caching\nCache stampede and invalidation notes.\n"
    "## Retry policy\nAnother retry note for truncation.\n"
)
PAGE_B = (
    "---\nid: tycho.page.beta\nkind: landing\ntitle: Beta landing\n---\n"
    "# Beta landing\n\nDeployment rollback overview for the landing page.\n"
)


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="tycho-search-fixture-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "book").mkdir()
        (self.root / "generated").mkdir()
        self.a = self.root / "book" / "a.md"
        self.b = self.root / "book" / "b.md"
        self.a.write_text(PAGE_A, encoding="utf-8")
        self.b.write_text(PAGE_B, encoding="utf-8")

    def docs(self):
        docs = []
        for path, identity, kind, title, topics, evidence in (
                (self.a, "tycho.page.alpha", "page", "Alpha search page",
                 ["search-architecture", "caching"], "source-linked"),
                (self.b, "tycho.page.beta", "landing", "Beta landing",
                 ["deployment"], "unknown")):
            text = path.read_text(encoding="utf-8")
            docs.append({
                "id": identity, "path": path.relative_to(self.root).as_posix(),
                "title": title, "kind": kind, "topics": topics,
                "evidence_status": evidence,
                "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            })
        return docs

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

    def search(self, *args, **kwargs):
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            return section_search.search(self.root, *args, **kwargs)

    def read(self, *args, **kwargs):
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            return section_search.read(self.root, *args, **kwargs)

    def test_ranked_search_returns_section_and_citation(self):
        self.build()
        result = self.search("zebra")
        self.assertEqual(result["status"], "ok")
        top = result["results"][0]
        self.assertEqual(top["section_id"], "retry-budget")
        self.assertEqual(top["section_key"], "tycho.page.alpha#retry-budget")
        self.assertEqual(top["citation"], "book/a.md#retry-budget")
        self.assertEqual(top["matched_terms"], ["zebra"])
        self.assertGreater(top["score"], 0)
        self.assertEqual(top["score_kind"], "bm25")
        self.assertFalse(top["excerpt"].startswith("## "))
        self.assertIn("token zebra", top["excerpt"])
        self.assertEqual(result["ranker_version"],
                         section_search.RANKER_VERSION)

    def test_limit_truncation_and_empty_result(self):
        self.build()
        result = self.search("overview", limit=1)
        self.assertEqual(result["returned"], 1)
        self.assertTrue(result["truncated"])
        self.assertEqual(self.search("nothingmatches")["status"], "no-results")
        self.assertEqual(self.search("nothingmatches")["returned"], 0)

    def test_default_returns_best_section_per_document(self):
        self.build()
        deduped = self.search("retry")
        self.assertEqual(deduped["returned"], 1)
        self.assertEqual(deduped["result_scope"],
                         "best-section-per-document")
        self.assertFalse(deduped["truncated"])
        sections = self.search("retry", all_sections=True)
        self.assertEqual(sections["returned"], 2)
        self.assertEqual(sections["result_scope"], "all-sections")

    def test_kind_topic_evidence_and_path_filters(self):
        self.build()
        self.assertEqual(self.search("rollback", kind="landing")["returned"], 1)
        self.assertEqual(self.search("rollback", kind="page")["status"],
                         "no-results")
        self.assertEqual(self.search("rollback", topic="deployment")["returned"], 1)
        self.assertEqual(self.search("rollback", topic="caching")["status"],
                         "no-results")
        self.assertEqual(
            self.search("rollback", evidence_status="unknown")["returned"], 1)
        self.assertEqual(
            self.search("rollback", evidence_status="source-linked")["status"],
            "no-results")
        self.assertEqual(
            self.search("rollback", path_prefix="book/b")["returned"], 1)
        self.assertEqual(
            self.search("rollback", path_prefix="book/a")["status"],
            "no-results")

    def test_multi_term_query_uses_any_term_ranking(self):
        self.build()
        result = self.search("zebra rollback")
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["match_mode"], "any-terms")
        self.assertNotIn("broadened", result)
        paths = {item["path"] for item in result["results"]}
        self.assertEqual(paths, {"book/a.md", "book/b.md"})

    def test_query_and_limit_validation(self):
        self.build()
        for query in ("", "   ", "...", "&&&"):
            with self.assertRaises(section_search.SearchError):
                self.search(query)
        for limit in (0, 21, -1):
            with self.assertRaises(section_search.SearchError):
                self.search("retry", limit=limit)
        with self.assertRaises(section_search.SearchError):
            self.search("retry", path_prefix="../outside")
        with self.assertRaises(section_search.SearchError):
            self.search("retry", path_prefix="/book")

    def test_fts_operator_text_is_quoted(self):
        self.build()
        result = self.search('zebra" OR "stampede')
        self.assertIn(result["status"], {"ok", "no-results"})
        self.assertEqual(result["query"], 'zebra" OR "stampede')

    def test_stale_snapshot_is_refused(self):
        self.build()
        self.a.write_text(self.a.read_text() + "\n## Later\nNew text.\n",
                          encoding="utf-8")
        with self.assertRaises(section_search.SnapshotMismatch) as caught:
            self.search("zebra")
        self.assertEqual(caught.exception.status, "snapshot-mismatch")

    def test_missing_or_tampered_index_is_unavailable(self):
        with self.assertRaises(section_search.SearchError) as caught:
            self.search("zebra")
        self.assertEqual(caught.exception.status, "not-available")
        self.build()
        path = self.root / "generated" / section_fts_index.INDEX_NAME
        with sqlite3.connect(path) as db:
            db.execute("DELETE FROM fts WHERE rowid=1")
            db.commit()
        with self.assertRaises(section_search.SearchError) as caught:
            self.search("zebra")
        self.assertEqual(caught.exception.status, "not-available")

    def test_bounded_read_offsets_and_truncation(self):
        self.build()
        key = "tycho.page.alpha#retry-budget"
        start = self.read(key, 0, 20)
        self.assertEqual(start["status"], "ok")
        self.assertEqual(start["returned_chars"], 20)
        self.assertEqual(
            start["content"],
            PAGE_A[PAGE_A.index("## Retry budget"):][:20])
        self.assertEqual(start["next_offset"], 20)
        self.assertTrue(start["truncated"])
        tail = self.read(key, start["total_chars"] - 5, 100)
        self.assertEqual(tail["returned_chars"], 5)
        self.assertIsNone(tail["next_offset"])
        self.assertFalse(tail["truncated"])
        self.assertGreater(tail["document_char_start"], 0)

    def test_read_validation_and_unknown_section(self):
        self.build()
        key = "tycho.page.alpha#retry-budget"
        with self.assertRaises(section_search.SearchError) as caught:
            self.read("missing#section", 0, 10)
        self.assertEqual(caught.exception.status, "not-found")
        for offset, budget in ((-1, 10), (0, 0), (0, 5001)):
            with self.assertRaises(section_search.SearchError):
                self.read(key, offset, budget)
        with self.assertRaises(section_search.SearchError):
            self.read(key, 100000, 10)


if __name__ == "__main__":
    unittest.main()

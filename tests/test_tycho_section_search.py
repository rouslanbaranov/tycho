"""Offline search/read tests over a synthetic section snapshot.

No external corpus, network, YAML/schema dependency or book rewriting.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import route_index  # noqa: E402
import section_evidence  # noqa: E402
import section_fts_index  # noqa: E402
import section_search  # noqa: E402

PAGE_A = (
    "---\nid: tycho.page.alpha\nkind: page\ntitle: Alpha search page\n---\n"
    "# Alpha search page\n\nOverview discusses bounded retrieval and snapshots.\n\n"
    "## Retry budget {#retry-budget}\nRetry budget detail with token zebra.\n\n"
    "### Nested detail\nNested text stays in its parent section.\n\n"
    "## Caching\nCache stampede and invalidation notes.\n\n"
    "### Stampede guard\nQuasar guard uses a single-flight lease.\n\n"
    "### Eviction\nEviction bounds resident memory.\n\n"
    "### TTL\nTTL bounds staleness.\n\n"
    "### Refresh\nRefresh loads ahead of demand.\n\n"
    "### Single flight\nSingle flight coalesces concurrent misses.\n\n"
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
        kwargs.setdefault("abstain", False)
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            return section_search.search(self.root, *args, **kwargs)

    def read(self, *args, **kwargs):
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            return section_search.read(self.root, *args, **kwargs)

    def open_manifest(self):
        db, manifest = section_search.open_snapshot(self.root)
        db.close()
        return manifest

    def index_path(self):
        return self.root / "generated" / section_fts_index.INDEX_NAME

    def tamper_manifest(self, **changes):
        with sqlite3.connect(self.index_path()) as db:
            raw = db.execute(
                "SELECT value FROM meta WHERE key='manifest'").fetchone()[0]
            manifest = json.loads(raw)
            manifest.update(changes)
            db.execute("UPDATE meta SET value=? WHERE key='manifest'",
                       (json.dumps(manifest),))
            db.commit()

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

    def test_section_rerank_is_opt_in(self):
        self.build()
        default = self.search("zebra")
        reranked = self.search("zebra", section_rerank=True)
        self.assertEqual(default["result_scope"],
                         "best-section-per-document")
        self.assertEqual(reranked["result_scope"], "section-rerank")
        self.assertEqual(default["results"][0]["score_kind"], "bm25")
        self.assertEqual(reranked["results"][0]["score_kind"],
                         "section-rerank")
        with self.assertRaises(section_search.SearchError):
            self.search("zebra", all_sections=True, section_rerank=True)

    def test_query_cache_returns_defensive_copy(self):
        self.build()
        first = self.search("zebra", limit=1)
        first["results"][0]["heading"] = "mutated"
        second = self.search("zebra", limit=1)
        self.assertNotEqual(second["results"][0]["heading"], "mutated")

    def test_query_cache_invalidates_after_book_and_index_change(self):
        self.build()
        first = self.search("zebra", limit=1)
        self.a.write_text(
            PAGE_A + "\n\n## Gamma section {#gamma-section}\n"
            "New gamma token for cache invalidation.\n", encoding="utf-8")
        self.build()
        second = self.search("zebra", limit=1)
        self.assertNotEqual(first["snapshot"], second["snapshot"])
        gamma = self.search("gamma", limit=1)
        self.assertEqual(gamma["results"][0]["section_id"], "gamma-section")

    def test_h3_match_maps_to_parent_h2_with_diagnostics(self):
        self.build()
        top = self.search("quasar", limit=1)["results"][0]
        self.assertEqual(top["section_key"], "tycho.page.alpha#caching")
        self.assertEqual(top["section_id"], "caching")
        self.assertEqual(top["heading"], "Caching")
        self.assertEqual(top["heading_level"], 2)
        self.assertEqual(top["citation"], "book/a.md#caching")
        self.assertEqual(top["match_source"], "h3-passage")
        self.assertEqual(top["matched_passage_id"], "stampede-guard")
        self.assertEqual(top["matched_passage_key"],
                         "tycho.page.alpha#caching~stampede-guard")
        self.assertEqual(top["matched_passage_heading"], "Stampede guard")
        self.assertGreater(top["matched_passage_score"], 0)
        self.assertLess(top["matched_passage_char_start"],
                        top["matched_passage_char_end"])
        self.assertIn("Quasar", top["matched_passage_excerpt"])
        self.assertNotIn("matched_passage_id", self.search("zebra")["results"][0])

    def test_h3_parent_read_keeps_parent_content_and_offsets(self):
        self.build()
        top = self.search("quasar", limit=1)["results"][0]
        read = self.read(top["section_key"], 0, 5000)
        self.assertEqual(read["section_id"], "caching")
        self.assertEqual(read["citation"], "book/a.md#caching")
        self.assertEqual(
            read["content"],
            PAGE_A[PAGE_A.index("## Caching"):PAGE_A.index("## Retry policy")])
        self.assertEqual(read["document_char_start"], top["char_start"])
        self.assertEqual(read["document_char_end"], top["char_end"])
        self.assertIn("### Stampede guard", read["content"])
        self.assertEqual(read["total_chars"],
                         top["char_end"] - top["char_start"])
        with self.assertRaises(section_search.SearchError) as caught:
            self.read(top["matched_passage_key"], 0, 50)
        self.assertEqual(caught.exception.status, "not-found")

    def test_h3_filters_and_all_sections_do_not_duplicate_parent(self):
        self.build()
        for filters in ({"kind": "page"}, {"topic": "caching"},
                        {"evidence_status": "source-linked"},
                        {"path_prefix": "book/a"}):
            self.assertEqual(self.search("quasar", **filters)["returned"], 1)
        self.assertEqual(self.search("quasar", kind="landing")["status"],
                         "no-results")
        self.assertEqual(self.search("quasar", topic="deployment")["status"],
                         "no-results")
        self.assertEqual(self.search("quasar", path_prefix="book/b")["status"],
                         "no-results")
        sections = self.search("quasar", all_sections=True)
        self.assertEqual(sections["returned"], 1)
        keys = [item["section_key"] for item in sections["results"]]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(sections["result_scope"], "all-sections")

    def test_tampered_h3_row_count_is_unavailable(self):
        self.build()
        path = self.root / "generated" / section_fts_index.INDEX_NAME
        with sqlite3.connect(path) as db:
            db.execute("DELETE FROM passage_fts WHERE rowid=1")
            db.commit()
        with self.assertRaises(section_search.SearchError) as caught:
            self.search("quasar")
        self.assertEqual(caught.exception.status, "not-available")

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

    def test_snapshot_scan_is_reused_for_unchanged_book(self):
        self.build()
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan) as scan:
            first = self.open_manifest()
            second = self.open_manifest()
            result_a = section_search.search(self.root, "zebra", abstain=False)
            result_b = section_search.search(self.root, "zebra", abstain=False)
        self.assertEqual(first, second)
        self.assertEqual(result_a, result_b)
        self.assertEqual(result_a["results"], result_b["results"])
        self.assertEqual(scan.call_count, 1)

    def test_cache_is_invalidated_by_book_change(self):
        self.build()
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan) as scan:
            self.open_manifest()
            self.assertEqual(scan.call_count, 1)
            self.a.write_text(
                self.a.read_text() + "\n## Later\nNew text.\n",
                encoding="utf-8")
            with self.assertRaises(section_search.SnapshotMismatch):
                self.open_manifest()
            self.assertEqual(scan.call_count, 2)

    def test_cached_scan_still_refuses_route_snapshot_mismatch(self):
        self.build()
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan) as scan:
            self.open_manifest()
            self.tamper_manifest(route_snapshot_sha256="0" * 64)
            with self.assertRaises(section_search.SnapshotMismatch) as caught:
                self.open_manifest()
            self.assertEqual(caught.exception.status, "snapshot-mismatch")
            self.assertEqual(scan.call_count, 1)

    def test_cached_scan_does_not_mask_missing_or_corrupt_index(self):
        self.build()
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            self.open_manifest()
            self.index_path().unlink()
            with self.assertRaises(section_search.SearchError) as caught:
                self.open_manifest()
            self.assertEqual(caught.exception.status, "not-available")
        self.build()
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            self.open_manifest()
        with sqlite3.connect(self.index_path()) as db:
            db.execute("DELETE FROM fts WHERE rowid=1")
            db.commit()
        with self.assertRaises(section_search.SearchError) as caught:
            self.open_manifest()
        self.assertEqual(caught.exception.status, "not-available")

    def test_cached_scan_does_not_mask_missing_manifest(self):
        self.build()
        with patch.object(route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            self.open_manifest()
        with sqlite3.connect(self.index_path()) as db:
            db.execute("DELETE FROM meta WHERE key='manifest'")
            db.commit()
        with self.assertRaises(section_search.SearchError) as caught:
            self.open_manifest()
        self.assertEqual(caught.exception.status, "not-available")

    def test_concurrent_validation_reuses_one_scan(self):
        self.build()
        calls = []
        calls_lock = threading.Lock()

        def slow_scan(root, allow_partial=False):
            with calls_lock:
                calls.append(1)
            time.sleep(0.05)
            return self.fake_scan(root, allow_partial)

        with patch.object(route_index, "canonical_scan",
                          side_effect=slow_scan):
            with ThreadPoolExecutor(max_workers=8) as pool:
                manifests = list(pool.map(
                    lambda _: self.open_manifest(), range(8)))
        self.assertEqual(len(calls), 1)
        self.assertTrue(all(item == manifests[0] for item in manifests))

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

    def test_read_includes_evidence_only_when_requested(self):
        self.build()
        key = "tycho.page.alpha#retry-budget"
        with patch.object(section_evidence, "build_store",
                          return_value={"fake": True}), \
             patch.object(section_evidence, "resolve_document",
                          return_value={"status": "ok",
                                        "document": {"document_id": "x"}}):
            result = self.read(key, 0, 20, include_evidence=True)
        self.assertEqual(result["evidence"]["status"], "ok")
        plain = self.read(key, 0, 20)
        self.assertNotIn("evidence", plain)

    def test_evidence_action_binds_search_snapshot(self):
        manifest = {"snapshot_id": "s" * 64,
                    "route_snapshot_sha256": "r" * 64}
        with patch.object(section_search, "open_snapshot",
                          return_value=(MagicMock(), manifest)), \
             patch.object(section_evidence, "build_store",
                          return_value={"fake": True}), \
             patch.object(section_evidence, "resolve_claim",
                          return_value={"status": "ok"}):
            result = section_search.evidence(self.root, claim_id="claim.x")
        self.assertEqual(result["search_snapshot"], "s" * 64)
        self.assertEqual(result["search_route_snapshot"], "r" * 64)

    def test_evidence_requires_one_identifier(self):
        with self.assertRaises(section_search.SearchError):
            section_search.evidence(self.root)
        with self.assertRaises(section_search.SearchError):
            section_search.evidence(self.root, document_id="a", claim_id="b")


    def test_bm25_weights_are_bounded(self):
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("TYCHO_BM25_WEIGHTS", None)
            self.assertEqual(section_search.bm25_weights(), (5.0, 2.0, 0.25))
        for raw in ("4,3", "4,0,1", "x,2,1"):
            with patch.dict(os.environ, {"TYCHO_BM25_WEIGHTS": raw}):
                with self.assertRaises(section_search.SearchError):
                    section_search.bm25_weights()


    def test_abstention_scope_and_bypass(self):
        self.build()
        query = "How do I configure a specific vendor cache policy?"
        blocked = self.search(query, abstain=True)
        self.assertEqual(blocked["status"], "no-confident-answer")
        self.assertEqual(blocked["returned"], 0)
        self.assertEqual(blocked["results"], [])
        self.assertTrue(blocked["answerability"]["no_confident_answer"])
        self.assertEqual(blocked["answerability"]["basis"],
                         "evidence-score-threshold")
        raw = self.search(query, abstain=False)
        self.assertIn(raw["status"], {"ok", "no-results"})
        self.assertTrue(raw["answerability"]["no_confident_answer"])


if __name__ == "__main__":
    unittest.main()

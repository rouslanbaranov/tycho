"""Offline tests for corpus qrels validation and metric computation.

No search layer, network, book rewriting or external corpus is required.
"""
import json
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import evaluate_corpus_qrels as evaluation  # noqa: E402
import validate_corpus_qrels as validator  # noqa: E402

SCHEMA = validator.load(ROOT / "schemas/corpus-qrels.v1.schema.json")
SNAPSHOT = "a" * 64
DOCS = [
    {"id": "tycho.page.aaaaaa", "path": "book/a.md",
     "parent_id": "tycho.chapter.cccccc", "kind": "page"},
    {"id": "tycho.page.bbbbbb", "path": "book/b.md",
     "parent_id": "tycho.chapter.cccccc", "kind": "page"},
    {"id": "tycho.page.dddddd", "path": "book/c.md",
     "parent_id": "tycho.chapter.eeeeee", "kind": "page"},
]
ROUTE = {"snapshot_sha256": SNAPSHOT, "documents": DOCS}


def answer(document, path, grade=2, section_id=None):
    return {
        "document_id": document,
        "path": path,
        "section_id": section_id,
        "grade": grade,
        "rationale": "Directly explains the requested mechanism.",
    }


def judge(qid, split, category, accepted):
    return {
        "id": qid,
        "split": split,
        "category": category,
        "question": "A synthetic question for metric testing.",
        "accepted": accepted,
        "notes": "",
    }


def make_qrels(items, status="bootstrap-author-labelled", snapshot=SNAPSHOT):
    return {
        "schema_version": 1,
        "status": status,
        "created": "2026-10-22",
        "snapshot": {
            "route_index_snapshot": snapshot,
            "document_count": len(DOCS),
        },
        "target_item_count": 50,
        "provenance": {
            "labels": "author-labelled",
            "method": "Synthetic fixture for metric and validation tests.",
            "independent_review": False,
            "review_note": "No independent review is claimed.",
        },
        "items": items,
    }


def base_items():
    return [
        judge("Q001", "dev", "fact", [answer("tycho.page.aaaaaa", "book/a.md")]),
        judge("Q002", "heldout", "tradeoff", [answer("tycho.page.dddddd", "book/c.md", 1)]),
        judge("Q003", "heldout", "unanswerable", []),
    ]


class QrelsValidationTests(unittest.TestCase):
    def test_valid_fixture(self):
        result = validator.validate(make_qrels(base_items()), ROUTE, SCHEMA)
        self.assertEqual(result["items"], 3)
        self.assertEqual(result["dev"], 1)
        self.assertEqual(result["heldout"], 2)
        self.assertEqual(result["accepted_answers"], 2)

    def test_stale_snapshot_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "snapshot"):
            validator.validate(make_qrels(base_items(), snapshot="b" * 64),
                               ROUTE, SCHEMA)
        result = validator.validate(make_qrels(base_items(), snapshot="b" * 64),
                                    ROUTE, SCHEMA, require_snapshot=False)
        self.assertEqual(result["status"], "ok")

    def test_id_and_path_must_agree(self):
        items = base_items()
        items[0]["accepted"][0]["path"] = "book/b.md"
        with self.assertRaisesRegex(ValueError, "disagree|documented page"):
            validator.validate(make_qrels(items), ROUTE, SCHEMA)

    def test_duplicate_item_id_is_rejected(self):
        items = base_items()
        items[1]["id"] = "Q001"
        with self.assertRaisesRegex(ValueError, "duplicate item id"):
            validator.validate(make_qrels(items), ROUTE, SCHEMA)

    def test_unanswerable_must_not_have_accepted_pages(self):
        items = base_items()
        items[2]["accepted"] = [answer("tycho.page.aaaaaa", "book/a.md")]
        with self.assertRaisesRegex(ValueError, "maxItems|schema violation"):
            validator.validate(make_qrels(items), ROUTE, SCHEMA)

    def test_answerable_must_have_accepted_pages(self):
        items = base_items()
        items[0]["accepted"] = []
        with self.assertRaisesRegex(ValueError, "minItems|schema violation"):
            validator.validate(make_qrels(items), ROUTE, SCHEMA)

    def test_non_bootstrap_requires_target_count(self):
        with self.assertRaisesRegex(ValueError, "target_item_count"):
            validator.validate(make_qrels(base_items(), status="author-labelled"),
                               ROUTE, SCHEMA)

    def test_committed_bootstrap_dataset_structure(self):
        qrels = validator.load(ROOT / "evaluation/corpus-qrels.v1.json")
        route = validator.load(ROOT / "generated/route-index.v1.json")
        result = validator.validate(qrels, route, SCHEMA, require_snapshot=False)
        self.assertEqual(result["items"], 100)
        self.assertEqual(result["dev"], 50)
        self.assertEqual(result["heldout"], 50)
        self.assertTrue(result["bootstrap"])


class MetricTests(unittest.TestCase):
    def setUp(self):
        self.parent_of = {doc["path"]: doc["parent_id"] for doc in DOCS}

    def fake_search(self, question):
        responses = {
            "A synthetic question for metric testing.": {
                "status": "ok",
                "snapshot": "s" * 64,
                "results": [
                    {"path": "book/b.md", "section_id": "overview"},
                    {"path": "book/a.md", "section_id": "overview"},
                ],
            },
        }
        return responses[question]

    def test_rank_scopes_and_metrics(self):
        items = base_items()[:1]
        result = evaluation.evaluate(items, self.fake_search, self.parent_of)
        overall = result["overall"]
        self.assertEqual(overall["answerable"], 1)
        self.assertEqual(overall["page"]["hit@1"], 0.0)
        self.assertEqual(overall["page"]["hit@3"], 1.0)
        self.assertEqual(overall["page"]["mrr"], 0.5)
        self.assertEqual(overall["chapter"]["hit@1"], 1.0)
        self.assertEqual(overall["section"]["hit@3"], 1.0)
        self.assertAlmostEqual(overall["ndcg@10"], 1 / math.log2(3), places=6)

    def test_unanswerable_and_snapshot(self):
        items = [base_items()[2]]
        result = evaluation.evaluate(items, lambda q: {
            "status": "no-results", "snapshot": "s" * 64, "results": []},
            self.parent_of)
        self.assertEqual(result["overall"]["unanswerable_no_result_rate"], 1.0)
        self.assertEqual(result["search_snapshots"], ["s" * 64])

    def test_page_and_chapter_ranks(self):
        items = [judge("Q010", "dev", "fact",
                       [answer("tycho.page.aaaaaa", "book/a.md")])]
        result = evaluation.evaluate(
            items,
            lambda q: {"status": "ok", "snapshot": "s" * 64,
                       "results": [{"path": "book/b.md", "section_id": "x"}]},
            self.parent_of)
        row = result["items"][0]
        self.assertIsNone(row["page_rank"])
        self.assertEqual(row["chapter_rank"], 1)
        self.assertEqual(result["overall"]["page"]["mrr"], 0.0)

    def test_section_specific_acceptance(self):
        items = [judge("Q011", "dev", "fact",
                       [answer("tycho.page.aaaaaa", "book/a.md", 2, "retry")])]
        result = evaluation.evaluate(
            items,
            lambda q: {"status": "ok", "snapshot": "s" * 64,
                       "results": [{"path": "book/a.md", "section_id": "overview"},
                                   {"path": "book/a.md", "section_id": "retry"}]},
            self.parent_of)
        row = result["items"][0]
        self.assertEqual(row["page_rank"], 1)
        self.assertEqual(row["section_rank"], 2)


if __name__ == "__main__":
    unittest.main()

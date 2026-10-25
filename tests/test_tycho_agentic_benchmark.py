"""Tests for the frozen agentic benchmark and its metric helpers."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_agentic_benchmark  # noqa: E402
import evaluate_agentic  # noqa: E402

DATASET = ROOT / "evaluation/agentic-qrels.v1.json"
SOURCE = ROOT / "evaluation/corpus-qrels.v2.json"


class AgenticBenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dataset = json.loads(DATASET.read_text(encoding="utf-8"))
        cls.source = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_dataset_shape_and_provenance(self):
        self.assertEqual(self.dataset["dataset"], "agentic-retrieval-v1")
        self.assertEqual(self.dataset["selection"]["total"], 40)
        self.assertEqual(len(self.dataset["items"]), 40)
        expected = {
            "fact": 10,
            "failure": 5,
            "tradeoff": 5,
            "synthesis": 5,
            "change_impact": 4,
            "contradiction": 3,
            "unanswerable": 8,
        }
        counts = {}
        for item in self.dataset["items"]:
            counts[item["category"]] = counts.get(item["category"], 0) + 1
        self.assertEqual(counts, expected)
        self.assertEqual(len({item["id"] for item in self.dataset["items"]}), 40)
        digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        self.assertEqual(self.dataset["source"]["sha256"], digest)

    def test_accepted_paths_and_answerability(self):
        for item in self.dataset["items"]:
            self.assertTrue(item["question"])
            if item["category"] == "unanswerable":
                self.assertEqual(item["accepted"], [])
                continue
            self.assertTrue(item["accepted"])
            for entry in item["accepted"]:
                self.assertTrue((ROOT / entry["path"]).is_file(), entry["path"])

    def test_selection_is_deterministic(self):
        first = build_agentic_benchmark.select(self.source)
        second = build_agentic_benchmark.select(self.source)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 40)

    def test_ndcg_and_rank_helpers(self):
        self.assertAlmostEqual(
            evaluate_agentic.ndcg_at(["a", "b"], ["b"]),
            1 / 1.584962500721156,
            places=6,
        )
        self.assertEqual(
            evaluate_agentic.first_relevant_rank(["x", "b", "c"], ["b"]), 2)
        self.assertIsNone(evaluate_agentic.ndcg_at(["a"], []))

    def test_summary_separates_retrieval_from_policy(self):
        records = [
            {
                "expected_abstention": False,
                "doc_hit": True,
                "mrr": 1.0,
                "top1": True,
                "ndcg@10": 1.0,
                "path_precision": 1.0,
                "default_would_abstain": False,
                "policy_confident": True,
                "tool_calls": 1,
                "context_bytes": 100,
                "latency_ms": 10,
                "abstained": False,
                "confident_wrong": False,
            },
            {
                "expected_abstention": True,
                "doc_hit": False,
                "mrr": 0.0,
                "top1": False,
                "ndcg@10": None,
                "path_precision": None,
                "default_would_abstain": True,
                "policy_confident": False,
                "tool_calls": 1,
                "context_bytes": 50,
                "latency_ms": 20,
                "abstained": True,
                "confident_wrong": False,
            },
        ]
        summary = evaluate_agentic.summarize(records)
        self.assertEqual(summary["answerable"]["recall@10"], 1.0)
        self.assertEqual(summary["answerable"]["policy_confident_rate"], 1.0)
        self.assertEqual(summary["unanswerable"]["abstention_rate"], 1.0)
        self.assertEqual(summary["overall"]["count"], 2)


if __name__ == "__main__":
    unittest.main()

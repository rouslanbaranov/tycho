"""Benchmark harness validation and aggregation."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import agent_benchmark as bench  # noqa: E402


class BenchmarkTests(unittest.TestCase):
    def test_validate_requires_one_hundred(self):
        errors = bench.validate({"questions": []})
        self.assertTrue(any("100" in e for e in errors))

    def test_v2_corpus_validates_and_splits(self):
        corpus = bench.load_json(ROOT / "evaluation/agent-benchmark/corpus-v2.json")
        self.assertEqual(bench.validate(corpus), [])
        self.assertEqual(sum(q["split"] == "dev" for q in corpus["questions"]), 50)
        self.assertEqual(sum(q["split"] == "holdout" for q in corpus["questions"]), 50)

    def test_dual_judge_consensus_is_strict(self):
        corpus = {"questions": [{"id": "Q1", "layer_expected": "book"}]}
        rows = [
            {"id": "Q1", "ok": True, "stdout": "{}",
             "judge": {"pass": True}, "judge2": {"pass": False},
             "judge_agreement": False, "consensus": False},
            {"id": "Q2", "ok": True, "stdout": "{}",
             "judge": {"pass": True}, "judge2": {"pass": True},
             "judge_agreement": True, "consensus": True},
        ]
        summary = bench.aggregate(rows, corpus)
        self.assertEqual(summary["pass_rate"], 0.5)
        self.assertEqual(summary["judge_agreement"], 0.5)

    def test_aggregate_detects_token_outlier(self):
        corpus = {"questions": [
            {"id": "Q%d" % i, "layer_expected": "book"} for i in range(1, 6)
        ]}
        values = [10, 10, 10, 10, 100000]
        rows = [{"id": "Q%d" % (i + 1), "ok": True,
                 "stdout": '{"token_usage":{"total":%d}}' % values[i],
                 "judge": {"pass": i < 2}} for i in range(5)]
        summary = bench.aggregate(rows, corpus)
        self.assertEqual(summary["pass_rate"], 0.4)
        self.assertEqual(summary["token_anomalies"][0]["id"], "Q5")


if __name__ == "__main__":
    unittest.main()

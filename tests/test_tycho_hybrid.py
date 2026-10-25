"""Tests for the bounded hashed-vector hybrid probe."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import evaluate_hybrid  # noqa: E402


class HybridProbeTests(unittest.TestCase):
    def test_vector_is_normalised_and_cosine_is_bounded(self):
        left = evaluate_hybrid.vector("cache retry")
        right = evaluate_hybrid.vector("cache retry")
        self.assertAlmostEqual(sum(value * value for value in left), 1.0)
        self.assertAlmostEqual(evaluate_hybrid.cosine(left, right), 1.0)

    def test_alpha_zero_preserves_bm25_order(self):
        items = [
            {"section_key": "a", "path": "a", "score": 2,
             "_bm25_norm": 1.0, "title": "a", "heading": "a", "excerpt": "a"},
            {"section_key": "b", "path": "b", "score": 1,
             "_bm25_norm": 0.0, "title": "b", "heading": "b", "excerpt": "b"},
        ]
        self.assertEqual(
            evaluate_hybrid.rank(items, "query", [], 0.0), ["a", "b"])

    def test_metrics_use_accepted_paths(self):
        values = evaluate_hybrid.metrics(["x", "y"], ["y"])
        self.assertEqual(values["recall@10"], 1.0)
        self.assertAlmostEqual(values["mrr"], 0.5)
        self.assertGreater(values["ndcg@10"], 0)


if __name__ == "__main__":
    unittest.main()

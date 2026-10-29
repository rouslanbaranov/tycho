"""Tests for the optional V12-gated top-1 reranker."""
import sys
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import top1_rerank  # noqa: E402

class RerankTests(unittest.TestCase):
    def test_skip_v12_and_long_queries(self):
        self.assertEqual(top1_rerank.skip_reason(
            "short query", [{"volume":"v12"}]), "skipped-v12")
        long_query=" ".join("word%d" % i for i in range(20))
        self.assertEqual(top1_rerank.skip_reason(
            long_query,[{"volume":"book"}]), "skipped-long-query")
        self.assertIsNone(top1_rerank.skip_reason(
            "short query",[{"volume":"book"}]))

    def test_features_shape(self):
        model=top1_rerank.load_model()
        result={"heading":"Cache","content":"TTL cache","score":1,
                "section_id":"cache","match_source":"nested"}
        vector=top1_rerank.features("cache ttl",result,1)
        self.assertEqual(len(vector),len(model["feature_order"]))

if __name__=="__main__":
    unittest.main()

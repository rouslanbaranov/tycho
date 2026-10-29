"""Tests for hybrid page-level RRF."""
import sys
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import hybrid_search  # noqa: E402

class HybridTests(unittest.TestCase):
    def test_page_rrf_preserves_bm25_and_adds_semantic(self):
        bm=[{"path":"a","section_id":"1","section_key":"a#1"}]
        sem=[{"path":"b","section_id":"2","section_key":"b#2"},
             {"path":"a","section_id":"9","section_key":"a#9"}]
        out=hybrid_search.page_rrf(bm,sem,weight=.1,limit=2)
        self.assertEqual([x["path"] for x in out],["a","b"])
        self.assertEqual(out[0]["bm25_rank"],1)
        self.assertEqual(out[0]["semantic_rank"],2)
        self.assertEqual(out[1]["bm25_rank"],None)
        self.assertTrue(out[1]["citation"].endswith("#2"))

if __name__=="__main__":
    unittest.main()

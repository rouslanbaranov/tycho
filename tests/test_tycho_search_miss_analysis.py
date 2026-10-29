"""Tests for BM25 miss classification."""
import sys
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import search_miss_analysis  # noqa: E402

class MissTests(unittest.TestCase):
    def test_classification_order(self):
        self.assertEqual(search_miss_analysis.classify(1,1),"hit")
        self.assertEqual(search_miss_analysis.classify(None,3),
                         "section-granularity")
        self.assertEqual(search_miss_analysis.classify(12,12),
                         "exact-rank-6-20")
        self.assertEqual(search_miss_analysis.classify(None,15),
                         "page-rank-6-20")
        self.assertEqual(search_miss_analysis.classify(None,None),
                         "not-top-20")

if __name__=="__main__":
    unittest.main()

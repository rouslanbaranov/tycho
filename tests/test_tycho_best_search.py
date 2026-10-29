"""Tests for the optional composed best-search mode."""
import sys
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import best_search  # noqa: E402

class BestSearchTests(unittest.TestCase):
    def test_v12_gate(self):
        self.assertTrue(best_search.is_v12("V12 question", []))
        self.assertTrue(best_search.is_v12("cache", [{"volume":"v12"}]))
        self.assertFalse(best_search.is_v12("cache", [{"volume":"book"}]))

if __name__=="__main__":
    unittest.main()

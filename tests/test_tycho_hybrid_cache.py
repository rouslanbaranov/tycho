"""Tests for hybrid semantic cache bounds."""
import sys
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import hybrid_search  # noqa: E402

class HybridCacheTests(unittest.TestCase):
    def test_cache_is_bounded_and_clearable(self):
        hybrid_search.clear_semantic_cache()
        for i in range(10):
            hybrid_search._remember(hybrid_search._MODEL_CACHE, i, i)
        self.assertLessEqual(len(hybrid_search._MODEL_CACHE),
                             hybrid_search._CACHE_MAX)
        hybrid_search.clear_semantic_cache()
        self.assertEqual(hybrid_search._MODEL_CACHE, {})

if __name__=="__main__":
    unittest.main()

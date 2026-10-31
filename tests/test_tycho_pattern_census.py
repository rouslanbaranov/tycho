"""Checks for the canonical page census, not page quality."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from pattern_census import build, load, CENSUS


class PatternCensusTests(unittest.TestCase):
    def test_census_counts(self):
        result = build(ROOT)
        self.assertGreaterEqual(result["document_count"], 423)
        self.assertEqual(result["counts"]["by_kind"]["volume"], 11)
        self.assertEqual(result["counts"]["by_kind"]["chapter"], 82)
        self.assertEqual(result["counts"]["by_volume"]["v11-pattern-atlas"], 80)

    def test_census_is_deterministic(self):
        self.assertEqual(build(ROOT), build(ROOT))

    def test_checked_in_census_matches(self):
        self.assertEqual(load(ROOT / CENSUS), build(ROOT))


if __name__ == "__main__":
    unittest.main()

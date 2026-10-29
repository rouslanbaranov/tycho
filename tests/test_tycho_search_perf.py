"""Pure percentile checks for the operational performance helper."""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import search_perf  # noqa: E402


class SearchPerfTests(unittest.TestCase):
    def test_percentile_bounds(self):
        values = [1.0, 2.0, 3.0, 4.0]
        self.assertEqual(search_perf.percentile(values, 0.5), 2.0)
        self.assertEqual(search_perf.percentile(values, 0.95), 4.0)
        self.assertIsNone(search_perf.percentile([], 0.5))


if __name__ == "__main__":
    unittest.main()

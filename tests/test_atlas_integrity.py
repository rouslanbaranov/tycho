import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_atlas_integrity import check


class AtlasIntegrityTests(unittest.TestCase):
    def test_cards_owners_and_promotions_are_consistent(self):
        result = check(ROOT)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["cards"], result["registry"])
        self.assertEqual(result["cardless"], 0)


if __name__ == "__main__":
    unittest.main()

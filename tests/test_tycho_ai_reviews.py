import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_ai_reviews import validate


class AIReviewIndexTests(unittest.TestCase):
    def test_saved_reports_match_index(self):
        self.assertEqual(validate(ROOT), {"reports": 95})


if __name__ == "__main__":
    unittest.main()

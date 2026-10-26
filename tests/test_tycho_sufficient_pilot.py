import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_sufficient_pilot import validate


class SufficientPilotTests(unittest.TestCase):
    def test_six_pilot_inputs_are_current(self):
        self.assertEqual(validate(ROOT), {"entries": 6})


if __name__ == "__main__":
    unittest.main()

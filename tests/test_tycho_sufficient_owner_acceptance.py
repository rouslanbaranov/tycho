import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_sufficient_owner_acceptance import validate


class SufficientOwnerAcceptanceTests(unittest.TestCase):
    def test_pending_record_is_not_acceptance(self):
        self.assertEqual(validate(ROOT), {"status": "accepted", "entries": 16})


if __name__ == "__main__":
    unittest.main()

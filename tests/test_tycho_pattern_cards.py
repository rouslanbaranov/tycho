import copy
import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_cards import check_backlink, check_card_text, load, validate_data


class PatternCardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.batches = load(ROOT / "edition/patterns/card-batches.v1.json")

    def check_error(self, data, message):
        with self.assertRaises(ValueError) as raised:
            validate_data(data, ROOT)
        self.assertIn(message, str(raised.exception))

    def test_complete_card_batch(self):
        result = validate_data(self.batches, ROOT)
        self.assertEqual(result["entries"], 24)

    def test_unknown_pattern_is_rejected(self):
        data = copy.deepcopy(self.batches)
        data["batches"][0]["entries"][0]["pattern_id"] = "tycho.pattern.not-real"
        self.check_error(data, "card-pattern-unknown")

    def test_owner_anchor_mismatch_is_rejected(self):
        data = copy.deepcopy(self.batches)
        data["batches"][0]["entries"][0]["owner_anchor"] = "not-a-real-anchor"
        self.check_error(data, "card-owner-anchor")

    def test_registry_owner_state_is_rejected(self):
        data = copy.deepcopy(self.batches)
        # The validator reads the registry from disk; mutate the batch to a pattern
        # whose registry owner does not match this owner path.
        data["batches"][0]["entries"][0]["owner_path"] = (
            "book/volumes/v02-application-boundaries-and-contracts/c02-domain-boundaries-"
            "data-ownership-and-contracts/domain-authority.md"
        )
        self.check_error(data, "card-owner-anchor")

    def test_ledger_record_is_rejected(self):
        data = copy.deepcopy(self.batches)
        data["batches"][0]["entries"][0]["ledger_record"] = "read.not-real.2026-10-21"
        self.check_error(data, "card-ledger-missing")

    def test_missing_backlink_is_rejected(self):
        with self.assertRaises(ValueError) as raised:
            check_backlink("no atlas link here",
                           "book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md",
                           "modular-monolith")
        self.assertIn("card-backlink-missing", str(raised.exception))

    def test_missing_card_marker_is_rejected(self):
        with self.assertRaises(ValueError) as raised:
            check_card_text("**Decision question.** only", "modular-monolith")
        self.assertIn("card-marker-missing", str(raised.exception))


if __name__ == "__main__":
    unittest.main()

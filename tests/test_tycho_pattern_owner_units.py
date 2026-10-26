import copy
import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_owner_units import expected_coverage, load, validate_data


class PatternOwnerUnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load(ROOT / "edition/patterns/owner-units.v1.json")

    def copy(self):
        return copy.deepcopy(self.data)

    def check_error(self, data, message):
        with self.assertRaises(ValueError) as raised:
            validate_data(data, ROOT)
        self.assertIn(message, str(raised.exception))

    def test_every_card_has_one_owner_unit(self):
        result = validate_data(self.data, ROOT)
        self.assertEqual(result["entries"], 145)
        self.assertEqual(result["owner_pages"], 69)
        self.assertEqual(result["shared_pages"], 33)
        self.assertEqual(result["bounded"] + result["partial"], 145)
        self.assertGreater(result["units"], 30)

    def test_missing_entry_is_rejected(self):
        data = self.copy()
        data["entries"].pop()
        self.check_error(data, "owner-units-schema")

    def test_duplicate_pattern_is_rejected(self):
        data = self.copy()
        data["entries"][1]["pattern_id"] = data["entries"][0]["pattern_id"]
        self.check_error(data, "owner-units-duplicate-pattern")

    def test_unknown_anchor_is_rejected(self):
        data = self.copy()
        data["entries"][0]["owner"]["anchor"] = "definitely-not-a-section"
        self.check_error(data, "owner-units-owner-anchor")

    def test_wrong_owner_path_is_rejected(self):
        data = self.copy()
        data["entries"][0]["owner"]["path"] = "book/README.md"
        self.check_error(data, "owner-units-owner-path")

    def test_non_verbatim_quote_is_rejected(self):
        data = self.copy()
        data["entries"][0]["technical_evidence"]["mechanism"]["quote"] = (
            "This sentence was invented and does not appear anywhere on the page.")
        self.check_error(data, "owner-units-quote-not-verbatim")

    def test_name_only_mechanism_is_rejected(self):
        data = self.copy()
        data["entries"][0]["technical_evidence"]["mechanism"]["state"] = "absent"
        data["entries"][0]["technical_evidence"]["mechanism"]["quote"] = ""
        data["entries"][0]["technical_evidence"]["mechanism"]["reason"] = "test"
        self.check_error(data, "owner-units-name-only")

    def test_supported_reason_is_required(self):
        data = self.copy()
        item = next(entry for entry in data["entries"]
                    if entry["technical_evidence"]["mechanism"]["state"] == "supported")
        item["technical_evidence"]["mechanism"]["reason"] = ""
        self.check_error(data, "owner-units-reason-missing-supported")

    def test_invariant_without_evidence_is_rejected(self):
        data = self.copy()
        item = next(entry for entry in data["entries"]
                    if entry["technical_coverage"] == "partial-bounded")
        item["technical_evidence"]["invariant"] = {
            "state": "absent", "quote": "", "reason": "test"}
        self.check_error(data, "owner-units-technical-derivation")

    def test_alternative_mismatch_is_rejected(self):
        data = self.copy()
        data["entries"][0]["decision_evidence"]["competing_alternative"] = "test"
        self.check_error(data, "owner-units-alternative")

    def test_card_components_are_required(self):
        data = self.copy()
        data["entries"][0]["decision_evidence"]["card_components"] = 9
        self.check_error(data, "owner-units-schema")

    def test_source_record_mismatch_is_rejected(self):
        data = self.copy()
        data["entries"][0]["source_support"]["ledger_record"] = "read.not-real.2026-10-21"
        self.check_error(data, "owner-units-ledger-record")

    def test_shared_page_decision_is_rejected(self):
        data = self.copy()
        data["shared_pages"][0]["decision"] = "merge"
        self.check_error(data, "owner-units-schema")

    def test_shared_page_pattern_list_is_rejected(self):
        data = self.copy()
        data["shared_pages"][0]["pattern_ids"].pop()
        self.check_error(data, "owner-units-shared-patterns")

    def test_sufficient_needs_a_promotion(self):
        evidence = self.data["entries"][0]["technical_evidence"]
        self.assertEqual(expected_coverage(evidence, "test"), "partial-bounded")
        self.assertEqual(
            expected_coverage(evidence, "test", {"technical": "pass"}),
            "sufficient")

    def test_sufficient_claim_is_rejected(self):
        data = self.copy()
        data["entries"][0]["technical_coverage"] = "sufficient"
        self.check_error(data, "owner-units-technical-derivation")

    def test_reviewed_claim_is_rejected(self):
        data = self.copy()
        data["entries"][0]["review_state"] = "independent-reviewed"
        self.check_error(data, "owner-units-reviewed-without-record")

    def test_summary_mismatch_is_rejected(self):
        data = self.copy()
        data["summary"]["owner_units"] = 40
        self.check_error(data, "owner-units-summary-mismatch")

    def test_shared_page_count_is_rejected(self):
        data = self.copy()
        data["shared_pages"].pop()
        self.check_error(data, "owner-units-schema")

    def test_split_deferrals_are_empty(self):
        self.assertEqual(self.data["split_deferrals"], [])
        self.assertEqual(self.data["summary"]["split_deferred"], 0)


if __name__ == "__main__":
    unittest.main()

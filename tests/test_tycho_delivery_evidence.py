import copy
import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_delivery_evidence import load, validate_data


class DeliveryEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load(ROOT / "edition/patterns/delivery-evidence.v1.json")

    def check_error(self, data, message):
        with self.assertRaises(ValueError) as raised:
            validate_data(data, ROOT)
        self.assertIn(message, str(raised.exception))

    def test_complete_evidence(self):
        result = validate_data(self.data, ROOT)
        self.assertEqual(result["entries"], 145)
        self.assertEqual(result["cards"], 145)

    def test_sufficient_claim_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["summary"]["sufficient_technical"] = 1
        self.check_error(data, "delivery-schema")

    def test_independent_editorial_review_claim_is_rejected(self):
        data = copy.deepcopy(self.data)
        item = next(x for x in data["dod"] if x["id"] == "independent-editorial-review")
        item["status"] = "met"
        self.check_error(data, "delivery-independent-review-claim")

    def test_owner_confirmed_review_is_required(self):
        data = copy.deepcopy(self.data)
        item = next(x for x in data["dod"] if x["id"] == "owner-confirmed-human-review")
        item["status"] = "not-met"
        self.check_error(data, "delivery-owner-confirmed-review-missing")

    def test_human_review_count_mismatch_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["summary"]["human_reviews"] = 0
        self.check_error(data, "delivery-human-review-count")

    def test_owner_acceptance_claim_is_rejected(self):
        data = copy.deepcopy(self.data)
        item = next(x for x in data["dod"] if x["id"] == "owner-acceptance")
        item["status"] = "met"
        self.check_error(data, "delivery-owner-acceptance-claim")

    def test_reviewed_status_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["status"] = "reviewed"
        self.check_error(data, "delivery-reviewed-claim")

    def test_route_count_mismatch_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["summary"]["routes"] += 1
        self.check_error(data, "delivery-route-count")

    def test_source_commit_must_be_an_ancestor(self):
        data = copy.deepcopy(self.data)
        data["source_commit"] = "0" * 40
        self.check_error(data, "delivery-source-commit-not-ancestor")


if __name__ == "__main__":
    unittest.main()

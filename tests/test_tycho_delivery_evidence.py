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
        self.assertEqual(result["cards"], 144)

    def test_sufficient_claim_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["summary"]["sufficient_technical"] = 1
        self.check_error(data, "delivery-schema")

    def test_independent_review_claim_is_rejected(self):
        data = copy.deepcopy(self.data)
        item = next(x for x in data["dod"] if x["id"] == "independent-editorial-review")
        item["status"] = "met"
        self.check_error(data, "delivery-independent-review-claim")

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


if __name__ == "__main__":
    unittest.main()

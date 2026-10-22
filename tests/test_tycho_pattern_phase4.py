import copy
import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_phase4 import load, validate_data


class Phase4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load(ROOT / "edition/patterns/phase4.v1.json")

    def check_error(self, data, message):
        with self.assertRaises(ValueError) as raised:
            validate_data(data, ROOT)
        self.assertIn(message, str(raised.exception))

    def test_complete_artifact(self):
        result = validate_data(self.data, ROOT)
        self.assertEqual(result["pages"], 421)
        self.assertEqual(result["entries"], 145)
        self.assertEqual(result["cards"], 145)

    def test_page_count_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["page_dispositions"].pop()
        self.check_error(data, "phase4-schema")

    def test_missing_dimension_is_rejected(self):
        data = copy.deepcopy(self.data)
        del data["entry_audit"][0]["dimensions"]["identity"]
        self.check_error(data, "phase4-schema")

    def test_unknown_route_endpoint_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["routes"][0]["to"] = "tycho.pattern.not-real"
        self.check_error(data, "phase4-route-endpoint")

    def test_duplicate_question_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["retrieval_questions"][1]["pattern_id"] = data["retrieval_questions"][0]["pattern_id"]
        self.check_error(data, "phase4-question-duplicate")

    def test_summary_mismatch_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["summary"]["routes"] = 999
        self.check_error(data, "phase4-summary-routes")

    def test_non_route_target_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["related_dispositions"][0]["target"] = "tycho.pattern.retry-with-exponential-backoff"
        self.check_error(data, "phase4-related-non-route-target")

    def test_non_route_count_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["summary"]["non_routes"] = 0
        self.check_error(data, "phase4-non-route-count")

    def test_unresolved_claim_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["summary"]["unresolved_related"] = 40
        self.check_error(data, "phase4-schema")


if __name__ == "__main__":
    unittest.main()

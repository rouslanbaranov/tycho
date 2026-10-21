import copy
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_semantic_audit import load, validate_data


class PatternSemanticAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load(ROOT / "edition/patterns/semantic-audit.v1.json")

    def copy(self):
        return copy.deepcopy(self.data)

    def check_error(self, data, message):
        with self.assertRaises(ValueError) as raised:
            validate_data(data, ROOT)
        self.assertIn(message, str(raised.exception))

    def test_complete_artifact(self):
        result = validate_data(self.data, ROOT)
        self.assertEqual(result["pages"], 419)
        self.assertGreaterEqual(result["open_gates"], 3)

    def test_missing_page_is_rejected(self):
        data = self.copy()
        data["pages"].pop()
        self.check_error(data, "semantic-audit-schema")

    def test_duplicate_page_is_rejected(self):
        data = self.copy()
        data["pages"][1]["path"] = data["pages"][0]["path"]
        self.check_error(data, "semantic-audit-duplicate-path")

    def test_stale_page_sha_is_rejected(self):
        data = self.copy()
        data["pages"][0]["sha256"] = "0" * 64
        self.check_error(data, "semantic-audit-sha")

    def test_unknown_finding_anchor_is_rejected(self):
        data = self.copy()
        page = next(item for item in data["pages"]
                    if item["review"]["findings"])
        page["review"]["findings"][0]["anchor"] = "definitely-not-a-section"
        self.check_error(data, "semantic-audit-finding-anchor")

    def test_sound_page_cannot_have_findings(self):
        data = self.copy()
        page = next(item for item in data["pages"]
                    if item["review"]["disposition"] == "sound")
        page["review"]["findings"].append({
            "severity": "low",
            "kind": "shallow",
            "summary": "A bounded finding that contradicts the sound disposition.",
            "anchor": "page",
            "remediation": "Clarify the page.",
            "gate": None,
        })
        self.check_error(data, "semantic-audit-sound-with-findings")

    def test_finding_needs_resolution(self):
        data = self.copy()
        page = next(item for item in data["pages"]
                    if item["review"]["disposition"] == "sound-with-findings"
                    and item["review"]["findings"])
        page["review"]["findings"][0]["remediation"] = None
        page["review"]["findings"][0]["gate"] = None
        self.check_error(data, "semantic-audit-finding-resolution-missing")

    def test_independent_reviewer_is_rejected(self):
        data = self.copy()
        data["pages"][0]["review"]["reviewer_role"] = "independent-reviewer"
        self.check_error(data, "semantic-audit-schema")

    def test_summary_mismatch_is_rejected(self):
        data = self.copy()
        data["summary"]["pages_with_findings"] += 1
        self.check_error(data, "semantic-audit-summary-mismatch")

    def test_owner_acceptance_claim_is_rejected(self):
        data = self.copy()
        data["summary"]["owner_acceptance"] = "accepted"
        self.check_error(data, "semantic-audit-schema")


if __name__ == "__main__":
    unittest.main()

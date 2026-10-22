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

    def bounded_page(self, data):
        page = next(item for item in data["pages"]
                    if item["review"]["disposition"] == "sound")
        page["review"]["disposition"] = "sound-with-findings"
        page["review"]["findings"] = [{
            "severity": "low",
            "kind": "status",
            "summary": "A bounded test finding.",
            "anchor": "page",
            "remediation": "Fix the local wording.",
            "gate": None,
        }]
        return page

    def test_complete_artifact(self):
        result = validate_data(self.data, ROOT)
        self.assertEqual(result["pages"], 423)
        self.assertGreaterEqual(result["open_gates"], 1)

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

    def test_substring_anchor_is_rejected(self):
        data = self.copy()
        page = self.bounded_page(data)
        page["review"]["findings"][0]["anchor"] = "invalid anchor"
        self.check_error(data, "semantic-audit-finding-anchor")

    def test_blocked_without_gate_is_rejected(self):
        data = self.copy()
        page = self.bounded_page(data)
        page["review"]["disposition"] = "blocked"
        page["review"]["findings"][0]["gate"] = None
        self.check_error(data, "semantic-audit-gate-missing")

    def test_needs_remediation_requires_medium_finding(self):
        data = self.copy()
        page = self.bounded_page(data)
        page["review"]["disposition"] = "needs-remediation"
        page["review"]["findings"] = []
        self.check_error(data, "semantic-audit-remediation-severity")

    def test_duplicate_document_id_is_rejected(self):
        data = self.copy()
        data["pages"][1]["document_id"] = data["pages"][0]["document_id"]
        self.check_error(data, "semantic-audit-duplicate-id")

    def test_tier_mismatch_is_rejected(self):
        data = self.copy()
        page = next(item for item in data["pages"]
                    if item["tier"] == "technical")
        page["tier"] = "navigation"
        self.check_error(data, "semantic-audit-tier")

    def test_non_ancestor_source_commit_is_rejected(self):
        data = self.copy()
        data["source_commit"] = "0" * 40
        self.check_error(data, "semantic-audit-source-commit-not-ancestor")

    def test_high_finding_in_bounded_is_rejected(self):
        data = self.copy()
        page = self.bounded_page(data)
        page["review"]["findings"].append({
            "severity": "high",
            "kind": "contradictory",
            "summary": "A high-severity finding cannot remain in a bounded disposition.",
            "anchor": "page",
            "remediation": "Escalate the disposition.",
            "gate": None,
        })
        self.check_error(data, "semantic-audit-medium-in-bounded")

    def test_missing_required_check_is_rejected(self):
        data = self.copy()
        page = next(item for item in data["pages"]
                    if item["tier"] == "technical")
        del page["review"]["checks"]["question"]
        self.check_error(data, "semantic-audit-check-missing")

    def test_needs_remediation_requires_medium_remediation(self):
        data = self.copy()
        page = self.bounded_page(data)
        finding = page["review"]["findings"][0]
        finding["severity"] = "medium"
        finding["remediation"] = None
        finding["gate"] = "A gate is not a remediation."
        page["review"]["disposition"] = "needs-remediation"
        self.check_error(data, "semantic-audit-remediation-missing")

    def test_kind_mismatch_is_rejected(self):
        data = self.copy()
        data["pages"][0]["kind"] = "chapter"
        self.check_error(data, "semantic-audit-kind")

    def test_id_mismatch_is_rejected(self):
        data = self.copy()
        data["pages"][0]["document_id"] = "tycho.page.00000000000000000000000000000000"
        self.check_error(data, "semantic-audit-id")

    def test_phase4_mismatch_is_rejected(self):
        data = self.copy()
        page = next(item for item in data["pages"]
                    if item["phase4_disposition"] != "navigation")
        page["phase4_disposition"] = "navigation"
        self.check_error(data, "semantic-audit-phase4")

    def test_medium_finding_in_bounded_is_rejected(self):
        data = self.copy()
        page = self.bounded_page(data)
        page["review"]["findings"].append({
            "severity": "medium",
            "kind": "contradictory",
            "summary": "A medium finding cannot remain in a bounded disposition.",
            "anchor": "page",
            "remediation": "Escalate the disposition.",
            "gate": None,
        })
        self.check_error(data, "semantic-audit-medium-in-bounded")

    def test_partial_check_on_sound_page_is_rejected(self):
        data = self.copy()
        page = next(item for item in data["pages"]
                    if item["review"]["disposition"] == "sound")
        check = next(iter(page["review"]["checks"]))
        page["review"]["checks"][check] = "partial"
        self.check_error(data, "semantic-audit-sound-with-partial")

    def test_open_gate_summary_mismatch_is_rejected(self):
        data = self.copy()
        data["summary"]["open_gates"] += 1
        self.check_error(data, "semantic-audit-summary-mismatch")

    def test_unknown_finding_anchor_is_rejected(self):
        data = self.copy()
        page = self.bounded_page(data)
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
        page = self.bounded_page(data)
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

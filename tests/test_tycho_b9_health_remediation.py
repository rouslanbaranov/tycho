"""Regression guards for the 2026-10-29 Health Readiness review remediation.

The Health, Readiness and Liveness Checks card remains partial-bounded. These
guards pin the five review corrections: both public sources in the card scope,
the auxiliary owner-unit declaration, refreshed review/source dates, a telemetry
supporting binding under the alternative, an owner failure-path summary, and the
full route question including startup completion. No promotion is asserted.
"""
import json
from pathlib import Path
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

PATTERN_ID = "tycho.pattern.health-readiness-and-liveness-checks"
CARD_PATH = (
    "book/volumes/v11-pattern-atlas/c11-security-operations/"
    "health-readiness-and-liveness-checks.md")
OWNER_PATH = (
    "book/volumes/v09-observability-security-and-operations/"
    "c06-incident-response-and-operational-change/incident-practice.md")
MICROSOFT_RECORD = "read.microsoft-health-endpoint.2026-10-29"
MICROSOFT_REVISION = (
    "b5b302585c4e60a5d696b128b6a03d21c9629848e9fa2be23e6e1bc1751d1d61")


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def frontmatter(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1])


class HealthCardTests(unittest.TestCase):
    def setUp(self):
        self.card = frontmatter(CARD_PATH)
        self.text = (ROOT / CARD_PATH).read_text(encoding="utf-8")

    def test_card_scope_lists_both_sources(self):
        self.assertEqual(
            self.card["evidence_scope"]["source_ids"],
            ["src.kubernetes", "src.microsoft-cloud-patterns"])
        self.assertIn("src.microsoft-cloud-patterns", self.text)

    def test_card_review_and_source_dates_are_current(self):
        self.assertEqual(self.card["content_review"]["reviewed_at"],
                         "2026-10-29")
        self.assertEqual(self.card["updated_at"], "2026-10-29")
        self.assertEqual(self.card["source_inspection_date"], "2026-10-29")
        self.assertIsNone(self.card["content_verified_at"])

    def test_route_question_includes_startup_completion(self):
        self.assertEqual(
            self.card["route_hints"]["questions"],
            ["Should the runtime distinguish process liveness, traffic readiness "
             "and startup completion?"])

    def test_failure_recovery_summarizes_owner_path_and_containment(self):
        section = self.text.split("**Failure and recovery.**", 1)[1]
        section = section.split("**Technical owner.**", 1)[0].lower()
        self.assertIn("false restart or traffic sent to an unready instance",
                      section)
        self.assertIn("bound probe", section)
        self.assertIn("consecutive failures", section)
        self.assertIn("shared-dependency checks out of liveness", section)


class HealthOwnerUnitTests(unittest.TestCase):
    def setUp(self):
        self.owners = {entry["pattern_id"]: entry for entry in load(
            "edition/patterns/owner-units.v1.json")["entries"]}
        self.owner = self.owners[PATTERN_ID]

    def test_auxiliary_source_declaration_matches_ledger(self):
        auxiliary = self.owner["source_support"]["auxiliary"]
        self.assertEqual(len(auxiliary), 1)
        self.assertEqual(auxiliary[0]["source_id"],
                         "src.microsoft-cloud-patterns")
        self.assertEqual(auxiliary[0]["ledger_record"], MICROSOFT_RECORD)
        self.assertEqual(auxiliary[0]["revision"], MICROSOFT_REVISION)
        records = {record["id"]: record for record in load(
            "edition/patterns/reading-ledger.v1.json")["records"]}
        self.assertEqual(records[MICROSOFT_RECORD]["source_id"],
                         "src.microsoft-cloud-patterns")
        self.assertEqual(records[MICROSOFT_RECORD]["content_sha256"],
                         MICROSOFT_REVISION)

    def test_alternative_has_telemetry_supporting_binding(self):
        alternative = self.owner["technical_evidence"]["alternative"]
        self.assertEqual(alternative["binding"]["section"],
                         "When to use this pattern")
        supporting = alternative["supporting_bindings"]
        self.assertEqual(len(supporting), 1)
        self.assertEqual(supporting[0]["section"],
                         "When to use this pattern")
        self.assertIn("platform-level metrics, log-based alerts, or internal",
                      supporting[0]["quote"])
        self.assertEqual(supporting[0]["ledger_record"], MICROSOFT_RECORD)
        self.assertEqual(supporting[0]["revision"], MICROSOFT_REVISION)

    def test_entry_stays_partial_bounded_and_unpromoted(self):
        self.assertEqual(self.owner["technical_coverage"], "partial-bounded")
        self.assertEqual(self.owner["decision_coverage"], "partial-bounded")
        self.assertEqual(self.owner["review_state"], "self-checked")
        promotions = {item["pattern_id"] for item in load(
            "edition/patterns/sufficient-promotions.v1.json")["promotions"]}
        self.assertNotIn(PATTERN_ID, promotions)
        registry = {item["id"]: item for item in load(
            "edition/patterns/registry.v1.json")["patterns"]}
        self.assertEqual(registry[PATTERN_ID]["coverage"],
                         {"technical": "partial-bounded",
                          "decision": "partial-bounded",
                          "overall": "partial-bounded"})


if __name__ == "__main__":
    unittest.main()

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARD = ROOT / "book/volumes/v11-pattern-atlas/c03-messaging-integration/claim-check.md"
OWNER = ROOT / (
    "book/volumes/v04-distributed-coordination-and-events/"
    "c06-messaging-families-and-delivery-contracts/claim-check.md"
)
OWNER_UNITS = ROOT / "edition/patterns/owner-units.v1.json"
CASES = (
    "orphaned payload",
    "unresolvable token",
    "duplicate claim check",
    "integrity mismatch",
    "store outage or data loss",
)


def squash(text):
    return " ".join(text.split())


def owner_section(text):
    start = text.index("# Claim Check")
    end = text.index("## Navigation", start)
    return text[start:end]


class ClaimCheckReviewGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.card = squash(CARD.read_text(encoding="utf-8"))
        cls.owner = squash(owner_section(OWNER.read_text(encoding="utf-8")))
        data = json.loads(OWNER_UNITS.read_text(encoding="utf-8"))
        cls.unit = next(
            item for item in data["entries"]
            if item["pattern_id"] == "tycho.pattern.claim-check"
        )

    def test_lifecycle_ownership_is_payload_not_token_only(self):
        self.assertIn("payload lifecycle", self.card)
        self.assertNotIn("token lifecycle, access control", self.card)
        self.assertIn("payload lifecycle", self.owner)
        self.assertNotIn("store durability have no owner", self.card)

    def test_owner_notes_limit_eip_to_stored_payload(self):
        notes = self.unit["notes"]
        self.assertIn("read.microsoft-claim-check.2026-10-28", notes)
        self.assertIn("EIP pattern page", notes)
        self.assertIn("supports only the stored-payload and claim-token description", notes)
        self.assertNotIn(
            "all four dimensions bind to the Microsoft Learn Claim Check page and the EIP",
            notes,
        )

    def test_failure_cases_are_sourced_across_all_five(self):
        failure = self.unit["technical_evidence"]["failure_recovery"]
        for case in CASES:
            self.assertIn(case, failure["quote"])
            self.assertIn(case, self.owner)
        binding = failure["binding"]["quote"]
        self.assertIn("Payload integrity", binding)
        self.assertIn("Payload availability and durability", binding)
        self.assertIn("Idempotent Consumer", binding)


if __name__ == "__main__":
    unittest.main()

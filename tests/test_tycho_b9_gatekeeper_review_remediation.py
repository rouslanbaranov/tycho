"""Regression guards for the 2026-10-29 Gatekeeper review remediation.

The Gatekeeper mechanism previously claimed the gatekeeper "authenticates the
caller and evaluates coarse authorization", while the bound source passage only
described validation and sanitization. The remediation narrows the mechanism to
the source's wording, binds the Solution passage for validation and
authorization checks, adds the Workload design sentence for authentication
initiation and authorization checks, and keeps the entry partial-bounded and
unpromoted.
"""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATTERN_ID = "tycho.pattern.gatekeeper"
CARD_PATH = "book/volumes/v11-pattern-atlas/c02-api-communication/gatekeeper.md"
OWNER_PATH = (
    "book/volumes/v02-application-boundaries-and-contracts/"
    "c07-authorization-boundaries-and-multitenancy/"
    "authorization-boundaries-and-multitenancy.md")
RECORD = "read.microsoft-gatekeeper.2026-10-21"
REVISION = "5af11b967b9ffe814df508afa3f4cd4d3797bdb6f280b78d1be61db8a53a28f0"


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def squash(text):
    return " ".join(text.split())


def field(text, label):
    match = re.search(
        r"\*\*" + re.escape(label) + r"\.\*\*\s*(.+?)(?:\n\n|\Z)",
        text, re.S)
    if match is None:
        raise AssertionError("missing card field: " + label)
    return squash(match.group(1))


class GatekeeperReviewRemediationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        units = load("edition/patterns/owner-units.v1.json")
        cls.unit = next(
            item for item in units["entries"]
            if item["pattern_id"] == PATTERN_ID)
        cls.mechanism = cls.unit["technical_evidence"]["mechanism"]
        cls.records = {
            item["id"]: item
            for item in load("edition/patterns/reading-ledger.v1.json")["records"]}
        cls.record = cls.records[RECORD]
        cls.card = (ROOT / CARD_PATH).read_text(encoding="utf-8")
        owner_text = (ROOT / OWNER_PATH).read_text(encoding="utf-8")
        start = owner_text.index("\n### Gatekeeper\n")
        cls.owner = owner_text[start:]

    def test_mechanism_claim_no_longer_says_the_gatekeeper_authenticates(self):
        claim = self.mechanism["quote"].lower()
        self.assertNotIn("authenticates the caller", claim)
        self.assertNotIn("coarse authorization", claim)
        self.assertIn("validates and sanitizes requests", claim)
        self.assertIn("authentication initiation", claim)
        self.assertIn("authorization checks", claim)

    def test_primary_binding_names_validation_and_authorization(self):
        binding = self.mechanism["binding"]
        self.assertEqual(binding["section"], "Solution")
        self.assertIn(
            "validate and sanitize the request content", binding["quote"])
        self.assertIn(
            "Gatekeepers might authorize the request", binding["quote"])
        self.assertEqual(binding["revision"], REVISION)
        self.assertEqual(self.record["content_sha256"], REVISION)
        self.assertIn(binding["section"], self.record["sections_read"])

    def test_supporting_binding_names_authentication_initiation(self):
        supporting = self.mechanism["supporting_bindings"]
        self.assertEqual(len(supporting), 1)
        binding = supporting[0]
        self.assertEqual(binding["section"], "Workload design")
        self.assertIn(
            "authentication initiation, and authorization checks",
            binding["quote"])
        self.assertEqual(binding["source_id"], "src.microsoft-cloud-patterns")
        self.assertEqual(binding["ledger_record"], RECORD)
        self.assertEqual(binding["revision"], REVISION)
        self.assertIn(binding["section"], self.record["sections_read"])

    def test_every_binding_uses_the_admitted_record(self):
        bindings = [self.mechanism["binding"]]
        bindings.extend(self.mechanism["supporting_bindings"])
        for binding in bindings:
            self.assertEqual(binding["source_id"], "src.microsoft-cloud-patterns")
            self.assertEqual(binding["ledger_record"], RECORD)
            self.assertEqual(binding["revision"], REVISION)
            self.assertIn(binding["section"], self.record["sections_read"])
            self.assertGreaterEqual(len(binding["quote"]), 30)

    def test_owner_page_and_card_use_the_narrowed_claim(self):
        self.assertIn(squash(self.mechanism["quote"]), squash(self.owner))
        good_fit = field(self.card, "Good-fit conditions")
        self.assertIn(
            "centralize authentication initiation and authorization checks",
            good_fit)
        self.assertNotIn("authenticate and forward trusted context", good_fit)
        sources = self.card.split("**Sources.**", 1)[1].split(
            "**Decision state.**", 1)[0]
        self.assertIn('"Solution"', sources)
        self.assertIn('"Workload design"', sources)
        self.assertIn('"Solution"', self.owner)
        self.assertIn('"Workload design"', self.owner)

    def test_limits_use_authentication_initiation_wording(self):
        limits = self.owner.split("**Limits.**", 1)[1].split(
            "**Source boundary.**", 1)[0]
        self.assertIn("only initiates authentication", limits)
        self.assertNotIn("only authenticates", limits)

    def test_entry_is_promoted_after_review(self):
        self.assertEqual(self.unit["technical_coverage"], "sufficient")
        self.assertEqual(self.unit["decision_coverage"], "sufficient")
        self.assertEqual(self.unit["review_state"], "self-checked")
        promotions = {
            item["pattern_id"]
            for item in load(
                "edition/patterns/sufficient-promotions.v1.json")["promotions"]}
        self.assertIn(PATTERN_ID, promotions)
        registry = {
            item["id"]: item
            for item in load("edition/patterns/registry.v1.json")["patterns"]}
        self.assertEqual(
            registry[PATTERN_ID]["coverage"],
            {"technical": "sufficient",
             "decision": "sufficient",
             "overall": "sufficient"})


if __name__ == "__main__":
    unittest.main()

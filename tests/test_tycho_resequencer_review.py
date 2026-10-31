import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARD = ROOT / "book/volumes/v11-pattern-atlas/c03-messaging-integration/resequencer.md"
OWNER = ROOT / (
    "book/volumes/v04-distributed-coordination-and-events/"
    "c06-messaging-families-and-delivery-contracts/resequencer.md"
)
OWNER_UNITS = ROOT / "edition/patterns/owner-units.v1.json"
LEDGER = ROOT / "edition/patterns/reading-ledger.v1.json"
PROMOTIONS = ROOT / "edition/patterns/sufficient-promotions.v1.json"
SOURCE_PLAN = ROOT / "edition/patterns/source-plan.v1.json"
RECORDS = (
    "read.batch2-resequencer.2026-10-21",
    "read.camel-resequence.2026-10-29",
    "read.microsoft-sequential-convoy.2026-10-29",
)
DIMENSIONS = ("mechanism", "invariant", "failure_recovery", "alternative")


def squash(text):
    return " ".join(text.split())


def owner_section(text):
    start = text.index("# Resequencer")
    end = text.index("## Navigation", start)
    return squash(text[start:end])


class ResequencerReviewGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.card = squash(CARD.read_text(encoding="utf-8"))
        cls.owner = owner_section(OWNER.read_text(encoding="utf-8"))
        units = json.loads(OWNER_UNITS.read_text(encoding="utf-8"))
        cls.unit = next(
            item for item in units["entries"]
            if item["pattern_id"] == "tycho.pattern.resequencer"
        )
        ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        cls.records = {item["id"]: item for item in ledger["records"]}
        plan = json.loads(SOURCE_PLAN.read_text(encoding="utf-8"))
        cls.plan = next(
            item for item in plan["entries"]
            if item["pattern_id"] == "tycho.pattern.resequencer"
        )

    def test_card_is_decision_first_and_bounded(self):
        body = self.card[self.card.index("# Resequencer"):]
        self.assertTrue(body.startswith("# Resequencer **Decision.**"), body[:120])
        self.assertIn("bounded buffer", self.card)
        self.assertIn("gap timeout", self.card)
        self.assertIn("late-message disposition", self.card)
        self.assertNotIn("sufficient", self.card.replace("not sufficient", ""))

    def test_all_four_dimensions_have_exact_bindings(self):
        evidence = self.unit["technical_evidence"]
        for name in DIMENSIONS:
            dimension = evidence[name]
            self.assertEqual(dimension["state"], "supported", name)
            self.assertIn(squash(dimension["quote"]), self.owner, name)
            binding = dimension["binding"]
            record = self.records[binding["ledger_record"]]
            self.assertEqual(record["source_id"], binding["source_id"], name)
            self.assertEqual(record["content_sha256"], binding["revision"], name)
            self.assertIn(binding["section"], record["sections_read"], name)
            self.assertTrue(binding["quote"].strip(), name)
        self.assertEqual(evidence["alternative"]["binding"]["source_id"],
                         "src.microsoft-cloud-patterns")
        self.assertEqual(evidence["failure_recovery"]["binding"]["source_id"],
                         "src.camel")

    def test_new_source_units_are_planned_and_read(self):
        units = {(unit["source_id"], unit["read_record_id"])
                 for unit in self.plan["required_units"]}
        self.assertIn(("src.camel", "read.camel-resequence.2026-10-29"), units)
        self.assertIn(
            ("src.microsoft-cloud-patterns", "read.microsoft-sequential-convoy.2026-10-29"),
            units,
        )
        for record_id in RECORDS:
            record = self.records[record_id]
            self.assertEqual(record["status"], "read")
            self.assertIn(record_id, self.card)
            self.assertIn(record["source_id"], self.card)

    def test_sufficient_and_promoted_after_final_review(self):
        promotions = [item["pattern_id"] for item in json.loads(
            PROMOTIONS.read_text(encoding="utf-8"))["promotions"]]
        self.assertIn("tycho.pattern.resequencer", promotions)
        self.assertEqual(len(promotions), 78)
        self.assertEqual(self.unit["technical_coverage"], "sufficient")
        self.assertEqual(self.unit["decision_coverage"], "sufficient")


if __name__ == "__main__":
    unittest.main()

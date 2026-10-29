import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "book/volumes/v11-pattern-atlas/c03-messaging-integration"
OWNERS = ROOT / (
    "book/volumes/v04-distributed-coordination-and-events/"
    "c06-messaging-families-and-delivery-contracts"
)
OWNER_UNITS = ROOT / "edition/patterns/owner-units.v1.json"
PROMOTIONS = ROOT / "edition/patterns/sufficient-promotions.v1.json"


def squash(text):
    return " ".join(text.split())


def section(text, start, end):
    begin = text.index(start)
    finish = text.index(end, begin)
    return squash(text[begin:finish])


def field(text, label):
    match = re.search(r"\*\*" + label + r"\.\*\*\s*(.+?)(?:\n\n|\Z)", text, re.S)
    if match is None:
        raise AssertionError("missing field: " + label)
    return squash(match.group(1))


class B8ReviewRemediationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resequencer_card_raw = (
            CARDS / "resequencer.md").read_text(encoding="utf-8")
        cls.pipes_card_raw = (
            CARDS / "pipes-and-filters.md").read_text(encoding="utf-8")
        cls.resequencer_card = squash(cls.resequencer_card_raw)
        cls.pipes_card = squash(cls.pipes_card_raw)
        cls.resequencer_owner = squash(
            (OWNERS / "resequencer.md").read_text(encoding="utf-8"))
        cls.pipes_owner = squash(
            (OWNERS / "pipes-and-filters.md").read_text(encoding="utf-8"))
        units = json.loads(OWNER_UNITS.read_text(encoding="utf-8"))
        cls.resequencer_unit = next(
            item for item in units["entries"]
            if item["pattern_id"] == "tycho.pattern.resequencer")
        cls.pipes_unit = next(
            item for item in units["entries"]
            if item["pattern_id"] == "tycho.pattern.pipes-and-filters")
        promotions = json.loads(PROMOTIONS.read_text(encoding="utf-8"))
        cls.promoted = {item["pattern_id"] for item in promotions["promotions"]}

    def test_resequencer_buffer_is_not_an_alternative_trigger(self):
        decision = section(self.resequencer_owner, "**Decision.**", "**Mechanism.**")
        self.assertNotIn("or the buffer cannot be bounded", decision)
        self.assertIn(
            "when the buffer cannot be bounded, reject the resequencer or fail "
            "the ordering scope", decision)
        self.assertIn(
            "Partition by key instead when global order is unnecessary.",
            self.resequencer_card)
        self.assertIn(
            "when the buffer cannot be bounded",
            field(self.resequencer_card_raw, "Hard contraindications"))
        self.assertIn(
            "fail the ordering scope",
            field(self.resequencer_card_raw, "Failure and recovery"))
        self.assertIn(
            "buffer cannot be bounded",
            field(self.resequencer_owner, "Failure and recovery"))

    def test_pipes_invariant_binds_ordering_not_ports(self):
        unit = self.pipes_unit["technical_evidence"]["invariant"]
        self.assertEqual(
            unit["binding"]["section"], "Parallel Processing (p.74)")
        self.assertNotIn("port", unit["quote"].lower())
        self.assertNotIn("port", unit["reason"].lower())
        self.assertIn(
            "A parallel or multi-instance stage can reorder messages",
            unit["quote"])
        mechanism = section(self.pipes_owner, "**Mechanism.**", "**Invariant.**")
        invariant = section(
            self.pipes_owner, "**Invariant.**", "**Failure and recovery.**")
        self.assertIn("one inbound and one outbound port", mechanism)
        self.assertIn("Each filter exposes a very simple interface", mechanism)
        self.assertNotIn("port", invariant.lower())

    def test_pipes_alternative_guidance_is_labelled_and_aligned(self):
        alternative = section(
            self.pipes_owner, "**Alternative.**", "**Limits.**")
        self.assertIn("Tycho guidance, not a source claim:", alternative)
        self.assertIn(
            "stages are small and cannot be operated independently", alternative)
        card_alternative = field(
            self.pipes_card_raw, "Competing alternative")
        self.assertIn("Tycho guidance, not a source claim:", card_alternative)
        self.assertIn(
            "stages are small and cannot be operated independently",
            card_alternative)
        self.assertEqual(
            card_alternative,
            self.pipes_unit["decision_evidence"]["competing_alternative"])
        self.assertIn(
            "per-stage latency and coordination exceed the value of isolation",
            self.pipes_owner)
        self.assertIn(
            "per-stage latency and coordination exceed the value of isolation",
            self.pipes_card)

    def test_pipes_card_review_date_is_current(self):
        self.assertIn('reviewed_at: "2026-10-29"', self.pipes_card)
        self.assertIn('updated_at: "2026-10-29"', self.pipes_card)

    def test_both_entries_remain_partial_bounded(self):
        for pattern_id, unit in (
            ("tycho.pattern.resequencer", self.resequencer_unit),
            ("tycho.pattern.pipes-and-filters", self.pipes_unit),
        ):
            self.assertNotIn(pattern_id, self.promoted)
            self.assertEqual(unit["technical_coverage"], "partial-bounded")
            self.assertEqual(unit["decision_coverage"], "partial-bounded")


class B8ClaimRequestSplitterRemediationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.request_card_raw = (
            CARDS / "request-reply-messaging.md").read_text(encoding="utf-8")
        cls.claim_card_raw = (
            CARDS / "claim-check.md").read_text(encoding="utf-8")
        cls.split_card_raw = (
            CARDS / "splitter.md").read_text(encoding="utf-8")
        cls.request_owner = squash(
            (OWNERS / "request-reply-messaging.md").read_text(encoding="utf-8"))
        cls.claim_owner = squash(
            (OWNERS / "claim-check.md").read_text(encoding="utf-8"))
        cls.split_owner = squash(
            (OWNERS / "splitter.md").read_text(encoding="utf-8"))
        units = json.loads(OWNER_UNITS.read_text(encoding="utf-8"))
        cls.units = {item["pattern_id"]: item for item in units["entries"]}
        promotions = json.loads(PROMOTIONS.read_text(encoding="utf-8"))
        cls.promoted = {item["pattern_id"] for item in promotions["promotions"]}

    def test_request_reply_has_explicit_limits_and_decision(self):
        self.assertIn("**Decision.**", self.request_card_raw)
        limits = field(self.request_owner, "Limits")
        for needle in ("publisher-abridged", "correlation-identifier", "timeouts",
                       "duplicate-reply", "callback contract"):
            self.assertIn(needle, limits)
        self.assertIn("one-outstanding-request", limits)
        self.assertIn("private-reply-channel", limits)

    def test_request_reply_removes_blocking_contraindication(self):
        card = squash(self.request_card_raw)
        self.assertNotIn("caller must block on a Remote Procedure Invocation", card)
        self.assertIn("Tycho synthesis", field(
            self.request_card_raw, "Competing alternative"))
        self.assertIn("Correlation Identifier", field(
            self.request_card_raw, "Good-fit conditions"))
        self.assertIn("Tycho guidance",
                      field(self.request_card_raw, "Good-fit conditions"))
        self.assertIn("one outstanding request", card)

    def test_request_reply_alternative_binding_and_quote(self):
        unit = self.units["tycho.pattern.request-reply-messaging"]
        alternative = unit["technical_evidence"]["alternative"]
        self.assertEqual(alternative["binding"]["section"], "Request-Reply")
        self.assertIn("does not present RPC", alternative["reason"])
        self.assertIn("Tycho synthesis", alternative["reason"])
        self.assertEqual(
            unit["decision_evidence"]["competing_alternative"],
            field(self.request_card_raw, "Competing alternative"))

    def test_request_reply_card_dates_are_current(self):
        self.assertIn('reviewed_at: "2026-10-29"', self.request_card_raw)
        self.assertIn('updated_at: "2026-10-29"', self.request_card_raw)

    def test_claim_check_separates_deletion_from_authorization(self):
        card = squash(self.claim_card_raw)
        self.assertIn("authorization can remain an independent interaction", card)
        self.assertIn(
            "authorization remains an independent interaction", card)
        self.assertNotIn(
            "payload lifecycle, access control and failure handling have owners",
            card)
        self.assertIn(
            "independent interaction between producer or consumer systems",
            self.claim_owner)
        unit = self.units["tycho.pattern.claim-check"]
        self.assertNotIn("authorization ownership", squash(json.dumps(unit)))
        binding = unit["technical_evidence"]["invariant"]["binding"]
        self.assertIn("Payload lifecycle ownership", binding["quote"])
        self.assertIn(
            "Leave authorization as an independent interaction", binding["quote"])

    def test_splitter_invariant_binds_unknown_size_and_release(self):
        unit = self.units["tycho.pattern.splitter"]
        invariant = unit["technical_evidence"]["invariant"]
        self.assertEqual(invariant["binding"]["section"], "Iterators")
        self.assertIn("SEQUENCE_SIZE", invariant["binding"]["quote"])
        self.assertIn("custom ReleaseStrategy", invariant["binding"]["quote"])
        self.assertIn("send-partial-result-on-expiry",
                      invariant["binding"]["quote"])
        self.assertIn("Iterators section", self.split_owner)
        self.assertIn("aggregate group remains incomplete", self.split_owner)

    def test_three_entries_remain_partial_bounded_and_unpromoted(self):
        for pattern_id in (
                "tycho.pattern.claim-check",
                "tycho.pattern.request-reply-messaging",
                "tycho.pattern.splitter"):
            self.assertNotIn(pattern_id, self.promoted)
            unit = self.units[pattern_id]
            self.assertEqual(unit["technical_coverage"], "partial-bounded")
            self.assertEqual(unit["decision_coverage"], "partial-bounded")


if __name__ == "__main__":
    unittest.main()

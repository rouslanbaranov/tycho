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

    def test_both_entries_are_promoted_and_sufficient(self):
        for pattern_id, unit in (
            ("tycho.pattern.resequencer", self.resequencer_unit),
            ("tycho.pattern.pipes-and-filters", self.pipes_unit),
        ):
            self.assertIn(pattern_id, self.promoted)
            self.assertEqual(unit["technical_coverage"], "sufficient")
            self.assertEqual(unit["decision_coverage"], "sufficient")


class B8ClaimRequestSplitterRemediationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.request_card_raw = (
            CARDS / "request-reply-messaging.md").read_text(encoding="utf-8")
        cls.claim_card_raw = (
            CARDS / "claim-check.md").read_text(encoding="utf-8")
        cls.split_card_raw = (
            CARDS / "splitter.md").read_text(encoding="utf-8")
        cls.split_card = squash(cls.split_card_raw)
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
        self.assertEqual(alternative["binding"]["section"], "Related patterns")
        self.assertIn("Related patterns", alternative["reason"])
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
        supporting = invariant["supporting_bindings"][0]
        self.assertEqual(supporting["section"], "Programming Model")
        self.assertIn("MessageHandler implementation", supporting["quote"])
        self.assertIn("CORRELATION_ID", supporting["quote"])
        self.assertIn("SEQUENCE_NUMBER", supporting["quote"])
        self.assertIn("MessageHandler implementation", self.split_card)
        self.assertIn("Iterators section", self.split_owner)
        self.assertIn("aggregate group remains incomplete", self.split_owner)

    def test_splitter_invariant_states_identity_position_and_size(self):
        invariant = field(self.split_owner, "Invariant")
        for needle in (
                "correlation identity",
                "sequence position",
                "total size",
                "when the total count is known",
                "custom release strategy or",
                "send-partial-result-on-expiry",
                "not evidence of successful completion"):
            self.assertIn(needle, invariant)
        self.assertIn("Tycho guidance, not a source claim", invariant)
        unit = self.units["tycho.pattern.splitter"]["technical_evidence"]["invariant"]
        self.assertIn("correlation identity", unit["quote"])
        self.assertIn("Tycho guidance, not a source claim", unit["quote"])
        decision = field(self.split_card_raw, "Decision")
        self.assertIn("total count is known, or an explicit release rule or expiry",
                      decision)
        self.assertIn("partial result or forced closure rather than silent success",
                      decision)
        self.assertIn("Tycho guidance", decision)

    def test_splitter_labels_error_inference_and_contraindications(self):
        good = field(self.split_card_raw, "Good-fit conditions")
        self.assertIn("Tycho inference: errors can be correlated to the parent",
                      good)
        contraindications = field(
            self.split_card_raw, "Hard contraindications")
        self.assertIn("Tycho guidance, not a source claim", contraindications)
        self.assertIn("ordering across parts is mandatory", contraindications)

    def test_splitter_watermark_is_attributed_to_camel(self):
        for text in (
                field(self.split_owner, "Failure and recovery"),
                field(self.split_card_raw, "Failure and recovery")):
            self.assertIn("Apache Camel's value-based watermark", text)
            self.assertIn("maxFailedRecords", text)
        unit = self.units["tycho.pattern.splitter"]
        self.assertIn(
            "Apache Camel's value-based watermark",
            unit["technical_evidence"]["failure_recovery"]["quote"])

    def test_splitter_mechanism_binds_default_output(self):
        unit = self.units["tycho.pattern.splitter"]
        mechanism = unit["technical_evidence"]["mechanism"]
        self.assertEqual(
            mechanism["binding"]["section"],
            "What is returned from Split EIP when its complete")
        self.assertIn("return the original input message",
                      mechanism["binding"]["quote"])
        self.assertIn("return the original input message", self.split_owner)

    def test_splitter_limits_state_provider_boundary_and_tycho_scope(self):
        limits = field(self.split_owner, "Limits")
        for needle in (
                "provider documentation",
                "provider-specific",
                "not a complete Splitter contract",
                "Tycho guidance",
                "bounded fan-out",
                "ordering"):
            self.assertIn(needle, limits)
        good = field(self.split_card_raw, "Good-fit conditions")
        self.assertIn("Tycho guidance, not a source claim", good)
        self.assertIn("has an owner", good)

    def test_splitter_card_dates_are_current(self):
        self.assertIn('reviewed_at: "2026-10-29"', self.split_card_raw)
        self.assertIn('updated_at: "2026-10-29"', self.split_card_raw)

    def test_claim_invariant_binding_contains_its_own_quote(self):
        unit = self.units["tycho.pattern.claim-check"]
        invariant = unit["technical_evidence"]["invariant"]
        binding_quote = invariant["binding"]["quote"]
        self.assertIn(
            "Publish the token only after the payload write succeeds",
            binding_quote)
        self.assertIn("Payload lifecycle ownership", binding_quote)
        self.assertIn(
            "Leave authorization as an independent interaction",
            binding_quote)
        self.assertIn(
            "Publish the token only after the payload write succeeds",
            invariant["quote"])

    def test_claim_mechanism_uses_source_wording(self):
        unit = self.units["tycho.pattern.claim-check"]
        mechanism = unit["technical_evidence"]["mechanism"]
        self.assertTrue(
            mechanism["quote"].startswith("A sending application writes"))
        self.assertIn(
            "Receiving applications use the reference to retrieve the payload",
            mechanism["quote"])
        self.assertEqual(mechanism["quote"], mechanism["binding"]["quote"])

    def test_claim_failure_count_is_six(self):
        unit = self.units["tycho.pattern.claim-check"]
        failure = unit["technical_evidence"]["failure_recovery"]
        self.assertIn("six failure cases", failure["quote"])
        self.assertIn("store outage, and data loss", failure["quote"])
        self.assertIn("six failure cases", self.claim_owner)
        card_failure = field(self.claim_card_raw, "Failure and recovery")
        self.assertIn("store outages and data loss", card_failure)
        self.assertIn("six failure cases",
                      field(self.claim_card_raw, "Sources"))

    def test_claim_alternative_binds_inline_sentence(self):
        unit = self.units["tycho.pattern.claim-check"]
        alternative = unit["technical_evidence"]["alternative"]
        self.assertEqual(alternative["binding"]["section"],
                         "When to use this pattern")
        self.assertIn("send them inline",
                      alternative["binding"]["quote"])
        supporting = alternative["supporting_bindings"][0]
        self.assertEqual(supporting["section"], "Alternatives")
        self.assertIn("Compression can reduce", supporting["quote"])
        self.assertIn("more compact serializer", supporting["quote"])
        self.assertIn("send them inline", self.claim_owner)
        self.assertNotIn("inline-compression alternative", self.claim_owner)
        card_alternative = field(
            self.claim_card_raw, "Competing alternative")
        self.assertIn("Tycho guidance, not a source claim: reverse",
                      card_alternative)
        self.assertEqual(
            unit["decision_evidence"]["competing_alternative"],
            card_alternative)

    def test_claim_labels_expiry_and_defines_tenant_binding(self):
        failure = field(self.claim_card_raw, "Failure and recovery")
        self.assertIn("Tycho guidance, not a source claim: expire", failure)
        self.assertIn("idempotent consumer", failure)
        limits = field(self.claim_owner, "Limits")
        self.assertIn("tenant binding (a claim token is usable only", limits)

    def test_claim_good_fit_access_control_wording(self):
        good = field(self.claim_card_raw, "Good-fit conditions")
        self.assertIn("dedicated access controls", good)
        self.assertNotIn("tighter access control", good)

    def test_request_decision_uses_private_thread_and_callback_path(self):
        decision = field(self.request_card_raw, "Decision")
        self.assertIn("private to the requesting thread", decision)
        self.assertIn("Synchronous Block", decision)
        self.assertIn("Asynchronous Callback", decision)
        self.assertIn("multiple outstanding requests", decision)
        self.assertIn("single reply thread", decision)
        self.assertIn("Correlation Identifier", decision)
        self.assertIn("Tycho synthesis: prefer a direct synchronous", decision)
        self.assertIn("does not serve correlation mechanics", decision)

    def test_request_limits_state_source_supports_sharing(self):
        limits = field(self.request_owner, "Limits")
        self.assertIn(
            "matching across multiple outstanding requests", limits)
        self.assertIn("Asynchronous Callback", limits)
        self.assertIn("matching across multiple outstanding requests", limits)
        self.assertIn("Tycho guidance", limits)
        invariant = self.units[
            "tycho.pattern.request-reply-messaging"]["technical_evidence"][
                "invariant"]
        supporting = invariant["supporting_bindings"][0]
        self.assertEqual(supporting["section"], "Asynchronous Callback")
        self.assertIn("single reply thread", supporting["quote"])
        good = field(self.request_card_raw, "Good-fit conditions")
        self.assertIn("private to the requesting thread", good)
        self.assertIn("single reply thread", good)

    def test_request_reply_and_other_entries_promoted(self):
        self.assertEqual(len(self.promoted), 38)
        request = self.units["tycho.pattern.request-reply-messaging"]
        self.assertIn("tycho.pattern.request-reply-messaging", self.promoted)
        self.assertEqual(request["technical_coverage"], "sufficient")
        self.assertEqual(request["decision_coverage"], "sufficient")
        for pattern_id in ("tycho.pattern.claim-check", "tycho.pattern.splitter"):
            unit = self.units[pattern_id]
            self.assertIn(pattern_id, self.promoted)
            self.assertEqual(unit["technical_coverage"], "sufficient")
            self.assertEqual(unit["decision_coverage"], "sufficient")


class B8FinalClaimRequestSplitterReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.request_card_raw = (
            CARDS / "request-reply-messaging.md").read_text(encoding="utf-8")
        cls.request_owner_raw = (
            OWNERS / "request-reply-messaging.md").read_text(encoding="utf-8")
        cls.claim_card_raw = (
            CARDS / "claim-check.md").read_text(encoding="utf-8")
        cls.claim_owner_raw = (
            OWNERS / "claim-check.md").read_text(encoding="utf-8")
        cls.split_card_raw = (
            CARDS / "splitter.md").read_text(encoding="utf-8")
        cls.split_owner_raw = (
            OWNERS / "splitter.md").read_text(encoding="utf-8")
        cls.claim_owner = squash(cls.claim_owner_raw)
        cls.split_owner = squash(cls.split_owner_raw)
        units = json.loads(OWNER_UNITS.read_text(encoding="utf-8"))
        cls.units = {item["pattern_id"]: item for item in units["entries"]}

    def test_claim_inline_fit_reject_is_scoped_to_no_other_reason(self):
        decision = field(self.claim_card_raw, "Decision")
        self.assertIn(
            "no sensitivity, retention or repeated-serialization reason applies",
            decision)
        self.assertIn("retention reason is Tycho synthesis", decision)
        self.assertIn("source-stated use conditions", decision)
        contraindications = field(
            self.claim_card_raw, "Hard contraindications")
        self.assertIn(
            "no sensitivity, retention or repeated-serialization reason applies",
            contraindications)
        self.assertIn("retention is Tycho synthesis", contraindications)
        owner_decision = field(
            self.claim_owner_raw, "Decision")
        self.assertIn(
            "no sensitivity, retention or repeated-serialization reason applies",
            owner_decision)
        limits = field(self.claim_owner_raw, "Limits")
        self.assertIn(
            "payload that fits the transport still warrants a claim check",
            limits)
        self.assertIn("sensitivity, retention or repeated serialization", limits)

    def test_claim_reversal_has_inline_fit_precondition(self):
        alternative = field(self.claim_card_raw, "Competing alternative")
        self.assertIn(
            "reverse the choice only when the payload fits inline", alternative)
        self.assertEqual(
            self.units["tycho.pattern.claim-check"]["decision_evidence"][
                "competing_alternative"],
            alternative)
        owner_alternative = field(self.claim_owner_raw, "Alternative")
        self.assertIn(
            "reverse the choice only when the payload fits inline",
            owner_alternative)
        self.assertIn("Tycho guidance, not a source claim", owner_alternative)

    def test_claim_mechanism_binds_write_and_retrieval(self):
        mechanism = self.units["tycho.pattern.claim-check"][
            "technical_evidence"]["mechanism"]
        for needle in (
                "writes the full payload",
                "The messaging system never sees or stores the payload",
                "Receiving applications use the reference to retrieve"):
            self.assertIn(needle, mechanism["binding"]["quote"])
        self.assertIn(
            "Receiving applications use the reference to retrieve",
            self.claim_owner)

    def test_splitter_unknown_count_closes_incomplete_not_success(self):
        failure = field(self.split_card_raw, "Failure and recovery")
        self.assertIn("unknown part count leaves the aggregate incomplete",
                      failure)
        self.assertIn("neither is evidence of successful completion", failure)
        self.assertIn("Tycho guidance, not a source claim", failure)
        owner_failure = field(
            self.split_owner_raw, "Failure and recovery")
        self.assertIn(
            "unknown part count leaves the aggregate incomplete", owner_failure)
        self.assertIn("not evidence of successful completion", owner_failure)
        limits = field(self.split_owner_raw, "Limits")
        self.assertIn("partial result or forced closure", limits)
        self.assertIn("not proof of successful completion", limits)
        invariant = self.units["tycho.pattern.splitter"][
            "technical_evidence"]["invariant"]
        self.assertIn(
            "release a partial result or force closure", invariant["reason"])
        self.assertIn(
            "not evidence of successful completion", invariant["quote"])

    def test_splitter_mechanism_is_narrowed_to_default_output(self):
        mechanism = self.units["tycho.pattern.splitter"][
            "technical_evidence"]["mechanism"]
        self.assertEqual(
            mechanism["binding"]["section"],
            "What is returned from Split EIP when its complete")
        self.assertIn("return the original input message",
                      mechanism["binding"]["quote"])
        self.assertNotIn("supporting_bindings", mechanism)
        self.assertNotIn("Use a Splitter to break out", self.split_owner)
        self.assertNotIn("Camel defines it", self.split_owner)
        self.assertIn("by default", mechanism["reason"])

    def test_request_question_separates_channels_and_invocation(self):
        question = field(self.request_card_raw, "Decision question")
        self.assertIn("separate messages on separate", question)
        self.assertIn("invoking the responder indirectly", question)
        self.assertIn("both approaches block the caller", question)
        self.assertEqual(
            self.units["tycho.pattern.request-reply-messaging"][
                "decision_evidence"]["question"],
            question)
        self.assertIn(
            "Should a request and its reply travel as separate messages",
            self.request_owner_raw)
        decision = field(self.request_card_raw, "Decision")
        self.assertIn(
            "Tycho synthesis: treat both the Synchronous Block messaging approach",
            decision)
        self.assertIn("blocking the caller's thread", decision)
        self.assertIn("Tycho synthesis: prefer a direct synchronous", decision)

    def test_request_alternative_state_is_partial_for_blocking_premise(self):
        unit = self.units["tycho.pattern.request-reply-messaging"]
        alternative = unit["technical_evidence"]["alternative"]
        self.assertEqual(alternative["state"], "supported")
        self.assertIn("Messaging page", alternative["reason"])
        self.assertIn("Tycho synthesis", alternative["reason"])
        card_alternative = field(
            self.request_card_raw, "Competing alternative")
        self.assertIn(
            "bound Messaging page names the RPI pattern", card_alternative)
        self.assertEqual(
            unit["decision_evidence"]["competing_alternative"],
            card_alternative)
        limits = field(self.request_owner_raw, "Limits")
        self.assertIn("does not present Block messaging and RPI", limits)
        self.assertIn("Tycho synthesis", limits)


if __name__ == "__main__":
    unittest.main()

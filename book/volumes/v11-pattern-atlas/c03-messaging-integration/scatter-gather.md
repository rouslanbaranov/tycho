---
metadata_version: 1
id: "tycho.page.b864f32bd58a4f7b8eaaa223cdecfea7"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/scatter-gather.md"
title: "Scatter-Gather"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Scatter-Gather with bounded owner evidence."
route_hints:
  questions:
    - "Should one request be broadcast to several recipients and their responses combined?"
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "scatter-gather"
    - "scatter gather"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.aws-scatter-gather"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---

# Scatter-Gather

**Identity.** Scatter-Gather; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should one request be broadcast to several recipients and their
responses combined?

**Good-fit conditions.** Recipients are known or discoverable; partial responses are
acceptable; per-recipient deadlines exist; the aggregate is bounded. Tycho guidance, not
a source claim: define a response contract and a quorum or completeness rule, and assign
a straggler policy to an owner.

**Hard contraindications.** Reject when one authoritative recipient suffices, when
responses are not comparable, when the aggregate must be globally consistent, or when
tail latency would exceed the caller's budget. Tycho guidance: fan-out that can exhaust
the caller is also a contraindication.

**Competing alternative.** Tycho synthesis: a standalone aggregator fits when responses
already exist and no broadcast is needed. The AWS page supports only the comparison: it
calls the aggregator "another messaging pattern" that collects and distills responses,
while scatter-gather adds the broadcast. Reverse the choice when only already-produced
responses must be combined.

**Failure and recovery.** AWS states that some recipients can time out and the
implementation "should communicate to the client that the response is incomplete"; its
scatter-by-distribution description also says "The responses that time out are ignored"
and that the aggregator combines partial responses into a final result. Tycho guidance, not
a source claim: return a bounded partial result or fail under a declared rule, and cancel
outstanding work. Verify deadlines and partial results in the owner section.

**Technical owner.** [Scatter-Gather](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/messaging-families-and-durable-workflows.md#scatter-gather) — fan-out/fan-in deadline is bounded; the source states incomplete-response and timeout-ignore behavior; partial-result, failure and cancellation policy is Tycho guidance.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-scatter.2026-10-21: three H2 examples; Problem and
Solution are unheaded, and the page is publisher-abridged.
[src.aws-scatter-gather](../../../../edition/patterns/reading-ledger.v1.json)
read record read.aws-scatter-gather.2026-10-28: the Intent section defines the
broadcast-and-aggregate pattern; "Issues and considerations" states the timeout and
incomplete-response behavior; the scatter-by-auction section calls the aggregator another
messaging pattern. The sources are public documentation, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Aggregator; Splitter; Hedged Requests; API Composition.

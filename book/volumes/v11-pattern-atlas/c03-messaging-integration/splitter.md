---
metadata_version: 1
id: "tycho.page.ed3237e11d1348a7898b79b16f3244c8"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/splitter.md"
title: "Splitter"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Splitter; bounded owner evidence and limits."
route_hints:
  questions:
    - "Should a composite message be divided into independently processed parts?"
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "provider-specific split implementations"
  keywords:
    - "pattern atlas"
    - "splitter"
evidence_scope:
  source_ids:
    - "src.camel"
    - "src.spring-integration"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-28"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-28"
content_verified_at: null
---

# Splitter

**Decision.** Split only when the parts have independent effects and completion is observable:
the total count is known, or a custom release rule or expiry closes the group (Tycho guidance,
not a source claim). Keep the composite whole when the parts must be processed atomically; use
an aggregator when the work is to combine related messages into one.

**Identity.** Splitter; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should a composite message be divided into independently processed
parts?

**Good-fit conditions.** The parts are independently actionable; each part can carry a
correlation identity, a sequence position and, when known, a total size. Tycho inference:
errors can be correlated to the parent. Tycho guidance, not a source claim: a completion or
compensation rule has an owner and the fan-out is bounded.

**Hard contraindications.** Reject when the parts must be processed atomically. Tycho
guidance, not a source claim: reject when ordering across parts is mandatory and no sequencer
reconstructs it, when the split loses required context, or when no one owns completion and
orphan cleanup.

**Competing alternative.** Aggregation is the mirror-image decision: "Basically a
mirror-image of the splitter, the aggregator is a type of message handler that receives
multiple messages and combines them into a single message." Tycho synthesis: choose
aggregation when related messages must be combined rather than one composite divided;
choose single-unit processing when atomicity dominates.

**Failure and recovery.** Apache Camel's value-based watermark is only updated when the split
completes successfully; an aborted split (for example, one that exceeds `maxFailedRecords`) does
not update it, so the failed batch can be retried. Tycho guidance, not a source claim: keep
completed effects idempotent or deduplicated because a retry can re-deliver parts. The source
states that an unknown part count leaves the aggregate incomplete; a custom release rule or
expiry must close it.

**Technical owner.** [Splitter](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/splitter.md#splitter) — bounded split decision, correlation identity, sequence position, known total size and completion; provider-specific release and watermark; not a channel implementation.

**Sources.** [src.camel](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-splitter.2026-10-21: mechanism, default output and value-based
watermark retry.
[src.spring-integration](../../../../edition/patterns/reading-ledger.v1.json)
read records read.spring-splitter.2026-10-28 and read.spring-aggregator.2026-10-28:
Programming Model base-splitter headers "It is a MessageHandler implementation that
encapsulates features common to splitters, such as filling in the appropriate message headers
(CORRELATION_ID, SEQUENCE_SIZE, and SEQUENCE_NUMBER) on the messages that are produced.";
correlation identity, sequence position, completion, unknown-size release or expiry; and the
aggregator alternative.
The sources are public documentation, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Aggregator; Scatter-Gather; Pipes and Filters; Process Manager.

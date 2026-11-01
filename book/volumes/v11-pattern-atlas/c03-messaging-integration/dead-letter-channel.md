---
metadata_version: 1
id: "tycho.page.a91747aee5c745d2a503de341ea1b7f6"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/dead-letter-channel.md"
title: "Dead Letter Channel / DLQ"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Dead Letter Channel / DLQ with bounded owner evidence."
route_hints:
  questions:
    - "Should messages that cannot be processed be isolated in a dead-letter channel?"
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "dead-letter-channel-dlq"
    - "dead letter queue"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.aws-sqs-dlq"
    - "src.azure-service-bus-dlq"
    - "src.hookdeck-dlq-alternatives"
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

# Dead Letter Channel / DLQ

**Identity.** Dead Letter Channel / DLQ; family Messaging and event-driven integration;
kind messaging-pattern; priority core.

**Decision question.** Should messages that cannot be processed be isolated in a
dead-letter channel?

**Good-fit conditions.** Failure is observable; poison messages have an owner and replay
policy; retention and access are bounded; alerting is defined.

**Hard contraindications.** Reject when failures are transient and immediate retry is
safe, when no one owns the DLQ, or when dead-lettering hides a programming error.

**Competing alternative.** Bounded retry with backoff and an audit record, then alert and
stop; drop with a recorded disposition or park the work in a repair table/outbox when failure
is deterministic. Hookdeck's alternatives guide presents database persistence, a retry table and a
transactional outbox as alternatives to a DLQ; the guide is webhook-specific, so the drop
variant and general transfer are Tycho guidance. Reverse the choice for high-scale systems with
dedicated platform teams, where the guide says traditional DLQs remain a solid choice; Tycho
guidance: also reverse when replay is frequent and needs automated policy.

**Failure and recovery.** Tycho guidance: monitor DLQ growth and silent abandonment. The Azure
page states there is no automatic cleanup and messages remain until retrieved, while AWS
documents retention and redrive. Verify poison-work policy in the owner section.

**Technical owner.** [Dead Letter Channel / DLQ](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/workflow-failure.md#dead-letter-channel-dlq) — poison-work policy is bounded, not a full DLQ operations manual.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-dlq.2026-10-21, revision
`714f6babd327e622695d9be989c93c704d23b034cb2e0fcc1065a0eaa203a278`: served
problem/solution; publisher-abridged. The source is a public pattern/documentation unit,
not a benchmark.
[src.aws-sqs-dlq](../../../../edition/patterns/reading-ledger.v1.json)
read record read.aws-sqs-dlq.2026-10-30: sections "Using dead-letter queues in Amazon SQS",
"Using policies for dead-letter queues" and "Understanding message retention periods for
dead-letter queues". Exact quotes: "The maxReceiveCount is the number of times a consumer can
receive a message from a source queue before it is moved to a dead-letter queue."; "To ensure
that your system is resilient against errors, set the maxReceiveCount high enough to allow for
sufficient retries."; "Move messages out of the dead-letter queue using dead-letter queue
redrive."; "Thus, it is a best practice to always set the retention period of a dead-letter
queue to be longer than the retention period of the original queue." Revision
`c6142288904155bbd99a057145c632195aa76ab86aa939a38a9f0825f3c7e74b`. Public AWS
documentation, not a benchmark.
[src.azure-service-bus-dlq](../../../../edition/patterns/reading-ledger.v1.json)
read record read.azure-service-bus-dlq.2026-10-30: sections "The dead-letter queue", "Moving
messages to the DLQ", "Maximum delivery count" and "Application-level dead-lettering". Exact
quotes: "The purpose of the dead-letter queue is to hold messages that
can't be delivered to any receiver, or messages that couldn't be processed."; "When the
delivery count exceeds the limit, the message is moved to the DLQ."; "The following two
properties (dead-letter reason and dead-letter description) are added to dead-lettered
messages."; "There's no automatic cleanup of the DLQ. Messages remain in the DLQ until you
explicitly retrieve them from the DLQ and complete the dead-letter message." Revision
`200c9ae3c042cab7a8852b33cda0214c14b5eab177a04f2bdcc02ae665005600`. Public Microsoft Learn
documentation, not a benchmark.
[src.hookdeck-dlq-alternatives](../../../../edition/patterns/reading-ledger.v1.json)
read record read.hookdeck-dlq-alternatives.2026-10-30: sections "The Database Persistence
Pattern", "The Retry Table Pattern", "The Transactional Outbox Pattern" and "Choosing the
Right Approach". Exact quotes: "Instead of moving failed events to a separate queue, persist
them directly to a database table."; "A variation of database persistence, the retry table
pattern uses a dedicated table specifically for events that need reprocessing."; "After a
maximum number of attempts, events move to a failed state for manual review."; "The
transactional outbox pattern solves the dual-write problem."; "For high-scale systems with
dedicated platform teams, traditional DLQs remain a solid choice." Revision
`bd4ed76074e2d44f3eaa3e0b8b5f85fed27b00f6867b71e5ba21c439a239d1af`. Public vendor
engineering guide, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Retry with Exponential Backoff; Idempotent Receiver; Workflow
Failure; Audit Trail.

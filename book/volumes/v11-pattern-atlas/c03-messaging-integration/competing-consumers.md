---
metadata_version: 1
id: tycho.page.96dd39cc495bf86ca177e11db21c070d
kind: page
parent_id: tycho.chapter.a4b31346a691566550633efe0cf2693e
canonical_path: book/volumes/v11-pattern-atlas/c03-messaging-integration/competing-consumers.md
title: Competing Consumers
topic_ids:
- messaging
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Competing Consumers.
route_hints:
  questions:
  - Should multiple consumers share one queue to scale processing and smooth bursts?
  prerequisites:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  related_ids:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - competing consumers
evidence_scope:
  source_ids:
  - src.enterprise-integration
  - src.aws-sqs-visibility
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Competing Consumers

**Identity.** Competing Consumers; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should multiple consumers share one queue to scale processing and
smooth bursts?

**Good-fit conditions.** Work is independent per message; consumers can run concurrently;
ordering requirements are partition-scoped; duplicate effects are controlled.

**Hard contraindications.** Reject when global order is mandatory, when consumers mutate
shared state without coordination, or when a slow message has no bounded-attempt or terminal
path.

**Competing alternative.** One ordered consumer per partition, or a partitioned work
queue. Reverse the choice when ordering dominates throughput.

**Failure and recovery.** Concurrency increases duplicate and reorder exposure; verify
ordering and acknowledgement in the owner section.

**Technical owner.**
 [Consumer requirements and messaging
families](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#competing-consumers)
— consumer-pool ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-competing.2026-10-21: served problem/solution; publisher-abridged.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Point-to-Point Queue; Idempotent Receiver; Resequencer; Dead Letter
Channel.

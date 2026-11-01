---
metadata_version: 1
id: tycho.page.d19aade79442b34461ad8e7f26010623
kind: page
parent_id: tycho.chapter.a4b31346a691566550633efe0cf2693e
canonical_path: book/volumes/v11-pattern-atlas/c03-messaging-integration/point-to-point-queue.md
title: Point-to-Point Queue
topic_ids:
- messaging
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Point-to-Point Queue.
route_hints:
  questions:
  - Should each message be consumed by exactly one worker, rather than broadcast to
    all subscribers?
  prerequisites:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  related_ids:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - point to point queue
evidence_scope:
  source_ids:
  - src.enterprise-integration
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

# Point-to-Point Queue

**Identity.** Point-to-Point Queue; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should each message be consumed by exactly one worker, rather than
broadcast to all subscribers?

**Good-fit conditions.** Work must be divided among consumers; ordering and retry scope
are understood; one logical effect per message; the queue can express visibility and
acknowledgement.

**Hard contraindications.** Reject when every subscriber needs a copy, when strict global
ordering is required without a partition key, or when consumers cannot handle duplicates.

**Competing alternative.** Publish/subscribe fan-out. Reverse the choice when independent
subscribers need the same event rather than one shared work item.

**Failure and recovery.** Duplicate delivery and poison messages are normal; verify
acknowledgement and redelivery semantics in the owner section.

**Technical owner.**
 [Point-to-Point
Queue](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#point-to-point-queue)
— queue dispatch and acknowledgement ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-p2p.2026-10-21: served problem/solution; publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Competing Consumers; Dead Letter Channel;
Idempotent Receiver.

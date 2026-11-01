---
metadata_version: 1
id: tycho.page.4126b6f934014506cd70d1d7c50d5548
kind: page
parent_id: tycho.chapter.a4b31346a691566550633efe0cf2693e
canonical_path: book/volumes/v11-pattern-atlas/c03-messaging-integration/publish-subscribe.md
title: Publish/Subscribe
topic_ids:
- messaging
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Publish/Subscribe.
route_hints:
  questions:
  - Should one event reach all interested subscribers without the publisher knowing
    their count?
  prerequisites:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  related_ids:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - publish subscribe
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

# Publish-Subscribe

**Identity.** Publish/Subscribe; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should one event reach all interested subscribers without the
publisher knowing their count?

**Good-fit conditions.** Subscribers have independent reactions; the publisher can
tolerate fan-out; delivery and retention semantics are explicit; duplicate handling is
owned.

**Hard contraindications.** Reject when one consumer must receive every message exactly
once, when subscriber count is unknown and unbounded, or when the broker cannot express
retention and durable delivery is required.

**Competing alternative.** Point-to-point queue with explicit routing. Reverse the choice
when one work item needs one consumer, not an independent copy per subscriber.

**Failure and recovery.** Fan-out amplifies load and duplicate effects; verify retention
and acknowledgement semantics in the owner section.

**Technical owner.**
 [Publish /
Subscribe](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#publish-subscribe)
— topic/cursor delivery ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-pubsub.2026-10-21: served problem/solution; publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Point-to-Point Queue; Durable Subscriber; Event-Driven Consumer;
Competing Consumers.

---
metadata_version: 1
id: tycho.page.8d70a9b8be5fc91a07bc690ba17e4cd0
kind: page
parent_id: tycho.chapter.a4b31346a691566550633efe0cf2693e
canonical_path: book/volumes/v11-pattern-atlas/c03-messaging-integration/durable-subscriber.md
title: Durable Subscriber
topic_ids:
- messaging
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Durable Subscriber.
route_hints:
  questions:
  - Should a subscriber retain messages across temporary disconnects?
  prerequisites:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  related_ids:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - durable subscriber
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

# Durable Subscriber

**Identity.** Durable Subscriber; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should a subscriber retain messages across temporary disconnects?

**Good-fit conditions.** The subscriber can be offline; retention scope and replay are
bounded; duplicate handling exists; the broker supports durable subscriptions.

**Hard contraindications.** Reject when the subscriber is disposable, when retention would
grow without bound, or when a late replay violates a business deadline.

**Competing alternative.** Ephemeral subscription with a separate durable store. Reverse
the choice when replay cost and retention exceed the continuity benefit.

**Failure and recovery.** Retention growth and stale replay are common; verify retention
and acknowledgement in the owner section.

**Technical owner.**
 [Durable
Subscriber](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#durable-subscriber)
— durable cursor and retention ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-durable.2026-10-21: no article headings; Example is
absent and the page is publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Event-Driven Consumer; Resequencer; Claim Check.

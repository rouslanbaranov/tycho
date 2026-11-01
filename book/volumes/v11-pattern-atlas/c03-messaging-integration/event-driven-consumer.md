---
metadata_version: 1
id: tycho.page.a4ae2a47cdbeabae431df265aae2b116
kind: page
parent_id: tycho.chapter.a4b31346a691566550633efe0cf2693e
canonical_path: book/volumes/v11-pattern-atlas/c03-messaging-integration/event-driven-consumer.md
title: Event-Driven Consumer
topic_ids:
- messaging
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Event-Driven Consumer.
route_hints:
  questions:
  - Should a consumer be invoked by message arrival rather than polling on a schedule?
  prerequisites:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  related_ids:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - event driven consumer
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

# Event-Driven Consumer

**Identity.** Event-Driven Consumer; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should a consumer be invoked by message arrival rather than polling
on a schedule?

**Good-fit conditions.** Arrival latency matters; the runtime can manage subscriptions;
backpressure and failure are observable; the consumer is idempotent.

**Hard contraindications.** Reject when the consumer cannot tolerate push concurrency,
when the broker cannot express acknowledgement, or when polling gives necessary batch
control.

**Competing alternative.** Polling consumer or scheduled batch job. Reverse the choice
when event volume and concurrency overwhelm the consumer.

**Failure and recovery.** Push delivery can outrun processing; verify backpressure and
acknowledgement in the owner section.

**Technical owner.**
 [Event-Driven
Consumer](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#event-driven-consumer)
— handler delivery and acknowledgement ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-event-consumer.2026-10-21: Problem and Solution are
unheaded; only the RabbitMQ example is an H2. The page is
publisher-abridged. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Point-to-Point Queue; Competing Consumers; Durable
Subscriber.

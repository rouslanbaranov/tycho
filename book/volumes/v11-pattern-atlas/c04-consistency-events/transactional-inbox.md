---
metadata_version: 1
id: "tycho.page.c934153c2f6c4adc9d73a32c997be89a"
kind: "page"
parent_id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/transactional-inbox.md"
title: "Transactional Inbox"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Transactional Inbox; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should message identity and consumer effect be recorded atomically to
      suppress duplicates?
  prerequisites:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  related_ids:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "transactional inbox"
    - "data consistency, transactions and event sourcing"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
    - "src.microsoft-cloud-patterns"
    - "src.kafka-design"
    - "src.postgresql"
    - "src.debezium-outbox"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch2-idempotent-consumer.2026-10-21,
    read.microsoft-idempotent-consumer.2026-10-31,
    read.microsoft-transactional-outbox-cosmos.2026-10-31,
    read.kafka41-design-exactly-once.2026-10-31,
    read.postgresql-select-locking.2026-10-31 and
    read.debezium-outbox-binding.2026-10-31; owner section and limits are
    bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Transactional Inbox

**Identity.** Transactional Inbox; family Data consistency, transactions and event
sourcing; kind data-pattern; priority core.

**Decision question.** Should message identity and consumer effect be recorded atomically
to suppress duplicates?

**Good-fit conditions.** Messages carry stable identity; the effect is local; identity
retention covers redelivery; concurrent duplicates are handled.

**Hard contraindications.** Reject when the consumer is naturally idempotent, when
identity cannot be retained, or when the effect spans multiple authorities.

**Competing alternative.** A unique constraint/conditional insert on effect identity, a
producer outbox or an idempotent downstream API. Reverse when the inbox table and retention
cost exceed the duplicate-impact risk.

**Failure and recovery.** Expired identities, concurrent duplicates and at-least-once
redelivery are common; verify inbox atomicity in the owner section. A crash between the
effect and the marker can suppress or duplicate the effect, and an external send that cannot
join the local transaction needs an in-progress/completed record and reconciliation before
acknowledgement. Tycho guidance: retain the marker through the replay horizon and treat the
broker acknowledgement as a separate uncertain step.

**Technical owner.** [Inbox processing and atomic consumer effects](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/inbox-atomicity.md#3-inbox-and-consumer-local-atomicity) — inbox atomicity is bounded, not a complete idempotent-consumer recipe.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-idempotent-consumer.2026-10-21: all five served headings read.
The Microsoft Idempotent Consumer page adds the Inbox name, the same-transaction rule, the
uniqueness constraint, the consumer-scoped composite key, the crash window, the two-phase
external-effect route and the retention rule (read.microsoft-idempotent-consumer.2026-10-31,
revision f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34). Microsoft's
transactional-outbox guide states that saving the business object and its events in one
database transaction guarantees no data loss, and that change-feed reprocessing can duplicate
sends (read.microsoft-transactional-outbox-cosmos.2026-10-31, revision
6a7b566c0b088e3d95bc3fac1c4f884a9008f0258c72e07aac788499770e143e). The Kafka 4.1 Design
page states the consumer-position/offset transaction and the at-least-once default
("Kafka guarantees at-least-once delivery by default")
(read.kafka41-design-exactly-once.2026-10-31, revision
674d7c7e0516cd1f511f8692a720b3b03123e6d9567b191f181eb8cdf165503b). PostgreSQL's SELECT
page adds the SKIP LOCKED queue-like claim and its inconsistent-view warning
(read.postgresql-select-locking.2026-10-31, revision
464470632f55ed1f7b662b71e2d1b42351a0adcff0d742df245cf1d18d48dc94). Debezium's Outbox
Event Router adds the producer-side outbox and the event ID used to remove duplicates
(read.debezium-outbox-binding.2026-10-31, revision
26c1b278b6e7bd2a85787fa38064b0e9651836ca1bf1e7830df46781d9b6872e). The four-dimension
mapping, the SKIP LOCKED limitation for duplicate suppression and the producer/consumer split
are Tycho synthesis. These are public documentation units, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Idempotent Receiver; Idempotency Key; Transactional Outbox;
Deduplication.
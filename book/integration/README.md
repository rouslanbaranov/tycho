---
metadata_version: 1
id: "tycho.landing.816c847b8daa4d67a3fe1e3a8cbe3830"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/integration/README.md"
title: "Integration, messaging and stream processing"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Reader entry for Integration, messaging and stream processing. Scope includes Human and agent reading route; Canonical authored pages; Prerequisite and adjacent canonical research."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Integration, messaging and stream processing?"
  prerequisites: []
  related_ids:
    - "tycho.page.0b493340594c4c4392c5d93940a7f319"
    - "tycho.page.98616bdc3c514ea997b2cfe30ad7c070"
    - "tycho.page.a2c47a0850154eaa95e1eb97e23f9c71"
    - "tycho.page.d4822cc1e71c4f73896b7f6509f6daae"
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.7beb6ba382a1458dbfba5800ff1b53af"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Integration"
    - "messaging"
    - "and"
    - "stream"
    - "processing"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Integration, messaging and stream processing

**Status:** first three bounded research chapters for Issue [#81](https://github.com/rouslanbaranov/tycho/issues/81). Published documentation versions are explicitly recorded; no installed broker, integration benchmark or human expert review is claimed.

## Purpose and mission

Help engineers understand which **communication guarantees**, message positions, durable states and recovery semantics an integration or stream architecture actually provides. Do not choose Kafka, RabbitMQ, Pulsar, NATS or Flink from user count or vendor popularity.

## Human and agent reading route

```mermaid
flowchart TD
    Requirement["Consumer and business contract"] --> Choice{"RPC, task queue or retained event log?"}
    Choice --> Kafka["Kafka partitions, replication and offsets"]
    Choice --> Alternatives["RabbitMQ, Pulsar and NATS mechanisms"]
    Kafka --> Stateful["Stateful processing / CDC / checkpointing"]
    Alternatives --> Stateful
    Stateful --> Proof["Recovery, replay and external-effect verification"]
```

Text alternative: establish the consumer/replay requirement first, then examine Kafka or alternate messaging mechanisms, and only then evaluate stateful processing and replay correctness. No one flow is a default architectural choice.

## Canonical authored pages

| Question | Page | Public source scope |
|---|---|---|
| How are Kafka partition records, consumer offsets, ISR/replica failures and producer/Kafka transactions bounded? | [Kafka partitions and delivery contracts](../volumes/v04-distributed-coordination-and-events/c07-kafka-logs-partitions-and-transactions/kafka-partitions-replication-and-contracts.md) | Selected Apache Kafka 4.1 docs, gRPC core concepts |
| When do task queues, durable subjects/streams or long-running workflows make sense? | [Messaging families and durable workflows](../volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/messaging-families-and-durable-workflows.md) | RabbitMQ 4.3, NATS JetStream rolling docs, Pulsar 4.1 |
| How does checkpoint/replay work in stream processors, and what does CDC move across boundaries? | [Stateful processing and CDC](../volumes/v04-distributed-coordination-and-events/c08-stateful-event-time-stream-processing/stateful-stream-processing-and-cdc.md) | Kafka Streams 4.1, archived Flink 2.1, PostgreSQL 17, Debezium 3.6 |

## Prerequisite and adjacent canonical research

- [Ordering and consensus](../volumes/v04-distributed-coordination-and-events/c01-time-causality-and-ordering/causality-ordering-and-consensus.md) — what ordering and majority replication mean.
- [Saga and local isolation](../volumes/v04-distributed-coordination-and-events/c03-consistency-and-distributed-transactions/transaction-isolation-and-sagas.md) — state invariants and compensation.
- [Transactional outbox and duplicate effects](../distributed/transactional-outbox-and-idempotency.md) — source transaction/relay and consumer dedup boundary.
- [CQRS and read projections](../distributed/cqrs-event-sourcing-and-projections.md) — durable event authority versus derived state.
- [Queueing and offered load](../volumes/v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) — capacity measurements and nonstationary bursts.

## Gaps and honest readiness

Version-specific Kafka Connect operational behavior, installed gRPC client deadlines, broker deployment and recovery runbooks, cross-region replication, full streaming DSL/SQL semantics, production event-time tests, unpinned recent Flink releases and named durable workflow engines need further independent research. A documentation comparison cannot establish benchmark winners, actual exactly-once external effects or availability SLOs.

The [proposed book structure](../PROPOSED-STRUCTURE.md) owns the larger coverage plan. This landing intentionally links only to currently existing pages.

---
metadata_version: 1
id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/README.md"
title: "V11/C04 — Data consistency, transactions and event sourcing"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 14 C04 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which consistency patterns preserve the required invariants?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "data consistency, transactions and event sourcing"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.fowler-cqrs"
    - "src.microservices-patterns"
    - "src.temporal"
    - "src.ietf-idempotency-key"
    - "src.aws-idempotency"
    - "src.stripe-idempotency"
    - "src.debezium-outbox"
    - "src.postgresql"
    - "src.postgres-logical"
    - "src.oracle-distributed-transactions"
    - "src.microsoft-cloud-patterns"
    - "src.kafka-design"
    - "src.aws-cqrs"
  claim_ids: []
  status: "source-linked"
  notes: >-
    14 cards cite read units; Idempotency Key binds four; Transactional Inbox
    adds four. CDC moved to a dedicated page on 2026-10-31 with Debezium,
    PostgreSQL 18 logical decoding and replication slots, and Kafka Connect
    units; the dual-write comparison remains an unbound heuristic.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# V11/C04 — Data consistency, transactions and event sourcing

**Owning question:** Which consistency patterns preserve the required invariants?

## Purpose and mission

This chapter is the atlas entry point for **Data consistency, transactions and event
sourcing**. It owns the conditional decision route for 14 catalog entries, not the deep
mechanism explanations. Read the exact owner section before applying a mechanism claim.

All 14 entries have a self-checked card. Owner sections are bounded: a CQRS, outbox or
saga page may own the consistency contract without owning every pattern mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus a dedicated card
page for CQRS; a later split is an editorial change, not a plan failure. Start with the
card, check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Command Query Responsibility Segregation (CQRS)

See the [dedicated CQRS card](cqrs.md).

### Event Sourcing

See the [Event Sourcing](event-sourcing.md) card.

### Domain Events

See the [Domain Events](domain-events.md) card.

### Saga

See the [dedicated Saga card](saga.md).

### Saga Choreography

See the [Saga Choreography](saga-choreography.md) card.

### Saga Orchestration

See the [dedicated Saga Orchestration card](saga-orchestration.md).

### Compensating Transaction

See the [Compensating Transaction](compensating-transaction.md) card.

### Transactional Outbox

See the [dedicated Transactional Outbox card](transactional-outbox.md).

### Transactional Inbox

See the [dedicated Transactional Inbox card](transactional-inbox.md).

### Idempotency Key

See the [dedicated Idempotency Key card](idempotency-key.md).

### Change Data Capture (CDC)

See the [dedicated Change Data Capture (CDC) card](change-data-capture-cdc.md).

### Materialized View

See the [Materialized View](materialized-view.md) card.

### Command-Side Replica

See the [Command-Side Replica](command-side-replica.md) card.

### Two-Phase Commit (2PC)

See the [dedicated Two-Phase Commit (2PC) card](two-phase-commit-2pc.md).

## Chapter result and counterexample

Fourteen cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: an event-sourced system that replays external side effects without
idempotency is not evidence for the event-sourcing card's recovery conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C03](../c03-messaging-integration/README.md).
- Next: [V11/C05](../c05-caching-retrieval/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 14 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.

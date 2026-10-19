---
metadata_version: 1
id: "tycho.landing.ddbfbbbe1a85406faa2705102378beea"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/distributed/README.md"
title: "Distributed coordination, transactions and events"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "Reader entry for Distributed coordination, transactions and events. Scope includes Reading route; Canonical researched pages; Adjacent and unfinished coverage."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Distributed coordination, transactions and events?"
  prerequisites: []
  related_ids:
    - "tycho.page.1b2657011d454460856103419095031b"
    - "tycho.page.d4822cc1e71c4f73896b7f6509f6daae"
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
    - "tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f"
    - "tycho.page.aa810dd152884b35a84f0f4cbe4369e9"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.7beb6ba382a1458dbfba5800ff1b53af"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Distributed"
    - "coordination"
    - "transactions"
    - "and"
    - "events"
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

# Distributed coordination, transactions and events

**Status:** independently researched technical manuscript pages, with two distinct new V04/C04–C05 owner drafts; the distributed-systems volume is **not** complete. Source revision verification and independent domain review remain separate work. A manually curated knowledge graph is not part of Tycho infrastructure.

## Purpose and mission

Explain how causal relationships, replicated agreement, local transaction isolation, business workflows and event-based read projections work across boundaries. A client timeout, broker acknowledgement, local commit and consensus commit are different facts: the book must not imply one proves another.

## Reading route

```mermaid
flowchart TD
    Causality["Causality and ordering"] --> Consensus["Consensus / quorum limits"]
    Consensus --> Invariants["Business invariants and local isolation"]
    Invariants --> Sagas["Distributed workflow / saga compensation"]
    Sagas --> Outbox["Outbox, retries and consumer dedup"]
    Outbox --> CQRS["CQRS, event sourcing and projections"]
    CQRS --> Decisions["Evidence, recovery and applicability checks"]
```

Text alternative: understand ordering and consensus before applying transactional invariants; then investigate distributed compensations, external event delivery, duplicate effects and read-model replay. The route is for selective reading, not a universal system implementation order.

## Canonical researched pages

| Engineering question | Canonical content | Evidence state |
|---|---|---|
| What survives leader changes, minority partitions and quorum reconfiguration? | [Replication, quorum and leader change](replication-consensus-and-leader-change.md) | V04/C02; Raft/etcd public protocol scope and synthetic failure matrix; no cluster exercised |
| What is causality, and when does a replicated log need consensus? | [Causality, ordering and consensus](causality-ordering-and-consensus.md) | Lamport 1978 abstract/bibliographic record; extended Raft 2014 §§2,5. Full Lamport PDF not reviewed |
| Which invariants fit local transactions, and what does a saga compensate? | [Transaction isolation and sagas](transaction-isolation-and-sagas.md) | PostgreSQL 17 §§13.2,13.5; Richardson public saga patterns |
| How should request IDs, retries and lost acknowledgments avoid duplicate domain effects? | [Retries, idempotency and ambiguous effects](retries-idempotency-and-ambiguous-effects.md) | V04/C04; RFC 9110 and scoped idempotent-consumer reference; no tests executed |
| What can local outbox/inbox transactions and durable saga steps guarantee? | [Outbox, inbox, sagas and durable workflows](outbox-inbox-sagas-and-durable-workflows.md) | V04/C05; Debezium 3.6 and independent transactional-outbox/saga sources; not executed |
| What was the combined earlier outbox/idempotency research? | [Earlier publication and retry research](transactional-outbox-and-idempotency.md) | Preserved supporting evidence for editorial claim reconciliation; not the primary owner of either V04/C04 or C05 |
| When is an event the authority, and what does CQRS introduce? | [CQRS, event sourcing and projections](cqrs-event-sourcing-and-projections.md) | Fowler 2005/2011/2017, Richardson CQRS pattern |

All examples and Mermaid sequences are original **fictional models**; no public primary source is copied into the book. Claims are bounded by each page's explicit evidence ledger. There is no verified production system or independent expert review.

## Adjacent and unfinished coverage

Detailed Kafka partition/replication/consumer-group semantics, RabbitMQ/Pulsar/NATS delivery patterns, Flink/Streams, gRPC and durable workflow products belong to [#81](https://github.com/rouslanbaranov/tycho/issues/81) and must be researched independently. Cross-service performance is connected to [queueing](../performance/queueing-littles-law.md); service decomposition to [application styles](../application/architecture-styles-and-module-boundaries.md); safe version migration to [rollout and recovery](../delivery/safe-rollout-and-recovery.md).

The proposal for all remaining topic ownership lives in [the book structure](../PROPOSED-STRUCTURE.md). No incomplete title is a live chapter.

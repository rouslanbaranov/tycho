---
metadata_version: 1
id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v04/README.md"
title: "V04 — Distributed coordination and event integration"
topic_ids:
  - "distributed-systems"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A failure trace from request to durable state to event consumer: causal order, retry identity and transaction scope are different promises."
route_hints:
  questions:
    - "A failure trace from request to durable state to event consumer: causal order, retry identity and transaction scope are different promises."
  prerequisites:
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
    - "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
  related_ids:
    - "tycho.chapter.510c0c78de2b450c8be93d708222a488"
    - "tycho.chapter.6eba0cf391184a709f2e23e5ecc1c3d2"
    - "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
    - "tycho.chapter.24729e8d9b7247b298956ab144c15225"
    - "tycho.chapter.566e576a945b44628386d520214d6c4a"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.grpc"
    - "src.http-semantics"
    - "src.kafka-design"
    - "src.kafka-streams"
    - "src.nats"
    - "src.rabbitmq"
  claim_ids: []
  status: "source-linked"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V04 — Distributed coordination and event integration

## Purpose and mission

Describe what can and cannot be guaranteed across failure-prone boundaries.

The outcome of this volume is: A failure trace from request to durable state to event consumer: causal order, retry identity and transaction scope are different promises.

## A worked cross-chapter synthesis

A fictional booking commits locally, publishes an event and triggers an independent notification. Kill the publisher after local commit, then lose an acknowledgment after consumer processing. These two failures expose separate uncertainty windows even when the normal-path diagram contains one arrow.

Choose the invariant and authoritative commit boundary before discussing a delivery guarantee. Follow causality, replicated authority, retry identity, publication intent, receiver state and stream recovery separately. An outbox can retain publication intent; the receiver still needs a durable effect and deduplication contract within its own transaction boundary.

## Questions and chapters

| Chapter | Owning question |
|---|---|
| [V04/C01 — Time, causality and ordering](c01/README.md) | Which ordering can a distributed system observe or guarantee? |
| [V04/C02 — Replication, consensus and leader changes](c02/README.md) | Which failure assumptions sustain agreement or availability? |
| [V04/C03 — Consistency and distributed transactions](c03/README.md) | Which invariants need coordination, isolation or reconciliation? |
| [V04/C04 — Retries, idempotency and duplicate effects](c04/README.md) | Which side effects survive retries and ambiguous acknowledgements? |
| [V04/C05 — Outbox, inbox, sagas and durable workflows](c05/README.md) | How are state changes coordinated without claiming global atomicity? |
| [V04/C06 — Messaging families and delivery contracts](c06/README.md) | What are the consequences of acknowledgement, retention and consumer state? |
| [V04/C07 — Kafka logs, partitions and transactions](c07/README.md) | What do producer/consumer guarantees cover and what stays at application level? |
| [V04/C08 — Stateful/event-time stream processing](c08/README.md) | How do replay, watermarks, state stores and recovery shape correctness? |

## Choosing a reading route

For a first reading, follow the chapter order. For diagnosis, connect the observed outcome to its authority and failure boundary using: [V04/C02](c02/README.md), [V04/C03](c03/README.md), [V04/C04](c04/README.md), [V04/C05](c05/README.md), [V04/C08](c08/README.md). Return to the exact page-local source ledger before making a version-specific claim.

Prerequisite context: V02/C02, C05; V03/C03–C05.

Read [V02/C02](../v02/c02/README.md), [V02/C05](../v02/c05/README.md), [V03/C03](../v03/c03/README.md), [V03/C05](../v03/c05/README.md) for the named entry assumptions.

### Reasoning boundaries

This original conceptual map separates competing inputs rather than promising a universal solution.

~~~mermaid
flowchart TD
    Q["V04/C02 — Replication, consensus and leader changes"] --> M["V04/C03 — Consistency and distributed transactions"]
    Q --> E["Evidence and unknown inputs"]
    M --> D{"Meets the declared constraints?"}
    E --> D
    D -->|Supported| R["V04/C08 — Stateful/event-time stream processing"]
    D -->|Unresolved| U["Measure, revise or retain the baseline"]
~~~

Text alternative: establish replication, consensus and leader changes, compare consistency and distributed transactions with the available evidence, and either carry a supported result forward or return to unresolved inputs. The figure describes a reasoning route, not observed runtime behavior.

## Counterexample and handoff

Neither a total order nor a processor checkpoint automatically covers an external side effect. A delayed compensation may itself need retries and reconciliation. Carry explicit transaction, replay, retention and authority assumptions into storage design, and distinguish useful asynchronous projections from state that must never temporarily disagree.

## Navigation and source boundaries

| Route | Destination |
|---|---|
| Parent | [Book contents](../../README.md) |
| Previous volume | [V03](../v03/README.md) |
| Next volume | [V05](../v05/README.md) |
| Historical applications | [Casebook and synthetic playbooks](../../cases/README.md) |

## Evidence and known limits

The scenario is original synthetic reasoning. The chapters contain the accepted manuscript and its published evidence; no synthetic number or historical result is a measured prediction for another system. This new synthesis is editorially self-checked, not independently certified. Source-access restrictions, unexecuted technology experiments and original case denominators remain explicit in their owning pages. Product-specific adoption still requires compatible versions and the target workload.

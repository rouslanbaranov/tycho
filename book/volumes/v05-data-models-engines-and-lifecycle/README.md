---
metadata_version: 1
id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/README.md"
title: "V05 — Data models, engines and lifecycle"
topic_ids:
  - "data-architecture"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A data-authority and lifecycle model from constraint/index/WAL through partitioning, migration and verified restore; storage engine is not an architecture shortcut."
route_hints:
  questions:
    - "A data-authority and lifecycle model from constraint/index/WAL through partitioning, migration and verified restore; storage engine is not an architecture shortcut."
  prerequisites:
    - "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
  related_ids:
    - "tycho.chapter.0bf6cdc27afdb2f2494b82013d92eb73"
    - "tycho.chapter.f5df10e26e27467887ee2b22b6ce50e7"
    - "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
    - "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
    - "tycho.chapter.4a127ad6ab514ede9ff74394e5174f9c"
    - "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
    - "tycho.chapter.388c48be24414421a63481b37d05fdce"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.sqlite"
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

# V05 — Data models, engines and lifecycle

## Purpose and mission

Connect data integrity, workload, engine internals and deployment costs.

The outcome of this volume is: A data-authority and lifecycle model from constraint/index/WAL through partitioning, migration and verified restore; storage engine is not an architecture shortcut.

## A worked cross-chapter synthesis

A fictional catalogue changes schema while readers of two versions remain active. An engine accepts the new columns and an asynchronous replica is reachable, yet an older reader may misinterpret a new value and a recent acknowledged write may not be on the recovery copy.

Connect domain invariants to relational constraints and isolation, then inspect WAL, access paths, alternative stores and partition ownership. A storage decision must account for both current operations and the lifecycle of their state: migration, retention, backup membership, replay and application reconciliation.

## Questions and chapters

| Chapter | Owning question |
|---|---|
| [V05/C01 — Relational modeling and transaction isolation](c01-relational-modeling-and-transaction-isolation/README.md) | Which invariants and anomalies are relevant to the data contract? |
| [V05/C02 — PostgreSQL MVCC, WAL and recovery](c02-postgresql-mvcc-wal-and-recovery/README.md) | What are the consequences of durability, vacuum and replication mechanisms? |
| [V05/C03 — Query planning, indexes and access paths](c03-query-planning-indexes-and-access-paths/README.md) | Which read/write trade-offs explain an observed query plan? |
| [V05/C04 — Alternative data models and stores](c04-alternative-data-models-and-stores/README.md) | When are document, wide-column, KV, distributed SQL or analytical stores useful? |
| [V05/C05 — Partitioning, sharding and rebalancing](c05-partitioning-sharding-and-rebalancing/README.md) | How do hot keys, routing, joins and ownership affect scale? |
| [V05/C06 — Schema evolution, data migration and retention](c06-schema-evolution-data-migration-and-retention/README.md) | What compatibility windows and irreversibility constraints exist? |
| [V05/C07 — Replication, backups and restore drills](c07-replication-backups-and-restore-drills/README.md) | How do consistency, lag, RPO/RTO and restore evidence connect? |
| [V05/C08 — Object storage, large transfers and publication](c08-object-storage-large-transfers-and-publication/README.md) | How can large immutable payloads be transferred, published and retired without confusing bytes with business state? |

## Choosing a reading route

For a first reading, follow the chapter order. For diagnosis, connect the observed outcome to its authority and failure boundary using: [V05/C01](c01-relational-modeling-and-transaction-isolation/README.md), [V05/C03](c03-query-planning-indexes-and-access-paths/README.md), [V05/C05](c05-partitioning-sharding-and-rebalancing/README.md), [V05/C06](c06-schema-evolution-data-migration-and-retention/README.md), [V05/C07](c07-replication-backups-and-restore-drills/README.md). Return to the exact page-local source ledger before making a version-specific claim.

Prerequisite context: V04/C03–C05.

Read [V04/C03](../v04-distributed-coordination-and-events/c03-consistency-and-distributed-transactions/README.md), [V04/C04](../v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/README.md), [V04/C05](../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/README.md) for the named entry assumptions.

### Reasoning boundaries

This original conceptual map separates competing inputs rather than promising a universal solution.

~~~mermaid
flowchart TD
    Q["V05/C01 — Relational modeling and transaction isolation"] --> M["V05/C03 — Query planning, indexes and access paths"]
    Q --> E["Evidence and unknown inputs"]
    M --> D{"Meets the declared constraints?"}
    E --> D
    D -->|Supported| R["V05/C07 — Replication, backups and restore drills"]
    D -->|Unresolved| U["Measure, revise or retain the baseline"]
~~~

Text alternative: establish relational modeling and transaction isolation, compare query planning, indexes and access paths with the available evidence, and either carry a supported result forward or return to unresolved inputs. The figure describes a reasoning route, not observed runtime behavior.

## Counterexample and handoff

A replica is not a historical backup, a balanced row count is not a balanced workload, and successful DDL is not behavioral compatibility. Carry authority and freshness requirements into caching/search; those mechanisms should accelerate or project known state without silently becoming a second writer.

## Navigation and source boundaries

| Route | Destination |
|---|---|
| Parent | [Book contents](../../README.md) |
| Previous volume | [V04](../v04-distributed-coordination-and-events/README.md) |
| Next volume | [V06](../v06-caching-indexing-and-retrieval/README.md) |
| Historical applications | [Casebook and synthetic playbooks](../../cases/README.md) |

## Evidence and known limits

The scenario is original synthetic reasoning. The chapters contain the accepted manuscript and its published evidence; no synthetic number or historical result is a measured prediction for another system. This new synthesis is editorially self-checked, not independently certified. Source-access restrictions, unexecuted technology experiments and original case denominators remain explicit in their owning pages. Product-specific adoption still requires compatible versions and the target workload.

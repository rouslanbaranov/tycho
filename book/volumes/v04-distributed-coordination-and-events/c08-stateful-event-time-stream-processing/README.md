---
metadata_version: 1
id: "tycho.chapter.566e576a945b44628386d520214d6c4a"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c08-stateful-event-time-stream-processing/README.md"
title: "V04/C08 — Stateful/event-time stream processing"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do replay, watermarks, state stores and recovery shape correctness? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do replay, watermarks, state stores and recovery shape correctness?"
  prerequisites:
    - "tycho.chapter.24729e8d9b7247b298956ab144c15225"
  related_ids:
    - "tycho.page.a2c47a0850154eaa95e1eb97e23f9c71"
    - "tycho.page.54c4335d1dd142e8b794daf4768fc3d2"
    - "tycho.page.205058a4a2da4523842395cc7864c8f0"
    - "tycho.page.57478c7e1ff6443fb3f41a2f143caa9b"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.kafka-streams"
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

# V04/C08 — Stateful/event-time stream processing

## Purpose and mission

How do replay, watermarks, state stores and recovery shape correctness? This chapter owns that question within distributed coordination and event integration. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Treat event time, watermarks, retained state, checkpointing and replay as one declared processing contract.

A consistent processor checkpoint cannot recover an expired input or reverse an independently committed external effect. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](stateful-stream-processing-and-cdc.md) | How do replay, watermarks, state stores and recovery shape correctness? |
| [CDC, task state and changelog replay](cdc-state.md) | Which records make an input and local processor state recoverable? |
| [Checkpoints, watermarks and late data](checkpoints-time.md) | Which state boundary and late-data policy define a corrected result? |
| [Processor selection and recovery experiments](processor-recovery.md) | Which topology and external effect must a recovery test actually cover? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C07 — Kafka logs, partitions and transactions](../c07-kafka-logs-partitions-and-transactions/README.md) |
| Next | [V05/C01 — Relational modeling and transaction isolation](../../v05-data-models-engines-and-lifecycle/c01-relational-modeling-and-transaction-isolation/README.md) |
| Prerequisite | [V04/C07 — Kafka logs, partitions and transactions](../c07-kafka-logs-partitions-and-transactions/README.md) |
| Source reading | [Page-local evidence and versions](stateful-stream-processing-and-cdc.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.a2c47a0850154eaa95e1eb97e23f9c71:8 -->
## Source-to-claim ledger

| ID | Versioned source and examined section | Bounded support |
|---|---|---|
| E01 | [PostgreSQL 17 Logical Replication](https://www.postgresql.org/docs/17/logical-replication.html), overview/publication and subscriber introduction | A public PostgreSQL mechanism for propagating committed changes, not a specific connector's operational guarantee |
| E02 | [Debezium 3.6 Outbox Event Router](https://debezium.io/documentation/reference/3.6/transformations/outbox-event-router.html), **Basic outbox table; Basic configuration; selective transformation** | Outbox-to-Kafka routed messages, event ID/key fields and transform limitations |
| E03 | [Kafka 4.1 Streams Architecture](https://kafka.apache.org/41/streams/architecture/), tasks, parallelism, stateful processing | Task/partition relation and local state |
| E04 | [Kafka 4.1 Streams Processor API](https://kafka.apache.org/41/streams/developer-guide/processor-api/), **State Stores, Fault-tolerant State Stores** | Changelog state restoration and store mechanisms, not independent external effect exactly-once |
| E05 | [Kafka 4.1 Streams Configuration](https://kafka.apache.org/41/configuration/kafka-streams-configs/), **processing.guarantee** | Documented `at_least_once` / `exactly_once_v2` options for selected release |
| E06 | [Flink archived 2.1 Checkpoints](https://nightlies.apache.org/flink/flink-docs-release-2.1/docs/ops/state/checkpoints/), **Overview, checkpoint storage and retained checkpoints** | Managed source/operator state recovery; version is explicitly outdated |
| E07 | [Flink archived 2.1 Checkpoints vs Savepoints](https://nightlies.apache.org/flink/flink-docs-release-2.1/docs/ops/state/checkpoints_vs_savepoints/), **Overview** | Lifecycle differences; not automatically applicable to the latest Flink |

**Review state:** original technical explanation, sources restricted to the named public pages. No running stream processor, source/sink integration test, checkpoint restoration measurement, Flink 2.1 production use, independent expert review or real SLO verification.
<!-- /tycho-question-source -->

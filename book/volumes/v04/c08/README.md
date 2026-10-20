---
metadata_version: 1
id: "tycho.chapter.566e576a945b44628386d520214d6c4a"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04/c08/README.md"
title: "V04/C08 — Stateful/event-time stream processing"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do replay, watermarks, state stores and recovery shape correctness?"
route_hints:
  questions:
    - "How do replay, watermarks, state stores and recovery shape correctness?"
  prerequisites:
    - "tycho.chapter.24729e8d9b7247b298956ab144c15225"
  related_ids: []
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

| Page | Owning question |
|---|---|
| [Stateful stream processing, Kafka Streams, Flink and CDC](stateful-stream-processing-and-cdc.md) | How do replay, watermarks, state stores and recovery shape correctness? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. From a database change to a replayable input](stateful-stream-processing-and-cdc.md#1-from-a-database-change-to-a-replayable-input).
- [2. Kafka Streams: tasks, state stores and changelogs](stateful-stream-processing-and-cdc.md#2-kafka-streams-tasks-state-stores-and-changelogs).
- [Engineering walkthrough — Late correction after checkpoint and restore](stateful-stream-processing-and-cdc.md#engineering-walkthrough-late-correction-after-checkpoint-and-restore).
- [Source-to-claim ledger](stateful-stream-processing-and-cdc.md#source-to-claim-ledger).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C07 — Kafka logs, partitions and transactions](../c07/README.md) |
| Next | [V05/C01 — Relational modeling and transaction isolation](../../v05/c01/README.md) |
| Prerequisite | [V04/C07 — Kafka logs, partitions and transactions](../c07/README.md) |
| Source reading | [Page-local evidence and versions](stateful-stream-processing-and-cdc.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

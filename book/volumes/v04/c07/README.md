---
metadata_version: 1
id: "tycho.chapter.24729e8d9b7247b298956ab144c15225"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04/c07/README.md"
title: "V04/C07 — Kafka logs, partitions and transactions"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What do producer/consumer guarantees cover and what stays at application level?"
route_hints:
  questions:
    - "What do producer/consumer guarantees cover and what stays at application level?"
  prerequisites:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.grpc"
    - "src.kafka-design"
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

# V04/C07 — Kafka logs, partitions and transactions

## Purpose and mission

What do producer/consumer guarantees cover and what stays at application level? This chapter owns that question within distributed coordination and event integration. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Locate Kafka ordering and transaction guarantees within their actual partition, producer and consumer boundaries.

A transactional log operation does not automatically include a remote database or external API effect. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Integration contracts, Kafka partitions and delivery boundaries](kafka-partitions-replication-and-contracts.md) | What do producer/consumer guarantees cover and what stays at application level? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Command, query, notification and durable event are distinct contracts](kafka-partitions-replication-and-contracts.md#1-command-query-notification-and-durable-event-are-distinct-contracts).
- [2. Kafka's partition is an ordering and load unit](kafka-partitions-replication-and-contracts.md#2-kafkas-partition-is-an-ordering-and-load-unit).
- [Versioned public source-to-claim ledger](kafka-partitions-replication-and-contracts.md#versioned-public-source-to-claim-ledger).
- [Applied M9 evidence: what transfers and what does not](kafka-partitions-replication-and-contracts.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C06 — Messaging families and delivery contracts](../c06/README.md) |
| Next | [V04/C08 — Stateful/event-time stream processing](../c08/README.md) |
| Prerequisite | [V04/C06 — Messaging families and delivery contracts](../c06/README.md) |
| Source reading | [Page-local evidence and versions](kafka-partitions-replication-and-contracts.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

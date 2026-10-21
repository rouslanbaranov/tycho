---
metadata_version: 1
id: "tycho.chapter.24729e8d9b7247b298956ab144c15225"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c07-kafka-logs-partitions-and-transactions/README.md"
title: "V04/C07 — Kafka logs, partitions and transactions"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What do producer/consumer guarantees cover and what stays at application level? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What do producer/consumer guarantees cover and what stays at application level?"
  prerequisites:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  related_ids:
    - "tycho.page.0b493340594c4c4392c5d93940a7f319"
    - "tycho.page.8662ef4dfccd418f9c77cc2bc64a8c25"
    - "tycho.page.1f2f7c346c2d492290d39f45f0ad2283"
    - "tycho.page.d97d84caed7e4d9a9a285996a2dde7d8"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](kafka-partitions-replication-and-contracts.md) | What do producer/consumer guarantees cover and what stays at application level? |
| [Kafka interaction contracts and partitioning](partitions-producers.md) | What is ordered within a partition and how does its key constrain load? |
| [Replication, ISR and acknowledgment](replication-acks.md) | Which replica and acknowledgment conditions bound durability and availability? |
| [Offsets, effects and recovery](offsets-effects.md) | Which crash point separates a committed application effect from a consumer offset? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C06 — Messaging families and delivery contracts](../c06-messaging-families-and-delivery-contracts/README.md) |
| Next | [V04/C08 — Stateful/event-time stream processing](../c08-stateful-event-time-stream-processing/README.md) |
| Prerequisite | [V04/C06 — Messaging families and delivery contracts](../c06-messaging-families-and-delivery-contracts/README.md) |
| Source reading | [Page-local evidence and versions](kafka-partitions-replication-and-contracts.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.


## Further mechanism and recovery questions

- [Rebalance, external effects and expired replay positions](offsets-effects.md#rebalance-external-effects-and-expired-replay-positions) — source-scoped enrichment; examples and proposed tests are not executed results.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.0b493340594c4c4392c5d93940a7f319:7 -->
## Versioned public source-to-claim ledger

| ID | Official public source and actually inspected scope | Supported / excluded claims |
|---|---|---|
| E01 | [gRPC core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/), RPC types, metadata, deadline concepts; web documentation observed 2026-10-18 | RPC interaction semantics, **not** guaranteed durable event history |
| E02 | [Apache Kafka 4.1 Design](https://kafka.apache.org/41/design/design/), sections **The Producer / Load balancing; The Consumer / Consumer Position; Message Delivery Semantics; Using Transactions; Replication** | Kafka 4.1 topic partitions, ordering/offset/producer and replication features; **not** current-latest behavior or tested production service |
| E03 | [Kafka 4.1 Eligible Leader Replicas](https://kafka.apache.org/41/operations/eligible-leader-replicas/), **Overview** | Version-aware leader failover eligibility and min-ISR relationship; avoids implying all old assumptions hold unchanged |
| E04 | [Kafka 4.1 Kafka Streams configuration](https://kafka.apache.org/41/configuration/kafka-streams-configs/), **processing.guarantee** | Names documented processing options `at_least_once` and `exactly_once_v2`, not arbitrary external system guarantees |

Research state: original manuscript, no executed Kafka cluster, request traces, broker tuning comparison, fault-injection or independently reviewed exactly-once proof. All examples and Mermaid diagrams here are explicitly synthetic.

<!-- /tycho-question-source -->

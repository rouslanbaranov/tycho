---
metadata_version: 1
id: "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/README.md"
title: "V04/C06 — Messaging families and delivery contracts"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What are the consequences of acknowledgement, retention and consumer state? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What are the consequences of acknowledgement, retention and consumer state?"
  prerequisites:
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
  related_ids:
    - "tycho.page.98616bdc3c514ea997b2cfe30ad7c070"
    - "tycho.page.0eee61f261054af0ad728d791036c5f4"
    - "tycho.page.148a37ff87ca4e42a2fec625c65319b0"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
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

# V04/C06 — Messaging families and delivery contracts

## Purpose and mission

What are the consequences of acknowledgement, retention and consumer state? This chapter owns that question within distributed coordination and event integration. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare messaging mechanisms by acknowledgment, retention, ordering scope, consumer state and recovery behavior.

Acknowledging receipt can precede a durable application effect; delivery terminology cannot substitute for the consumer's commit contract. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](messaging-families-and-durable-workflows.md) | What are the consequences of acknowledgement, retention and consumer state? |
| [Consumer requirements and messaging families](message-selection.md) | Which ownership, retention and replay contract selects a messaging family? |
| [Workflow state and messaging failure gates](workflow-failure.md) | When does a queue need an additional durable business-state protocol? |
| [Resequencer owner note](resequencer.md) | Should out-of-order messages be buffered and released in an acceptable order? |
| [Pipes and Filters owner note](pipes-and-filters.md) | Should processing be composed as independent stages connected by a message contract? |
| [Claim Check owner note](claim-check.md) | Should a large or sensitive payload travel outside the message and be retrieved through a claim check? |
| [Request-Reply Messaging owner note](request-reply-messaging.md) | Should a request and response travel as a pair of messages on separate channels? |
| [Splitter owner note](splitter.md) | Should a composite message be divided into independently processed parts? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C05 — Outbox, inbox, sagas and durable workflows](../c05-outbox-inbox-sagas-and-durable-workflows/README.md) |
| Next | [V04/C07 — Kafka logs, partitions and transactions](../c07-kafka-logs-partitions-and-transactions/README.md) |
| Prerequisite | [V04/C05 — Outbox, inbox, sagas and durable workflows](../c05-outbox-inbox-sagas-and-durable-workflows/README.md) |
| Source reading | [Page-local evidence and versions](messaging-families-and-durable-workflows.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.


## Further mechanism and recovery questions

- [Scheduled runs, durable timers and poison-work recovery](workflow-failure.md#scheduled-runs-durable-timers-and-poison-work-recovery) — source-scoped enrichment; examples and proposed tests are not executed results.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.98616bdc3c514ea997b2cfe30ad7c070:5 -->
## Public evidence and review scope

| ID | Official public source (observed version) and exact inspected section | Supports / does not prove |
|---|---|---|
| E01 | [RabbitMQ 4.3 Reliability Guide](https://www.rabbitmq.com/docs/reliability), *Data Safety, Clustering and Queue Content Replication* | Acks, confirms and replicated queue roles, not actual application end-to-end exactly-once |
| E02 | [RabbitMQ 4.3 Consumer Acknowledgements and Publisher Confirms](https://www.rabbitmq.com/docs/confirms), *The Basics, Publisher Confirms, Consumer Acknowledgements* | Publisher/consumer ack independence and recovery hazards |
| E03 | [NATS JetStream](https://docs.nats.io/concepts/jetstream), *How It Works, Streams, Consumers*, accessed 2026-10-18 (rolling site) | Core vs JetStream durable state and redelivery, not pinned server binary behavior |
| E04 | [Apache Pulsar 4.1 Architecture Overview](https://pulsar.apache.org/docs/4.1.x/concepts-architecture-overview/), *Brokers, Persistent storage* | Broker/BookKeeper architecture, not test results or ranking |
| E05 | [RabbitMQ quorum queues](https://www.rabbitmq.com/docs/quorum-queues), *When Not to Use Quorum Queues* | Documented contraindications and durability trade-offs, version observed 4.3 |

**Review state:** bounded documentation comparison, synthetic illustrations only. No software installed, measurements collected, benchmark conducted, broker disaster recovery rehearsed, full product alternatives researched or external domain review completed.

<!-- /tycho-question-source -->

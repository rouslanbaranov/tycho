---
metadata_version: 1
id: "tycho.page.0b493340594c4c4392c5d93940a7f319"
kind: "page"
parent_id: "tycho.chapter.24729e8d9b7247b298956ab144c15225"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c07-kafka-logs-partitions-and-transactions/kafka-partitions-replication-and-contracts.md"
title: "Integration contracts, Kafka partitions and delivery boundaries"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Kafka logs, partitions and transactions. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What do producer/consumer guarantees cover and what stays at application level?"
  prerequisites: []
  related_ids:
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.8662ef4dfccd418f9c77cc2bc64a8c25"
    - "tycho.page.1f2f7c346c2d492290d39f45f0ad2283"
    - "tycho.page.d97d84caed7e4d9a9a285996a2dde7d8"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Integration"
    - "contracts"
    - "Kafka"
    - "partitions"
    - "and"
    - "delivery"
    - "boundaries"
evidence_scope:
  source_ids:
    - "src.grpc"
    - "src.kafka-design"
  claim_ids: []
  status: "source-linked"
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
<!-- tycho-question-source:tycho.page.0b493340594c4c4392c5d93940a7f319:-1 -->

# Integration contracts, Kafka partitions and delivery boundaries

> Technical research for Tycho [#81](https://github.com/rouslanbaranov/tycho/issues/81), proposed V04/C06–C07. Source inspection **2026-10-18**, explicitly anchored to **Apache Kafka 4.1 documentation**. Version 4.1 is a selected **older documentation release**, not a claim that it is the newest. Examples and diagrams are original synthetic scenarios, not executed benchmarks or proof of external exactly-once effects.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0b493340594c4c4392c5d93940a7f319:0 -->
## Purpose and mission

A reliable integration must make clear **who owns state, what is a command versus a fact, where a message is persisted, how ordering is scoped and when a consumer's external effect is durable**. A service API, an event stream and a task queue solve different requirements; Kafka has specific mechanics, not general-purpose magic "exactly once".

**Primary question:** How do Kafka's partitions, leaders, ISR, offsets, consumer groups and transactional producer/Streams contracts compose—and what happens when an acknowledgment or consumer fails?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0b493340594c4c4392c5d93940a7f319:8 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [LinkedIn — Kafka tiers](../../../cases/linkedin-kafka-tiered-completeness.md)**. **Relevant mechanism or architectural contrast:** Kafka broker health and acknowledged writes do not substitute for end-to-end tier/consumer completeness audits. **Not established by this report/playbook:** Historical LinkedIn tier scale and audit numbers do not establish universal Kafka exactly-once external effects.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Locate Kafka ordering and transaction guarantees within their actual partition, producer and consumer boundaries.

A transactional log operation does not automatically include a remote database or external API effect.

The detailed pages separate the mechanisms that make this decision conditional:

- [Kafka interaction contracts and partitioning](partitions-producers.md) — What is ordered within a partition and how does its key constrain load?
- [Replication, ISR and acknowledgment](replication-acks.md) — Which replica and acknowledgment conditions bound durability and availability?
- [Offsets, effects and recovery](offsets-effects.md) — Which crash point separates a committed application effect from a consumer offset?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

---
metadata_version: 1
id: "tycho.page.98616bdc3c514ea997b2cfe30ad7c070"
kind: "page"
parent_id: "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/messaging-families-and-durable-workflows.md"
title: "Messaging families: RabbitMQ, Pulsar, NATS and durable workflows"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Messaging families and delivery contracts. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What are the consequences of acknowledgement, retention and consumer state?"
  prerequisites: []
  related_ids:
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
    - "tycho.page.0eee61f261054af0ad728d791036c5f4"
    - "tycho.page.148a37ff87ca4e42a2fec625c65319b0"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Messaging"
    - "families"
    - "RabbitMQ"
    - "Pulsar"
    - "NATS"
    - "and"
    - "durable"
    - "workflows"
evidence_scope:
  source_ids:
    - "src.nats"
    - "src.rabbitmq"
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
<!-- tycho-question-source:tycho.page.98616bdc3c514ea997b2cfe30ad7c070:-1 -->

# Messaging families: RabbitMQ, Pulsar, NATS and durable workflows

> Tycho Issue [#81](https://github.com/rouslanbaranov/tycho/issues/81), proposed V04/C06. Public documentation inspected on 2026-10-18; versions indicated per vendor. Original conceptual comparisons and synthetic diagrams, **not** a benchmark or generic product ranking.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.98616bdc3c514ea997b2cfe30ad7c070:0 -->
## Purpose and mission

A messaging decision is about the **observable consumer contract**, not a feature-comparison checkbox. Transient subjects, durable work queues, replicated partitioned logs and independently replayable consumer views have distinct state/ack/recovery behavior.

**Primary question:** Under what workload, ownership, replay and failure constraints do RabbitMQ quorum queues, Pulsar, NATS Core/JetStream or Kafka-style logs make an appropriate candidate—and when is a managed durable workflow needed instead of ordinary message transport?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.98616bdc3c514ea997b2cfe30ad7c070:6 -->
## Engineering walkthrough — Work queue versus ephemeral fan-out versus replayable history

**Synthetic requirement triad:** an order system needs (A) a transient dashboard refresh, (B) a durable image-processing job and (C) an audit-replayable history of order transitions. They do not require the same message transport. A broker feature list without consumer durability, ordering key, retention and acknowledgment semantics is insufficient.

| Demand | Plausible mechanism | Negative case and recovery |
|---|---|---|
| Dashboard may lose interim updates | Ephemeral publish/subscribe or state snapshot feed | Disconnected subscriber gets current snapshot; no invented replay promise |
| Job must eventually complete or be classified failed | Work queue with persistent acceptance and explicit ack/nack / redelivery policy | Worker commits effect then crashes before ack; durable job/effect identity suppresses repeats |
| Auditor must rebuild ordered state transitions | Retained per-key log with offset and replay horizon | Consumer lags beyond retention or key-order scope; declare gap and restore authoritative snapshot |

RabbitMQ quorum queues, NATS JetStream and Pulsar expose different storage/consumer controls under their documented versions; "NATS" without saying Core NATS or JetStream obscures durability. No general broker makes a non-transactional external payment exactly once. A durable workflow adds step identity, state, deadlines and human repair responsibilities beyond queuing one message.

**Proposed test, not run:** disconnect a dashboard, kill a job worker after its database commit, truncate replay history at a declared horizon and restart a consumer across a partition change. Acceptance is per-use-case: no unjustified data replay claim for the dashboard, one logical job effect for work, and declared completeness/recovery for audit. For a small single-transaction process, a local durable table and worker may be less complex than a distributed broker family.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.98616bdc3c514ea997b2cfe30ad7c070:7 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Cloudflare — Super Slurper queues](../../../cases/cloudflare-super-slurper-queues.md)**. **Relevant mechanism or architectural contrast:** At-least-once queue workers need durable progress and explicit dedup boundaries during object import. **Not established by this report/playbook:** A company fivefold result has a particular workload and baseline; it does not prove queue use always increases throughput.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Compare messaging mechanisms by acknowledgment, retention, ordering scope, consumer state and recovery behavior.

Acknowledging receipt can precede a durable application effect; delivery terminology cannot substitute for the consumer's commit contract.

The detailed pages separate the mechanisms that make this decision conditional:

- [Consumer requirements and messaging families](message-selection.md) — Which ownership, retention and replay contract selects a messaging family?
- [Workflow state and messaging failure gates](workflow-failure.md) — When does a queue need an additional durable business-state protocol?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

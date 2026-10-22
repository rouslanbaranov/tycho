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

> **Pattern atlas:**
> [Request-Reply Messaging](../../v11-pattern-atlas/c03-messaging-integration/README.md#request-reply-messaging) — decision conditions and contraindications.
> [Splitter](../../v11-pattern-atlas/c03-messaging-integration/README.md#splitter) — decision conditions and contraindications.
> [Aggregator](../../v11-pattern-atlas/c03-messaging-integration/README.md#aggregator) — decision conditions and contraindications.
> [Scatter-Gather](../../v11-pattern-atlas/c03-messaging-integration/README.md#scatter-gather) — decision conditions and contraindications.

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

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is
not the main subject of this page. They are synthetic design guidance, not
measured evidence, and they do not create a new source claim.

### Aggregator

An aggregator fans in related results from multiple participants and returns one composed
result. It needs correlation, a per-participant timeout, a partial-failure policy and a
rule for late or duplicate responses. Use it when callers need one response and the
participants can be queried independently. Do not use it when one participant is
authoritative, when atomicity across participants is required, or when one slow
participant would consume the caller complete budget.

**Limits.** Per-participant state, duplicate responses and cancellation are costs; a partial
result needs a versioned schema and a caller-visible completeness marker.

The failure path is a stuck or missing participant; the aggregator must return a declared
partial result, cancel remaining work or fail as a whole. Client-side composition is the
alternative when the caller can tolerate multiple responses.

### Splitter

A splitter turns one input into several independently processable messages. It needs
stable partition identity, per-part idempotency, a completion or compensation rule and a
bounded fan-out. Use it when downstream steps can make progress independently and partial
completion is meaningful. Do not use it when the whole input must succeed atomically or
when downstream ordering cannot be reconstructed.

**Limits.** Fan-out multiplies message volume, tracking state and partial-failure cleanup; a
split with no completion marker leaks orphaned work and needs an owner.

The failure path is a split that produces only some parts; record part identity and
completion, then retry missing parts without duplicating completed effects. A single
consumer with internal fan-out is the alternative when the parts are small and atomicity
is required.

### Scatter-Gather

Scatter-gather sends one request to several participants and gathers their responses. It
needs a response contract, a quorum or completeness rule, a deadline and a policy for
stragglers. Use it when independent participants can answer the same question and a
partial view is useful. Do not use it when one authority must answer, when responses are
not comparable, or when tail latency would exceed the caller budget.

The failure path is a slow or missing participant; gather must return a bounded partial
result or fail under a declared rule, and cancel outstanding work. A single authoritative
call is the alternative when consistency matters more than coverage.

**Limits.** Fan-out cost and tail latency grow with participants; a quorum result must name
which participants answered and which did not.

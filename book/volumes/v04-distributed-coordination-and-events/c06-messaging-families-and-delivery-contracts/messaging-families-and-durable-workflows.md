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
    - "src.enterprise-integration"
    - "src.aws-scatter-gather"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-30"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.98616bdc3c514ea997b2cfe30ad7c070:-1 -->

# Messaging families: RabbitMQ, Pulsar, NATS and durable workflows

> Tycho Issue [#81](https://github.com/rouslanbaranov/tycho/issues/81), proposed V04/C06. Public documentation inspected on 2026-10-18; versions indicated per vendor. Original conceptual comparisons and synthetic diagrams, **not** a benchmark or generic product ranking.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Request-Reply Messaging](../../v11-pattern-atlas/c03-messaging-integration/request-reply-messaging.md#request-reply-messaging) — decision conditions and contraindications.
> [Splitter](../../v11-pattern-atlas/c03-messaging-integration/splitter.md#splitter) — decision conditions and contraindications.
> [Aggregator](../../v11-pattern-atlas/c03-messaging-integration/aggregator.md#aggregator) — decision conditions and contraindications.
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
measured evidence; the Aggregator and Scatter-Gather alternatives carry
separate source bindings recorded in their cards and owner units.

### Aggregator

An aggregator fans in related results from multiple participants and returns one composed
result. It needs correlation, a completeness condition and an aggregation algorithm.
Tycho guidance, not a source claim: add a per-participant timeout, a partial-failure
policy and a rule for late or duplicate responses. Define the expected participant set, a
completion rule (all or quorum), and eviction of late responses. Use it when callers need
one response and the participants can be queried independently. Tycho guidance: do not use
it when one participant is authoritative, when atomicity across participants is required,
or when one slow participant would consume the caller's complete budget.

**Failure and recovery.** The source states: "A single missing or delayed message will
prevent further processing of the whole aggregate." Recovery is bounded: "One way to deal with
missing messages is to re-request the message."
and, for a timeout strategy, "If no responses are received, the system may report an
exception or retry."
Tycho guidance, not a source claim: return a declared partial result, cancel remaining
work or fail as a whole.

**Alternative.** Tycho synthesis: API composition is the alternative when the caller can
invoke the data-owning services and join their responses at query time. The source defines
an API Composer that invokes those services and "performs an in-memory join of the
results." The source does not compare API composition with aggregator; the comparison and
reversal are Tycho synthesis. Reverse the choice when the related results already arrive
as messages and completion must trigger the combined result. Scatter-gather is a related
composite, not this alternative: it broadcasts a request and uses an aggregator as its
gather step.

**Limits.** Per-participant state, duplicate responses and cancellation are costs; a
partial result needs a versioned schema and a caller-visible completeness marker.

**Source boundary.** Enterprise Integration Patterns,
[Aggregator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html),
section "Aggregator", read 2026-11-01; canonical text SHA-256
`e1c4a2c4cef8a220390b9bab78851e35d9d473bee3dd0c3e0e2f7f84e925c494` (raw HTML
`15d8640d5ad149a0e54a23c4cfe4a84c0abdcec421de2f9eb301daf21d708f58`). microservices.io,
[API Composition](https://microservices.io/patterns/data/api-composition.html), sections
"Solution" and "Resulting context", read 2026-11-01; canonical text SHA-256
`75fae4c75e4c6d5cc8084bd4a4ecec5fed6aaf9a1816437cecf4950e0d82b4b7` (raw HTML
`7ec014c171b2421f216c3a82ddb60af0104a2f38e6bb3af93e93c8065f04750b`). The pages are
living documents; no benchmark or execution was performed. The partial-result and
cancellation rules, the API-composition comparison and the reversal are Tycho synthesis,
not source statements.

### Splitter

See the [dedicated Splitter owner note](splitter.md).

### Scatter-Gather

Scatter-gather sends one request to several participants and gathers their responses. It
needs a completeness condition and a deadline; the source names wait-for-all, first-best
and fixed-timeout strategies. Tycho guidance, not a source claim: define a response
contract, a quorum or completeness rule, a deadline and a policy for stragglers. Assign a
per-recipient deadline and a correlation key; accept at most one reply per recipient. Use
it when independent participants can answer the same question and a partial view is
useful. Tycho guidance: do not use it when one authority must answer, when responses are
not comparable, or when tail latency would exceed the caller's budget.

**Failure and recovery.** The AWS Prescriptive Guidance page's "Partial responses"
consideration states: "When requests are scattered to multiple recipients, some recipients
can time out. In these cases, the implementation should communicate to the client that the
response is incomplete." Its scatter-by-distribution description adds that the controller
"can configure a timeout parameter to ignore responses that take too long", that "The
responses that time out are ignored" and that "The aggregator combines the partial
responses and returns the final result to the client." These sentences support timeout
handling, a client-visible incomplete response, ignoring late responses and combining
partial responses into a returned result. Tycho guidance, not a source claim: gather should
return a bounded partial result or fail under a declared rule, and cancel outstanding work.

**Alternative.** The same page describes the aggregator as "another messaging pattern" and
states: "Because the root controller isn't aware of the recipients, the gathering process
uses an aggregator (another messaging pattern) to collect the responses and distill them
into a single response message." That supports a message-aggregation comparison, not a
standalone alternative: the aggregator is the gather component inside scatter-gather.
Tycho synthesis: an aggregator alone is the alternative when responses already exist and
no broadcast is needed; reverse the choice when only already-produced responses must be
combined.

**Limits.** Fan-out cost and tail latency grow with participants; a quorum result must name
which participants answered and which did not.

**Source boundary.** AWS Prescriptive Guidance, "Scatter-gather pattern", read 2026-10-30;
canonical text SHA-256
`4b5c777b08c089f6753dc3f5743627d17a35720b7bc1e5fecaae69c31f64fda3`; sections "Issues and
considerations", "Scatter by distribution (overview)" and "Scatter by auction (overview)".
The page is a living document; no benchmark or execution was performed. The standalone
aggregator alternative and the bounded partial-result, failure and cancellation rules are
Tycho guidance, not AWS statements.

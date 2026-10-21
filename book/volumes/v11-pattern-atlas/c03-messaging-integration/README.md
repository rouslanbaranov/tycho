---
metadata_version: 1
id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/README.md"
title: "V11/C03 — Messaging and event-driven integration"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 20 C03 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which messaging pattern fits the delivery and ownership contract?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "messaging integration"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.camel"
  claim_ids: []
  status: "source-linked"
  notes: "All 20 cards cite read units; owner links are bounded sections, not dedicated EIP pages."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-21"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# V11/C03 — Messaging and event-driven integration

**Owning question:** Which messaging pattern fits the delivery and ownership contract?

## Purpose and mission

This chapter is the atlas entry point for **Messaging and event-driven integration**.
It owns the conditional decision route for 20 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 20 entries have a self-checked card. Owner sections are bounded: a messaging-family
or workflow page may own the delivery contract without owning every EIP mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Publish / Subscribe

**Identity.** Publish/Subscribe; family Messaging and event-driven integration; kind messaging-pattern; priority core.

**Decision question.** Should one event reach all interested subscribers without the publisher knowing their count?

**Good-fit conditions.** Subscribers have independent reactions; the publisher can tolerate fan-out; delivery and retention semantics are explicit; duplicate handling is owned.

**Hard contraindications.** Reject when one consumer must receive every message exactly once, when subscriber count is unknown and unbounded, or when the broker cannot express retention.

**Competing alternative.** Point-to-point queue with explicit routing. Reverse the choice when every subscriber needs the same durable work, not an independent copy.

**Failure and recovery.** Fan-out amplifies load and duplicate effects; verify retention and acknowledgement semantics in the owner section.

**Technical owner.** [Consumer requirements and messaging families](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#consumer-requirements-and-messaging-families) — consumer ownership is the bounded owner, not a dedicated channel page.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-pubsub.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Point-to-Point Queue; Durable Subscriber; Event-Driven Consumer; Competing Consumers.

### Point-to-Point Queue

**Identity.** Point-to-Point Queue; family Messaging and event-driven integration; kind messaging-pattern; priority core.

**Decision question.** Should each message be consumed by exactly one worker, rather than broadcast to all subscribers?

**Good-fit conditions.** Work must be divided among consumers; ordering and retry scope are understood; one logical effect per message; the queue can express visibility and acknowledgement.

**Hard contraindications.** Reject when every subscriber needs a copy, when strict global ordering is required without a partition key, or when consumers cannot handle duplicates.

**Competing alternative.** Publish/subscribe fan-out. Reverse the choice when independent subscribers need the same event rather than one shared work item.

**Failure and recovery.** Duplicate delivery and poison messages are normal; verify acknowledgement and redelivery semantics in the owner section.

**Technical owner.** [Consumer requirements and messaging families](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#consumer-requirements-and-messaging-families) — consumer ownership is the bounded owner, not a dedicated channel page.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-p2p.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Competing Consumers; Dead Letter Channel; Idempotent Receiver.

### Competing Consumers

**Identity.** Competing Consumers; family Messaging and event-driven integration; kind messaging-pattern; priority core.

**Decision question.** Should multiple consumers share one queue to scale processing and smooth bursts?

**Good-fit conditions.** Work is independent per message; consumers can run concurrently; ordering requirements are partition-scoped; duplicate effects are controlled.

**Hard contraindications.** Reject when global order is mandatory, when consumers mutate shared state without coordination, or when one slow message blocks the queue head.

**Competing alternative.** One ordered consumer per partition, or a partitioned work queue. Reverse the choice when ordering dominates throughput.

**Failure and recovery.** Concurrency increases duplicate and reorder exposure; verify ordering and acknowledgement in the owner section.

**Technical owner.** [Consumer requirements and messaging families](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#consumer-requirements-and-messaging-families) — consumer ownership is the bounded owner, not a dedicated channel page.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-competing.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Point-to-Point Queue; Idempotent Receiver; Resequencer; Dead Letter Channel.

### Event-Driven Consumer

**Identity.** Event-Driven Consumer; family Messaging and event-driven integration; kind messaging-pattern; priority core.

**Decision question.** Should a consumer be invoked by message arrival rather than polling on a schedule?

**Good-fit conditions.** Arrival latency matters; the runtime can manage subscriptions; backpressure and failure are observable; the consumer is idempotent.

**Hard contraindications.** Reject when the consumer cannot tolerate push concurrency, when the broker cannot express acknowledgement, or when polling gives necessary batch control.

**Competing alternative.** Polling consumer or scheduled batch job. Reverse the choice when event volume and concurrency overwhelm the consumer.

**Failure and recovery.** Push delivery can outrun processing; verify backpressure and acknowledgement in the owner section.

**Technical owner.** [Consumer requirements and messaging families](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#consumer-requirements-and-messaging-families) — consumer ownership is the bounded owner, not a dedicated channel page.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-event-consumer.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Point-to-Point Queue; Competing Consumers; Durable Subscriber.

### Request-Reply Messaging

**Identity.** Request-Reply Messaging; family Messaging and event-driven integration; kind integration-pattern; priority core.

**Decision question.** Should a request and its response travel as correlated messages rather than one synchronous call?

**Good-fit conditions.** The caller can tolerate asynchronous completion; a reply channel and correlation are available; timeouts and lost replies are handled.

**Hard contraindications.** Reject when the caller needs an immediate answer, when no durable reply path exists, or when correlation state has no owner.

**Competing alternative.** Synchronous request-reply with a bounded deadline. Reverse the choice when asynchronous coordination adds more failure modes than latency benefit.

**Failure and recovery.** Lost replies and duplicate requests are normal; verify correlation and timeout handling in the owner section.

**Technical owner.** [A durable workflow is more than a queue](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/workflow-failure.md#3-a-durable-workflow-is-more-than-a-queue) — workflow failure gates are bounded, not a complete request-reply contract.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-request-reply.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Correlation Identifier; Asynchronous Request-Reply; API Gateway; Timeout.

### Correlation Identifier

**Identity.** Correlation Identifier; family Messaging and event-driven integration; kind integration-pattern; priority core.

**Decision question.** Should related messages carry an explicit identifier so replies and follow-ups can be matched?

**Good-fit conditions.** Flows span multiple messages or services; the identifier is stable per logical operation; retention and collision policy are defined.

**Hard contraindications.** Reject when one synchronous call carries the whole exchange, when identifiers are reused across operations, or when the receiver cannot retain correlation state.

**Competing alternative.** Transport-level request IDs only, or a synchronous call. Reverse the choice when correlation state and retention cost exceed the routing benefit.

**Failure and recovery.** Identifier collisions or premature expiry break matching; verify scope and retention in the owner section.

**Technical owner.** [A durable workflow is more than a queue](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/workflow-failure.md#3-a-durable-workflow-is-more-than-a-queue) — workflow failure gates are bounded, not a complete request-reply contract.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-correlation.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Request-Reply Messaging; Idempotency Key; Distributed Tracing; Process Manager.

### Content-Based Router

**Identity.** Content-Based Router; family Messaging and event-driven integration; kind integration-pattern; priority core.

**Decision question.** Should routing be decided from message content rather than a fixed destination?

**Good-fit conditions.** Routing rules are explicit and testable; message content is trustworthy; rule changes can be versioned; the router can expose unmatched messages.

**Hard contraindications.** Reject when a fixed route suffices, when routing depends on untrusted fields, or when rules become domain workflow without ownership.

**Competing alternative.** Static routing or a workflow/orchestrator. Reverse the choice when content rules become a hidden process engine.

**Failure and recovery.** Rule drift and unmatched messages are common; verify rule ownership and fallback in the owner section.

**Technical owner.** [Requirement-driven comparison, not a ranking](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#2-requirement-driven-comparison-not-a-ranking) — the comparison section is bounded; it does not own every EIP mechanism.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-cbr.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Message Filter; Pipes and Filters; Process Manager; Message Broker.

### Message Filter

**Identity.** Message Filter; family Messaging and event-driven integration; kind integration-pattern; priority advanced.

**Decision question.** Should messages be removed when they do not meet explicit criteria?

**Good-fit conditions.** Filter criteria are stable and testable; rejected messages have a defined disposition; filtering is cheaper than downstream handling.

**Hard contraindications.** Reject when every message has a required effect, when rejected messages need durable audit without an owner, or when criteria depend on mutable domain state.

**Competing alternative.** Route all messages and let the consumer decide. Reverse the choice when downstream cost dominates and rejection is safe.

**Failure and recovery.** Silent loss is the main risk; verify rejected-message policy in the owner section.

**Technical owner.** [Requirement-driven comparison, not a ranking](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#2-requirement-driven-comparison-not-a-ranking) — the comparison section is bounded; it does not own every EIP mechanism.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-filter.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Content-Based Router; Dead Letter Channel; Pipes and Filters; Audit Trail.

### Pipes and Filters

**Identity.** Pipes and Filters; family Messaging and event-driven integration; kind integration-pattern; priority advanced.

**Decision question.** Should processing be composed as independent stages connected by channels?

**Good-fit conditions.** Stages have distinct responsibilities; intermediate messages can be observed; each stage can fail and retry independently; ordering requirements are explicit.

**Hard contraindications.** Reject when one stage needs global transaction state, when intermediate latency is unacceptable, or when the pipeline becomes an unowned distributed workflow.

**Competing alternative.** One cohesive consumer with internal functions. Reverse the choice when stage isolation and reuse no longer justify message hops.

**Failure and recovery.** Partial failure and duplicate processing grow with stages; verify stage contracts in the owner section.

**Technical owner.** [Requirement-driven comparison, not a ranking](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#2-requirement-driven-comparison-not-a-ranking) — the comparison section is bounded; it does not own every EIP mechanism.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-pipes.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Splitter; Aggregator; Content-Based Router; Process Manager.

### Splitter

**Identity.** Splitter; family Messaging and event-driven integration; kind integration-pattern; priority advanced.

**Decision question.** Should a composite message be divided into independently processed parts?

**Good-fit conditions.** The parts are independently actionable; aggregation or completion policy is defined; each part has an identity; errors can be correlated.

**Hard contraindications.** Reject when the parts must be processed atomically, when ordering across parts is mandatory without a coordinator, or when the split loses required context.

**Competing alternative.** Process the composite as one unit. Reverse the choice when independent processing creates more coordination than value.

**Failure and recovery.** Partial completion and orphaned parts are common; verify aggregation and error policy in the owner section.

**Technical owner.** [Work queue versus ephemeral fan-out versus replayable history](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/messaging-families-and-durable-workflows.md#engineering-walkthrough-work-queue-versus-ephemeral-fan-out-versus-replayable-history) — the walkthrough owns fan-out/history trade-offs, not a dedicated splitter/aggregator page.

**Sources.** [src.camel](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-splitter.2026-10-21: sections "Split", "Options". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Aggregator; Scatter-Gather; Pipes and Filters; Process Manager.

### Aggregator

**Identity.** Aggregator; family Messaging and event-driven integration; kind integration-pattern; priority advanced.

**Decision question.** Should related messages be combined using completion and timeout rules?

**Good-fit conditions.** Correlation is stable; completion conditions are explicit; partial results are representable; duplicate and late messages are handled.

**Hard contraindications.** Reject when responses are independent, when no bounded completion rule exists, or when aggregation state has no durable owner.

**Competing alternative.** Process each response independently. Reverse the choice when aggregation state and timeout complexity exceed the combined result benefit.

**Failure and recovery.** Late, missing and duplicate messages are common; verify completion and eviction in the owner section.

**Technical owner.** [Work queue versus ephemeral fan-out versus replayable history](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/messaging-families-and-durable-workflows.md#engineering-walkthrough-work-queue-versus-ephemeral-fan-out-versus-replayable-history) — the walkthrough owns fan-out/history trade-offs, not a dedicated splitter/aggregator page.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-aggregator.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Splitter; Scatter-Gather; Correlation Identifier; Resequencer.

### Scatter-Gather

**Identity.** Scatter-Gather; family Messaging and event-driven integration; kind integration-pattern; priority advanced.

**Decision question.** Should one request be broadcast to several recipients and their responses combined?

**Good-fit conditions.** Recipients are known or discoverable; partial responses are acceptable; per-recipient deadlines exist; the aggregate is bounded.

**Hard contraindications.** Reject when one authoritative recipient suffices, when all responses must be globally consistent, or when fan-out can exhaust the caller.

**Competing alternative.** Single recipient or sequential calls. Reverse the choice when latency benefit is outweighed by fan-out and partial-failure cost.

**Failure and recovery.** Slow or missing recipients dominate tail latency; verify deadlines and partial results in the owner section.

**Technical owner.** [Work queue versus ephemeral fan-out versus replayable history](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/messaging-families-and-durable-workflows.md#engineering-walkthrough-work-queue-versus-ephemeral-fan-out-versus-replayable-history) — the walkthrough owns fan-out/history trade-offs, not a dedicated splitter/aggregator page.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-scatter.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Aggregator; Splitter; Hedged Requests; API Composition.

### Dead Letter Channel / DLQ

**Identity.** Dead Letter Channel / DLQ; family Messaging and event-driven integration; kind messaging-pattern; priority core.

**Decision question.** Should messages that cannot be processed be isolated in a dead-letter channel?

**Good-fit conditions.** Failure is observable; poison messages have an owner and replay policy; retention and access are bounded; alerting is defined.

**Hard contraindications.** Reject when failures are transient and immediate retry is safe, when no one owns the DLQ, or when dead-lettering hides a programming error.

**Competing alternative.** Bounded retry with backoff, then alert and stop. Reverse the choice when replay is frequent and needs automated policy.

**Failure and recovery.** DLQ growth and silent abandonment are common; verify poison-work policy in the owner section.

**Technical owner.** [Poison work is a policy state](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/workflow-failure.md#poison-work-is-a-policy-state) — poison-work policy is bounded, not a full DLQ operations manual.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-dlq.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Retry with Exponential Backoff; Idempotent Receiver; Workflow Failure; Audit Trail.

### Durable Subscriber

**Identity.** Durable Subscriber; family Messaging and event-driven integration; kind messaging-pattern; priority advanced.

**Decision question.** Should a subscriber retain messages across temporary disconnects?

**Good-fit conditions.** The subscriber can be offline; retention scope and replay are bounded; duplicate handling exists; the broker supports durable subscriptions.

**Hard contraindications.** Reject when the subscriber is disposable, when retention would grow without bound, or when a late replay violates a business deadline.

**Competing alternative.** Ephemeral subscription with a separate durable store. Reverse the choice when replay cost and retention exceed the continuity benefit.

**Failure and recovery.** Retention growth and stale replay are common; verify retention and acknowledgement in the owner section.

**Technical owner.** [Consumer requirements and messaging families](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#consumer-requirements-and-messaging-families) — consumer ownership is the bounded owner, not a dedicated channel page.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-durable.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Event-Driven Consumer; Resequencer; Claim Check.

### Idempotent Receiver

**Identity.** Idempotent Receiver; family Messaging and event-driven integration; kind messaging-pattern; priority core.

**Decision question.** Should the receiver detect duplicate deliveries and avoid duplicate effects?

**Good-fit conditions.** Messages carry stable identity; effect and identity are recorded atomically; retention covers the redelivery window; concurrent duplicates are handled.

**Hard contraindications.** Reject when the effect is naturally idempotent, when identity is unstable, or when deduplication state cannot be retained.

**Competing alternative.** Natural idempotency or a transactional inbox. Reverse the choice when identity retention and lookup cost exceed duplicate risk.

**Failure and recovery.** Identity collisions and retention expiry create duplicate effects; verify dedup authority in the owner section.

**Technical owner.** [Message redelivery and consumer effects](../../v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/dedup-authority.md#5-message-redelivery-and-consumer-effects) — deduplication authority is bounded, not a complete idempotent-receiver recipe.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-idempotent.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Point-to-Point Queue; Transactional Inbox; Idempotency Key; Retry with Exponential Backoff.

### Resequencer

**Identity.** Resequencer; family Messaging and event-driven integration; kind messaging-pattern; priority advanced.

**Decision question.** Should out-of-order messages be buffered and released in an acceptable order?

**Good-fit conditions.** Ordering key and expected sequence are explicit; missing-message policy is bounded; buffer limits are known; late messages have a disposition.

**Hard contraindications.** Reject when order is irrelevant, when the buffer can grow without bound, or when one missing message blocks the stream indefinitely.

**Competing alternative.** Process concurrently and reconcile order downstream. Reverse the choice when buffering delays and missing-message risk exceed ordering value.

**Failure and recovery.** Head-of-line blocking and buffer growth are common; verify timeout and missing policy in the owner section.

**Technical owner.** [Requirement-driven comparison, not a ranking](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#2-requirement-driven-comparison-not-a-ranking) — the comparison section is bounded; it does not own every EIP mechanism.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-resequencer.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Competing Consumers; Aggregator; Correlation Identifier; Message Sequence.

### Claim Check

**Identity.** Claim Check; family Messaging and event-driven integration; kind messaging-pattern; priority advanced.

**Decision question.** Should large or sensitive payloads be stored separately and referenced by a claim check?

**Good-fit conditions.** Payload size or sensitivity warrants separation; storage lifetime and access control are owned; the reference is stable; retrieval failure is handled.

**Hard contraindications.** Reject when payloads are small, when the extra retrieval hop violates latency, or when the store cannot enforce access and retention.

**Competing alternative.** Inline payload with transport compression/encryption. Reverse the choice when retrieval and storage complexity exceed transport savings.

**Failure and recovery.** Orphaned claims and access leaks are common; verify storage and retrieval policy in the owner section.

**Technical owner.** [A durable workflow is more than a queue](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/workflow-failure.md#3-a-durable-workflow-is-more-than-a-queue) — workflow failure gates are bounded, not a complete request-reply contract.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-claim.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Message Broker; Dead Letter Channel; Valet Key; Pipes and Filters.

### Message Broker / Messaging Bridge

**Identity.** Message Broker / Messaging Bridge; family Messaging and event-driven integration; kind messaging-pattern; priority core.

**Decision question.** Should a broker mediate routing and delivery between producers and consumers, possibly bridging protocols?

**Good-fit conditions.** Multiple producers/consumers need decoupling; routing and delivery policy are owned; bridge semantics are explicit; the broker can be observed.

**Hard contraindications.** Reject when one direct call suffices, when the broker becomes an unowned single point, or when protocol bridging hides semantic loss.

**Competing alternative.** Direct messaging or a simpler queue. Reverse the choice when broker complexity and operational cost exceed decoupling benefit.

**Failure and recovery.** Broker outage and bridge semantic drift are common; verify bridge contracts in the owner section.

**Technical owner.** [Consumer requirements and messaging families](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#consumer-requirements-and-messaging-families) — consumer ownership is the bounded owner, not a dedicated channel page.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-broker.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Point-to-Point Queue; Canonical Data Model; Gateway Routing.

### Canonical Data Model

**Identity.** Canonical Data Model; family Messaging and event-driven integration; kind integration-pattern; priority advanced.

**Decision question.** Should interapplication messages use a shared canonical model rather than point-to-point translations?

**Good-fit conditions.** Multiple systems exchange the same concepts; a canonical model has an owner; versioning and translation are funded; semantic drift is controlled.

**Hard contraindications.** Reject when only two systems integrate, when one team cannot own the canonical model, or when translation cost exceeds reuse.

**Competing alternative.** Point-to-point message contracts or an anti-corruption layer. Reverse the choice when canonical-model governance becomes a bottleneck.

**Failure and recovery.** Model drift and translation debt are common; verify ownership and versioning in the owner section.

**Technical owner.** [Requirement-driven comparison, not a ranking](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#2-requirement-driven-comparison-not-a-ranking) — the comparison section is bounded; it does not own every EIP mechanism.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-canonical.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Anti-Corruption Layer; Message Broker; Domain-Driven Design / Bounded Context; Schema Evolution.

### Process Manager / Routing Slip

**Identity.** Process Manager / Routing Slip; family Messaging and event-driven integration; kind integration-pattern; priority core.

**Decision question.** Should a durable coordinator own a multi-step message flow and its recovery?

**Good-fit conditions.** Steps span services; progress must survive failure; compensation/rollback is a business protocol; the workflow state has an owner.

**Hard contraindications.** Reject when one local transaction suffices, when no one owns workflow state, or when the process is only a fixed pipeline.

**Competing alternative.** Saga/choreography or a simple pipeline. Reverse the choice when central coordination becomes a bottleneck or a hidden monolith.

**Failure and recovery.** Stuck workflows and ambiguous effects are common; verify workflow recovery in the owner section.

**Technical owner.** [A saga is a business protocol, not an automatic rollback](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#4-a-saga-is-a-business-protocol-not-an-automatic-rollback) — saga protocol ownership is bounded, not a full process-manager engine specification.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-process.2026-10-21: sections "Problem", "Solution", "Example". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Routing Slip; Correlation Identifier; Workflow Failure.

## Chapter result and counterexample

Twenty cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a durable subscriber that replays an unbounded history without an owner
is not evidence for the durable-subscriber card's retention conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C02](../c02-api-communication/README.md).
- Next: [V11/C04](../c04-consistency-events/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 20 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated EIP pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.

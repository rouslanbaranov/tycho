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
    - "src.aws-scatter-gather"
    - "src.microsoft-cloud-patterns"
    - "src.aws-sqs-dlq"
    - "src.azure-service-bus-dlq"
    - "src.hookdeck-dlq-alternatives"
  claim_ids: []
  status: "source-linked"
  notes: "All 20 cards cite read units; owner links are bounded sections, not dedicated EIP pages."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-30"
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

Page count is content-dependent. This chapter uses a landing page plus dedicated card
pages for entries prepared for independent review; a later split is an editorial change, not
a plan failure. Start with the card, check its conditions and contraindications, then read the
exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Publish / Subscribe

**Identity.** Publish/Subscribe; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should one event reach all interested subscribers without the
publisher knowing their count?

**Good-fit conditions.** Subscribers have independent reactions; the publisher can
tolerate fan-out; delivery and retention semantics are explicit; duplicate handling is
owned.

**Hard contraindications.** Reject when one consumer must receive every message exactly
once, when subscriber count is unknown and unbounded, or when the broker cannot express
retention and durable delivery is required.

**Competing alternative.** Point-to-point queue with explicit routing. Reverse the choice
when one work item needs one consumer, not an independent copy per subscriber.

**Failure and recovery.** Fan-out amplifies load and duplicate effects; verify retention
and acknowledgement semantics in the owner section.

**Technical owner.** [Publish / Subscribe](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#publish-subscribe) — topic/cursor delivery ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-pubsub.2026-10-21: served problem/solution; publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Point-to-Point Queue; Durable Subscriber; Event-Driven Consumer;
Competing Consumers.

### Point-to-Point Queue

**Identity.** Point-to-Point Queue; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should each message be consumed by exactly one worker, rather than
broadcast to all subscribers?

**Good-fit conditions.** Work must be divided among consumers; ordering and retry scope
are understood; one logical effect per message; the queue can express visibility and
acknowledgement.

**Hard contraindications.** Reject when every subscriber needs a copy, when strict global
ordering is required without a partition key, or when consumers cannot handle duplicates.

**Competing alternative.** Publish/subscribe fan-out. Reverse the choice when independent
subscribers need the same event rather than one shared work item.

**Failure and recovery.** Duplicate delivery and poison messages are normal; verify
acknowledgement and redelivery semantics in the owner section.

**Technical owner.** [Point-to-Point Queue](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#point-to-point-queue) — queue dispatch and acknowledgement ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-p2p.2026-10-21: served problem/solution; publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Competing Consumers; Dead Letter Channel;
Idempotent Receiver.

### Competing Consumers

**Identity.** Competing Consumers; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should multiple consumers share one queue to scale processing and
smooth bursts?

**Good-fit conditions.** Work is independent per message; consumers can run concurrently;
ordering requirements are partition-scoped; duplicate effects are controlled.

**Hard contraindications.** Reject when global order is mandatory, when consumers mutate
shared state without coordination, or when a slow message has no bounded-attempt or terminal
path.

**Competing alternative.** One ordered consumer per partition, or a partitioned work
queue. Reverse the choice when ordering dominates throughput.

**Failure and recovery.** Concurrency increases duplicate and reorder exposure; verify
ordering and acknowledgement in the owner section.

**Technical owner.** [Consumer requirements and messaging families](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#competing-consumers) — consumer-pool ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-competing.2026-10-21: served problem/solution; publisher-abridged.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Point-to-Point Queue; Idempotent Receiver; Resequencer; Dead Letter
Channel.

### Event-Driven Consumer

**Identity.** Event-Driven Consumer; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should a consumer be invoked by message arrival rather than polling
on a schedule?

**Good-fit conditions.** Arrival latency matters; the runtime can manage subscriptions;
backpressure and failure are observable; the consumer is idempotent.

**Hard contraindications.** Reject when the consumer cannot tolerate push concurrency,
when the broker cannot express acknowledgement, or when polling gives necessary batch
control.

**Competing alternative.** Polling consumer or scheduled batch job. Reverse the choice
when event volume and concurrency overwhelm the consumer.

**Failure and recovery.** Push delivery can outrun processing; verify backpressure and
acknowledgement in the owner section.

**Technical owner.** [Event-Driven Consumer](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#event-driven-consumer) — handler delivery and acknowledgement ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-event-consumer.2026-10-21: Problem and Solution are
unheaded; only the RabbitMQ example is an H2. The page is
publisher-abridged. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Point-to-Point Queue; Competing Consumers; Durable
Subscriber.

### Request-Reply Messaging

See the [dedicated Request-Reply Messaging card](request-reply-messaging.md).

### Correlation Identifier

See the [dedicated Correlation Identifier card](correlation-identifier.md).

### Content-Based Router

**Identity.** Content-Based Router; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should routing be decided from message content rather than a fixed
destination?

**Good-fit conditions.** Routing rules are explicit and testable; message content is
trustworthy; rule changes can be versioned; the router can expose unmatched messages.

**Hard contraindications.** Reject when a fixed route suffices, when routing depends on
untrusted fields, or when rules become domain workflow without ownership.

**Competing alternative.** Static routing or a workflow/orchestrator. Reverse the choice
when content rules become a hidden process engine.

**Failure and recovery.** Rule drift and unmatched messages are common; verify rule
ownership and fallback in the owner section.

**Technical owner.** [Content-Based Router](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#content-based-router) — predicate ownership, fallback and rule versioning are bounded, not every EIP mechanism.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-cbr.2026-10-21: only the Camel example is an H2;
Problem and Solution are unheaded, and the page is publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Message Filter; Pipes and Filters; Process Manager; Message Broker.

### Message Filter

See the [dedicated Message Filter card](message-filter.md).

### Pipes and Filters

See the [dedicated Pipes and Filters card](pipes-and-filters.md).

### Splitter

See the [dedicated Splitter card](splitter.md).

### Aggregator

See the [dedicated Aggregator card](aggregator.md).

### Scatter-Gather

See the [dedicated Scatter-Gather card](scatter-gather.md).

### Dead Letter Channel / DLQ

See the [dedicated Dead Letter Channel / DLQ card](dead-letter-channel.md).

### Durable Subscriber

**Identity.** Durable Subscriber; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should a subscriber retain messages across temporary disconnects?

**Good-fit conditions.** The subscriber can be offline; retention scope and replay are
bounded; duplicate handling exists; the broker supports durable subscriptions.

**Hard contraindications.** Reject when the subscriber is disposable, when retention would
grow without bound, or when a late replay violates a business deadline.

**Competing alternative.** Ephemeral subscription with a separate durable store. Reverse
the choice when replay cost and retention exceed the continuity benefit.

**Failure and recovery.** Retention growth and stale replay are common; verify retention
and acknowledgement in the owner section.

**Technical owner.** [Durable Subscriber](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#durable-subscriber) — durable cursor and retention ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-durable.2026-10-21: no article headings; Example is
absent and the page is publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Event-Driven Consumer; Resequencer; Claim Check.

### Idempotent Receiver

See the [dedicated Idempotent Receiver card](idempotent-receiver.md).

### Resequencer

See the [dedicated Resequencer card](resequencer.md).

### Claim Check

See the [dedicated Claim Check card](claim-check.md).

### Message Broker / Messaging Bridge

**Identity.** Message Broker / Messaging Bridge; family Messaging and event-driven
integration; kind messaging-pattern; priority core.

**Decision question.** Should a broker mediate routing and delivery between producers and
consumers, possibly bridging protocols?

**Good-fit conditions.** Multiple producers/consumers need decoupling; routing and
delivery policy are owned; bridge semantics are explicit; the broker can be observed.

**Hard contraindications.** Reject when one direct call suffices, when the broker becomes
an unowned single point, or when protocol bridging hides semantic loss.

**Competing alternative.** Direct messaging or a simpler queue. Reverse the choice when
broker complexity and operational cost exceed decoupling benefit.

**Failure and recovery.** Broker outage, bridge semantic drift and duplicate or delayed crossing
are common; verify broker availability, the bridge contract, identity mapping and dead-letter
path in the owner section.

**Technical owner.** [Message Broker / Messaging Bridge](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#message-broker-messaging-bridge) — bridge contract and failure-domain ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-broker.2026-10-21: no article headings; Example is
absent and the page is publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Point-to-Point Queue; Canonical Data Model;
Gateway Routing.

### Canonical Data Model

**Identity.** Canonical Data Model; family Messaging and event-driven integration; kind
integration-pattern; priority advanced.

**Decision question.** Should interapplication messages use a shared canonical model
rather than point-to-point translations?

**Good-fit conditions.** Multiple systems exchange the same concepts; a canonical model
has an owner; versioning and translation are funded; semantic drift is controlled.

**Hard contraindications.** Reject when only two systems integrate, when one team cannot
own the canonical model, or when translation cost exceeds reuse.

**Competing alternative.** Point-to-point message contracts or an anti-corruption layer.
Reverse the choice when canonical-model governance becomes a bottleneck.

**Failure and recovery.** Model drift and translation debt are common; verify ownership
and versioning in the owner section.

**Technical owner.** [Canonical Data Model](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#canonical-data-model) — canonical schema ownership is bounded, not every EIP mechanism.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-canonical.2026-10-21: no article headings; Example is
absent and the page is publisher-abridged.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Anti-Corruption Layer; Message Broker; Domain-Driven Design / Bounded
Context; Schema Evolution.

### Process Manager-Routing Slip

**Identity.** Process Manager / Routing Slip; family Messaging and event-driven
integration; kind integration-pattern; priority advanced.

**Decision question.** Should a durable coordinator or a routing-slip itinerary own a
multi-step message flow and its recovery?

**Good-fit conditions.** Steps span services; progress must survive failure; a central
durable state or a fixed itinerary can carry progress; the workflow state has an owner.

**Hard contraindications.** Reject when one local transaction suffices, when no one owns
workflow state, or when the itinerary cannot be made durable.

**Competing alternative.** Saga/choreography or a simple pipeline. Reverse the choice when
central coordination becomes a bottleneck or the itinerary cannot be fixed.

**Failure and recovery.** Stuck workflows, lost dispatch, duplicate steps and ambiguous
effects are common; verify recorded dispatch intent in the owner section.

**Technical owner.** [Process Manager-Routing Slip](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#process-manager-routing-slip) — process-manager and routing-slip coordination is bounded, not a full engine specification.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-process.2026-10-21: two H2 vendor examples; Problem
and Solution are unheaded, and the page is publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark. The cited source supports the process-manager concept; the
routing-slip variant is bounded to the owner section's original design guidance, not this
source.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Idempotent Receiver; Correlation Identifier; Workflow Failure.

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

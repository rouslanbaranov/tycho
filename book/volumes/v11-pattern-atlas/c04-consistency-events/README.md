---
metadata_version: 1
id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/README.md"
title: "V11/C04 — Data consistency, transactions and event sourcing"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 14 C04 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which consistency patterns preserve the required invariants?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "data consistency, transactions and event sourcing"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.fowler-cqrs"
    - "src.microservices-patterns"
    - "src.temporal"
    - "src.ietf-idempotency-key"
    - "src.debezium-outbox"
    - "src.postgresql"
  claim_ids: []
  status: "source-linked"
  notes: "14 cards cite read units; owner links are bounded."
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
# V11/C04 — Data consistency, transactions and event sourcing

**Owning question:** Which consistency patterns preserve the required invariants?

## Purpose and mission

This chapter is the atlas entry point for **Data consistency, transactions and event
sourcing**. It owns the conditional decision route for 14 catalog entries, not the deep
mechanism explanations. Read the exact owner section before applying a mechanism claim.

All 14 entries have a self-checked card. Owner sections are bounded: a CQRS, outbox or
saga page may own the consistency contract without owning every pattern mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Command Query Responsibility Segregation (CQRS)

**Identity.** CQRS; family Data consistency, transactions and event sourcing; kind
architecture-pattern; priority core.

**Decision question.** Should command and query models be separated so reads and writes
can evolve independently?

**Good-fit conditions.** Read and write workloads differ; projections can be asynchronous;
stale reads are acceptable; duplicate/order handling is owned.

**Hard contraindications.** Reject when one model meets both needs, when read-after-write
is mandatory for every client, or when projection maintenance has no owner.

**Competing alternative.** Single model with indexes/views. Reverse the choice when
projection lag and dual-model complexity exceed read-scale benefit.

**Failure and recovery.** Projection lag, duplicate apply, cursor gaps and schema drift are
common; make the apply idempotent, commit view and cursor atomically, and rebuild with side
effects disabled.

**Technical owner.** [Command Query Responsibility Segregation (CQRS)](../../../distributed/cqrs-event-sourcing-and-projections.md#command-query-responsibility-segregation-cqrs) — projection freshness is the bounded owner, not a full CQRS implementation guide.

**Sources.** [src.fowler-cqrs](../../../../edition/patterns/reading-ledger.v1.json)
read record read.fowler-cqrs.2026-10-21: sections "CQRS", "When to use it", "Further
Reading". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Event Sourcing; Materialized View; Command-Side Replica; Domain
Events.

### Event Sourcing

**Identity.** Event Sourcing; family Data consistency, transactions and event sourcing;
kind data-pattern; priority advanced.

**Decision question.** Should authoritative state be derived from an ordered event history
rather than stored as current rows?

**Good-fit conditions.** The event history is the business record; replay and audit are
required; schema evolution and snapshots are owned; external effects are separated.

**Hard contraindications.** Reject when current-state queries dominate, when event schema
cannot evolve, or when replay side effects cannot be controlled.

**Competing alternative.** Current-state store plus audit log/outbox or event notification.
Reverse when full replay is unnecessary, schema ownership is absent or external side effects
cannot be isolated.

**Failure and recovery.** A stale expected version rejects the append; re-read and retry with
the same operation identity. Replay duplication needs idempotent projectors, and schema drift
needs versioned handlers and a rebuild plan.

**Technical owner.** [Event sourcing: what becomes authoritative?](../../../distributed/cqrs-event-sourcing-and-projections.md#2-event-sourcing-what-becomes-authoritative) — event authority is the bounded owner, not a complete event-store design.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-event-sourcing.2026-10-21: sections "Context", "Problem",
"Forces", "Solution", "Example", "Resulting context". The source is a public
pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** CQRS; Domain Events; Transactional Outbox; Materialized View.

### Domain Events

**Identity.** Domain Events; family Data consistency, transactions and event sourcing;
kind integration-pattern; priority core.

**Decision question.** Should a meaningful state change be published as an event that
other owners can react to?

**Good-fit conditions.** The event represents a committed business fact with identity,
version and causation; consumers own their reactions; publication reliability and ordering
are explicit.

**Hard contraindications.** Reject when the event is only a command in disguise, when
publication is not tied to the state change, or when consumers need a shared transaction.

**Competing alternative.** Synchronous call or a command message. Reverse the choice when
event fan-out and eventual consistency exceed the decoupling benefit.

**Failure and recovery.** Duplicate, late, out-of-order and schema-evolved events are
common; deduplicate by identity, preserve aggregate order and keep an unknown/repair state
when publication is not atomic with the state change.

**Technical owner.** [Domain Events](../../../distributed/cqrs-event-sourcing-and-projections.md#domain-events) — the distinction is bounded, not a domain-event catalogue.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-domain-event.2026-10-21: sections "Context", "Problem", "Forces",
"Solution", "Example", "Resulting context". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Event Sourcing; Transactional Outbox; Saga; CQRS.

### Saga

**Identity.** Saga; family Data consistency, transactions and event sourcing; kind
transaction-pattern; priority core.

**Decision question.** Should a multi-service business process be coordinated through
local transactions and compensations?

**Good-fit conditions.** Steps cross service boundaries; intermediate states are
acceptable; compensation is a business decision; progress is durable.

**Hard contraindications.** Reject when one local transaction can preserve the invariant,
when no compensation is possible, or when intermediate visibility is unacceptable.

**Competing alternative.** Single local transaction or two-phase commit. Reverse when steps do
not genuinely cross independent owners or compensation is
unsafe.

**Failure and recovery.** Partial completion and compensation failure are common; verify
saga protocol in the owner section.

**Technical owner.** [Saga](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#saga) — saga recovery is the bounded owner, not a full saga engine.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-saga.2026-10-21: sections "Context", "Problem", "Forces",
"Solution", "Example", "Resulting context". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga Choreography; Saga Orchestration; Compensating Transaction;
Transactional Outbox.

### Saga Choreography

**Identity.** Saga Choreography; family Data consistency, transactions and event sourcing;
kind transaction-pattern; priority advanced.

**Decision question.** Should saga participants react to events without a central
coordinator?

**Good-fit conditions.** Participants can own reactions; event contracts are stable;
correlation, deduplication, dead-letter and timeout policy exist; the overall protocol is
observable.

**Hard contraindications.** Reject when no one can see global progress, when cyclic
reactions are likely, or when compensation ordering must be centrally enforced.

**Competing alternative.** Orchestrated saga or one local transaction. Reverse the choice
when event chains become hard to trace and recover.

**Failure and recovery.** Hidden coupling, unbounded event chains and conflicting
compensations are common; traces show correlation, not durable business truth.

**Technical owner.** [Saga Choreography](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#saga-choreography) — compensation/branching is bounded, not a complete orchestration product guide.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-saga.2026-10-21: sections "Context", "Problem", "Forces",
"Solution", "Example", "Resulting context". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Saga Orchestration; Domain Events; Process Manager.

### Saga Orchestration

**Identity.** Saga Orchestration; family Data consistency, transactions and event
sourcing; kind transaction-pattern; priority advanced.

**Decision question.** Should a central coordinator drive saga steps and compensations?

**Good-fit conditions.** The workflow is complex; central visibility and recovery are
required; the orchestrator can own durable history, timers, idempotent activities and
versioned workflow code.

**Hard contraindications.** Reject when the orchestrator becomes a hidden monolith, when
participants must remain autonomous, or when no team can own workflow state.

**Competing alternative.** Choreography or one local transaction. Reverse the choice when
central coordination becomes a bottleneck or single point of failure.

**Failure and recovery.** Coordinator loss, stuck histories, duplicate activities and
incompatible upgrades are common; replay from durable history and hold unknown external
effects for repair.

**Technical owner.** [Saga Orchestration](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#saga-orchestration) — workflow selection is bounded, not a dedicated Temporal or orchestration manual.

**Sources.** [src.temporal](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-temporal-workflows.2026-10-21: sections "Workflows", "Workflow
Execution", "Determinism". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Saga Choreography; Process Manager; Workflow Failure.

### Compensating Transaction

**Identity.** Compensating Transaction; family Data consistency, transactions and event
sourcing; kind transaction-pattern; priority advanced.

**Decision question.** Should a failed saga step be undone by an explicit business
compensation rather than a rollback?

**Good-fit conditions.** The original effect is durable; compensation is a meaningful
business action; ordering and idempotency are defined.

**Hard contraindications.** Reject when true rollback is possible, when compensation has
irreversible side effects, or when no owner can decide the business reversal.

**Competing alternative.** Avoid the effect, or use a transaction boundary that can roll
back. Reverse the choice when compensation cost exceeds the failed-step risk.

**Failure and recovery.** Compensation is a new business action that can fail or be applied
twice; use idempotent effect identity, bounded retries and a repair state for unknown
counter-effects.

**Technical owner.** [Compensating Transaction](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#compensating-transaction) — compensation/branching is bounded, not a complete orchestration product guide.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-saga.2026-10-21: sections "Context", "Problem", "Forces",
"Solution", "Example", "Resulting context". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Saga Orchestration; Idempotent Receiver; Workflow Failure.

### Transactional Outbox

**Identity.** Transactional Outbox; family Data consistency, transactions and event
sourcing; kind data-pattern; priority core.

**Decision question.** Should publication intent be stored in the same local transaction
as the state change?

**Good-fit conditions.** The database supports a local transaction; a relay can publish
later within a bounded age; duplicate publication is deduplicated; relay ownership and
retention are explicit.

**Hard contraindications.** Reject when the state store cannot share a transaction with an
outbox, when publication latency is unacceptable, or when no relay is operated.

**Competing alternative.** Publish directly after commit with reconciliation. Reverse the
choice when relay complexity exceeds the lost/duplicate publication risk it removes.

**Failure and recovery.** A crash after publish/before checkpoint duplicates; a crash after
commit/before publish retries; a poison row can block progress. Bound attempts/age and keep
repair evidence.

**Technical owner.** [Transactional Outbox](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/outbox-inbox-sagas-and-durable-workflows.md#transactional-outbox) — outbox coordination is bounded, not a connector manual.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-outbox.2026-10-21: sections "Context", "Problem", "Forces",
"Solution", "Example", "Resulting context". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Transactional Inbox; Domain Events; CDC; Idempotent Receiver.

### Transactional Inbox

**Identity.** Transactional Inbox; family Data consistency, transactions and event
sourcing; kind data-pattern; priority core.

**Decision question.** Should message identity and consumer effect be recorded atomically
to suppress duplicates?

**Good-fit conditions.** Messages carry stable identity; the effect is local; identity
retention covers redelivery; concurrent duplicates are handled.

**Hard contraindications.** Reject when the consumer is naturally idempotent, when
identity cannot be retained, or when the effect spans multiple authorities.

**Competing alternative.** A unique constraint/conditional insert on effect identity, a
producer outbox or an idempotent downstream API. Reverse when the inbox table and retention
cost exceed the duplicate-impact risk.

**Failure and recovery.** Expired identities and concurrent duplicates are common; verify
inbox atomicity in the owner section.

**Technical owner.** [Inbox processing and atomic consumer effects](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/inbox-atomicity.md#3-inbox-and-consumer-local-atomicity) — inbox atomicity is bounded, not a complete idempotent-consumer recipe.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-idempotent-consumer.2026-10-21: sections "Context", "Problem",
"Forces", "Solution", "Example", "Resulting context". The source is a public
pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Idempotent Receiver; Idempotency Key; Transactional Outbox;
Deduplication.

### Idempotency Key

**Identity.** Idempotency Key; family Data consistency, transactions and event sourcing;
kind api-pattern; priority core.

**Decision question.** Should a client-supplied key let the server recognize retries of
one logical request?

**Good-fit conditions.** Retries are expected; key scope, payload fingerprint and retention
window are defined; the server records the outcome atomically with the effect.

**Hard contraindications.** Reject when operations are naturally idempotent, when keys can
collide across tenants, or when retention cannot cover the retry window.

**Competing alternative.** Natural idempotency or server-generated operation identity.
Reverse the choice when key storage and fingerprinting cost exceed retry risk.

**Failure and recovery.** Expiry ends historical deduplication; a reused key with changed
intent is a conflict, not idempotency. Reject mismatched fingerprints and keep the record
for the retry window.

**Technical owner.** [Idempotency Key](../../v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/retries-idempotency-and-ambiguous-effects.md#idempotency-key) — retry/idempotency is bounded, not a complete HTTP idempotency guide.

**Sources.**
[src.ietf-idempotency-key](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-ietf.2026-10-21: sections "Introduction", "Uniqueness of
Idempotency Key", "Idempotency Key Validity and Expiry", "Idempotency Fingerprint", "Error
Handling". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Idempotent Receiver; Transactional Inbox; Retry with Exponential
Backoff; Correlation Identifier.

### Change Data Capture (CDC)

**Identity.** Change Data Capture (CDC); family Data consistency, transactions and event
sourcing; kind data-pattern; priority advanced.

**Decision question.** Should database changes be captured as a replayable stream instead
of dual-written by the application?

**Good-fit conditions.** The database log is available; ordering per key is sufficient;
schema evolution is handled; consumers can tolerate duplicates.

**Hard contraindications.** Reject when the log is unavailable or unsupported, when
cross-table ordering is required, or when schema changes cannot be governed.

**Competing alternative.** Transactional outbox plus relay, dual-write with reconciliation or
scheduled batch extraction. Reverse when log access is unavailable, the source cannot retain a
slot, or connector operations exceed the replay benefit.

**Failure and recovery.** Connector lag, WAL/slot retention, schema changes and
snapshot-to-stream gaps are common; monitor lag/slot health, resnapshot deliberately and make
downstream apply idempotent.

**Technical owner.** [Change Data Capture (CDC)](../../v04-distributed-coordination-and-events/c08-stateful-event-time-stream-processing/cdc-state.md#change-data-capture-cdc) — CDC replay is bounded, not a full Debezium operations guide.

**Sources.** [src.debezium-outbox](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-debezium-outbox.2026-10-21: sections "Outbox Event Router",
"Configuration", "Example". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Transactional Outbox; Event Sourcing; Materialized View; Command-Side
Replica.

### Materialized View

**Identity.** Materialized View; family Data consistency, transactions and event sourcing;
kind data-pattern; priority core.

**Decision question.** Should a query result be stored and refreshed explicitly rather
than recomputed per request?

**Good-fit conditions.** The query is expensive or cross-store; source version/offset and
freshness contract are explicit; refresh ownership and locking are defined.

**Hard contraindications.** Reject when strong freshness is required on every read, when
refresh blocks critical traffic, or when invalidation has no owner.

**Competing alternative.** Query on demand or a cache with TTL. Reverse the choice when
refresh cost and staleness exceed query cost.

**Failure and recovery.** Projector crash, cursor gaps, schema drift and partial rebuilds
are common; resume from a recorded cursor and rebuild with side effects disabled.

**Technical owner.** [Materialized View](../../../distributed/cqrs-event-sourcing-and-projections.md#materialized-view) — projection freshness is bounded, not a PostgreSQL materialized-view manual.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-pg-matview.2026-10-21: sections "Materialized Views", "Create
Materialized View", "Refresh Materialized View". The source is a public
pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** CQRS; Command-Side Replica; Cache Invalidation; CDC.

### Command-Side Replica

**Identity.** Command-Side Replica; family Data consistency, transactions and event
sourcing; kind data-pattern; priority advanced.

**Decision question.** Should a command service keep a local read replica of remote facts
to decide without synchronous calls?

**Good-fit conditions.** The replica is read-only for decisions; staleness bounds are
acceptable; reconciliation is owned; writes remain remote.

**Hard contraindications.** Reject when command decisions require linearizable remote
state, when reconciliation cannot be tested, or when the replica becomes a second writer.

**Competing alternative.** Synchronous read or API composition. Reverse the choice when
stale decisions and reconciliation cost exceed latency benefit.

**Failure and recovery.** Stale replicas and split-brain decisions are common; verify
authority in the owner section.

**Technical owner.** [CQRS and asynchronous projection freshness](../../../distributed/cqrs-event-sourcing-and-projections.md#command-side-replica) — command-side replication is bounded to the projection discussion.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-command-side.2026-10-21: sections "Context", "Problem", "Forces",
"Solution", "Example", "Resulting context". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** CQRS; Materialized View; Self-Contained Service; Database per
Service.

### Two-Phase Commit (2PC)

**Identity.** Two-Phase Commit (2PC); family Data consistency, transactions and event
sourcing; kind transaction-pattern; priority advanced.

**Decision question.** Should a distributed transaction use a prepare/commit protocol
across resource managers?

**Good-fit conditions.** Participants support a prepare phase; the coordinator is highly
available; blocking and recovery are acceptable; the invariant spans resources.

**Hard contraindications.** Reject when participants cannot prepare, when coordinator
failure would block critical resources, or when compensation-based saga is sufficient.

**Competing alternative.** Saga/compensation or one local transaction. Reverse the choice
when blocking and coordinator complexity exceed atomicity benefit.

**Failure and recovery.** Prepared transactions can hold locks and block recovery; verify
protocol limits in the owner section.

**Technical owner.** [Local atomic commit does not include the outside world](../../v04-distributed-coordination-and-events/c03-consistency-and-distributed-transactions/invariants-isolation.md#two-phase-commit-2pc) — local/global commit limits are bounded, not a 2PC protocol reference.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-pg-2pc.2026-10-21: sections "Two-Phase Transactions", "Prepare
Transaction", "Commit Prepared". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Compensating Transaction; Transactional Outbox; Distributed
Transactions.

## Chapter result and counterexample

Fourteen cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: an event-sourced system that replays external side effects without
idempotency is not evidence for the event-sourcing card's recovery conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C03](../c03-messaging-integration/README.md).
- Next: [V11/C05](../c05-caching-retrieval/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 14 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.

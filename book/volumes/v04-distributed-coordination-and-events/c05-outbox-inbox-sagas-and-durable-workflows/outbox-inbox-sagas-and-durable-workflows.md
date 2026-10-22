---
metadata_version: 1
id: "tycho.page.aa810dd152884b35a84f0f4cbe4369e9"
kind: "page"
parent_id: "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/outbox-inbox-sagas-and-durable-workflows.md"
title: "Outbox, inbox, sagas and durable workflow coordination"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Outbox, inbox, sagas and durable workflows. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How are state changes coordinated without claiming global atomicity?"
  prerequisites: []
  related_ids:
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.ddbfbbbe1a85406faa2705102378beea"
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
    - "tycho.page.0b493340594c4c4392c5d93940a7f319"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.9daa9ce90a5047fa849c637f24b063f7"
    - "tycho.page.eba0d0f0151c4044a71589c4d216b4b9"
    - "tycho.page.71aea7bc58a6411ba7baf8a2ff40ffbd"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Outbox"
    - "inbox"
    - "sagas"
    - "and"
    - "durable"
    - "workflow"
    - "coordination"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.aa810dd152884b35a84f0f4cbe4369e9:-1 -->

# Outbox, inbox, sagas and durable workflow coordination

> **Tycho manuscript — proposed V04/C05**, 2026-10-19. Primary public references: transactional-outbox and saga/consumer patterns, plus Debezium 3.6 configuration. Original synthetic sequence and state diagram. No broker, CDC process, workflow runner or actual database was deployed, exercised or independently reviewed. Earlier combined [outbox/idempotency research](../../../distributed/transactional-outbox-and-idempotency.md) remains preserved for line-level source comparison.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Distributed Workflow Orchestration](../../v11-pattern-atlas/c08-coordination/README.md#distributed-workflow-orchestration) — decision conditions and contraindications.


> **Pattern atlas:**
> [Transactional Outbox](../../v11-pattern-atlas/c04-consistency-events/README.md#transactional-outbox) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.aa810dd152884b35a84f0f4cbe4369e9:0 -->
## Purpose and decision question

A relational database can commit an authoritative state change inside one local transaction. An unrelated message broker or external service is usually *not part of the same atomic commit*. A long-running workflow crossing several independent owners therefore needs explicit persistent state, publication and failure contracts. A distributed event architecture is not made reliable by drawing an arrow from a transaction to a queue.

Four patterns address different questions:
- **Transactional outbox:** how can the local state change and a durable intent to publish one event be committed atomically?
- **Inbox/idempotent consumer:** how can a downstream owner apply a redelivered event without duplicating its local business effect?
- **Saga:** how can several owners coordinate business steps and appropriate compensating actions without claiming one global transaction?
- **Durable workflow:** how can a coordinator record its progress, resume after failure and surface unknown outcomes?

**Workflow state.** A durable workflow is a persistent state machine: steps, timers,
retries, versions, compensation and human tasks survive process loss. The engine records
history and replays deterministic code; activity boundaries hold non-deterministic or
external effects. [Temporal documentation](https://docs.temporal.io/workflows) describes
this execution model; it is not a product recommendation.

**Failure and recovery.** Stuck workflows, duplicate activities, lost timers,
non-deterministic replay and version conflicts are common. Recovery needs replay from
durable history, idempotent activities, explicit retry/cancel/compensation, and a repair
state for unknown external effects. Do not infer success from a completed workflow flag
when an external effect is uncertain.

**Alternative.** Saga choreography, a database-backed job table, or a simple queue
pipeline may be simpler when steps are few, no long timers are needed, or the team cannot
operate an engine. Reverse when coordination and versioning cost exceed the workflow
benefit.

**Outbox mechanism.** Commit the authoritative state change and a publication-intent row
in one local transaction. A relay reads unpublished rows, publishes them and records a
checkpoint; consumers deduplicate by event identity. The outbox gives durable intent, not
atomicity with the broker or exactly-once delivery.

**Failure and recovery.** A relay can crash after publish but before checkpoint, causing a
duplicate; after commit but before publish, causing a retry; a poison row can block
progress. Bound attempts and age, retain repair evidence and make publication idempotent.
Snapshot/log-based CDC, transactional messaging, or direct publish with reconciliation may
be preferable when the outbox table or relay is not operationally justified.

The exact retry/operation identity contract is owned by [V04/C04](../c04-retries-idempotency-and-duplicate-effects/retries-idempotency-and-ambiguous-effects.md); this chapter owns multi-boundary state coordination.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Separate local atomic publication intent, relay retries, consumer deduplication and compensation state.

Writing an outbox does not make a remote notification atomic with the original transaction; relay and receiver failures still need recovery.

The detailed pages separate the mechanisms that make this decision conditional:

- [Outbox publication and ordering](outbox-publication.md) — Which local atomic record closes a dual-write loss window?
- [Inbox processing and atomic consumer effects](inbox-atomicity.md) — When can a receiver commit an effect and its deduplication record together?
- [Sagas, workflow recovery and compensation](saga-workflows.md) — What business recovery contract replaces a nonexistent global rollback?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

### Transactional Outbox

An outbox commits the authoritative state change and a publication-intent row in one local
transaction. A separate relay publishes rows and checkpoints progress; the row is the durable
intent, not the broker's acknowledgement.

The outbox gives durable intent, not atomicity with the broker or exactly-once delivery. A relay can
crash after publish but before checkpoint, causing a duplicate; after commit but before publish,
causing a retry; a poison row can block progress. Consumers still need effect identity. Bound relay
attempts and age, retain the repair evidence for the declared window and give a poison
row a terminal quarantine decision.

Use an outbox when the lost/duplicate publication risk justifies relay complexity. Reverse to direct
publish with reconciliation only when relay complexity exceeds the risk it removes; CDC or
transactional messaging may fit when the log is accessible.

### Distributed Workflow Orchestration

A durable workflow is a persistent state machine: steps, timers, retries, versions, compensation and
human tasks survive process loss. The workflow history is the authority for progress, not an
in-memory coroutine.

Recovery needs replay from durable history, idempotent activities, explicit retry/cancel/compensation,
and a repair state for unknown external effects. Do not infer success from a completed workflow flag
when an external effect is uncertain. Upgrade workflow code with versioning so a replayed history
does not change meaning.

Saga choreography, a database-backed job table, or a simple queue pipeline may be simpler when steps
are few, no long timers are needed, or the team cannot operate an engine. Orchestration is a fit when
long waits, visibility and compensation justify the engine.

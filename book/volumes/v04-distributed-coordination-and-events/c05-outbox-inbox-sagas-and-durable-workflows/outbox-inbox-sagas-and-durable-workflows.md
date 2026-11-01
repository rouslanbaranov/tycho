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
  source_ids:
    - "src.microservices-patterns"
    - "src.temporal"
  claim_ids: []
  status: "source-linked"
  notes: "Read source-plan units; page-level, not claim-mapped."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-11-01"
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

See the [dedicated Transactional Outbox owner note](transactional-outbox.md).

### Distributed Workflow Orchestration

A durable workflow records progress as a state machine, not as an in-memory coroutine. Steps,
timers, retries, human tasks and compensation must survive process loss. Temporal records each
command and event in an Event History and replays that history to rebuild state after a crash
([Temporal Workflows](https://docs.temporal.io/workflows)); Cadence documents the same replay
model ([Cadence workflow engine](https://cadenceworkflow.io/docs/concepts/workflow-engine/)).
Recovery replays durable history, so activities need stable identities and explicit retry,
cancel and compensation outcomes. The state machine is a coordination record, not a claim
that every external call is atomic.

**Failure and recovery (Tycho synthesis).** A worker can call an external service and crash before
the result is recorded. Temporal states that an Activity Task can be lost "after the Activity
Function is called and the Worker crashed", then relies on the Start-To-Close timeout to retry it
([Temporal Activity Execution](https://docs.temporal.io/activity-execution)). AWS Step Functions
fails an activity execution with `ExecutionTimedOut` when the worker does not call
`SendTaskSuccess` or send a heartbeat, invalidates the task token, and can later redrive the
failed Task state (AWS activities,
<https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html>;
AWS redrive,
<https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html>).
Cadence "does not recover activity state" and regular activities may execute more than once under
a retry policy ([Cadence Activities](https://cadenceworkflow.io/docs/concepts/activities/)). AWS
Standard workflows are exactly-once for "your tasks and states" unless a `Retry` is declared,
while Express workflows are at-least-once (AWS workflow types,
<https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html>).
Those guarantees cover the orchestration record, not the external effect. Keep a repair state for
an unknown external effect; a completed flag is not proof that the effect committed. That repair
rule is Tycho guidance. Version workflow code so replay preserves meaning. Record the workflow
version and repair owner in the runbook.

**Alternative (Tycho comparison).** Use choreography, a job table or a simple queue when steps
are few, timers are short, or no engine can be operated. Temporal's job-queue guidance uses a
Workflow only to orchestrate several activities or hold state
between steps ([Temporal Job queues](https://docs.temporal.io/evaluate/features/job-queue));
Cadence says a queue is usually the right tool for "simple fire-and-forget fanout", and describes
the queue-plus-database pattern as working for "simple flows" while dispersing state across tables
([Cadence FAQ](https://cadenceworkflow.io/faq/cadence-faq/);
[Cadence workflow engine](https://cadenceworkflow.io/docs/concepts/workflow-engine/)). Temporal's
Saga comparison lists event-driven choreography as an alternative with "Very loose" coupling
([Temporal Saga pattern](https://docs.temporal.io/design-patterns/saga-pattern)). The operability
condition and the final selection rule are Tycho guidance; an engine is justified by long waits,
visibility and compensation. Escalate a history that cannot progress to the named workflow owner.

**Sources and limits.** The 2026-11-01 records bind Temporal *Workflows*, *Activities*, *Activity
Execution*, *Saga Pattern* and *Job queues*; AWS Step Functions *Choosing workflow type*,
*Activities*, *Redrive* and *Best practices*; and Cadence *Activities*, *FAQ* and *Workflow
Engine*. Proposed records: `read.temporal-workflows.2026-11-01`,
`read.temporal-activities.2026-11-01`, `read.temporal-activity-execution.2026-11-01`,
`read.temporal-saga-pattern.2026-11-01`, `read.temporal-job-queue.2026-11-01`,
`read.aws-step-functions-workflow-types.2026-11-01`,
`read.aws-step-functions-activities.2026-11-01`,
`read.aws-step-functions-redrive.2026-11-01`,
`read.aws-step-functions-best-practices.2026-11-01`,
`read.cadence-activities.2026-11-01`, `read.cadence-faq.2026-11-01` and
`read.cadence-workflow-engine.2026-11-01`. Source identity `src.temporal` is existing;
`src.aws-step-functions` and `src.cadence` are proposed and not yet in the shared register. No
engine, worker, activity, timer, retry, outage or repair state was exercised; no independent
review is claimed.

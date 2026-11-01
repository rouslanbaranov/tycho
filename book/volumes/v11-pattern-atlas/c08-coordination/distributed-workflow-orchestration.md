---
metadata_version: 1
id: "tycho.page.d6c23f6a944a40ba83af85dffdd63642"
kind: "page"
parent_id: "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c08-coordination/distributed-workflow-orchestration.md
title: "Distributed Workflow Orchestration"
topic_ids:
  - "distributed-systems"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Distributed Workflow Orchestration; source-anchored on
  Temporal workflows, activities, replay, saga and job queues, AWS Step
  Functions workflow types, activities, redrive and best practices, and Cadence
  activities, FAQ and workflow engine; coverage remains partial-bounded, no
  promotion.
route_hints:
  questions:
    - >-
      Should a durable orchestration engine own multi-step progress, timers and
      recovery?
  prerequisites:
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  related_ids:
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  excludes:
    - >-
      Product-specific engine configuration and benchmark results.
  keywords:
    - "pattern atlas"
    - "distributed workflow orchestration"
    - "distributed coordination"
evidence_scope:
  source_ids:
    - "src.temporal"
    - "src.aws-step-functions"
    - "src.cadence"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch2-temporal-workflows.2026-10-21 and the twelve
    2026-11-01 records for Temporal, AWS Step Functions and Cadence; owner
    section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# Distributed Workflow Orchestration

**Identity.** Distributed Workflow Orchestration; family Distributed coordination; kind
coordination-pattern; priority core.

**Decision question.** Should a durable orchestration engine own multi-step progress,
timers and recovery?

**Good-fit conditions.** Steps span services or long timers; progress must survive crashes;
activities can be idempotent; retries, cancellation and compensation are business
decisions; the team can operate a durable engine and version its workflow code while preserving
replay compatibility.

**Hard contraindications.** Reject when one local transaction suffices, when workflow state
has no owner, when replay/versioning cannot be governed, or when orchestration becomes a
hidden monolith.

**Competing alternative.** Saga choreography, a database-backed job table or a simple queue
pipeline. Temporal's job-queue guidance reserves a Workflow for several activities or state
between steps; Cadence says a queue is usually right for simple fire-and-forget fanout and
that the queue-plus-database pattern works for simple flows while dispersing state across
tables. Temporal's Saga comparison lists event-driven choreography as a distinct option.
Reverse when central workflow state and engine operations exceed coordination benefit; that
selection rule is Tycho guidance.

**Failure and recovery.** Stuck workflows, duplicate activities, delayed timers,
nondeterministic replay and version conflicts are possible failure modes. Temporal records that an
Activity Task can be lost after the Activity Function ran and the Worker crashed, then retries
it under the activity retry policy; AWS Step Functions times out an activity when no success,
failure or heartbeat arrives before TimeoutSeconds, invalidates the task token and can redrive
the Task;
Cadence does not recover activity state and regular activities can run more than once under
a retry policy. AWS Standard workflows are exactly-once for "your tasks and states" per
execution attempt unless `Retry` is declared; redrive reruns the failed Task state even
without an ASL Retry, so external effects still need idempotency or a repair state.
Express workflows are at-least-once. **Tycho runbook:** replay from durable history, keep
activities idempotent, and use a repair state for unknown external effects; a completed flag
is not proof that the effect committed.

**Technical owner.** [Distributed Workflow Orchestration](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/outbox-inbox-sagas-and-durable-workflows.md#distributed-workflow-orchestration) — durable workflow coordination is bounded, not a Temporal product guide.

**Sources.** [src.temporal](../../../../edition/patterns/reading-ledger.v1.json)
retained record `read.batch2-temporal-workflows.2026-10-21`; 2026-11-01 records
`read.temporal-workflows.2026-11-01`, `read.temporal-activities.2026-11-01`,
`read.temporal-activity-execution.2026-11-01`,
`read.temporal-saga-pattern.2026-11-01`, `read.temporal-job-queue.2026-11-01`,
`read.aws-step-functions-workflow-types.2026-11-01`,
`read.aws-step-functions-activities.2026-11-01`,
`read.aws-step-functions-redrive.2026-11-01`,
`read.aws-step-functions-best-practices.2026-11-01` (src.aws-step-functions);
`read.cadence-activities.2026-11-01`, `read.cadence-faq.2026-11-01` and
`read.cadence-workflow-engine.2026-11-01` (src.cadence). Public documentation,
not a benchmark, engine run, outage drill or repair-state test.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga Orchestration; Process Manager; Transactional Outbox;
Lease-Based Ownership.

**Limits.** Coverage is partial-bounded and self-checked, not independent
review, promotion or owner acceptance. The repair-state rule, the
completed-flag caution and the selection rule are Tycho guidance; no engine,
worker, activity, timer, retry, outage or repair state was exercised.


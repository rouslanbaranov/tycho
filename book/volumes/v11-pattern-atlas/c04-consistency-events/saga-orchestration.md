---
metadata_version: 1
id: "tycho.page.3624cafbc3e448d1b218861cd06d059b"
kind: "page"
parent_id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/saga-orchestration.md"
title: "Saga Orchestration"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Saga Orchestration with bounded owner evidence."
route_hints:
  questions:
    - "Should a central coordinator drive saga steps and compensations?"
  prerequisites:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  related_ids:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "saga orchestration"
    - "workflow orchestration"
evidence_scope:
  source_ids:
    - "src.temporal"
    - "src.microservices-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
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

# Saga Orchestration

**Identity.** Saga Orchestration; family Data consistency, transactions and event
sourcing; kind transaction-pattern; priority core.

**Decision question.** Should a central coordinator drive saga steps and compensations?

**Good-fit conditions.** The workflow is complex; central visibility and recovery are
required; the orchestrator can own durable history, timers, idempotent activities and
versioned workflow code.

**Hard contraindications.** Reject when the orchestrator becomes a hidden monolith, when
participants must remain autonomous, or when no team can own workflow state.

**Competing alternative.** Choreography or one local transaction. Reverse the choice when
central coordination becomes a bottleneck or single point of failure.

**Failure and recovery.** Coordinator loss, stuck histories, duplicate activities and
upgrade conflicts are possible; replay from durable history and hold unknown external
effects for repair.

**Technical owner.** [Saga Orchestration](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#saga-orchestration) — workflow selection is bounded, not a dedicated Temporal or orchestration manual.

**Sources.**
[src.temporal](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-temporal-workflows.2026-10-21: all four served headings read.
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-saga.2026-10-21: all eleven served headings read.
[src.temporal](../../../../edition/patterns/reading-ledger.v1.json)
read record read.temporal-saga-pattern.2026-11-01: sections "Overview", "Solution",
"Comparison with alternatives" and "Best practices". The records support durable orchestration
and the choreography/orchestration distinction; saga compensation semantics remain Tycho
guidance. The sources are public pattern/specification and documentation units, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Saga Choreography; Process Manager; Workflow Failure.

## Evidence and limits

Temporal, "Saga Pattern" (`read.temporal-saga-pattern.2026-11-01`, revision
`987aec66a21037418c7f9930c139aaeb2a20b76690ef140769d6886c5e11e5c9`): "For example, a credit
card may be charged but the Activity fails before returning success." and "All compensations
must be idempotent and able to handle cases where the forward Activity never executed." The
comparison table rates choreography as "Very loose" coupling with "Event-driven compensations".

Microservices.io, "Saga" (`read.batch2-saga.2026-10-21`, revision
`54805df89f619c8432fd280263a88670ed66fac6cbe0b5429a1ebdc5d4cd1047`): "There are two ways of
coordination sagas": choreography publishes domain events that trigger other services, while
orchestration uses an orchestrator that tells participants what to execute.

Tycho guidance, not a source claim: prefer one transaction when every effect shares an owner and
a database. Orchestration earns its cost only when the operation spans independently owned
effects whose failures and repairs differ. The owner section remains bounded; this page does not
claim sufficient coverage or independent review.

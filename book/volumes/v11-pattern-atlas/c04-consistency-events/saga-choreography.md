---
metadata_version: 1
id: tycho.page.83eba08943484783de91c92f6e19e954
kind: page
parent_id: tycho.chapter.e9c650012060143639af44b0cfdc4236
canonical_path: book/volumes/v11-pattern-atlas/c04-consistency-events/saga-choreography.md
title: Saga Choreography
topic_ids:
- consistency
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Saga Choreography.
route_hints:
  questions:
  - Should saga participants react to events without a central coordinator?
  prerequisites:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  related_ids:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - saga choreography
evidence_scope:
  source_ids:
  - src.microservices-patterns
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Saga Choreography

**Identity.** Saga Choreography; family Data consistency, transactions and event sourcing;
kind transaction-pattern; priority core.

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

**Technical owner.**
 [Saga
Choreography](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#saga-choreography)
— event-driven saga coordination is bounded, not a complete orchestration product guide.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-saga.2026-10-21: all eleven served headings read.
The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Saga Orchestration; Domain Events; Process Manager.

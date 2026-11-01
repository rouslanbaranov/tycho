---
metadata_version: 1
id: tycho.page.d19ee75f841ebf9a5c4a5893eb27dbdc
kind: page
parent_id: tycho.chapter.e9c650012060143639af44b0cfdc4236
canonical_path: book/volumes/v11-pattern-atlas/c04-consistency-events/compensating-transaction.md
title: Compensating Transaction
topic_ids:
- consistency
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Compensating Transaction.
route_hints:
  questions:
  - Should a failed saga step be undone by an explicit business compensation rather
    than a rollback?
  prerequisites:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  related_ids:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - compensating transaction
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

# Compensating Transaction

**Identity.** Compensating Transaction; family Data consistency, transactions and event
sourcing; kind transaction-pattern; priority core.

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

**Technical owner.**
 [Compensating
Transaction](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#compensating-transaction)
— compensation/branching is bounded, not a complete orchestration product guide.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-saga.2026-10-21: all eleven served headings read.
The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Saga Orchestration; Idempotent Receiver; Workflow Failure.

---
metadata_version: 1
id: tycho.page.8928049120feb19c0ca2262ae535bf76
kind: page
parent_id: tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
canonical_path: book/volumes/v11-pattern-atlas/c06-database-storage/cqrs-read-projections.md
title: CQRS Read Projections
topic_ids:
- database-and-storage-architecture
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for CQRS Read Projections.
route_hints:
  questions:
  - Should a read model be projected asynchronously from an authoritative write model?
  prerequisites:
  - tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
  related_ids:
  - tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - cqrs read projections
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

# CQRS Read Projections

**Identity.** CQRS Read Projections; family Database and storage architecture; kind
data-pattern; priority core.

**Decision question.** Should a read model be projected asynchronously from an
authoritative write model?

**Good-fit conditions.** Stale reads are acceptable; projection ownership exists;
duplicate/order handling is defined; rebuild is possible.

**Hard contraindications.** Reject when every read needs immediate consistency, when
projection lag violates the contract, or when rebuild cost is unbounded.

**Competing alternative.** Synchronous read from the write model or a materialized view.
Reverse the choice when projection freshness/complexity exceeds read-scale benefit.

**Failure and recovery.** Stale and duplicate projections are common; verify freshness in
the owner section.

**Technical owner.**
 [CQRS Read
Projections](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/cqrs-event-sourcing-and-read-projections.md#cqrs-read-projections) —
projection freshness is bounded, not a complete read-model design.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-cqrs.2026-10-21: all nine served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** CQRS; Materialized View; Event Sourcing; CDC.

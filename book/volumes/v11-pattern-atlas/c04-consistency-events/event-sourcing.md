---
metadata_version: 1
id: tycho.page.0856b21dbe7ece72283c1e445f34520a
kind: page
parent_id: tycho.chapter.e9c650012060143639af44b0cfdc4236
canonical_path: book/volumes/v11-pattern-atlas/c04-consistency-events/event-sourcing.md
title: Event Sourcing
topic_ids:
- consistency
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Event Sourcing.
route_hints:
  questions:
  - Should authoritative state be derived from an ordered event history rather than
    stored as current rows?
  prerequisites:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  related_ids:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - event sourcing
evidence_scope:
  source_ids:
  - src.microservices-patterns
  - src.fowler-event-sourcing
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

# Event Sourcing

**Identity.** Event Sourcing; family Data consistency, transactions and event sourcing;
kind data-pattern; priority core.

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
the same operation identity. Replay needs versioned handlers and a rebuild plan; external
effects and duplicate delivery need an explicit boundary, not an assumed idempotent projector.

**Technical owner.**
 [Event sourcing: what becomes
authoritative?](../../../distributed/cqrs-event-sourcing-and-projections.md#2-event-sourcing-what-becomes-authoritative)
— event authority is the bounded owner, not a complete event-store design.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-event-sourcing.2026-10-21: all nine served headings
read. The source is a public
pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** CQRS; Domain Events; Transactional Outbox; Materialized View.

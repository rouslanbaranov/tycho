---
metadata_version: 1
id: tycho.page.aae5b499ca5128ab9d30ff6c524b94db
kind: page
parent_id: tycho.chapter.e9c650012060143639af44b0cfdc4236
canonical_path: book/volumes/v11-pattern-atlas/c04-consistency-events/materialized-view.md
title: Materialized View
topic_ids:
- consistency
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Materialized View.
route_hints:
  questions:
  - Should a query result be stored and refreshed explicitly rather than recomputed
    per request?
  prerequisites:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  related_ids:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - materialized view
evidence_scope:
  source_ids:
  - src.postgresql
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

# Materialized View

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

**Failure and recovery.** Stale rows, refresh duration and lock contention are common; a
plain refresh can block reads, while CONCURRENTLY needs a unique index covering all rows,
allows one refresh at a time and still consumes I/O. Define the freshness contract and
refresh trigger, monitor duration and locks, and rebuild from the base tables rather than
treating the view as an authority.

**Technical owner.**
 [Materialized View](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/cqrs-event-sourcing-and-read-projections.md#materialized-view)
— stored-query freshness is bounded, not a full PostgreSQL materialized-view manual.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch9-pg-matview-refresh.2026-10-22: all eight served headings
read. The source is public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** CQRS; Command-Side Replica; Cache Invalidation; CDC.

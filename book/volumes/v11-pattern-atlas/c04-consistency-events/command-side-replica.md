---
metadata_version: 1
id: tycho.page.1655f7c12a8da0940cfe9b14b482b76f
kind: page
parent_id: tycho.chapter.e9c650012060143639af44b0cfdc4236
canonical_path: book/volumes/v11-pattern-atlas/c04-consistency-events/command-side-replica.md
title: Command-Side Replica
topic_ids:
- consistency
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Command-Side Replica.
route_hints:
  questions:
  - Should a command service keep a local read replica of remote facts to decide without
    synchronous calls?
  prerequisites:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  related_ids:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - command side replica
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

# Command-Side Replica

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

**Technical owner.**
 [CQRS and asynchronous projection
freshness](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/cqrs-event-sourcing-and-read-projections.md#command-side-replica) —
command-side replication is bounded to the projection discussion.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-command-side.2026-10-21: Forces is not a heading and no
Example section exists. The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** CQRS; Materialized View; Self-Contained Service; Database per
Service.

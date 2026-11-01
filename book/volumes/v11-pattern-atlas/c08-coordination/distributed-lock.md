---
metadata_version: 1
id: tycho.page.5edaae3d1c4d2ccc9f7c473a9e309e43
kind: page
parent_id: tycho.chapter.bee261b76181706235dd8fa7ccde01a9
canonical_path: book/volumes/v11-pattern-atlas/c08-coordination/distributed-lock.md
title: Distributed Lock
topic_ids:
- coordination
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Distributed Lock.
route_hints:
  questions:
  - Should a shared lock prevent concurrent access to one resource across processes?
  prerequisites:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  related_ids:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - distributed lock
evidence_scope:
  source_ids:
  - src.kubernetes
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

# Distributed Lock

**Identity.** Distributed Lock; family Distributed coordination; kind
coordination-pattern; priority advanced.

**Decision question.** Should a shared lock prevent concurrent access to one resource
across processes?

**Good-fit conditions.** The lock protects a correctness-critical section; the service
can maintain quorum; expiry and ownership are explicit; the resource checks a fencing
epoch.

**Hard contraindications.** Reject when work is naturally partitioned, when lock loss
would corrupt state, when the lock service cannot maintain quorum, or when the resource
cannot reject a stale holder.

**Competing alternative.** Lease-based ownership with fencing, single-writer partitioning,
or a conditional write/unique constraint. Reverse the choice when lock safety cannot be proven.

**Failure and recovery.** Pauses, delayed writes, quorum loss and release races are
common. Treat ownership as uncertain after a missed renewal; fence stale epochs at the
resource or keep the outcome explicitly unsafe.

**Technical owner.**
 [Distributed
Lock](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/leader-recovery.md#distributed-lock)
— locks/leases/fencing are bounded, not a lock-service API guide.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-k8s-leases.2026-10-21: all six served headings read.
The prior truncation note is superseded.
The record covers leases; fencing and quorum guidance is synthetic owner evidence.
The source is a public pattern/documentation unit, not a benchmark.
[src.kleppmann-distributed-locking](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-fencing.2026-10-21: all nine served headings read.
The article supports fencing tokens; it does not benchmark
this design.

**Decision state.** applicable-under-conditions.

**Related entries.** Lease-Based Ownership; Fencing Tokens; Leader Election; Consensus.

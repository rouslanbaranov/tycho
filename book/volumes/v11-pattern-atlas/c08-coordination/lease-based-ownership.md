---
metadata_version: 1
id: tycho.page.b35826f5700905df072bf6a4d2b0c2ed
kind: page
parent_id: tycho.chapter.bee261b76181706235dd8fa7ccde01a9
canonical_path: book/volumes/v11-pattern-atlas/c08-coordination/lease-based-ownership.md
title: Lease-Based Ownership
topic_ids:
- coordination
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Lease-Based Ownership.
route_hints:
  questions:
  - Should ownership expire after a bounded lease rather than remain until explicit
    release?
  prerequisites:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  related_ids:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - lease based ownership
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

# Lease-Based Ownership

**Identity.** Lease-Based Ownership; family Distributed coordination; kind
coordination-pattern; priority core.

**Decision question.** Should ownership expire after a bounded lease rather than remain
until explicit release?

**Good-fit conditions.** A lease duration is known; renewal is observable; expired owners
stop acting; destination fencing exists.

**Hard contraindications.** Reject when the owner cannot renew, when clock skew is
unbounded, or when expiry could allow two active owners without fencing.

**Competing alternative.** Static ownership or quorum-backed ownership. Reverse the choice
when lease renewal cost exceeds availability benefit.

**Failure and recovery.** Pauses, delayed renewal and quorum loss can leave two owners
acting. Treat ownership as uncertain after a missed renewal and fence the stale epoch at
the destination.

**Technical owner.**
 [Lease-Based
Ownership](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/leader-recovery.md#lease-based-ownership)
— lease ownership is bounded, not a scheduler implementation.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-k8s-leases.2026-10-21: all six served headings read. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Distributed Lock; Fencing Tokens; Leader Election; Health Endpoint
Monitoring.

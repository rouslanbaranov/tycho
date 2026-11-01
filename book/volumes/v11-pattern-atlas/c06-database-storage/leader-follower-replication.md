---
metadata_version: 1
id: tycho.page.dc1342d7ee4520cc3c36a23840adc4e1
kind: page
parent_id: tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
canonical_path: book/volumes/v11-pattern-atlas/c06-database-storage/leader-follower-replication.md
title: Leader-Follower Replication
topic_ids:
- database-and-storage-architecture
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Leader-Follower Replication.
route_hints:
  questions:
  - Should one leader accept writes while followers replicate and serve reads?
  prerequisites:
  - tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
  related_ids:
  - tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - leader follower replication
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

# Leader-Follower Replication

**Identity.** Leader-Follower Replication; family Database and storage architecture; kind
replication-pattern; priority core.

**Decision question.** Should one leader accept writes while followers replicate and serve
reads?

**Good-fit conditions.** A single writer is acceptable; failover is owned; replication lag
is observable; read-after-write can be routed to the leader.

**Hard contraindications.** Reject when writes must be accepted in multiple regions, when
lag violates a hard read contract, or when failover is untested.

**Competing alternative.** Multi-leader or quorum writes. Reverse the choice when leader
unavailability or write locality dominates.

**Failure and recovery.** Lag, failover and split-brain are common; verify leader change
in the owner section.

**Technical owner.**
 [Leader-Follower
Replication](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md#leader-follower-replication)
— replication/leader change is bounded, not a complete multi-leader protocol.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-warm.2026-10-21: all twenty headings read; Hot
Standby and Failover are separate pages. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Multi-Leader Replication; Read Replicas; Quorum; Backup/PITR.

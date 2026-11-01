---
metadata_version: 1
id: tycho.page.204b289ec2dc87381c47713971254ce1
kind: page
parent_id: tycho.chapter.bee261b76181706235dd8fa7ccde01a9
canonical_path: book/volumes/v11-pattern-atlas/c08-coordination/leader-election.md
title: Leader Election
topic_ids:
- coordination
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Leader Election.
route_hints:
  questions:
  - Should one node be chosen to coordinate work while others stand by?
  prerequisites:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  related_ids:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - leader election
evidence_scope:
  source_ids:
  - src.raft
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

# Leader Election

**Identity.** Leader Election; family Distributed coordination; kind coordination-pattern;
priority core.

**Decision question.** Should one node be chosen to coordinate work while others stand by?

**Good-fit conditions.** A single coordinator is useful; terms/epochs are available;
failover and stale leaders are handled; clients can observe leadership.

**Hard contraindications.** Reject when work is safely partitioned without a leader, when
election cannot be made safe, or when leader failover would block progress.

**Competing alternative.** Leaderless/quorum coordination or static assignment. Reverse
the choice when election latency and split-brain risk exceed coordination benefit.

**Failure and recovery.** Split votes, quorum loss, stale leaders and divergent uncommitted
logs are common. A follower read can miss committed state; require read-index or lease
confirmation for linearizable reads. Stop authoritative writes without quorum, keep retries
idempotent, and treat durability as contingent on stable storage and membership change.

**Technical owner.**
 [Leader elections, logs and client
observations](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/leader-recovery.md#4-leader-elections-logs-and-client-observations)
— leader election is bounded, not a complete Raft implementation.

**Sources.** [src.raft](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-raft.2026-10-21: sections "The Raft Consensus Algorithm",
"What is Raft?". The landing page does not document term/vote/log safety or election details;
those are synthetic owner guidance. The source is a public pattern/documentation unit, not a
benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Consensus; Lease-Based Ownership; Fencing Tokens; Quorum
Coordination.

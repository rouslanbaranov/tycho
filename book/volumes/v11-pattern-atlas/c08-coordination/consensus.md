---
metadata_version: 1
id: tycho.page.d2e66ea8bd211e98e366cc18247fdde2
kind: page
parent_id: tycho.chapter.bee261b76181706235dd8fa7ccde01a9
canonical_path: book/volumes/v11-pattern-atlas/c08-coordination/consensus.md
title: Consensus
topic_ids:
- coordination
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Consensus.
route_hints:
  questions:
  - Should replicas agree on an ordered log despite failures and partitions?
  prerequisites:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  related_ids:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - consensus
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

# Consensus

**Identity.** Consensus; family Distributed coordination; kind coordination-pattern;
priority core.

**Decision question.** Should replicas agree on an ordered log despite failures and
partitions?

**Good-fit conditions.** A quorum exists; safety and progress requirements are explicit;
membership changes are owned; clients tolerate retries.

**Hard contraindications.** Reject when a single writer suffices, when the network cannot
provide a stable quorum, or when availability must override consistency.

**Competing alternative.** Leader-follower replication with weaker guarantees. Reverse the
choice when consensus latency/availability cost exceeds agreement benefit.

**Failure and recovery.** Quorum loss and leader churn are common; verify safety/progress
in the owner section.

**Technical owner.**
[Consensus](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md#consensus)
— consensus is bounded to safety/progress discussion.

**Sources.** [src.raft](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-raft.2026-10-21: sections "The Raft Consensus Algorithm",
"What is Raft?". The landing page does not document safety/term details; those are synthetic
owner guidance. The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader Election; Quorum Coordination; Leader-Follower Replication;
2PC.

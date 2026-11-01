---
metadata_version: 1
id: tycho.page.1e381b168fd7f99e8d053e8f4d5ba190
kind: page
parent_id: tycho.chapter.bee261b76181706235dd8fa7ccde01a9
canonical_path: book/volumes/v11-pattern-atlas/c08-coordination/quorum-coordination.md
title: Quorum Coordination
topic_ids:
- coordination
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Quorum Coordination.
route_hints:
  questions:
  - Should decisions require a majority of replicas rather than one node?
  prerequisites:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  related_ids:
  - tycho.chapter.bee261b76181706235dd8fa7ccde01a9
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - quorum coordination
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

# Quorum Coordination

**Identity.** Quorum Coordination; family Distributed coordination; kind
coordination-pattern; priority core.

**Decision question.** Should decisions require a majority of replicas rather than one
node?

**Good-fit conditions.** Replica set and failure domains are known; majority arithmetic is
explicit; latency of quorum calls is acceptable.

**Hard contraindications.** Reject when a single authority suffices, when the network
cannot maintain a majority, or when quorum latency violates the budget.

**Competing alternative.** Leader-based coordination or static assignment. Reverse the
choice when quorum availability/latency exceeds safety benefit.

**Failure and recovery.** Quorum loss, slow replicas and unsafe membership changes are
common. A minority must refuse conflicting authority; membership changes need joint or
overlapping safeguards.

**Technical owner.**
 [Quorum
Coordination](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/quorum-envelope.md#quorum-coordination)
— quorum arithmetic is bounded, not a consensus protocol.

**Sources.** [src.raft](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-raft.2026-10-21: sections "The Raft Consensus Algorithm",
"What is Raft?". The landing page does not document safety/term details; those are synthetic
owner guidance. The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Consensus; Leader Election; Quorum-Based Reads/Writes; 2PC.

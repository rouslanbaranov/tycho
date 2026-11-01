---
metadata_version: 1
id: "tycho.page.253d5a98933c4cee947545acb8eaa72a"
kind: "page"
parent_id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/read-replicas.md"
title: "Read Replicas"
topic_ids:
  - "data-architecture"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Read Replicas with bounded owner evidence."
route_hints:
  questions:
    - "Should read-only replicas serve queries to offload the writer?"
  prerequisites:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  related_ids:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "read replicas"
    - "replication"
evidence_scope:
  source_ids:
    - "src.postgresql"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Read Replicas

**Identity.** Read Replicas; family Database and storage architecture; kind
replication-pattern; priority core.

**Decision question.** Should read-only replicas serve queries to offload the writer?

**Good-fit conditions.** Reads tolerate bounded lag; routing can separate stale reads;
replica health and lag are observable.

**Hard contraindications.** Reject when every read requires linearizable freshness, when
lag is unbounded, or when replicas add no capacity benefit.

**Competing alternative.** Single writer or cached read models. Reverse the choice when
replica lag and routing complexity exceed read-scale benefit.

**Failure and recovery.** Stale reads and replica lag are common; verify read routing in
the owner section.

**Technical owner.** [Read Replicas](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md#read-replicas) — read-replica scaling is bounded by replica lag, read routing and staleness.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-warm.2026-10-21: all twenty headings read; Hot
Standby and Failover are separate pages. The source is a public pattern/documentation
unit, not a benchmark.

**Evidence and limits.** PostgreSQL's high-availability chapter states that
"Read-only database servers can be combined relatively easily" and that
asynchronous solutions can return "slightly stale results". The leader-or-quorum
preference and the staleness budget are Tycho guidance, not source claims. Read
record read.pg18-ha.2026-10-30; public page served 2026-10-30, revision
d698df8b9a70f099937b74505a17be21a69f53c133668a6fca28563149d56f9d.
No benchmark, lag measurement or failover exercise is claimed.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Quorum; Materialized View; CQRS.

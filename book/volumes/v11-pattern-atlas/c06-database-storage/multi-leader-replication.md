---
metadata_version: 1
id: "tycho.page.1f0f0984036746779cc0bc96826db1e9"
kind: "page"
parent_id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/multi-leader-replication.md"
title: "Multi-Leader Replication"
topic_ids:
  - "data-architecture"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Multi-Leader Replication with bounded owner evidence."
route_hints:
  questions:
    - "Should more than one node accept writes for the same data?"
  prerequisites:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  related_ids:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  excludes:
    - "No owner acceptance is claimed for this card."
  keywords:
    - "pattern atlas"
    - "multi-leader replication"
    - "replication"
evidence_scope:
  source_ids:
    - "src.cassandra"
    - "src.postgresql"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Multi-Leader Replication

**Identity.** Multi-Leader Replication; family Database and storage architecture; kind
replication-pattern; priority advanced.

**Decision question.** Should more than one node accept writes for the same data?

**Good-fit conditions.** Write locality/availability requires multiple leaders; conflict
policy is explicit; versioning and reconciliation are owned.

**Hard contraindications.** Reject when one leader meets availability, when conflicts
cannot be resolved, when monotonic writes are mandatory, or when the resolver cannot preserve
causal order; the conflict contract must name the resolver and its audit trail.

**Competing alternative.** Leader-follower (primary/standby) replication or quorum/consensus
writes. PostgreSQL's comparison notes that synchronous multi-master lets any server accept
writes but is best for mostly read workloads, with locking and commit delays under heavy write
activity, and that asynchronous multi-master needs conflict resolution. Reverse the choice when
conflict handling and divergent histories exceed locality benefit.

**Failure and recovery.** Conflicting writes and reconciliation are common; verify
versioning in the owner section.

**Technical owner.** [Replication, consensus and leader change](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md#multi-leader-replication) — replication/leader change is bounded, not a complete multi-leader protocol.

**Sources.** [src.cassandra](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-cassandra-dynamo.2026-10-21: all nineteen served headings
read. The source is a public
pattern/documentation
unit, not a benchmark.
Alternative comparison: [PostgreSQL 18, section 26.1 Comparison of Different
Solutions](https://www.postgresql.org/docs/current/different-replication-solutions.html),
served 2026-10-29, SHA-256
7a5bc0622dd4ff65ca5e13a3b449c0e7d2855f3ad875305d1f7df1569d2604f9.
Read record read.postgresql-replication-solutions.2026-10-29, section 26.1.
The comparison is documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Quorum; Read Replicas; Conflict
Resolution.

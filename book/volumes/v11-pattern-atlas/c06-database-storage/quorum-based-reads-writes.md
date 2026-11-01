---
metadata_version: 1
id: "tycho.page.6f56fff79cb74db0b699c504412e1f54"
kind: "page"
parent_id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/quorum-based-reads-writes.md"
title: "Quorum-Based Reads / Writes"
topic_ids:
  - "data-architecture"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Quorum-Based Reads / Writes with bounded owner evidence."
route_hints:
  questions:
    - "Should reads and writes require intersecting majorities to guarantee consistency?"
  prerequisites:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  related_ids:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "quorum-based reads / writes"
    - "database and storage architecture"
evidence_scope:
  source_ids:
    - "src.cassandra"
    - "src.dynamo"
    - "src.riak"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch3-cassandra-dynamo.2026-10-21,
    read.cassandra-read-repair.2026-10-30, read.dynamo-sosp2007.2026-10-30 and
    read.riak-replication-properties.2026-10-30; owner section and limits are
    bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# Quorum-Based Reads / Writes

**Identity.** Quorum-Based Reads/Writes; family Database and storage architecture; kind
replication-pattern; priority advanced.

**Decision question.** Should reads and writes require intersecting majorities to
guarantee consistency?

**Good-fit conditions.** Replica count and failure domains are known; quorum arithmetic is
explicit; the application defines a version selector and a repair path; latency of majority
calls is acceptable.

**Hard contraindications.** Reject when a single leader suffices, when quorum latency
violates the budget, when failure domains make majority meaningless, or when concurrent
versions cannot be ordered or repaired.

**Competing alternative.** Leader-based replication or eventual consistency. Sloppy quorum
is the availability fallback within the pattern. Reverse the choice when quorum
availability/latency cost exceeds consistency benefit, or when sloppy quorum is the
intended availability trade-off.

**Failure and recovery.** Intersection alone does not guarantee freshness. Cassandra read
repair returns the most up-to-date data and repairs replicas; Dynamo reconciles causally
unrelated versions and uses hinted handoff and Merkle-tree anti-entropy; Riak uses read
repair and active anti-entropy. Tycho guidance: a highest-version selector needs an
application-defined total order, because Dynamo and Riak can expose concurrent siblings;
a membership change needs the old
and new quorums to overlap, or an explicit sloppy-quorum trade-off. See the owner section.

**Technical owner.** [Quorum-Based Reads / Writes](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/quorum-envelope.md#quorum-based-reads-writes) — quorum arithmetic is bounded, not a universal consistency guarantee.

**Sources.** [src.cassandra](../../../../edition/patterns/reading-ledger.v1.json)
read records `read.batch3-cassandra-dynamo.2026-10-21` and
`read.cassandra-read-repair.2026-10-30`: the Cassandra "Dynamo" architecture page and
the read-repair page, including "Tunable Consistency", "Replica Synchronization" and
"Expectation of Monotonic Quorum Reads".
[src.dynamo](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.dynamo-sosp2007.2026-10-30`: sections 4.4-4.7 and 4.9;
quorum arithmetic, version reconciliation, hinted handoff, anti-entropy and
membership handoff.
[src.riak](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.riak-replication-properties.2026-10-30`: "Primary Reads and
Writes with PR and PW", "Symbolic Consistency Names" and "Illustrative
Scenarios"; sloppy and strict quorum, read repair and vector-clock/timestamp
resolution. The sources are public documentation and a paper, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Multi-Leader Replication; Read Replicas;
2PC.

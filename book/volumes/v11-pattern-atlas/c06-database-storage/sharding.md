---
metadata_version: 1
id: "tycho.page.e59ddfc6c410468ab44119cedbe4c171"
kind: "page"
parent_id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/sharding.md"
title: "Sharding"
topic_ids:
  - "data-architecture"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Sharding with bounded owner evidence."
route_hints:
  questions:
    - "Should data be split across shards by a partition key to scale beyond one node?"
  prerequisites:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  related_ids:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "sharding"
    - "database and storage architecture"
evidence_scope:
  source_ids:
    - "src.mongo-sharding"
    - "src.citus"
    - "src.postgresql"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch3-citus.2026-10-21, the 2026-10-30 MongoDB, Citus and
    PostgreSQL records and the retained PostgreSQL partition record; owner
    section and limits are bounded.
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
# Sharding

**Identity.** Sharding; family Database and storage architecture; kind
data-distribution-pattern; priority core.

**Decision question.** Should data be split across shards by a partition key to scale
beyond one node?

**Good-fit conditions.** A stable partition key exists; cross-shard transactions are
avoidable; routing and rebalancing are owned; hotspots can be measured; a failed
migration has a bounded retry or rollback path.

**Hard contraindications.** Reject when one node suffices, when the key creates hot
tenants, when cross-shard joins/transactions dominate, or when a failed migration
cannot be detected and verified.

**Competing alternative.** Partitioning within one database, read replicas (hot
standby) or vertical scaling. PostgreSQL documents partitioning and hot-standby
read-only replicas; Citus recommends PostgreSQL table partitioning for time-ordered data and
warns that joins cross the network boundary; MongoDB notes that vertical scaling has a
practical maximum. Reverse
the choice when distribution adds cross-shard coordination without relieving the
measured constraint; that reversal rule is Tycho synthesis.

**Failure and recovery.** Hotspots, hot chunks and failed migrations are documented;
MongoDB identifies uneven load from monotonic keys, the balancer pauses reads/writes
while updating range metadata, and retryable writes remain retryable for five minutes
after a reshard. Citus takes a brief write-lock while promoting a shard. Map drift and
split brain are Tycho failure modes; hot-key throttling and dual-read/verify are Tycho
controls; verify them in the owner section.

**Technical owner.** [Sharding](../../v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/shard-keys-hotspots-and-resharding.md#sharding) — shard key choice and resharding cost are bounded; per-engine placement is platform-specific.

**Sources.** [src.citus](../../../../edition/patterns/reading-ledger.v1.json)
mechanism record `read.batch3-citus.2026-10-21`; 2026-10-30 records
`read.citus-cluster.2026-10-30` and `read.citus-datamodel.2026-10-30`
("Choosing Distribution Column").
[src.mongo-sharding](../../../../edition/patterns/reading-ledger.v1.json)
records `read.mongo-sharding.2026-10-30`, `read.mongo-choose-key.2026-10-30`,
`read.mongo-troubleshoot-key.2026-10-30`, `read.mongo-balancer.2026-10-30` and
`read.mongo-reshard.2026-10-30`.
[src.postgresql](../../../../edition/patterns/reading-ledger.v1.json) record
`read.pg18-ha.2026-10-30`; the retained
`read.batch3-pg-partition.2026-10-21` binds partitioning (revision
`6f4540b06405f349bbffa5a003e1788584c1f3dbe6167e997e76c7e721406001`). Public documentation,
not a benchmark, cluster run or migration test.

**Decision state.** applicable-under-conditions.

**Related entries.** Partitioning; Consistent Hashing; Online Data Migration; Read
Replicas.

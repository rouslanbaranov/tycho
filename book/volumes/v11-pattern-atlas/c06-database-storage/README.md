---
metadata_version: 1
id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/README.md"
title: "V11/C06 — Database and storage architecture"
topic_ids:
  - "data-architecture"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "13 C06 cards with bounded owner links."
route_hints:
  questions:
    - "Which storage patterns fit the workload and recovery boundary?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  excludes:
    - "No entry claims sufficient technical or decision coverage."
  keywords:
    - "pattern atlas"
    - "database and storage architecture"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.citus"
    - "src.postgresql"
    - "src.sre"
    - "src.aws-backup"
    - "src.azure-backup"
    - "src.cassandra"
    - "src.dynamo"
    - "src.riak"
    - "src.microservices-patterns"
    - "src.flyway"
    - "src.gh-ost"
    - "src.aws-cqrs"
    - "src.microsoft-cloud-patterns"
    - "src.debezium-outbox"
  claim_ids: []
  status: "source-linked"
  notes: >-
    13 cards cite read units; Index Table and Backup/PITR bind all four
    dimensions; Polyglot Persistence binds invariant and recovery.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# V11/C06 — Database and storage architecture

**Owning question:** Which storage patterns fit the workload and recovery boundary?

## Purpose and mission

This chapter is the atlas entry point for **Database and storage architecture**. It
owns the conditional decision route for 13 catalog entries, not the deep mechanism
explanations. All thirteen entries have a bounded card; Polyglot Persistence uses a
public article and the V05/C04 selection section.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus dedicated card
pages for moved entries; a later split is an editorial change, not a plan failure. Start
with the card, check its conditions and contraindications, then read the exact owner
section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Sharding

See the [dedicated Sharding card](sharding.md).

### Partitioning

**Identity.** Partitioning; family Database and storage architecture; kind
data-distribution-pattern; priority core.

**Decision question.** Should a large table or stream be divided into partitions for
pruning, retention or parallelism?

**Good-fit conditions.** Partition key aligns with query/retention; partition count is
manageable; pruning is observable; maintenance is owned.

**Hard contraindications.** Reject when queries cross all partitions, when partition count
grows unbounded, or when partition keys create skew.

**Competing alternative.** Single table/index or sharding across nodes. Reverse the choice
when partition maintenance and pruning no longer justify the split.

**Failure and recovery.** Partition skew and maintenance are common; verify
pruning/lifecycle in the owner section.

**Technical owner.** [Sharding, partition keys, hotspots and safe resharding](../../v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/shard-keys-hotspots-and-resharding.md#partitioning) — partition key and pruning are bounded; per-engine partition mechanics are implementation-specific.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-partition.2026-10-21: all thirteen headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Sharding; Consistent Hashing; Index Table; Online Data Migration.

### Consistent Hashing

See the [dedicated Consistent Hashing card](consistent-hashing.md).

### Leader-Follower Replication

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

**Technical owner.** [Leader-Follower Replication](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md#leader-follower-replication) — replication/leader change is bounded, not a complete multi-leader protocol.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-warm.2026-10-21: all twenty headings read; Hot
Standby and Failover are separate pages. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Multi-Leader Replication; Read Replicas; Quorum; Backup/PITR.

### Multi-Leader Replication

See the [dedicated Multi-Leader Replication card](multi-leader-replication.md).

### Read Replicas

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

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Quorum; Materialized View; CQRS.

### Quorum-Based Reads / Writes

See the [dedicated Quorum-Based Reads / Writes card](quorum-based-reads-writes.md).

### Index Table

See the [dedicated Index Table card](index-table.md).

### Polyglot Persistence

See the [dedicated Polyglot Persistence card](polyglot-persistence.md).

### CQRS Read Projections

**Identity.** CQRS Read Projections; family Database and storage architecture; kind
data-pattern; priority core.

**Decision question.** Should a read model be projected asynchronously from an
authoritative write model?

**Good-fit conditions.** Stale reads are acceptable; projection ownership exists;
duplicate/order handling is defined; rebuild is possible.

**Hard contraindications.** Reject when every read needs immediate consistency, when
projection lag violates the contract, or when rebuild cost is unbounded.

**Competing alternative.** Synchronous read from the write model or a materialized view.
Reverse the choice when projection freshness/complexity exceeds read-scale benefit.

**Failure and recovery.** Stale and duplicate projections are common; verify freshness in
the owner section.

**Technical owner.** [CQRS Read Projections](../../../distributed/cqrs-event-sourcing-and-projections.md#cqrs-read-projections) — projection freshness is bounded, not a complete read-model design.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-cqrs.2026-10-21: all nine served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** CQRS; Materialized View; Event Sourcing; CDC.

### Expand-and-Contract Schema

**Identity.** Expand-and-Contract Schema; family Database and storage architecture; kind
migration-pattern; priority core.

**Decision question.** Should a schema change be deployed in expand, migrate and contract
stages?

**Good-fit conditions.** Old and new code coexist during rollout; a compatibility window
is owned; backfill and validation are explicit.

**Hard contraindications.** Reject when old and new readers cannot coexist, when no
compatibility window or contract owner exists, or when the mapping cannot preserve identity
and references.

**Competing alternative.** Keep the schema and add a mapping layer, or use a smaller change
when authority need not move. Reverse when staged migration cost exceeds rollout risk.

**Failure and recovery.** Partial backfills and old readers are common; verify gates in
the owner section.

**Technical owner.** [Expand-and-Contract Schema](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/migration-retirement.md#expand-and-contract-schema) — expand/contract is bounded, not a complete migration runbook.

**Sources.** [src.flyway](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-flyway.2026-10-21: all seventeen served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Online Data Migration; Expand-and-Contract; Backup/PITR; Migration
Retirement.

### Online Data Migration

**Identity.** Online Data Migration; family Database and storage architecture; kind
migration-pattern; priority core.

**Decision question.** Should data be backfilled while the system continues serving reads
and writes?

**Good-fit conditions.** Writes continue during migration; dual-read/write or CDC is
owned; validation and cutover are gated.

**Hard contraindications.** Reject when a maintenance window is acceptable, when no
reconciliation path exists, or when migration load would exhaust the source.

**Competing alternative.** Offline migration or a full export/import. Reverse the choice
when online complexity exceeds downtime cost.

**Failure and recovery.** Stale backfills and cutover ambiguity are common; verify
acceptance in the owner section.

**Technical owner.** [Online Data Migration](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/migration-retirement.md#online-data-migration) — backfill acceptance is bounded, not an online migration tool guide.

**Sources.** [src.gh-ost](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-gh-ost.2026-10-21: all ten served headings read. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Expand-and-Contract Schema; Sharding; CDC; Backup/PITR.

### Backup, PITR and Restore

**Identity.** Backup, PITR and Restore; family Database and storage architecture; kind
recovery-pattern; priority core.

**Decision question.** Should recovery rely on base backups plus point-in-time WAL/log
replay?

**Good-fit conditions.** A base backup and a continuous archive are both retained; the chain,
recovery target, encryption keys and retention are owned; restore drills are scheduled; and
the target can be validated with business invariants. PostgreSQL says "you need a continuous
sequence of archived WAL files that extends back at least as far as the start time of your
backup." These are Tycho conditions.

**Hard contraindications.** Reject when the archive has gaps, when retention cannot cover the
detection window, when no restore has been tested, or when RPO/RTO cannot be measured. Also
reject a replica-only plan for accidental deletion or corruption. **Tycho contraindication.**

**Competing alternative.** Snapshot-only recovery or replica failover. Google SRE says
replication "can’t protect you from many sources of data loss" and that "a corrupt database
row or errant delete are pushed to all of your copies". Azure Backup separates "data
protection (backup and restore)" from "disaster recovery and failover orchestration". **Tycho
choice rule:** use a replica for availability and a backup chain for historical state; reverse
when snapshot/restore cost meets recovery needs.

**Failure and recovery.** Corrupt backups and untested restores are common. PostgreSQL warns
that "If recovery finds corrupted WAL data, recovery will halt at that point and the server
will not start"; a missing or inaccessible archive bounds the reachable point. AWS Backup
restore testing "provides automated and periodic evaluation of restore viability"; Google SRE
says "you only know that you can recover your recent state if you actually do so". **Tycho
runbook:** restore into an isolated target, verify checksums, chain and business invariants,
record the achieved point and gap, and keep the old writer fenced.

**Technical owner.** [Backup, restore and recovery drills: proving data recoverability](../../v05-data-models-engines-and-lifecycle/c07-replication-backups-and-restore-drills/backup-restore-pitr-and-recovery-drills.md#backup-pitr-and-restore) — backup/restore is bounded, not a universal RPO/RTO model.

**Sources.** Five public units inspected on 2026-10-31: PostgreSQL 17 *Continuous Archiving
and Point-in-Time Recovery (PITR)*; AWS Backup *What is AWS Backup?* and *Restore testing*;
Azure Backup *What is the Azure Backup service?*; and Google SRE *Data Integrity: What You
Read Is What You Wrote*. Retained: `read.batch3-pg-archiving.2026-10-21`;
new records: `read.pg-pitr.2026-10-31`, `read.aws-backup.2026-10-31`,
`read.aws-backup-restore-testing.2026-10-31`,
`read.azure-backup.2026-10-31` and `read.sre-data-integrity.2026-10-31`. Source ids:
`src.postgresql` and `src.sre` are registered; `src.aws-backup` and `src.azure-backup` are
proposed pending registration. Canonical text SHA-256 `3aeddd67...`, `edbc0b59...`,
`8a0be467...`, `628a6734...` and `8afec387...`. Exact URLs, sections and revisions are in
the lane note and owner section. None is a benchmark or production observation; no database,
backup or restore was run.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Read Replicas; Expand-and-Contract;
Disaster Recovery.

## Chapter result and counterexample

Thirteen cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a sharded system with one hot tenant and no resharding plan is not
evidence for the sharding card's partition-key conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C05](../c05-caching-retrieval/README.md).
- Next: [V11/C07](../c07-resilience/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- Thirteen cards cite read ledger units; owner links and backlinks are self-checked.
- Polyglot Persistence is bounded by a public article and an embedded owner section.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.

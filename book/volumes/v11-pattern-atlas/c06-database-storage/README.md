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
summary: "12 C06 cards with bounded owner links; Polyglot Persistence remains blocked."
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
    - "Polyglot Persistence remains blocked; no card or sufficient coverage is claimed."
  keywords:
    - "pattern atlas"
    - "database and storage architecture"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.citus"
    - "src.postgresql"
    - "src.cassandra"
    - "src.microservices-patterns"
    - "src.flyway"
    - "src.gh-ost"
  claim_ids: []
  status: "source-linked"
  notes: "12 cards cite read units; Polyglot Persistence remains blocked."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-21"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# V11/C06 — Database and storage architecture

**Owning question:** Which storage patterns fit the workload and recovery boundary?

## Purpose and mission

This chapter is the atlas entry point for **Database and storage architecture**. It
owns the conditional decision route for 13 catalog entries, not the deep mechanism
explanations. Twelve entries have a card; Polyglot Persistence remains blocked by its
bibliography-only source and is not carded.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Sharding

**Identity.** Sharding; family Database and storage architecture; kind
data-distribution-pattern; priority advanced.

**Decision question.** Should data be split across shards by a partition key to scale
beyond one node?

**Good-fit conditions.** A stable partition key exists; cross-shard transactions are
avoidable; routing and rebalancing are owned; hotspots can be measured.

**Hard contraindications.** Reject when one node suffices, when the key creates hot
tenants, or when cross-shard joins/transactions dominate.

**Competing alternative.** Partitioning within one database or vertical scaling. Reverse
the choice when operational shard complexity exceeds scale benefit.

**Failure and recovery.** Hotspots and resharding are common; verify routing/rebalancing
in the owner section.

**Technical owner.** [Sharding, partition keys, hotspots and safe resharding](../../v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/shard-keys-hotspots-and-resharding.md#purpose-and-mission) — sharding/partition keys are bounded, not a universal distribution recipe.

**Sources.** [src.citus](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-citus.2026-10-21: sections "Concepts". The source is a public
pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Partitioning; Consistent Hashing; Online Data Migration; Read
Replicas.

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

**Technical owner.** [Sharding, partition keys, hotspots and safe resharding](../../v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/shard-keys-hotspots-and-resharding.md#partitioning) — sharding/partition keys are bounded, not a universal distribution recipe.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-partition.2026-10-21: sections "Table Partitioning", "Partition
Pruning", "Partitioning Best Practices". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Sharding; Consistent Hashing; Index Table; Online Data Migration.

### Consistent Hashing

**Identity.** Consistent Hashing; family Database and storage architecture; kind
data-distribution-pattern; priority advanced.

**Decision question.** Should keys and nodes share a hash ring so membership changes move
only a fraction of data?

**Good-fit conditions.** Membership changes often; the hash ring is owned; virtual
nodes/replication are configured; key distribution is measured.

**Hard contraindications.** Reject when a static assignment is stable, when the ring
creates hotspots, or when rebalancing cannot be observed.

**Competing alternative.** Modulo sharding or explicit range assignment. Reverse the
choice when ring operations and virtual-node tuning exceed movement savings.

**Failure and recovery.** Hotspots and uneven rebalancing are common; verify ring
ownership in the owner section.

**Technical owner.** [Resharding is a multi-state data transition](../../v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/resharding-transition.md#consistent-hashing) — resharding transition is bounded, not a consistent-hashing implementation.

**Sources.** [src.cassandra](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-cassandra-arch.2026-10-21: sections "Overview", "Architecture".
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Sharding; Partitioning; Resharding; Read Replicas.

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

**Technical owner.** [Replication, consensus and leader change](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md#engineering-walkthrough-new-leader-old-client-and-a-lost-acknowledgment) — replication/leader change is bounded, not a complete multi-leader protocol.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-warm.2026-10-21: sections "Log-Shipping Standby Servers",
"Planning", "Failover". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Multi-Leader Replication; Read Replicas; Quorum; Backup/PITR.

### Multi-Leader Replication

**Identity.** Multi-Leader Replication; family Database and storage architecture; kind
replication-pattern; priority advanced.

**Decision question.** Should more than one node accept writes for the same data?

**Good-fit conditions.** Write locality/availability requires multiple leaders; conflict
policy is explicit; versioning and reconciliation are owned.

**Hard contraindications.** Reject when one leader meets availability, when conflicts
cannot be resolved, or when monotonic writes are mandatory.

**Competing alternative.** Leader-follower or quorum writes. Reverse the choice when
conflict handling and divergent histories exceed locality benefit.

**Failure and recovery.** Conflicting writes and reconciliation are common; verify
versioning in the owner section.

**Technical owner.** [Replication, consensus and leader change](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md#multi-leader-replication) — replication/leader change is bounded, not a complete multi-leader protocol.

**Sources.** [src.cassandra](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-cassandra-dynamo.2026-10-21: sections "Dynamo", "Multi-master
Replication: Versioned Data and Tunable Consistency". The source is a public
pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Quorum; Read Replicas; Conflict
Resolution.

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

**Technical owner.** [Replication, consensus and leader change](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/replication-consensus-and-leader-change.md#read-replicas) — replication/leader change is bounded, not a complete multi-leader protocol.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-warm.2026-10-21: sections "Log-Shipping Standby Servers",
"Implementation". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Quorum; Materialized View; CQRS.

### Quorum-Based Reads / Writes

**Identity.** Quorum-Based Reads/Writes; family Database and storage architecture; kind
replication-pattern; priority advanced.

**Decision question.** Should reads and writes require intersecting majorities to
guarantee consistency?

**Good-fit conditions.** Replica count and failure domains are known; quorum arithmetic is
explicit; latency of majority calls is acceptable.

**Hard contraindications.** Reject when a single leader suffices, when quorum latency
violates the budget, or when failure domains make majority meaningless.

**Competing alternative.** Leader-based replication or eventual consistency. Reverse the
choice when quorum availability/latency cost exceeds consistency benefit.

**Failure and recovery.** Quorum loss and slow replicas are common; verify failure
envelope in the owner section.

**Technical owner.** [Majority quorum arithmetic and the failure envelope](../../v04-distributed-coordination-and-events/c02-replication-consensus-and-leader-changes/quorum-envelope.md#2-majority-quorum-arithmetic-and-the-failure-envelope) — quorum arithmetic is bounded, not a universal consistency guarantee.

**Sources.** [src.cassandra](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-cassandra-dynamo.2026-10-21: sections "Tunable Consistency",
"Multi-master Replication: Versioned Data and Tunable Consistency". The source is a public
pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Multi-Leader Replication; Read Replicas;
2PC.

### Index Table

**Identity.** Index Table; family Database and storage architecture; kind
data-structure-pattern; priority core.

**Decision question.** Should a separate lookup table maintain a secondary access path?

**Good-fit conditions.** The access path is stable; index maintenance and write cost are
acceptable; consistency with the source is owned.

**Hard contraindications.** Reject when the primary index suffices, when dual-write
consistency cannot be maintained, or when the lookup is rarely used.

**Competing alternative.** Secondary index or query-time join. Reverse the choice when
index maintenance and drift exceed lookup benefit.

**Failure and recovery.** Stale index rows and write amplification are common; verify
lifecycle in the owner section.

**Technical owner.** [An index is a data lifecycle change](../../v05-data-models-engines-and-lifecycle/c03-query-planning-indexes-and-access-paths/plan-lifecycle.md#5-an-index-is-a-data-lifecycle-change) — index lifecycle is bounded, not a full access-path catalogue.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-indexes.2026-10-21: sections "Indexes", "Index Types",
"Multicolumn Indexes". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Partitioning; Materialized View; CQRS Read Projections; Sharding.

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

**Technical owner.** [CQRS and asynchronous projection freshness](../../../distributed/cqrs-event-sourcing-and-projections.md#3-cqrs-and-asynchronous-projection-freshness) — projection freshness is bounded, not a complete read-model design.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-cqrs.2026-10-21: sections "Context", "Problem", "Forces",
"Solution", "Example", "Resulting context". The source is a public pattern/documentation
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

**Hard contraindications.** Reject when downtime is acceptable and a direct migration is
simpler, when no compatibility window exists, or when rollback is impossible.

**Competing alternative.** Direct migration or a versioned API boundary. Reverse the
choice when staged migration cost exceeds rollout risk.

**Failure and recovery.** Partial backfills and old readers are common; verify gates in
the owner section.

**Technical owner.** [Expand, migrate, contract as a gated lifecycle](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/migration-retirement.md#3-expand-migrate-contract-as-gated-lifecycle) — expand/contract is bounded, not a complete migration runbook.

**Sources.** [src.flyway](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-flyway.2026-10-21: sections "Migrations", "Versioned Migrations",
"Repeatable Migrations". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Online Data Migration; Expand-and-Contract; Backup/PITR; Migration
Retirement.

### Online Data Migration

**Identity.** Online Data Migration; family Database and storage architecture; kind
migration-pattern; priority advanced.

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

**Technical owner.** [Backfill acceptance is more than row totals](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/migration-retirement.md#backfill-acceptance-is-more-than-row-totals) — backfill acceptance is bounded, not an online migration tool guide.

**Sources.** [src.gh-ost](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-gh-ost.2026-10-21: sections "How?", "Highlights", "Usage". The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Expand-and-Contract Schema; Sharding; CDC; Backup/PITR.

### Backup, PITR and Restore

**Identity.** Backup, PITR and Restore; family Database and storage architecture; kind
recovery-pattern; priority core.

**Decision question.** Should recovery rely on base backups plus point-in-time WAL/log
replay?

**Good-fit conditions.** Recovery objectives are stated; backup retention and WAL
continuity are owned; restore drills are scheduled.

**Hard contraindications.** Reject when no restore has been tested, when WAL/backup
continuity has gaps, or when RPO/RTO cannot be measured.

**Competing alternative.** Snapshot-only recovery or replica failover. Reverse the choice
when snapshot/restore cost meets recovery needs.

**Failure and recovery.** Corrupt backups and untested restores are common; verify PITR in
the owner section.

**Technical owner.** [Backup, restore and recovery drills: proving data recoverability](../../v05-data-models-engines-and-lifecycle/c07-replication-backups-and-restore-drills/backup-restore-pitr-and-recovery-drills.md#backup-pitr-and-restore) — backup/restore is bounded, not a universal RPO/RTO model.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-archiving.2026-10-21: sections "Continuous Archiving and
Point-in-Time Recovery (PITR)", "Setting Up WAL Archiving", "Recovering Using a Continuous
Archive Backup". The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Read Replicas; Expand-and-Contract;
Disaster Recovery.

### Polyglot Persistence

**Catalog problem:** Choose different stores for different data responsibilities while preserving
cross-store consistency and operations.

**State:** blocked; the admitted book is bibliography-only and no card is asserted.

**Technical owner:** `technical-owner-missing` — no admissible technical owner
exists. Remediation is tracked by #284; the entry remains blocked and uncarded.
The entry remains visible for catalog completeness.

## Chapter result and counterexample

Twelve cards establish a conditional decision route. Owner sections are bounded; none
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

- Twelve cards cite read ledger units; owner links and backlinks are self-checked.
- Polyglot Persistence remains blocked and has no card.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.

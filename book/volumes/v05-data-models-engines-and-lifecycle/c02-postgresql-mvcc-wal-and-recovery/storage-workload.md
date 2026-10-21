---
metadata_version: 1
id: "tycho.page.89cd7853a0d04d78a02a772de59dbf38"
kind: "page"
parent_id: "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/c02-postgresql-mvcc-wal-and-recovery/storage-workload.md"
title: "Workload costs of durable state"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Which write, replication and retention demands constrain storage capacity?"
route_hints:
  questions:
    - "Which write, replication and retention demands constrain storage capacity?"
  prerequisites:
    - "tycho.page.4b98ce4b82bf481b93f2bfce51e882b1"
  related_ids:
    - "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "storage"
    - "workload"
evidence_scope:
  source_ids:
    - "src.postgres17-wal-introduction"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.ddeff7f1556f44f18c67659b73e6e15f; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: "2026-10-20"
content_verified_at: null
---
# Workload costs of durable state

**Owning question:** Which write, replication and retention demands constrain storage capacity?

This page belongs to [V05/C02 — PostgreSQL MVCC, WAL and recovery](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.ddeff7f1556f44f18c67659b73e6e15f:6 -->
## 6. Workload and scale considerations

A physical standby may offload some eligible reads at the cost of freshness and replication resource consumption; it cannot automatically make writes scale out. Index maintenance/WAL volume, long transactions, bulk imports, logical decoding slots, hot tables and checkpoint IO all change performance.

Choosing synchronous replicas affects request tail and failure availability. Choosing async replicas affects acknowledged-write recovery risk. The right configuration follows a **business-approved RPO/RTO**, fault-domain assumptions, load experiments and support capabilities. See the [rollout/recovery chapter](../../../delivery/safe-rollout-and-recovery.md) for source-to-user acceptance distinctions.

**Insufficient evidence:** "We have three copies of PostgreSQL data, so RPO=0, RTO under 30 seconds and no data divergence." No. Need placement, physical/logical mode, sync config, guaranteed/fenced promotion, WAL positions, restore test, integrity and client-level measurements.

<!-- /tycho-question-source -->

## Original workload model — retained log is a recovery budget

Use a fictional change stream that generates ten units of log per second while an archival destination accepts six. During that interval the local archive backlog grows by four units per second. After thirty seconds the additional retained amount is 120 units, before considering any pre-existing backlog. Units are deliberately abstract: they are not bytes per transaction, a PostgreSQL measurement or a sizing recommendation.

If the destination later accepts fourteen units per second while generation remains ten, the backlog drains by four units per second. It therefore needs another thirty seconds to remove that additional backlog, assuming uninterrupted service and no other retention requirement. A healthy-looking average over the entire minute conceals the maximum amount that had to remain available locally.

The architecture question is what happens before that budget is exhausted. Identify which consumers or recovery objectives require the retained history, which failure can pause progress, who observes the backlog and what the permitted degraded action is. Deleting required history, refusing new work and adding storage have different correctness and availability consequences. Do not choose between them from a storage-utilization percentage alone.

The [PostgreSQL 17 WAL introduction](https://www.postgresql.org/docs/17/wal-intro.html) explains log-before-data ordering and recovery from logged changes. It does not establish this fictional generation rate, archive service rate or retention capacity. The arithmetic above is an illustrative queue model; real sizing additionally needs measured log generation, failure duration, recovery membership and the target deployment's actual retention rules.

## Long transactions, deadlocks and online index work

**Enrichment contract:** connect a database symptom to the transaction or maintenance boundary that can explain it. PostgreSQL 17 is the reference; no live server was exercised.

### Original deadlock interleaving

A fictional reservation update changes two workshop rows. Transaction A locks row X and then requests Y. Transaction B locks Y and then requests X. Neither can progress while both retain their first lock. PostgreSQL's explicit-locking chapter explains deadlock detection and abortion of a participating transaction; the application must not assume which contender is chosen.

Use one deterministic lock order where possible. A retry restarts the entire logical transaction after failure, using the declared external-effect contract. Repeating only the last SQL statement on an aborted transaction is not a recovery strategy. Sending an external notification before the transaction commits can make a rolled-back attempt visible; use the [outbox owner](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/README.md).

~~~mermaid
sequenceDiagram
    participant A as Transaction A
    participant D as Database
    participant B as Transaction B
    A->>D: Lock X
    B->>D: Lock Y
    A->>D: Request Y and wait
    B->>D: Request X and wait
    Note over A,B: Cycle requires resolution
    D-->>B: Abort one participant
    D-->>A: Other participant may proceed
~~~

Text alternative: opposite acquisition order can create a lock cycle. The aborted participant shown is illustrative, not a promised victim-selection rule.

### Long snapshots and maintenance

A long-lived transaction may retain an old visibility horizon while the application appears idle. Inspect transaction age and blockers, not just active query duration. MVCC cleanup depends on which row versions can still be observed; the [snapshot/vacuum page](mvcc-snapshots-and-vacuum.md) owns that mechanism.

In a fictional update-heavy table, the application slows while old versions accumulate. Increasing connection capacity can create more concurrent snapshots and contention. It does not release the oldest transaction. Distinguish dead tuples, outdated estimates, I/O pressure and a blocking lock before selecting a remedy. Vacuum itself consumes resources; VACUUM FULL adds a different lock/rewrite contract and is not a generic emergency first step.

### Concurrent does not mean free or wait-free

PostgreSQL 17's CREATE INDEX documentation states that a concurrent build performs additional phases/scans and waits for relevant transactions or snapshots. A failed build can leave an invalid index with update overhead. A unique concurrent build has additional enforcement timing caveats; inspect actual validity and constraint behavior rather than treating command failure as complete rollback of every consequence.

For an original rollout plan, establish a measured maintenance budget; identify old transactions; limit concurrent background work; monitor progress and user latency; and stop under declared conditions. Check index validity and query behavior before relying on the new access path. Select version-specific repair steps with an operator; this prose is not an executable maintenance runbook.

### Evidence and acceptance

Inspected 2026-10-20: [PostgreSQL 17 locking](https://www.postgresql.org/docs/17/explicit-locking.html#LOCKING-DEADLOCKS) (deadlock model); [concurrent index builds](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY) (waits/failure caveats); [Routine vacuuming](https://www.postgresql.org/docs/17/routine-vacuuming.html) (maintenance scope). The fictional interleaving and rollout plan are original reasoning.

Proposed tests: reproduce the two-row lock cycle; retain an old snapshot through a concurrent build; fail a unique build; observe validity and write overhead; compare user latency under a controlled maintenance budget. No SQL, maintenance command or throughput experiment was executed.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](replica-recovery.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](postgresql-wal-replication-and-recovery.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

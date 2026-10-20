---
metadata_version: 1
id: "tycho.page.689c7d51faf1441caa7edfcb6152345e"
kind: "page"
parent_id: "tycho.landing.43b3f0c107e34e5a800d6c1de65069e8"
canonical_path: "book/cases/uber-mysql-to-myrocks.md"
title: "Uber — MySQL to MyRocks: storage engine economics under real workloads"
topic_ids:
  - "architecture-case-studies"
perspectives:
  - "architecture"
  - "migration"
summary: "Reader entry for Uber — MySQL to MyRocks: storage engine economics under real workloads. Scope includes Situation — the legacy architecture and constraint; Chosen architectural change; Migration and validation."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Uber — MySQL to MyRocks: storage engine economics under real workloads?"
  prerequisites: []
  related_ids: []
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Uber"
    - "MySQL"
    - "MyRocks"
    - "storage"
    - "engine"
    - "economics"
    - "under"
    - "real"
    - "workloads"
evidence_scope:
  source_ids:
    - "U03"
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Uber — MySQL to MyRocks: storage engine economics under real workloads

**Case ID:** `case.uber.mysql-to-myrocks` | **Milestone:** M9 E16-05 #118 | **Status:** evidence-bound original draft; technical review pending.  
**Source:** U03 — [original company engineering article](https://www.uber.com/us/en/blog/mysql-to-myrocks-migration-in-uber-distributed-datastores/) (2022 Uber engineering account); primary evidence: Migration overview; datastore trade-offs; operational rollout. Source reuse: original link and attributable paraphrase only; no copied diagrams or pages.

## Situation — the legacy architecture and constraint

A MySQL/InnoDB-backed distributed datastore needed more efficient storage and operational capacity. Selecting the next engine solely from microbenchmarks risked ignoring compaction, write amplification, range-read patterns and recovery behavior under production traffic.

## Chosen architectural change

Uber described changing its distributed-datastore engine from MySQL/InnoDB to MyRocks, which uses a RocksDB-style LSM approach. The change is at an engine/data lifecycle boundary: it does not imply that business APIs changed to an unrelated database product.

```mermaid
flowchart LR
  A[Distributed datastore / InnoDB] --> B[Backfill and validation boundary]
  B --> C[MyRocks / LSM datastore]
```

**Diagram alternative:** Distributed datastore / InnoDB evolved through Backfill and validation boundary toward MyRocks / LSM datastore. This is a deliberately simplified, original decision/transition sketch; it is not the original company's infrastructure map.

## Migration and validation

For a comparable project, pin query distribution and secondary-index assumptions, shadow representative read patterns, validate data consistency across snapshot and live writes, trial write/compaction backlog and staged failover, and retain a rollback before deleting the old representation. These are Tycho's recommended tests, not a reproduced Uber deployment script.

Suggested decision record for a different organization:

| Verification gate | Evidence needed before accepting change | Rollback or hold |
|---|---|---|
| Interface and ownership | Inventory of dependent clients, schema/contract/API compatibility and authorized owner | Preserve existing public contract |
| Representative workload | Actual traffic mix, failure modes and capacity baseline; no invented p99 | Roll back the cohort if its own SLO worsens |
| Correctness | Domain-specific business invariants, dual-state reconciliation if used, idempotent replays | Keep authoritative old representation until proven |
| Operability | Error budgets, runbooks, trace continuity, incident ownership and cost | Stop rollout without a clear incident response owner |

The gates in this table are Tycho's **analytical adaptation**, not an assertion that the source's engineers measured these same four things.

## Negative evidence, costs and alternatives

LSM storage savings can come with different compaction/lookup economics. It would be incorrect to claim MyRocks universally lowers latency, read amplification or SSD wear without a workload-specific comparison. New operational knowledge and restore procedures are an explicit cost.

**Alternatives:** retain/tune the legacy architecture if capacity and correctness already meet requirements; incrementally constrain its internal dependency graph; adopt the described transition only if its own reported bottleneck exists; otherwise conclude **insufficient evidence** rather than copying the brand's solution. These are synthetic architecture alternatives and must not be presented as alternatives the company explicitly evaluated unless the source said so.

## Observed results and temporal validity

The article provides a first-party motivation and migration for the selected distributed datastore; independent cost or p99 equivalence for a different workload is unknown here.

This is a company-reported historical result, not an independently reproduced benchmark. Precise current topology, total engineering effort, p99 and comparative cost must be regarded as **unknown** unless the named primary article supplies them. Do not extrapolate a dated deployment to October 2026 current practice.

## Exact motivation and preparatory version dependency

The [September 1, 2022 first-party report](https://www.uber.com/us/en/blog/mysql-to-myrocks-migration-in-uber-distributed-datastores/) (U03, **Motivation** and **Challenges**) distinguishes **disk-capacity pressure** from a generic demand for a faster database. Schemaless and Docstore stored tens of petabytes and served tens of millions of requests per second in the published operating environment. Disk footprint constrained node density and slowed backup/resynchronization while CPU and memory were underutilized. Node splitting could hit sharding limits, and InnoDB table compression saved only about **5%** because an upstream query-engine layer already compressed payloads. An early MyRocks benchmark reported **over 30% space saving** at acceptable read latency, with the same MySQL client protocol: a **storage-engine replacement**, not a client API rewrite.

The source reports a prerequisite that is easy to omit from a short modernization plan: Uber initially ran **MySQL 5.7** while its chosen XtraBackup tooling supported MyRocks beginning with **MySQL 8.0**. That prerequisite version upgrade took **more than a year**. Reported blockers included increased 8.0 memory use, changed optimizer plans, slow data-dictionary population on installations with many tables, stalls during resource release and an InnoDB index/tablespace corruption defect. These were encountered during the upgrade and should not all be falsely attributed to the later RocksDB engine. [U03, **MySQL 8.0 Upgrade**].

## Two distinct migrations and their source-reported safety gates

The underlying datastore used shards mapped to physical partitions, with multiple Raft-backed replicas within one region and replication to other geographic regions. The 5.7→8.0 binary upgrade followed **follower → other followers → leader, then next partition, then next region**. An engine migration, however, needed a **newly built replica and table conversion** rather than just replacing a binary. The difference matters to availability, data checks and how rollback is possible.

| Gate in U03 | Source-reported sequence | What can still fail |
|---|---|---|
| Candidate build | Add a MySQL 8.0 node by XtraBackup; collect table count and checksums | Snapshot/backup compatibility and the time required to resynchronize |
| Engine conversion | Convert user tables to RocksDB with bulk-load mode and worker threads | Out-of-memory interruption; source authors found **missing tables after restart** |
| Post-conversion evidence | Compare table count/checksums, regenerate table statistics, replay real queries | Changed optimizer plan/performance; one issue yielded a **different result for the same SQL** across engines |
| First partition | Add second, then third MyRocks follower, temporarily **3 MyRocks + 2 MySQL** replicas | Promotion correctness and new-engine read/write behavior under real traffic |
| Leader handoff | Promote MyRocks leader to accept writes, remove old-engine replicas one by one | A successful follower check is not proof of leader/write equivalence |
| Region gate | Convert other partitions in region, then pause and compare **latency, errors, CPU and I/O across regions** | Regression relative to a MySQL region; remote MySQL region retained as a failover option |
| Other regions | Once first-region results acceptable, replace nodes in subsequent regions without extra capacity | Earlier validation may not represent regional workload differences |

**Primary source anchors:** U03, **Upgrade and Migration**, **MySQL 8.0 Upgrade**, **MyRocks Migration**. The sequence is a reported production method. The article does not provide a reproducible code revision or recovery point objective for every intermediate state.

## The two failure findings that invalidate a purely structural cutover

In the article, table conversion interrupted by **out-of-memory during handler commit** could leave a table missing after restart. Before/after table counts and checksums detected this, rather than treating an ostensibly completed ALTER as the only correctness oracle. In another case, a reproduced SQL request produced a **different result** under the two engines (the cited defect **PS-7722**). This is stronger negative evidence than generic concern over different storage-engine performance: **identical query text and client API did not guarantee identical semantics**.

Those observed problems justify an explicit **value-level read oracle** as well as backup/row-count validation and runtime query replay. A matching table checksum proves only the checked representation under its defined snapshot; a query may diverge due to engine behavior or plan changes after statistics are rebuilt. These statements are a Tycho analytical consequence of the described failures, not a claim Uber used an unpublished complete formal-verification procedure.

## Costs, measured outcomes and historical scope

The publisher reports **over 30% less disk usage across migrated workloads**, but admits **higher CPU and disk I/O on some instances**. A capacity reduction without matching CPU/compaction/SSD-wear and recovery evidence is not a universal reduction in total cost of ownership. As of the **2022** publication, Uber reported **all Schemaless** migrated and **only some Docstore** instances; continued Docstore migration, performance tuning and stronger MyRocks backup/recovery remained future work. Do not reinterpret the article as a 2026 all-fleet state, a free 30% TCO reduction or a controlled p99 improvement.

| Analytical alternative for another legacy store | When to test | A reason not to select it |
|---|---|---|
| Keep InnoDB and rebalance/split nodes | Small capacity problem with predictable key distribution | Maximum shard/node count and operational rebalancing can become bottlenecks |
| Tune compression and data lifecycle | Data is not already heavily compressed; archival policy permits retention reduction | Compression may yield little extra benefit and can increase CPU |
| Move the storage engine behind unchanged SQL APIs | Disk efficiency dominates, and engine parity can be proven for actual query mix | Differing query results, compaction costs, backup gaps, or SQL incompatibility |
| Rewrite client/data model instead | Current API itself prevents domain correctness or scale | Much larger release surface with no guarantee of better persistence economics |

The alternatives are **Tycho analysis**, not an assertion that Uber empirically trialed all four. Its article does explicitly describe trying compression and evaluating MyRocks.

## Reversible transfer and refusal criteria

For a different Raft-replicated MySQL store, perform a **separate version-upgrade gate** before engine conversion; pin binary/client/backup revisions and capture representative SQL, query plans, object identity, checksums and per-class p95/p99. Promote one converted follower only after backup recovery, complete table enumeration, query-value comparisons and plan/capacity checks; retain another region on the old engine until read/write, replica-lag and failover tests pass. Test OOM during conversion and interrupted promotion, not only clean startups. Only remove the last old-region escape path with a documented recovery/forward-fix procedure.

**Stop conditions:** missing table after ALTER, different query result on replay, backup incompatibility, unsustainable CPU or compaction I/O, unexplained read tail, or a rollback whose old-engine copy can no longer represent accepted new writes. If actual workload/recovery evidence cannot be obtained, return **insufficient evidence** instead of selecting an LSM engine from a public percentage.

## Applicability to legacy modernization

Consider LSM engines when persistent footprint and sustained ingestion dominate and the team can operate compaction/recovery. Prefer retaining a familiar B-tree engine when read behavior, licensing, replication or troubleshooting costs make that safer. Before a roadmap is approved, require a baseline with data ownership and blast radius, a comparison to a smaller intervention, and measurable acceptance gates. An agent should retrieve this case as **evidence for conditions and counterconditions**, not as a universal preferred architecture.

**Provenance:** [U03 primary](https://www.uber.com/us/en/blog/mysql-to-myrocks-migration-in-uber-distributed-datastores/), sections Migration overview; datastore trade-offs; operational rollout. Cross-case comparisons must retain the original company's architecture and historical observation window. **Case review:** not yet independently approved under #121.

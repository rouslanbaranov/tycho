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

## Applicability to legacy modernization

Consider LSM engines when persistent footprint and sustained ingestion dominate and the team can operate compaction/recovery. Prefer retaining a familiar B-tree engine when read behavior, licensing, replication or troubleshooting costs make that safer. Before a roadmap is approved, require a baseline with data ownership and blast radius, a comparison to a smaller intervention, and measurable acceptance gates. An agent should retrieve this case as **evidence for conditions and counterconditions**, not as a universal preferred architecture.

**Provenance:** [U03 primary](https://www.uber.com/us/en/blog/mysql-to-myrocks-migration-in-uber-distributed-datastores/), sections Migration overview; datastore trade-offs; operational rollout. Cross-case comparisons must retain the original company's architecture and historical observation window. **Case review:** not yet independently approved under #121.

# Decision Playbook — Data migration: compatibility, shadow differences and authoritative cutover

**ID:** `decision.data-migration-shadow-reconcile` | **Owner:** M9 E16-06 #119 | **State:** original analytical draft, independent reviewer pending.  
**Method:** compare contrasting historical cases; distinguish each company's *reported past decision* from the **synthetic** decision below. No company is claimed to have assessed the other firm's choices.

## Synthetic legacy system and decision problem

An online billing platform must move active invoice state out of a shared Customer record without losing updates, while a second analytics workflow may change how immutable Cassandra snapshots are converted to Iceberg. Transactionality and equality are different for these flows.

## Contrasting historical evidence

| Actual company case | What its primary source does and does not establish |
|---|---|
| [Stripe](../stripe-online-subscriptions-migration.md) | ST01: four-phase dual-write/read/write/retire and Scientist comparison |
| [Netflix](../netflix-casspactor-shadow-migration.md) | N11: row-set differences and cohort selector/fallback |
| [Uber](../uber-mezzanine-pg-to-schemaless.md) | U02: query/ID seam, backfill and mirrored writes |
| [Discord](../discord-cassandra-scylladb-messages.md) | DI01: token range checkpoints, tombstone final-range blocker |
| [Meta](../meta-ingestion-shadow-migration-lifecycle.md) | ME03 (May 2026): per-job shadow **→ reverse shadow (new writes production, old writes shadow) → cleanup**, with CDC bad-partition containment and rollback |

**Why the apparent conflict is useful:** Stripe's Scientist compares online read behavior and shifts **all reads before all writes** to a new mutable subscription table. Netflix compares **C−M and M−C** on materialized batch outputs while preserving user-job contracts; Uber created an identifier/client-query seam before trip-store migration. Meta's warehouse ingestion instead preserves the **old job running as shadow *after* the new job starts writing production**, then retires it only after renewed quality/resource checks. Discord demonstrates why migration progress at 99.9999% is not source-independent proof of correctness. **Do not silently apply Stripe's write-path cutover order to Meta's CDC job authority transfer.**

## Decision tree and chosen ADR

```mermaid
flowchart TD
  A[Legacy constraints / actual workload] --> B{Evidence sufficient?}
  B -->|no| C[Measure or preserve current state]
  B -->|yes| D[Select smallest reversible change]
  D --> E[Shadow / canary / verification]
  E -->|gates pass| F[Incrementally adopt]
  E -->|regression| G[Rollback and record contradiction]
```

**Text alternative:** collect requirements and legacy workload evidence first. When evidence is missing, measure rather than select a fashionable pattern. When evidence suffices, prefer the smallest reversible change, run shadow/canary validation, adopt only after acceptance gates, otherwise roll back.

**ADR — Proposed for the synthetic system, not a historical company ADR.**  
**Status:** proposed, subject to measured baseline and security review.  
**Context:** An online billing platform must move active invoice state out of a shared Customer record without losing updates, while a second analytics workflow may change how immutable Cassandra snapshots are converted to Iceberg. Transactionality and equality are different for these flows.  
**Decision:** Use phased expand/dual-write/backfill/shadow-reads/cutover/contract for mutable billing data, and shadow-output set equality plus fallback for immutable batch data. Define one authoritative state at each transition; never assume counts or full-backup metadata alone prove business equivalence.  
**Rejected for now:** a large irreversible rearchitecture without a verified bottleneck, tests, source/data provenance or fallback.  
**Consequences:** additional migration observability and temporary dual-state complexity are acceptable while the rollout is reversible; these costs must be budgeted explicitly.

## Applicability and counterindications

**Use this evidence when:** a real system has the same dominant constraint, the relevant execution model/data semantics have been measured and its team can operate the new architecture.

**Do not generalize when:** Two independently written stores can diverge with retry races or partial failure. Identical outputs can still reflect a shared semantic bug; backfills need live-write ordering. Avoid a big-bang cutover when you cannot reconcile every mutation class.

**Independent decision dimensions to measure:** Missing/extra rows per cohort and snapshot, referential/business invariants, shadow mismatch root causes, dual-write conflict count, backlog age, rollback recovery time.

## Modernization plan

Version contracts → establish old source authority → implement dual-state writes → backfill snapshot IDs/checkpoints → compare old/new values with temporal alignment → switch low-risk reads → invert writes under canary → decommission old only after proven zero callers.

**Reversal triggers / insufficient evidence:** If the new model cannot preserve legacy business semantics, redesign domain/API contract with consumers before cutover rather than forcing opaque equality.

## Data-authority decision guard: Stripe versus Meta

**Stripe ST01 (2017):** expand/dual-write from old Customer array to new Subscription rows; backfill; use Scientist read comparisons; route **all reads to the new representation before changing write authority**, then remove obsolete writes and data after callers are migrated.

**Meta ME03 (2026):** output-equivalence gates on shadow ingestion; switch the **new ingestion job to the production table while the old job begins producing shadow output**; keep comparing and backfilling; on CDC bad-partition detection stop unsafe delta propagation or reconstruct an affected target snapshot and roll back; only then retire the old job. This is an **ingestion job** lifecycle with full/delta/target partitions, not a two-representation online billing schema cutover.

**Transferred decision test:** ask which representation/job is authoritative *at each phase*, whether former execution remains runnable after authority switches, which exact mismatch triggers rollback, and how CDC errors avoid contaminating later partitions. A row-count equality alone cannot answer those questions. For any other legacy system, choose stages from its own data-write semantics and consumer contracts; the above are historically observed, not a universal migration state machine.

## Failure analysis and evidence provenance

The company cases are not A/B comparisons of two architectures under one workload. Published outcomes describe different organizations, production periods, release versions, traffic mixes and operating constraints. This playbook compares *mechanisms and constraints*, not raw numerical results across companies.

Before passing a recommendation to Rocinante, an agent should return: legacy facts, requirement/SLO evidence, selected/avoided pattern, evidence rows with company/date/source ID, alternative mechanism, caveats, a reversible transition sequence, what would falsify the choice, and whether human review is needed. Never invent what original engineering teams rejected.

Sources are linked through each original case page above, ultimately referring to [the M9 public source register](../../../sources/REAL_WORLD_ARCHITECTURE_CASES.md). All analytical ADRs are original Tycho examples. **Independent review:** #121, not yet completed.

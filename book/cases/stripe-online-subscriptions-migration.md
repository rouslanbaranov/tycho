# Stripe — four-stage online migration of subscription data ownership

**Case ID:** `case.stripe.online-subscriptions` | **Milestone:** M9 E16-05 #118 | **Status:** evidence-grounded draft, pending reviewer.  
**Public primary:** ST01 [official engineering account](https://stripe.com/blog/online-migrations), 2017-02-02, Jacqueline Xu / Stripe; source anchors: A pattern for online migrations; Part 1: Dual writing; Part 2: Changing all read paths; Part 3: Changing all write paths; Part 4: Removing old data. No private materials or copyrighted graphics reproduced.

## Original pressure and baseline

Early Stripe billing represented subscriptions on Customer records. As subscriptions became plural and more complex, updating an entire Customer and scanning embedded subscription structures hampered features. A simultaneous rewrite of all the dependent services would threaten live financial correctness and downtime.

## Architecture shift and ownership

Stripe moved subscriptions into a dedicated table with a four-phase compatibility path: dual-write and backfill; switch reads after shadow comparison; redirect writes so the new table becomes authoritative; retire the old field. The method separates storage-copy existence from actual read/write ownership transfer.

```mermaid
flowchart LR
 A[Subscriptions embedded in Customer] --> B[Dual-write + backfill + Scientist comparisons]
 B --> C[Separate authoritative Subscriptions table]
```

**Text alternative:** Subscriptions embedded in Customer, through Dual-write + backfill + Scientist comparisons, evolved toward Separate authoritative Subscriptions table. Diagram is a simplified original architectural transition, not a provider topology inventory.

## Execution stages, validation and reversibility

Source details matter: Stripe copied missing records with offline Hadoop/MapReduce snapshots rather than loading live databases with full table scans, and used GitHub Scientist to run production-read comparisons while serving the old path until verified. After switching to new reads it incrementally changed mutation sites, then made old-field access throw errors and removed old data. This is a reported real sequence, not generic speculation.

A **synthetic migration readiness checklist** for applying the lesson elsewhere (not a claim that the original authors used this exact checklist):

1. Define the old and new ownership boundaries and which API/data contract must stay invariant throughout coexistence.
2. Capture representative traffic and error distributions, not solely a success-path benchmark. Specify performance baselines with release version, dataset and sample size.
3. Compare old/new result sets and temporal semantics; test retried writes, old clients, skipped batches and partial deployment.
4. Observe canary failure and rollback behavior with exact data-authority ordering. Do not retire the legacy system before provable invariants hold.
5. Retest under realistic resource limits, hot keys and failure injections. A change in infra topology is not a substitute for demand shaping.

## Measured or reported outcome

Stripe reports an online migration without downtime while API behavior remained stable; the article gives process detail but not a transferable quantified p99 or labor-saving gain. No claim of independent proof is made.

## Failed assumptions and when not to transfer the design

A two-table representation may diverge during retries, time windows or schema-dependent business logic. Comparing only counts is insufficient; read results must match under a defined subscription identity and temporal snapshot. Switching new writes before all old reads are migrated risks inconsistencies.

**Architecture choice:** Use this for high-value evolving data models with many callers when existing transactions must remain online and compatible. Reject if you cannot define reconciliation or reversibly switch authoritative reads/writes.

A lesser change (query optimization, archive policy, package boundary, deploy-tuning) is a valid alternative when it meets SLOs and costs less. A counter-architecture for this case requires workload, team skills, and service-level constraints; do not infer that the original company explicitly evaluated every alternative in this paragraph.

## Provenance and acceptance boundary

Evidence is company-authored and scoped to the publication date and sections: [ST01](https://stripe.com/blog/online-migrations), **A pattern for online migrations; Part 1: Dual writing; Part 2: Changing all read paths; Part 3: Changing all write paths; Part 4: Removing old data**. Numerical results, where stated, are publisher-reported; no Tycho benchmark, source reproduction or copyright permissions inferred. Source status must be reconciled with [the candidate audit](../../sources/REAL_WORLD_CASES_CANDIDATE_AUDIT.md) and E16-01 #114. This case remains a draft until independent #121 correctness and source review.

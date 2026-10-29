# R5 external review remediation

Review report: `authoring/ai-reviews/2026-10-27-sufficient-batch-review-codex.md`

Reviewed HEAD: `ca77efd2`. Verdict: reject. No entry is promoted; `sufficient: 0`.

## Status

| Pattern | Dimension | Severity | Status |
|---|---|---|---|
| `tycho.pattern.gateway-offloading` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.backend-for-frontend-bff` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.transactional-outbox` | decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.cache-invalidation` | technical_sufficiency | major | downgraded to partial |
| `tycho.pattern.stale-while-revalidate` | technical_sufficiency | major | downgraded to partial |
| `tycho.pattern.partitioning` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.quorum-based-reads-writes` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.backup-pitr-and-restore` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.deadline-propagation` | technical_sufficiency | major | downgraded to partial |
| `tycho.pattern.graceful-degradation` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.load-shedding` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.rate-limiting` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.hedged-requests` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.causal-ordering` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.causal-ordering` | regression_consistency | major | B12-RESULT created in 365adeb6 |
| `tycho.pattern.cell-based-architecture` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.shuffle-sharding` | decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.deployment-stamps` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.geode` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.static-content-hosting` | technical_sufficiency | major | downgraded to partial |
| `tycho.pattern.tenant-based-resource-isolation` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.immutable-infrastructure` | technical_sufficiency | major | downgraded to partial |
| `tycho.pattern.zero-trust-architecture` | technical_sufficiency,decision_sufficiency | major | downgraded to partial |
| `tycho.pattern.structured-logging` | technical_sufficiency | major | downgraded to partial |
| `artifact.delivery-evidence` | regression_consistency | major | fixed in 365adeb6/790f94b2 |
| `artifact.batch-plan` | regression_consistency | major | fixed in 365adeb6/790f94b2 |

## Required remediation

- `tycho.pattern.gateway-offloading` / technical_sufficiency,decision_sufficiency: Downgrade the affected dimensions to partial and remove the entry from review-ready, or bind exact admitted-source passages supporting the stated security failure and alternatives. Regenerate B01-RESULT.json afterward.
- `tycho.pattern.backend-for-frontend-bff` / technical_sufficiency,decision_sufficiency: Narrow the claims to the quoted behavior or add exact bindings for drift recovery and the additional boundary requirements; otherwise mark those dimensions partial and update B01-RESULT.json.
- `tycho.pattern.transactional-outbox` / decision_sufficiency: Bind a passage supporting the actual competing alternative and reversal condition, or rewrite the owner/card alternative to the supported comparison and mark the current alternative partial until reviewed.
- `tycho.pattern.cache-invalidation` / technical_sufficiency: Split or narrow the claims to the exact supported behavior, or add exact bindings for versioning, durable retry, and versioned-key alternatives; downgrade unsupported dimensions meanwhile.
- `tycho.pattern.stale-while-revalidate` / technical_sufficiency: Remove the unsupported single-owner and observability assertions from the bound claims or supply separate exact evidence; mark affected dimensions partial before re-review.
- `tycho.pattern.partitioning` / technical_sufficiency,decision_sufficiency: Bind the pruning and alternative assertions to exact passages or narrow the claims. Recompute review-ready status after each dimension has direct support.
- `tycho.pattern.quorum-based-reads-writes` / technical_sufficiency,decision_sufficiency: Downgrade invariant and failure_recovery to partial or bind a source covering joint membership and version selection. Do not infer membership-transition safety from ordinary R/W overlap.
- `tycho.pattern.backup-pitr-and-restore` / technical_sufficiency,decision_sufficiency: Separate sourced PITR mechanics from synthetic operational guidance. Add exact sources for restore validation, drills, and replica limitations, or mark those dimensions partial.
- `tycho.pattern.deadline-propagation` / technical_sufficiency: Resolve the relative-duration versus absolute-deadline contradiction and bind the transport-specific behavior actually claimed. Reclassify failure_recovery until its stated failures are directly evidenced.
- `tycho.pattern.graceful-degradation` / technical_sufficiency,decision_sufficiency: Use claims matching the cited failure and alternative passages, or add exact evidence for correctness disclosure and the named alternatives; otherwise downgrade those dimensions.
- `tycho.pattern.load-shedding` / technical_sufficiency,decision_sufficiency: Rebind the bottleneck-placement and governance claims or narrow them to utilization-triggered task protection and criticality trade-offs. Mark unsupported dimensions partial.
- `tycho.pattern.rate-limiting` / technical_sufficiency,decision_sufficiency: Add direct evidence for each rate-limit parameter, failure mode, and alternative, or reduce the claims and downgrade the dimensions before review-ready classification.
- `tycho.pattern.hedged-requests` / technical_sufficiency,decision_sufficiency: Bind each safety precondition and competing alternative explicitly, or narrow the owner/card claims and mark invariant, failure_recovery, and alternative partial.
- `tycho.pattern.causal-ordering` / technical_sufficiency,decision_sufficiency: Narrow the failure claim and distinguish the required model from mechanisms that may implement it, or add exact sources. Reclassify unsupported dimensions before review-ready status.
- `tycho.pattern.causal-ordering` / regression_consistency: Complete the B12 binding audit and commit a result artifact derived from B12.json and owner-units, or remove Causal Ordering from the review-ready set until that result exists.
- `tycho.pattern.cell-based-architecture` / technical_sufficiency,decision_sufficiency: Bind shared-dependency failure behavior and the actual competing alternative, or narrow and downgrade the affected dimensions.
- `tycho.pattern.shuffle-sharding` / decision_sufficiency: Add exact fixed-cell comparison evidence or replace the alternative with one actually supported by the cited unit; mark alternative partial until then.
- `tycho.pattern.deployment-stamps` / technical_sufficiency,decision_sufficiency: Supply separate bindings for the missing invariant components and the cell comparison, or narrow the claims and downgrade invariant and alternative.
- `tycho.pattern.geode` / technical_sufficiency,decision_sufficiency: Bind the stale-route, freshness, fencing, and active-passive assertions directly, or remove them and mark the dimensions partial.
- `tycho.pattern.static-content-hosting` / technical_sufficiency: Split the failure claim and retain support only for purge behavior, or add exact evidence for cold-cache and origin-failover behavior before restoring supported state.
- `tycho.pattern.tenant-based-resource-isolation` / technical_sufficiency,decision_sufficiency: Separate deployment isolation from application-level tenant scoping and testing. Bind each claimed layer explicitly or downgrade mechanism, invariant, and failure_recovery.
- `tycho.pattern.immutable-infrastructure` / technical_sufficiency: Bind digest identity, drift detection, and reproducible rebuild behavior directly, or narrow the claims and downgrade invariant and failure_recovery.
- `tycho.pattern.zero-trust-architecture` / technical_sufficiency,decision_sufficiency: Bind the named failures and alternatives exactly or narrow the entry to the continuous contextual-authorization behavior supported by ASVS and mark other dimensions partial.
- `tycho.pattern.structured-logging` / technical_sufficiency: Separate schema stability from redaction and sensitive-data controls. Add exact admitted evidence for the latter or downgrade invariant and failure_recovery.
- `artifact.delivery-evidence` / regression_consistency: Regenerate delivery evidence against a declared content commit containing the reviewed batch artifacts, update counts and limits from that commit, and avoid describing an older snapshot as current.
- `artifact.batch-plan` / regression_consistency: Update the plan to an accurate as-of lifecycle state, record completed and missing results explicitly, and regenerate any derived status rather than retaining pilot-era status as current.

## Limits

Downgrading a dimension is containment, not closure. Closure requires either a narrowed claim or an exact admitted binding, then a fresh external review. The two entries without R5 findings (Valet Key and SLI/SLO and Error Budgets) still need a fresh review before any promotion.

## Focused survivor review — 2026-10-27

Report: `authoring/ai-reviews/2026-10-27-sufficient-survivors-review-codex.md`.
Reviewed HEAD: `3f965e0d`. Verdict: **reject**.

Both survivors were downgraded:

- Valet Key: invariant, failure_recovery and alternative -> partial;
- SLI/SLO and Error Budgets: all four dimensions -> partial.

No review-ready entries remain. Other open findings:

- `edition/patterns/sufficient-review-reconciliation.v1.json` still records
  `derived_state: promoted-after-remediation` for both entries. The reviewer called this an
  unsupported promotion assertion. It is a historical agent-review reconciliation artifact,
  not the sufficient promotion file, but the state label must be corrected or explicitly
  bounded before any later promotion review. **Open.**
- The SLI/SLO failure_recovery quote transcribes `client -side`; the current public page reads
  `client-side`. The pinned representation must be checked before changing the exact quote.
  **Open, minor.**

## Shuffle Sharding focused review — 2026-10-27

Review: `/tmp/shuffle-review.json` at HEAD `73c07e41`; verdict **reject**.
Findings: unsupported `random subset`/hash-based qualifiers, generalized recovery, and an
unsupported fixed-shard alternative. The card edits were reverted; all four dimensions are
`partial`, and Shuffle Sharding is remediation again. The report is retained in the R5
survivor/batch evidence trail and is not a promotion.

Final batch state after R5 and focused reviews: **0 review-ready**, **0 sufficient**,
**0 promotions**. All 145 entries are rejected or partial-bounded.

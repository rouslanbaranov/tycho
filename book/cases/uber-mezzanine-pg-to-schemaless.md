# Uber — Project Mezzanine: moving trip data behind a compatibility seam

**Case ID:** `case.uber.mezzanine-trip-data` | **Milestone:** M9 E16-05 #118 | **Status:** evidence-bound original draft; technical review pending.  
**Source:** U02 — [original company engineering article](https://www.uber.com/us/en/blog/mezzanine-codebase-data-migration/) (historical Uber engineering account); primary evidence: From SQLAlchemy to Schemaless; Changing trip ids; Backfilling; Mirrored Writes; Validation. Source reuse: original link and attributable paraphrase only; no copied diagrams or pages.

## Situation — the legacy architecture and constraint

Trip identifiers and SQLAlchemy queries tied large parts of Uber's backend to PostgreSQL and implicit relational relationships. Extracting the storage engine without first changing those application assumptions would expose callers to incompatible query shapes and identifier semantics.

## Chosen architectural change

A tripstore library presented a narrower compatible interface and could dispatch to PostgreSQL or Uber's Schemaless store. The project converted sequence identifiers to UUIDs, remodeled trip data, backfilled prior data, mirrored writes, rewrote queries and validated behavior. Schemaless intentionally did not support all relational joins.

```mermaid
flowchart LR
  A[Direct SQLAlchemy + PostgreSQL trips] --> B[Tripstore compatibility API / write mirror]
  B --> C[Sharded Schemaless data]
```

**Diagram alternative:** Direct SQLAlchemy + PostgreSQL trips evolved through Tripstore compatibility API / write mirror toward Sharded Schemaless data. This is a deliberately simplified, original decision/transition sketch; it is not the original company's infrastructure map.

## Migration and validation

The source enumerates explicit milestones: change trip IDs, remodel columns, backfill, mirror writes, rewrite queries, and validate repeatedly. In addition, a new implementation should define consistency under write races, idempotent retries and observed counters before switching reads; those latter controls are Tycho analytical gates rather than a blanket claim about Uber's exact implementation.

Suggested decision record for a different organization:

| Verification gate | Evidence needed before accepting change | Rollback or hold |
|---|---|---|
| Interface and ownership | Inventory of dependent clients, schema/contract/API compatibility and authorized owner | Preserve existing public contract |
| Representative workload | Actual traffic mix, failure modes and capacity baseline; no invented p99 | Roll back the cohort if its own SLO worsens |
| Correctness | Domain-specific business invariants, dual-state reconciliation if used, idempotent replays | Keep authoritative old representation until proven |
| Operability | Error budgets, runbooks, trace continuity, incident ownership and cost | Stop rollout without a clear incident response owner |

The gates in this table are Tycho's **analytical adaptation**, not an assertion that the source's engineers measured these same four things.

## Negative evidence, costs and alternatives

Dual writes can diverge; removing JOIN capability can force surprising API changes. A backfill that succeeds on row counts but mishandles key relationships is not correct. The resulting system remains subject to shard and indexing operational costs.

**Alternatives:** retain/tune the legacy architecture if capacity and correctness already meet requirements; incrementally constrain its internal dependency graph; adopt the described transition only if its own reported bottleneck exists; otherwise conclude **insufficient evidence** rather than copying the brand's solution. These are synthetic architecture alternatives and must not be presented as alternatives the company explicitly evaluated unless the source said so.

## Observed results and temporal validity

Uber reports a completed trip-data store migration and interface-seam pattern. The published narrative is not a reproducible, environment-independent proof of lower database costs or universally safe dual writes.

This is a company-reported historical result, not an independently reproduced benchmark. Precise current topology, total engineering effort, p99 and comparative cost must be regarded as **unknown** unless the named primary article supplies them. Do not extrapolate a dated deployment to October 2026 current practice.

## Applicability to legacy modernization

Prefer API strangling and explicit change of identifiers when a storage migration crosses many teams. If the original relational store still meets capacity and operational requirements, a new distributed engine may not justify this migration. Before a roadmap is approved, require a baseline with data ownership and blast radius, a comparison to a smaller intervention, and measurable acceptance gates. An agent should retrieve this case as **evidence for conditions and counterconditions**, not as a universal preferred architecture.

**Provenance:** [U02 primary](https://www.uber.com/us/en/blog/mezzanine-codebase-data-migration/), sections From SQLAlchemy to Schemaless; Changing trip ids; Backfilling; Mirrored Writes; Validation. Cross-case comparisons must retain the original company's architecture and historical observation window. **Case review:** not yet independently approved under #121.

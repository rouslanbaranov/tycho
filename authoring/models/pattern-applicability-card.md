# Pattern applicability and contraindication cards — decision contract

> Tycho Issue [#19](https://github.com/rouslanbaranov/tycho/issues/19), E01-03 / M1. Original authoring contract, 2026-10-19. This is a **human/agent decision model**, not an executable architecture recommender, a universal taxonomy, a vetted pattern catalogue or an accepted JSON Schema.

## Purpose and canonical ownership

An architecture pattern is useful only under a defined problem, workload, correctness invariant and operating environment. A card describes **when to consider the pattern and when to reject or defer it**, its mechanism-specific evidence, alternatives, costs and a falsifiable validation experiment. No pattern is `best` across unspecified workloads. A software product is an implementation candidate, not a synonym for a pattern; a broad architecture style is not the same as a protocol mechanism.

Related canonical sources: the [requirements/workload model](requirements-workload-profile.md), [legacy baseline model](legacy-modernization-profile.md), [queueing research](../../book/performance/queueing-littles-law.md) and [outbox and idempotency pilot](../../book/distributed/transactional-outbox-and-idempotency.md). Use the [blank reusable template](../../templates/pattern-applicability-card.md). The worked [admission-control example](../../examples/synthetic-admission-control-card.md) is fiction.

## Card identity and classification

| Field | Requirement |
|---|---|
| `pattern_id`, `revision` | Stable card ID and revision, independent of file name and vendor/product |
| `name` and `class` | Human-readable concept and one provisional class: architecture style, architectural pattern, integration pattern, resilience mechanism, data pattern, deployment pattern |
| `canonical_owner` | Single existing book page that owns technical guarantees, normal/failure behavior and evidence; don't reimplement it in each card |
| `problem` | Falsifiable engineering issue, not a technology preference |
| `requirements` and `workload_envelope` | Refer to measured/proposed workload scenario, objective IDs, version and time boundaries |
| `evidence_status` | Public-source passages actually inspected, synthetic inference, reproducible experiment, or unknown; keep separate |
| `review_status` | Draft, self-checked, independent-reviewed by identified reviewer or accepted by explicit authority; do not infer from GitHub merge |

Class labels are an initial editorial taxonomy, **not** final frontmatter enums, semantic graph types or schema validation. #32–#34 own formal metadata semantics.

## Applicability as evidence-gated predicates

Write every material predicate using four parts: **condition**, **evidence**, **why it matters**, **test or recheck**. Example predicate: `The offered burst lasts longer than an autoscaler warm-up` is *unknown* without offered-arrival traces and the actual provisioning delay. Missing evidence should become `measure first`, not `applicable`.

A card must provide:

1. **Good-fit conditions**: workload and business capabilities under which this mechanism could satisfy a named objective, including exact assumptions.
2. **Prerequisites**: ownership, operational skill, observability, supporting contracts, security constraints and platform/version features.
3. **Hard contraindications**: a condition that would violate an invariant or hard constraint even when throughput/cost look attractive. Distinguish a proven contraindication from an unknown risk requiring experimentation.
4. **Trade-offs and failure modes**: new operational components, coordination/consistency costs, overload response and recovery; identify risks introduced by adoption.
5. **Alternatives including retain/simplify**: same scenario boundaries and comparable goals, not marketing claims or numerical rankings.
6. **Combinations**: constraints on layering with retries, transactions, caching or additional isolation. Extra patterns may amplify rather than mitigate failure.
7. **Implementation/version scope**: only if a specific vendor/library feature is referenced; separate general intent from version-specific behavior.
8. **Migration/transition**: current-state prerequisites, coexistence, data compatibility, reversibility and go/no-go gates.

## Decision statuses and safeguards

| Decision status | Meaning | Next step |
|---|---|---|
| `candidate` | No proven violation, but measurable benefit not validated | Compare a simpler option under same workload |
| `applicable-under-conditions` | Exact evidence supports conditions; risk and constraints remain explicit | Carry out defined validation before production adoption |
| `contraindicated` | A proven hard invariant/constraint fails | Reject for this scenario and log the disqualifying evidence |
| `insufficient-evidence` | Critical fact unknown or only synthetic/model-based | Measure, inspect code/source or investigate assumptions |
| `not-required` | Problem absent or smaller existing design meets goals | Retain/simplify, document why extra complexity adds no value |

**No score overrides a hard constraint.** Confidence is claim-specific and time-bound; a checked documentation entry does not establish performance under an unknown workload. A card can present several conditional outcomes for different scenarios rather than one global status.

## Architecture comparison and falsification

At minimum compare the proposed pattern to *retain existing design / tune simplest boundary* and one distinct alternative. Hold constant the user outcome, correctness invariant, offered arrivals, downstream resource budget and failure experiment. Record cost/operations and rollback consequences. Define rejection conditions **before** testing; successful request rates alone cannot hide errors, rejected demand or incorrect operations.

A card's `decision_question` is answered by a small evidence matrix:

| Option / scenario | Targeted benefit (hypothesis) | Failure and correctness conditions | Required observation | Possible rejection |
|---|---|---|---|---|
| Maintain current path | Lowest change risk, if existing limits still meet goals | Existing overload may remain | Workload + p99 + errors + failures | Constraint or SLO violates gate |
| Proposed pattern | Benefit conditional on identified mechanism | New overload, state or ordering constraints | Controlled same-budget comparison | Improvement disappears or invariant fails |
| Simpler/distinct alternative | Might meet goal with less operational burden | Its own failure domain | Identical scenario and rollout constraint | No credible marginal benefit |

If experiments cannot reproduce the real operating envelope or primary source constraints are missing, output must be `insufficient-evidence` with an explicit action, not an invented selection.

## Evidence and provenance standards

- Cite **exact independently public inspected sections/revisions**; a source register discovery entry is not technical proof. For source-linked claims, separate documentation facts from Tycho's operational recommendation and from synthetic numerical assumptions.
- Keep quantitative thresholds scenario-local. "Use microservices beyond N users" and "always shard beyond N RPS" are prohibited universal thresholds.
- No employer/private corpus details, unauthorized book excerpts, borrowed diagrams or unverified production metrics.
- Each technical Mermaid diagram must be original, scoped and accompanied by a text alternative. Cards should **link** canonical technical pages rather than duplicate source diagrams.
- When a source becomes outdated, record `last_validated`, affected claims and a specific re-verification trigger instead of silently asserting continuous validity.

## Structural and semantic acceptance checklist

- Card ID/class/canonical owner/revision; correct existing relative links, no dangling proposed pages.
- Explicit workload/requirements and hard gates, assumptions and `unknown` fields.
- Good-fit *and* disqualifying conditions, alternatives, failure/recovery, operational cost.
- Versioned source-to-claim ledger, actual inspection scope, counterexample or `not-required` path.
- Falsifiable experiment, measurable expected and rejection observations, migration/rollback where appropriate.
- True check/review state with no fabricated deployment, benchmark or human approval.

**Implementation boundary:** Formal frontmatter/schema validators, a complete graph of applicability, AI recommendation engine and independent review remain separate backlog work. This deliverable establishes a documented method plus one bounded pilot, not a fully evaluated architecture-selector.

# Candidate comparison and evidence-backed architecture decisions

> Tycho E01-04 [#20](https://github.com/rouslanbaranov/tycho/issues/20), methodology v0.1, 2026-10-19. This is a decision method, not an automated recommender, a real system assessment or an approved architecture. Its example is entirely synthetic.

## Canonical inputs and question

The decision question is: **which feasible option meets a named user outcome and hard requirements under a defined workload, at defensible cost and change risk?** Inputs are the [requirements/workload profile](requirements-workload-profile.md), a [legacy modernization baseline](legacy-modernization-profile.md) when an existing system is involved, and the [pattern applicability and contraindication model](pattern-applicability-card.md). References must carry IDs, source/revision and current confidence. Unknown high-consequence inputs require a study or experiment, not a guessed value.

Each comparison MUST include **retaining or improving the current design** for a modernization problem. An existing modular system can be a viable option even when distributed alternatives exist. For greenfield design, include a comparable simple starting design. More complexity must be justified by a measurable benefit.

## Decision protocol

1. **Frame a testable outcome.** Name the affected journey, problem, scenario, SLO and correctness invariants with measurement windows, unit definitions and responsible decision authority. Separate mandatory constraints from preferences and unknowns.
2. **Generate alternatives.** Capture baseline/retain or tune, and at least one distinct solution. Pattern cards can nominate alternatives but cannot select for an unspecified workload.
3. **Apply hard gates first.** For each candidate, test compatibility, correctness, security/privacy, downtime and recoverability against actual evidence. Status is pass / fail / unknown. A **fail** disqualifies; an **unknown** suspends approval and creates a validation task. A weighted score can never override a hard failure.
4. **Compare only conditionally viable options.** Align scope, load, cost window, functional outcomes, operation, failure envelope and evidence age. Describe benefit, cost, incident modes, implementation/transition effort, irreversibility, and uncertainty. Use original plain-language reasoning before any optional numeric scores.
5. **Investigate decision-critical uncertainty.** Establish a falsifiable hypothesis for each disputed benefit, propose a controlled observation, thresholds agreed BEFORE the run, adversarial counterexample, repeated trials, and rollback/abort rule. A synthetic arithmetic example is not empirical proof.
6. **Decide explicitly.** Possible outcomes: accepted option with proven constraints; provisionally accepted pending gates; retain existing; defer; insufficient evidence. Only an authorized decision-maker can mark an ADR accepted; GitHub merge is not approval of a real system architecture.
7. **Keep a reversible record.** Write an ADR with alternatives rejected and their reasons, versioned evidence, positive/negative consequences, transition/rollout conditions and revisit triggers. Link the acceptance record and superseding ADR if later replaced.

## Hard-gate matrix, then discriminating evidence

| Gate | Baseline improvement | Candidate B | Candidate C |
|---|---|---|---|
| Business correctness and concurrency invariants | pass / fail / unknown, with evidence | same | same |
| Data/contract compatibility and mixed-version overlap | same | same | same |
| Residency, authorization and privacy | same | same | same |
| Maximum outage, RTO/RPO and forward recovery | same | same | same |
| Approved cost/team/operation ceiling when mandatory | same | same | same |

The word **unknown** is an executable result: record a test owner and material evidence request. Do not misclassify a missing SLO as a pass. If all options fail hard gates, revise constraints with appropriate authority or return no feasible option; do not secretly relax them.

## Optional scoring, uncertainty and sensitivity

A small weighted matrix can help *explain preferences* for options that passed hard gates. It does not quantify truth. For each quality attribute, record weight, relative direction, rationale and confidence. Normalize weight sum to 1. Use 0..5 scores only when readers understand they are **subjective estimates**, not measured fitness.

One fictional arithmetic comparison:

| Preference | Weight | A: retain/tune | B: split service |
|---|---:|---:|---:|
| Operational simplicity | 0.50 | 4 | 2 |
| Independent releases | 0.30 | 2 | 5 |
| Implementation effort | 0.20 | 5 | 2 |
| Weighted illustrative sum | 1.00 | 3.60 | 2.90 |

Under those *assumed* ratings, A leads; this **does not select an architecture**. A single uncertain assumption changes the outcome: if independent releases receive weight 0.60 and operations 0.20, with effort still 0.20, then A scores 0.20×4 + 0.60×2 + 0.20×5 = **3.00**, while B scores 0.20×2 + 0.60×5 + 0.20×2 = **3.80**. This rank reversal is a reason to discuss preferences and validate benefit, not to treat the largest calculated number as evidence.

When some attribute rating is unknown, show an interval or an explicit sensitivity challenge rather than a fabricated precise score. Keep mandatory invariants **outside** the weighted sum. A score sensitivity experiment must never mask a correctness violation.

## Provisional hypotheses and rejection gates

For each meaningful alternative, formulate: “Under workload and operating conditions X, adopting change Y is expected to improve measure Z relative to unchanged baseline A while preserving hard constraints C; experiment E will reject this claim if observation R occurs.” Predefine the measurement boundary, sample, time window, data/behavioral compatibility, p95/p99, admitted/successful/failed operations and actual operational effort. Include a dependency-loss or rollback case where relevant.

A viable decision can be **retain** because the baseline already meets required outcomes, **measure first** because a bottleneck is unlocated, or **stop** because a migration cannot meet compatibility constraints. Those are deliberate decision outputs, not failures of the workflow.

## ADR evidence and lifecycle contract

An ADR must have a stable identifier, title, author/decision owner, status (proposed, accepted, rejected, superseded), date, context, requirement/legacy IDs, hard gates, candidates and rejected options, measured versus hypothesized findings, consequences, decision/reversal, transition reference, validation obligations and review triggers. Update a decision by writing a superseding record rather than silently overwriting history. A “proposed” status is honest when the required approving owner is unavailable.

Original Mermaid decision gate:

~~~mermaid
flowchart TD
    Need["Defined outcome and scenario"] --> Options["Baseline plus genuine alternatives"]
    Options --> Gate{"All hard constraints evidenced?"}
    Gate -->|Fail| Reject["Exclude violating candidate"]
    Gate -->|Unknown| Measure["Insufficient evidence: precise research or experiment"]
    Gate -->|Pass| Compare["Same-boundary trade-offs and sensitivity"]
    Compare --> ADR["Proposed ADR and consequences"]
    ADR --> Approval{"Review owner approves with evidence?"}
    Approval -->|No| Measure
    Approval -->|Yes| Decision["Accepted decision with revisit triggers"]
~~~

Text alternative: define measurable outcomes, generate baseline and alternatives, reject hard failures and defer unknown hard constraints to research. Compare preferences only after the gates, record a proposed ADR and require explicit approval before acceptance.

## Source-to-claim ledger (inspected public scope, 2026-10-19)

| ID | Primary public source and section | Supported point; explicit exclusion |
|---|---|---|
| D01 | [arc42, Architecture Decisions, Section 9](https://docs.arc42.org/section-9/), *Content, Motivation, Form, Our proposal concerning decisions* | Document selection criteria, rationale, rejected alternatives and consequences; it does not dictate Tycho's weighting formula |
| D02 | [Architecture Decision Records, Nygard template](https://github.com/architecture-decision-record/architecture-decision-record/blob/main/locales/en-us/templates/decision-record-template-by-michael-nygard/index.md), *Title, Status, Context, Decision, Consequences* | Minimal recognized record fields and lifecycle; Tycho adds evidence and requirements traceability |
| D03 | [Tycho legacy profile](legacy-modernization-profile.md) and [Tycho pattern model](pattern-applicability-card.md), their respective decision/contraindication sections | Canonical original profile and applicability contracts; no production feasibility of any option established |

All calculations are original fictional scoring. There is no empirical comparison, no independently approved architectural decision and no formal machine-readable ADR schema in this issue; full decision graph/evaluation remains separate roadmap scope.

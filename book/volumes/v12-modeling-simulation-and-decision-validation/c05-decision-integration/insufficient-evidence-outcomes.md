---
metadata_version: 1
id: "tycho.page.ea9adae8cf8a3196a3515d383b075f53"
kind: "page"
parent_id: "tycho.chapter.2147ec1471d027ef256437a345f9c1e7"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c05-decision-integration/insufficient-evidence-outcomes.md"
title: "Insufficient-evidence outcomes"
topic_ids:
  - "decision-records"
  - "model-validation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When a verified, converged model still cannot support a recommendation."
route_hints:
  questions:
    - "When should a decision record return no recommendation?"
    - "What makes an insufficient-evidence outcome actionable?"
  prerequisites: []
  related_ids:
    - "tycho.page.3cfd08ee56330be9b7a2d37975c3fe26"
    - "tycho.page.ea00bb677b242deed4a1ff3fa91f948a"
    - "tycho.page.b0c704c825b2faf15a1d118dc9a6b1cc"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "insufficient evidence"
    - "no-go"
    - "unknowns"
    - "reversal"
evidence_scope:
  source_ids:
    - "src.sargent-vv"
    - "src.jcgm-100"
    - "src.nygard-adr"
  claim_ids: []
  status: "source-linked"
  notes: "Page-local source records and limits; not independent review."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "DeepSeek Harness authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Insufficient-evidence outcomes

**Question.** When should a decision record return no recommendation, and how is that
different from a failed model?

**Short answer.** A record returns insufficient evidence when the model is implemented but
the inputs, constraints or observations needed for a decision are missing or contradictory.
The model can be verified and the run converged; the decision still cannot be supported.

## Insufficient evidence is not a model failure

A model can be:

- verified: the engine preserves its invariants;
- converged: the sampling error is small;
- executable: the run replays;

and still fail to support a decision. The missing evidence is about the world, not the code.
Examples:

- the dual-write lag is assumed over a wide range and never measured;
- a hard constraint depends on a regulatory approval that has not been obtained;
- two stakeholders disagree about the objective, so no metric ranking is valid;
- a candidate's rollback has never been rehearsed;
- the observed divergence exceeds the business threshold in every scenario.

A decision record that forces a recommendation in these conditions hides the missing
evidence. The correct outcome is insufficient evidence plus a list of what would change it.

## The modernization example

The staged modernization run reports:

- success rate 1.0 (the model serves the offered traffic);
- maximum divergence 8,925.5 records (95% CI 5,561.6-12,289.3);
- rollback completed 0.1 (it finishes within the 2,400-second horizon in only 10% of replications);
- rollback seconds censored at the horizon, 2,400.

The no-cutover baseline reports zero divergence and no rollback requirement. The staged
candidate looks better only if the divergence is ignored. But the dual-write lag and
reconciliation capacity are assumed over wide ranges and are negatively correlated. The
model cannot tell whether a real migration would diverge by ten records or ten thousand.

The decision record returns insufficient evidence, recommendation none. It lists the
measurements that would change the outcome: measured dual-write lag, measured reconciliation
capacity, a rehearsed rollback and a measured divergence below the threshold.

## A checklist for insufficient evidence

Return insufficient evidence when any of the following holds:

- a hard input is assumed and its range spans the decision boundary;
- a hard constraint cannot be evaluated by the model;
- the confidence interval includes both a pass and a fail on a decision-relevant metric;
- two candidates are indistinguishable on the declared metrics;
- the model's validity limits exclude the operating condition under test;
- the rollback or recovery path has not been exercised;
- the objective or metric ranking is contested.

Return a conditional decision when the missing evidence is explicitly non-quantitative and
the decision record can state the condition. The checkout record does this for operability:
it recommends B under the quantitative constraints and marks C3 unverified.

## What would change the outcome

A useful insufficient-evidence record is actionable. It names:

- the measurement;
- the range that would support or reject the decision;
- the owner of the measurement;
- the consequence of staying in the current state;
- the next review trigger.

For the modernization record, the trigger is a measured lag and capacity plus a rehearsed
rollback. For the checkout record, the trigger is a measured arrival rate, service time or
retry rate outside the declared range.

## Failure modes

- **Forced recommendation.** An analyst picks the least-bad candidate to avoid an
  incomplete-looking record.
- **Score to the rescue.** A weighted score converts a hard constraint failure into a small
  penalty.
- **Unknown as zero.** A missing input is set to zero and the model reports a precise but
  meaningless result.
- **Sensitivity as evidence.** A sensitivity ranking is used to fill a missing measurement.
- **Perpetual insufficient evidence.** The record never names the measurement or the trigger,
  so it cannot be resolved.

## Evidence ledger

- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports the distinction between model validity and data validity.
  It does not resolve the missing measurement.
- JCGM 100:2008 (source src.jcgm-100; see the reading ledger)
  supports reporting a value with its uncertainty and coverage.
  It does not create a measurement where none exists.
- [Nygard, Documenting Architecture
  Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
  supports recording status and consequences.
  It does not require a recommendation.

## Navigation

- Parent: [V12/C05 - Decision integration](../README.md)
- Previous: [Comparative decision worked example](comparative-decision-worked-example.md)
- Next: [V12/C06 - Migration simulation](../c06-migration-simulation/README.md)
- Modernization decision: edition/v12/decisions/modernization-cutover.json

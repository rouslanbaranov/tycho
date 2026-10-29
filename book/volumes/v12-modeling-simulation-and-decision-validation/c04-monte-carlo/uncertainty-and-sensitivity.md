---
metadata_version: 1
id: "tycho.page.7a8c030b04dc4f4809d4943e9be47ede"
kind: "page"
parent_id: "tycho.chapter.9548ac72fafbee8773ad7309a51d512b"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c04-monte-carlo/uncertainty-and-sensitivity.md"
title: "Uncertainty and sensitivity"
topic_ids:
  - "monte-carlo"
  - "uncertainty"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Input uncertainty, correlation and a bounded first-order/total-order sensitivity screen."
route_hints:
  questions:
    - "How is input uncertainty propagated?"
    - "Which inputs change the output variance?"
  prerequisites: []
  related_ids:
    - "tycho.page.0fff38d91e019ef6d81869c4b462c5fb"
    - "tycho.page.4e13fd6ac1103a15c800e939b13bd2f9"
    - "tycho.page.3cfd08ee56330be9b7a2d37975c3fe26"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "Monte Carlo"
    - "uncertainty"
    - "sensitivity"
    - "Sobol"
    - "correlation"
evidence_scope:
  source_ids:
    - "src.owen-monte-carlo"
    - "src.jcgm-100"
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

# Uncertainty and sensitivity

**Question.** Which inputs are uncertain, how should their uncertainty be propagated, and
which inputs actually change the decision?

**Short answer.** Declare a distribution or a range for each uncertain input, sample it with
a recorded seed, run the model across the sample, and report the output distribution with
its error. Then estimate a sensitivity index that separates a main effect from an
interaction. An assumed distribution is not a measurement, and a sensitivity ranking is not
a causal claim.

## Two kinds of uncertainty

V12 distinguishes:

- **input uncertainty:** the arrival rate, service time, timeout, dual-write lag or another
  parameter is not known exactly;
- **sampling error:** even with fixed inputs, a finite number of replications gives an
  estimate with error.

Replications address sampling error. Parameter draws address input uncertainty. Increasing
replications does not reduce input uncertainty. Increasing the number of input draws does not
remove sampling error.

## The Monte Carlo procedure

1. State the model and the output metric.
2. Declare a distribution or range for each uncertain input, with its evidence status.
3. Declare correlations between inputs, or state that they are independent.
4. Generate a sample matrix with a recorded seed.
5. Run the model for each row and each replication.
6. Report the output mean, standard error and confidence interval.
7. Decompose the output variance into main and interaction terms.
8. Record the assumptions, the sample size and the limits.

The V12 engine implements steps 4-7. The scenario contract records steps 1-3; the run record
records steps 4-8.

## Correlated inputs

Independent draws are a modelling assumption, not a neutral default. In the modernization
scenario, a longer dual-write lag plausibly coincides with a lower reconciliation capacity:
the same operational pressure produces both. V12 declares a negative correlation of -0.4
between those inputs and labels the uncertainty method as a Gaussian copula.

The engine's sampling applies the declared correlation to the input draws. It does not infer
a correlation from data. A model that ignores a known correlation produces an output
distribution that is too narrow and a decision that looks more certain than it is.

## First-order and total-order sensitivity

For an output Y with variance V, the first-order Sobol' index for input i is the share of V
explained by input i alone. The total-order index includes every interaction that involves
input i. A first-order index near zero does not mean the input is irrelevant; it may act
only through an interaction.

Owen's appendix describes the ANOVA decomposition and the Sobol' indices. The pick-freeze
estimator uses paired model evaluations: one matrix with the input of interest fixed and one
with it varied. The estimator is unbiased only under its assumptions and is noisy at small
sample sizes.

## The V12 screen

A full pick-freeze analysis is expensive for a discrete-event model. V12 uses a quadratic
response-surface screen:

1. Draw 48 input rows from the declared distributions.
2. Run the model for each row.
3. Fit a quadratic surface in standardized input coordinates.
4. Decompose the fitted variance into main effects and the interaction term.
5. Report the first-order and total-order shares.

The screen is an approximation. It assumes that a quadratic surface is adequate over the
sampled range and that the input standardization is meaningful. It also requires independent
inputs: the sensitivity scenario declares no correlation, and the engine rejects a correlated
screen. Correlated inputs are propagated by the separate Monte Carlo run, not by this
independent-input variance decomposition. The screen is not a full Sobol' analysis.

For the candidate B sensitivity run, the fitted screen reports:

- arrival rate: first-order 0.361, total-order 0.464;
- service mean: first-order 0.536, total-order 0.639.

The service mean has the larger main effect in this sampled range. The arrival rate has a
substantial interaction share. The two first-order indices sum to 0.897, leaving about 0.103
for interaction and unexplained variation. The screen does not prove that service time is
more important in production; it says that, under the declared distributions and the
quadratic approximation, it explains more of the fitted variance.

## A separate insufficient-sample case

The sensitivity scenario itself is converged at a 0.00016 relative error, but it is still a
screening approximation. A separate two-replication convergence-stress run has a relative
error of 0.032, above the 0.02 threshold, and is marked insufficient-sample. Its wide input
draws and small replication budget show the failure mode without pretending that the
sensitivity screen is precise.

This is deliberate. A ranking from an unstable sample can reverse; the stress run records
the instability instead of hiding it.

## Failure modes

- **Assumed as measured.** A uniform range is treated as if it came from a measured
  distribution.
- **Independent by default.** Correlated inputs are sampled independently, narrowing the
  output distribution.
- **Sensitivity without error.** Indices are reported without the sample size or a
  convergence check.
- **Quadratic overreach.** The response surface is extrapolated beyond the sampled range.
- **Bounded-output distortion.** Success rate near 1.0 has little variance, so a variance
  decomposition can look unstable even when the underlying effect is real.

## Evidence ledger

- [Owen, Monte Carlo chapters 1-2 and appendix A](https://artowen.su.domains/mc/)
  supports sampling error, confidence intervals, failure modes and Sobol' indices.
  It does not validate the V12 screen or its distributions.
- JCGM 100:2008 (source src.jcgm-100; see the reading ledger)
  supports measurement uncertainty and coverage vocabulary.
  It does not establish a V12 uncertainty budget.

## Navigation

- Parent: [V12/C04 - Monte Carlo](../README.md)
- Next: [Convergence and error](convergence-and-error.md)
- Sensitivity run: edition/v12/runs/checkout-sensitivity.json

---
metadata_version: 1
id: "tycho.page.0fff38d91e019ef6d81869c4b462c5fb"
kind: "page"
parent_id: "tycho.chapter.9548ac72fafbee8773ad7309a51d512b"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c04-monte-carlo/convergence-and-error.md"
title: "Convergence and error"
topic_ids:
  - "monte-carlo"
  - "uncertainty"
perspectives:
  - "evaluation"
  - "architecture"
summary: "Standard error, confidence intervals, relative error and the limits of convergence."
route_hints:
  questions:
    - "When is a Monte Carlo result stable enough to use?"
    - "What does a confidence interval cover?"
  prerequisites: []
  related_ids:
    - "tycho.page.7a8c030b04dc4f4809d4943e9be47ede"
    - "tycho.page.4e13fd6ac1103a15c800e939b13bd2f9"
    - "tycho.page.6fd0d561e3e2900dc8b59a3011071cd2"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "standard error"
    - "confidence interval"
    - "convergence"
    - "batch means"
evidence_scope:
  source_ids:
    - "src.owen-monte-carlo"
    - "src.little-law"
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

# Convergence and error

**Question.** When is a Monte Carlo result stable enough to use, and what does a confidence
interval actually cover?

**Short answer.** A result is stable when its estimated standard error is small relative to
the decision-relevant effect and the sampling assumptions hold. V12 reports the standard
error, a 95% confidence interval and a relative-error threshold. It marks the run
insufficient-sample when the threshold is not met.

## Standard error

For n independent replications with sample standard deviation s, the standard error of the
mean is:

    se = s / sqrt(n)

A 95% confidence interval under a normal approximation is:

    mean +/- 1.96 * se

The interval is narrower when n is larger or the output is less variable. It does not become
more valid if the replications are correlated or the output distribution is heavy-tailed.

V12 uses the normal approximation across replications. For 30 replications the approximation
is reasonable for a bounded metric such as success rate. For a heavy-tailed latency, it can
understate the tail uncertainty. The decision record records that limit.

## Relative error

V12's convergence rule compares the standard error with the absolute value of the metric:

    relative error = se / |mean|

The threshold is 0.02. A run is converged when the relative error is at most 0.02 and
insufficient-sample otherwise.

For candidate A, the success rate is 0.9218 with a standard error of about 0.00038, giving a
relative error of 0.00041. For candidate B, the relative error is 0.00003. The sensitivity
run is converged at 0.00016. The separate two-replication convergence-stress run has a
success rate of 0.909 and a relative error of 0.032, so it is marked insufficient-sample.
The first three are converged; the stress run is not.

A relative-error threshold is a decision aid, not a universal rule. A metric near zero can
have a small absolute error and a large relative error. A metric with a wide business
tolerance can accept a larger relative error.

## Coverage and its assumptions

A 95% confidence interval covers the true mean in repeated sampling about 95% of the time
under the model's assumptions. It does not cover the true production value if the model is
biased or the inputs are mis-specified. It does not cover a single future request.

Owen's chapters describe when simple Monte Carlo fails: heavy tails, dependent samples,
misspecified distributions and rare events. A bounded success rate avoids some of those
problems but introduces a ceiling effect: when success is near 1.0, the variance is small and
the interval is narrow, but the metric cannot reveal failures that the model does not
represent.

## Batch means and dependence

Replications are independent by construction in V12: each replication uses its own seed.
Within a replication, events are dependent by design. If a metric were computed from a
single long run, batch means would be needed to estimate its standard error.

Kim and Whitt recommend batch means for simulation output analysis and discuss edge effects
in finite-window Little's law measurements. V12 uses independent replications for its
confidence intervals, so batch means are not applied. The run's limitations say so. A future
model with one long run would need a different error method.

## What convergence does not mean

Convergence does not mean:

- the model is valid;
- the inputs are measured;
- the decision is correct;
- the confidence interval contains the production value;
- more replications will fix a biased model.

It means the sampling error of the reported metric is small under the declared model. That is
a narrow but useful statement.

## A stopping rule

A practical stopping rule is:

1. Run a pilot with at least 10 replications.
2. Estimate the standard error of the primary metric.
3. Compute the required n for the target relative error.
4. Run to that n or to a declared budget, whichever is smaller.
5. Record the achieved error and whether the target was met.

V12 does not adapt n during a run. The scenario declares the replication count, and the run
reports the achieved error. This keeps the result reproducible; an adaptive stopping rule
would need its own seeded decision log.

## Failure modes

- **Peeking.** The analyst stops when the interval looks favorable, which invalidates the
  nominal coverage.
- **Correlated replications.** A shared random stream makes the standard error too small.
- **Heavy-tail denial.** A latency tail is summarized by a mean and a normal interval.
- **Threshold shopping.** The relative-error threshold is changed after seeing the result.
- **Convergence without calibration.** A stable estimate of a biased model is still biased.

## Evidence ledger

- [Owen, Monte Carlo chapters 1-2](https://artowen.su.domains/mc/)
  supports standard error, confidence intervals, failure modes and concentration bounds.
  It does not establish a V12 coverage guarantee.
- Kim and Whitt (source src.little-law; see the reading ledger) supports batch means and
  finite-window measurement caveats.
  It does not validate the V12 replication scheme.

## Navigation

- Parent: [V12/C04 - Monte Carlo](../README.md)
- Previous: [Uncertainty and sensitivity](uncertainty-and-sensitivity.md)
- Next: [Monte Carlo reference cases](monte-carlo-reference-cases.md)

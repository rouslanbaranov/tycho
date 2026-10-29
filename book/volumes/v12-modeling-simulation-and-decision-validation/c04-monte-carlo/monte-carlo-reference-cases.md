---
metadata_version: 1
id: "tycho.page.4e13fd6ac1103a15c800e939b13bd2f9"
kind: "page"
parent_id: "tycho.chapter.9548ac72fafbee8773ad7309a51d512b"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c04-monte-carlo/monte-carlo-reference-cases.md"
title: "Monte Carlo reference cases"
topic_ids:
  - "monte-carlo"
  - "model-validation"
perspectives:
  - "evaluation"
  - "implementation"
summary: "Small known-answer and invariant checks that catch broken samplers and false convergence."
route_hints:
  questions:
    - "Which reference cases can catch a broken estimator?"
    - "What do the current cases not prove?"
  prerequisites: []
  related_ids:
    - "tycho.page.0fff38d91e019ef6d81869c4b462c5fb"
    - "tycho.page.621e495fcadc4849d2f21d55be4c52e4"
    - "tycho.page.6fd0d561e3e2900dc8b59a3011071cd2"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "reference case"
    - "conservation"
    - "replay"
    - "boundary"
evidence_scope:
  source_ids:
    - "src.owen-monte-carlo"
    - "src.sargent-vv"
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

# Monte Carlo reference cases

**Question.** Which small cases with known answers can catch a broken sampler, a wrong
estimator or a false convergence claim?

**Short answer.** A reference case should have an analytic answer, a clear tolerance and a
failure mode that the test can detect. V12 uses conservation, boundary cases, deterministic
replay and a sensitivity-screen sanity check. It does not claim that these cases validate a
real model.

## Why reference cases matter

A Monte Carlo implementation can look plausible while being wrong in several ways:

- the sampler uses a biased distribution;
- the standard error is computed from the wrong denominator;
- the confidence interval uses the wrong quantile;
- the sensitivity estimator confuses main and interaction effects;
- the seed is ignored and the "independent" replications are identical.

A reference case with a known answer catches some of these. It does not catch a model that is
implemented correctly but mis-specified for the decision.

## Case 1: conservation

The stock-flow model must preserve:

    offered = completed + rejected + backlog

The test runs a below-capacity case, a saturation case and a zero-arrival case. It checks
the identity at every step and refuses a negative backlog. A broken service calculation
usually shows up as a conservation gap or a negative stock.

The observed results are in the order-intake baseline and saturation runs. The baseline has
zero rejection and zero backlog; the saturation case has 0.2 rejection, a 77.6-request
backlog and a 24-request-per-second throughput.

## Case 2: deterministic replay

The discrete-event model must produce the same result hash for the same model, scenario and
seed. The test runs the same scenario twice and compares the hash. A broken event order, a
wall-clock dependency or a hidden module cache fails the test.

Replay is also a command: it checks the stored model and scenario hashes, reruns the
scenario and compares the result hash. A formatting-only change to the run record does not
change the hash because the hash covers the substantive fields.

## Case 3: boundary cases

The engine tests:

- zero arrivals: no requests, no completions;
- zero servers: no service, explicit rejection or backlog;
- zero queue capacity: a request that cannot start immediately is rejected;
- zero timeout: not allowed by the schema; the minimum is positive;
- maximum attempts one: no retry;
- full bulkhead: explicit rejection.

A boundary case is valuable because many models are only tested in the comfortable middle.
The V12 tests assert the boundary outcome, not just that the run finishes.

## Case 4: sensitivity sanity

A sensitivity screen should satisfy two sanity conditions:

- each first-order index is between 0 and 1;
- each total-order index is at least the corresponding first-order index.

The V12 screen enforces the second condition by construction: the total-order share includes
the fitted interaction variance. A screen that reports a total index below a first-order
index is rejected as incoherent.

The candidate B screen reports arrival 0.345/0.522 and service 0.478/0.655. Both pairs satisfy
the condition. The screen's 48-row sample is small; the indices are a screen, not a
precision estimate.

## Case 5: known-answer checks not yet implemented

A stronger reference suite would include:

- estimating pi from uniform samples with a known standard error;
- estimating the mean of an exponential distribution with a known variance;
- comparing an M/M/1 queue's mean wait with the analytic formula for a stable system;
- checking empirical coverage of a confidence interval over many synthetic samples.

V12 does not claim these checks. They are recorded as future verification work, not as
completed evidence. The current reference cases exercise the implemented accounting, event
order and sensitivity sanity, not the statistical calibration of the sampler.

## A reference-case record

Each verification case in the model contract has:

- an identifier;
- a description;
- the expected result;
- the observed result;
- a pass, fail or not-run status;
- the test path.

A case without a test path is not a verification case. A case marked pass without an observed
result is a claim, not evidence.

## Failure modes

- **Testing the happy path only.** A model passes one steady-state run and fails at zero
  arrivals or full capacity.
- **Asserting no exception.** The test checks that the function returns, not that the result
  is correct.
- **Reference to a moving target.** The expected value is copied from the current output, so
  the test can never fail.
- **Coverage without power.** A confidence-interval check uses too few samples to detect a
  real coverage error.

## Evidence ledger

- [Owen, Monte Carlo chapters 1-2](https://artowen.su.domains/mc/)
  supports error estimation and failure-mode reasoning.
  It does not establish that the V12 reference cases are sufficient.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports degenerate tests, extreme-condition tests and traces.
  It does not validate the V12 test suite.

## Navigation

- Parent: [V12/C04 - Monte Carlo](../README.md)
- Previous: [Convergence and error](convergence-and-error.md)
- Next: [V12/C05 - Decision integration](../c05-decision-integration/README.md)

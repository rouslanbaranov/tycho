---
metadata_version: 1
id: "tycho.chapter.9548ac72fafbee8773ad7309a51d512b"
kind: "chapter"
parent_id: "tycho.volume.fd0c1a798f9968eed4a679b048deea14"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c04-monte-carlo/README.md"
title: "V12/C04 - Monte Carlo uncertainty and sensitivity"
topic_ids:
  - "simulation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How should sampling error, convergence and sensitivity be reported?"
route_hints:
  questions:
    - "How should sampling error, convergence and sensitivity be reported?"
  prerequisites: []
  related_ids:
    - "tycho.page.7a8c030b04dc4f4809d4943e9be47ede"
    - "tycho.page.0fff38d91e019ef6d81869c4b462c5fb"
    - "tycho.page.4e13fd6ac1103a15c800e939b13bd2f9"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "simulation"
    - "architecture decision"
    - "model evidence"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Chapter landing; page-local sources carry the evidence."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "DeepSeek Harness authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: null
content_verified_at: null
---

# V12/C04 - Monte Carlo uncertainty and sensitivity

**Status:** self-checked chapter landing, 2026-10-29. The sensitivity screen is a bounded
approximation; the page states its limits.

## Purpose and mission

A single simulation run with one set of assumed inputs hides uncertainty. This chapter
separates input uncertainty from sampling error, defines convergence criteria and reports
which inputs matter through a sensitivity screen.

The chapter answers how sampling error, convergence and sensitivity should be reported. It
does not claim that an assumed distribution is a measured distribution.

## Pages and reasoning route

- [Uncertainty and sensitivity](uncertainty-and-sensitivity.md): distributions,
  correlation, first-order and total-order sensitivity.
- [Convergence and error](convergence-and-error.md): standard error, confidence intervals,
  relative error and when Monte Carlo fails.
- [Monte Carlo reference cases](monte-carlo-reference-cases.md): analytic checks, coverage
  and the limits of a reference case.

Read the uncertainty page before interpreting a confidence interval. Read the convergence
page before saying a result is stable. Read the reference cases before trusting a new
estimator.

## Diagram

~~~mermaid
flowchart LR
    I["Input distributions"] --> S["Sample matrix"]
    S --> R["Seeded replications"]
    R --> M["Metric distribution"]
    M --> C["Convergence and CI"]
    M --> V["Variance decomposition"]
    V --> P["Sensitivity ranking"]
~~~

Text alternative: input distributions generate a sample matrix. Seeded replications produce
a metric distribution, which feeds convergence diagnostics and a variance decomposition.
The decomposition produces a bounded sensitivity ranking.

## Boundaries and evidence

Owen's Monte Carlo chapters support sampling error, confidence intervals, failure modes and
Sobol' indices. JCGM 100 supports the measurement-uncertainty vocabulary. The V12 screen uses
a quadratic response-surface decomposition rather than a full pick-freeze Sobol analysis;
the page says so and reports first-order and total-order indices only as a screening result.

The chapter does not cover variance reduction, Markov-chain Monte Carlo, quasi-Monte Carlo or
a full metrological uncertainty budget.

## Navigation and prerequisites

- Previous: [V12/C03 - Deterministic and DES](../c03-deterministic-and-des/README.md)
- Next: [V12/C05 - Decision integration](../c05-decision-integration/README.md)
- Sensitivity run:
  [checkout-sensitivity.json](../../../../edition/v12/runs/checkout-sensitivity.json)

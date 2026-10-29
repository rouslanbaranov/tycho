---
metadata_version: 1
id: "tycho.page.3cfd08ee56330be9b7a2d37975c3fe26"
kind: "page"
parent_id: "tycho.chapter.2147ec1471d027ef256437a345f9c1e7"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c05-decision-integration/comparative-decision-worked-example.md"
title: "Comparative decision worked example"
topic_ids:
  - "decision-records"
  - "monte-carlo"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A/B/C comparison under one workload, hard constraints and a conditional recommendation."
route_hints:
  questions:
    - "How does the A/B/C comparison reach a recommendation?"
    - "Which measurement would reverse it?"
  prerequisites: []
  related_ids:
    - "tycho.page.b8e3757528ca1f60a472a6fd9deb7489"
    - "tycho.page.ea9adae8cf8a3196a3515d383b075f53"
    - "tycho.page.c264e48a38af3148eff0c87a3b98a8dd"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "A/B/C"
    - "comparison"
    - "constraints"
    - "recommendation"
    - "reversal"
evidence_scope:
  source_ids:
    - "src.simpy"
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

# Comparative decision worked example

**Question.** How does the V12 checkout comparison move from three runs to a conditional
recommendation?

**Short answer.** The comparison fixes the workload, seed scheme and metrics, eliminates a
candidate that violates hard constraints, compares the survivors on business-comparable
metrics, and records the non-quantitative constraint that the model cannot test.

## The experiment

Three candidates receive the same Poisson workload at 20 requests per second for 1,800
seconds after a 300-second warmup. Each uses 30 replications with the seed base 20261029. The
metrics are success rate, p95 latency, throughput, cost per 1000 successful requests,
rejection rate and retry amplification.

The candidates differ in capacity, deadline, queue, retry and unit cost:

- A: 12 servers, 0.5-second mean service, 50-request queue, 1-second timeout, one attempt,
  60-request bulkhead, cost 10.0;
- B: 12 servers, 0.5-second mean service, 200-request queue, 2-second timeout, three attempts,
  exponential backoff with full jitter, 240-request bulkhead, cost 8.0;
- C: 18 servers, 0.75-second mean service, 120-request queue, 1.5-second timeout, two
  attempts, linear backoff, 160-request bulkhead, cost 14.0.

## The results

- A: success 0.9218 (95% CI 0.9211-0.9226), p95 0.870 s, cost 1.81, timeout 0.0778.
- B: success 0.9996 (95% CI 0.9995-0.9997), p95 1.206 s, cost 1.34, timeout 0.0041.
- C: success 0.9679 (95% CI 0.9595-0.9764), p95 1.769 s, cost 3.63, timeout 0.111.

All three runs are converged by the 0.02 relative-error rule. The confidence intervals are
narrow because the workload is synthetic and the replications are independent. Narrow
intervals do not make the inputs measured.

## Applying the constraints

The decision record declares:

- C1: every offered request is accounted for (hard);
- C2: no silent drop (hard);
- C3: operable by the existing team (non-quantitative);
- C4: cost per 1000 successes at most 3.0 (hard);
- C5: p95 latency at most 1.5 seconds (hard).

C1 and C2 hold for all three runs: the model reports a conservation flag and the engine
aborts on a failure. C4 eliminates C: 3.63 is above 3.0. C5 also eliminates C: 1.769 is
above 1.5. A and B pass both constraints.

B and A both pass. B has higher success (0.9996 versus 0.9218) and lower cost (1.34 versus
1.81). A has lower p95 latency (0.870 versus 1.206). The record recommends B because the
declared decision prioritizes successful completions and cost per success over the latency
difference inside the 1.5-second ceiling. That prioritization is a decision, not a fact
produced by the simulation.

C3 is not tested. The record says the operability constraint remains unverified and requires
an operational review. The recommendation is therefore conditional.

## Sensitivity and uncertainty

The candidate B sensitivity screen reports arrival rate first-order 0.361 and total-order
0.464, service mean first-order 0.536 and total-order 0.639. The screen is a quadratic
approximation over 48 rows. It says service time explains more of the fitted variance in the
sampled range. It does not prove that service time is the dominant production factor.

The sensitivity scenario is converged at a 0.00016 relative error. A separate two-replication
convergence-stress run is insufficient-sample at 0.032. The decision record does not use the
sensitivity ranking to support a production claim; it uses it to identify what to measure
first.

## What would reverse the recommendation

- A measured arrival rate above 22 requests per second or a mean service time above 0.65
  seconds changes the utilization boundary.
- A measured p95 service time whose tail pushes B above 1.5 seconds.
- A cost weight under which B no longer beats A per successful request.
- A failure of the operability review.
- A measured retry rate materially above the modeled 1.003.

The record also says what would not reverse it: a narrower confidence interval on the
synthetic workload. More replications would make the synthetic estimate more precise, not
more representative.

## A decision tree

~~~mermaid
flowchart TD
    S["Same workload and seeds"] --> H{"Hard constraints pass?"}
    H -- "No" --> E["Eliminate candidate"]
    H -- "Yes" --> C["Compare success and cost"]
    C --> N{"Non-quantitative constraint?"}
    N -- "Unverified" --> Q["Conditional recommendation"]
    N -- "Verified" --> R["Recommendation with limits"]
    Q --> T["Reversal triggers"]
    R --> T
~~~

Text alternative: candidates that fail a hard constraint are eliminated. Survivors are compared
on success and cost. An unverified non-quantitative constraint keeps the recommendation
conditional. Reversal triggers are recorded either way.

## Evidence ledger

- [SimPy 4.1 documentation](https://simpy.readthedocs.io/en/latest/)
  supports the queue and timeout semantics.
  It does not establish the candidate metrics.
- [Owen, Monte Carlo chapters](https://artowen.su.domains/mc/)
  supports sampling error and sensitivity vocabulary.
  It does not validate the sensitivity screen.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports the separation of model verification and operational validity.
  It does not validate the decision.

## Navigation

- Parent: [V12/C05 - Decision integration](../README.md)
- Previous: [Decision records and pattern links](decision-records-and-pattern-links.md)
- Next: [Insufficient-evidence outcomes](insufficient-evidence-outcomes.md)
- Decision record: edition/v12/decisions/checkout-candidate.json

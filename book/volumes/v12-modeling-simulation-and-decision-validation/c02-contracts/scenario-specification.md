---
metadata_version: 1
id: "tycho.page.dedc5f2d31912a9ba5f562a86009fda0"
kind: "page"
parent_id: "tycho.chapter.3a47e8385cccb8a2ce764bfa765cc740"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c02-contracts/scenario-specification.md"
title: "Scenario specification contract"
topic_ids:
  - "simulation"
  - "experiment-design"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A versioned contract for workload, configuration, uncertainty, seeds and metrics."
route_hints:
  questions:
    - "Which fields make a scenario reproducible?"
    - "What must remain identical across candidates?"
  prerequisites: []
  related_ids:
    - "tycho.page.d8d9d15b402d8f65928ca0e3f3e5b939"
    - "tycho.page.201248045fa3cd67e617ce04a1c56feb"
    - "tycho.page.3cfd08ee56330be9b7a2d37975c3fe26"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "scenario"
    - "workload"
    - "seeds"
    - "metrics"
    - "uncertainty"
evidence_scope:
  source_ids:
    - "src.simpy"
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

# Scenario specification contract

**Question.** Which fields make a scenario reproducible and comparable across candidates?

**Short answer.** A V12 scenario fixes the model identifier, workload, candidate
configuration, uncertainty inputs, replication count, seed scheme, metrics and constraints.
For a candidate comparison, the workload, duration, warmup, metric definitions and seed
scheme are identical. Only the candidate configuration changes.

## The identical-workload rule

A comparison is not a comparison if each candidate receives a different arrival pattern,
duration or warmup. The V12 A/B/C scenarios share:

- a 1,800-second horizon and a 300-second warmup;
- a Poisson arrival process at 20 requests per second;
- the same metric identifiers and units;
- the same seed base and the same seed = base + replication scheme;
- the same hard constraints.

The candidate configuration differs: server count, service-time distribution, queue
capacity, timeout, retry budget, bulkhead and unit cost. That is the intended experimental
variable.

If a candidate needs a different workload to look good, the comparison is invalid. The
correct response is to record the workload as part of the candidate and compare under a
declared workload family, not to silently change the arrivals.

## Required structure

A scenario contract contains:

- id, version, title, model_id and purpose;
- workload: duration, warmup, time unit and arrival process;
- configuration: servers, service time, queue capacity, timeout, attempts, backoff,
  bulkhead and cost;
- uncertainty: parameter draws and correlations;
- replications and seed;
- metrics: identifier, unit, direction and business-comparable flag;
- constraints: hard, soft and non-quantitative;
- evidence_status and validity_limits.

The schema requires every field. A scenario with no constraints is still a scenario, but it
cannot support a decision record that claims to respect hard constraints.

## Seeds and replications

A seed is not a random number chosen to make a result look stable. It is part of the input
contract. V12 uses a base seed and a deterministic per-replication seed. The run record
stores the base seed and replication count, and the result hash covers the metrics.

Replications estimate sampling error. A larger number reduces the standard error but does not
remove input uncertainty. If the input distribution is assumed, more replications make the
assumption more precise, not more true.

## Example: candidate B

Candidate B declares 12 servers, a lognormal service time with mean 0.5 seconds and
coefficient of variation 0.6, a 200-request queue, a 2-second timeout, three attempts,
exponential backoff with base 0.2 seconds and full jitter, a 240-request bulkhead and a
relative cost of 8.0 per server-hour. It uses 30 replications and the shared seed base.

The same file also declares the metrics: success rate, p95 latency, throughput, cost per
1000 successes, rejection rate and retry amplification. The decision record uses a subset of
those metrics; the run record stores all of them.

## Business-comparable metrics

A metric is business-comparable when two candidates can be compared without hidden
normalization. Success rate and cost per 1000 successful requests are comparable. Average
CPU utilization is not comparable across candidates with different server counts unless the
cost and work units are also stated.

The scenario contract marks every metric with a direction and a unit. A decision record that
uses a metric not declared in the scenario is a validation failure.

## Failure modes

- **Workload drift.** A candidate gets a shorter warmup or a lower arrival rate. The
  comparison is invalid.
- **Seed reuse across candidates.** Sharing the same random stream can create common random
  numbers, which is sometimes desirable, but it must be a declared choice. V12 uses the same
  seed scheme for all candidates; the engine samples independently per replication.
- **Ignored correlation.** Two inputs are drawn independently even though they move together.
  The resulting uncertainty is too narrow.
- **Metric substitution.** A decision uses p99 latency while the scenario declares p95. The
  validator rejects the mismatch.
- **Constraint laundering.** A hard cost ceiling becomes a soft preference after a candidate
  fails it. The decision record must show the constraint and the failure.

## Evidence ledger

- [SimPy 4.1 documentation](https://simpy.readthedocs.io/en/latest/)
  supports event, resource and timeout semantics used by the scenario configuration.
  It does not establish the synthetic parameter values.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports the requirement to state data and operational validity.
  It does not validate the workload.

## Navigation

- Parent: [V12/C02 - Contracts](../README.md)
- Previous: [Model specification contract](model-specification.md)
- Next: [Run and result provenance contract](run-and-result-provenance.md)
- Schema:
  schemas/v12/scenario-specification.v1.schema.json

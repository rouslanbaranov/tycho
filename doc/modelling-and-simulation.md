# Modelling and simulation

V12 is Tycho's isolated modelling volume. It adds executable, deterministic
models and decision records without rewriting the existing book. The volume is
deliberately small: three models, ten scenarios, ten seeded runs and two decision
records.

The canonical artifacts live under [`edition/v12/`](../edition/v12/).
The reader-facing pages are the [V12 volume][v12-reader].

## What V12 is for

V12 demonstrates a discipline for decision modelling:

- declare a model and its assumptions;
- declare a scenario, workload and seeded inputs;
- run replications and report uncertainty;
- record invariants and convergence;
- compare candidates under declared constraints;
- return `decision-supported` or `insufficient-evidence`;
- preserve provenance and result hashes.

It is not a production digital twin and its numbers are not measurements of any
real system.

## Artifact inventory

| Artifact | Count |
|---|---:|
| Reader-facing V12 pages | 31 |
| V12 chapters | 7 |
| Models | 3 |
| Scenarios | 10 |
| Seeded runs | 10 |
| Decision records | 2 |
| V12 engine tests | 21 |

## Models

| Model | ID | What it represents |
|---|---|---|
| Checkout DES | `tycho.model.checkout-des` | Discrete-event queue with deadlines and retries |
| Order intake | `tycho.model.order-intake` | Stock-and-flow backlog with arrivals and capacity |
| Modernization path | `tycho.model.modernization-path` | Legacy/coexistence shift and rollback |

All models are uncalibrated. Their parameters are declared synthetic assumptions.

## Scenarios

The ten scenarios cover:

- three checkout candidates (synchronous, bounded queue, partitioned);
- convergence stress and overload boundaries;
- a sensitivity screen;
- modernization with no cutover and staged cutover;
- order-intake baseline and saturation.

Scenarios are versioned JSON files. They declare arrivals, service behavior,
deadlines, retries, costs and the seed scheme. A scenario is not a measurement.

## Runs and provenance

Each run records:

- model and scenario IDs;
- engine name and version;
- Python and platform;
- model, scenario and input SHA-256;
- engine SHA-256;
- seed base and replication count;
- convergence result;
- invariants;
- uncertainty method;
- result SHA-256;
- explicit limitations.

The checkout model uses 30 replications with seed base `20261029`. Its
convergence check uses relative error on success rate with a 0.02 threshold.

The run record is deterministic: replaying the same model, scenario and engine
must reproduce the same result hash. The V12 tests exercise that property.

## Metrics

The metrics are conditional on the declared model and scenario. They include:

| Metric | Unit | Direction |
|---|---|---|
| `success_rate` | ratio | higher |
| `latency_mean` | second | lower |
| `latency_p95` | second | lower |
| `latency_p99` | second | lower |
| `cost_per_1k_success` | cost-unit / 1000 successes | lower |
| `rejection_rate` | ratio | lower |
| `timeout_rate` | ratio | lower |
| `retry_amplification` | ratio | lower |
| `throughput` | request/second | higher |
| `server_utilization` | ratio | context-dependent |
| `max_queue_length` | request | lower |
| `mean_queue_length` | request | context-dependent |

Confidence intervals use a normal approximation across independent replications.
The run files state that limitation; the intervals are not a substitute for
measured data.

## Checkout comparison

The checkout decision compares three candidates under a synthetic 20
requests/second workload and hard constraints:

- C1: request conservation.
- C2: no silent drops.
- C3: team operability, not established by simulation.
- C4: synthetic cost per 1000 successes at most 3.0.
- C5: synthetic p95 latency at most 1.5 seconds.

| Candidate | Success | p95 (s) | Cost / 1k | Timeout | Throughput |
|---|---:|---:|---:|---:|---:|
| A: synchronous | 0.9218 | 0.8703 | 1.8095 | 0.0778 | 18.4213 |
| B: bounded queue | 0.9996 | 1.2059 | 1.3356 | 0.0041 | 19.9670 |
| C: partitioned | 0.9679 | 1.7692 | 3.6260 | 0.1110 | 19.3142 |

Source: the three run files in
[`edition/v12/runs/`](../edition/v12/runs/).

The decision record recommends **B** under the declared constraints. B has the
highest success rate and the lowest cost per successful request, while conceding
p95 latency to A. C violates both the declared cost and p95 constraints. The
recommendation is conditional: C3 operability remains unverified and no
production behavior is established.

## Modernization decision

The second decision compares a staged cutover with a no-cutover baseline. It
returns `insufficient-evidence`, not a recommendation:

- synthetic maximum divergence is 8,925.5 records
  (95% CI 5,561.6-12,289.3);
- rollback completes within the 2,400-second horizon in 10% of replications;
- non-completing rollback durations are censored at the horizon.
- dual-write lag and reconciliation capacity are assumed, not measured.

The correct outcome is to measure the missing inputs and rehearse rollback. A
model cannot turn an unmeasured operational assumption into a decision.

## Decision records

A V12 decision record contains:

- question and context;
- hard and non-quantitative constraints;
- candidate definitions and linked runs;
- metric directions;
- model verification and calibration status;
- recommendation or `insufficient-evidence`;
- reversal triggers;
- limits and pattern links.

The two current decisions are `decision-supported` (checkout) and
`insufficient-evidence` (modernization). Both are conditional on synthetic
inputs.

## Verify V12

```sh
python3 scripts/build_v12_index.py --check
python3 scripts/validate_v12.py
python3 -m unittest tests.test_tycho_v12_engine -v
```

The test module covers the three models, conservation, rollback handling,
sensitivity, convergence and committed-run replay.

## Limits

- All V12 inputs and outputs are synthetic.
- No model is calibrated to a production system.
- No cost is a currency amount or vendor quote.
- Simulation does not establish team operability, security or legal compliance.
- The engine is a reference implementation, not a capacity-planning product.
- A decision record can be `insufficient-evidence`; that is a valid result.

[v12-reader]: ../book/volumes/v12-modeling-simulation-and-decision-validation/README.md

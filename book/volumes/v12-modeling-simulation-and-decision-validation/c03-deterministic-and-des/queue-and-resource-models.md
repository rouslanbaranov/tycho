---
metadata_version: 1
id: "tycho.page.c264e48a38af3148eff0c87a3b98a8dd"
kind: "page"
parent_id: "tycho.chapter.ad6455916f994c0e22e0df7881857f23"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c03-deterministic-and-des/queue-and-resource-models.md"
title: "Queue and resource models"
topic_ids:
  - "queueing"
  - "discrete-event-simulation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Capacity, utilization, Little's law and finite-window measurement in queue models."
route_hints:
  questions:
    - "How are arrival rate, capacity and utilization related?"
    - "When does a finite window mislead?"
  prerequisites: []
  related_ids:
    - "tycho.page.687d2196433c3b076d00c73144dad431"
    - "tycho.page.f914586e44ea034deaf2710c570328fc"
    - "tycho.page.3a70b1cf7e6d7dbbf95c47bd085fc6f4"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "queueing"
    - "utilization"
    - "Little law"
    - "capacity"
    - "backpressure"
evidence_scope:
  source_ids:
    - "src.simpy"
    - "src.little-law"
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

# Queue and resource models

**Question.** How should capacity, occupancy and waiting time be related in a queue model,
and when does a finite-window measurement mislead?

**Short answer.** Arrival rate, service capacity, utilization and occupancy are related but
not interchangeable. Little's law connects average occupancy, arrival rate and average time
in system under stated conditions. A finite simulation window is not the long-run average,
so the model must report the window, the warmup and the uncertainty.

## The basic quantities

- Arrival rate (lambda): requests per second offered to the queue.
- Service capacity (mu): requests per second the server pool can complete when busy.
- Utilization (rho): offered load divided by capacity, rho = lambda / mu for one server
  class, or lambda / (c * mu) for c identical servers.
- Queue length: requests waiting for a server.
- In-system count: waiting plus in service.
- Time in system: from first arrival to terminal outcome.

For the checkout baseline, lambda is 20 requests per second, c is 12 and the mean service
time is 0.5 seconds. The service capacity is 12 / 0.5 = 24 requests per second, so the
utilization is 20 / 24 = 0.833. The measured server utilization in the run is 0.833, which
confirms the arithmetic for this synthetic case.

The saturation stock-flow scenario offers 30 requests per second against 24 requests per
second of service capacity. Utilization is 1.0 after the backlog fills, throughput is 24
requests per second and the rejection rate is 0.2 because admission is capped at 80 requests.
The backlog stays at 77.6 requests in the measurement window.

## Little's law and its finite-window caveat

Little's law states that, under its conditions, the long-run average number in system equals
the arrival rate times the average time in system: L = lambda * W. It is a relation among
averages, not a per-request identity and not a guarantee for a short window.

Kim and Whitt's paper makes the finite-window problem explicit. Measurements over a finite
interval are neither long-run averages nor stationary expectations. Edge effects matter when
the system does not start and end empty. The paper recommends a statistical approach, batch
means and confidence intervals, and shows how to estimate and remove some edge bias.

V12 uses Little's law in two places:

- the stock-flow model reports an approximate time in system as mean backlog divided by
  throughput, labeled as derived;
- the report warns that a finite warmup and horizon can bias the estimate.

The discrete-event model measures latency directly from completed requests, so it does not
need Little's law for its latency metric. It still reports occupancy and throughput, which a
reader can use to check the relation approximately.

## Resource semantics

The SimPy documentation describes resources as capacity-bounded acquisition with a queue,
priority variants and preemption. V12 implements a simpler resource:

- a fixed number of servers;
- a FIFO queue with a capacity;
- a bulkhead limiting queue plus in-service requests;
- a timeout per attempt;
- a bounded retry budget.

The engine does not implement priority or preemption. A model that needs them requires a new
contract and new tests, not an undocumented flag.

## Backpressure and rejection

When the queue is full or the bulkhead is reached, the engine rejects the request and records
the rejection. It does not block the arrival process silently. This matters because a model
that hides rejection can report a high success rate while refusing work at the front door.

The overload scenario demonstrates the difference. A with a 40-request queue and a one-second
deadline succeeds on 0.6488 of offered requests; 0.3495 time out and 0.0005 are rejected.
The timeout rate, not the rejection rate, is the dominant failure mode. A model that reported
only rejection would understate the loss.

## Worked comparison

| Case | Lambda | Capacity | Success | p95 | Timeout |
|---|---|---|---|---|---|
| Baseline stock-flow | 20 | 24 | 1.000 | n/a | 0.000 |
| Saturation stock-flow | 30 | 24 | 0.800 | n/a | 0.000 |
| Checkout A | 20 | 24 | 0.9218 | 0.870 | 0.0778 |
| Checkout B | 20 | 24 | 0.9996 | 1.206 | 0.0041 |
| Checkout C | 20 | 24 | 0.9679 | 1.769 | 0.111 |

The table is deliberately compact. The stock-flow model has no individual p95; the checkout
model does. Candidate B has a higher p95 than A because it waits longer before timing out,
but it completes far more requests and costs less per success.

## Failure modes

- **Utilization above one.** A model reports 120% utilization because it ignores queueing or
  counts capacity incorrectly.
- **Little's law on a short window.** A finite sample is treated as a stationary average
  without edge correction or a confidence interval.
- **Hidden rejection.** The queue is unbounded, so the model never rejects and never shows
  the overload failure.
- **Service-time confusion.** The mean service time is divided by servers in the wrong
  direction, producing a capacity that is too high or too low.
- **Warmup leakage.** Pre-warmup completions are counted in the measurement window.

## Evidence ledger

- [SimPy 4.1 documentation](https://simpy.readthedocs.io/en/latest/)
  supports resource capacity, queueing, priority and preemption vocabulary.
  It does not establish the V12 resource implementation.
- Kim and Whitt, Statistical Analysis with Little's Law (source src.little-law; see the
  reading ledger) supports the finite-window caveat and batch-means approach.
  It does not validate the V12 workload.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports internal-validity and sensitivity checks.
  It does not establish a production capacity.

## Navigation

- Parent: [V12/C03 - Deterministic and DES](../README.md)
- Previous: [Reference engine architecture](reference-engine-architecture.md)
- Next: [Event ordering and timeouts](event-ordering-and-timeouts.md)

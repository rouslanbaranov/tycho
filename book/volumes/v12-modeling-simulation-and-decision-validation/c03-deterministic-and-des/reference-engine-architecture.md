---
metadata_version: 1
id: "tycho.page.687d2196433c3b076d00c73144dad431"
kind: "page"
parent_id: "tycho.chapter.ad6455916f994c0e22e0df7881857f23"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c03-deterministic-and-des/reference-engine-architecture.md"
title: "Reference engine architecture"
topic_ids:
  - "simulation"
  - "reproducibility"
perspectives:
  - "implementation"
  - "evaluation"
summary: "A small dependency-free engine with an event queue, seeds, model families and provenance."
route_hints:
  questions:
    - "Which components make the reference engine verifiable?"
    - "Which determinism rules must hold?"
  prerequisites: []
  related_ids:
    - "tycho.page.c264e48a38af3148eff0c87a3b98a8dd"
    - "tycho.page.f914586e44ea034deaf2710c570328fc"
    - "tycho.page.6c54ed1288a4f0806889865916dc8ccf"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "engine"
    - "event queue"
    - "determinism"
    - "provenance"
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

# Reference engine architecture

**Question.** Which components and determinism rules make the V12 reference engine small
enough to verify and explicit enough to replay?

**Short answer.** The engine is a dependency-free Python module with an event queue, a
seeded random source, three model families, metric aggregation, a sensitivity screen and
canonical hashing. It is intentionally separate from the book pages and from any production
simulator.

## Scope

The engine implements:

- a fixed-step stock-and-flow backlog model with exact request conservation;
- a discrete-event checkout model with capacity, queueing, timeouts, retries and
  backpressure;
- a staged modernization model with dual-write lag, reconciliation and rollback;
- seeded replications and Monte Carlo aggregation;
- a quadratic response-surface sensitivity screen;
- canonical JSON hashing and a replay command.

It does not implement a general-purpose simulation language, distributed execution, a
graphical interface, a database or a production scheduler. A model family that needs a new
mechanism gets a new explicit contract, not an unrecorded engine extension.

## Components

The engine has six parts:

1. **Event queue.** A heap ordered by time, then priority, then insertion sequence.
2. **Random source.** A per-replication random.Random instance seeded from the scenario.
3. **Model families.** Stock-flow, discrete-event and modernization functions selected by
   the model identifier and dynamics kind.
4. **Metric aggregation.** Mean, standard error, confidence interval and convergence status
   across replications.
5. **Sensitivity screen.** A quadratic response surface fitted to sampled outputs, with a
   variance decomposition into main and interaction terms.
6. **Provenance.** SHA-256 over model, scenario, inputs and the substantive result record.

The engine writes a run record only after the model, scenario and result hashes are known.
A failed invariant aborts the run instead of writing a partial record.

## Determinism rules

- The seed comes from the scenario, not from the wall clock.
- Events at the same time are ordered by priority and insertion sequence.
- A retry gets a new timeout event at the retry time.
- A timeout that fires after a completion is ignored by the request state.
- Metric windows use the declared warmup and duration, not the process clock.
- The result hash covers metrics, convergence, uncertainty, sensitivity and limitations.

Determinism is not the same as reproducibility across platforms. The engine stores the
Python version and platform string. The metrics should match on the same input and engine
version; a different floating-point platform can change the last digits.

## A run's life cycle

~~~mermaid
flowchart LR
    M["Load model"] --> S["Load scenario"]
    S --> V["Check model and scenario IDs"]
    V --> R["Run replications"]
    R --> I["Check invariants"]
    I --> A["Aggregate metrics"]
    A --> C["Convergence and sensitivity"]
    C --> H["Hash result"]
    H --> W["Write run record"]
~~~

Text alternative: the engine loads a model and scenario, checks their identifiers, runs the
declared replications, checks invariants, aggregates metrics, computes convergence and
sensitivity, hashes the result and writes the record.

## Replay

The replay command loads the stored run, model and scenario, checks the stored model and
scenario hashes, reruns the scenario and compares the recomputed result hash. It fails on a
changed model, scenario or output. It does not fetch sources, call a network or modify the
book.

## Failure modes

- **Clock leakage.** A metric uses wall-clock time and becomes irreproducible.
- **Unstable event order.** A set or dictionary iteration order changes tie-breaking.
- **Hidden state.** A module-level cache carries state between replications.
- **Partial write.** A run record is written before an invariant check, leaving a plausible
  but invalid result.
- **Silent model fallback.** An unknown model identifier runs a default model instead of
  failing.

The engine fails closed on unknown identifiers and failed invariants.

## Evidence ledger

- [SimPy 4.1 documentation](https://simpy.readthedocs.io/en/latest/)
  supports event, process, resource and scheduling vocabulary.
  It does not establish the V12 engine's correctness.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports computerized-model verification as a distinct concern.
  It does not validate the engine against a production system.

## Navigation

- Parent: [V12/C03 - Deterministic and DES](../README.md)
- Next: [Queue and resource models](queue-and-resource-models.md)
- Engine: scripts/v12_engine.py

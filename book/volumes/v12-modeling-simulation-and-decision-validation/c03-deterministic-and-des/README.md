---
metadata_version: 1
id: "tycho.chapter.ad6455916f994c0e22e0df7881857f23"
kind: "chapter"
parent_id: "tycho.volume.fd0c1a798f9968eed4a679b048deea14"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c03-deterministic-and-des/README.md"
title: "V12/C03 - Deterministic and discrete-event models"
topic_ids:
  - "simulation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which event and queue semantics make a DES result reproducible?"
route_hints:
  questions:
    - "Which event and queue semantics make a DES result reproducible?"
  prerequisites: []
  related_ids:
    - "tycho.page.687d2196433c3b076d00c73144dad431"
    - "tycho.page.c264e48a38af3148eff0c87a3b98a8dd"
    - "tycho.page.f914586e44ea034deaf2710c570328fc"
    - "tycho.page.3a70b1cf7e6d7dbbf95c47bd085fc6f4"
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

# V12/C03 - Deterministic and discrete-event models

**Status:** self-checked chapter landing, 2026-10-29. The reference engine is implemented
and tested locally; it is not a production simulator.

## Purpose and mission

This chapter fixes the execution semantics that make a discrete-event result reproducible:
event ordering, tie-breaking, timeouts, retries, queue capacity, backpressure and replay.
It also defines the deterministic reference cases that a model must pass before its output
is used in a decision.

The chapter does not claim that a queue model predicts a production service. It makes the
model's assumptions and failure boundaries explicit.

## Pages and reasoning route

- [Reference engine architecture](reference-engine-architecture.md): modules, event queue,
  seeds and provenance.
- [Queue and resource models](queue-and-resource-models.md): capacity, utilization,
  Little's law and finite-window measurement.
- [Event ordering and timeouts](event-ordering-and-timeouts.md): the event calendar,
  tie-breaking, cancellation and stale events.
- [Retries and backpressure](retries-and-backpressure.md): retry budgets, backoff,
  amplification and load shedding.

Read the engine page for implementation, the queue page for the arithmetic, the ordering
page for determinism and the retry page for overload behavior.

## Diagram

~~~mermaid
sequenceDiagram
    participant A as Arrival
    participant Q as Queue
    participant S as Server
    participant T as Timeout
    A->>Q: admit or reject
    Q->>S: dispatch when capacity is free
    S-->>Q: release on completion
    T-->>S: cancel expired attempt
    S-->>A: completed, failed or retried
~~~

Text alternative: an arrival is admitted to a bounded queue or rejected. A free server
dispatches a queued request, and completion releases capacity. A timeout can cancel an
expired attempt and trigger a bounded retry.

## Boundaries and evidence

SimPy documentation supports the event, resource and timeout vocabulary. Little's law
supports the relation between average occupancy, arrival rate and time in system, with the
paper's finite-window caveat. Sargent supports the verification and validation distinction.
The engine is independently implemented; no SimPy code is embedded.

The chapter does not model dependency calls, network transport, storage consistency or
deployment failure inside the service.

## Navigation and prerequisites

- Previous: [V12/C02 - Contracts](../c02-contracts/README.md)
- Next: [V12/C04 - Monte Carlo](../c04-monte-carlo/README.md)
- Engine: [scripts/v12_engine.py](../../../../scripts/v12_engine.py)

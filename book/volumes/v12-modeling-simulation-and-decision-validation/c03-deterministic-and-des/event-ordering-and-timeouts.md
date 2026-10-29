---
metadata_version: 1
id: "tycho.page.f914586e44ea034deaf2710c570328fc"
kind: "page"
parent_id: "tycho.chapter.ad6455916f994c0e22e0df7881857f23"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c03-deterministic-and-des/event-ordering-and-timeouts.md"
title: "Event ordering and timeouts"
topic_ids:
  - "discrete-event-simulation"
  - "simulation"
perspectives:
  - "implementation"
  - "evaluation"
summary: "A total event order and per-attempt timeout lifecycle that make DES runs reproducible."
route_hints:
  questions:
    - "Which event-ordering rules are required for reproducibility?"
    - "How does a timeout interact with completion and retry?"
  prerequisites: []
  related_ids:
    - "tycho.page.687d2196433c3b076d00c73144dad431"
    - "tycho.page.c264e48a38af3148eff0c87a3b98a8dd"
    - "tycho.page.3a70b1cf7e6d7dbbf95c47bd085fc6f4"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "event ordering"
    - "timeout"
    - "tie-breaking"
    - "stale event"
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

# Event ordering and timeouts

**Question.** Which event-ordering and timeout rules must be fixed so that two runs with the
same seed produce the same outcome?

**Short answer.** A discrete-event engine must define a total order over events, schedule
timeouts explicitly, cancel stale events and record how a retry resets a deadline. V12 uses
(time, priority, insertion sequence) and a per-attempt timeout event.

## Why event order is part of the model

Two events at the same timestamp can produce different results depending on which is
processed first. A service completion at t=1.0 and a timeout at t=1.0 are the same timestamp.
If the completion is processed first, the request succeeds. If the timeout is processed
first, the request fails and may retry.

A model that relies on dictionary iteration order or an unstable sort is not reproducible.
The V12 event queue orders by time, then priority, then insertion sequence. The insertion
sequence is a monotonically increasing integer, so the order is total and deterministic.

## Priorities

V12 uses three priorities:

- 0 for service completion and timeout;
- 1 for arrival;
- 2 for retry.

The priorities are a modeling choice, not a universal rule. A different system may need a
different order. The important property is that the choice is declared and tested.

## Timeout lifecycle

A request receives a timeout event when it enters the system. The deadline is the arrival
time plus the configured timeout. If the request completes before the deadline, the later
timeout event finds a completed request and is ignored. If the timeout fires first:

- a queued request is removed from the queue;
- an in-service request releases its server;
- the attempt is counted as timed out;
- if attempts remain, a retry event is scheduled after the backoff;
- otherwise the request is terminally failed.

A retry schedules a new timeout at the retry time plus the timeout. The deadline is
per-attempt, not per-request lifetime. This matters: a request with three attempts can spend
up to three timeouts plus two backoffs in the system.

## A worked sequence

Consider a request arriving at t=0 with a one-second timeout and a service time of 0.4
seconds. If a server is free, the completion event is at t=0.4 and the timeout at t=1.0. The
completion is processed first; the timeout is ignored. If the queue is full, the request is
rejected at t=0 and no service event exists; the timeout event later finds a completed
request and is ignored.

Now consider a request that waits 0.9 seconds and then starts service with a 0.4-second
service time. Its timeout is at t=1.0, before its completion at t=1.3. The timeout fires,
releases the server and schedules a retry. The completion event at t=1.3 finds no in-service
request and is ignored. The request can succeed on a later attempt, but its first attempt is
recorded as a timeout.

## A sequence diagram

~~~mermaid
sequenceDiagram
    participant R as Request
    participant Q as Queue
    participant S as Server
    participant T as Timeout
    R->>Q: arrive at t=0
    Q->>S: dispatch at t=0.9
    S->>T: completion scheduled at t=1.3
    T->>S: timeout at t=1.0
    S-->>Q: release and retry
~~~

Text alternative: a request arrives, waits, starts service, and is cancelled by its timeout
before the scheduled completion. The server is released and a retry is scheduled.

## Stale events

A stale event is an event that was scheduled before a state change and is no longer valid.
The completion event after a timeout is stale. The timeout event after a completion is stale.
The engine does not delete stale events from the heap; it checks the request state when the
event is processed. This keeps the heap simple and the behavior deterministic.

A stale event must never change the outcome. The engine's tests include a completion after a
timeout and a timeout after a completion.

## Failure modes

- **Unstable tie-breaking.** Two events at the same time depend on hash order.
- **Timeout resets on retry omitted.** A retry inherits an expired deadline and fails
  immediately.
- **Timeout not cancelled on completion.** A completed request is later marked failed.
- **Double release.** A timeout and a completion both free the same server, increasing
  capacity beyond the configured pool.
- **Floating-point equality.** Events at 1.0 and 1.0000000001 are treated as equal or not
  equal without a declared tolerance.

V12 rounds scheduled times to 12 decimal places and compares event times as floats. That is
sufficient for the synthetic scenarios; a model with very small time units would need a
declared tolerance.

## Evidence ledger

- [SimPy 4.1 documentation](https://simpy.readthedocs.io/en/latest/)
  supports event scheduling, process interaction and timeout vocabulary.
  It does not establish the V12 ordering rules.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports traces and event-validity checks as verification techniques.
  It does not validate a V12 sequence.

## Navigation

- Parent: [V12/C03 - Deterministic and DES](../README.md)
- Previous: [Queue and resource models](queue-and-resource-models.md)
- Next: [Retries and backpressure](retries-and-backpressure.md)

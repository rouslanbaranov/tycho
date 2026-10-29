---
metadata_version: 1
id: "tycho.page.3a70b1cf7e6d7dbbf95c47bd085fc6f4"
kind: "page"
parent_id: "tycho.chapter.ad6455916f994c0e22e0df7881857f23"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c03-deterministic-and-des/retries-and-backpressure.md"
title: "Retries and backpressure"
topic_ids:
  - "discrete-event-simulation"
  - "decision-records"
perspectives:
  - "architecture"
  - "operations"
summary: "Retry budgets, jitter and explicit admission limits under overload."
route_hints:
  questions:
    - "When do retries amplify overload?"
    - "Which backpressure limits make loss explicit?"
  prerequisites: []
  related_ids:
    - "tycho.page.c264e48a38af3148eff0c87a3b98a8dd"
    - "tycho.page.f914586e44ea034deaf2710c570328fc"
    - "tycho.page.3cfd08ee56330be9b7a2d37975c3fe26"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "retry"
    - "backoff"
    - "jitter"
    - "backpressure"
    - "load shedding"
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

# Retries and backpressure

**Question.** When do retries absorb transient failure, and when do they amplify overload?

**Short answer.** A retry helps only when the failure is transient and the retry budget is
bounded. Without a budget, backoff and jitter, retries add load to an already saturated
system. Backpressure, queue capacity and a bulkhead decide whether the system rejects work
explicitly or collapses under it.

## Retry amplification

If every request is attempted 1.05 times on average, the service load is 5% higher than the
offered load. If every request is attempted three times, the load can be three times higher.
The retry amplification metric is total attempts divided by offered requests. V12 reports it
for every discrete-event run.

The A/B/C comparison shows the difference:

- A has no retry budget: retry amplification 1.000, timeout rate 0.0778, success 0.9218.
- B has three attempts with exponential backoff and full jitter: retry amplification 1.004,
  timeout rate 0.0041, success 0.9996.
- C has two attempts with linear backoff: retry amplification 1.079, timeout rate 0.111,
  success 0.9679.

B's retry budget absorbs transient service-time variation without materially increasing load.
C's retries amplify load and do not prevent an 11.1% timeout rate. A's lack of retries avoids
amplification but loses 7.8% of requests to its one-second deadline.

## Backoff and jitter

Exponential backoff increases the delay after each attempt. Full jitter replaces the delay
with a uniform draw between zero and the computed delay. Jitter reduces synchronized retry
waves: without it, many clients that failed at the same time retry at the same time.

V12 implements three backoff kinds: none, exponential and linear. It implements no jitter,
full jitter and equal jitter. The scenario declares the choice. A model that uses jitter
without recording it is not reproducible.

## Backpressure

Backpressure is the explicit refusal or delay of work when capacity is exhausted. V12 uses
three limits:

- queue capacity: maximum waiting requests;
- bulkhead: maximum waiting plus in-service requests;
- timeout: maximum time an attempt may occupy the system.

When a limit is reached, the request is rejected and counted. A model with an unbounded queue
never rejects; it accumulates backlog and reports a latency that is an artifact of the
horizon. A model with no timeout lets a slow request occupy a server indefinitely.

## The overload boundary

The overload scenario offers 30 requests per second to a 24-request-per-second pool with a
40-request queue and a one-second deadline. The run reports:

- success rate 0.6488 (95% CI 0.6443-0.6534);
- timeout rate 0.3495 (95% CI 0.3451-0.3540);
- rejection rate 0.0005;
- mean queue length 12.79;
- server utilization 0.9966.

The dominant failure is timeout, not rejection. The queue is large enough to absorb arrivals
but not large enough to prevent deadline expiry. A report that focuses on rejection alone
would miss most of the loss: rejection is 0.05% while timeout is 35.0%.

## A retry state diagram

~~~mermaid
stateDiagram-v2
    [*] --> Queued
    Queued --> InService: server free
    InService --> Completed: before deadline
    InService --> TimedOut: deadline reached
    Queued --> TimedOut: deadline reached
    TimedOut --> RetryWait: attempts remain
    RetryWait --> Queued: backoff elapsed
    TimedOut --> Failed: no attempts remain
    Queued --> Rejected: queue or bulkhead full
    Completed --> [*]
    Failed --> [*]
    Rejected --> [*]
~~~

Text alternative: a request waits or enters service, then completes, times out, retries or is
rejected. A timed-out request with attempts remaining waits for backoff and re-enters the
queue; otherwise it fails.

## Failure modes

- **Retry storm.** Every client retries immediately. The service sees a load spike just as it
  is least able to handle it.
- **Unbounded retries.** A request can retry forever and consume capacity indefinitely.
- **Timeout larger than the caller deadline.** The server continues work after the caller
  has given up, wasting capacity.
- **Retry without idempotency.** A timed-out request may have committed an effect; the retry
  duplicates it. The queue model does not represent business idempotency.
- **Backpressure without observation.** The system rejects work but does not count it, so the
  success rate looks better than the user experience.

The last two are outside the queue model's boundary. They must be recorded as limitations,
not solved by a simulation parameter.

## Evidence ledger

- [SimPy 4.1 documentation](https://simpy.readthedocs.io/en/latest/)
  supports resource capacity, process interruption and timeout vocabulary.
  It does not establish the V12 retry policy.
- Kim and Whitt (source src.little-law; see the reading ledger) supports finite-window
  occupancy and time-in-system measurement.
  It does not validate the retry behavior.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports extreme-condition and sensitivity checks.
  It does not establish production resilience.

## Navigation

- Parent: [V12/C03 - Deterministic and DES](../README.md)
- Previous: [Event ordering and timeouts](event-ordering-and-timeouts.md)
- Next: [V12/C04 - Monte Carlo](../c04-monte-carlo/README.md)

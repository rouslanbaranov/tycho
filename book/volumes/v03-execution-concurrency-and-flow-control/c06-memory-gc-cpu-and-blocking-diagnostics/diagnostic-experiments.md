---
metadata_version: 1
id: "tycho.page.0d095fa3993a48f0b70ae375cb60c493"
kind: "page"
parent_id: "tycho.chapter.22e3f1a320e54179a176871646debd00"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c06-memory-gc-cpu-and-blocking-diagnostics/diagnostic-experiments.md"
title: "Discriminating runtime experiments"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "What controlled observation would justify changing execution or garbage collection?"
route_hints:
  questions:
    - "What controlled observation would justify changing execution or garbage collection?"
  prerequisites:
    - "tycho.page.e5f63598da754ee181804df0ce297b95"
  related_ids:
    - "tycho.chapter.22e3f1a320e54179a176871646debd00"
    - "tycho.page.b6cecfd7301b408db611228b4cec59c5"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "diagnostic"
    - "experiments"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.b6cecfd7301b408db611228b4cec59c5; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Discriminating runtime experiments

**Owning question:** What controlled observation would justify changing execution or garbage collection?

This page belongs to [V03/C06 — Memory, GC, CPU and blocking diagnostics](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:5 -->
## 5. Original synthetic failure: the misleading virtual-thread fix

Invent a web application that accepts 200 attempted requests/s. The first team hypothesis is “platform threads are blocking, so switch to virtual threads.” The actual limiting condition is unknown. Suppose a *hypothetical* dependency can execute only 60 concurrent queries, and each query becomes slower as active DB connections increase.

- Replacing platform threads with virtual threads may allow far more simultaneous waiting tasks at lower thread overhead. It does **not** give the DB more query capacity.
- Increasing the JDBC pool may raise database contention, reduce throughput and enlarge request tails.
- Reducing connection hold time, adding bounded admission, reducing query cost or fixing a lock can be more effective **if the measured data supports those causes**.
- If the real workload is CPU-bound, adding concurrency alone can merely add scheduling and contention; use CPU hot-path profiling rather than an I/O-oriented execution model argument.

The hypotheses would be falsified by a correlation matrix at fixed **offered** rate and data contents: service/pool wait, CPU running fraction, query time distribution, DB saturation and completed legitimate outcomes. Without these readings, “virtual threads solved performance” would be a fictional assertion.

### An incident chronology worth collecting

1. Record offered arrivals, retries and user-visible success/failure in the degradation window.
2. Record node/container CPU use versus limits and throttling; separate process RSS and Java heap.
3. Align per-request/span latency, queue/pool waits, GC pause timestamps and runtime thread state.
4. Capture a bounded profile with the right permissions and safety controls; prevent sensitive data disclosure.
5. Form at least two rival hypotheses; test the least risky reversible intervention under equivalent load.
6. Assert business correctness and recovery, not only smaller p99, before approving a change.

A change that lowers p99 by rejecting unobserved requests or weakening data correctness is not a performance success.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:6 -->
## 6. How to choose the next experiment

| Hypothesis | Small, falsifiable experiment | Correctness gate |
|---|---|---|
| CPU code is expensive | Profile hot path; vary algorithmic workload at fixed data and arrivals | Identical output and error outcomes |
| Pool wait dominates | Measure acquisition/call time; adjust admission before connection ceiling | No duplicate/omitted effects, no backend exhaustion |
| GC is dominant | Correlate GC pause with user traces, allocation and live-set; modify one supported knob in isolated environment | No memory exhaustion or hidden latency regression |
| Native memory is leaking | Reconcile RSS/native allocations with buffer/thread lifetimes and workload state | Memory remains bounded and recovered resources are reusable |
| One lock serializes work | Sample lock owners and vary concurrent keys | Enforced invariants remain intact |
| Execution model limits IO concurrency | Compare bounded platform versus virtual/reactive configurations under equal downstream capacity | Same cancellation, error and backpressure behavior |

There is no automatic threshold for selecting a different garbage collector or executor. The measured critical resource and failure semantics determine whether redesign is justified.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](memory-tools.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](cpu-memory-gc-and-blocking-diagnostics.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

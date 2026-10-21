---
metadata_version: 1
id: "tycho.page.e5f63598da754ee181804df0ce297b95"
kind: "page"
parent_id: "tycho.chapter.22e3f1a320e54179a176871646debd00"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c06-memory-gc-cpu-and-blocking-diagnostics/memory-tools.md"
title: "Memory domains and diagnostic evidence"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "What can heap, native-memory, CPU and blocking tools actually establish?"
route_hints:
  questions:
    - "What can heap, native-memory, CPU and blocking tools actually establish?"
  prerequisites:
    - "tycho.page.5567c6c6ca5148a2b117c858d305e0f3"
  related_ids:
    - "tycho.chapter.22e3f1a320e54179a176871646debd00"
    - "tycho.page.b6cecfd7301b408db611228b4cec59c5"
    - "tycho.page.0d095fa3993a48f0b70ae375cb60c493"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "memory"
    - "tools"
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
# Memory domains and diagnostic evidence

**Owning question:** What can heap, native-memory, CPU and blocking tools actually establish?

This page belongs to [V03/C06 — Memory, GC, CPU and blocking diagnostics](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:3 -->
## 3. Java heap is only one memory domain

The JVM heap stores managed objects, but overall process memory may also include thread stacks, native libraries, direct buffers, memory mappings, JIT/compiler and runtime structures. A container can exceed its physical or configured memory limit even if recorded heap occupancy appears acceptable.

A high allocation rate can be harmless if objects die young and collection work fits the resource budget; a small allocation rate can still cause a persistent live-set leak. Heap **used before collection** is not a sufficient leak indicator. Compare live data after comparable collection points, object lifetimes, retention roots and request mix. Large allocation profiles may reflect high-throughput normal paths, not retained data.

[Oracle Java 21 G1 documentation](https://docs.oracle.com/en/java/javase/21/gctuning/garbage-first-g1-garbage-collector1.html) describes mostly concurrent G1 collection and its probabilistic pause-time goal, rather than hard pause guarantees. [G1 tuning documentation](https://docs.oracle.com/en/java/javase/21/gctuning/garbage-first-garbage-collector-tuning.html) distinguishes throughput-versus-pause trade-offs and conditions associated with full collection. A collector's default and tuning controls are version-specific. Do not assume identical semantics in a different JDK release or vendor runtime.

**Trade-off:** reducing GC pause duration can use more concurrent CPU or memory headroom; maximizing throughput can worsen individual response pauses. The user journey, offered workload, allocation rate, real live-set and latency distribution determine what to optimize—not a universal GC flag.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:4 -->
## 4. What the actual diagnostic tools prove

[JDK Flight Recorder (JFR) and Mission Control](https://docs.oracle.com/en/java/javase/25/troubleshoot/diagnostic-tools.html) support timestamped JVM events on configured runtimes. The [JDK 25 jcmd manual](https://docs.oracle.com/en/java/javase/25/docs/specs/man/jcmd.html) documents supported diagnostics and their possible impact. Only issue exact tool commands after confirming JVM vendor, version, access, safe recording policy and expected overhead.

The independent open-source [async-profiler](https://github.com/async-profiler/async-profiler) documents CPU, allocation, lock and native/wall-clock profiling modes. Its [profiling modes guidance](https://github.com/async-profiler/async-profiler/blob/master/docs/ProfilingModes.md) distinguishes sample sources and warns that collecting everything continuously can be inappropriate. A CPU flame graph can point to hot functions; it cannot prove request critical path, end-to-end correctness or cause of waiting without correlated evidence.

| Instrument | Evidence it can help produce | Limitation to record |
|---|---|---|
| End-to-end request trace | Parent and instrumented span durations; dependency correlation | Uninstrumented waits, sampling and clock boundaries may hide work |
| CPU sampling profile | Code executing on CPU across sampled stacks | Missing waiting states or low-frequency intermittent events |
| Wall-clock stack sampling | Running and blocked stacks in a time window | Sampling overhead, thread grouping and signal/runtime limits |
| Allocation profile | Sources and approximate volume of allocations | Does not itself identify retained live-set or leak |
| JFR/GC event records | Pause timing, allocation and runtime events by configured event set | Disabled events, inaccessible data or sampling may omit causal context |
| Thread dump / lock diagnostics | Contention candidates, stack snapshots and lock ownership | Instantaneous snapshot cannot establish prevalence |
| OS/container accounting | CPU quota, memory limit, page faults, scheduling signals | Process metrics alone cannot locate application effect or business success |

Always compare timestamps for the **same load window**. A recording from an idle, already warmed service cannot validate the behavior of a cold-start peak.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](latency-diagnosis.md) |
| Next | [Continue the reasoning](diagnostic-experiments.md) |
| Integrated question | [Original scenario and limits](cpu-memory-gc-and-blocking-diagnostics.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

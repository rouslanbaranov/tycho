---
metadata_version: 1
id: "tycho.page.b6cecfd7301b408db611228b4cec59c5"
kind: "page"
parent_id: "tycho.chapter.22e3f1a320e54179a176871646debd00"
canonical_path: "book/volumes/v03/c06/cpu-memory-gc-and-blocking-diagnostics.md"
title: "CPU, memory, garbage collection and blocking: an evidence-first diagnosis"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Memory, GC, CPU and blocking diagnostics. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How should bottleneck observations constrain execution-model choice?"
  prerequisites: []
  related_ids:
    - "tycho.page.02238832b395417bae63939cd96b9134"
    - "tycho.page.114da51171c2474ebd56ee3bebad3bcb"
    - "tycho.page.883194a820194482bc2508c8e4568d86"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.e181d96c75784f818a330bb0f266520c"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.5567c6c6ca5148a2b117c858d305e0f3"
    - "tycho.page.e5f63598da754ee181804df0ce297b95"
    - "tycho.page.0d095fa3993a48f0b70ae375cb60c493"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "CPU"
    - "memory"
    - "garbage"
    - "collection"
    - "and"
    - "blocking"
    - "evidence-first"
    - "diagnosis"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:-1 -->

# CPU, memory, garbage collection and blocking: an evidence-first diagnosis

> **Tycho draft chapter V03/C06**, independently researched from public JDK and profiling documentation on 2026-10-19. Synthetic symptoms and decision experiments only. No process profiling, benchmarking, production recording or independent technical review has been executed for this page.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:0 -->
## Purpose and mission

A slow Java service may be limited by CPU execution, heap allocation and garbage collection, native memory, thread/executor contention, blocking I/O or a saturated dependency. The same user-visible latency curve can arise from each of these causes. **Thread count, low CPU utilization and heap occupancy are observations—not diagnoses and not automatic evidence for reactive programming, virtual threads or a new garbage collector.**

The central task is to identify **where elapsed time is spent**, which resource is saturated, and what evidence would falsify the leading cause. This chapter introduces a reproducible symptom-to-mechanism diagnostic workflow. The execution-model chapters own the mechanisms of [platform/virtual threads](../c02/platform-threads-executors-and-virtual-threads.md), [reactive backpressure](../c03/reactor-webflux-r2dbc-and-backpressure.md), and [event loops and frameworks](../../../execution/vertx-netty-quarkus-mutiny-and-rxjava.md). [Queueing](../../v07/c01/queueing-littles-law.md) and [tail latency](../../v07/c04/tail-latency-fanout-and-deadline-budgets.md) own request-level inference.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:9 -->
## Engineering walkthrough — High latency with low JVM heap pressure

**Original hypothetical diagnostic:** enabling virtual-thread request handling coincides with doubled p99 and rising RSS memory while GC pause duration remains low. An engineer immediately blames the garbage collector and selects a new collection algorithm. Yet the dominant delay may be a database connection queue; RSS growth might instead arise from native buffers, thread stacks, direct memory or container-level accounting.

| Evidence requested | Supports which diagnosis | Does *not* establish |
|---|---|---|
| JVM JFR allocation, GC pause and safepoints | Heap allocation/collection contribution | Native RSS cause or remote DB throughput |
| Async-profiler CPU and lock modes | Hot CPU paths or contention | Complete network wait accounting |
| Native memory and process/container telemetry | Off-heap pools and reserved/committed memory | User-visible latency without request spans |
| Connection-acquire and queue timestamps | Scarce downstream wait | Virtual threads are fundamentally slower |

Suppose synthetic traces show 180 ms of 230 ms request time spent acquiring a DB lease and only 8 ms in GC pauses across the same interval. A collector swap does not target the dominant per-request wait even if collector tuning is useful for a different workload. Releasing connections before unrelated remote waits, bounding admission or optimizing the query is a more discriminating candidate; verify with equal arrivals.

**Negative test (not run):** hold the JDBC pool fixed and alternate execution model, then independently enlarge the pool under a safe DB budget. Correlate JFR, GC, CPU, allocation, native RSS, connection wait and correct completion, including restarts and canceled calls. Source manuals for JFR/jcmd and collectors describe diagnostic mechanisms; they do not certify the fictional decomposition or establish a particular collector choice.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:10 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — Generational ZGC workloads](../../../cases/netflix-generational-zgc-workloads.md)**. **Relevant mechanism or architectural contrast:** GC selection depends on latency, allocation, heap and memory/cpu budgets; some workloads favor alternatives. **Not established by this report/playbook:** Company-reported JDK21 observations do not prove Generational ZGC is universally best or specify another service's p99.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Use workload-correlated CPU, allocation, GC, blocking and dependency observations to distinguish competing bottleneck explanations.

Low CPU and many waiting threads do not identify a collector problem; change one hypothesis only after establishing the limiting resource.

The detailed pages separate the mechanisms that make this decision conditional:

- [Latency decomposition and symptom hypotheses](latency-diagnosis.md) — Which competing bottleneck explanations fit the same slow request?
- [Memory domains and diagnostic evidence](memory-tools.md) — What can heap, native-memory, CPU and blocking tools actually establish?
- [Discriminating runtime experiments](diagnostic-experiments.md) — What controlled observation would justify changing execution or garbage collection?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

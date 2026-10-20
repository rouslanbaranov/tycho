---
metadata_version: 1
id: "tycho.chapter.22e3f1a320e54179a176871646debd00"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03/c06/README.md"
title: "V03/C06 — Memory, GC, CPU and blocking diagnostics"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How should bottleneck observations constrain execution-model choice? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How should bottleneck observations constrain execution-model choice?"
  prerequisites:
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
  related_ids:
    - "tycho.page.b6cecfd7301b408db611228b4cec59c5"
    - "tycho.page.5567c6c6ca5148a2b117c858d305e0f3"
    - "tycho.page.e5f63598da754ee181804df0ce297b95"
    - "tycho.page.0d095fa3993a48f0b70ae375cb60c493"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V03/C06 — Memory, GC, CPU and blocking diagnostics

## Purpose and mission

How should bottleneck observations constrain execution-model choice? This chapter owns that question within execution models, concurrency and flow control. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Use workload-correlated CPU, allocation, GC, blocking and dependency observations to distinguish competing bottleneck explanations.

Low CPU and many waiting threads do not identify a collector problem; change one hypothesis only after establishing the limiting resource. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](cpu-memory-gc-and-blocking-diagnostics.md) | How should bottleneck observations constrain execution-model choice? |
| [Latency decomposition and symptom hypotheses](latency-diagnosis.md) | Which competing bottleneck explanations fit the same slow request? |
| [Memory domains and diagnostic evidence](memory-tools.md) | What can heap, native-memory, CPU and blocking tools actually establish? |
| [Discriminating runtime experiments](diagnostic-experiments.md) | What controlled observation would justify changing execution or garbage collection? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V03/C05 — Thread, connection and buffer pools](../c05/README.md) |
| Next | [V04/C01 — Time, causality and ordering](../../v04/c01/README.md) |
| Prerequisite | [V03/C05 — Thread, connection and buffer pools](../c05/README.md) |
| Source reading | [Page-local evidence and versions](cpu-memory-gc-and-blocking-diagnostics.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:7 -->
## 7. Evidence ledger and honesty boundary

| Public material inspected | Supported scope | Not demonstrated |
|---|---|---|
| [Oracle Java 21 G1 GC](https://docs.oracle.com/en/java/javase/21/gctuning/garbage-first-g1-garbage-collector1.html) | Collector concurrency and pause-time target semantics | Runtime characteristics of synthetic service or JDK 25 configuration |
| [Oracle Java 21 G1 tuning](https://docs.oracle.com/en/java/javase/21/gctuning/garbage-first-garbage-collector-tuning.html) | Documented pause/throughput and full-GC considerations | Any observed improvement from changing flags |
| [Oracle JDK 25 diagnostic tools/JFR](https://docs.oracle.com/en/java/javase/25/troubleshoot/diagnostic-tools.html) | Diagnostic event, Mission Control and basic tooling purpose | Actual JFR recording or data collection |
| [Open-source async-profiler usage and profiling modes](https://github.com/async-profiler/async-profiler/blob/master/docs/ProfilingModes.md) | CPU, wall-clock, allocation and lock sample distinctions | Universal cross-platform sampling completeness |

All diagrams, suspected failures, rates, experiments and recommendations for the invented workload are synthetic. No sensitive process was accessed, no profiler was run, and no real user-impact claim is supported. Independent review, version-specific runtime reproduction and full text-to-source precision checks remain open.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b6cecfd7301b408db611228b4cec59c5:8 -->
## Navigation

- Intended book owner: **V03/C06** in [proposed TOC](../../../PROPOSED-STRUCTURE.md); current section [Java concurrency and execution](../../../execution/README.md).
- Relevant runtime: [Platform and virtual threads](../c02/platform-threads-executors-and-virtual-threads.md); [Reactive execution](../c03/reactor-webflux-r2dbc-and-backpressure.md); [Event-loop frameworks](../../../execution/vertx-netty-quarkus-mutiny-and-rxjava.md).
- Cross-layer: [Connection pool budgets](../c05/connection-pools-hikaricp-pgbouncer.md); [Queueing](../../v07/c01/queueing-littles-law.md); [Tail latency](../../v07/c04/tail-latency-fanout-and-deadline-budgets.md).

<!-- /tycho-question-source -->

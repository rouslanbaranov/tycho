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
summary: "How should bottleneck observations constrain execution-model choice?"
route_hints:
  questions:
    - "How should bottleneck observations constrain execution-model choice?"
  prerequisites:
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
  related_ids: []
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

| Page | Owning question |
|---|---|
| [CPU, memory, garbage collection and blocking: an evidence-first diagnosis](cpu-memory-gc-and-blocking-diagnostics.md) | How should bottleneck observations constrain execution-model choice? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Divide wall-clock latency before selecting a remedy](cpu-memory-gc-and-blocking-diagnostics.md#1-divide-wall-clock-latency-before-selecting-a-remedy).
- [2. Working symptom matrix](cpu-memory-gc-and-blocking-diagnostics.md#2-working-symptom-matrix).
- [Engineering walkthrough — High latency with low JVM heap pressure](cpu-memory-gc-and-blocking-diagnostics.md#engineering-walkthrough-high-latency-with-low-jvm-heap-pressure).
- [Applied M9 evidence: what transfers and what does not](cpu-memory-gc-and-blocking-diagnostics.md#applied-m9-evidence-what-transfers-and-what-does-not).

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

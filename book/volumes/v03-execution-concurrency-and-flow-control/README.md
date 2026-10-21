---
metadata_version: 1
id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/README.md"
title: "V03 — Execution models, concurrency and flow control"
topic_ids:
  - "execution-models"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A resource-budget view tracing request admission, execution/task/connection pools and cancellation to the external effect boundary."
route_hints:
  questions:
    - "A resource-budget view tracing request admission, execution/task/connection pools and cancellation to the external effect boundary."
  prerequisites:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
  related_ids:
    - "tycho.chapter.13ad4371e75b49dcb5e082ea62083ee3"
    - "tycho.chapter.d5b789c9cd7e4cb693c22943423531c2"
    - "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
    - "tycho.chapter.7a07973ba5314c3983a4c93acc1d1b89"
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
    - "tycho.chapter.22e3f1a320e54179a176871646debd00"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.hikaricp"
    - "src.jep444"
    - "src.jep491"
    - "src.r2dbc"
  claim_ids: []
  status: "source-linked"
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

# V03 — Execution models, concurrency and flow control

## Purpose and mission

Explain the execution and resource budgets behind a request.

The outcome of this volume is: A resource-budget view tracing request admission, execution/task/connection pools and cancellation to the external effect boundary.

## A worked cross-chapter synthesis

A fictional endpoint fans out to two dependencies and then writes through a bounded database pool. Replacing worker threads changes waiting overhead, while the database permits and the caller's time budget remain finite. Diagnose which resource is limiting before attributing the outcome to the programming model.

Trace admission, task lifetime, scheduling, buffered work, connection acquisition and the external effect. Assign an owner and a limit at each boundary. Compare blocking, virtual-thread and reactive approaches against the same cancellation and downstream-capacity contract rather than assuming one runtime model dominates every workload.

## Questions and chapters

| Chapter | Owning question |
|---|---|
| [V03/C01 — Threads, tasks and coordination](c01-threads-tasks-and-coordination/README.md) | What creates concurrency and which shared state creates contention? |
| [V03/C02 — Java execution and virtual threads](c02-java-execution-and-virtual-threads/README.md) | What improves concurrency without creating downstream capacity? |
| [V03/C03 — Reactive streams, demand and cancellation](c03-reactive-streams-demand-and-cancellation/README.md) | How do backpressure, scheduling and blocking boundaries affect execution? |
| [V03/C04 — Asynchronous APIs and streaming](c04-asynchronous-apis-and-streaming/README.md) | Which flow and cancellation semantics are required across protocols? |
| [V03/C05 — Thread, connection and buffer pools](c05-thread-connection-and-buffer-pools/README.md) | How do pool sizes, queues and timeouts compose across layers? |
| [V03/C06 — Memory, GC, CPU and blocking diagnostics](c06-memory-gc-cpu-and-blocking-diagnostics/README.md) | How should bottleneck observations constrain execution-model choice? |

## Choosing a reading route

For a first reading, follow the chapter order. For diagnosis, connect the observed outcome to its authority and failure boundary using: [V03/C01](c01-threads-tasks-and-coordination/README.md), [V03/C02](c02-java-execution-and-virtual-threads/README.md), [V03/C03](c03-reactive-streams-demand-and-cancellation/README.md), [V03/C05](c05-thread-connection-and-buffer-pools/README.md), [V03/C06](c06-memory-gc-cpu-and-blocking-diagnostics/README.md). Return to the exact page-local source ledger before making a version-specific claim.

Prerequisite context: V01/C02 and V02/C05.

Read [V01/C02](../v01-requirements-and-architecture/c02-workload-and-demand-models/README.md), [V02/C05](../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/README.md) for the named entry assumptions.

### Reasoning boundaries

This original conceptual map separates competing inputs rather than promising a universal solution.

~~~mermaid
flowchart TD
    Q["V03/C01 — Threads, tasks and coordination"] --> M["V03/C02 — Java execution and virtual threads"]
    Q --> E["Evidence and unknown inputs"]
    M --> D{"Meets the declared constraints?"}
    E --> D
    D -->|Supported| R["V03/C06 — Memory, GC, CPU and blocking diagnostics"]
    D -->|Unresolved| U["Measure, revise or retain the baseline"]
~~~

Text alternative: establish threads, tasks and coordination, compare java execution and virtual threads with the available evidence, and either carry a supported result forward or return to unresolved inputs. The figure describes a reasoning route, not observed runtime behavior.

## Counterexample and handoff

Cancellation may stop local waiting after the remote effect has committed. Backpressure on one publisher does not bound a hidden queue elsewhere. Handoff to distributed semantics must therefore include logical effect identity and recovery lookup, alongside the execution budget. Product-specific tuning still needs a compatible version and a real workload.

## Navigation and source boundaries

| Route | Destination |
|---|---|
| Parent | [Book contents](../../README.md) |
| Previous volume | [V02](../v02-application-boundaries-and-contracts/README.md) |
| Next volume | [V04](../v04-distributed-coordination-and-events/README.md) |
| Historical applications | [Casebook and synthetic playbooks](../../cases/README.md) |

## Evidence and known limits

The scenario is original synthetic reasoning. The chapters contain the accepted manuscript and its published evidence; no synthetic number or historical result is a measured prediction for another system. This new synthesis is editorially self-checked, not independently certified. Source-access restrictions, unexecuted technology experiments and original case denominators remain explicit in their owning pages. Product-specific adoption still requires compatible versions and the target workload.

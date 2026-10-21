---
metadata_version: 1
id: "tycho.chapter.13ad4371e75b49dcb5e082ea62083ee3"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c01-threads-tasks-and-coordination/README.md"
title: "V03/C01 — Threads, tasks and coordination"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What creates concurrency and which shared state creates contention? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What creates concurrency and which shared state creates contention?"
  prerequisites:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
  related_ids:
    - "tycho.page.4e075e4ebc644f0e9b92c05294f62ca4"
    - "tycho.page.2cdffb0fc6394a1596c8358c852a30e8"
    - "tycho.page.113050e25ec643da98578b98eba1c519"
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

# V03/C01 — Threads, tasks and coordination

## Purpose and mission

What creates concurrency and which shared state creates contention? This chapter owns that question within execution models, concurrency and flow control. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Give concurrent work a lifetime, result owner and cancellation policy rather than treating each thread as an independent business operation.

Cancelling a task requests termination; it cannot undo a downstream commit that already occurred. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](threads-tasks-structured-coordination.md) | What creates concurrency and which shared state creates contention? |
| [Task ownership, lifetimes and cancellation](task-lifetime.md) | Who owns concurrent work and what happens when its parent leaves? |
| [Shared invariants and irreversible effects](shared-state-effects.md) | Why do concurrency-safe classes and cancellation not establish a business invariant? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V02/C07 — Authorization boundaries and multitenancy](../../v02-application-boundaries-and-contracts/c07-authorization-boundaries-and-multitenancy/README.md) |
| Next | [V03/C02 — Java execution and virtual threads](../c02-java-execution-and-virtual-threads/README.md) |
| Prerequisite | [V01/C02 — Workload and demand models](../../v01-requirements-and-architecture/c02-workload-and-demand-models/README.md) |
| Prerequisite | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/README.md) |
| Source reading | [Page-local evidence and versions](threads-tasks-structured-coordination.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.4e075e4ebc644f0e9b92c05294f62ca4:6 -->
## 6. Proposed tests and source ledger

A reviewable fixture would: fork two tasks then force one to fail; cancel the parent with an outstanding connection; inject a lost response after write commit; force an uncooperative blocking call; vary virtual-thread count while holding the datastore pool fixed; check error, cleanup and duplicate-effect invariants. **None was run** in preparing this chapter.

| Source | Narrow support | Still unknown |
|---|---|---|
| [Java SE 25 ExecutorService](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ExecutorService.html) | Submission, shutdown and limits of interruption | Actual library/driver interruption semantics |
| [Java 25 StructuredTaskScope preview](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/StructuredTaskScope.html) | Child lifetime and structured joins | Future API stability or empirical capacity benefit |
| [gRPC Cancellation](https://grpc.io/docs/guides/cancellation/) | Signaling no-longer-needed remote work | Undo of committed external effects |

All examples and intended outcomes are original teaching material. Full source/version/claim review, actual code-level tests and editorial acceptance remain pending.

**Navigation:** target **V03/C01** in [book outline](../../../PROPOSED-STRUCTURE.md), current [execution landing](../../../execution/README.md). Expand to [virtual-thread models](../c02-java-execution-and-virtual-threads/platform-threads-executors-and-virtual-threads.md), [reactive scheduling](../c03-reactive-streams-demand-and-cancellation/reactor-webflux-r2dbc-and-backpressure.md), [CPU and blocking diagnosis](../c06-memory-gc-cpu-and-blocking-diagnostics/cpu-memory-gc-and-blocking-diagnostics.md), [connection pool budgets](../c05-thread-connection-and-buffer-pools/connection-pools-hikaricp-pgbouncer.md).

<!-- /tycho-question-source -->

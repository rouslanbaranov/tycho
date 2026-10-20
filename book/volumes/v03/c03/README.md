---
metadata_version: 1
id: "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03/c03/README.md"
title: "V03/C03 — Reactive streams, demand and cancellation"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do backpressure, scheduling and blocking boundaries affect execution? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do backpressure, scheduling and blocking boundaries affect execution?"
  prerequisites:
    - "tycho.chapter.d5b789c9cd7e4cb693c22943423531c2"
  related_ids:
    - "tycho.page.114da51171c2474ebd56ee3bebad3bcb"
    - "tycho.page.83e414ec3d1b4b07a443de2c96ce2c4e"
    - "tycho.page.0c7b8f00661648f3b50e448471f5cc7e"
    - "tycho.page.577d52b851c3478eb73e301ace1bcfea"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
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

# V03/C03 — Reactive streams, demand and cancellation

## Purpose and mission

How do backpressure, scheduling and blocking boundaries affect execution? This chapter owns that question within execution models, concurrency and flow control. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Trace demand, queues and blocking work across the complete reactive pipeline, including scheduler boundaries.

Subscriber backpressure cannot bound an unrelated blocking queue; an event-loop-friendly API may still hide a bottleneck downstream. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](reactor-webflux-r2dbc-and-backpressure.md) | How do backpressure, scheduling and blocking boundaries affect execution? |
| [Nonblocking execution and demand](demand-blocking.md) | Which demand boundary actually controls a producer and where can blocking escape it? |
| [Schedulers, context and reactive database access](scheduler-context.md) | Which scheduling and context assumptions must hold at a reactive-to-database boundary? |
| [Reactive failure and decision limits](reactive-recovery.md) | What failure or overload observation would reject the proposed reactive design? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V03/C02 — Java execution and virtual threads](../c02/README.md) |
| Next | [V03/C04 — Asynchronous APIs and streaming](../c04/README.md) |
| Prerequisite | [V03/C02 — Java execution and virtual threads](../c02/README.md) |
| Source reading | [Page-local evidence and versions](reactor-webflux-r2dbc-and-backpressure.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.114da51171c2474ebd56ee3bebad3bcb:6 -->
## Evidence ledger

- **[E01] Spring Framework 6.2 official reference:** [WebFlux — Overview](https://docs.spring.io/spring-framework/reference/6.2/web/webflux/new-framework.html), *Define “Reactive”*, *Performance*, *Concurrency Model*, *Invoking a Blocking API*. Supports nonblocking assumptions, backpressure limits and MVC comparison.
- **[E02] Reactor Core 3.7.0 official reference:** [Threading and Schedulers](https://projectreactor.io/docs/core/3.7.0/reference/coreFeatures/schedulers.html), *publishOn*, *subscribeOn*, *boundedElastic*. Supports scheduler behavior, blocking isolation and virtual-thread option.
- **[E03] Reactor Core 3.7.0 official reference:** [Adding a Context to a Reactive Sequence](https://projectreactor.io/docs/core/3.7.0/reference/advancedFeatures/context.html), *Context API*, *Tying a Context to a Flux*, *Reading a Context*. Supports per-subscriber context semantics.
- **[E04] R2DBC SPI 1.0.0.RELEASE specification:** [R2DBC specification](https://r2dbc.io/spec/1.0.0.RELEASE/spec/html/), *Introduction — The R2DBC SPI*, *Compliance — R2DBC SPI Compliance*, *Connections*, *Transactions*. Supports SPI requirements, not a concrete driver's cancellation performance.

**Research status:** inspected the cited published sections and identified untested driver-specific behavior. **Not performed:** compilation, Spring/driver integration, latency measurement, source-code audit, formal backpressure proof or independent human review.

<!-- /tycho-question-source -->

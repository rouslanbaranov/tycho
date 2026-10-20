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
summary: "How do backpressure, scheduling and blocking boundaries affect execution?"
route_hints:
  questions:
    - "How do backpressure, scheduling and blocking boundaries affect execution?"
  prerequisites:
    - "tycho.chapter.d5b789c9cd7e4cb693c22943423531c2"
  related_ids: []
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

| Page | Owning question |
|---|---|
| [Reactive execution, WebFlux, R2DBC and backpressure](reactor-webflux-r2dbc-and-backpressure.md) | How do backpressure, scheduling and blocking boundaries affect execution? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Nonblocking I/O is an end-to-end contract](reactor-webflux-r2dbc-and-backpressure.md#1-nonblocking-io-is-an-end-to-end-contract).
- [2. Reactive Streams is demand coordination, not a magic queue](reactor-webflux-r2dbc-and-backpressure.md#2-reactive-streams-is-demand-coordination-not-a-magic-queue).
- [Engineering walkthrough — Subscriber demand does not protect an unseen blocking queue](reactor-webflux-r2dbc-and-backpressure.md#engineering-walkthrough-subscriber-demand-does-not-protect-an-unseen-blocking-queue).
- [Applied M9 evidence: what transfers and what does not](reactor-webflux-r2dbc-and-backpressure.md#applied-m9-evidence-what-transfers-and-what-does-not).

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

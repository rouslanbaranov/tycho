---
metadata_version: 1
id: "tycho.chapter.e436af815dc442f694deb55966077d9e"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03/c05/README.md"
title: "V03/C05 — Thread, connection and buffer pools"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do pool sizes, queues and timeouts compose across layers?"
route_hints:
  questions:
    - "How do pool sizes, queues and timeouts compose across layers?"
  prerequisites:
    - "tycho.chapter.7a07973ba5314c3983a4c93acc1d1b89"
  related_ids:
    - "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.hikaricp"
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

# V03/C05 — Thread, connection and buffer pools

## Purpose and mission

How do pool sizes, queues and timeouts compose across layers? This chapter owns that question within execution models, concurrency and flow control. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Budget connections, workers and buffers across every replica and intermediary, with bounded waits and timeouts.

Increasing replicas can multiply backend connections beyond the database budget, turning local pool tuning into a shared failure. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Connection pools: HikariCP, PgBouncer and end-to-end database budgets](connection-pools-hikaricp-pgbouncer.md) | How do pool sizes, queues and timeouts compose across layers? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Capacity belongs to the entire dependency topology](connection-pools-hikaricp-pgbouncer.md#1-capacity-belongs-to-the-entire-dependency-topology).
- [2. HikariCP bounds per-process JDBC connection use](connection-pools-hikaricp-pgbouncer.md#2-hikaricp-bounds-per-process-jdbc-connection-use).
- [Engineering walkthrough — Pool capacity is a fleet equation, not a per-replica setting](connection-pools-hikaricp-pgbouncer.md#engineering-walkthrough-pool-capacity-is-a-fleet-equation-not-a-per-replica-setting).
- [Source-to-claim ledger](connection-pools-hikaricp-pgbouncer.md#source-to-claim-ledger).

## Boundaries and further reading

- [V07/C02 — Contention, saturation and scaling laws](../../v07/c02/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V03/C04 — Asynchronous APIs and streaming](../c04/README.md) |
| Next | [V03/C06 — Memory, GC, CPU and blocking diagnostics](../c06/README.md) |
| Prerequisite | [V03/C04 — Asynchronous APIs and streaming](../c04/README.md) |
| Source reading | [Page-local evidence and versions](connection-pools-hikaricp-pgbouncer.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

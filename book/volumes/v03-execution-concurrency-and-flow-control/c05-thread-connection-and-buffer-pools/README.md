---
metadata_version: 1
id: "tycho.chapter.e436af815dc442f694deb55966077d9e"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/README.md"
title: "V03/C05 — Thread, connection and buffer pools"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do pool sizes, queues and timeouts compose across layers? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do pool sizes, queues and timeouts compose across layers?"
  prerequisites:
    - "tycho.chapter.7a07973ba5314c3983a4c93acc1d1b89"
  related_ids:
    - "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.345b19b2f5c1498187048b755b74d876"
    - "tycho.page.ac83eb7361a94d3fb27101cf7666346c"
    - "tycho.page.cbc0f664610b4f73bc0ddc10a22cb50b"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](connection-pools-hikaricp-pgbouncer.md) | How do pool sizes, queues and timeouts compose across layers? |
| [Fleet resource budgets and queueing](fleet-budgets.md) | How do replica count, permits and wait budgets compose across the dependency topology? |
| [HikariCP and PgBouncer contracts](pool-modes.md) | Which session and transaction assumptions distinguish the pool modes? |
| [Pool failure and recovery decisions](pool-recovery.md) | What happens to waiters, prepared state and useful capacity during connection failure? |

## Boundaries and further reading

- [V07/C02 — Contention, saturation and scaling laws](../../v07-performance-scale-and-resilience/c02-contention-saturation-and-scaling-laws/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V03/C04 — Asynchronous APIs and streaming](../c04-asynchronous-apis-and-streaming/README.md) |
| Next | [V03/C06 — Memory, GC, CPU and blocking diagnostics](../c06-memory-gc-cpu-and-blocking-diagnostics/README.md) |
| Prerequisite | [V03/C04 — Asynchronous APIs and streaming](../c04-asynchronous-apis-and-streaming/README.md) |
| Source reading | [Page-local evidence and versions](connection-pools-hikaricp-pgbouncer.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.dc2470904e004a4aa733abcdb25517ed:8 -->
## Source-to-claim ledger

| ID | Primary public reference and inspected scope (2026-10-19) | Supports and limits |
|---|---|---|
| E01 | [HikariCP project README](https://github.com/brettwooldridge/HikariCP), **Configuration: frequently used, maximumPoolSize, minimumIdle, connectionTimeout, maxLifetime**; rolling main documentation at inspection | Documented Java pool settings and their bounded behavior, not a benchmark of the synthetic example |
| E02 | [PgBouncer Configuration](https://www.pgbouncer.org/config), **pool_mode, max_client_conn, default_pool_size** and pooling semantics; rolling public docs observed 2026-10-19 | Session/transaction/statement backend reuse, pool cardinality considerations; actual installed release unpinned |
| E03 | [PostgreSQL 17 Connection Settings](https://www.postgresql.org/docs/17/runtime-config-connection.html), `max_connections` and limits | Server connection limits, not a universal optimal pool size |

**Review state:** conceptual guidance and original arithmetic, no Java Hikari pool test, real PostgreSQL backend measurement, PgBouncer compatibility integration, failover or independent human approval. The current online HikariCP/PgBouncer docs require commit/release pinning before product-specific operational rollout.
<!-- /tycho-question-source -->

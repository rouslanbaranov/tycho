---
metadata_version: 1
id: "tycho.page.dc2470904e004a4aa733abcdb25517ed"
kind: "page"
parent_id: "tycho.chapter.e436af815dc442f694deb55966077d9e"
canonical_path: "book/volumes/v03/c05/connection-pools-hikaricp-pgbouncer.md"
title: "Connection pools: HikariCP, PgBouncer and end-to-end database budgets"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Thread, connection and buffer pools. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do pool sizes, queues and timeouts compose across layers?"
  prerequisites: []
  related_ids:
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.02238832b395417bae63939cd96b9134"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.345b19b2f5c1498187048b755b74d876"
    - "tycho.page.ac83eb7361a94d3fb27101cf7666346c"
    - "tycho.page.cbc0f664610b4f73bc0ddc10a22cb50b"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Connection"
    - "pools"
    - "HikariCP"
    - "PgBouncer"
    - "and"
    - "end-to-end"
    - "database"
    - "budgets"
evidence_scope:
  source_ids:
    - "src.hikaricp"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.dc2470904e004a4aa733abcdb25517ed:-1 -->

# Connection pools: HikariCP, PgBouncer and end-to-end database budgets

> Tycho research chapter for [Issue #84](https://github.com/rouslanbaranov/tycho/issues/84), public docs inspected **2026-10-19**. Main source scopes: HikariCP public README configuration, official PgBouncer configuration and PostgreSQL 17 server connections. Original examples and Mermaid diagrams only; no running connection pool, benchmark or independent expert review.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.dc2470904e004a4aa733abcdb25517ed:0 -->
## Purpose and mission

A connection pool protects finite resources and amortizes connection setup. It is **not** an engine that increases the database's useful query capacity. Larger application request concurrency, virtual threads or reactive task count can increase time waiting for a smaller and fixed connection budget.

**Primary question:** How should a system apportion a fixed database connection budget across instances, reserve headroom, select session/transaction/statement pooling, and test overload without relying on arbitrary universal pool-size advice?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.dc2470904e004a4aa733abcdb25517ed:7 -->
## Engineering walkthrough — Pool capacity is a fleet equation, not a per-replica setting

**Original synthetic budget:** eight application replicas each configure HikariCP maximum 20 connections; PgBouncer mediates 60 server-side database connections. A simplistic calculation of 8×20 = 160 client leases is **not 160 simultaneous database executions**. Transaction-pooling behavior can reuse physical server connections between transactions but has session-state compatibility constraints; a lease held across a long transaction retains scarce capacity.

| Resource | Hypothetical fleet ceiling | Safety observation |
|---|---:|---|
| App JDBC leases | 8×20 = 160 | Waiting client requests and heap still require bounded admission |
| PgBouncer server connections | 60 shared slots | Observed active transactions and wait time, not configured number alone |
| Database heavy write path | Unknown, key- and lock-dependent | Must be measured; neither pool limit equals true throughput |
| Request buffers | E.g. 1,000 queued × 16 KiB = ~15.6 MiB payload only | Objects, TLS, headers and fragmentation add overhead |

If a request holds a leased connection for 400 ms, the idealized service bound at 60 independent leases is at most 150 starts/s under uniform service-time assumptions—**not** a safe p99 guarantee, nor a forecast under lock contention or transaction pooling limitations. Doubling application replicas could increase waiting clients and retry amplification while leaving server DB connections fixed.

**Failure/recovery:** inject a database outage where all 60 slots are unavailable, then recover. A bounded waiting queue, deadline and distinct overload response must prevent unbounded user memory and retry storms. [PgBouncer configuration](https://www.pgbouncer.org/config) distinguishes pooling modes; HikariCP public documentation describes client pool behavior. Proposed comparison of transaction mode vs session mode must audit session-affine features (e.g. temporary state and prepared statements under version/configuration rules). No deployment or benchmark was run.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Budget connections, workers and buffers across every replica and intermediary, with bounded waits and timeouts.

Increasing replicas can multiply backend connections beyond the database budget, turning local pool tuning into a shared failure.

The detailed pages separate the mechanisms that make this decision conditional:

- [Fleet resource budgets and queueing](fleet-budgets.md) — How do replica count, permits and wait budgets compose across the dependency topology?
- [HikariCP and PgBouncer contracts](pool-modes.md) — Which session and transaction assumptions distinguish the pool modes?
- [Pool failure and recovery decisions](pool-recovery.md) — What happens to waiters, prepared state and useful capacity during connection failure?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

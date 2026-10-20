---
metadata_version: 1
id: "tycho.page.cbc0f664610b4f73bc0ddc10a22cb50b"
kind: "page"
parent_id: "tycho.chapter.e436af815dc442f694deb55966077d9e"
canonical_path: "book/volumes/v03/c05/pool-recovery.md"
title: "Pool failure and recovery decisions"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
summary: "What happens to waiters, prepared state and useful capacity during connection failure?"
route_hints:
  questions:
    - "What happens to waiters, prepared state and useful capacity during connection failure?"
  prerequisites:
    - "tycho.page.ac83eb7361a94d3fb27101cf7666346c"
  related_ids:
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "pool"
    - "recovery"
evidence_scope:
  source_ids:
    - "src.hikaricp"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.dc2470904e004a4aa733abcdb25517ed; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Pool failure and recovery decisions

**Owning question:** What happens to waiters, prepared state and useful capacity during connection failure?

This page belongs to [V03/C05 — Thread, connection and buffer pools](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.dc2470904e004a4aa733abcdb25517ed:5 -->
## 5. Failure modes and recovery

| Condition | What the user/operator observes | Evidence and mitigation |
|---|---|---|
| Too many replicas with large independent pools | PostgreSQL connection exhaustion after scaling | Bound total replica×pool count with operating headroom |
| Pool saturated despite idle DB CPU | Waiting clients and timeouts; perhaps long-held sessions | Trace connection hold time, transaction boundaries and pool wait |
| DB already CPU/lock saturated | Larger pools worsen queue, p99 or deadlocks | Stop scaling concurrency; optimize query and admission |
| PgBouncer transaction mode breaks app | Errors or missing session state across requests | Audit driver/session features and run compatibility tests |
| Database failover | Broken/invalid connections, transaction abort, retry storm | Detect invalid connections, jitter/retry budget, idempotent commands |
| Slow connection creation after outage | Recovery lag and thundering herd | Warm pools carefully, cap simultaneous retries/connection attempts |
| Stale or leaked connection | Long-lived wait, resource exhaustion | Leak/timeout instrumentation, closing resources and lifetime limits |

### Cancellation and transaction correctness

Client cancellation can occur after a database has committed. Returning the connection to the pool or throwing a timeout does **not** prove the business operation was undone. Use logical request keys and replay/reconciliation where necessary; see [outbox and idempotency](../../../distributed/transactional-outbox-and-idempotency.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.dc2470904e004a4aa733abcdb25517ed:6 -->
## 6. Design choice procedure

1. Inventory every DB client: services, replicas, async workers, migrations and administrative tools.
2. Define how many backends the actual PostgreSQL configuration safely supports **for this workload** (not merely its hard max).
3. Reserve failure, failover, admin, monitoring and migration headroom.
4. Measure connection acquisition wait, active/idle counts, hold time percentiles, transaction duration, lock waits and resource utilization.
5. Choose per-service `maximumPoolSize` as a bounded share of the aggregate budget; account for peak replica count, not normal replica count.
6. Choose PgBouncer mode only after driver/session/transaction compatibility tests.
7. Under overload, shed or queue with explicit bounded budgets; do not accumulate arbitrary infinite waiting.
8. Test failure recovery and auto-scale spikes, then change settings from evidence.

**Insufficient evidence:** "An API has 30,000 concurrent users, so the JDBC pool should have 30,000 connections." Cannot infer that. Concurrency of logged-in users is not active DB operation count; actual pool budget depends on query/transaction demand, holds, topology, DB service capacity and SLOs.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](pool-modes.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](connection-pools-hikaricp-pgbouncer.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

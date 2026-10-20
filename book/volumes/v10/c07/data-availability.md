---
metadata_version: 1
id: "tycho.page.22b12598c23b4fc5ac74b1adc960ebe5"
kind: "page"
parent_id: "tycho.chapter.5fb14670d0b24967a5e6c24df7221d74"
canonical_path: "book/volumes/v10/c07/data-availability.md"
title: "Data, availability and hard feasibility gates"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Which authoritative-state and recovery assumptions reject an appealing design?"
route_hints:
  questions:
    - "Which authoritative-state and recovery assumptions reject an appealing design?"
  prerequisites:
    - "tycho.page.2eb290f6307f4797a5981510f1248d70"
  related_ids:
    - "tycho.chapter.5fb14670d0b24967a5e6c24df7221d74"
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
    - "tycho.page.aaed70abf79447c89a544eaf84f0da96"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "data"
    - "availability"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Data, availability and hard feasibility gates

**Owning question:** Which authoritative-state and recovery assumptions reject an appealing design?

This page belongs to [V10/C07 — Cross-domain worked comparisons and unresolved cases](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:4 -->
## 4. Third example: a slow query may not need a cache

**Synthetic symptom:** p99 latency increased during evening bursts. One proposal is to add a distributed cache.

Competing hypotheses:
1. Connection pool wait is growing while backend DB CPU is not saturated.
2. One hot aggregate key serializes otherwise cheap writes.
3. The SQL access path changed and scans more data.
4. Retry storm amplifies downstream calls.
5. Read traffic is high and repetitive with a tolerable staleness budget.

A cache addresses only a subset of these causes and can create **invalidated reads, stampedes, credential/data isolation concerns and another failure path**. Measure query traces, actual DB plans, pool waiting, key skew, cacheability, write invalidation and acceptable staleness before selecting.

| Candidate | Helps only if | Falsifying observation |
|---|---|---|
| Tune query/index | Slow plan is measurable and fixable | Plan already optimal; delay elsewhere |
| Right-size pool/timeouts | Pool wait limits actual throughput | Dependency CPU/lock is bottleneck; more connections worsen it |
| Cache selected reads | High repeated reads with bounded staleness and clear invalidation | Low reuse, strict freshness or write-heavy hotspots |
| Shard data | Independent partitions with distributed ownership justified | One hot key dominates; split does not remove serialization |
| Separate read model | Different read projections/workload justify denormalized state | Lag/consistency contract is incompatible |

Read [PostgreSQL query plans](../../../data/postgresql-mvcc-indexes-and-query-plans.md), [cache invalidation](../../../scaling/local-distributed-caching-and-invalidation.md), and [shard hotspots](../../v05/c05/shard-keys-hotspots-and-resharding.md). Correctness and retrieval freshness are first-class criteria, not afterthoughts.

**Decision state:** INSUFFICIENT_EVIDENCE. The next action is instrumenting the suspected boundary with a source-anchored query plan and user-visible latency trace.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:5 -->
## 5. Fourth example: high availability is not a deployment logo

**Synthetic requirement:** an application must continue a limited read journey after a zone loss, with a separate objective for authoritative state restoration after a region loss.

Options include multi-zone pre-provisioned capacity, standby region with replicated state or backup-and-restore. The right choice depends on *different failure classes and RPO/RTO objectives*, role fencing, service access, data correctness and the ability to restore a named user journey.

Two active regions can be inappropriate when they introduce conflicting writes and no reconciled ownership policy. A single region with a practiced restore can outperform a superficially redundant setup against the *specific* required disaster class, if the time/loss targets permit it.

Read [deployment/control-plane](../../v08/c03/runtime-placement-and-control-plane.md), [disaster recovery](../../../deployment/multi-region-disaster-recovery-contracts.md) and [safe rollout](../../../delivery/safe-rollout-and-recovery.md). The correct outcome is not a deployment selection unless actual drills and data reconciliation support it.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:6 -->
## 6. Security and cost are hard gates, not a ranking afterthought

A candidate that violates object authorization, tenant isolation, data restoration or permissions boundaries is not a viable choice even when it appears fastest or easiest to deploy. The [security architecture chapter](../../v09/c05/identity-authorization-and-isolation.md) describes mandatory enforcement and failure checks; a gateway cannot compensate for missing resource-level authorization.

Likewise, evaluate *total operating cost*: components, retention/egress, high-cardinality telemetry, staff skills, on-call load, separate environments, dependency lifecycle, recovery drills and irreversible migration expense. A small deployment count is not a sufficient proxy for lower total ownership cost, and a high RPS figure is not a sufficient reason to introduce distributed state.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](workload-runtime.md) |
| Next | [Continue the reasoning](worked-adr.md) |
| Integrated question | [Original scenario and limits](cross-domain-modernization-and-adr-examples.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

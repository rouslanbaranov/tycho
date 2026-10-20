---
metadata_version: 1
id: "tycho.page.32a5de3daa2d4f74b879165a4119f63a"
kind: "page"
parent_id: "tycho.chapter.b7924b3db65949df952fbb5ca706236c"
canonical_path: "book/volumes/v07/c07/capacity-cost-model.md"
title: "Capacity envelopes and total operating cost"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which correct outcomes and lifecycle costs belong in a capacity comparison?"
route_hints:
  questions:
    - "Which correct outcomes and lifecycle costs belong in a capacity comparison?"
  prerequisites:
    - "tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8"
  related_ids:
    - "tycho.chapter.b7924b3db65949df952fbb5ca706236c"
    - "tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8"
    - "tycho.page.f8f41847ac424c17a5ac3e33fd5b0c6a"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "capacity"
    - "cost"
    - "model"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Capacity envelopes and total operating cost

**Owning question:** Which correct outcomes and lifecycle costs belong in a capacity comparison?

This page belongs to [V07/C07 — Capacity planning and cost/performance trade-offs](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8:1 -->
## 1. Write a capacity envelope, not a magic instance count

A candidate must be checked under at least:

| Load state | Required description | What changes |
|---|---|---|
| Normal | Typical arrival rate, key mix, background jobs and success outcomes | Steady resource footprint, latency and idle cost |
| Predictable peak | Known time and duration, credible scheduled work | Pre-warming, scale schedule, headroom |
| Unexpected burst | Short demand increase with unknown onset | Admission policy, queue age, warm capacity |
| Degraded dependency | Loss or slowness of one necessary or optional service | Retry amplification, fallback, bulkheads |
| Recovery | Backlog catch-up and reconciliation after outage | Extra temporary processing versus user load |
| Growth | More state/data/cardinality, not merely more registered users | Storage, index, rebalancing, data transfer, retention |

A 60-second spike cannot necessarily be served by a replica that takes two minutes to become genuinely ready. Provisioning lag and scale-down stabilization are distinct costs. See [autoscaling lag](../c06/autoscaling-lag-and-capacity-limits.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8:2 -->
## 2. Cost must include more than infrastructure instance prices

Define a review period and consistent cost categories:

- Compute resources, idle headroom, reserved minimum replicas and cold starts.
- Datastore storage, IOPS/queries, replication, backups, restoration and growth.
- Network egress/transfer and cross-region data propagation.
- Queues, cache memory, index builds, search replicas and retained events.
- Logging, metrics, traces, high-cardinality ingestion and data retention.
- CI, test environments, deployment machinery, security reviews and vulnerability handling.
- Operator/on-call skill, incident response, upgrades, backup drills, dependency support.
- Migration effort, temporary double-running, data-copy traffic and irreversibility exposure.

**Operational labor and risk are not made zero by using a managed service.** Managed systems can shift some tasks and price the remaining constraints differently. A low monthly hosting estimate that excludes restorable backups and staffed response cannot be ranked against a fully operated alternative as though they were comparable.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8:3 -->
## 3. Original synthetic comparison

Imagine a public audio-transcript reading application with daily normal demand, a short weekly import surge and a relatively expensive search index. Two invented deployment options exist:

- **A — two warm read replicas**, one shared authoritative data service, bounded optional import workers, simple cache and fixed minimum capacity.
- **B — one warm read replica plus a scale-out policy**, same source authority and index, with new replicas arriving after an assumed startup delay.

The following invented values are **not provider prices**:

| Invented monthly cost component (units) | A | B |
|---|---:|---:|
| Warm application resources | 400 | 210 |
| Extra scale-out resources | 0 | 90 |
| Datastore and replication | 300 | 300 |
| Backup, observability and index | 180 | 180 |
| Platform management and recovery allowance | 100 | 145 |
| **Subtotal excluding migration and risk** | **980** | **925** |

At this simplistic accounting boundary, B is 55 units cheaper, but only if it satisfies the same failure, cold-start and user-journey gates. If B's single warm instance fails during a burst, its scale-up may arrive too late; that violates an availability requirement regardless of cost. A's second warm replica may be required for redundancy, not performance. Both options need a test for shared datastore and index ceilings.

These invented numbers should never be converted to actual currency or used as a procurement estimate without vendor prices, region, usage schedule, resource class and pricing validity.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](capacity-planning-and-cost-performance.md) |
| Next | [Continue the reasoning](sensitivity-options.md) |
| Integrated question | [Original scenario and limits](capacity-planning-and-cost-performance.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

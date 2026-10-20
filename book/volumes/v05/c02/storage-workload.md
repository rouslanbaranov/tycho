---
metadata_version: 1
id: "tycho.page.89cd7853a0d04d78a02a772de59dbf38"
kind: "page"
parent_id: "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
canonical_path: "book/volumes/v05/c02/storage-workload.md"
title: "Workload costs of durable state"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Which write, replication and retention demands constrain storage capacity?"
route_hints:
  questions:
    - "Which write, replication and retention demands constrain storage capacity?"
  prerequisites:
    - "tycho.page.4b98ce4b82bf481b93f2bfce51e882b1"
  related_ids:
    - "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "storage"
    - "workload"
evidence_scope:
  source_ids:
    - "src.postgres17-wal-introduction"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.ddeff7f1556f44f18c67659b73e6e15f; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: "2026-10-20"
content_verified_at: null
---
# Workload costs of durable state

**Owning question:** Which write, replication and retention demands constrain storage capacity?

This page belongs to [V05/C02 — PostgreSQL MVCC, WAL and recovery](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.ddeff7f1556f44f18c67659b73e6e15f:6 -->
## 6. Workload and scale considerations

A physical standby may offload some eligible reads at the cost of freshness and replication resource consumption; it cannot automatically make writes scale out. Index maintenance/WAL volume, long transactions, bulk imports, logical decoding slots, hot tables and checkpoint IO all change performance.

Choosing synchronous replicas affects request tail and failure availability. Choosing async replicas affects acknowledged-write recovery risk. The right configuration follows a **business-approved RPO/RTO**, fault-domain assumptions, load experiments and support capabilities. See the [rollout/recovery chapter](../../../delivery/safe-rollout-and-recovery.md) for source-to-user acceptance distinctions.

**Insufficient evidence:** "We have three copies of PostgreSQL data, so RPO=0, RTO under 30 seconds and no data divergence." No. Need placement, physical/logical mode, sync config, guaranteed/fenced promotion, WAL positions, restore test, integrity and client-level measurements.

<!-- /tycho-question-source -->

## Original workload model — retained log is a recovery budget

Use a fictional change stream that generates ten units of log per second while an archival destination accepts six. During that interval the local archive backlog grows by four units per second. After thirty seconds the additional retained amount is 120 units, before considering any pre-existing backlog. Units are deliberately abstract: they are not bytes per transaction, a PostgreSQL measurement or a sizing recommendation.

If the destination later accepts fourteen units per second while generation remains ten, the backlog drains by four units per second. It therefore needs another thirty seconds to remove that additional backlog, assuming uninterrupted service and no other retention requirement. A healthy-looking average over the entire minute conceals the maximum amount that had to remain available locally.

The architecture question is what happens before that budget is exhausted. Identify which consumers or recovery objectives require the retained history, which failure can pause progress, who observes the backlog and what the permitted degraded action is. Deleting required history, refusing new work and adding storage have different correctness and availability consequences. Do not choose between them from a storage-utilization percentage alone.

The [PostgreSQL 17 WAL introduction](https://www.postgresql.org/docs/17/wal-intro.html) explains log-before-data ordering and recovery from logged changes. It does not establish this fictional generation rate, archive service rate or retention capacity. The arithmetic above is an illustrative queue model; real sizing additionally needs measured log generation, failure duration, recovery membership and the target deployment's actual retention rules.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](replica-recovery.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](postgresql-wal-replication-and-recovery.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

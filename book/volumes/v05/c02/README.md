---
metadata_version: 1
id: "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
kind: "chapter"
parent_id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
canonical_path: "book/volumes/v05/c02/README.md"
title: "V05/C02 — PostgreSQL MVCC, WAL and recovery"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What are the consequences of durability, vacuum and replication mechanisms? The reading route separates 4 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What are the consequences of durability, vacuum and replication mechanisms?"
  prerequisites:
    - "tycho.chapter.f5df10e26e27467887ee2b22b6ce50e7"
  related_ids:
    - "tycho.chapter.388c48be24414421a63481b37d05fdce"
    - "tycho.chapter.30e63461f024419ab87cd012b140c600"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
    - "tycho.page.021b06125a5c46d488493b87d384509f"
    - "tycho.page.82feb39b805a4fbfa80c1b00034b13f6"
    - "tycho.page.4b98ce4b82bf481b93f2bfce51e882b1"
    - "tycho.page.89cd7853a0d04d78a02a772de59dbf38"
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

# V05/C02 — PostgreSQL MVCC, WAL and recovery

## Purpose and mission

What are the consequences of durability, vacuum and replication mechanisms? This chapter owns that question within data models, engines and lifecycle. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Trace acknowledged writes through transaction state, WAL, replication and recovery before assigning a durability promise.

A reachable replica may lag, and a replication setting alone does not establish a successful restore or the application's recovery objective. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](postgresql-wal-replication-and-recovery.md) | What are the consequences of durability, vacuum and replication mechanisms? |
| [MVCC snapshots and the lifetime of row versions](mvcc-snapshots-and-vacuum.md) | Why can an old row version remain necessary after an update commits, and how does that differ from WAL durability? |
| [WAL ordering and acknowledgment](wal-durability.md) | What must be durable when a primary acknowledges a transaction? |
| [Replication and restore boundaries](replica-recovery.md) | How do physical and logical replication differ from recovering a consistent state? |
| [Workload costs of durable state](storage-workload.md) | Which write, replication and retention demands constrain storage capacity? |

## Boundaries and further reading

- [V05/C07 — Replication, backups and restore drills](../c07/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V08/C07 — Multi-region recovery and data reconciliation](../../v08/c07/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V05 — Data models, engines and lifecycle](../README.md) |
| Previous | [V05/C01 — Relational modeling and transaction isolation](../c01/README.md) |
| Next | [V05/C03 — Query planning, indexes and access paths](../c03/README.md) |
| Prerequisite | [V05/C01 — Relational modeling and transaction isolation](../c01/README.md) |
| Source reading | [Page-local evidence and versions](postgresql-wal-replication-and-recovery.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.


## Further mechanism and recovery questions

- [Long transactions, deadlocks and online index work](storage-workload.md#long-transactions-deadlocks-and-online-index-work) — source-scoped enrichment; examples and proposed tests are not executed results.
- [Replica lag, retained WAL and standby feedback](replica-recovery.md#replica-lag-retained-wal-and-standby-feedback) — source-scoped enrichment; examples and proposed tests are not executed results.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.ddeff7f1556f44f18c67659b73e6e15f:8 -->
## Exact public evidence ledger

| ID | PostgreSQL 17 documentation; actual inspected scope | Supports and boundaries |
|---|---|---|
| E01 | [§28.3 WAL introduction](https://www.postgresql.org/docs/17/wal-intro.html), recovery and WAL ordering rationale | WAL supports crash recovery when configured correctly; not inherently zero loss on total-site failure |
| E02 | [§26.2 Log-Shipping Standby Servers](https://www.postgresql.org/docs/17/warm-standby.html), streaming replication, async/synchronous concepts and §26.2.8 | Replica roles, streaming progress and synchronous durability/availability trade-offs |
| E03 | [Chapter 31 Logical Replication](https://www.postgresql.org/docs/17/logical-replication.html), overview/publication and subscription | Logical change propagation; not a physical whole-cluster backup |
| E04 | [Chapter 25 Backup and Restore](https://www.postgresql.org/docs/17/backup.html) and [§25.3 Continuous Archiving](https://www.postgresql.org/docs/17/continuous-archiving.html), broad concepts only | Independently recoverable base backup/WAL artifacts and PITR; no actual restore performed |

**Verification state:** bounded research draft, no PostgreSQL deployment, replication-slot inspection, backup restore, failover or measured RTO/RPO. Mermaid diagrams describe original systems, not operationally proven procedures or independent expert review.
<!-- /tycho-question-source -->

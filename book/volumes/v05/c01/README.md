---
metadata_version: 1
id: "tycho.chapter.f5df10e26e27467887ee2b22b6ce50e7"
kind: "chapter"
parent_id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
canonical_path: "book/volumes/v05/c01/README.md"
title: "V05/C01 — Relational modeling and transaction isolation"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which invariants and anomalies are relevant to the data contract? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which invariants and anomalies are relevant to the data contract?"
  prerequisites:
    - "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
  related_ids:
    - "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
    - "tycho.page.6b42723bd575413bb0d1b94d3e179b6a"
    - "tycho.page.8d8150a14bc04b989fc34432ab7c99e1"
    - "tycho.page.7749abee206c490f97f3ea4ce4dbad8a"
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

# V05/C01 — Relational modeling and transaction isolation

## Purpose and mission

Which invariants and anomalies are relevant to the data contract? This chapter owns that question within data models, engines and lifecycle. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Derive relational constraints and isolation requirements from the anomalies the application must forbid.

Selecting an isolation label without considering transaction retries and constraint placement leaves the invariant unproven. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](relational-modeling-and-transaction-isolation.md) | Which invariants and anomalies are relevant to the data contract? |
| [Relational identities, constraints and snapshots](relational-invariants.md) | Which invariant belongs in the relational model and which anomaly can a snapshot permit? |
| [Isolation anomalies, retries and workload trade-offs](serializable-retry.md) | What does a serializable retry protocol need beyond an isolation setting? |

## Boundaries and further reading

- [V04/C03 — Consistency and distributed transactions](../../v04/c03/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V05 — Data models, engines and lifecycle](../README.md) |
| Previous | [V04/C08 — Stateful/event-time stream processing](../../v04/c08/README.md) |
| Next | [V05/C02 — PostgreSQL MVCC, WAL and recovery](../c02/README.md) |
| Prerequisite | [V04/C03 — Consistency and distributed transactions](../../v04/c03/README.md) |
| Prerequisite | [V04/C04 — Retries, idempotency and duplicate effects](../../v04/c04/README.md) |
| Prerequisite | [V04/C05 — Outbox, inbox, sagas and durable workflows](../../v04/c05/README.md) |
| Source reading | [Page-local evidence and versions](relational-modeling-and-transaction-isolation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.6b42723bd575413bb0d1b94d3e179b6a:7 -->
## 7. Public source ledger and nonclaims

| Primary reference | Narrow support | Still unverified |
|---|---|---|
| [PostgreSQL 17, §5.5 Constraints](https://www.postgresql.org/docs/17/ddl-constraints.html) | PK/FK, unique/check/exclusion constraint types | Exact domain overlap constraint and DDL execution |
| [PostgreSQL 17, §13.1 MVCC](https://www.postgresql.org/docs/17/mvcc-intro.html) | Snapshot visibility and read/write behavior | Benchmark performance or correctness under a real schema |
| [PostgreSQL 17, §8.17 Range Types](https://www.postgresql.org/docs/17/rangetypes.html) | Range boundaries, overlap operator and time interval modeling | Actual tested reservation schema |
| [PostgreSQL 17, Appendix F.8 `btree_gist`](https://www.postgresql.org/docs/17/btree-gist.html) | GiST-equivalent integer equality operators for multicolumn exclusion constraints | Actual installed extension/DDL success |
| [PostgreSQL 17, §13.2 Transaction Isolation](https://www.postgresql.org/docs/17/transaction-iso.html) | Read Committed/Repeatable Read/Serializable, anomaly and retry semantics | Executed isolation test or actual transaction outcome |
| [Tycho earlier combined source](../../../data/postgresql-mvcc-indexes-and-query-plans.md) | Previous version-scoped relational/index discussion | Independent final chapter review |

All domain names, operations, diagrams, failure modes and test plans are fictional. No database, workload generator, observed SQL result, architecture decision or publication-ready metadata has been produced.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.6b42723bd575413bb0d1b94d3e179b6a:8 -->
## Navigation

Proposed owner **V05/C01** in the [planned 10-volume outline](../../../PROPOSED-STRUCTURE.md), [data landing](../../../data/README.md). Related [PostgreSQL indexes and plans](../c03/postgresql-indexes-statistics-and-query-plans.md), [transactions and sagas](../../v04/c03/transaction-isolation-and-sagas.md), [backup/PITR recovery](../c07/backup-restore-pitr-and-recovery-drills.md).
<!-- /tycho-question-source -->

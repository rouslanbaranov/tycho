---
metadata_version: 1
id: "tycho.page.8d8150a14bc04b989fc34432ab7c99e1"
kind: "page"
parent_id: "tycho.chapter.f5df10e26e27467887ee2b22b6ce50e7"
canonical_path: "book/volumes/v05/c01/relational-invariants.md"
title: "Relational identities, constraints and snapshots"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Which invariant belongs in the relational model and which anomaly can a snapshot permit?"
route_hints:
  questions:
    - "Which invariant belongs in the relational model and which anomaly can a snapshot permit?"
  prerequisites:
    - "tycho.page.6b42723bd575413bb0d1b94d3e179b6a"
  related_ids:
    - "tycho.chapter.f5df10e26e27467887ee2b22b6ce50e7"
    - "tycho.page.6b42723bd575413bb0d1b94d3e179b6a"
    - "tycho.page.7749abee206c490f97f3ea4ce4dbad8a"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "relational"
    - "invariants"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.6b42723bd575413bb0d1b94d3e179b6a; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Relational identities, constraints and snapshots

**Owning question:** Which invariant belongs in the relational model and which anomaly can a snapshot permit?

This page belongs to [V05/C01 — Relational modeling and transaction isolation](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.6b42723bd575413bb0d1b94d3e179b6a:1 -->
## 1. Model business identities before tables

**Original fictional example:** a community workshop lends tools by time interval. The important entities are ToolUnit, Member and Reservation. A model name can describe many units; a physical unit has one stable identity and a series of reservation intervals.

A sound model distinguishes:
- immutable unit ID versus mutable display label;
- member identity from authorization to reserve a particular unit;
- one reservation ID and stable logical request ID across retries;
- accepted/cancelled states and their permitted transitions;
- time boundaries (inclusive/exclusive interval semantics and timezone);
- constraints on overlapping accepted intervals;
- ownership and deletion of data, plus retained history.

A foreign key can guarantee that a referenced member/tool identity exists within a chosen DB consistency boundary. It does not independently guarantee that a member is currently authorized to reserve this unit or that two time intervals do not overlap.

[PostgreSQL 17 Constraints, §5.5](https://www.postgresql.org/docs/17/ddl-constraints.html) explains primary keys, unique and foreign-key constraints, checks, and exclusion constraints. Exclusion constraints can support conflicts that cannot be expressed with a simple equality-based unique key; actual interval/index/operator design requires a versioned tested schema.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.6b42723bd575413bb0d1b94d3e179b6a:2 -->
## 2. A snapshot is not an invariant

PostgreSQL uses MVCC (multiversion concurrency control) so readers can observe committed snapshots without treating every concurrent writer as a global reader-blocking lock. [PostgreSQL 17 MVCC Introduction, §13.1](https://www.postgresql.org/docs/17/mvcc-intro.html) describes snapshot visibility and concurrent reads/writes.

This improves concurrency properties but doesn't mean two transactions checking “no overlapping reservation exists” can safely both insert a reservation under an arbitrary isolation mode. A transaction boundary groups operations; its declared isolation rules determine which concurrent observations and updates remain possible.

| Isolation / mechanism | PostgreSQL 17 documented behavior | Decision risk |
|---|---|---|
| Read Committed (default) | Ordinary SELECT gets statement-level committed snapshot; successive queries may see different committed changes | Read-check-write logic can race and must be protected |
| Repeatable Read | Stable snapshot beginning at the first non-transaction-control statement, not necessarily at BEGIN; PostgreSQL disallows phantom reads at this level, but serialization anomalies remain possible | Snapshot stability is not proof of a serializable invariant |
| Serializable | Committed transactions behave as some serial execution if transactions handle serialization failures correctly | Application must retry the complete transaction safely |
| Uniqueness / exclusion constraint | DB enforces the declared key/overlap restriction for relevant writes | Restriction must encode the *actual* domain rule |
| Explicit locks / conditional update | Can coordinate selected rows/keys where appropriate | Locks may be missing for absent rows, cause deadlocks or bottlenecks |

The precise isolation table and retry notes are in [PostgreSQL 17 Transaction Isolation, §13.2](https://www.postgresql.org/docs/17/transaction-iso.html). PostgreSQL maps Read Uncommitted behavior to Read Committed, so do not assume four distinct implemented levels.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](relational-modeling-and-transaction-isolation.md) |
| Next | [Continue the reasoning](serializable-retry.md) |
| Integrated question | [Original scenario and limits](relational-modeling-and-transaction-isolation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

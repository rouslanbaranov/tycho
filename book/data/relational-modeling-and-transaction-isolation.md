# Relational modeling, business constraints and transaction isolation

> **Tycho manuscript — proposed V05/C01**, 2026-10-19. Versioned primary evidence is PostgreSQL 17 chapters 5 and 13. All examples and decision tests are original and fictional, not production data. No PostgreSQL instance was started or tested and no independent technical/editorial acceptance was performed. The previously combined [MVCC and index research](postgresql-mvcc-indexes-and-query-plans.md) remains for source mapping.

## Purpose and mission

A relational model defines identities and integrity, while a transaction isolation contract constrains which concurrent operations can produce a committed state. The schema must encode invariants where the database can enforce them and make explicitly visible which business requirements still need coordinated application logic.

This chapter owns *relational authority and correctness under concurrency*. [Indexes and query access paths](postgresql-indexes-statistics-and-query-plans.md) owns read performance and planner behavior; performance tuning must never silently weaken correctness.

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

## 2. A snapshot is not an invariant

PostgreSQL uses MVCC (multiversion concurrency control) so readers can observe committed snapshots without treating every concurrent writer as a global reader-blocking lock. [PostgreSQL 17 MVCC Introduction, §13.1](https://www.postgresql.org/docs/17/mvcc-intro.html) describes snapshot visibility and concurrent reads/writes.

This improves concurrency properties but doesn't mean two transactions checking “no overlapping reservation exists” can safely both insert a reservation under an arbitrary isolation mode. A transaction boundary groups operations; its declared isolation rules determine which concurrent observations and updates remain possible.

| Isolation / mechanism | PostgreSQL 17 documented behavior | Decision risk |
|---|---|---|
| Read Committed (default) | Ordinary SELECT gets statement-level committed snapshot; successive queries may see different committed changes | Read-check-write logic can race and must be protected |
| Repeatable Read | Stable transaction snapshot; PostgreSQL disallows phantom reads at this level, but serialization anomalies remain possible | Snapshot stability is not proof of a serializable invariant |
| Serializable | Committed transactions behave as some serial execution if transactions handle serialization failures correctly | Application must retry the complete transaction safely |
| Uniqueness / exclusion constraint | DB enforces the declared key/overlap restriction for relevant writes | Restriction must encode the *actual* domain rule |
| Explicit locks / conditional update | Can coordinate selected rows/keys where appropriate | Locks may be missing for absent rows, cause deadlocks or bottlenecks |

The precise isolation table and retry notes are in [PostgreSQL 17 Transaction Isolation, §13.2](https://www.postgresql.org/docs/17/transaction-iso.html). PostgreSQL maps Read Uncommitted behavior to Read Committed, so do not assume four distinct implemented levels.

## 3. A synthetic two-transaction anomaly

Two concurrent clients attempt to reserve the same tool for an overlapping time. Suppose application logic performs “SELECT current reservations; if none, INSERT new reservation,” without a suitable DB-enforced overlap constraint or serializable predicate protection.

```mermaid
sequenceDiagram
    participant A as Transaction A
    participant DB as Database
    participant B as Transaction B
    A->>DB: Read free interval in snapshot A
    B->>DB: Read same free interval in snapshot B
    DB-->>A: No conflicting row
    DB-->>B: No conflicting row
    A->>DB: Insert accepted reservation RA
    B->>DB: Insert accepted reservation RB
    Note over A,B: Without the right invariant guard, both can commit
```

**Text alternative:** separate snapshots can both report an empty interval; subsequent inserts may violate an exclusivity requirement unless the complete business restriction is enforced at a valid transactional authority boundary. This example is a *proposed failure model*, not an executed PostgreSQL trace.

Mitigations depend on actual semantics: use a well-designed exclusion constraint, a serializable transaction with correct retries, or an explicit single-owner conditional state model. Simply introducing a mutex inside one application instance does not protect a deployment with multiple replicas.

## 4. Serializable still needs a retry protocol

PostgreSQL Serializable isolation can abort a transaction with a serialization failure to prevent a non-serializable committed outcome. A correct application should recognize that outcome and, where permitted, **retry the complete transaction from the beginning** with its stable logical operation identity. Blindly replaying external notifications or non-idempotent side effects during transaction retries can multiply effects.

A failed transaction is not an accepted business reservation. A committed transaction whose *network acknowledgment* was lost is a different condition: reconciling that effect requires a durable operation ID and a status query. [Retry semantics](../distributed/retries-idempotency-and-ambiguous-effects.md) owns that distinction.

## 5. Correctness and query performance must be evaluated together

A unique or exclusion constraint may add write/index cost while protecting a mandatory invariant. Removing it to improve throughput is not equivalent to a valid architecture optimization. Adding an index can speed a predicate but does not generally enforce uniqueness/overlap unless the index/constraint is defined for it.

Correctness and performance acceptance should check:
- races from multiple independent callers;
- client retries after lost response;
- schema/state transition constraints;
- actual query plan and lock waits under representative load;
- deadlocks and serialization retries;
- stale replicas and search projections not being used as authoritative write guards;
- full backup/restore of accepted records and referential relationships.

## 6. Architecture alternatives and limits

For a limited self-contained application with an authoritative PostgreSQL store, in-DB constraints and local transactions may be a simpler and stronger choice than moving the reservation decision across services. Another store/consistency model may be appropriate if requirements demand it—but only after comparing which invariants each implementation demonstrably enforces and how it recovers.

A normalized relational schema is not always the optimal storage model for large analytics or document-oriented reads. That separate choice belongs to [data storage alternatives](storage-model-alternatives-and-workload-fit.md), not a presumption that transaction isolation itself picks the entire product architecture.

## 7. Public source ledger and nonclaims

| Primary reference | Narrow support | Still unverified |
|---|---|---|
| [PostgreSQL 17, §5.5 Constraints](https://www.postgresql.org/docs/17/ddl-constraints.html) | PK/FK, unique/check/exclusion constraint types | Exact domain overlap constraint and DDL execution |
| [PostgreSQL 17, §13.1 MVCC](https://www.postgresql.org/docs/17/mvcc-intro.html) | Snapshot visibility and read/write behavior | Benchmark performance or correctness under a real schema |
| [PostgreSQL 17, §13.2 Transaction Isolation](https://www.postgresql.org/docs/17/transaction-iso.html) | Read Committed/Repeatable Read/Serializable, anomaly and retry semantics | Executed isolation test or actual transaction outcome |
| [Tycho earlier combined source](postgresql-mvcc-indexes-and-query-plans.md) | Previous version-scoped relational/index discussion | Independent final chapter review |

All domain names, operations, diagrams, failure modes and test plans are fictional. No database, workload generator, observed SQL result, architecture decision or publication-ready metadata has been produced.

## Navigation

Proposed owner **V05/C01** in the [planned 10-volume outline](../PROPOSED-STRUCTURE.md), [data landing](README.md). Related [PostgreSQL indexes and plans](postgresql-indexes-statistics-and-query-plans.md), [transactions and sagas](../distributed/transaction-isolation-and-sagas.md), [backup/PITR recovery](backup-restore-pitr-and-recovery-drills.md).

---
metadata_version: 1
id: "tycho.landing.984c44f8dbd44d8e89105b4d31787636"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/data/README.md"
title: "Database design, storage engines and recovery"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Reader entry for Database design, storage engines and recovery. Scope includes Reading route; Canonical researched pages; Cross-domain ownership."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Database design, storage engines and recovery?"
  prerequisites: []
  related_ids:
    - "tycho.page.6b42723bd575413bb0d1b94d3e179b6a"
    - "tycho.page.7a136445bbfe4a8194c2c4db8a8818ee"
    - "tycho.page.9176c39f97f544f884666e291ae38b90"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
    - "tycho.page.81efb7e6d72349768b6f202845cbe35e"
    - "tycho.page.357c2d162bd44f3aa06a995a1e691551"
    - "tycho.page.c75a11f9786442a5b5456f11c2412df4"
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.a2c47a0850154eaa95e1eb97e23f9c71"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Database"
    - "design"
    - "storage"
    - "engines"
    - "and"
    - "recovery"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
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

# Database design, storage engines and recovery

> Status: independent-source technical draft chapters, including distinct V05/C01 and V05/C03 owners for [Issue #83](https://github.com/rouslanbaranov/tycho/issues/83), not complete coverage of all databases or a tested operational deployment. Example queries, failure cases and architecture diagrams are fictional and original.

## Purpose and mission

Choose data architecture from business invariants, query access paths, concurrency and durability requirements, not database labels or registered-user counts. Distinguish authoritative transactional state, replica state, event history and derived analytical or graph views.

## Reading route

```mermaid
flowchart LR
    Requirements["Transaction and query requirements"] --> Local["PostgreSQL MVCC / indexes / plans"]
    Local --> Durability["WAL, replication and recovery"]
    Durability --> Alternatives["Embedded, distributed, document, KV, wide-column, OLAP, graph"]
    Alternatives --> Evidence["Representative queries, failures and test evidence"]
```

Text alternative: define actual transaction and query requirements before exploring PostgreSQL's visibility/planner mechanisms, its persistence/replica semantics and specialized engine alternatives. A migration decision still requires workload and recovery evidence.

## Canonical researched pages

| Reader question | Page | Primary evidence |
|---|---|---|
| Which relational identities, constraints and isolation guarantees preserve business invariants? | [Relational modeling and transaction isolation](../volumes/v05/c01/relational-modeling-and-transaction-isolation.md) | V05/C01, PostgreSQL 17 §§5,13, original concurrency counterexample; not executed |
| What governs index selection, planner statistics and estimated-versus-actual query behavior? | [PostgreSQL indexes, statistics and query plans](../volumes/v05/c03/postgresql-indexes-statistics-and-query-plans.md) | V05/C03, PostgreSQL 17 §§11,14, original benchmark/negative cases; no DB run |
| Where is the original combined PostgreSQL MVCC/index research? | [Combined MVCC and query-planning research](postgresql-mvcc-indexes-and-query-plans.md) | Retained historical evidence source pending claim-by-claim reconciliation; no longer sole chapter owner |
| What survives a crash/failover, and how do WAL, replicas and backups differ? | [PostgreSQL WAL, replication and recovery](../volumes/v05/c02/postgresql-wal-replication-and-recovery.md) | PostgreSQL 17 WAL, standby/logical replication and archive recovery |
| How are restorable backup chains, WAL gaps and business-level RPO/RTO proven? | [Backup, PITR and recovery drills](../volumes/v05/c07/backup-restore-pitr-and-recovery-drills.md) | PostgreSQL 17 §§25–26 and original recovery acceptance experiments; no restore performed |
| How can data identity, schema changes, backfill and retirement preserve historical meaning? | [Schema lifecycle and semantic migration](../volumes/v05/c06/schema-lifecycle-and-semantic-migration.md) | V05/C06; independently sourced original data transition draft; no migration executed |
| When are embedded SQL, distributed SQL/KV, document, wide-column, OLAP, graph and time-series storage good candidates? | [Storage model alternatives and workload fit](../volumes/v05/c04/storage-model-alternatives-and-workload-fit.md) | Public official SQLite, CockroachDB v24.3, FoundationDB 8.0, MongoDB, Cassandra 5.0, ClickHouse and Neo4j docs |

## Cross-domain ownership

- [Local isolation and distributed sagas](../volumes/v04/c03/transaction-isolation-and-sagas.md) owns correctness across service boundaries.
- [Transactional outbox and idempotency](../distributed/transactional-outbox-and-idempotency.md) owns asynchronous external event effects.
- [Performance and queueing](../volumes/v07/c01/queueing-littles-law.md) owns rate/concurrency mathematics.
- [Stateful stream processing and CDC](../volumes/v04/c08/stateful-stream-processing-and-cdc.md) owns continuous derived state and replay.
- [Rollout and recovery](../delivery/safe-rollout-and-recovery.md) owns application/schema migration acceptance.

## Open gaps

Measured workloads, DDL evolution with installed drivers, partition/sharding implementation, query planner/optimizer settings, executed backup/restore drills, geographically distributed failure tests and detailed specialized-engine internals require further bounded source/experiment work. This landing does not imply a complete volume or a working database service.

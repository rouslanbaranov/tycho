---
metadata_version: 1
id: "tycho.page.b92e251caf4b47d58bd3101fde058206"
kind: "page"
parent_id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/change-data-capture-cdc.md"
title: "Change Data Capture (CDC)"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Change Data Capture (CDC); all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should database changes be captured as a replayable stream instead of
      dual-written by the application?
  prerequisites:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  related_ids:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "change data capture"
    - "data consistency, transactions and event sourcing"
evidence_scope:
  source_ids:
    - "src.debezium-architecture"
    - "src.debezium-outbox"
    - "src.debezium-postgresql"
    - "src.kafka-connect"
    - "src.kafka-connect-guide"
    - "src.postgres-logical-decoding"
    - "src.postgres-replication-config"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.debezium-architecture.2026-10-31,
    read.debezium-postgresql.2026-10-31,
    read.postgres-logical-decoding.2026-10-31,
    read.postgres-slot-retention.2026-10-31,
    read.kafka-connect-offsets.2026-10-31 and
    read.kafka-connect-overview.2026-10-31; the outbox comparison cites
    read.debezium-outbox-binding.2026-10-31; read.batch8-postgres-logical.2026-10-22
    is retained historical evidence; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Change Data Capture (CDC)

**Identity.** Change Data Capture (CDC); family Data consistency, transactions and event
sourcing; kind data-pattern; priority core.

**Decision question.** Should database changes be captured as a replayable stream instead
of dual-written by the application?

**Good-fit conditions.** The database exposes a logical change stream and a replication
slot can retain the required log; the key identifies the row and keeps its changes on
one partition; transaction metadata is enabled when transaction grouping matters;
schema changes are governed; consumers apply changes idempotently by key and log
position. Debezium's architecture page says its PostgreSQL connector "reads from a
logical replication stream" and streams captured row changes through Kafka Connect.
PostgreSQL defines a logical slot as "a stream of changes that can be replayed to a
client in the order they were made on the origin server." **Tycho conditions:** record
the slot, the key/partition policy, the snapshot position and the idempotency identity.

**Hard contraindications.** Reject when the log is unavailable or unsupported, when
cross-table or global order is required, when the source cannot retain a slot, or when
schema changes cannot be governed. Logical decoding "does not support DDL changes," so
DDL is not in the stream; Debezium also "does not support schema changes while an
incremental snapshot is running." A slot left behind "will prevent removal of required
resources even when there is no connection using them" and can fill storage or be
invalidated by `max_slot_wal_keep_size` or `idle_replication_slot_timeout`.
**Tycho contraindication:** do not assume exactly-once across the database and
downstream; on a fault Debezium can emit duplicate change events and provides
at-least-once delivery.

**Competing alternative.** A transactional outbox plus relay, or scheduled
extraction. Dual-write with reconciliation remains an unbound heuristic. Debezium's
Outbox Event Router says an outbox implementation "avoids inconsistencies between a
service's internal state ... and state in events consumed by services that need the
same data"; its event ID can "remove duplicate messages," and its event key is
"important for maintaining correct order in Kafka partitions." Kafka Connect documents
a source connector that "would import a relational database into Kafka" and a mapping
that "uses a timestamp column to generate queries incrementally returning new data";
that is a scheduled-extraction shape, not a log tail. No bound unit evaluates
dual-write with reconciliation. **Tycho choice rule:** reverse the CDC choice when log
access is unavailable, the source cannot retain a slot, schema changes cannot be
governed, or connector operations exceed the replay benefit.

**Failure and recovery.** Connector lag, slot retention, schema changes and a
snapshot-to-stream gap are common. Debezium exposes `MilliSecondsBehindSource`, the
gap "between the last change event's timestamp and the connector processing it", plus
percentile variants. Its `confirmed_flush_lsn` and `restart_lsn` slot fields bound what
WAL is still available; a slot can be invalidated when `restart_lsn` falls behind
`max_slot_wal_keep_size`. Debezium restarts from the recorded LSN while the slot
remains intact; dropping the slot means "you will lose data", and the removed WAL
cannot be reconstructed. The initial snapshot reads the log position and then streams
from it; if the snapshot fails before completion, "upon restart the connector begins a
new snapshot." **Tycho runbook:** monitor lag and slot health, alert before the
retention limit, test schema changes across the snapshot and streaming paths, and
rebuild from a consistent snapshot rather than assuming the stream is complete.

**Technical owner.** [Change Data Capture (CDC)](../../v04-distributed-coordination-and-events/c08-stateful-event-time-stream-processing/cdc-state.md#change-data-capture-cdc) — CDC replay is bounded, not a full connector operations guide.

**Sources.** Six public units were inspected on 2026-10-31, plus the retained Debezium
Outbox Event Router unit: Debezium *Architecture*; the *Debezium connector for
PostgreSQL*; PostgreSQL 18 *47.2 Logical Decoding Concepts*;
PostgreSQL 18 *19.6 Replication* settings; Kafka Connect 4.1 *Connector Development
Guide*; and Kafka Connect 4.1 *Overview*. Read records:
`read.debezium-architecture.2026-10-31`,
`read.debezium-postgresql.2026-10-31`,
`read.postgres-logical-decoding.2026-10-31`,
`read.postgres-slot-retention.2026-10-31`, `read.kafka-connect-offsets.2026-10-31`
and `read.kafka-connect-overview.2026-10-31`; the retained
`read.debezium-outbox-binding.2026-10-31` supports the outbox comparison. Source ids:
`src.debezium-architecture`, `src.debezium-postgresql`,
`src.postgres-logical-decoding`, `src.postgres-replication-config`,
`src.kafka-connect`, `src.kafka-connect-guide` and `src.debezium-outbox`. The units
are documentation, not benchmarks or production observations.

**Decision state.** applicable-under-conditions.

**Related entries.** Transactional Outbox; Event Sourcing; Materialized View; Command-Side
Replica.

---
metadata_version: 1
id: "tycho.page.82feb39b805a4fbfa80c1b00034b13f6"
kind: "page"
parent_id: "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/c02-postgresql-mvcc-wal-and-recovery/wal-durability.md"
title: "WAL ordering and acknowledgment"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "What must be durable when a primary acknowledges a transaction?"
route_hints:
  questions:
    - "What must be durable when a primary acknowledges a transaction?"
  prerequisites:
    - "tycho.page.021b06125a5c46d488493b87d384509f"
  related_ids:
    - "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
    - "tycho.page.4b98ce4b82bf481b93f2bfce51e882b1"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "wal"
    - "durability"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.ddeff7f1556f44f18c67659b73e6e15f; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# WAL ordering and acknowledgment

**Owning question:** What must be durable when a primary acknowledges a transaction?

This page belongs to [V05/C02 — PostgreSQL MVCC, WAL and recovery](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.ddeff7f1556f44f18c67659b73e6e15f:1 -->
## 1. Why write-ahead logging exists

PostgreSQL 17 §28.3 **Write-Ahead Logging (WAL)** explains the durability approach: record modifications into a log before the affected data pages must be written to their permanent table/index files. WAL records and commit policies permit recovery after a crash without forcing every changed page to disk at transaction commit. WAL is both a recovery mechanism and a foundation for replication approaches. [E01]

```mermaid
flowchart LR
    Client["Client transaction"] --> Buffer["Modified in-memory pages"]
    Buffer --> WAL["Write-ahead log records"]
    WAL --> Commit{"WAL/commit durability settings satisfied?"}
    Commit --> Reply["COMMIT acknowledgement"]
    Buffer --> Flush["Later dirty page write"]
    Flush --> Files[("Table and index files")]
    WAL --> Recovery["Crash replay and recovery"]
    Recovery --> Files
```

Text alternative: transaction changes affect in-memory pages, and corresponding WAL records must meet the configured commit durability policy before acknowledgement. Table/index pages can be flushed later. Following a crash, recovery uses durable WAL to restore a consistent state. This is a conceptual flow; the exact flush ordering is controlled by PostgreSQL internals and configuration.

### Durability has configuration boundaries

`synchronous_commit`, `fsync`, `full_page_writes`, replica availability and storage-level guarantees change what an acknowledged write can survive. A diagram with WAL arrows does **not** guarantee resistance to disk firmware corruption, total-site loss or an incorrectly operated restore.

Avoid saying "transactions use WAL, therefore RPO=0" without specifying the failure (process crash, disk loss, node loss, network partition, region outage) and durable/replicated positions. Under async replication, a primary can acknowledge writes that a standby has not yet received; failing over to that standby may lose the not-yet-replayed or not-yet-received portion. PostgreSQL's §26.2 describes this delay and its implications. [E02]

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.ddeff7f1556f44f18c67659b73e6e15f:3 -->
## 3. Acknowledgments and replication are not one binary switch

PostgreSQL §26.2.8 **Synchronous Replication** documents configurable commit waiting for standby acknowledgment, with trade-offs in lag and availability. It distinguishes the stage at which a standby has written/flushed/applied changes under configured policies. In a topology whose primary waits for one synchronous standby, an unreachable standby may prevent timely commit progress until configuration or availability changes. [E02]

```mermaid
sequenceDiagram
    participant Client
    participant Primary as Primary DB
    participant Standby as Streaming standby
    Client->>Primary: Commit transaction
    Primary->>Primary: Flush local WAL according to configuration
    Primary->>Standby: Stream WAL records
    Standby-->>Primary: Report WAL receive/write/flush/apply progress
    Primary-->>Client: Commit response at configured acknowledgement level
    Note over Client,Standby: Async mode can reply before standby catches up
```

Text alternative: primary sends WAL and receives progress from a standby. Whether the client waits for any standby progress depends on the synchronous replication configuration. This is not proof of a measured replication delay, cross-region RPO or external event commit.

**A replica count is not a durability SLA.** Deployment must account for quorum/ack configuration, data-center placement, network tail, replication slots/retention, failover fencing, split-brain prevention, old primary reintegration and application retry semantics.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](mvcc-snapshots-and-vacuum.md) |
| Next | [Continue the reasoning](replica-recovery.md) |
| Integrated question | [Original scenario and limits](postgresql-wal-replication-and-recovery.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

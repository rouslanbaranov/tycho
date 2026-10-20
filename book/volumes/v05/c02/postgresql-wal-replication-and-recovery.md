---
metadata_version: 1
id: "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
kind: "page"
parent_id: "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
canonical_path: "book/volumes/v05/c02/postgresql-wal-replication-and-recovery.md"
title: "PostgreSQL 17 WAL, physical/logical replication and recovery evidence"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for PostgreSQL MVCC, WAL and recovery. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What are the consequences of durability, vacuum and replication mechanisms?"
  prerequisites: []
  related_ids:
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.021b06125a5c46d488493b87d384509f"
    - "tycho.page.82feb39b805a4fbfa80c1b00034b13f6"
    - "tycho.page.4b98ce4b82bf481b93f2bfce51e882b1"
    - "tycho.page.89cd7853a0d04d78a02a772de59dbf38"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "PostgreSQL"
    - "WAL"
    - "physical/logical"
    - "replication"
    - "and"
    - "recovery"
    - "evidence"
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
<!-- tycho-question-source:tycho.page.ddeff7f1556f44f18c67659b73e6e15f:-1 -->

# PostgreSQL 17 WAL, physical/logical replication and recovery evidence

> Tycho Issue [#83](https://github.com/rouslanbaranov/tycho/issues/83). Version-pinned public source reading: PostgreSQL **17**, on 2026-10-19. Original mechanism explanations and fictional system diagrams, not a live restore drill, benchmark or operational guarantee.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.ddeff7f1556f44f18c67659b73e6e15f:0 -->
## Purpose and mission

Durability and availability depend on **which state has been acknowledged, where it has been persisted, which copies have received it and what was actually restored**. A replica is not automatically a backup. A WAL archive is not automatically a working point-in-time recovery procedure. Local COMMIT, replication acknowledgment and user-visible success must be distinguished.

**Primary question:** How do write-ahead logging, asynchronous/synchronous streaming replication, logical replication and backup/recovery complement one another in PostgreSQL, and what evidence is needed to claim a defined RPO/RTO?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.ddeff7f1556f44f18c67659b73e6e15f:7 -->
## Engineering walkthrough — Primary acknowledgment is not standby completeness

**Original fictional write:** a PostgreSQL 17 primary accepts booking R7, records WAL and acknowledges according to its actual configured durability policy. The asynchronous standby is behind by one WAL interval when the primary becomes unavailable. A failover to that standby can omit R7 even though the original caller saw a success; the precise outcome depends on the acknowledgment, WAL flush/replay and failover configuration.

| Observed evidence | Meaning | Incorrect claim |
|---|---|---|
| Primary commit acknowledged | Local commit durability under chosen setting | Every replica has replayed it |
| Standby received WAL | Data reached standby transport/storage boundary | Business row is queryable or replayed already |
| Standby replay position known | A measurable recovery frontier | All externally committed effects are reconciled |
| New primary promoted | New writable authority if old primary fenced | No historical acknowledged write can be missing |

Physical replication carries low-level state; logical replication has publication/subscription and object/DDL semantics that cannot be equated to one universal backup. If a primary returns with divergent transactions, it cannot safely rejoin as an independent writer. **Recovery:** select a verified timeline, fence the old authority, reconcile accepted operation IDs and delayed consumers, then expose booking reads/writes only after user-level constraints hold.

The existing PostgreSQL 17 WAL, streaming and logical replication sources describe specific mechanisms, not this imagined disaster's RPO. **Proposed, not run:** inject primary loss immediately after acknowledgment and at differing standby replay positions; test data and user outcomes, including PITR to a chosen timeline. If no acknowledged-write loss is permitted, compare suitable synchronous acknowledgment policies and their availability/latency trade-offs instead of advertising async replicas as lossless.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Trace acknowledged writes through transaction state, WAL, replication and recovery before assigning a durability promise.

A reachable replica may lag, and a replication setting alone does not establish a successful restore or the application's recovery objective.

The detailed pages separate the mechanisms that make this decision conditional:

- [MVCC snapshots and the lifetime of row versions](mvcc-snapshots-and-vacuum.md) — Why can an old row version remain necessary after an update commits, and how does that differ from WAL durability?
- [WAL ordering and acknowledgment](wal-durability.md) — What must be durable when a primary acknowledges a transaction?
- [Replication and restore boundaries](replica-recovery.md) — How do physical and logical replication differ from recovering a consistent state?
- [Workload costs of durable state](storage-workload.md) — Which write, replication and retention demands constrain storage capacity?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

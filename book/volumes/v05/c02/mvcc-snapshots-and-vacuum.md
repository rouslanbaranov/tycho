---
metadata_version: 1
id: "tycho.page.021b06125a5c46d488493b87d384509f"
kind: "page"
parent_id: "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
canonical_path: "book/volumes/v05/c02/mvcc-snapshots-and-vacuum.md"
title: "MVCC snapshots and the lifetime of row versions"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Why can an old row version remain necessary after an update commits, and how does that differ from WAL durability?"
route_hints:
  questions:
    - "Why can an old row version remain necessary after an update commits, and how does that differ from WAL durability?"
  prerequisites:
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
  related_ids:
    - "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
    - "tycho.page.82feb39b805a4fbfa80c1b00034b13f6"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "mvcc"
    - "snapshots"
    - "and"
    - "vacuum"
evidence_scope:
  source_ids:
    - "src.postgres17-mvcc-pages"
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
# MVCC snapshots and the lifetime of row versions

**Owning question:** Why can an old row version remain necessary after an update commits, and how does that differ from WAL durability?

This page belongs to [V05/C02 — PostgreSQL MVCC, WAL and recovery](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.


## Visibility is a question about a reader

[PostgreSQL 17 section 13.1](https://www.postgresql.org/docs/17/mvcc-intro.html) describes a multiversion model in which statements observe a snapshot. A committed update therefore does not mean every concurrent reader must immediately interpret the new row version as its own view. Snapshot visibility and durable logging answer different questions: what this reader may observe, versus which changes can be recovered after a crash.

The useful architectural consequence is to identify the reader's observation boundary before describing a result as current. A dashboard query, a long-running report and a transaction enforcing an invariant can require different evidence. Avoid turning the existence of MVCC into a claim that no operation waits for a lock; explicit locks and write conflicts still belong to their own contracts.

## Isolation determines how the view evolves

[Section 13.2](https://www.postgresql.org/docs/17/transaction-iso.html) distinguishes Read Committed statement snapshots from Repeatable Read transaction snapshots. Successive statements at Read Committed can see concurrent committed changes. Repeatable Read retains a stable transaction view but does not itself exclude every serialization anomaly. Serializable transactions add a stronger committed-history guarantee and still require an application retry protocol when a transaction cannot commit.

Consider an original fictional report that reads an item classification, then reads its associated allocations. Another transaction commits between those statements. Decide whether the report permits that mixed observation before choosing isolation or application reconciliation. A stable snapshot can solve an observation problem without proving that two concurrent writers preserve the allocation invariant. The adjacent relational-isolation chapter owns that enforcement question.

## Old versions consume a lifecycle budget

[Section 24.1](https://www.postgresql.org/docs/17/routine-vacuuming.html) explains why updated or deleted versions cannot be removed while another transaction may still need to see them. Vacuuming can make obsolete-version space reusable after it is no longer needed. Ordinary reuse inside a relation is different from immediately shrinking its file on the operating system.

In an invented timeline, reader R begins before writer W commits a changed item. R may still need an earlier version under its snapshot, while a later reader can see the new one. Ending W is therefore not the same event as making every older version reclaimable. Keeping R open indefinitely can extend the relevant retention horizon; the magnitude and operational impact require actual observation, not a universal threshold.

| Question | Evidence needed | Invalid inference |
|---|---|---|
| What may R observe? | Isolation, snapshot and query contract | Latest committed data is automatically every reader's view |
| Can the old version be reused? | Visibility/retention horizon and maintenance progress | Writer commit alone proves the old version can disappear |
| Is a committed write recoverable? | WAL, storage and acknowledgment contract | Snapshot consistency proves crash durability |

## Failure probe and limits

A proposed experiment holds a read transaction open while another session updates the chosen rows. Record the reader's permitted observations, transaction lifetime and maintenance behavior, then end the reader and observe the later state. Do not change isolation, workload and maintenance configuration simultaneously and attribute every difference to one cause.

No PostgreSQL process was executed for this page. The official sections above were textually inspected; the report, row identities and schedule are original educational examples. They do not specify a production tuning value, a recovery objective or measured space growth. This page fills snapshot/version-lifetime explanation; WAL, replication and restore remain separate canonical questions.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](postgresql-wal-replication-and-recovery.md) |
| Next | [Continue the reasoning](wal-durability.md) |
| Integrated question | [Original scenario and limits](postgresql-wal-replication-and-recovery.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

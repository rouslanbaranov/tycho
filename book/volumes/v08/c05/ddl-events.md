---
metadata_version: 1
id: "tycho.page.48d9c34e755c4f7ab912ecad14f5794f"
kind: "page"
parent_id: "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
canonical_path: "book/volumes/v08/c05/ddl-events.md"
title: "DDL budgets and event compatibility"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Which resource and consumer contracts can fail despite a compatible table shape?"
route_hints:
  questions:
    - "Which resource and consumer contracts can fail despite a compatible table shape?"
  prerequisites:
    - "tycho.page.96a702434b714ed4906b1301bc6e0248"
  related_ids:
    - "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
    - "tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb"
    - "tycho.page.d1fa0462922e4a37922cea279975a3bd"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "ddl"
    - "events"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# DDL budgets and event compatibility

**Owning question:** Which resource and consumer contracts can fail despite a compatible table shape?

This page belongs to [V08/C05 — Backward-compatible database change](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb:3 -->
## 3. DDL is part of the runtime resource budget

[PostgreSQL 17 ALTER TABLE](https://www.postgresql.org/docs/17/sql-altertable.html) documents different lock requirements by alteration; absent a weaker stated lock, ACCESS EXCLUSIVE is acquired. A syntactically simple migration can block concurrent work or require a table rewrite depending on its exact form.

Operations like index creation, adding constraints, validating existing records, backfill and large DDL statements consume CPU, I/O, lock time, WAL and replica replay capacity. Their safety requires knowing the PostgreSQL version, table size and workload.

A safe preflight for an exact proposed statement asks:
- what lock mode and potentially blocking duration?
- does the subcommand rewrite a table or block writes?
- how many rows/bytes and what estimated WAL/replica lag?
- are long transactions and connection queues present?
- how will a partially finished job resume or clean up?
- what does failure do to old and new readers?
- how can we stop the migration before the no-return point?

A lock estimate is not a measurement; test with a realistic fixture before promising a zero-downtime change.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb:4 -->
## 4. Event schema compatibility is an additional axis

[Confluent Schema Registry schema evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) distinguishes BACKWARD, FORWARD, FULL and transitive variants, with format-specific rules. It explicitly notes that simple BACKWARD checks cover the previous schema version, not every historical revision.

Even a successful schema registry check is not a guarantee that a domain enum's *meaning* remains compatible. If a new event “Approved” is interpreted as “Pending” by an older consumer, wire parsing might succeed while the user effect fails.

A complete compatibility matrix tests versioned **API, database record, event schema, business status, authorization scope and retention/replay history**. A service may satisfy one transport contract and fail another.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](reader-writer-matrix.md) |
| Next | [Continue the reasoning](no-return-recovery.md) |
| Integrated question | [Original scenario and limits](mixed-version-database-compatibility-and-online-ddl.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

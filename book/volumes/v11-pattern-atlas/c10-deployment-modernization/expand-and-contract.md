---
metadata_version: 1
id: "tycho.page.301477f3c7324fe8932d3a2608516a20"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/expand-and-contract.md"
title: "Expand-and-Contract"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "migration"
summary: >-
  Decision card for Expand-and-Contract; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should a schema change be rolled out in expand, migrate and contract stages?
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "expand and contract"
    - "deployment and legacy modernization"
evidence_scope:
  source_ids:
    - "src.fowler-parallel-change"
    - "src.aws-blue-green-deployments"
    - "src.postgresql"
    - "src.mysql"
    - "src.flyway"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.fowler-parallel-change.2026-10-31,
    read.aws-blue-green-data.2026-10-30,
    read.postgresql-alter-table.2026-10-31,
    read.postgresql-explicit-locking.2026-10-31,
    read.mysql-online-ddl.2026-10-31,
    read.mysql-alter-table.2026-10-31 and the retained
    read.batch3-flyway.2026-10-21 record; owner section and limits are bounded.
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
# Expand-and-Contract

**Identity.** Expand-and-Contract; family Deployment and legacy modernization; kind
migration-pattern; priority core.

**Decision question.** Should a schema change be rolled out in expand, migrate and
contract stages?

**Good-fit conditions.** Old and new readers coexist; each phase is additive and
backward compatible; the compatibility window and reader inventory are owned; the
backfill, validation and cutover gate are explicit; the engine's DDL lock or rewrite
budget is known; a rollback or forward-repair path is defined.

**Hard contraindications.** Reject when old and new readers cannot coexist, when the
change requires an immediate destructive rewrite with no compatibility window, when a
rollback cannot restore the old schema and data, or when no one owns the reader
inventory.

**Competing alternative.** Big-bang migration, parallel run, explicit API versioning,
branch by abstraction, or engine-native online DDL for a single compatible change.
Fowler presents parallel change as an alternative to explicit versioning and calls
branch by abstraction better for a large client population. MySQL instant and in-place
DDL avoids a table copy for compatible changes, but a type change is COPY-only and
blocks concurrent DML. Reverse when no compatibility window is possible, the dataset is
small enough to pause, or the engine can complete the change online.

**Failure and recovery.** Partial backfills, old readers and destructive rewrites are
common; hold the window, repair forward, and contract only after reader absence. AWS
warns that deletive changes can make the earlier version non-operational; PostgreSQL
rewrites are not MVCC-safe; MySQL limits instant column versions and falls back to
COPY/INPLACE.

**Technical owner.** [Expand-and-Contract](../../v08-delivery-deployment-and-recovery/c05-backward-compatible-database-change/reader-writer-matrix.md#expand-and-contract) — expand/contract is bounded to reader/writer compatibility.

**Sources.** [src.fowler-parallel-change](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.fowler-parallel-change.2026-10-31`: Danilo Sato, "Parallel Change,"
published 2014-05-13; canonical text SHA-256
`af2cd77b9048f39fdee984b371305ecc362f236d485a21ff02008a65787dfed7`.
[src.aws-blue-green-deployments](../../../../edition/patterns/reading-ledger.v1.json)
retained record `read.aws-blue-green-data.2026-10-30`: "Best Practices for Managing
Data Synchronization and Schema Changes", historical reference.
[src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
records `read.postgresql-alter-table.2026-10-31` and
`read.postgresql-explicit-locking.2026-10-31`: PostgreSQL 18.6 "ALTER TABLE" and
"Explicit Locking", canonical text SHA-256
`2f8630304b6159e52681a0d9502a1d09b497da7ffb8918b86c0ebf4d76003924` and
`defdd38bf3d5aeaa3174012e51c6e02c56cb76e1153fc21da8c5ffcb42646e23`.
[src.mysql](../../../../edition/patterns/reading-ledger.v1.json) records
`read.mysql-online-ddl.2026-10-31` and `read.mysql-alter-table.2026-10-31`:
MySQL 8.4 Reference Manual "Online DDL Operations" and "ALTER TABLE", canonical text
SHA-256 `6f7b0113f99388ab4a29f9016a05fedb46b86277174162fe4bc5cbca295de3de` and
`d47cb8ed8933e515b8ec2771583aeea9916741840eb45704c2a5235a9c5d92f2`. The retained
[src.flyway](../../../../edition/patterns/reading-ledger.v1.json) record
`read.batch3-flyway.2026-10-21` remains tooling context, not phase evidence.
The sources are public documentation and articles, not benchmarks;
Tycho-labelled rules are synthesis.

**Decision state.** applicable-under-conditions.

**Related entries.** Online Data Migration; Controlled Cutover; Reader/Writer
Compatibility; Backup/PITR.

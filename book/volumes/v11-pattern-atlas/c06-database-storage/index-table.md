---
metadata_version: 1
id: "tycho.page.41daaaaf1b34f0d26e3346804ac0e85e"
kind: "page"
parent_id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/index-table.md"
title: "Index Table"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Index Table; all four dimensions source-bound; coverage
  remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should a separate lookup table maintain a secondary access path?
  prerequisites:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  related_ids:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "index table"
    - "database and storage architecture"
evidence_scope:
  source_ids:
    - "src.postgresql"
    - "src.microsoft-sql-server"
    - "src.use-the-index-luke"
    - "src.aws-dynamodb-gsi"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.pg17-index-only-scans.2026-10-31,
    read.microsoft-included-columns.2026-10-31,
    read.luke-index-only-scan.2026-10-31 and
    read.aws-dynamodb-gsi-overloading.2026-10-31; retained
    read.batch3-pg-indexes.2026-10-21; owner section and limits are bounded.
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
# Index Table

**Identity.** Index Table; family Database and storage architecture; kind
data-structure-pattern; priority core.

**Decision question.** Should a separate lookup table maintain a secondary access path?

**Good-fit conditions.** The access path is stable and frequent; the write path can
maintain the lookup and repair drift; the base row stays authoritative; maintenance
and write cost are acceptable against the scan or drift cost removed.

**Hard contraindications.** Reject when a native covering index, materialized view,
query-time join or overloaded managed secondary index already serves the path; when
dual-write consistency cannot be maintained; when payload columns would become a
second key; or when the lookup is rarely used.

**Competing alternative.** Native covering index (PostgreSQL INCLUDE or SQL Server
included columns), materialized view, query-time join, or an overloaded DynamoDB
GSI. Reverse the choice when index maintenance and drift exceed lookup benefit, or
when one managed index can serve many query shapes.

**Failure and recovery.** A covering path fails quietly when its shape changes:
Luke shows that adding a filter "can cause “illogical” performance behavior" and
that "The table access increases the response time although the query selects fewer
rows". PostgreSQL requires visibility-map bits; otherwise "the heap entry must be
visited" and no advantage is gained. SQL Server warns that wide included columns add
update cost and that nonkey columns "can't be dropped from a table unless that
table's index is dropped first". Tycho guidance: reconcile stale or duplicate lookup
rows with a repair job, keep the key immutable, bound rebuild time and re-check the
plan after query changes.

**Technical owner.** [Index Table](../../v05-data-models-engines-and-lifecycle/c03-query-planning-indexes-and-access-paths/plan-lifecycle.md#index-table) — index lifecycle is bounded, not a full access-path catalogue.

**Sources.** The owner section binds four 2026-10-31 units:
[src.postgresql](../../../../edition/patterns/reading-ledger.v1.json) record
read.pg17-index-only-scans.2026-10-31 (*11.9. Index-Only Scans and Covering
Indexes*);
[src.microsoft-sql-server](../../../../edition/patterns/reading-ledger.v1.json)
record read.microsoft-included-columns.2026-10-31 (*Create indexes with
included columns*);
[src.use-the-index-luke](../../../../edition/patterns/reading-ledger.v1.json)
record read.luke-index-only-scan.2026-10-31 (*Index-Only Scan: Avoiding Table
Access*);
[src.aws-dynamodb-gsi](../../../../edition/patterns/reading-ledger.v1.json)
record read.aws-dynamodb-gsi-overloading.2026-10-31 (*Overloading Global
Secondary Indexes in DynamoDB*). The retained citation
read.batch3-pg-indexes.2026-10-21 covers the PostgreSQL 11 chapter, not the new
bounded units. Canonical text revisions are bound in the owner page. Public
documentation and a practitioner book site, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Partitioning; Materialized View; CQRS Read Projections; Sharding.

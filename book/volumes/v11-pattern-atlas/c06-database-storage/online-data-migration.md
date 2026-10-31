---
metadata_version: 1
id: "tycho.page.480477bf68a84b33b01440df8a0ccc96"
kind: "page"
parent_id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/online-data-migration.md"
title: "Online Data Migration"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Online Data Migration; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should data be backfilled while the system continues serving reads and
      writes?
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
    - "online data migration"
    - "database and storage architecture"
evidence_scope:
  source_ids:
    - "src.aws-dms"
    - "src.flyway-expand-contract"
    - "src.gh-ost"
    - "src.m9-st01"
    - "src.postgresql"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.stripe-online-migrations.2026-10-31,
    read.postgres-pgdump.2026-10-31, read.postgres-copy.2026-10-31,
    read.aws-dms-overview.2026-10-31, read.aws-dms-cdc.2026-10-31 and
    read.flyway-expand-contract.2026-10-31; read.batch3-gh-ost.2026-10-21 is
    retained historical mechanism context; owner section and limits are bounded.
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
# Online Data Migration

**Identity.** Online Data Migration; family Database and storage architecture; kind
migration-pattern; priority core.

**Decision question.** Should data be backfilled while the system continues serving reads
and writes?

**Good-fit conditions.** Writes continue during migration; one authoritative writer or a
reconciled second write is owned; change capture and a checkpoint are operable; validation
and cutover are gated. Stripe's "4 step dual writing pattern" dual-writes to old and new
tables, then moves reads and writes before removing the old store. **Tycho conditions:**
record the mapping revision, checkpoint, replay window and reconciliation rule.

**Hard contraindications.** Reject when a maintenance window is acceptable, when no
reconciliation path exists, or when the changed-row set is small enough for a quiesced
migration. PostgreSQL `COPY FROM` inserts rows "as it progresses"; a failed command leaves
them "in a deleted state", invisible until vacuum and still occupying space.

**Competing alternative.** A stop-the-world export/restore (`pg_dump` plus `COPY`; Tycho
shape). Online implementation options include Flyway expand/contract, AWS DMS full-load plus
CDC and dual-write. Reverse the stop-the-world choice when online complexity exceeds
downtime cost. Flyway's guidance says to "add new columns nullable,
dual-write, backfill, switch reads, then drop" so a partial rollout "keeps working".

**Failure and recovery.** Checkpoint lag, changed mappings and cutover ambiguity are risks;
changed mapping and cutover are Tycho, untested concerns.
AWS DMS caches a checkpoint "from time to time" and can "recover a failed migration task"
from it; a resume still needs a replay window and duplicate-tolerant apply. Verify coverage
and acceptance status in the owner section; no owner acceptance is claimed.

**Technical owner.** [Online Data Migration](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/migration-retirement.md#online-data-migration) — backfill acceptance is bounded, not an online migration tool guide.

**Sources.** Six public pages were inspected on 2026-10-31: Stripe *Online migrations at
scale*; PostgreSQL 18.6 *pg_dump* and *COPY*; AWS DMS *What is AWS Database Migration
Service?* and *Creating tasks for ongoing replication using AWS DMS*; and Flyway *Rolling
out updates from a single schema to multiple production databases* (expand/contract
guidance). Read records: `read.stripe-online-migrations.2026-10-31`,
`read.postgres-pgdump.2026-10-31`, `read.postgres-copy.2026-10-31`,
`read.aws-dms-overview.2026-10-31`, `read.aws-dms-cdc.2026-10-31` and
`read.flyway-expand-contract.2026-10-31`. Source ids: `src.m9-st01`, `src.postgresql`,
`src.aws-dms`, `src.flyway-expand-contract` and the retained `src.gh-ost` (historical
mechanism context). The units are documentation or an engineering article, not benchmarks
or production observations.

**Decision state.** applicable-under-conditions.

**Related entries.** Expand-and-Contract Schema; Sharding; CDC; Backup/PITR.

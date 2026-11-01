---
metadata_version: 1
id: "tycho.page.1daaed0aff5964fb0e79ca3397b8e5b8"
kind: "page"
parent_id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/backup-pitr-and-restore.md"
title: "Backup, PITR and Restore"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Backup, PITR and Restore; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should recovery rely on base backups plus point-in-time WAL/log replay?
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
    - "backup"
    - "point-in-time recovery"
    - "database and storage architecture"
evidence_scope:
  source_ids:
    - "src.postgresql"
    - "src.aws-backup"
    - "src.azure-backup"
    - "src.sre"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.pg-pitr.2026-10-31, read.aws-backup.2026-10-31,
    read.aws-backup-restore-testing.2026-10-31, read.azure-backup.2026-10-31
    and read.sre-data-integrity.2026-10-31; retained
    read.batch3-pg-archiving.2026-10-21; owner section and limits are bounded.
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
# Backup, PITR and Restore

**Identity.** Backup, PITR and Restore; family Database and storage architecture; kind
recovery-pattern; priority core.

**Decision question.** Should recovery rely on base backups plus point-in-time WAL/log
replay?

**Good-fit conditions.** A base backup and a continuous archive are both retained; the chain,
recovery target, encryption keys and retention are owned; restore drills are scheduled; and
the target can be validated with business invariants. PostgreSQL says "you need a continuous
sequence of archived WAL files that extends back at least as far as the start time of your
backup." These are Tycho conditions.

**Hard contraindications.** Reject when the archive has gaps, when retention cannot cover the
detection window, when no restore has been tested, or when RPO/RTO cannot be measured. Also
reject a replica-only plan for accidental deletion or corruption. **Tycho contraindication.**

**Competing alternative.** Replica failover. Google SRE says
replication "can’t protect you from many sources of data loss" and that "a corrupt database
row or errant delete are pushed to all of your copies". Azure Backup separates "data
protection (backup and restore)" from "disaster recovery and failover orchestration".
**Tycho choice rule:** use a replica for availability and a backup/PITR chain for historical
state; reverse when availability, not restoration of a prior point, is the objective.

**Failure and recovery.** Untested restores are unproven; corrupt backups can halt
recovery. PostgreSQL warns that "If recovery finds corrupted WAL data, recovery will halt at
that point and the server will not start"; a missing or inaccessible archive bounds the
reachable point. AWS Backup restore testing "provides automated and periodic evaluation of
restore viability"; Google SRE says "you only know that you can recover your recent state if
you actually do so". **Tycho runbook:** restore into an isolated target, verify checksums,
chain and business invariants, record the achieved point and gap, and keep the old writer fenced.

**Technical owner.** [Backup, restore and recovery drills: proving data recoverability](../../v05-data-models-engines-and-lifecycle/c07-replication-backups-and-restore-drills/backup-restore-pitr-and-recovery-drills.md#backup-pitr-and-restore)
— backup/restore is bounded, not a universal RPO/RTO model.

**Sources.** Five public units inspected on 2026-10-31: PostgreSQL 17 *Continuous Archiving
and Point-in-Time Recovery (PITR)*; AWS Backup *What is AWS Backup?* and *Restore testing*;
Azure Backup *What is the Azure Backup service?*; and Google SRE *Data Integrity: What You
Read Is What You Wrote*. Retained: `read.batch3-pg-archiving.2026-10-21`;
new records: `read.pg-pitr.2026-10-31`, `read.aws-backup.2026-10-31`,
`read.aws-backup-restore-testing.2026-10-31`,
`read.azure-backup.2026-10-31` and `read.sre-data-integrity.2026-10-31`. Source ids:
`src.postgresql`, `src.sre`, `src.aws-backup` and `src.azure-backup` are registered.
Canonical text SHA-256 `3aeddd67...`, `edbc0b59...`,
`8a0be467...`, `628a6734...` and `8afec387...`. Exact URLs, sections and revisions are in the
owner section; section-level evidence is in the owner-unit record. AWS immutability/soft
delete and Azure cross-Region are out of scope for this partial-bounded check. None is a
benchmark or production observation; no database, backup or restore was run.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Read Replicas; Expand-and-Contract;
Disaster Recovery.

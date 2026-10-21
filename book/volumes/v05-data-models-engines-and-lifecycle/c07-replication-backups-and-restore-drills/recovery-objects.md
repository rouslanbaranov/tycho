---
metadata_version: 1
id: "tycho.page.8ff8bad016ba4b92ba968c18a9210020"
kind: "page"
parent_id: "tycho.chapter.388c48be24414421a63481b37d05fdce"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/c07-replication-backups-and-restore-drills/recovery-objects.md"
title: "Recovery objectives, backup types and WAL continuity"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Which backup membership and replay chain can recover the declared failure?"
route_hints:
  questions:
    - "Which backup membership and replay chain can recover the declared failure?"
  prerequisites:
    - "tycho.page.81efb7e6d72349768b6f202845cbe35e"
  related_ids:
    - "tycho.chapter.388c48be24414421a63481b37d05fdce"
    - "tycho.page.81efb7e6d72349768b6f202845cbe35e"
    - "tycho.page.60ffc845d47c44cba4af2760474d68c7"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "recovery"
    - "objects"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.81efb7e6d72349768b6f202845cbe35e; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Recovery objectives, backup types and WAL continuity

**Owning question:** Which backup membership and replay chain can recover the declared failure?

This page belongs to [V05/C07 — Replication, backups and restore drills](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.81efb7e6d72349768b6f202845cbe35e:1 -->
## 1. Recovery objectives have a named failure and clock

- **RPO (recovery point objective):** maximum acceptable loss of acknowledged business state, defined for a specified failure and measurement basis.
- **RTO (recovery time objective):** allowed time from a defined disruption/start marker until a tested user journey is restored, not just until a database process starts.
- **Integrity invariant:** what committed data and relationships must remain internally consistent after restore.
- **Reconciliation contract:** how operations accepted after the restored point are identified, replayed, rejected or recovered from other independent evidence.
- **Recovery authority:** who can authorize destructive restore, cutover, temporary read-only mode, and reopening writes.

RPO/RTO values are **requirements or observed drill results**, not inherent database settings. A page saying “RPO = zero” must specify the modeled failure class and commit acknowledgment boundary; an asynchronously replicated system cannot simply assume no data loss on primary loss.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.81efb7e6d72349768b6f202845cbe35e:2 -->
## 2. Logical backup, physical backup and WAL replay differ

The [PostgreSQL 17 Backup and Restore guide](https://www.postgresql.org/docs/17/backup.html) distinguishes SQL dumps, file-system-level backup, and continuous archiving. The [PostgreSQL 17 continuous archiving/PITR section](https://www.postgresql.org/docs/17/continuous-archiving.html) explains how a valid base backup plus a continuous suitable WAL sequence supports point-in-time recovery; logical dumps are **not** physical base backups usable for WAL replay.

| Method | Useful when | Recovery limitation |
|---|---|---|
| Logical SQL dump | Portable export/import within supported format/version limits; selected objects | Import time; transaction/version/extensions and role/permission compatibility; not WAL-base PITR |
| Physical cluster backup | Reconstruct a compatible database cluster | Correct base backup contents, ownership, tablespaces and version compatibility needed |
| Physical backup + WAL archive | Restore to permitted point after base backup under continuous WAL coverage | Missing/corrupted segments, archive lag, storage and replay time |
| Streaming replica | Reduce outage for some instance/host failures | May mirror corruption/deletion; replica promotion/fencing and lag matter |
| Application-level export or journal | Recover particular business entities/effects | Must prove completeness, identity, ordering, privacy and reconciliation |

Do not call synchronous replication, standby promotion and PITR interchangeable. They differ on what they protect, which failure they survive and what state can be reconstructed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.81efb7e6d72349768b6f202845cbe35e:4 -->
## 4. WAL gaps, timelines and version dependencies

PostgreSQL 17 documentation describes WAL archive segments, recovery targets, timeline histories, base backup requirements, and how incremental base backups depend on prior backups and WAL summaries. It notes that archive lag can increase potential data loss and create local WAL-disk pressure; configuration files are not automatically protected by WAL replay.

For a recoverability contract record:
- database major version, supported tooling/extension and archive/backup formats;
- source cluster/system ID, base-backup manifest and hash or verification evidence;
- tablespaces, external files, config, secrets and network/identity requirements;
- WAL sequence and archive completeness, timeline history and recovery stop point;
- incremental backup ancestry, which earlier backups cannot be deleted safely;
- restore location, target disk size, network/archive throughput and access permissions;
- expected replay duration and whether recent unarchived WAL is accessible;
- permitted return to service and which clients need revalidation after state rewind.

A restore target before the completion of the selected base backup is not automatically available using that base backup. Timeline and archive retention must permit the actual desired point. The PostgreSQL docs explain these constraints; only a **rehearsed restore of an admitted backup set** can show that the local implementation meets them.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](backup-restore-pitr-and-recovery-drills.md) |
| Next | [Continue the reasoning](restore-drills.md) |
| Integrated question | [Original scenario and limits](backup-restore-pitr-and-recovery-drills.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

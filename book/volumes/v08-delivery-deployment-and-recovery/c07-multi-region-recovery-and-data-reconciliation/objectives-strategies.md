---
metadata_version: 1
id: "tycho.page.4b654b81026f4d8b8909563bcffc01e4"
kind: "page"
parent_id: "tycho.chapter.30e63461f024419ab87cd012b140c600"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/objectives-strategies.md"
title: "Recovery clocks, historical state and alternatives"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Which failure and data-loss contract distinguishes recovery strategies?"
route_hints:
  questions:
    - "Which failure and data-loss contract distinguishes recovery strategies?"
  prerequisites:
    - "tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765"
  related_ids:
    - "tycho.chapter.30e63461f024419ab87cd012b140c600"
    - "tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765"
    - "tycho.page.aeedcc93ea554edc9059b8f9ddefa292"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "objectives"
    - "strategies"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Recovery clocks, historical state and alternatives

**Owning question:** Which failure and data-loss contract distinguishes recovery strategies?

This page belongs to [V08/C07 — Multi-region recovery and data reconciliation](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765:1 -->
## 1. Define objectives by meaningful clocks and outcomes

- **RTO:** the permitted interval from a named disruption/impact start marker until a specified user journey returns *correct usable service*. Starting the clock after human detection hides part of the outage.
- **RPO:** the permitted age/loss of committed business state for a named failure class, at the chosen acknowledgment boundary.
- **Integrity gate:** what user-visible invariants must hold after recovery (e.g., one accepted allocation for one exclusive tool/time interval).
- **Recovery authority:** who may promote state, fence the old writer, cut traffic and authorize restored operations.
- **Evidence record:** what exact drill revision, event chronology, source data snapshot and observed results support the RTO/RPO claim.

These are *requirements* until an appropriate drill measures outcomes. An intended RPO=0 is not evidence the implementation can acknowledge writes with no possible loss under the declared region failure.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765:2 -->
## 2. Replication is not historical recovery

Consider three distinct incidents:
1. **One instance lost:** another valid replica may take over with correct membership/fencing.
2. **Entire region lost:** recover in an independent failure domain, maybe from replicas or retained backups depending on actual loss.
3. **Bad deletion or data corruption:** live replicas may faithfully copy the bad transaction; a historical restore point and business-effect reconciliation are needed.

The [PostgreSQL 17 PITR documentation](https://www.postgresql.org/docs/17/continuous-archiving.html) describes base backups plus appropriate WAL coverage and warns that archive lag increases data-loss risk. Merely storing periodic SQL dumps is not equivalent to physical base backup plus WAL replay.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765:4 -->
## 4. Strategy alternatives have different costs and risks

| Strategy | Potential benefit | Needed proof |
|---|---|---|
| Backup and restore | Economical protected historical state where delay is acceptable | Accessible valid backups, keys/config, data integrity, actual restoration time |
| Pilot-light minimal recovery | Some minimal components/state are prepared | Cold capacity and dependent services become ready within required time |
| Warm standby | Faster restore than fully cold provision for some cases | Replica lag, cutover/fencing, sufficient warm capacity |
| Active/active | Both locations may serve useful work concurrently | Cross-region authority/consistency, conflict handling and higher cost |

The [Well-Architected DR strategies](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_disaster_recovery.html) describe these families and implementation constraints, not numerical promises for this fictional system. A supposedly active/active design that independently allocates the same exclusive resource in two disconnected regions may violate correctness, even though both regions serve requests.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](disaster-recovery-and-recovery-objectives.md) |
| Next | [Continue the reasoning](authority-failback.md) |
| Integrated question | [Original scenario and limits](disaster-recovery-and-recovery-objectives.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

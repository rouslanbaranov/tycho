---
metadata_version: 1
id: "tycho.page.36bfc8635514db33025afd706a6b4c85"
kind: "page"
parent_id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/failover-failback.md"
title: "Failover / Failback"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: >-
  Decision card for Failover / Failback; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should traffic move to a standby and later return to the original
      authority?
  prerequisites:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  related_ids:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "failover"
    - "resilience"
evidence_scope:
  source_ids:
    - "src.postgresql"
    - "src.sre"
    - "src.aws-route53"
    - "src.azure-site-recovery"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.pg-failover.2026-10-31, read.aws-route53-failover.2026-10-31,
    read.azure-asr-failover.2026-10-31, read.azure-asr-failback.2026-10-31 and
    read.sre-testing-disaster.2026-10-31; retained
    read.batch3-pg-warm.2026-10-21; owner section and limits are bounded.
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
# Failover / Failback

**Identity.** Failover / Failback; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should traffic move to a standby and later return to the original
authority?

**Good-fit conditions.** A standby exists; promotion is fenced; data reconciliation is
owned; failback is planned as a new migration, not a DNS switch. PostgreSQL defines
failover as starting standby procedures and promotion through `pg_ctl promote` or
`pg_promote()`; Azure Site Recovery requires reprotection and a complete synchronization
before failback. **Tycho conditions:** an authority epoch, a reconciliation owner and a
verified user journey are prerequisites.

**Hard contraindications.** Reject when no standby is maintained, when split brain cannot
be fenced, or when failback would lose writes. Also reject a DNS-only return while the old
authority can still accept writes. Route 53's active-passive choice follows health status;
health does not prove data authority. **Tycho contraindication.**

**Competing alternative.** Restore from backup or stay on the promoted primary. PostgreSQL
says "To return to normal operation, a standby server must be recreated, either on the
former primary system when it comes up, or on a third, possibly new, system"; Azure Site
Recovery reprotects the failed-over region before returning traffic. **Tycho choice rule:**
stay on the promoted region and rebuild the old region as a standby when fencing or
reconciliation evidence is incomplete; reverse only when the old region can be proven
consistent.

**Failure and recovery.** Split brain and lost writes are common; quarantine the old
authority, reconcile before failback, and hold writes when fencing evidence is missing.
PostgreSQL warns that two primaries lead to "confusion and ultimately data loss"; Azure
Site Recovery warns "If the source VM is powered on then it fails and thus fails the
failback operation." Route 53 health checks route to a healthy record, not to a reconciled
authority. Google SRE says disaster recovery tools compute a "checkpoint state that is
equivalent to cleanly stopping the service" and that broken constraints make confidence
harder. **Tycho runbook:** fence, reconcile, verify a user journey and record the achieved
RPO/RTO before declaring recovery.

**Technical owner.** [Failover / Failback](../../v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/authority-failback.md#failover-failback) — failover/failback is bounded to recovery state machines.

**Sources.** Five public units inspected on 2026-10-31: AWS Route 53 *Active-active and
active-passive failover*; Azure Site Recovery *Run a failover from on-premises to Azure*
and *Tutorial: Fail back Azure VM to the primary region*; PostgreSQL 17 *26.3. Failover*;
and Google SRE *Testing for Reliability*, section *Testing Disaster*. Retained:
`read.batch3-pg-warm.2026-10-21`; new records:
`read.aws-route53-failover.2026-10-31`, `read.azure-asr-failover.2026-10-31`,
`read.azure-asr-failback.2026-10-31`, `read.pg-failover.2026-10-31` and
`read.sre-testing-disaster.2026-10-31`. Source ids: `src.postgresql`, `src.sre`,
`src.aws-route53` and `src.azure-site-recovery` are registered. Canonical text SHA-256
`cbeed64d...`, `5b1475e4...`, `dd092294...`,
`bd1cf093...` and `425eb0ec...`. Exact URLs, sections and revisions are in the owner
section and lane note. None is a benchmark or production observation; no failover,
failback or DNS change was run.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Backup/PITR; Health Endpoint Monitoring;
Recovery Objectives.

---
metadata_version: 1
id: "tycho.page.43c706143e9208cbcb1770bcc62e9695"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c11-security-operations/health-readiness-and-liveness-checks.md
title: "Health, Readiness and Liveness Checks"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Health, Readiness and Liveness Checks; bounded owner
evidence and explicit limits."
route_hints:
  questions:
    - "Should the runtime distinguish process liveness, traffic readiness"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "health-readiness-and-liveness-checks"
evidence_scope:
  source_ids:
    - "src.kubernetes"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-27"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-27"
updated_at: "2026-10-27"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# Health, Readiness and Liveness Checks

**Identity.** Health, Readiness and Liveness Checks; family Security, isolation and
operational architecture; kind operations-pattern; priority core.

**Decision question.** Should the runtime distinguish process liveness, traffic readiness
and startup completion?

**Good-fit conditions.** Probes have different failure meanings; dependencies are not
conflated; restart/traffic removal are separate.

**Hard contraindications.** Reject when one probe is used for every failure, when a
liveness probe restarts healthy processes on a shared dependency, or when startup is
ignored.

**Competing alternative.** External journey monitoring plus process supervision. Reverse
the choice when probe complexity causes false restarts.

**Failure and recovery.** False positives and shared-dependency coupling are common;
verify semantics in the owner section.

**Technical owner.** [Practice response before production failure](../../v09-observability-security-and-operations/c06-incident-response-and-operational-change/incident-practice.md#health-readiness-and-liveness-checks) — health checks are bounded to recovery readiness.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-k8s-probes.2026-10-21: all fifteen served headings read.
The source is a public pattern/specification unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Synthetic Monitoring; Failover/Failback; Incident Response; SLI/SLO.

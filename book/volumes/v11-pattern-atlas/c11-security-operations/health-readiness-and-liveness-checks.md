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

**Competing alternative.** External journey monitoring when probes cannot observe the
user-visible contract. For process or host liveness, a platform-managed transport-level
probe, or existing platform metrics, log-based alerts or internal heartbeats, instead of
dedicated application health endpoints. Reverse the choice when application-specific
logic, a dependency chain or functional behavior must be verified.

**Failure and recovery.** False positives and shared-dependency coupling are common;
verify semantics in the owner section.

**Technical owner.** [Practice response before production failure](../../v09-observability-security-and-operations/c06-incident-response-and-operational-change/incident-practice.md#health-readiness-and-liveness-checks) — health checks are bounded to recovery readiness.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-k8s-probes.2026-10-21: all fifteen served headings read.
The transport-level and telemetry alternative is bound in the owner section to the public
Health Endpoint Monitoring pattern (`src.microsoft-cloud-patterns`), canonical text SHA-256
`b5b302585c4e60a5d696b128b6a03d21c9629848e9fa2be23e6e1bc1751d1d61`
(accessed 2026-10-29). Both sources are public documentation or pattern units, not
benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Synthetic Monitoring; Failover/Failback; Incident Response; SLI/SLO.

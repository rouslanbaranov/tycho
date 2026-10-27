---
metadata_version: 1
id: "tycho.page.b8f80e03e8346a4ba26e9d692a38945d"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/sli-slo-and-error-budgets.md"
title: "SLI / SLO and Error Budgets"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for SLI / SLO and Error Budgets; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should service health be governed by user-visible indicators,"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "sli-slo-and-error-budgets"
evidence_scope:
  source_ids:
    - "src.sre"
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
# SLI / SLO and Error Budgets

**Identity.** SLI/SLO and Error Budgets; family Security, isolation and operational
architecture; kind operations-pattern; priority core.

**Decision question.** Should service health be governed by user-visible indicators,
objectives and an explicit error budget?

**Good-fit conditions.** An SLI measures a meaningful journey; SLO target/window are
agreed; error budget drives action.

**Hard contraindications.** Reject when metrics are not user-visible, when targets are
arbitrary, or when budget breach has no consequence.

**Competing alternative.** Synthetic checks or raw infrastructure metrics alone. Reverse
the choice when measurement cost exceeds decision value.

**Failure and recovery.** Gaming and window mismatch are common; verify decisions in the
owner section.

**Technical owner.** [SLI / SLO and Error Budgets](../../v09-observability-security-and-operations/c01-slis-slos-and-error-budgets/service-level-indicators-objectives-and-alerts.md#sli-slo-and-error-budgets) — SLOs are bounded, not a complete measurement system.

**Sources.** [src.sre](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-sre-slo.2026-10-21: all eighteen served headings
read. Error Budgets was not a section; budget arithmetic is synthetic
guidance. The source is a public pattern/specification unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Synthetic Monitoring; Alerting; Incident Response; Health Checks.

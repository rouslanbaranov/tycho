---
metadata_version: 1
id: "tycho.page.77e5d6cab6c083335efb7fc74b423809"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/synthetic-monitoring.md"
title: "Synthetic Monitoring"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Synthetic Monitoring; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should probes exercise user-visible behavior from outside the"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "synthetic-monitoring"
evidence_scope:
  source_ids:
    - "src.sre-workbook"
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
# Synthetic Monitoring

**Identity.** Synthetic Monitoring; family Security, isolation and operational
architecture; kind operations-pattern; priority core.

**Decision question.** Should probes exercise user-visible behavior from outside the
service rather than rely only on internal metrics?

**Good-fit conditions.** A representative journey can be probed; coverage/locations are
known; false positives are triaged.

**Hard contraindications.** Reject when probes cannot authenticate safely, when they test
only shallow endpoints, or when alert noise exceeds signal.

**Competing alternative.** Real-user monitoring or internal SLOs. Reverse the choice when
synthetic coverage cost exceeds detection benefit.

**Failure and recovery.** Probe blindness and credential leakage are common; verify
journey coverage in the owner section.

**Technical owner.** [Burn-rate and alerts are actions, not decorations](../../v09-observability-security-and-operations/c01-slis-slos-and-error-budgets/budget-actions.md#synthetic-monitoring) — synthetic monitoring is bounded to alert/action reasoning.

**Sources.** [src.sre-workbook](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-sre-workbook-monitoring.2026-10-21: all twenty-three
headings read; no Synthetic Monitoring or Alerting headings exist. The source is a public
pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** SLI/SLO; Health Checks; Incident Response; Alerting.

---
metadata_version: 1
id: "tycho.page.ebee5e8bd7ca90b878acad1df2d8630a"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/audit-trail.md"
title: "Audit Trail"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Audit Trail; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should security-relevant actions be recorded in an append-only,"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "audit-trail"
evidence_scope:
  source_ids:
    - "src.openlineage"
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
# Audit Trail

**Identity.** Audit Trail; family Security, isolation and operational architecture; kind
observability-pattern; priority core.

**Decision question.** Should security-relevant actions be recorded in an append-only,
attributable log?

**Good-fit conditions.** The audited events are defined; identity/time/source are
captured; retention and access are controlled.

**Hard contraindications.** Reject when logs are mutable/deletable by the actor, when
events cannot be attributed, or when audit data is excessive/unused.

**Competing alternative.** Application logs with stricter retention or external SIEM.
Reverse the choice when audit completeness cannot be evidenced.

**Failure and recovery.** Tampering and missing events are common; verify authority in the
owner section.

**Technical owner.** [Audit Trail](../../v09-observability-security-and-operations/c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md#audit-trail) — logging/audit is bounded, not a logging platform manual.

**Sources.** [src.openlineage](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-openlineage.2026-10-21: sections "About OpenLineage",
"Object Model". The unit
covers lineage, not tamper-proof audit records; audit policy is synthetic design guidance.
The source is a public pattern/specification unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Structured Logging; Distributed Tracing; Least Privilege; Retention.

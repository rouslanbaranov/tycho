---
metadata_version: 1
id: "tycho.page.fd57fe37e916adffc5819aa849245d1d"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/structured-logging.md"
title: "Structured Logging"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Structured Logging; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should logs be emitted as structured events with stable fields"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "structured-logging"
evidence_scope:
  source_ids:
    - "src.otel"
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
# Structured Logging

**Identity.** Structured Logging; family Security, isolation and operational architecture;
kind observability-pattern; priority core.

**Decision question.** Should logs be emitted as structured events with stable fields
rather than free text?

**Good-fit conditions.** Fields are stable; redaction is defined; retention/cost are
owned; correlation IDs are available.

**Hard contraindications.** Reject when logs contain unredactable sensitive data, when
schema churn is unowned, or when volume overwhelms storage.

**Competing alternative.** Unstructured text parsed at query time. Reverse the choice when
structured logging cost exceeds diagnostic benefit.

**Failure and recovery.** On leakage, stop emission, rotate credentials, purge/redact retained
records and notify. On schema drift, migrate/backfill or dual-write with a compatibility window.

**Technical owner.** [Structured logging, authoritative audit and data lineage](../../v09-observability-security-and-operations/c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md#structured-logging) — logging/audit is bounded, not a logging platform manual.

**Sources.** [src.otel](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-otel-logs.2026-10-21: all seventeen served headings read. Attributes and
correlation were not headings; correlation policy is synthetic guidance. The source is a public
pattern/specification unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Distributed Tracing; Audit Trail; OpenLineage; Retention.

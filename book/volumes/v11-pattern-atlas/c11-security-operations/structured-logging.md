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
    - "Should logs be emitted as structured events with stable fields rather than free text?"
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
    - "src.owasp-asvs"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; owner-unit bindings carry both source records."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-27"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---
# Structured Logging

**Identity.** Structured Logging; family Security, isolation and operational architecture;
kind observability-pattern; priority core.

**Decision question.** Should logs be emitted as structured events with stable fields
rather than free text?

**Good-fit conditions.** Events use a consistent, machine-readable schema; sensitive data is
excluded or hashed or masked to its protection level; retention/cost are owned; correlation IDs
are available.

**Hard contraindications.** Reject when logs contain unredactable sensitive data, when
schema churn is unowned, or when volume overwhelms storage.

**Competing alternative.** Unstructured text parsed at query time. Reverse the choice when
structured logging cost exceeds diagnostic benefit.

**Failure and recovery.** Logging sensitive personal data without a legal basis, or failing to
protect logs as a high-value asset, can compromise privacy or system security; a schema that
varies across emitters also needs normalization before reliable analysis. Protect logs from
unauthorized access and modification, and transmit them securely to a separate system for
analysis, detection, alerting and escalation. Tycho recovery guidance, not an ASVS requirement:
stop emission, rotate exposed credentials, purge or redact retained records and notify.

**Technical owner.** [Structured logging, authoritative audit and data lineage](../../v09-observability-security-and-operations/c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md#structured-logging) — logging/audit is bounded, not a logging platform manual.

**Sources.** [src.otel](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-otel-logs.2026-10-21: all seventeen served headings read. Attributes and
correlation were not headings; correlation policy is synthetic guidance. The source is a public
pattern/specification unit, not a benchmark.
[src.owasp-asvs](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-asvs.2026-10-21, section "V16 Security Logging and Error Handling",
requirements 16.2.4, 16.2.5, 16.4.2 and 16.4.3; pinned PDF revision
a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5. ASVS is a
verification standard; it does not define a schema-versioning policy or a
purge/rotation/notification procedure.

**Decision state.** applicable-under-conditions.

**Related entries.** Distributed Tracing; Audit Trail; OpenLineage; Retention.

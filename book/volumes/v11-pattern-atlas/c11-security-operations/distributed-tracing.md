---
metadata_version: 1
id: "tycho.page.ff387baa8697be02afec1be6807b858f"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/distributed-tracing.md"
title: "Distributed Tracing"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Distributed Tracing; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should requests carry a trace context so spans across services can"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "distributed-tracing"
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
# Distributed Tracing

**Identity.** Distributed Tracing; family Security, isolation and operational
architecture; kind observability-pattern; priority core.

**Decision question.** Should requests carry a trace context so spans across services can
be correlated?

**Good-fit conditions.** Context propagation is possible; sampling policy is explicit;
sensitive data is excluded; storage/retention are owned.

**Hard contraindications.** Reject when one service suffices, when context cannot cross a
boundary, or when trace data would leak sensitive payloads.

**Competing alternative.** Structured logs with request IDs. Reverse the choice when
cross-service latency diagnosis justifies trace infrastructure.

**Failure and recovery.** Broken context and sampling bias are common; verify propagation
in the owner section.

**Technical owner.** [Distributed Tracing](../../v09-observability-security-and-operations/c03-distributed-tracing-and-propagation/distributed-tracing-context-and-sampling.md#distributed-tracing) — tracing is bounded, not an SDK implementation.

**Sources.** [src.otel](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-otel-traces.2026-10-21: all nineteen served headings read.
Sampling was not a section; sampling policy is synthetic guidance. The source is a
public pattern/specification unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Structured Logging; Audit Trail; SLI/SLO; Sampling.

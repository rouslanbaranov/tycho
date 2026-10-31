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
summary: "Decision card for Distributed Tracing; five bound public units and explicit limits."
route_hints:
  questions:
    - >-
      Should requests carry a trace context so spans across services can be
      correlated?
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
    - "src.trace-context"
    - "src.dapper"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Bound 2026-10-31 to five public units: OpenTelemetry traces, context
    propagation and sampling; W3C Trace Context; and Google Dapper. The
    src.dapper source id is registered. No claim-level mapping, independent
    review, promotion or source-completeness claim is made.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-27"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Distributed Tracing

**Identity.** Distributed Tracing; family Security, isolation and operational
architecture; kind observability-pattern; priority core.

**Decision question.** Should requests carry a trace context so spans across services can be
correlated?

**Good-fit conditions.** Context propagation is possible across every controlled boundary;
sampling policy and instrumentation coverage are explicit; sensitive data is excluded; storage
and retention are owned. OpenTelemetry says "With Context Propagation, Spans can be correlated
with each other and assembled into a trace, regardless of where Spans are generated." These are
Tycho conditions.

**Invariant — sampled observation, untrusted context.** A trace is a selected execution
story, not an authoritative business record. OpenTelemetry defines "Not sampled: A trace or
span is not processed or exported", and W3C's sampled flag means the caller "may have
recorded trace data". A missing span is unknown, not proof that no work occurred, until
instrumentation coverage and sampling policy are known. Trace and baggage values are
untrusted input: never use them for authorization, and keep business-effect authority with
the audit or log owner. **Tycho rule.**

**Hard contraindications.** Reject when no cross-service correlation is needed for the
decision question, when context cannot cross a boundary, or when trace data would leak
sensitive payloads. **Tycho contraindication.**

**Competing alternative.** Metrics and structured logs. OpenTelemetry notes that if you "only
use observability data in aggregate, and can thus pre-aggregate data", sampling may not be
appropriate, and metrics can "aggregate measurements in that context." A trace is "a collection
of structured logs with context, correlation, hierarchy, and more baked in"; Dapper "is not
intended to replace all other tools." **Tycho choice rule:** metrics for aggregate latency or
error rate; structured logs or audit for a discrete event; tracing when the cross-component
path is the question. Reverse when trace cost exceeds diagnostic benefit.

**Failure and recovery.** Broken context, instrumentation gaps and sampling loss are common.
Dapper says instrumentation "is often broken due to instrumentation bugs or omissions";
low-traffic workloads "may miss important events at such low sampling rates". W3C permits a
restart mutation: "Restart trace: All properties (trace-id, parent-id, trace-flags) are
regenerated"; separately, a version it cannot parse gets a new traceparent
and loses tracestate. OpenTelemetry says it is "critical to monitor tail-sampling components".
**Tycho runbook:** alert on instrumentation coverage, sampling-policy changes and context
rejection separately from product errors; record the sampling decision; treat a gap as
unknown, not success; restore propagation first.

**Technical owner.** [Distributed Tracing](../../v09-observability-security-and-operations/c03-distributed-tracing-and-propagation/distributed-tracing-context-and-sampling.md#distributed-tracing) — tracing is bounded, not an SDK implementation.

**Sources.** Five public units inspected on 2026-10-31: OpenTelemetry "Traces", "Context
propagation" and "Sampling"; W3C "Trace Context" (Recommendation of 23 November 2021); and
Google "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure" (technical report
dapper-2010-1). Retained: `read.batch6-otel-traces.2026-10-21`; new:
`read.otel-traces.2026-10-31`, `read.otel-context-propagation.2026-10-31`,
`read.otel-sampling.2026-10-31`, `read.w3c-trace-context.2026-10-31` and
`read.dapper-tracing.2026-10-31`. Source ids: `src.otel`, `src.trace-context` and
`src.dapper`. Exact URLs, revisions and limits are in the lane note and owner
section. None is a benchmark or production observation; no trace, sampler or
backend was run.

**Decision state.** applicable-under-conditions.

**Related entries.** Structured Logging; Audit Trail; SLI/SLO; Sampling.

---
metadata_version: 1
id: "tycho.page.f921597aae854c6996459fc025a9bca3"
kind: "page"
parent_id: "tycho.chapter.03ec5acf85e043a5a6d552a036bf4659"
canonical_path: "book/volumes/v09-observability-security-and-operations/c03-distributed-tracing-and-propagation/distributed-tracing-context-and-sampling.md"
title: "Distributed tracing: context propagation, sampling and causal limits"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated decision and bounded source limits for Distributed tracing and propagation. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which context, sampling and async boundaries determine trace usefulness?"
  prerequisites: []
  related_ids:
    - "tycho.page.436c2b22dc9e47acaaca7d18fadb511c"
    - "tycho.page.c987c475cc5340bcb967f4b6f963b295"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.a2c47a0850154eaa95e1eb97e23f9c71"
    - "tycho.page.6b9a3f5c7bae455ab4f56f151f17b406"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b7ea8fb13ebb4079af2333e475f97106"
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
    - "tycho.page.aac0f46189b74948bedfc30a81ec80e5"
    - "tycho.page.bc30179a9cda4c12b9deb383e8751d47"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Distributed"
    - "tracing"
    - "context"
    - "propagation"
    - "sampling"
    - "and"
    - "causal"
    - "limits"
evidence_scope:
  source_ids:
    - "src.trace-context"
    - "src.otel"
    - "src.dapper"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Bound 2026-10-31 to five public units: OpenTelemetry traces, context
    propagation and sampling; W3C Trace Context; and Google Dapper. The
    src.dapper source id is registered. No claim-level mapping, independent
    review, promotion or source-completeness claim is made.
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-31"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.f921597aae854c6996459fc025a9bca3:-1 -->

# Distributed tracing: context propagation, sampling and causal limits

> **Tycho independent book draft V09/C03, 2026-10-19; evidence bound 2026-10-31.**
> Draws on W3C Trace Context (Recommendation of 2021), published OpenTelemetry
> tracing semantics and the Dapper technical report. All requests, diagrams and
> fault scenarios are original fiction. No trace collection, backend or
> distributed experiment was executed. The content_review field records a
> self-check; no independent acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Distributed Tracing](../../v11-pattern-atlas/c11-security-operations/distributed-tracing.md#distributed-tracing) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.f921597aae854c6996459fc025a9bca3:0 -->
## Purpose and mission

Distributed tracing reconstructs *a selected execution story*: a request enters a component, starts work, calls another component and may later complete asynchronously. A trace can illuminate critical-path waiting, retries and failure propagation—but **it is not an authoritative record of every business effect**. A missing span may mean no work occurred, the instrumentation failed, or the sampling policy intentionally discarded it.

The architectural problem is to propagate enough correlation context across controlled boundaries while limiting overhead, data exposure, stale assumptions and accidental linkability. [Logging, audit and lineage](../c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md) owns authoritative business and dataset histories; [metrics/SLOs](../c01-slis-slos-and-error-budgets/service-level-indicators-objectives-and-alerts.md) owns user-visible success and objectives.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Interpret traces as sampled, propagated observations with explicit trust and asynchronous boundaries.

A missing span does not prove no effect occurred, and untrusted baggage must not become an authorization decision.

The detailed pages separate the mechanisms that make this decision conditional:

- [Trace identity and causal interpretation](trace-causality.md) — What execution relationship can a span and its timing establish?
- [Propagation, sampling and untrusted context](sampling-trust.md) — What does a missing span or forged context prevent a trace from proving?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
## Bounded pattern ownership notes

### Distributed Tracing

**Mechanism.** Distributed tracing reconstructs *a selected execution story*: a request enters a
component, starts work, calls another component and may later complete asynchronously. A trace
is assembled from propagated context and sampled spans, not from a complete transaction log.
OpenTelemetry describes a trace as "The path of a request through your application" and says
"With Context Propagation, Spans can be correlated with each other and assembled into a trace,
regardless of where Spans are generated." W3C Trace Context "defines standard HTTP headers and
a value format to propagate context information that enables distributed tracing scenarios."
Dapper describes "A trace context is a small and easily copyable container of span attributes
such as trace and span ids." **Tycho reading:** trace usefulness depends on context crossing
each controlled boundary and on spans being emitted at those boundaries.

**Invariant.** A trace is a sampled, propagated observation, not an authoritative record of
every business effect. W3C says the sampled flag "denotes that the caller may have recorded
trace data", not that every span was recorded; the trace-id "SHOULD be globally unique", not
guaranteed. OpenTelemetry defines "Not sampled: A trace or span is not processed or exported."
Dapper says that, although "Dapper alone is sometimes sufficient for a developer to identify
the source of a performance anomaly", "it is not intended to replace all other tools." Context is also untrusted input: OpenTelemetry warns that
"Malicious actors could send forged trace headers to manipulate your tracing data or potentially
exploit vulnerabilities in context parsing" and suggests that you may want to ignore or sanitize
it. **Tycho rule:** a missing span is ambiguous until instrumentation coverage and sampling
policy are known; do not read absence as proof that no work occurred, and keep business-effect
authority in the audit/log owner. Never promote trace or baggage values into an authorization
decision.

**Failure and recovery.** Instrumentation gaps and sampling loss are normal failure modes.
Dapper warns that a tracing infrastructure relying on application collaboration "becomes
extremely fragile, and is often broken due to instrumentation bugs or omissions"; low-traffic
workloads "may miss important events at such low sampling rates". OpenTelemetry notes that with
head sampling "it is not possible to make a sampling decision based on data in the entire
trace", while consistent-probability head sampling keeps whole traces and avoids missing spans
inside a sampled trace. W3C restarts a trace when context is invalid: "Restart trace: All
properties (trace-id, parent-id, trace-flags) are regenerated", and if "the version cannot be
parsed, the vendor creates a new traceparent header and deletes tracestate." **Tycho runbook:**
alert on instrumentation coverage, sampling-policy changes and context rejection separately from
product errors; record the sampling decision with the trace; investigate a gap as unknown, not
as success. Recovery means restoring propagation and instrumentation coverage first, then
re-reading the trace under the new policy.

**Alternative.** Metrics and structured logs are alternatives for different questions. For
aggregate observation, OpenTelemetry advises that if you "only use observability data in
aggregate, and can thus pre-aggregate data", sampling may not be appropriate; context
propagation also lets you "aggregate measurements in that context." Traces themselves are "a
collection of structured logs with context, correlation, hierarchy, and more baked in", so a
discrete event may be answered by a structured log when the cross-component path is not the
question. Dapper is "not intended to replace all other tools", and general-purpose debug logs
remain a separate collection path. **Tycho choice rule:** use metrics for aggregate latency or
error rates, structured logs or audit for a discrete business event, and tracing when the
cross-component path itself is the question; reverse when trace storage and instrumentation
cost exceed the diagnostic benefit.

**Bound source limits.** Five public units were inspected on 2026-10-31: OpenTelemetry,
"Traces", "Context propagation" and "Sampling"; W3C, "Trace Context", Recommendation of
23 November 2021; and Google, "Dapper, a Large-Scale Distributed Systems Tracing
Infrastructure", technical report dapper-2010-1. The exact units are:
<https://opentelemetry.io/docs/concepts/signals/traces/>,
<https://opentelemetry.io/docs/concepts/context-propagation/>,
<https://opentelemetry.io/docs/concepts/sampling/>,
<https://www.w3.org/TR/2021/REC-trace-context-1-20211123/> and
<https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36356.pdf>.
The bound or retained records are `read.batch6-otel-traces.2026-10-21` (retained),
`read.otel-traces.2026-10-31`,
`read.otel-context-propagation.2026-10-31`, `read.otel-sampling.2026-10-31`,
`read.w3c-trace-context.2026-10-31` and `read.dapper-tracing.2026-10-31`. They are living
documentation, a dated Recommendation and a technical report, not benchmarks or production
observations. The OTel pages record their last edits (January 2026, August 2026 and
October 2025); the W3C unit is the dated 2021 Recommendation; the Dapper PDF is the 2010
report. No trace, sampler or backend was run. The missing-span interpretation, choice rule
and runbook remain Tycho guidance, not source claims.

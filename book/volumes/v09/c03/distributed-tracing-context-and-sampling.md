---
metadata_version: 1
id: "tycho.page.f921597aae854c6996459fc025a9bca3"
kind: "page"
parent_id: "tycho.chapter.03ec5acf85e043a5a6d552a036bf4659"
canonical_path: "book/volumes/v09/c03/distributed-tracing-context-and-sampling.md"
title: "Distributed tracing: context propagation, sampling and causal limits"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for Distributed tracing: context propagation, sampling and causal limits. Scope includes 1. A trace, a span and a request are different entities; 2. Causal and temporal interpretation; 3. Propagation is also a trust boundary."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Distributed tracing: context propagation, sampling and causal limits?"
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
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Distributed tracing: context propagation, sampling and causal limits

> **Tycho independent book draft V09/C03, 2026-10-19.** Draws on W3C Trace Context (Recommendation of 2021) and published OpenTelemetry tracing semantics. All requests, diagrams and fault scenarios are original fiction. No trace collection, backend or distributed experiment was executed.

## Purpose and mission

Distributed tracing reconstructs *a selected execution story*: a request enters a component, starts work, calls another component and may later complete asynchronously. A trace can illuminate critical-path waiting, retries and failure propagation—but **it is not an authoritative record of every business effect**. A missing span may mean no work occurred, the instrumentation failed, or the sampling policy intentionally discarded it.

The architectural problem is to propagate enough correlation context across controlled boundaries while limiting overhead, data exposure, stale assumptions and accidental linkability. [Logging, audit and lineage](../c04/logs-audit-and-data-lineage.md) owns authoritative business and dataset histories; [metrics/SLOs](../c01/service-level-indicators-objectives-and-alerts.md) owns user-visible success and objectives.

## 1. A trace, a span and a request are different entities

| Identity | What it describes | What it does not prove |
|---|---|---|
| Trace ID | Correlates selected spans for one distributed trace | All effects, users or messages were recorded |
| Span ID and parent | A named timed operation and immediate relationship | Child timing is entirely CPU execution |
| Span link | Relationship to another span or asynchronous context | Guaranteed causal consistency or exactly-once delivery |
| Request/operation ID | Stable logical business intent where application defines one | Equivalent to a trace ID across all retries |
| Data/event identity | Durable domain effect with revision/sequence when required | A traced request committed successfully |

The [W3C Trace Context recommendation](https://www.w3.org/TR/trace-context/) standardizes HTTP propagation through traceparent and tracestate. It does not require every receiving service to create an exported span or guarantee a centralized complete trace. Trace context may be continued, ignored or regenerated at trust boundaries according to documented behavior.

## 2. Causal and temporal interpretation

A parent/child span structure records instrumented containment or relationships. This is not a global wall-clock ordering guarantee: clocks can differ across hosts, and asynchronous work may start after an HTTP response. A parent duration need not equal the sum of child durations because children overlap or traces omit work.

```mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant Q as Durable queue
    participant W as Worker
    C->>A: Request with trace context
    A->>Q: Publish accepted work + job ID
    A-->>C: Accepted/pending response
    Q-->>W: Deliver job later (new execution context)
    W->>W: Process and record durable result
    Note over A,W: Correlation/link helps diagnosis but cannot prove exactly-once effect
```

**Text alternative:** API accepts a durable job then responds before background processing finishes. A later worker may create a distinct trace linked to the initiating operation. The job's authoritative status remains a separate domain record. No real runtime or messaging product was used.

Trace data can help locate where a delay happened only when:
- clocks/timestamps and parent relationships are interpreted at the correct boundaries;
- instrumentation covers the suspected operation;
- spans include meaningful errors, retries, concurrency and dependency context;
- one logical business operation may have several network attempts/traces;
- sampling and export failures are disclosed.

## 3. Propagation is also a trust boundary

External callers can send headers bearing fabricated trace IDs, flags and vendor state. Do not treat externally supplied context as authorization, tenant membership, evidence of an authenticated principal, or permission to attach protected metadata to a trace.

The [W3C spec privacy/security considerations](https://www.w3.org/TR/trace-context/#security-considerations) discuss propagation risks, including sensitive data through trace context and boundaries. Do not carry credentials or personally identifying values in trace IDs, tracestate or span attributes. Generate or scrub context as appropriate for trust zones and apply policy-based access to traces and their search metadata.

**Synthetic failure:** a fictional catalog sends a full contact address as a trace label. The telemetry backend allows broad diagnostic access; an otherwise harmless trace becomes a privacy disclosure. The architecture must instead use bounded safe correlation and restrict detailed identity to the actual authorized business system.

## 4. Sampling limits what the trace can support

| Policy | Advantage | Limitation |
|---|---|---|
| Head sampling | Can limit collection near request start | Later severe error may be missed |
| Tail sampling | Can prefer slow/error traces using fuller context | Requires buffered state and collector resources; decisions can be late |
| Always-on bounded development sampling | Excellent reproduction for controlled fixtures | May be too costly or intrusive for arbitrary high-volume traffic |
| Adaptive/service-specific | Fits selected cost/diagnostic objectives | Biases populations; not a statistical census |

The [OpenTelemetry sampling concepts](https://opentelemetry.io/docs/concepts/sampling/) explain sampling decisions and trade-offs. A small selected trace set cannot accurately estimate every service success ratio unless the sampling design supports that inference and uncertainty is disclosed.

A missing trace for a transaction does not prove that no accepted write exists. A trace with a successful span status does not prove the database commit or downstream external effect was correct.

## 5. Context, async messages and retries

When an RPC call times out, the client can retry under the same logical operation key but a new span or trace. The tracing design should represent **attempt** versus **operation**, preserve optional links, and avoid inflating business throughput from multiple attempts.

An asynchronous workflow may have multiple producers and consumers; a single parent chain can be misleading. Span links or stable message/job IDs support correlation but do not enforce message order or a distributed transaction. [Outbox/idempotency](../../../distributed/transactional-outbox-and-idempotency.md) owns acknowledgment and duplicate-effect boundaries; [streaming](../../v04/c08/stateful-stream-processing-and-cdc.md) owns versioned event/replay state.


### Worked trust-boundary example: an upstream sampling flag is not an authorization grant

**Original hypothetical:** an unauthenticated client sends a crafted `traceparent` with the sampled bit set and a reused trace ID. A trusted API gateway forwards the incoming header to three services. If each service blindly performs expensive full recording whenever the external sampled bit is set, an attacker could inflate telemetry work or contaminate correlations. Even without malicious intent, a missing downstream exporter may create a misleading partial trace.

The [W3C Trace Context Recommendation, sampled flag](https://www.w3.org/TR/trace-context/#sampled-flag) describes propagation and a *hint about recording behavior*, not authenticated proof that every ancestor span was stored. Its [security guidance](https://www.w3.org/TR/trace-context/#security-considerations) warns about untrusted sampling and information/denial-of-service risks.

| Crossing | Safe design policy | What a trace cannot establish |
|---|---|---|
| Internet client → gateway | Parse and bound headers; follow a deliberate restart/normalization and sampling policy on the trust boundary | Incoming trace identity is authentic |
| Gateway → internal RPC | Propagate correlation according to specification, enforce independently bounded telemetry costs | Every hop exported a span |
| Queue/event consumer | Link execution to stable message/business identifiers across retries, if appropriate | One correlation ID proves single delivery or ordering |
| API mutation → user effect | Record domain-authoritative effect identity and audit separately | A trace span proves a database transaction committed |

**Recovery/failure reasoning:** when trace data is incomplete, use request counts and unsampled user-level SLIs to detect population impact. Missing spans cannot be treated as missing work. Forensics that needs a complete durable business history should use a controlled audit mechanism, not sampling-dependent traces.

**Proposed negative test, not run:** send malformed, oversized, reused and forcibly sampled incoming headers; verify safe rejection/restart, no unauthorized correlation of tenant records, bounded exporter cost and continuity for permitted internal requests. Compare sampled spans against independently counted attempts without extrapolating sample p99 to the full population without an appropriate sampling design. The [audit owner](../c04/logs-audit-and-data-lineage.md) covers durable accountable effects; the [security owner](../c05/identity-authorization-and-isolation.md) covers the actual authorization boundary.

### Forged W3C Baggage is not authenticated tracing context

[W3C Baggage](https://www.w3.org/TR/baggage/) is a **separate specification** from W3C Trace Context. Its `baggage` header propagates arbitrary application-defined key/value data across service calls; it gives no authorization or confidentiality guarantee for a propagated value. It may contain user-identifiable or proprietary values; §4–§5 of the standard discuss malicious header parsing, information exposure, boundary filtering and privacy risks. A `traceparent` sampled bit, a `tracestate` vendor member and a `baggage` key are three different trust inputs; none proves the caller owns an arbitrary tenant.

**Original fictional attack:** an internet client sends `traceparent` with a forced sampled bit and `baggage: tenant_id=internal-admin,customer_email=private%40example.test,experiment=priority`. An API gateway has authenticated the caller as **tenant t1**; a downstream worker handles t2-only objects. If the gateway forwards the arbitrary baggage unchanged and a collector turns it into indexed span attributes, a private address and fabricated admin tenant identifier can leak. If authorization middleware mistakenly reads `tenant_id` from baggage, the request may cross object permissions even though the actual authentication context remains t1.

| Boundary | Safe requirement | Insecure inference |
|---|---|---|
| Untrusted client → gateway | Parse size/grammar, drop or allow-list incoming baggage and remove user identifiers | Header-supplied `tenant_id` is a verified principal |
| Gateway → trusted worker | Derive tenant/access scope from authenticated session/authorization; propagate only approved operational context | Copying baggage grants authority to t2 |
| Worker → external provider | Explicitly strip private/internal baggage across the outgoing trust boundary | All tracing metadata is harmless diagnostic text |
| Instrumentation → telemetry backend | Limit baggage-to-attribute conversion, restrict read rights, test redaction in collector/exporter | Backend indexing is automatically privacy-safe |

**Proposed negative test, not executed:** send forged tenant fields, oversized/malformed headers and a valid `traceparent` paired with confidential baggage; observe whether the gateway removes unauthorized keys, whether every outbound header and downstream span omits private values, and whether t1 ever reads t2-only business state. Independently drop sampled traces and verify the business audit remains complete. The failure oracle is *zero unauthorized business access and zero sensitive baggage egress*, not merely HTTP success or a trace visualization. W3C Baggage gives propagation syntax and warnings, not a universal filtering implementation.

## 6. Original diagnostic decision

A hypothetical API's p99 worsens after a release. One proposal is to migrate to a different transport. First inspect sampled parent critical paths, dependency queues/pool wait, timeouts and retries; compare with unsampled user-level error/latency metrics. If only ten percent of requests were sampled, a p99 measurement from those traces cannot automatically be treated as the population p99.

**Falsifiable test (not run):** inject a slow dependent RPC and a separate canceled background job; verify context propagation, trace/export gaps, parent critical-path visibility, safe cardinality/labels and business operation reconciliation. The test may fail in different places: tracing is diagnostic evidence, while final effect identity and correct outcomes require domain checks.

## 7. Public source ledger and nonclaims

| Public source read | Narrow support | Not proven |
|---|---|---|
| [W3C Trace Context Recommendation, 23 Nov 2021](https://www.w3.org/TR/trace-context/) | traceparent/tracestate propagation and privacy/security context | Actual interop between fictional services |
| [OpenTelemetry sampling concepts](https://opentelemetry.io/docs/concepts/sampling/) | Sampling approaches, trace-data selection limits | Recorded trace completeness or analytical p99 validity |
| [Tycho earlier tracing/logging research](../../../observability/trace-context-lineage-and-audit.md) | Prior cross-domain conceptual distinctions | Separate owner acceptance or collected evidence |

All example events, diagrams and tracing behaviors are hypothetical educational work. No tracing backend, software build, distributed request, review or sampling evaluation was performed. Former combined tracing/logging research remains preserved for claim-level editorial reconciliation, not reproduced in full.

**Navigation:** proposed **V09/C03** in [book outline](../../../PROPOSED-STRUCTURE.md), current [observability landing](../../../observability/README.md). Related [Metrics and SLOs](../c01/service-level-indicators-objectives-and-alerts.md), [Audit and lineage](../c04/logs-audit-and-data-lineage.md), [Tail latency](../../v07/c04/tail-latency-fanout-and-deadline-budgets.md).

<!-- tycho-edition-navigation -->

## Edition navigation and evidence scope

| Route | Destination |
|---|---|
| Parent chapter | [Question, conclusions and reading route](README.md) |
| Parent volume | [Volume synthesis](../README.md) |
| Book | [Authoritative contents](../../../README.md) |
| Source versions and access scope | [Registered sources](../../../../sources/README.md) and the exact page-local citation ledger above |

The original manuscript was accepted under #213 at the recorded baseline. Earlier draft/review labels describe historical authoring events. Source access, versions, unexecuted experiments and nonclaims retain their original scope; assembly does not assert a new source read or benchmark. The chapter landing adds editorial synthesis and navigation.

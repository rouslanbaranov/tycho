---
metadata_version: 1
id: "tycho.page.bc30179a9cda4c12b9deb383e8751d47"
kind: "page"
parent_id: "tycho.chapter.03ec5acf85e043a5a6d552a036bf4659"
canonical_path: "book/volumes/v09-observability-security-and-operations/c03-distributed-tracing-and-propagation/sampling-trust.md"
title: "Propagation, sampling and untrusted context"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "What does a missing span or forged context prevent a trace from proving?"
route_hints:
  questions:
    - "What does a missing span or forged context prevent a trace from proving?"
  prerequisites:
    - "tycho.page.aac0f46189b74948bedfc30a81ec80e5"
  related_ids:
    - "tycho.chapter.03ec5acf85e043a5a6d552a036bf4659"
    - "tycho.page.f921597aae854c6996459fc025a9bca3"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "sampling"
    - "trust"
evidence_scope:
  source_ids:
    - "src.trace-context"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.f921597aae854c6996459fc025a9bca3; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Propagation, sampling and untrusted context

**Owning question:** What does a missing span or forged context prevent a trace from proving?

This page belongs to [V09/C03 — Distributed tracing and propagation](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.f921597aae854c6996459fc025a9bca3:3 -->
## 3. Propagation is also a trust boundary

External callers can send headers bearing fabricated trace IDs, flags and vendor state. Do not treat externally supplied context as authorization, tenant membership, evidence of an authenticated principal, or permission to attach protected metadata to a trace.

The [W3C spec privacy/security considerations](https://www.w3.org/TR/trace-context/#security-considerations) discuss propagation risks, including sensitive data through trace context and boundaries. Do not carry credentials or personally identifying values in trace IDs, tracestate or span attributes. Generate or scrub context as appropriate for trust zones and apply policy-based access to traces and their search metadata.

**Synthetic failure:** a fictional catalog sends a full contact address as a trace label. The telemetry backend allows broad diagnostic access; an otherwise harmless trace becomes a privacy disclosure. The architecture must instead use bounded safe correlation and restrict detailed identity to the actual authorized business system.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f921597aae854c6996459fc025a9bca3:4 -->
## 4. Sampling limits what the trace can support

| Policy | Advantage | Limitation |
|---|---|---|
| Head sampling | Can limit collection near request start | Later severe error may be missed |
| Tail sampling | Can prefer slow/error traces using fuller context | Requires buffered state and collector resources; decisions can be late |
| Always-on bounded development sampling | Excellent reproduction for controlled fixtures | May be too costly or intrusive for arbitrary high-volume traffic |
| Adaptive/service-specific | Fits selected cost/diagnostic objectives | Biases populations; not a statistical census |

The [OpenTelemetry sampling concepts](https://opentelemetry.io/docs/concepts/sampling/) explain sampling decisions and trade-offs. A small selected trace set cannot accurately estimate every service success ratio unless the sampling design supports that inference and uncertainty is disclosed.

A missing trace for a transaction does not prove that no accepted write exists. A trace with a successful span status does not prove the database commit or downstream external effect was correct.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f921597aae854c6996459fc025a9bca3:5 -->
## 5. Context, async messages and retries

When an RPC call times out, the client can retry under the same logical operation key but a new span or trace. The tracing design should represent **attempt** versus **operation**, preserve optional links, and avoid inflating business throughput from multiple attempts.

An asynchronous workflow may have multiple producers and consumers; a single parent chain can be misleading. Span links or stable message/job IDs support correlation but do not enforce message order or a distributed transaction. [Outbox/idempotency](../../../distributed/transactional-outbox-and-idempotency.md) owns acknowledgment and duplicate-effect boundaries; [streaming](../../v04-distributed-coordination-and-events/c08-stateful-event-time-stream-processing/stateful-stream-processing-and-cdc.md) owns versioned event/replay state.


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

**Proposed negative test, not run:** send malformed, oversized, reused and forcibly sampled incoming headers; verify safe rejection/restart, no unauthorized correlation of tenant records, bounded exporter cost and continuity for permitted internal requests. Compare sampled spans against independently counted attempts without extrapolating sample p99 to the full population without an appropriate sampling design. The [audit owner](../c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md) covers durable accountable effects; the [security owner](../c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md) covers the actual authorization boundary.

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

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f921597aae854c6996459fc025a9bca3:6 -->
## 6. Original diagnostic decision

A hypothetical API's p99 worsens after a release. One proposal is to migrate to a different transport. First inspect sampled parent critical paths, dependency queues/pool wait, timeouts and retries; compare with unsampled user-level error/latency metrics. If only ten percent of requests were sampled, a p99 measurement from those traces cannot automatically be treated as the population p99.

**Falsifiable test (not run):** inject a slow dependent RPC and a separate canceled background job; verify context propagation, trace/export gaps, parent critical-path visibility, safe cardinality/labels and business operation reconciliation. The test may fail in different places: tracing is diagnostic evidence, while final effect identity and correct outcomes require domain checks.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](trace-causality.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](distributed-tracing-context-and-sampling.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

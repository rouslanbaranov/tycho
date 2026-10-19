---
metadata_version: 1
id: "tycho.page.6b9a3f5c7bae455ab4f56f151f17b406"
kind: "page"
parent_id: "tycho.landing.b7ea8fb13ebb4079af2333e475f97106"
canonical_path: "book/observability/trace-context-lineage-and-audit.md"
title: "Distributed tracing, structured logs, data lineage and trustworthy audit"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for Distributed tracing, structured logs, data lineage and trustworthy audit. Scope includes 1. Trace context and causality boundaries; What a trace may fail to show; 2. Correlation without recording credentials."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Distributed tracing, structured logs, data lineage and trustworthy audit?"
  prerequisites: []
  related_ids: []
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Distributed"
    - "tracing"
    - "structured"
    - "logs"
    - "data"
    - "lineage"
    - "and"
    - "trustworthy"
    - "audit"
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

# Distributed tracing, structured logs, data lineage and trustworthy audit

> Tycho E14-11 [#89](https://github.com/rouslanbaranov/tycho/issues/89). Original technical manuscript using official public source sections inspected 2026-10-19. Examples are fictional and conceptual; no capture pipeline, incident, authorized forensic procedure or human review was executed.

## Purpose and mission

Four superficially similar records answer **different questions**:

1. **Trace:** how one distributed request or causal activity progressed across spans, where time was spent and which operations were sampled.
2. **Operational log:** what one component reported at a particular time, including context, severity and diagnostic details.
3. **Data/build lineage:** which input assets, transformations, jobs and versions contributed to a derived output.
4. **Audit record:** who or what was authorized to perform a material action, which policy decision was made, and which tamper-evident record supports later accountability.

Putting all four in the same search system does not make them equivalent or complete. The goal is to link identities appropriately without leaking secrets, inventing causal edges or assuming best-effort telemetry is authoritative evidence of a committed business action.

## 1. Trace context and causality boundaries

The W3C Trace Context recommendation standardizes the traceparent and tracestate propagation headers for interoperable distributed tracing. Traceparent identifies a position in a trace, while tracestate may carry vendor-related information. The specification also discusses privacy and malicious-header risks. [E01]

A **span** represents a named operation with start/end timestamps and attributes; it may have a parent or one or more links to other contexts. These records can model nested synchronous calls and causal associations across asynchronous processing, but **a span's existence is not proof that a database transaction committed**.

Consider a synthetic request:

Client → API ingress (trace T) → registration service (child span) → relational commit → outbox record → relay later publishes message → consumer updates projection.

The relay and consumer may execute much later, potentially in other traces. A parent/child relation may be inappropriate for an asynchronous job that was enqueued hours earlier; explicit span links or a separate stable business/event identity may communicate causality more truthfully. An event ID, request idempotency key, transaction/outbox ID and trace ID are separate concepts.

### What a trace may fail to show

- Unsampled requests or collector/exporter drops; absence of a span is not proof that an operation did not happen.
- A long pause on the client or in a queue before instrumentation began; measured span duration depends on start/end boundary.
- Retries that changed trace IDs but are one logical user operation.
- Clock skew between hosts; subtracting wall-clock span timestamps across machines is unsafe without clock assumptions.
- A missing external dependency, asynchronous queue or client retry that was not instrumented.
- Sensitive information in baggage/tracestate/attributes if sanitization is missing.

Sampling must declare whether it is head-based, tail-based or operation-aware; head sampling may drop rare failures, while tail sampling requires buffering and therefore changes memory/latency/retention costs. A low sample rate makes traces useful for exemplars but weak as the sole authority for a user SLO.

## 2. Correlation without recording credentials

Use multiple bounded identities:
- **Trace ID / Span ID:** telemetry correlation, generated independently of user secrets.
- **Logical request/idempotency identity:** repeated user intent, scoped and retained under application contract.
- **Business/event ID:** authoritative domain operation or durable event, access-controlled according to data sensitivity.
- **Deployment artifact/config ID:** exact software/environment identity of the producer.
- **Dataset/job/run identity:** lineage between inputs and derived outputs.

Only store the minimum necessary fields at a suitable trust boundary. W3C explicitly flags potential information leakage through trace headers; a downstream party may correlate otherwise separate requests. [E01] Do not place tokens, passwords, raw account-like identifiers or unrestricted personal payloads in headers, span attributes or logs.

Logs can include a trace/span ID when applicable, but must not fabricate them for unrelated background events. OpenTelemetry's Logs Data Model distinguishes origin Timestamp, collector ObservedTimestamp, TraceId, SpanId, severity, body, resource and attributes. [E02] Preserve clock source and event-vs-observation times when examining delayed delivery.

## 3. Logging is operational evidence, not an unlimited audit trail

| Property | Operational log | Dedicated authoritative audit record |
|---|---|---|
| Primary purpose | Diagnose behavior and errors | Reconstruct accountable, security-relevant and irreversible decisions |
| Typical durability | Often best-effort, sampled/filtered/short retention | Explicit durability, retention, access, integrity and failure policy |
| Identity | Component/time/trace correlation | Principal, actor/delegation, action, target, policy decision, time and immutable event ID |
| Ordering | May be delayed, duplicated and reordered | Stable per-authority sequence/hash or external evidence with documented ordering bounds |
| Privacy | Sanitize freeform messages and attributes | Bounded schema, access restrictions, redaction, retention and legal requirements |
| Trust | A compromised application may forge its own logs | Stronger isolation/append integrity/verification is necessary for accountability |

An audit event has to say **what happened**, not just what code intended to do. A command-requested audit event written *before* a failed business transaction is not proof of a completed business effect. When audit must agree with authoritative state, define transactional or reconciliation mechanisms and their failure behavior.

If the audit pipeline is unavailable, choose a documented policy: reject a protected operation, buffer with a durable bounded queue, or accept a declared loss risk if permitted. Sending an audit record asynchronously on a best-effort channel while promising no evidence gaps is a contradiction.

### Proposed original audit record envelope

| Field | Intended semantics |
|---|---|
| event_id | Uniquely identifies one audit event for dedup/replay |
| occurred_at / observed_at | Origin and collection times, with clock/synchronization caveat |
| actor_id / delegated_from | Authenticated service or principal and delegated authority |
| action / resource_kind / resource_id | Exactly which protected operation was attempted/committed |
| decision / outcome / reason_code | Authorization outcome versus durable business outcome; distinguish pending/unknown |
| policy_version / artifact_digest | Versioned policy and software identity relevant to the decision |
| correlation_id | Bounded link to eligible traces or business event, not a secret |
| integrity_reference | Hash/sequence/signature or external append-only witness as designed and tested |
| classification / retention_rule | Handling restrictions and deletion/retention contract |

Fields are a **Tycho illustrative contract**, not a claim that OpenTelemetry defines this audit schema or that any signature implementation is present.

## 4. Data lineage is not a request trace

OpenLineage's public specification identifies jobs, runs and input/output datasets, with facets that record additional metadata such as producer, execution parameters and explicit lineage. [E03] Its lineage facets can describe dataset- or job-owned relationships with fields, avoiding an inferred all-inputs-to-all-outputs cross-product. [E04]

Example, entirely fictional: a nightly reporting job reads registrations and event-delivery records, then outputs a summary dataset. Request traces show how particular API calls executed; they do not establish which historical dataset versions and transformation code produced this report. A lineage record should instead link:

source dataset namespace/name/version → transformation job/version/run → output dataset namespace/name/version, plus any qualifying field-level relationship actually known.

The existence of a shared job does not prove every input field affects every output field. Unknown column-level mappings must be marked unknown. Likewise a Git code dependency is not automatically an input-data lineage edge, and two concepts appearing in the same document do not create data provenance.

Build provenance is another distinct boundary: it describes how a software artifact was built. Link it through artifact digests and job identity when appropriate, but do not confuse it with runtime data transformation lineage or human audit events.

## 5. Failure chronology: traces present, business truth missing

Imagine a fictional registration deployment with these events:

1. The API receives a request and creates trace T; span A calls the database.
2. The database transaction commits a record and an outbox intent, but A's response is lost.
3. The client retries with idempotency identity K, now in another trace T2.
4. A relay redelivers event E after an acknowledgment timeout. A consumer's trace T3 shows two deliveries.
5. The audit log collector drops an event due to a full buffer.

An analyst who counts traces concludes there were two registration attempts, but that does **not** tell whether there were one or two committed business registrations. The authoritative registration/event tables and idempotency outcomes decide the count. The trace IDs diagnose timing; the event ID helps deduplicate; the missing audit record must be reported as a gap, never reconstructed from a guessed span.

The safe question sequence is: define business invariant → query authoritative state at a consistent point → obtain idempotency and event identities → use logs and traces as supporting timing/context → reconcile audit coverage and declare missing evidence.

## 6. Architecture decisions and access controls

- Use a request-tracing pipeline for distributed latency, sampled causal diagnosis and dependency maps, with bounded trace propagation trust.
- Use structured operational logs for errors/context with strict attribute allowlists, retention and incident access.
- Use lineage where recurring transformations and datasets require reproducibility or impact analysis; not every small service needs a dedicated lineage platform.
- Design authoritative audit where permissions, irreversible effects and accountability require a durable record; make audit retention, immutability and access enforceable, not aspirational.
- Keep raw sensitive input out of centralized telemetry; hash/redact only where correlation remains valid and collision/rotation implications are understood.
- Evaluate storage/egress cardinality, sampling coverage, recovery during an outage, query latency and cost separately for each signal.

**Insufficient-evidence outcome:** if two traces suggest duplicate commands but source-of-truth keys and consumer durable side effects are inaccessible, it is not possible to conclude how many registrations completed. Ask for a safe read of authoritative records and correlation identities; do not fabricate a causal graph.

## 7. Source-to-claim ledger and research gaps

| Ref | Official public source inspected 2026-10-19 | Supports and limits |
|---|---|---|
| E01 | [W3C Trace Context](https://www.w3.org/TR/trace-context/), traceparent, tracestate and security/privacy | Propagation semantics, not guaranteed end-to-end delivery, completeness or trustworthy external records |
| E02 | [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/), log record fields and timestamps | Interoperable log shape, not durable authoritative audit guarantees |
| E03 | [OpenLineage Facets & Extensibility](https://openlineage.io/docs/spec/facets/), Run, Job, Dataset and facets, observed 1.54 docs | Published lineage vocabulary, not that any example dataset was traced |
| E04 | [OpenLineage Lineage Job Facet](https://openlineage.io/docs/spec/facets/job-facets/lineage/) and [Lineage Dataset Facet](https://openlineage.io/docs/spec/facets/dataset-facets/lineage/), explicit source/target relationships | Does not prove accuracy of producer-emitted lineage or hidden column dependencies |

**Research gap:** a formal immutable audit-evidence implementation, audit control policy, authorized access review, retention obligations, signature/key rotation and tamper test require separate exact specifications and executed verification. No generic observability document alone establishes those properties. No running tracer, logging platform, lineage integration, audit service, source-code read or independent human review is asserted.

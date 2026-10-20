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
summary: "Integrated question, original scenario and transfer limits for Distributed tracing and propagation. Detailed mechanisms have separate question owners."
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
<!-- tycho-question-source:tycho.page.f921597aae854c6996459fc025a9bca3:-1 -->

# Distributed tracing: context propagation, sampling and causal limits

> **Tycho independent book draft V09/C03, 2026-10-19.** Draws on W3C Trace Context (Recommendation of 2021) and published OpenTelemetry tracing semantics. All requests, diagrams and fault scenarios are original fiction. No trace collection, backend or distributed experiment was executed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f921597aae854c6996459fc025a9bca3:0 -->
## Purpose and mission

Distributed tracing reconstructs *a selected execution story*: a request enters a component, starts work, calls another component and may later complete asynchronously. A trace can illuminate critical-path waiting, retries and failure propagation—but **it is not an authoritative record of every business effect**. A missing span may mean no work occurred, the instrumentation failed, or the sampling policy intentionally discarded it.

The architectural problem is to propagate enough correlation context across controlled boundaries while limiting overhead, data exposure, stale assumptions and accidental linkability. [Logging, audit and lineage](../c04/logs-audit-and-data-lineage.md) owns authoritative business and dataset histories; [metrics/SLOs](../c01/service-level-indicators-objectives-and-alerts.md) owns user-visible success and objectives.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Interpret traces as sampled, propagated observations with explicit trust and asynchronous boundaries.

A missing span does not prove no effect occurred, and untrusted baggage must not become an authorization decision.

The detailed pages separate the mechanisms that make this decision conditional:

- [Trace identity and causal interpretation](trace-causality.md) — What execution relationship can a span and its timing establish?
- [Propagation, sampling and untrusted context](sampling-trust.md) — What does a missing span or forged context prevent a trace from proving?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

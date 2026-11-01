---
metadata_version: 1
id: tycho.page.61097253d34b199c87b896c4fd3338c1
kind: page
parent_id: tycho.chapter.9825cb82eb2142754c638aea1ba8d845
canonical_path: book/volumes/v11-pattern-atlas/c02-api-communication/gateway-aggregation.md
title: Gateway Aggregation
topic_ids:
- api
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Gateway Aggregation.
route_hints:
  questions:
  - Should a gateway aggregate several downstream responses into one client-facing
    result, rather than making the client orchestrate every call?
  prerequisites:
  - tycho.chapter.9825cb82eb2142754c638aea1ba8d845
  related_ids:
  - tycho.chapter.9825cb82eb2142754c638aea1ba8d845
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - gateway aggregation
evidence_scope:
  source_ids:
  - src.microsoft-cloud-patterns
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Gateway Aggregation

**Identity.** Gateway Aggregation; family API and service communication; kind
integration pattern; priority core.

**Decision question.** Should a gateway aggregate several downstream responses into one
client-facing result, rather than making the client orchestrate every call?

**Good-fit conditions.** Clients need a small stable response from several owners; the
aggregation is read-mostly; per-call deadlines and partial-failure policy can be
defined; the gateway can expose which dependency failed.

**Hard contraindications.** Reject the claim when the aggregate needs strong
consistency across owners; when one slow dependency would exhaust the gateway; when
the aggregate becomes a hidden domain workflow; when partial results cannot be
represented honestly.

**Competing alternative.** Client-side composition or an API Composition layer with a
narrow contract. Reverse the choice when aggregation latency and coupling exceed the
client simplification benefit.

**Failure and recovery.** Fan-out latency, partial failure and retry amplification are
common. Recovery requires per-dependency deadlines and explicit partial results;
verify the gateway boundary and aggregation mechanics in the owner section.

**Technical owner.**
 [Gateway boundaries and
offloading](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/gateway-boundaries-and-offloading.md#gateway-aggregation)
— bounded edge boundary and aggregation mechanics.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-gateway-aggregation.2026-10-21: all nine served
headings read. Vendor pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; API Composition; Gateway Routing; Backend for
Frontend.

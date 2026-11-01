---
metadata_version: 1
id: tycho.page.0094509c037cba8c3e9030b8c8ff8963
kind: page
parent_id: tycho.chapter.9825cb82eb2142754c638aea1ba8d845
canonical_path: book/volumes/v11-pattern-atlas/c02-api-communication/reverse-proxy.md
title: Reverse Proxy
topic_ids:
- api
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Reverse Proxy.
route_hints:
  questions:
  - Should a reverse proxy terminate client connections and forward requests to backends,
    rather than exposing backends directly?
  prerequisites:
  - tycho.chapter.9825cb82eb2142754c638aea1ba8d845
  related_ids:
  - tycho.chapter.9825cb82eb2142754c638aea1ba8d845
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - reverse proxy
evidence_scope:
  source_ids:
  - src.envoy
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

# Reverse Proxy

**Identity.** Reverse Proxy; family API and service communication; kind infrastructure
pattern; priority core.

**Decision question.** Should a reverse proxy terminate client connections and forward
requests to backends, rather than exposing backends directly?

**Good-fit conditions.** Backends need connection management, TLS termination or
header normalization; the proxy can be operated with health checks and draining; backend
selection is explicit; the extra hop is acceptable.

**Hard contraindications.** Reject the claim when one backend can be exposed safely;
when the proxy would become an unowned single point; when it hides backend authorization;
when connection draining or timeout behavior cannot be tested.

**Competing alternative.** Direct backend exposure or a richer API gateway. Reverse the
choice when proxy configuration and outage cost exceed the connection-management
benefit.

**Failure and recovery.** Stale connections, proxy bypass, header trust and draining failures
are common. Recovery requires connection lifecycle tests and explicit forwarded-header and
draining policy.

**Technical owner.**
 [Gateway boundaries and
offloading](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/gateway-boundaries-and-offloading.md#reverse-proxy)
— proxy and gateway boundary; not a full Envoy operations guide.

**Sources.** [src.envoy](../../../../edition/patterns/reading-ledger.v1.json)
read record read.envoy-http-connection.2026-10-21: all fourteen served headings read. Vendor
documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; Gateway Offloading; Service Discovery; Sidecar.

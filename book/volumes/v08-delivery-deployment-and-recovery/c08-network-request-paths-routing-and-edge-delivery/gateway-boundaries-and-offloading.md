---
{
  "metadata_version": 1,
  "id": "tycho.page.99c509e133d9494fbb3080b6212b7ba7",
  "kind": "page",
  "parent_id": "tycho.chapter.8a86707018773def410689efbc79cf94",
  "canonical_path": "book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/gateway-boundaries-and-offloading.md",
  "title": "Gateway boundaries and offloading",
  "topic_ids": [
    "network-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "Which policy and connection functions may a gateway own without hiding backend authority?",
  "route_hints": {
    "questions": [
      "Which policy and connection functions may a gateway own without hiding backend authority?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.8a86707018773def410689efbc79cf94"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "gateway",
      "proxy",
      "offloading",
      "aggregation",
      "authorization"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.http-semantics",
      "src.owasp-rest-enrichment"
    ],
    "claim_ids": [],
    "status": "source-linked",
    "notes": "Exact selected passages and source limitations are recorded in the page ledger and dated enrichment inspection record. Synthetic protocols are original design reasoning."
  },
  "content_review": {
    "status": "self-checked",
    "reviewed_at": "2026-10-22",
    "reviewer": "Tycho agent; execution gates pending",
    "proof_uri": null
  },
  "authored_at": "2026-10-22",
  "updated_at": "2026-10-22",
  "source_inspection_date": "2026-10-20",
  "content_verified_at": null
}
---

# Gateway boundaries and offloading

**Owning question:** Which policy and connection functions may a gateway own without hiding
backend authority?

A gateway can centralize routing, quotas and common policy. That concentration is useful only
when the trust boundary is explicit and the backend still enforces the authority it owns.

> **Pattern atlas:**
> [API Gateway](../../v11-pattern-atlas/c02-api-communication/README.md#api-gateway) — decision conditions and contraindications.
> [Gateway Aggregation](../../v11-pattern-atlas/c02-api-communication/README.md#gateway-aggregation) — decision conditions and contraindications.
> [Gateway Offloading](../../v11-pattern-atlas/c02-api-communication/README.md#gateway-offloading) — decision conditions and contraindications.
> [Reverse Proxy](../../v11-pattern-atlas/c02-api-communication/README.md#reverse-proxy) — decision conditions and contraindications.

## API Gateway

A gateway can centralize routing, quotas and common policy. It is a trusted intermediary only
for the functions it actually enforces. Keep resource authorization at the boundary owning
the resource, with documented delegation if a central decision service is used. Removing
every backend check creates a privileged bypass path unless network and identity contracts
actually exclude it.

**Failure and alternative.** Gateway bypass, configuration drift, a stale route and an outage
that blocks every backend are common. Keep backend authorization, test the network path that
excludes the gateway and version gateway policy. A BFF, a service-mesh sidecar or direct
backend exposure with an explicit identity contract may be preferable when the gateway adds a
shared bottleneck without a required central policy.

**Limits.** A gateway cannot certify object ownership or replace backend authorization.
A bypass path, a compromised policy plane or an unversioned configuration can defeat the
edge. Keep gateway policy versioned, tested and observable, and treat a gateway outage as
its own failure domain rather than assuming every backend remains reachable.

## Gateway Aggregation

A gateway aggregation layer calls several downstream services for one client request and
returns a single composed response. Each downstream call must carry its own deadline, and a
partial failure must be represented explicitly in the aggregate response.

One slow participant delays the whole response, and a silent omission hides incomplete data;
fan out in parallel with per-call budgets and mark missing parts. Client-side composition or a
backend for frontend keeps aggregation closer to the client; use gateway aggregation when the
composition is shared and the gateway is already the trust boundary.

## Gateway Offloading

An edge can terminate TLS, validate tokens, compress, cache or enforce quotas before
forwarding. Offloading changes the trust boundary: downstream must receive an authenticated
identity from a trusted intermediary and still enforce resource authorization. Header
spoofing, confused-deputy paths and a proxy that becomes the only authorization point are
common failures. A service-mesh sidecar, application-level authorization or direct
pass-through may be preferable when the edge cannot attest identity.

## Reverse Proxy

A reverse proxy accepts client connections and forwards them to a selected backend, hiding
topology and optionally terminating TLS. It must define route identity, peer authentication,
forwarded-header policy and backend failure behavior. Proxy bypass, stale routes and trusting
a client-supplied identity header are common. Direct service discovery, a gateway/BFF or a
mesh sidecar may be preferable when the proxy adds a shared bottleneck without a required
policy function.

## Failure, recovery and acceptance

A control-plane outage should not silently remove authentication or open a bypass. Test an
untrusted direct-backend request, stale route, forged forwarded context and gateway outage;
record denied versus unavailable outcomes, not only handshake success.

## Navigation

Parent: [network chapter](README.md). Previous: [TLS trust boundaries](tls-gateway-boundaries.md).
Next: [edge caching](edge-cache-origin.md).

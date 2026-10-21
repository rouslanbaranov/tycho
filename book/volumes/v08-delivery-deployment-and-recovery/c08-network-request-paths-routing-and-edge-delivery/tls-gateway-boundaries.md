---
{
  "metadata_version": 1,
  "id": "tycho.page.37a28a568f7e987941749e198c03439a",
  "kind": "page",
  "parent_id": "tycho.chapter.8a86707018773def410689efbc79cf94",
  "canonical_path": "book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/tls-gateway-boundaries.md",
  "title": "TLS termination, gateways and trusted identity",
  "topic_ids": [
    "network-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "Which identity and confidentiality boundary does each proxy hop establish?",
  "route_hints": {
    "questions": [
      "Which identity and confidentiality boundary does each proxy hop establish?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.8a86707018773def410689efbc79cf94"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "which",
      "identity",
      "confidentiality",
      "boundary",
      "does",
      "each",
      "proxy",
      "establish"
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
    "reviewed_at": "2026-10-20",
    "reviewer": "Codex enrichment author; execution gates pending",
    "proof_uri": null
  },
  "authored_at": "2026-10-20",
  "updated_at": "2026-10-20",
  "source_inspection_date": "2026-10-20",
  "content_verified_at": null
}
---

# TLS termination, gateways and trusted identity

**Owning question:** Which identity and confidentiality boundary does each proxy hop establish?


> **Pattern atlas:**
> [API Gateway](../../v11-pattern-atlas/c02-api-communication/README.md#api-gateway) — decision conditions and contraindications.
> [Gateway Aggregation](../../v11-pattern-atlas/c02-api-communication/README.md#gateway-aggregation) — decision conditions and contraindications.
> [Gateway Offloading](../../v11-pattern-atlas/c02-api-communication/README.md#gateway-offloading) — decision conditions and contraindications.
> [Reverse Proxy](../../v11-pattern-atlas/c02-api-communication/README.md#reverse-proxy) — decision conditions and contraindications.

## The trust question

Draw each hop and name its authenticated peer. In a client → edge → gateway → application path, the certificate seen by the client normally identifies the TLS endpoint it contacted. It does not by itself authenticate the final application process or authorize a particular object. If encryption terminates at a proxy, the next connection needs its own declared protection.

RFC 9110 section 4.3.4 describes certificate verification for HTTPS. OWASP's REST guidance calls for HTTPS, endpoint access control and validated token claims. Neither source certifies an arbitrary proxy configuration.

**Offloading mechanism.** An edge can terminate TLS, validate tokens, compress, cache or
enforce quotas before forwarding. Offloading changes the trust boundary: downstream must
receive an authenticated identity from a trusted intermediary and still enforce resource
authorization. Header spoofing, confused-deputy paths and a proxy that becomes the only
authorization point are common failures. A service-mesh sidecar, application-level
authorization or direct pass-through may be preferable when the edge cannot attest identity.

**Reverse-proxy mechanism.** A reverse proxy accepts client connections and forwards them to
a selected backend, hiding topology and optionally terminating TLS. It must define route
identity, peer authentication, forwarded-header policy and backend failure behavior.
Proxy bypass, stale routes and trusting a client-supplied identity header are common.
Direct service discovery, a gateway/BFF or a mesh sidecar may be preferable when the proxy
adds a shared bottleneck without a required policy function.

## Original fictional boundary contract

A private image catalogue uses a public edge and an internal service. Its contract requires: only permitted callers see an image; client-facing names match validated certificates; forwarded identity comes only from an authenticated trusted intermediary; and internal policy cannot be bypassed by calling a backend directly.

| Boundary | Proposed enforcement | Failure to reject |
|---|---|---|
| Client to edge | Validated server identity and protected channel | Accept any certificate because traffic is encrypted |
| Edge to gateway | Deliberate peer authentication and allowed ingress | Trust a caller-supplied identity header |
| Gateway to application | Integrity-protected principal/context or independently validated token | Treat network location as object permission |
| Application to data | Resource-level decision with tenant and action | Use a storage key as proof of authorization |

**API-gateway failure and alternative.** Gateway bypass, configuration drift, a stale route
and an outage that blocks every backend are common. Keep backend authorization, test the
network path that excludes the gateway and version gateway policy. A BFF, a service-mesh
sidecar or direct backend exposure with an explicit identity contract may be preferable when
the gateway adds a shared bottleneck without a required central policy.
| Administrative policy path | Separate authority and controlled changes | Let ordinary request data alter trusted routes |

A gateway can centralize routing, quotas and common policy. Keep resource authorization at the boundary owning the resource, with documented delegation if a central decision service is used. Removing every backend check creates a privileged bypass path unless network and identity contracts actually exclude it.

## Normal rotation and compromise differ

For routine certificate or signing-key replacement, plan overlap across producers, verifiers, caches and long-lived connections. Verify the new chain before making it the only accepted path. During compromise, continued acceptance of an old key may violate the threat contract; availability and revocation need an explicit incident decision. See [key lifecycle](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/object-credentials.md#key-rotation-revocation-and-unavailable-authorities).

**Original counterexample:** a proxy strips an external header named principal but leaves a second alternate header consumed by one backend. Both hops use TLS; the confused identity still reaches the application. Enumerate all accepted identity inputs and reject ambiguity rather than adding another encryption layer.

## Failure, recovery and acceptance

A control-plane outage should not silently remove authentication or refresh unknown credentials indefinitely. Determine whether already established sessions and locally verifiable credentials can continue within their original validity and policy horizon. New unknown keys and privileged mutations need their own failure decision.

Proposed tests include an untrusted direct-backend request, stale certificate chain, wrong audience/issuer, forged forwarded context, revoked object access and policy distribution delay. Record denied versus unavailable outcomes, not only a handshake success rate.

Choose a simpler reverse proxy when it meets these contracts. Adopt service-mesh identity when the number and dynamism of service relationships justify its operational cost; a mesh name is not an assurance argument.

## Evidence and navigation

Selected public passages inspected 2026-10-20: [HTTPS authority](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.3.4) and [OWASP HTTPS, access control and JWT sections](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html). The table and counterexample are original unexecuted design analysis.

Parent: [network chapter](README.md). Previous: [connection fate](connections-draining.md). Next: [edge caching](edge-cache-origin.md). Related: [threat identity](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/threat-identity.md).

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Gateway Aggregation

A gateway aggregation layer calls several downstream services for one client request and returns a
single composed response. Each downstream call must carry its own deadline, and a partial failure
must be represented explicitly in the aggregate response.

One slow participant delays the whole response, and a silent omission hides incomplete data; fan out
in parallel with per-call budgets and mark missing parts. Client-side composition or a backend for
frontend keeps aggregation closer to the client; use gateway aggregation when the composition is
shared and the gateway is already the trust boundary.

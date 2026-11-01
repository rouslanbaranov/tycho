---
metadata_version: 1
id: "tycho.page.10b081ee27734830924e7223c5f64165"
kind: "page"
parent_id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/gateway-routing.md"
title: "Gateway Routing"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Gateway Routing with bounded owner evidence."
route_hints:
  questions:
    - >-
      Should a gateway route requests to the responsible backend using an
      explicit contract rather than exposing every backend address to clients?
  prerequisites:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  related_ids:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "gateway routing"
    - "edge routing"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
    - "src.kubernetes"
    - "src.envoy"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# Gateway Routing

**Identity.** Gateway Routing; family API and service communication; kind integration
pattern; priority core.

**Decision question.** Should a gateway route requests to the responsible backend using
an explicit contract rather than exposing every backend address to clients?

**Good-fit conditions.** Multiple backends or versions exist; routing rules are stable
enough to own; route selection, service membership and backend endpoints are separable;
discovery and health signals are available; the gateway can resolve version and tenant
routing without guessing.

**Hard contraindications.** Reject the claim when clients can resolve one stable
backend; when routes are ad hoc and unversioned; when routing depends on unchecked
client-supplied identifiers; when a route change cannot be rolled back.

**Competing alternative.** Direct client-to-backend calls, a simpler reverse proxy,
client-side discovery or a BFF. Azure's pattern says gateway routing may not suit a simple
application and warns that the gateway can become a single point of failure; Envoy
describes edge reverse-proxy handling and a service-to-service mesh. Reverse the choice
when routing logic becomes domain logic or the gateway cannot observe backend health. The
choice rule is Tycho guidance.

**Failure and recovery.** Stale routes, ambiguous matches, wrong-version selection, no-match
behavior and bypass around the gateway are common. Recovery requires route versioning,
precedence tests and observability.

**Technical owner.** [Gateway Routing](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/routing-and-health.md#gateway-routing) — routing and backend selection; not a dedicated gateway routing product guide.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-gateway-routing.2026-10-21: all eleven served headings read.
Kubernetes "Ingress" (`read.k8s-ingress.2026-11-01`), Kubernetes "Gateway API"
(`read.k8s-gateway-api.2026-11-01`) and Envoy "HTTP routing"
(`read.envoy-http-routing.2026-11-01`) are bound for the invariant and alternative;
exact quotes and revisions are in this card and the reading ledger. Vendor and project
documentation, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; Service Discovery; Reverse Proxy; Gateway
Aggregation.

## Evidence and limits

Azure, "Gateway Routing" (`read.microsoft-gateway-routing.2026-10-21`, revision
`c2c7ecda427fb76fa98431ccfab5aa20c610e1fc9d2485293625da7e2b435b4f`): "The complexity
of registering and unregistering service instances is encapsulated in the gateway." It
"might not be suitable when you have a simple application that uses only one or two
services" and warns that the gateway "can introduce a single point of failure" and "a
bottleneck".

Kubernetes, "Ingress" (`read.k8s-ingress.2026-11-01`, revision
`43cd6851dcbfb321feee973e676f9c2b6369cdc328a3b4d1279a0c779e7cd688`): "Ingress exposes
HTTP and HTTPS routes from outside the cluster to services within the cluster." and "A
Kubernetes Service that identifies a set of Pods using label selectors." It also lists
`Service.Type=LoadBalancer` and `Service.Type=NodePort` as ways to expose a Service
"that don't directly involve the Ingress resource".

Kubernetes, "Gateway API" (`read.k8s-gateway-api.2026-11-01`, revision
`309a8a58019953a763e9eb7f6251cdde02772aab8b4b3e7acc42a5bdd7ccc3ff`): the DNS resolver
learns "a mapping to one or more IP addresses associated with the Gateway"; the reverse
proxy uses the Host header to match the attached HTTPRoute; and a Service backend may be
represented "as a Service IP or the backing EndpointSlices of the Service".

Envoy, "HTTP routing" (`read.envoy-http-routing.2026-11-01`, revision
`d16659a8025833f15c330a33909c59f29b2de1de5b262993e42d63e23725491c`): the router "matches
it to an upstream cluster, acquires a connection pool to a host in the upstream cluster,
and forwards the request", for "handling edge traffic (traditional reverse proxy request
handling)" as well as a service-to-service mesh.

The four-layer separation of externally resolved name, service membership, connection
destination and selected backend, and the preference rule, are Tycho synthesis. The pages
describe mechanisms; none measures this page's route table or proves a preference.

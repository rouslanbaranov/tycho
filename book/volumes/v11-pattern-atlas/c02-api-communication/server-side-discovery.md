---
metadata_version: 1
id: "tycho.page.3021b4dfae7d4c9e9b902581898c6413"
kind: "page"
parent_id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/server-side-discovery.md"
title: "Server-Side Discovery"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Server-Side Discovery; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should a proxy or load balancer own service lookup and backend selection for the caller?"
  prerequisites:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  related_ids:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "No owner acceptance is claimed for this card."
  keywords:
    - "pattern atlas"
    - "server-side discovery"
    - "service discovery"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
    - "src.envoy"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "independent-reviewed"
  reviewed_at: "2026-11-01"
  reviewer: "DeepSeek Reviewer"
  proof_uri: "https://github.com/rouslanbaranov/tycho/blob/5649803b/authoring/ai-reviews/2026-10-30-server-side-deepseek.md"
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: "2026-11-01"
---

# Server-Side Discovery

**Identity.** Server-Side Discovery; family API and service communication; kind
discovery pattern; priority core.

**Decision question.** Should a proxy or load balancer own service lookup and backend
selection for the caller?

**Good-fit conditions.** Clients should stay simple; the intermediary can observe
health and membership, and its discovery view can be eventually consistent, though a
removed-but-healthy backend can remain routable until convergence or a drain completes
(Tycho guidance); selection policy is centrally owned; the
extra hop and proxy lifecycle are acceptable.

**Hard contraindications.** Reject the claim when the intermediary becomes an unowned
single point; when it cannot observe backend health; when clients need a selection
policy the proxy cannot express; when the extra hop violates a hard latency budget.

**Competing alternative.** Client-side discovery is the bound alternative. Tycho guidance:
static endpoints, a service mesh or direct endpoint configuration may be simpler when
membership changes are rare. Reverse when proxy blast radius and operational cost exceed
the client simplification benefit.

**Failure and recovery.** The proxy is a shared dependency; replicate it for availability and
capacity. Envoy's "On eventually consistent service discovery" section states the routing
limit:

> If a host continues to pass health check even after becoming absent from the discovery data,
> Envoy will still route.

Active health checks remove unhealthy backends, not a removed-but-healthy backend; that host
remains routable until discovery converges or a drain completes. Tycho guidance, not a source
claim: bound retries, expose a degraded path, and plan proxy failover; the source gives no
propagation bound, drain procedure or health-check interval.

**Technical owner.** [Server-Side Discovery](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/discovery-balancing.md#server-side-discovery) — discovery and selection; server-side specifics are bounded to the linked section.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-server-discovery.2026-10-21: Server-side service
discovery, sections "Context", "Problem", "Forces", "Solution", "Examples", "Resulting
context", "Related patterns". Pattern page, not a benchmark.

The invariant is bound to
[src.envoy](../../../../edition/patterns/reading-ledger.v1.json) read record
read.envoy-service-discovery-consistency.2026-10-29, section "On eventually consistent
service discovery", revision
`f07699d00554ee3b3cf13d6644b115645ba5efe4258cbb5331471bbdd0a59e6e`: a host that keeps
passing health checks can still receive traffic after discovery removes it. The record
pins the 2026-10-29 served page; it covers eventual consistency and health checking, not
a propagation bound or drain procedure.

**Decision state.** applicable-under-conditions.

**Related entries.** Service Discovery; Client-Side Discovery; Gateway Routing; API
Gateway.

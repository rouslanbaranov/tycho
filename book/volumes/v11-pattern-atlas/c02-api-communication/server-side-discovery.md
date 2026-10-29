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
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
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
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Server-Side Discovery

**Identity.** Server-Side Discovery; family API and service communication; kind
discovery pattern; priority core.

**Decision question.** Should a proxy or load balancer own service lookup and backend
selection for the caller?

**Good-fit conditions.** Clients should stay simple; the intermediary can observe
health and membership, and its discovery view can be eventually consistent because
active health checks remove stale backends; selection policy is centrally owned; the
extra hop and proxy lifecycle are acceptable.

**Hard contraindications.** Reject the claim when the intermediary becomes an unowned
single point; when it cannot observe backend health; when clients need a selection
policy the proxy cannot express; when the extra hop violates a hard latency budget.

**Competing alternative.** Client-side discovery or static endpoints. Reverse the
choice when proxy blast radius and operational cost exceed the client simplification
benefit.

**Failure and recovery.** Proxy outage, stale membership, retry amplification and a shared
proxy bottleneck are common. Envoy's "On eventually consistent service discovery" section
states the routing limit:

> If a host continues to pass health check even after becoming absent from the discovery data,
> Envoy will still route.

Active health checking is the documented mitigation. Expose a degraded path and bound retries;
the source gives no propagation bound or health-check interval, so those remain Tycho guidance.

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

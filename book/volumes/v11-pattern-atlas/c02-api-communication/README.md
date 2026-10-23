---
metadata_version: 1
id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/README.md"
title: "V11/C02 — API and service communication"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 12 C02 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which API and discovery patterns fit the trust boundary?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.e996607f707421ca388796732547cafd"
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "api and service communication"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
    - "src.microsoft-cloud-patterns"
    - "src.envoy"
  claim_ids: []
  status: "source-linked"
  notes: "12 cards cite read units; owner links are bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-21"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# V11/C02 — API and service communication

**Owning question:** Which API and discovery patterns fit the trust boundary?

## Purpose and mission

This chapter is the atlas entry point for **API and service communication**. It owns
the conditional decision route for 12 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 12 entries have a self-checked card. Their owner sections are bounded: a gateway
page may own the edge boundary and aggregation mechanics without owning every BFF
mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### API Gateway

**Identity.** API Gateway; family API and service communication; kind integration
pattern; priority core.

**Decision question.** Should external clients enter through a managed gateway that
owns routing, authentication and cross-cutting edge policy?

**Good-fit conditions.** Multiple clients or backends share edge concerns; routing,
TLS, authentication or rate policy must be consistent; the gateway can be operated and
observed as a critical component; backend authority remains explicit.

**Hard contraindications.** Reject the claim when one simple client can call one
backend directly; when the gateway would become an unowned single point of failure;
when it hides domain authorization in the backend; when every request needs a unique
policy that the gateway cannot safely express.

**Competing alternative.** A reverse proxy with a narrow edge contract, or direct
backend exposure with client-side policy. Reverse the choice when gateway complexity
and outage blast radius exceed the shared edge benefit.

**Failure and recovery.** Gateway bypass, configuration drift, stale routes, confused
authentication and an outage blocking every backend are common. Keep backend authorization,
test the bypass path and version gateway policy.

**Technical owner.** [Gateway boundaries and offloading](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/gateway-boundaries-and-offloading.md#api-gateway) — edge identity and gateway boundary; not a full API management specification.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-api-gateway.2026-10-21: API Gateway, sections
"Context", "Problem", "Forces", "Solution", "Variation: Backends for frontends",
"Examples", "Resulting context", "Related patterns". Pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Gateway Routing; Gateway Aggregation; Gateway Offloading; Reverse
Proxy.

### Gateway Routing

**Identity.** Gateway Routing; family API and service communication; kind integration
pattern; priority core.

**Decision question.** Should a gateway route requests to the responsible backend using
an explicit contract rather than exposing every backend address to clients?

**Good-fit conditions.** Multiple backends or versions exist; routing rules are stable
enough to own; discovery and health signals are available; the gateway can resolve
version and tenant routing without guessing.

**Hard contraindications.** Reject the claim when clients can resolve one stable
backend; when routes are ad hoc and unversioned; when routing depends on unchecked
client-supplied identifiers; when a route change cannot be rolled back.

**Competing alternative.** Direct client-to-backend calls or a simpler reverse proxy.
Reverse the choice when routing logic becomes domain logic or the gateway cannot observe
backend health.

**Failure and recovery.** Stale routes, ambiguous matches, wrong-version selection, no-match
behavior and bypass around the gateway are common. Recovery requires route versioning,
precedence tests and observability.

**Technical owner.** [Gateway Routing](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/routing-and-health.md#gateway-routing) — routing and backend selection; not a dedicated gateway routing product guide.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-gateway-routing.2026-10-21: Gateway Routing pattern,
sections "Context and problem", "Solution", "Multiple disparate services", "Multiple
instances of the same service", "Multiple versions of the same service", "Issues and
considerations", "When to use this pattern", "Workload design", "Example". Vendor
pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; Service Discovery; Reverse Proxy; Gateway
Aggregation.

### Gateway Aggregation

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

**Technical owner.** [Gateway boundaries and offloading](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/gateway-boundaries-and-offloading.md#gateway-aggregation) — bounded edge boundary and aggregation mechanics.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-gateway-aggregation.2026-10-21: Gateway Aggregation pattern,
sections "Context and problem", "Solution", "Problems and considerations", "When to use
this pattern", "Workload design", "Example". Vendor pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; API Composition; Gateway Routing; Backend for
Frontend.

### Gateway Offloading

**Identity.** Gateway Offloading; family API and service communication; kind integration
pattern; priority core.

**Decision question.** Should reusable cross-cutting functions be moved to a gateway
without moving domain authority there?

**Good-fit conditions.** TLS, authentication, rate policy or compression is shared
across backends; the gateway can enforce and observe the function; backend authority
and object-level authorization remain explicit.

**Hard contraindications.** Reject the claim when the offloaded function needs domain
state; when the gateway becomes the only authorization check; when a gateway outage
blocks all work; when the team cannot own gateway configuration.

**Competing alternative.** A library in each backend or a narrower reverse proxy.
Reverse the choice when gateway configuration drift or blast radius exceeds the reuse
benefit.

**Failure and recovery.** Misconfigured TLS, stale policy, header spoofing and a gateway that
becomes the only authorization point are common. Recovery requires configuration tests and
an explicit trust boundary with downstream authorization.

**Technical owner.** [Gateway boundaries and offloading](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/gateway-boundaries-and-offloading.md#gateway-offloading) — edge functions and trusted identity; not a complete offloading catalogue.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-gateway-offloading.2026-10-21: Gateway Offloading pattern,
sections "Context and problem", "Solution", "Problems and considerations", "When to use
this pattern", "Workload design", "Example", "Application Gateway with TLS offloading",
"Supporting technologies". Vendor pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; Reverse Proxy; Gatekeeper; Gateway Routing.

### Backend for Frontend (BFF)

**Identity.** Backend for Frontend; alias BFF; family API and service communication;
kind integration pattern; priority core.

**Decision question.** Should each client population get a tailored server contract,
rather than share one general-purpose API?

**Good-fit conditions.** Client populations have materially different interaction
needs; a team can own each BFF; shared domain services remain authoritative; duplicated
client-specific composition is acceptable.

**Hard contraindications.** Reject the claim when one client contract is adequate; when
BFFs would duplicate domain logic; when no team owns a BFF lifecycle; when the split
multiplies deployments without a measured client benefit.

**Competing alternative.** One API with versioned representations or a gateway
aggregation. Reverse the choice when BFF maintenance and duplication exceed the client
fit benefit.

**Failure and recovery.** Contract drift across BFFs and duplicated logic are common.
Recovery requires shared domain contracts and per-BFF observability; verify the API
contract boundary in the owner section.

**Technical owner.** [HTTP and RPC contracts: compatibility, deadlines and retry safety](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md#backend-for-frontend-bff) — API contract ownership; BFF tailoring is not a dedicated section.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-bff.2026-10-21: Backends for Frontends pattern, sections
"Context and problem", "Solution", "Problems and considerations", "When to use this
pattern", "Workload design", "Example", "Design". Vendor pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; Gateway Aggregation; API Composition; Reverse Proxy.

### API Composition

**Identity.** API Composition; family API and service communication; kind integration
pattern; priority core.

**Decision question.** Should an in-memory composition layer assemble a response from
several service owners, rather than forcing one owner to duplicate all data?

**Good-fit conditions.** The query is read-mostly; per-owner calls have bounded
deadlines; partial results can be represented; composition logic is owned and tested;
the response does not require a distributed transaction.

**Hard contraindications.** Reject the claim when strong consistency is required; when
fan-out latency exceeds the client budget; when composition needs writes across owners;
when one service can answer the query directly without duplicating authority.

**Competing alternative.** A materialized read model, CQRS projection or direct
service query. Reverse the choice when composition latency and partial-failure
complexity exceed the duplication alternative.

**Failure and recovery.** Slow dependencies, partial results and retry amplification are
common. Recovery requires deadlines and explicit degradation; verify the API contract
boundary in the owner section.

**Technical owner.** [HTTP and RPC contracts: compatibility, deadlines and retry safety](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md#api-composition) — contract boundary; composition is not a dedicated section.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-api-composition.2026-10-21: API Composition, sections
"Context", "Problem", "Solution", "Example", "Resulting context", "Related patterns".
Pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Backend for Frontend; Gateway Aggregation; CQRS; Self-Contained
Service.

### Reverse Proxy

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

**Technical owner.** [Gateway boundaries and offloading](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/gateway-boundaries-and-offloading.md#reverse-proxy) — proxy and gateway boundary; not a full Envoy operations guide.

**Sources.** [src.envoy](../../../../edition/patterns/reading-ledger.v1.json)
read record read.envoy-http-connection.2026-10-21: HTTP connection management, sections
"HTTP protocols", "HTTP lifecycle", "HTTP header sanitizing", "Route table
configuration", "Retry plugin configuration", "Internal redirects", "Timeouts". Vendor
documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; Gateway Offloading; Service Discovery; Sidecar.

### Service Discovery

**Identity.** Service Discovery; family API and service communication; kind
infrastructure pattern; priority core.

**Decision question.** Should callers resolve backend instances through a discovery
mechanism rather than static addresses?

**Good-fit conditions.** Instances change frequently; membership and health are
observable; stale membership can be detected; callers can handle resolution failure and
backoff; the routing contract is owned.

**Hard contraindications.** Reject the claim when a small static endpoint is stable;
when discovery would publish stale or unauthorized endpoints; when clients cannot
maintain backoff and observability; when discovery is treated as authorization.

**Competing alternative.** Static endpoints, DNS or a single proxy. Reverse the choice
when discovery control-plane cost and stale-state risk exceed the change rate.

**Failure and recovery.** Stale membership, discovery outage and fast-error attraction
are common. Recovery requires last-known-good policy and health checks; verify the
routing contract in the owner section.

**Technical owner.** [Service Discovery](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/discovery-balancing.md#service-discovery) — discovery and selection; not a full control-plane implementation.

**Sources.** [src.envoy](../../../../edition/patterns/reading-ledger.v1.json)
read record read.envoy-service-discovery.2026-10-21: Service discovery, sections
"Supported service discovery types", "Static", "Strict DNS", "Logical DNS", "Original
destination", "Endpoint discovery service (EDS)", "Custom cluster", "On eventually
consistent service discovery". Vendor documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Client-Side Discovery; Server-Side Discovery; Gateway Routing;
Reverse Proxy.

### Client-Side Discovery

**Identity.** Client-Side Discovery; family API and service communication; kind
discovery pattern; priority advanced.

**Decision question.** Should the caller own service lookup and backend selection,
rather than delegating both to an intermediary?

**Good-fit conditions.** Clients can maintain membership, backoff and observability;
the client platform is controlled; selection policy is stable; stale membership can be
detected and bounded.

**Hard contraindications.** Reject the claim when clients cannot be upgraded; when
discovery logic would be duplicated across many runtimes; when the client cannot observe
backend health; when selection policy must be centrally governed.

**Competing alternative.** Server-side discovery through a proxy or load balancer.
Reverse the choice when client complexity and inconsistent policies exceed the
resolution benefit.

**Failure and recovery.** Registry outage, stale caches, divergent client policies and
retry storms are common. Keep a last-known set for reads, detect staleness and bound retries.

**Technical owner.** [Client-Side Discovery](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/discovery-balancing.md#client-side-discovery) — discovery and selection; client-specific policy is bounded to the linked section.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-client-discovery.2026-10-21: Client-side service
discovery, sections "Context", "Problem", "Forces", "Solution", "Examples", "Resulting
context", "Related patterns". Pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Service Discovery; Server-Side Discovery; Gateway Routing; Reverse
Proxy.

### Server-Side Discovery

**Identity.** Server-Side Discovery; family API and service communication; kind
discovery pattern; priority core.

**Decision question.** Should a proxy or load balancer own service lookup and backend
selection for the caller?

**Good-fit conditions.** Clients should stay simple; the intermediary can observe
health and membership; selection policy is centrally owned; the extra hop and proxy
lifecycle are acceptable.

**Hard contraindications.** Reject the claim when the intermediary becomes an unowned
single point; when it cannot observe backend health; when clients need a selection
policy the proxy cannot express; when the extra hop violates a hard latency budget.

**Competing alternative.** Client-side discovery or static endpoints. Reverse the
choice when proxy blast radius and operational cost exceed the client simplification
benefit.

**Failure and recovery.** Proxy outage, stale membership, retry amplification and a shared
proxy bottleneck are common. Health-check backends, expose a degraded path and bound retries.

**Technical owner.** [Server-Side Discovery](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/discovery-balancing.md#server-side-discovery) — discovery and selection; server-side specifics are bounded to the linked section.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-server-discovery.2026-10-21: Server-side service
discovery, sections "Context", "Problem", "Forces", "Solution", "Examples", "Resulting
context", "Related patterns". Pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Service Discovery; Client-Side Discovery; Gateway Routing; API
Gateway.

### Asynchronous Request-Reply

**Identity.** Asynchronous Request-Reply; family API and service communication; kind
integration pattern; priority core.

**Decision question.** Should a client submit work and later fetch a result, rather than
hold one synchronous request open?

**Good-fit conditions.** Work exceeds a request deadline; durable acceptance and
recovery are required; clients can poll or receive a callback; operation identity and
cleanup are defined.

**Hard contraindications.** Reject the claim when a synchronous call reliably meets the
deadline; when the client cannot handle pending state; when result retention and
cleanup have no owner; when duplicate submission cannot be made safe by an idempotency
key or reconciliation.

**Competing alternative.** Synchronous request-reply with a bounded deadline. Reverse
the choice when durable work and client polling add more complexity than the latency
benefit.

**Failure and recovery.** Lost replies, duplicate submissions and orphaned jobs are
common. Recovery requires stable operation IDs and status cleanup; verify the async
contract in the owner section.

**Technical owner.** [Asynchronous APIs and streaming: demand, deadlines and cancellation](../../v03-execution-concurrency-and-flow-control/c04-asynchronous-apis-and-streaming/asynchronous-apis-streaming-and-cancellation.md#asynchronous-request-reply) — async demand and cancellation; not a full request-reply implementation.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-async-request-reply.2026-10-21: Asynchronous Request-Reply
pattern, sections "Context and problem", "Solution", "Problems and considerations",
"When to use this pattern", "Workload design", "Example". Vendor pattern page, not a
benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; API Composition; Retry with Idempotency; Deadline
Propagation.

### Gatekeeper

**Identity.** Gatekeeper; family API and service communication; kind security pattern;
priority advanced.

**Decision question.** Should a narrow gatekeeper validate and shape requests before
they reach a sensitive backend, rather than exposing the backend directly?

**Good-fit conditions.** A small validation surface can reject malformed or
unauthorized requests; the gatekeeper can authenticate and forward trusted context;
the backend retains object-level authorization; the gatekeeper is highly available.

**Hard contraindications.** Reject the claim when the gatekeeper would become the only
authorization check; when it forwards unchecked identity or tenant headers; when its
outage blocks all access; when validation logic needs backend domain state.

**Competing alternative.** Backend-side validation and authorization, or an API gateway
with a narrow policy. Reverse the choice when gatekeeper complexity and blast radius
exceed the reduced attack surface.

**Failure and recovery.** False trust in forwarded identity, stale policy and gatekeeper
outage are common. Recovery requires explicit trust boundaries and backend checks;
verify the authorization boundary in the owner section.

**Technical owner.** [Authorization boundaries and multitenancy: domain ownership and isolation](../../v02-application-boundaries-and-contracts/c07-authorization-boundaries-and-multitenancy/authorization-boundaries-and-multitenancy.md#gatekeeper) — authorization boundary; gatekeeper mechanics are bounded to the linked section.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-gatekeeper.2026-10-21: Gatekeeper pattern, sections "Context
and problem", "Solution", "Problems and considerations", "When to use this pattern",
"Workload design", "Example". Vendor pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; Gateway Offloading; Zero Trust Architecture; Valet
Key.

## Chapter result and counterexample

Twelve cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: an API gateway that validates a token but forwards an untrusted tenant
header to every backend is not evidence for the gatekeeper or offloading cards.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C01](../c01-application-boundaries/README.md).
- Next: [V11/C03](../c03-messaging-integration/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 12 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern manuscripts.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.

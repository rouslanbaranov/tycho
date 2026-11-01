---
{
  "metadata_version": 1,
  "id": "tycho.page.07904f22ca8249069cedc8c2e1140630",
  "kind": "page",
  "parent_id": "tycho.chapter.8a86707018773def410689efbc79cf94",
  "canonical_path": "book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/routing-and-health.md",
  "title": "Request routing and health signals",
  "topic_ids": [
    "network-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "Which route selects a backend, and which health signal may admit or remove it?",
  "route_hints": {
    "questions": [
      "Which route selects a backend, and which health signal may admit or remove it?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.8a86707018773def410689efbc79cf94"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "route",
      "backend",
      "health",
      "readiness",
      "liveness",
      "gateway"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.sre-frontend-enrichment",
      "src.sre-balancing-enrichment"
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
  "updated_at": "2026-10-30",
  "source_inspection_date": "2026-10-21",
  "content_verified_at": null
}
---

# Request routing and health signals

**Owning question:** Which route selects a backend, and which health signal may admit or remove it?

A route decides where a request may go; a health signal decides whether an instance is
eligible to receive it. Collapsing both into "the load balancer is healthy" hides stale
routes, mixed readiness semantics and a backend that answers quickly but cannot do useful
work.

> **Pattern atlas:**
> [Gateway Routing](../../v11-pattern-atlas/c02-api-communication/README.md#gateway-routing) — decision conditions and contraindications.

> **Pattern atlas:**
> [Health Endpoint Monitoring](../../v11-pattern-atlas/c07-resilience/README.md#health-endpoint-monitoring) — decision conditions and contraindications.

## The routing contract

A caller needs a route to an eligible instance, not a timeless list of machines. Describe
separately the externally resolved name, the service membership view, the connection
destination and the backend selected for each request. A global route may choose a location;
an internal selector chooses a process. A stale membership view can outlive a rollout.

**Gateway-routing mechanism.** A gateway matches request attributes to a declared route and
backend, then applies its policy. Routes need stable identity, precedence, versioning and an
explicit no-match behavior; the selected backend still needs its own authorization and
failure budget. Stale routes, ambiguous matches and bypass around the gateway are common.
A reverse proxy, client-side discovery or a BFF may be preferable when routing policy is
simple or the gateway would become a hidden shared dependency.

The two SRE load-balancing chapters distinguish global routing from backend selection. Their
examples support the need to examine locality, workload and selection policy; they do not
prescribe one algorithm for every service.

## Health endpoint monitoring

**Health endpoint monitoring.** A startup probe answers "has initialization finished";
readiness answers "may this instance receive new work"; liveness answers "must the process be
restarted". Tycho guidance: they must not be collapsed into one endpoint. External monitoring should also
observe user-level success and dependency state, because a green liveness probe does not
prove readiness, correct routing or a healthy dependency.

Define startup eligibility, readiness, draining and permanent removal separately. A liveness
endpoint should not restart every healthy process because one shared dependency is
unavailable.

**Failure and recovery (Tycho synthesis).** A shared dependency failure can fail every probe
and cause mass ejection or restart; a cached "healthy" answer can keep sending traffic to a
draining instance. The parts are documented. Kubernetes says a pod whose containers report
that they are not ready "does not receive traffic through Kubernetes Services"; a failed
liveness check makes the kubelet "kill and restart the container"; and its readiness example
includes applications that "depend on external services after startup". Google SRE records
that health checking "may create a failure mode in which health-checking itself makes the
service unhealthy". The distinction between process health checking for a scheduler and service
health checking for a load balancer is Tycho's framing. AWS takes a target out of service after a
bounded number of consecutive failures, puts it back after a bounded number of successes, and,
"if all targets fail health checks at the same time in all enabled Availability Zones", the load
balancer "fails open". The composition
is Tycho: one shared dependency can fail every probe, so readiness removes the whole fleet
from traffic or liveness drives a restart loop, and the load balancer may then fail open to
the same unhealthy targets. Cached answers are composed too: Google SRE notes that resolvers
"cache responses" within the DNS TTL and that authoritative servers cannot flush those
caches, so a previously healthy answer can outlive the health change that should remove it;
reading that cached answer as current health is Tycho. Bound probe frequency and timeouts,
keep liveness independent of shared dependencies, separate instance-local from shared faults,
and drain before removal.

**Alternative (Tycho comparison).** Synthetic checks or SLO-based external monitoring may be
preferable when the runtime probe cannot observe the user journey. AWS describes canaries as
"configurable scripts that run on a schedule, to monitor your endpoints and APIs" that "follow
the same routes and perform the same actions as a customer", so an external check can verify
the journey "even when you don't have any customer traffic on your applications". Google SRE
argues that SLOs measuring reliability "as experienced by your customers" provide the
"highest-quality indication for when an on-call engineer should respond". The choice rule is
Tycho guidance: prefer an external journey check when a process-local probe cannot observe
the journey, keep the runtime probes for local semantics, and do not treat a synthetic check
that shares the dependency under test as independent evidence. A canary that reuses the same
failing dependency is not an external observer.

**Sources and limits.** The bindings use Kubernetes "Configure Liveness, Readiness and
Startup Probes" (`read.batch4-k8s-probes.2026-10-21`), Google SRE "Addressing Cascading
Failures" (`read.batch4-sre-cascading.2026-10-21`) and "Load Balancing at the Frontend"
(`read.batch5-sre-frontend.2026-10-21`), AWS "Health checks for Application Load Balancer
target groups" (`read.aws-elb-health-checks.2026-10-30`), AWS "Synthetic monitoring
(canaries)" (`read.aws-synthetics-canaries.2026-10-30`) and Google SRE Workbook "Alerting on
SLOs" (`read.sre-workbook-slos.2026-10-30`). The AWS and workbook records are recorded in the
shared ledger. These pages describe probe, health-check and monitoring
mechanics; none measures this page's fleet or proves that a shared dependency will be
detected. Exact probe behavior belongs to the chosen runtime and version.

**Unknown probe data and path independence.** No response is not evidence of health.
Define fail-open or fail-closed per dependency and privilege, run probes on a path that does
not depend on the ingress, DNS or control plane they observe, and alert when probe data is
missing rather than treating silence as a pass.

**Exposure and authorization.** State who may call each probe, what version or dependency
topology its response discloses, and whether an unauthenticated dependency check amplifies
load. Keep liveness/readiness cheap and internal; protect detailed diagnostics separately.

## Failure and recovery

| Failure | Design consequence | Discriminating observation |
|---|---|---|
| Stale or ambiguous route | Version routes and define precedence/no-match | Requests reaching a retired backend after publication |
| Gateway bypass | Keep backend authorization and test the bypass path | Direct calls that skip the declared policy point |
| Shared dependency failure | Do not turn one dependency fault into fleet-wide ejection | Instance-local versus shared probe failures |
| Cached healthy answer | Bound probe age and drain before removal | Traffic to a draining instance after readiness changes |

## Bounded pattern ownership notes

### Gateway Routing

Gateway routing is an edge contract over a versioned route table: a gateway matches request
attributes to a route and applies policy, each route binds match predicates to a backend and a
policy version, and the table changes independently of the backends.
The route is a contract about host, path, headers, method and backend identity, not a wildcard that
silently absorbs every new path.

**Invariant and route decomposition (Tycho synthesis).** Describe separately the externally
resolved name, the service membership view, the connection destination and the backend selected
for each request. Azure's Gateway Routing pattern says "The complexity of registering and
unregistering service instances is encapsulated in the gateway" and uses Layer 7 routing to
"route the request to the appropriate instances"; Kubernetes says an Ingress "exposes HTTP and
HTTPS routes from outside the cluster to services within the cluster" and a Service "identifies a
set of Pods", while Gateway API's request flow starts with the DNS resolver learning "a mapping to
one or more IP addresses associated with the Gateway" and then matching the Host header to a route;
Gateway API also notes that a Service backend may be represented "as a Service IP or the backing
EndpointSlices of the Service". Envoy's router "matches it to an upstream cluster, acquires a
connection pool to a host in the upstream cluster, and forwards the request." The four-layer
separation is Tycho's framing. Version routes, test precedence and no-match behavior, and recover
wrong-version selection explicitly. Stale routes, ambiguous matches and bypass around the gateway
are common. Test the bypass path and the ambiguous-match rejection, and emit the selected route
plus backend in the request trace.

**Alternative (Tycho comparison).** A reverse proxy, client-side discovery or a BFF may be
preferable when routing policy is simple or the gateway would become a hidden shared dependency.
Azure's pattern says it "might not be suitable when you have a simple application that uses only
one or two services" and warns that the gateway "can introduce a single point of failure" and
"a bottleneck". Kubernetes lists Service.Type=LoadBalancer and Service.Type=NodePort as ways to
expose a Service "that don't directly involve the Ingress resource", and Envoy describes its
router for "handling edge traffic (traditional reverse proxy request handling)" and a
service-to-service mesh. The preference rule and the client-side discovery and BFF alternatives
are Tycho guidance. Gateway routing is a fit when one edge policy must apply across many backends
and the bypass surface is closed.

**Sources and limits.** The bindings use Azure "Gateway Routing"
(`read.microsoft-gateway-routing.2026-10-21`), Kubernetes "Ingress"
(`read.k8s-ingress.2026-11-01`) and "Gateway API" (`read.k8s-gateway-api.2026-11-01`), and Envoy
"HTTP routing" (`read.envoy-http-routing.2026-11-01`). The Kubernetes and Envoy units were read on
2026-11-01. The pages describe route decomposition, service membership and simpler exposure forms;
none measures this page's route table, proves that a given alternative is preferable, or defines
one no-match behavior across products. Exact matching, precedence and default behavior belong to
the chosen gateway and version.

## Navigation

Parent: [network chapter](README.md). Previous: [discovery and selection](discovery-balancing.md).
Next: [connection draining](connections-draining.md). Related:
[overload admission](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/admission-resource.md).

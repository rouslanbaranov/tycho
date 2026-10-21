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
  "updated_at": "2026-10-22",
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
restarted". They must not be collapsed into one endpoint. External monitoring should also
observe user-level success and dependency state, because a green liveness probe does not
prove readiness, correct routing or a healthy dependency.

Define startup eligibility, readiness, draining and permanent removal separately. A liveness
endpoint should not restart every healthy process because one shared dependency is
unavailable.

**Failure and recovery.** A shared dependency failure can fail every probe and cause mass
ejection or restart; a cached "healthy" answer can keep sending traffic to a draining
instance. Bound probe frequency/timeouts, separate instance-local from shared faults, and
drain before removal. Synthetic checks or SLO-based external monitoring may be preferable
when the runtime probe cannot observe the user journey. Exact probe behavior belongs to the
chosen runtime/version.

## Failure and recovery

| Failure | Design consequence | Discriminating observation |
|---|---|---|
| Stale or ambiguous route | Version routes and define precedence/no-match | Requests reaching a retired backend after publication |
| Gateway bypass | Keep backend authorization and test the bypass path | Direct calls that skip the declared policy point |
| Shared dependency failure | Do not turn one dependency fault into fleet-wide ejection | Instance-local versus shared probe failures |
| Cached healthy answer | Bound probe age and drain before removal | Traffic to a draining instance after readiness changes |

## Navigation

Parent: [network chapter](README.md). Previous: [discovery and selection](discovery-balancing.md).
Next: [connection draining](connections-draining.md). Related:
[overload admission](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/admission-resource.md).

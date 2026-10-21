---
{
  "metadata_version": 1,
  "id": "tycho.page.ad9c044731ff175a4d0bb6106fe2a0f7",
  "kind": "page",
  "parent_id": "tycho.chapter.8a86707018773def410689efbc79cf94",
  "canonical_path": "book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/discovery-balancing.md",
  "title": "Discovery, load balancing and backend selection",
  "topic_ids": [
    "network-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "How does an endpoint change become a correctly balanced request rather than merely a new address?",
  "route_hints": {
    "questions": [
      "How does an endpoint change become a correctly balanced request rather than merely a new address?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.8a86707018773def410689efbc79cf94"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "does",
      "endpoint",
      "change",
      "become",
      "correctly",
      "balanced",
      "request",
      "rather",
      "than",
      "merely",
      "address"
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
    "reviewed_at": "2026-10-20",
    "reviewer": "Codex enrichment author; execution gates pending",
    "proof_uri": null
  },
  "authored_at": "2026-10-20",
  "updated_at": "2026-10-21",
  "source_inspection_date": "2026-10-20",
  "content_verified_at": null
}
---

# Discovery, load balancing and backend selection

**Owning question:** How does an endpoint change become a correctly balanced request rather than merely a new address?


> **Pattern atlas:**
> [Gateway Routing](../../v11-pattern-atlas/c02-api-communication/README.md#gateway-routing) — decision conditions and contraindications.
> [Service Discovery](../../v11-pattern-atlas/c02-api-communication/README.md#service-discovery) — decision conditions and contraindications.
> [Client-Side Discovery](../../v11-pattern-atlas/c02-api-communication/README.md#client-side-discovery) — decision conditions and contraindications.
> [Server-Side Discovery](../../v11-pattern-atlas/c02-api-communication/README.md#server-side-discovery) — decision conditions and contraindications.


> **Pattern atlas:**
> [Health Endpoint Monitoring](../../v11-pattern-atlas/c07-resilience/README.md#health-endpoint-monitoring) — decision conditions and contraindications.


> **Pattern atlas:**
> [Load Balancing](../../v11-pattern-atlas/c09-scalability/README.md#load-balancing) — decision conditions and contraindications.

## The routing contract

A caller needs a route to an eligible instance, not a timeless list of machines. Describe separately the externally resolved name, the service membership view, the connection destination and the backend selected for each request. A global route may choose a location; an internal selector chooses a process. A stale membership view can outlive a rollout.

The two SRE load-balancing chapters distinguish global routing from backend selection. Their examples support the need to examine locality, workload and selection policy; they do not prescribe one algorithm for every service.

## DNS and discovery have different update boundaries

In a typical DNS path, a recursive resolver may answer from a cached record or consult the authoritative naming hierarchy. The application/runtime can also retain resolved addresses or established connections. A DNS TTL governs a DNS record's caching contract; it is not an application transaction deadline or a guarantee that every client stops using an existing connection at that instant.

Service discovery may publish addresses plus eligibility metadata to a proxy or client. Document who observes updates and how stale membership is detected. Distinguish the discovery control path from data-plane requests that can continue against a last-known usable set. If membership is stale, continued reachability still cannot establish write authority.

For an original cutover decision, publish the replacement endpoint, establish its readiness and trust, and account for old route/connection lifetimes before retiring the former endpoint. A DNS change alone is neither a drain procedure nor a database failover protocol. The exact resolver/runtime's cache and failure behavior remains a product-specific verification task.

## Original worked design: one connection is not one unit of work

Assume a fictional catalogue has three interchangeable read replicas. One client multiplexes 90 long requests over one connection; two others send one request each. These are invented counts. A selector that balances connections can produce 90/1/1 requests even when its connection counts are equal. A request-aware selector could redistribute new eligible requests, but cannot move an already executing operation without a protocol for interruption.

Compare round-robin, random choice, least-active requests and affinity against request cost, stale load signals and state placement. An active-request count still cannot predict a single unusually expensive query. Affinity may preserve a local working set but overload one backend when a key becomes hot. Rebalancing belongs to [partition ownership](../../v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-rebalancing/README.md) when requests depend on stateful placement.

~~~mermaid
flowchart TD
    C["Client route and connection cache"] --> P["Proxy with endpoint snapshot"]
    D["Discovery control plane"] --> P
    P --> A["Backend A: active work"]
    P --> B["Backend B: active work"]
    P --> E["Backend C: draining"]
    E --> F["Existing work completes or reconciles"]
~~~

Text alternative: discovery updates the proxy's view. The proxy sends eligible new work to active backends; a draining backend may still own existing work. This is an original conceptual topology, not a deployed configuration.

### Selection signals are not interchangeable

A selector can count connections, active requests, completed work, errors or
resource utilization. These signals answer different questions and fail in
different ways.

- **Connection count** reflects how many transports a client holds. It
  misleads when one connection multiplexes many requests or when idle
  connections still consume memory and health-check work.
- **Active requests** reflect unfinished work visible to that client. They
  misrank I/O-bound work: a request waiting on a remote response consumes
  little CPU but still occupies a slot. The count also excludes work sent by
  other clients, so each client sees only a partial view.
- **Completed work and latency** capture useful progress but react after the
  fact; a short window is noisy, and a slow-but-successful backend can look
  better than a fast-but-failing one.
- **Resource utilization** (CPU, queue depth, memory) is closer to capacity
  but depends on comparable measurement across heterogeneous machines and
  on the backend reporting it promptly.

The source's *Weighted Round Robin* example combines backend-reported
query, error and utilization signals into a capability score; its weights
and thresholds are contextual. Choose a signal that matches the protected
outcome: completed correct work, not raw connection count. Cap request cost
at the interface where one request can dominate a backend, and test the
selector under the real cost distribution.

### Fast errors can attract traffic

A least-loaded or active-request selector assumes that a backend with spare
capacity will do useful work. A seriously unhealthy backend can instead
return an error in milliseconds, so its active-request count falls and the
selector sends it more traffic. The backend becomes a sinkhole.

- Count recent errors, health signals or an explicit success rate as part of
  the load signal, not only open requests.
- Distinguish a fast failure from a slow dependency: the first can look idle,
  the second can look busy while making no progress.
- Keep recovery probes separate from the load signal so a recovered backend
  can return without a thundering herd.
- Test with a backend that fails in roughly 1 ms; observe whether new work is
  diverted before the error budget is exhausted.

### Bounded subsets reduce connection cost and churn

A client does not need a connection to every backend. A bounded subset limits
memory, health-check traffic and reconnect work, at the cost of a smaller
choice set.

- Assign backends uniformly so one subset does not overload a backend; a
  skewed subset forces fleet-wide overprovisioning.
- Handle restarts and resizes with minimal churn: replacing one backend
  should not reconnect every client at once.
- Use a larger subset when clients burst or when request costs vary widely;
  a small subset concentrates a burst on fewer backends.
- Keep the subset selection deterministic enough to reproduce, but not so
  static that a failed backend remains in every client's set.
- Test a rolling restart and a backend loss; measure reconnect rate,
  per-backend load skew and time to uniform distribution.

The retry decision that follows a rejection is owned by `V02/C05`
(`tycho.page.43414664520b4866929f7f006f27f59b`); this page owns the selection
signal and the connection topology. Overload shedding is owned by `V07/C05`
(`tycho.page.d9abd43bb7394c04a6bf77d4014f870d`).

## Failure and recovery

| Failure | Design consequence | Discriminating observation |
|---|---|---|
| Resolver unavailable | Decide whether a bounded cached answer remains usable | Successful new connections versus resolver errors, by cache age |
| Removed backend still cached | Removal and connection shutdown require coordinated policy | Attempts to the removed endpoint after route publication |
| Every backend probes a shared failed dependency | Ejecting all instances can make local capacity unusable | Shared dependency failures versus instance-local faults |
| Fresh discovery is unavailable | A last-known endpoint set may permit reads, but cannot grant write authority | Membership age, reachable data plane and authority epoch |
| Retry selects another replica | May amplify work or repeat a committed effect | Logical operation IDs and retry budgets |

Define startup eligibility, readiness, draining and permanent removal separately. A liveness endpoint should not restart every healthy process because one shared dependency is unavailable. Exact probe behavior belongs to the chosen runtime/version.

## Choice, acceptance and evidence

Use a simple static endpoint or one proxy when its failure and maintenance contract is adequate. Introduce client-side discovery only if clients can maintain and test membership, backoff, observability and upgrade behavior. A mesh adds a policy/control plane; it does not remove those obligations.

Proposed acceptance: maintain requests during endpoint churn, skew costs deliberately, disconnect discovery, and compare useful throughput, per-backend outstanding work and completion correctness. No benchmark or DNS convergence bound was measured.

Sources: [Load Balancing at the Frontend](https://sre.google/sre-book/load-balancing-frontend/)
(global routing and DNS discussion);
[Load Balancing in the Datacenter](https://sre.google/sre-book/load-balancing-datacenter/)
(subsetting, selection policies, resource and error signals). Sections
*Limiting the Connections Pool with Subsetting*, *Varying query costs*,
*Least-Loaded Round Robin* and *Weighted Round Robin* were inspected
2026-10-21. Algorithm comparisons and the failure matrix are original design
reasoning.

## Navigation

Parent: [network chapter](README.md). Next: [connection draining](connections-draining.md). Related: [failure domains](../c06-high-availability-and-failure-domain-placement/README.md), [overload admission](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/admission-resource.md).

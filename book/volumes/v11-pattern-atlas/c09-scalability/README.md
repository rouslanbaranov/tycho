---
metadata_version: 1
id: "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c09-scalability/README.md"
title: "V11/C09 — Scalability and load distribution"
topic_ids:
  - "scaling-mechanisms"
  - "performance-engineering"
perspectives:
  - "architecture"
  - "operations"
summary: "All 10 C09 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which scaling patterns fit the bottleneck and failure domain?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "scalability and load distribution"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.sre-frontend-enrichment"
    - "src.k8s-hpa"
    - "src.kubernetes"
    - "src.keda"
    - "src.microsoft-cloud-patterns"
    - "src.cortex-shuffle-sharding"
    - "src.cell-boundaries"
    - "src.microsoft-multitenant"
  claim_ids: []
  status: "source-linked"
  notes: "10 cards cite read units; owner links are bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---
# V11/C09 — Scalability and load distribution

**Owning question:** Which scaling patterns fit the bottleneck and failure domain?

## Purpose and mission

This chapter is the atlas entry point for **Scalability and load distribution**. It
owns the conditional decision route for 10 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 10 entries have a self-checked card. Owner sections are bounded: a scaling or
placement page may own the bottleneck/failure contract without owning every pattern.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Load Balancing

**Identity.** Load Balancing; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should requests be distributed across equivalent backends by a
resolver or proxy?

**Good-fit conditions.** Multiple eligible backends exist; health/selection signals are
available; the client or proxy can retry safely.

**Hard contraindications.** Reject when one backend can serve the load, when backends are
not equivalent, or when selection would amplify a hot spot.

**Competing alternative.** Client-side selection or a single backend. Reverse the choice
when balancing complexity and stale membership exceed availability benefit.

**Failure and recovery.** Stale membership and fast-error attraction are common; verify
selection in the owner section.

**Technical owner.** [Load Balancing](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/discovery-balancing.md#load-balancing) — load balancing is bounded, not a product-specific algorithm survey.

**Sources.**
[src.sre-frontend-enrichment](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-sre-frontend.2026-10-21: all four headings read; DNS,
VIP and anycast are not literal headings. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Horizontal Scaling; Autoscaling; Service Discovery; Read Replicas.

### Horizontal Scaling

**Identity.** Horizontal Scaling; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should capacity be added by running more instances rather than a
larger instance?

**Good-fit conditions.** The workload can partition across instances; shared state is
removable; startup and coordination costs are bounded.

**Hard contraindications.** Reject when the bottleneck is a single shared resource, when
instances cannot be stateless, or when coordination cost grows faster than capacity.

**Competing alternative.** Vertical scaling or a larger partition. Reverse the choice when
shared-state contention dominates added instances.

**Failure and recovery.** Coordination and cold-start lag are common; verify ceiling in
the owner section.

**Technical owner.** [Horizontal Scaling](../../v07-performance-scale-and-resilience/c06-horizontal-vertical-scaling-and-autoscaling-delay/autoscaling-lag-and-capacity-limits.md#horizontal-scaling) — replica scaling and coordination cost are bounded; per-service capacity math is owner-specific.

**Sources.** [src.k8s-hpa](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-k8s-hpa.2026-10-21: all thirty served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Vertical Scaling; Autoscaling; Load Balancing; Sharding.

### Vertical Scaling

See the [dedicated Vertical Scaling card](vertical-scaling.md).

### Autoscaling

**Identity.** Autoscaling; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should capacity be adjusted automatically from observed or
predicted demand?

**Good-fit conditions.** Metrics reflect useful demand; scale-up/down delays are
acceptable; stabilization prevents oscillation.

**Hard contraindications.** Reject when demand is stable, when startup lag exceeds the
burst, or when the metric can be gamed.

**Competing alternative.** Static capacity or scheduled scaling. Reverse the choice when
autoscaling churn and cold starts dominate cost.

**Failure and recovery.** Lag and oscillation are common; verify stability in the owner
section.

**Technical owner.** [Autoscaling](../../v07-performance-scale-and-resilience/c06-horizontal-vertical-scaling-and-autoscaling-delay/autoscaling-lag-and-capacity-limits.md#autoscaling) — signal, lag and hysteresis are bounded; capacity forecast is service-specific.

**Sources.** [src.keda](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-keda.2026-10-21: the single served heading read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Horizontal Scaling; Vertical Scaling; Load Balancing; Capacity
Planning.

### Cell-Based Architecture

**Identity.** Cell-Based Architecture; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should the system be partitioned into cells with bounded blast
radius and independent operation?

**Good-fit conditions.** Workloads can be routed to a cell; a cell is a dependency
boundary; cell failover/migration is owned.

**Hard contraindications.** Reject when a single global dependency defeats isolation, when
cell routing is unowned, or when the cost of duplicate cells is prohibitive.

**Competing alternative.** Single shared deployment or deployment stamps without
isolation. Reverse the choice when cell duplication and routing complexity exceed
blast-radius benefit.

**Failure and recovery.** Cell routing and cross-cell dependencies are common; verify
boundaries in the owner section.

**Technical owner.** [Cell-Based Architecture](../../v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-domain-placement/cells-shuffle-sharding.md#cell-based-architecture) — cell placement is bounded, not a universal stamp deployment recipe.

**Sources.**
[src.cell-boundaries](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch7-cell-boundaries.2026-10-22: sections "What is a cell-based
architecture?", "A typical workload", "A workload with cell-based architecture". The
Deployment Stamps page remains a comparison only, not the cell source.

**Decision state.** applicable-under-conditions.

**Related entries.** Deployment Stamps; Shuffle Sharding; Tenant Isolation; Failover.

### Shuffle Sharding

**Identity.** Shuffle Sharding; family Scalability and load distribution; kind
scalability-pattern; priority advanced.

**Decision question.** Should each tenant be assigned a random subset of shards to reduce
overlapping blast radius?

**Good-fit conditions.** Many tenants exist; shard assignment can be consistent; enough
shards exist to reduce overlap.

**Hard contraindications.** Reject when there are too few shards, when assignment cannot
be stable, or when the operational cost of many assignments is high.

**Competing alternative.** Cell-based partitioning or dedicated shards. Reverse the choice
when overlap reduction does not justify assignment complexity.

**Failure and recovery.** Hot tenants and uneven overlap are common; verify assignment in
the owner section.

**Technical owner.** [Shuffle Sharding](../../v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-domain-placement/cells-shuffle-sharding.md#shuffle-sharding) — shuffle sharding is bounded, not a hashing implementation guide.

**Sources.**
[src.cortex-shuffle-sharding](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-cortex-shuffle.2026-10-21: all eighteen served headings
read. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Cell-Based Architecture; Sharding; Tenant Isolation; Load Balancing.

### Deployment Stamps

**Identity.** Deployment Stamps; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should independent deployment units be replicated as stamps for
scale, isolation or locality?

**Good-fit conditions.** Each stamp can be independently operated; routing/state ownership
is explicit; duplication cost is acceptable.

**Hard contraindications.** Reject when one deployment suffices, when stamps would share a
hidden global dependency, or when routing/state duplication is unowned.

**Competing alternative.** Cell-based architecture or one shared deployment. Reverse the
choice when stamp operations and duplication exceed isolation benefit.

**Failure and recovery.** Configuration drift and state duplication are common; verify
boundaries in the owner section.

**Technical owner.** [Deployment Stamps](../../v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-domain-placement/cells-shuffle-sharding.md#deployment-stamps) — independent deployment units for scale, isolation or locality, with routing keys and upgrade ownership.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-deployment-stamps.2026-10-21: all thirteen served
headings read. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Cell-Based Architecture; Geode; Tenant Isolation; Multi-Region.

### Geode

**Identity.** Geode; family Scalability and load distribution; kind scalability-pattern;
priority advanced.

**Decision question.** Should identical nodes be deployed across regions behind a global
routing layer?

**Good-fit conditions.** Latency/locality matters; data replication and failover are
owned; global routing can direct clients.

**Hard contraindications.** Reject when one region meets latency/availability, when data
replication cannot be reconciled, or when global routing adds a single point.

**Competing alternative.** Cell-based single-region deployment or active-passive recovery.
Reverse the choice when cross-region consistency and cost exceed locality benefit.

**Failure and recovery.** Replication lag and regional failover are common; verify
recovery in the owner section.

**Technical owner.** [Disaster recovery: measured RTO/RPO, fencing and state reconciliation](../../v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/disaster-recovery-and-recovery-objectives.md#geode) — geode is bounded to regional recovery; not a product template.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-geode.2026-10-21: all seven served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Deployment Stamps; Cell-Based Architecture; Multi-Region Recovery;
CDN.

### Static Content Hosting

See the [dedicated Static Content Hosting card](static-content-hosting.md).

### Tenant-Based Resource Isolation

**Identity.** Tenant-Based Resource Isolation; family Scalability and load distribution;
kind scalability-pattern; priority core.

**Decision question.** Should tenants receive isolated compute/data/networking quotas
rather than share one unbounded pool?

**Good-fit conditions.** Tenant identity is known; noisy-neighbor risk is material;
quotas/isolation can be enforced and observed.

**Hard contraindications.** Reject when one tenant exists, when isolation would strand
most capacity, or when quotas cannot be enforced at the resource.

**Competing alternative.** Shared pool with per-tenant rate limits. Reverse the choice
when isolation cost exceeds noisy-neighbor risk.

**Failure and recovery.** Quota bypass and cross-tenant leakage are common; verify
isolation in the owner section.

**Technical owner.** [Multitenant isolation](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/multitenant-isolation.md#tenant-based-resource-isolation) — tenant isolation is bounded, not a full control catalogue.

**Sources.**
[src.microsoft-multitenant](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-ms-multitenant.2026-10-21: all three served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Cell-Based Architecture; Rate Limiting; Bulkhead; Multitenant
Isolation.

## Chapter result and counterexample

Ten cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: adding replicas to a workload with one shared writer is not evidence
for the horizontal-scaling card's conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C08](../c08-coordination/README.md).
- Next: [V11/C10](../c10-deployment-modernization/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 10 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.

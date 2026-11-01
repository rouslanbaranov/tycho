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
    - "src.sre-workbook"
  claim_ids: []
  status: "source-linked"
  notes: >-
    10 cards cite read units; owner links are bounded. Tenant-Based Resource
    Isolation moved to a dedicated page on 2026-10-31 with AWS SaaS Lens tenant,
    pool and cross-tenant guidance, Kubernetes multi-tenancy, PostgreSQL row
    security and Microsoft multitenant approaches. Geode failure/recovery and
    alternative bind 2026-11-01 to the Geodes pattern, Traffic Manager and
    multiregion guidance; proposed sources are not yet registered.
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
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

See the [dedicated Deployment Stamps card](deployment-stamps.md).

### Geode

**Identity.** Geode; family Scalability and load distribution; kind scalability-pattern;
priority advanced.

**Decision question.** Should identical nodes be deployed across regions behind a global
routing layer?

**Good-fit conditions.** Both regions can serve any request; locality or regional survival
matters; replication, conflict handling and failover authority are owned; a health signal and
a separate freshness gate exist; global routing can send clients to a healthy region.

**Hard contraindications.** Reject when one region meets latency/availability, when state
cannot be replicated or writes must stay in one region, when conflicts cannot be resolved, or
when a stale DNS route or isolated region would defeat the design.

**Competing alternative.** Active-passive recovery when strict write-region requirements,
hard-to-replicate state, cost constraints or RTO tolerance make active-active routing
unjustified; a single-region cell when locality is not needed. Active-active is justified when
both regions can serve any request and the lowest RTO is required, accepting bidirectional
replication and conflict resolution. Active-passive lowers cost but its passive path can
drift; test failover and failback. Reverse when consistency and routing complexity exceed
locality benefit; this selection rule is Tycho guidance.

**Failure and recovery.** Stale DNS, long-lived connections, an isolated region, a successful
but non-authoritative health probe, replication lag and an old writer are common. Traffic
Manager clients keep a cached endpoint "until the DNS cache expires"; geographic routing
"returns a response whether the endpoint is healthy or not"; when all eligible endpoints are
degraded it makes a "best effort" attempt and answers as if they were online. Probe the serving
path, including database availability where possible; treat the probe as authoritative for
reachability, not freshness, and monitor replication lag. Fence the old writer before failover;
the sources delegate quorum to the replication backplane and require conflict handling for
bidirectional writes, but do not prescribe fencing, so that rule is Tycho guidance. The router
is a critical dependency, but Azure Traffic Manager is "a single, global service" designed to
be "resilient to a complete failure of any Azure region"; residual risk is stale routing and
freshness, not a proven regional single point of failure.

**Technical owner.** [Disaster recovery: measured RTO/RPO, fencing and state reconciliation](../../v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/disaster-recovery-and-recovery-objectives.md#geode) — geode is bounded to regional recovery; not a product template.

**Sources.** [src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
retained record `read.batch5-geode.2026-10-21`; proposed 2026-11-01 record
`read.geode-pattern.2026-11-01` (src.microsoft-cloud-patterns); proposed
`read.azure-traffic-manager-routing.2026-11-01`,
`read.azure-traffic-manager-monitoring.2026-11-01` and
`read.azure-traffic-manager-faq.2026-11-01` (proposed src.azure-traffic-manager);
proposed `read.azure-multiregion-network.2026-11-01` (proposed
src.azure-multiregion-design); and proposed
`read.azure-appservice-multiregion.2026-11-01` (proposed
src.azure-multiregion-appservice). Public documentation, not a benchmark, failover, routing
or replication-lag test.

**Decision state.** applicable-under-conditions.

**Related entries.** Deployment Stamps; Cell-Based Architecture; Multi-Region Recovery;
CDN.

### Static Content Hosting

See the [dedicated Static Content Hosting card](static-content-hosting.md).

### Tenant-Based Resource Isolation

See the [dedicated Tenant-Based Resource Isolation card](tenant-based-resource-isolation.md).

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

---
metadata_version: 1
id: "tycho.page.6f2a9c4e1b7d4a8f9e3c5b0d2a6f8e1c"
kind: "page"
parent_id: "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
canonical_path: "book/volumes/v11-pattern-atlas/c09-scalability/geode.md"
title: "Geode"
topic_ids:
  - "scaling-mechanisms"
  - "performance-engineering"
perspectives:
  - "architecture"
  - "operations"
summary: >-
  Decision card for Geode; source-anchored on the Microsoft Geodes pattern,
  Traffic Manager routing, monitoring and FAQ, multiregion network design and
  multiple-region App Service guidance; coverage remains partial-bounded, no
  promotion.
route_hints:
  questions:
    - >-
      Should identical nodes be deployed across regions behind a global routing
      layer?
  prerequisites:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  related_ids:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "geode"
    - "scalability and load distribution"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
    - "src.azure-traffic-manager"
    - "src.azure-multiregion-design"
    - "src.azure-multiregion-appservice"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch5-geode.2026-10-21 and the 2026-11-01 records
    read.geode-pattern.2026-11-01,
    read.azure-traffic-manager-routing.2026-11-01,
    read.azure-traffic-manager-monitoring.2026-11-01,
    read.azure-traffic-manager-faq.2026-11-01,
    read.azure-multiregion-network.2026-11-01 and
    read.azure-appservice-multiregion.2026-11-01; owner section and limits are
    bounded.
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
# Geode

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
retained record `read.batch5-geode.2026-10-21`; 2026-11-01 records
`read.geode-pattern.2026-11-01` (src.microsoft-cloud-patterns),
`read.azure-traffic-manager-routing.2026-11-01`,
`read.azure-traffic-manager-monitoring.2026-11-01` and
`read.azure-traffic-manager-faq.2026-11-01` (src.azure-traffic-manager),
`read.azure-multiregion-network.2026-11-01` (src.azure-multiregion-design) and
`read.azure-appservice-multiregion.2026-11-01` (src.azure-multiregion-appservice).
Public documentation, not a benchmark, failover, routing or replication-lag test.

**Decision state.** applicable-under-conditions.

**Related entries.** Deployment Stamps; Cell-Based Architecture; Multi-Region Recovery;
CDN.

**Limits.** Coverage is partial-bounded and self-checked, not independent review, promotion
or owner acceptance. Fencing, the separate freshness gate and the active-active selection rule
are Tycho synthesis; no routing profile, geode, failover, conflict, replication-lag or fencing
test was run.

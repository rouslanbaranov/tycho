---
metadata_version: 1
id: "tycho.page.6b3725950fad4c0db82417b3d0225d32"
kind: "page"
parent_id: "tycho.chapter.9e35eb7b056f428093e36a2faf644a23"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-domain-placement/availability-zones-placement-and-failure-domains.md"
title: "Availability zones, placement and failure-domain architecture"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated question, original scenario and transfer limits for High availability and failure-domain placement. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What survives machine, zone, dependency or region loss?"
  prerequisites: []
  related_ids:
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
    - "tycho.page.2f6602f8e20b4f80a22e0ef85a6d1765"
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.page.1b2657011d454460856103419095031b"
    - "tycho.landing.6f58e5c00dea4f4086963169a2590bf5"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.page.3e79e1a21bd944a5bddf9564daed5066"
    - "tycho.page.c579aa863be74f9ca5718e58f6f34c21"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Availability"
    - "zones"
    - "placement"
    - "and"
    - "failure-domain"
    - "architecture"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.6b3725950fad4c0db82417b3d0225d32:-1 -->

# Availability zones, placement and failure-domain architecture

> **Independent Tycho manuscript — V08/C06**, 2026-10-19. Public Kubernetes
> scheduling/topology and AWS Well-Architected DR planning references inform the
> explanation. The topology and fault tests are original hypothetical examples. No
> cluster, deployment, failover or independent technical
> acceptance was performed. The earlier [combined region/recovery
> research](../../../deployment/multi-region-disaster-recovery-contracts.md) is preserved.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.6b3725950fad4c0db82417b3d0225d32:0 -->
## Purpose and mission

A process can be healthy and the overall user journey unavailable because all replicas share a datastore, network gateway, certificate issuer, routing plane or failure domain. Running *more replicas* does not guarantee isolation unless their placement and dependencies are modeled.

This chapter owns the **physical and logical allocation of compute/network/state across failure domains**, including single-zone and multi-zone service availability. [V08/C07 disaster recovery](../c07-multi-region-recovery-and-data-reconciliation/disaster-recovery-and-recovery-objectives.md) owns regional catastrophe response and RPO/RTO/restore acceptance; [runtime topology](../c03-vms-containers-orchestration-and-serverless/runtime-placement-and-control-plane.md) owns container, VM and control-plane mechanics.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.6b3725950fad4c0db82417b3d0225d32:7 -->
## Engineering walkthrough — Two zones, one shared dependency and no real isolation

**Original synthetic deployment:** three API replicas are spread across zones A and B. All replicas use one identity endpoint and one database writer reachable only through a zone-A dependency chain. When zone A fails, replicas in B may remain healthy at process level but cannot authorize or commit reservations; a zone-spread label did not eliminate the shared failure domain.

| Dependency | Claimed independence | Hidden coupling to falsify |
|---|---|---|
| App replicas | Different compute zones | Both require one failed regional load-balancing/control endpoint |
| Booking data | One authoritative database | No safely promoted writer or routing outside zone A |
| Identity/credentials | Cross-zone request admission | Token validation or signing-key service solely in zone A |
| External payment | Provider/network connection | Route depends on a failed shared NAT/egress path |

The correct user-level capability after a zone loss might be read-only public catalogue access, while new reservations must be refused until one writer can be recovered safely. Such degraded operation is valid if explicitly promised; counting 200 OK responses from an obsolete cache as healthy booking service is not.

**Proposed isolated experiment:** remove zone A's compute and selected network services, then independently inject database loss and identity loss, recording correct completed journeys, unauthorized/stale responses, detection-to-routing time, RPO/RTO and required operator interventions. Recovery must avoid promoting two booking writers. Kubernetes topology-spread guidance supports placement controls and AWS recovery guidance supports failure-scoped objectives; neither certifies this hypothetical multi-zone architecture. A simpler active/passive topology with demonstrated failover may be safer than nominal active/active without state fencing.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Model shared dependencies and traffic authority when placing replicas across failure domains.

Two zones can still depend on one datastore or control path; nominal placement diversity does not demonstrate surviving user journeys.

The detailed pages separate the mechanisms that make this decision conditional:

- [Shared dependencies and replica placement](failure-domains.md) — Which dependency sets remain common despite nominal zone diversity?
- [Authority, control loss and availability tests](authority-availability.md) — Which traffic and state ownership transfer must be validated after a domain fails?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

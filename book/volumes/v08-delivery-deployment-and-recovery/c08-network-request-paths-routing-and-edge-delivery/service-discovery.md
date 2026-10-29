---
metadata_version: 1
id: "tycho.page.21ec7c5f9aa44e2aae9a3160695bdd2e"
kind: "page"
parent_id: "tycho.chapter.8a86707018773def410689efbc79cf94"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/service-discovery.md"
title: "Service Discovery"
topic_ids:
  - "network-architecture"
perspectives:
  - "architecture"
  - "operations"
  - "evaluation"
summary: "Bounded technical ownership note for Service Discovery; Envoy EDS mechanism, eventual consistency and health-check limits."
route_hints:
  questions:
    - "Should Envoy fetch cluster members from a xDS discovery service rather than a static endpoint list?"
  prerequisites:
    - "tycho.chapter.8a86707018773def410689efbc79cf94"
  related_ids:
    - "tycho.chapter.8a86707018773def410689efbc79cf94"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "service discovery"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.envoy"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the discovery and balancing page; the bound source claims and limits remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Service Discovery

> **Pattern atlas:**
> [Service Discovery](../../v11-pattern-atlas/c02-api-communication/service-discovery.md#service-discovery) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[discovery, load balancing and backend selection page](discovery-balancing.md#service-discovery)
on 2026-10-29. Client-side discovery, server-side discovery and load balancing remain on the
chapter page.

Envoy fetches cluster members from a xDS management server through the endpoint discovery service.
The cluster members are called endpoints; for each cluster Envoy fetches the endpoints from the
discovery service. EDS carries per-host attributes such as load-balancing weight, canary status
and zone. Envoy assumes hosts come and go in an eventually consistent way. Active health checking
determines cluster health. EDS is the preferred service discovery mechanism for Envoy. Static endpoint configuration is the
simplest alternative. Envoy supports static, strict DNS, logical DNS, endpoint discovery service
and original destination service discovery. With EDS, Envoy has explicit knowledge of each upstream
host and can make more intelligent load-balancing decisions. Extra attributes carried in the
discovery response inform Envoy of load-balancing weight, canary status and zone.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V08/C08 — Network request paths, routing and edge delivery](README.md) |
| Originating page | [Discovery, load balancing and backend selection](discovery-balancing.md#service-discovery) |

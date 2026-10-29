---
metadata_version: 1
id: "tycho.page.b503488c20a947b581ef45e84ea735d6"
kind: "page"
parent_id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/service-discovery.md"
title: "Service Discovery"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Service Discovery; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should Envoy fetch cluster members from a xDS discovery service
      rather than a static endpoint list?"
  prerequisites:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  related_ids:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "service discovery"
evidence_scope:
  source_ids:
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
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Service Discovery

**Identity.** Service Discovery; family API and service communication; kind infrastructure
pattern; priority core.

**Decision question.** Should Envoy fetch cluster members from a xDS discovery service rather
than a static endpoint list?

**Good-fit conditions.** Cluster membership changes; a xDS management server is available;
Envoy can use the endpoint discovery service.

**Hard contraindications.** Reject when no xDS management server exists.

**Competing alternative.** Static endpoint configuration is the simplest alternative.

**Failure and recovery.** Discovery is eventually consistent; active health checking determines
cluster health.

**Technical owner.** [Network request paths: discovery and balancing](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/service-discovery.md#service-discovery) — bounded to Envoy EDS, not a generic discovery contract.

**Sources.** [src.envoy](../../../../edition/patterns/reading-ledger.v1.json)
read record read.envoy-service-discovery.2026-10-21: Envoy service discovery page read.
The source is public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Client-Side Discovery; Server-Side Discovery; Load Balancing; DNS.

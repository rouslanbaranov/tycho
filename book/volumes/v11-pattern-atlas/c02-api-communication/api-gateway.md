---
metadata_version: 1
id: "tycho.page.a24f9c4b9fb94addaae978843412ffac"
kind: "page"
parent_id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/api-gateway.md"
title: "API Gateway"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for API Gateway with bounded owner evidence."
route_hints:
  questions:
    - >-
      Should external clients enter through a managed gateway that owns routing,
      authentication and cross-cutting edge policy?
  prerequisites:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  related_ids:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "api gateway"
    - "edge policy"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
    - "src.aws-api-gateway"
    - "src.azure-api-management"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# API Gateway

**Identity.** API Gateway; family API and service communication; kind integration
pattern; priority core.

**Decision question.** Should external clients enter through a managed gateway that
owns routing, authentication and cross-cutting edge policy?

**Good-fit conditions.** Multiple clients or backends share edge concerns; routing,
TLS, authentication or rate policy must be consistent; the gateway can be operated and
observed as a critical component; backend authority remains explicit.

**Hard contraindications.** Reject the claim when one simple client can call one
backend directly; when the gateway would become an unowned single point of failure;
when the gateway masks the absence of domain authorization in the backend; when every
request needs a unique policy that the gateway cannot safely express.

**Competing alternative.** A BFF, a service-mesh sidecar or direct backend exposure with an
explicit identity contract. Tycho synthesis: a reverse proxy with a narrow edge contract is
a further alternative; reverse when gateway complexity and outage blast radius exceed the
shared edge benefit.

**Failure and recovery.** Gateway bypass, configuration drift, a stale route, a rate-limit
or quota failure and an outage that blocks every backend are common. AWS's REST API
developer guide documents stage snapshots, the need to redeploy for new settings,
best-effort throttling and 429 responses; Azure documents 429 and 403 rate and quota
responses, quota lag after a platform restart, and a self-hosted gateway that keeps its
last configuration while disconnected. Keep backend authorization, test the bypass path and
version gateway policy. Bypass, stale-route and total backend-blocking outage consequences remain
Tycho analysis; the sources do not test them.

**Technical owner.** [Gateway boundaries and offloading](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/gateway-boundaries-and-offloading.md#api-gateway) — edge identity and gateway boundary; not a full API management specification.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-api-gateway.2026-10-21: all ten served headings
read. AWS API Gateway Developer Guide and Azure API Management pages accessed 2026-10-30;
source records, sections and canonical revisions are in the reading ledger and owner unit.

**Decision state.** applicable-under-conditions.

**Related entries.** Gateway Routing; Gateway Aggregation; Gateway Offloading; Reverse
Proxy.

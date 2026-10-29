---
{
  "metadata_version": 1,
  "id": "tycho.chapter.8a86707018773def410689efbc79cf94",
  "kind": "chapter",
  "parent_id": "tycho.volume.cb10070ba233477fae8aa5d18e74fee8",
  "canonical_path": "book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/README.md",
  "title": "V08/C08 — Network request paths, routing and edge delivery",
  "topic_ids": [
    "network-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "Which network boundary owns routing, transport, trust and the fate of an interrupted request?",
  "route_hints": {
    "questions": [
      "Which network boundary owns routing, transport, trust and the fate of an interrupted request?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "which",
      "network",
      "boundary",
      "owns",
      "routing",
      "transport",
      "trust",
      "fate",
      "interrupted",
      "request"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.sre-frontend-enrichment",
      "src.sre-balancing-enrichment",
      "src.rfc9113-enrichment",
      "src.rfc9111-enrichment"
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

# V08/C08 — Network request paths, routing and edge delivery

**Owning question:** Which network boundary owns routing, transport, trust and the fate of an interrupted request?

## Purpose and mission

Follow one operation from name resolution to the authoritative service and back. Separate route choice, connection lifetime, identity and application outcome so a healthy proxy cannot conceal a failed user journey.

## A worked boundary decision

**Original fictional scenario:** an image catalogue adds an edge cache and a reverse proxy. During a rollout, old connections continue reaching a draining backend, a new certificate is trusted at the edge but not on the internal hop, and a timed-out write is retried. Adding another replica solves none of those contracts by itself. The design must name the resolver/discovery owner, backend selector, termination points and effect identity.

## Pages and reasoning route

| Page | Question |
|---|---|
| [Discovery and selection](discovery-balancing.md) | How do clients find a usable backend and avoid concentrating work on it? |
| [Request routing and health](routing-and-health.md) | Which route selects a backend, and which health signal may admit or remove it? |
| [Connections and shutdown](connections-draining.md) | What can an interrupted stream reveal about an application effect? |
| [Trust at proxies and gateways](tls-gateway-boundaries.md) | Which principal and transport boundary does each hop actually establish? |
| [Gateway boundaries and offloading](gateway-boundaries-and-offloading.md) | Which policy and connection functions may a gateway own without hiding backend authority? |
| [Edge cache and origin protection](edge-cache-origin.md) | Which representations may be cached and what happens when the origin is unavailable? |
| [Static Content Hosting owner note](static-content-hosting.md) | What does the host own for origin protection, purge and rollback? |
| [Service Discovery owner note](service-discovery.md) | Which discovery behavior does Envoy own, and what does eventual consistency leave to health checking? |

## Synthesis and counterexample

A route update does not fence a former database writer; a TLS connection does not authorize a business object; an HTTP/2 shutdown does not certify rollback. Draw distinct data and control paths. Prefer one well-understood proxy over a mesh when the latter's additional policy and operating costs solve no demonstrated problem.

## Failure and acceptance boundary

Proposed review sequence: change the endpoint set while connections remain open; interrupt a write after its effect; rotate a certificate on one hop; revoke access while an edge object is fresh; then restore the origin under queued retries. Observe correct outcomes, not only listener health. These are proposed experiments, not performed results.

## Navigation and prerequisites

Parent: [V08](../README.md). Previous chapter: [region recovery](../c07-multi-region-recovery-and-data-reconciliation/README.md). Next chapter: [SLIs and SLOs](../../v09-observability-security-and-operations/c01-slis-slos-and-error-budgets/README.md). Start with [API effects](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/effect-identity.md), [overload admission](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/admission-resource.md) and [object authorization](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/object-credentials.md).

## Chapter source ledger

Selected passages were inspected on 2026-10-20; no implementation or network experiment was run. [Load Balancing at the Frontend](https://sre.google/sre-book/load-balancing-frontend/) and [Load Balancing in the Datacenter](https://sre.google/sre-book/load-balancing-datacenter/) provide published routing lessons; [HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html) defines HTTP/2, and [HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html) defines cache semantics. Page-local ledgers narrow the claim scope.

- Exact sections re-inspected 2026-10-21 for #227: *Limiting the Connections Pool
  with Subsetting*, *Varying query costs*, *Least-Loaded Round Robin* and
  *Weighted Round Robin*. No new source or measurement is claimed.

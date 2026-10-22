---
{
  "metadata_version": 1,
  "id": "tycho.page.1db0a6e1679448e392ee8422eb5a3beb",
  "kind": "page",
  "parent_id": "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2",
  "canonical_path": "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/multitenant-isolation.md",
  "title": "Multitenant isolation",
  "topic_ids": [
    "security-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "How are tenant data and effects kept separate across every access path?",
  "route_hints": {
    "questions": [
      "How are tenant data and effects kept separate across every access path?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "tenant",
      "isolation",
      "multitenancy",
      "quota",
      "scope"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.owasp-rest-enrichment"
    ],
    "claim_ids": [],
    "status": "source-linked",
    "notes": "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
  },
  "content_review": {
    "status": "self-checked",
    "reviewed_at": "2026-10-22",
    "reviewer": "Tycho agent; execution gates pending",
    "proof_uri": null
  },
  "authored_at": "2026-10-22",
  "updated_at": "2026-10-22",
  "source_inspection_date": null,
  "content_verified_at": null
}
---

# Multitenant isolation

**Owning question:** How are tenant data and effects kept separate across every access path?

Tenant isolation is a property of every query, cache key, queue consumer and credential,
not a deployment label. The tenant scope must come from authenticated context and be enforced
centrally. OWASP REST guidance treats object-level authorization as part of access control;
it does not prescribe this isolation design.

> **Pattern atlas:**
> [Multitenant Isolation](../../v11-pattern-atlas/c11-security-operations/README.md#multitenant-isolation) — decision conditions and contraindications.
> [Tenant-Based Resource Isolation](../../v11-pattern-atlas/c09-scalability/README.md#tenant-based-resource-isolation) — decision conditions and contraindications.

## Tenant-Based Resource Isolation

Tenant-based isolation assigns each tenant a bounded share of compute, storage and quota, with
routing and credentials that keep the tenant scope explicit. No query, cache key, queue consumer
or credential may cross a tenant boundary without an explicit shared-resource contract.

A shared cache or background worker leaks one tenant's data or consumes another's capacity;
scope keys by tenant and test indirect paths with a foreign identifier. A shared pool with
tenant-scoped predicates is cheaper at low scale; choose dedicated resources when
noisy-neighbour or compliance risk dominates.

**Limits.** Per-tenant quotas, noisy-neighbour isolation and cross-tenant test paths are costs;
a shared pool needs explicit fairness and escape hatches. A dedicated pool is justified only
when measured noisy-neighbour cost exceeds its operational cost.

## Multitenant Isolation

Multitenant isolation keeps tenant data and effects separate inside a shared application by
deriving tenant scope from authenticated context at every access path. The tenant identifier
must be derived from authentication and authorization, never accepted from an arbitrary caller
field alone.

A missing tenant predicate in a query, cache or background task exposes another tenant's
records; test indirect paths and enforce the predicate centrally. A tenant-per-deployment
boundary removes shared-code risk at higher cost; share a deployment only when scoping is
enforced consistently across every path.

**Limits.** Central tenant predicates add coupling and migration cost; a missing predicate in one
background path defeats the shared-deployment saving. Per-tenant encryption, backup and deletion are part of
the isolation contract, not only query predicates.

## Navigation

Parent: [identity chapter](README.md). Previous: [authorization policy](authorization-policy-and-least-privilege.md).
Next: [threat models](threat-identity.md).

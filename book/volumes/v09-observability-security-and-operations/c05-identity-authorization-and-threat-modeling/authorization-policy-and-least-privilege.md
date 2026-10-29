---
{
  "metadata_version": 1,
  "id": "tycho.page.99e04ece579d426ba5e48bbb1f6f3695",
  "kind": "page",
  "parent_id": "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2",
  "canonical_path": "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/authorization-policy-and-least-privilege.md",
  "title": "Authorization policy and least privilege",
  "topic_ids": [
    "security-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "Where is authorization decided, and how is each principal limited to the access it needs?",
  "route_hints": {
    "questions": [
      "Where is authorization decided, and how is each principal limited to the access it needs?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "authorization",
      "rbac",
      "abac",
      "least privilege",
      "zero trust"
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

# Authorization policy and least privilege

**Owning question:** Where is authorization decided, and how is each principal limited to the
access it needs?

Authentication establishes a principal; authorization decides what that principal may do.
The decision belongs at the resource boundary, with a policy and attribute scope that can be
explained and denied safely. OWASP REST guidance calls for endpoint access control and
validated claims; it does not prescribe this policy design.

> **Pattern atlas:**
> [Zero Trust Architecture](../../v11-pattern-atlas/c11-security-operations/zero-trust-architecture.md#zero-trust-architecture) — decision conditions and contraindications.
> [Least Privilege](../../v11-pattern-atlas/c11-security-operations/least-privilege.md#least-privilege) — decision conditions and contraindications.
> [RBAC / ABAC](../../v11-pattern-atlas/c11-security-operations/rbac-abac.md#rbac--abac) — decision conditions and contraindications.

## Zero Trust Architecture

**Zero-trust mechanism.** Every request is authenticated and authorized at the resource
boundary using principal identity, workload/device posture, policy and least privilege.
Network location is not trust; a valid token is not object permission. Continuous
verification applies to service-to-service and user-to-service paths alike.

**Failure and recovery.** Policy gaps, legacy bypass paths and identity-provider outages are
common. Deny by default, test indirect and confused-deputy paths, keep a bounded break-glass
path with audit, and fail closed when authority cannot be established.

**Alternative.** Network segmentation, a VPN or mTLS-only service identity may be preferable
when legacy components cannot enforce per-request identity or when policy-evaluation cost
exceeds the threat reduction. Reverse the zero-trust choice when the remaining perimeter
control is the only enforceable boundary.

**Limits.** Policy-decision latency and telemetry coverage are costs; a zero-trust label does
not prove enforcement.

## Least Privilege

Least privilege grants each principal only the permissions its task needs, limited in resource
scope, action and time. Every credential must have a bounded scope, an owner and a revocation
path that does not depend on the compromised principal.

Permission creep and long-lived credentials widen the blast radius without any visible
incident; review grants on a schedule and prefer short-lived scoped credentials. Coarse roles
are simpler to administer for small stable systems; narrow them once measured access reviews
or incident impact justify the overhead.

**Limits.** Permission reviews, role granularity and revocation propagation are ongoing costs;
least privilege without an owner becomes stale entitlement. Emergency access needs a time-boxed,
audited path with revocation tests and logging rather than a permanent broad role.

## RBAC-ABAC

See the [dedicated RBAC-ABAC owner note](rbac-abac.md).

## Navigation

Parent: [identity chapter](README.md). Previous: [identity and workload trust](identity-authorization-and-isolation.md).
Next: [multitenant isolation](multitenant-isolation.md).

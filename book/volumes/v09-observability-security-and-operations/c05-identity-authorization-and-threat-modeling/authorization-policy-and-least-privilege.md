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
    "reviewed_at": "2026-10-29",
    "reviewer": "Tycho agent; execution gates pending",
    "proof_uri": null
  },
  "authored_at": "2026-10-22",
  "updated_at": "2026-10-29",
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
**Tycho synthesis:** network location is not trust and a valid token is not object permission. Continuous
verification applies to service-to-service and user-to-service paths alike. **Tycho synthesis:**
the every-request/resource-boundary rule extends the ASVS session controls.

**Failure and recovery (Tycho analysis).** Policy gaps, legacy bypass paths and identity-provider
outages are possible. NIST warns that "If one vital component is disrupted or unreachable, there
could be a cascade of failures that impact one or multiple business processes." Deny by default,
test indirect and confused-deputy paths, keep a bounded break-glass path with audit, and fail
closed when authority cannot be established; these responses are Tycho guidance.

**Alternative (Tycho comparison).** NIST expects that "Most enterprise infrastructures will
operate in a hybrid zero trust/perimeter-based mode." Network segmentation, a VPN or mTLS-only
service identity may therefore be preferable when legacy components cannot enforce per-request
identity or when policy-evaluation cost exceeds the threat reduction. Reverse the zero-trust
choice when the remaining perimeter control is the only enforceable boundary; the preference
rule is Tycho guidance.

**Limits.** Policy-decision latency and telemetry coverage are costs; a zero-trust label does
not prove enforcement.

## Least Privilege

Least privilege grants each principal only the permissions its task needs, limited in resource
scope, action and time. Every credential must have a bounded scope, an owner and a revocation path that does not
depend on the compromised principal. **Tycho analysis:** ASVS binds revocation mechanics, not
this per-credential ownership rule.

**Tycho guidance:** permission creep and long-lived credentials widen the blast radius without
a visible incident; review grants on a schedule and prefer short-lived scoped credentials.

**Alternative: dual control.** When no narrow role can express the task, keep a task-capable
identity and require independent approval by more than one principal before a high-value
action executes, instead of splitting the entitlement. ASVS 5.0.0 requirement 2.3.5 states:
"Verify that high‑value business logic flows require multi‑user approval to prevent
unauthorized or accidental actions. This could include but is not limited to large monetary
transfers, contract approvals, access to classified information, or safety overrides in
manufacturing." The requirement names the approval control and its examples; it does not
compare the control with least privilege, so the substitution is a Tycho decision inference,
not an ASVS rule. Reverse the choice when approval latency or approver availability would
block a time-critical or automated action, or when approvals become routine.

**Source boundary.** The alternative is bound to `src.owasp-asvs`, ledger record
`read.batch6-asvs.2026-10-21`, requirement 2.3.5 in "V2 Validation and Business Logic". The
pinned PDF SHA-256 is
`a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5`
(reverified 2026-10-29). ASVS places the requirement at Level 3, so it is a high-assurance
control rather than a baseline rule. The requirement covers multi-user approval for high-value
flows; it does not define approver independence or approval evidence, and it does not compare
approval with entitlement minimization. Those design details remain Tycho synthesis.

**Limits.** Permission reviews, role granularity and revocation propagation are ongoing costs;
least privilege without an owner becomes stale entitlement. Emergency access needs a time-boxed,
audited path with revocation tests and logging rather than a permanent broad role.

## RBAC-ABAC

See the [dedicated RBAC-ABAC owner note](rbac-abac.md).

## Navigation

Parent: [identity chapter](README.md). Previous: [identity and workload trust](identity-authorization-and-isolation.md).
Next: [multitenant isolation](multitenant-isolation.md).

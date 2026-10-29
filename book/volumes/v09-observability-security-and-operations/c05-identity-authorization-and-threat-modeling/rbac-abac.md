---
metadata_version: 1
id: "tycho.page.701f492e0f6b4801a832153ac94ad22a"
kind: "page"
parent_id: "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
canonical_path: "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/rbac-abac.md"
title: "RBAC-ABAC"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "operations"
  - "evaluation"
summary: "Bounded technical ownership note for RBAC and ABAC; role, attribute, decision-point and revocation limits."
route_hints:
  questions:
    - "Should authorization use predefined roles, evaluated attributes, or a bounded combination?"
  prerequisites:
    - "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
  related_ids:
    - "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "rbac"
    - "abac"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.owasp-asvs"
    - "src.nist-sp-800-162"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the authorization policy and least privilege page; the bound source claims and limits remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: null
content_verified_at: null
---

# RBAC-ABAC

> **Pattern atlas:**
> [RBAC / ABAC](../../v11-pattern-atlas/c11-security-operations/rbac-abac.md#rbac-abac) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[authorization policy and least privilege page](authorization-policy-and-least-privilege.md#rbac-abac)
on 2026-10-29. The zero-trust and least-privilege walkthrough remains on the chapter page.

RBAC employs pre-defined roles that carry a specific set of privileges. ABAC evaluates
principal, resource and context attributes to reach a decision. Authorization is determined by evaluating attributes associated with the subject, object,
requested operations, and, where applicable, environment conditions against policy.

Policy decision and enforcement can be separate components: a policy decision point evaluates
policy and attributes, a policy enforcement point applies the decision, a policy information
point supplies attributes and a policy administration point manages policy. Distributed
placement makes attribute freshness and audit harder.

In ACL/IBAC systems, failure to remove or revoke access over time leads to users accumulating
privileges. ACLs work on the attribute of identity; RBAC works on the attribute of role.

**Limits.** Policy/attribute freshness and decision logging are costs; an unexplainable deny or
allow is a production incident, not a policy detail. Attribute sources need freshness SLAs; a
stale attribute is an authorization failure, not a cache miss.

**Source boundary.** The NIST SP 800-162 record supports the PDP/PEP/PIP/PAP separation and
policy administration. Revocation mechanics, role explosion and attribute-freshness guidance
above remain synthetic.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V09/C05 — Identity, authorization and threat modeling](README.md) |
| Originating page | [Authorization policy and least privilege](authorization-policy-and-least-privilege.md#rbac-abac) |

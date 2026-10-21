---
metadata_version: 1
id: "tycho.page.e9524931fbcc4b4e833f6b0465a27698"
kind: "page"
parent_id: "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
canonical_path: "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/threat-identity.md"
title: "Threat models and authenticated identity"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Which asset and principal are protected and what does authentication establish?"
route_hints:
  questions:
    - "Which asset and principal are protected and what does authentication establish?"
  prerequisites:
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
  related_ids:
    - "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.43bf5d29ec5b4327b0c4cf57391679da"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "threat"
    - "identity"
evidence_scope:
  source_ids:
    - "src.oauth-security"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.dde63373c50f4f4a80e727b6e160def5; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Threat models and authenticated identity

**Owning question:** Which asset and principal are protected and what does authentication establish?

This page belongs to [V09/C05 — Identity, authorization and threat modeling](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:1 -->
## 1. Start with protected outcomes and an explicit threat model

Name assets: user records, authorization and entitlement policy, secrets and signing credentials, immutable artifacts, event streams, backups, operational metadata, financial or other sensitive values *only when actually in system scope*, and the integrity of the business state owner. Then name legitimate principals and untrusted callers.

A minimal threat worksheet includes:

| Dimension | Questions | Evidence needed |
|---|---|---|
| Actor and capability | End user, service, administrator, delegated agent, job, contractor? | Real identity source, delegation and credential lifetime |
| Entry point | API, callback, web session, message, command, import or administrative workflow? | Authenticated/unauthenticated routes and origin/context checks |
| Protected object | Which record/tenant/field or side effect can be read/changed? | Object ownership and data classification |
| Trust boundary | Where does untrusted input become a privileged action or identity? | Entry/egress and middleware/service enforcement paths |
| Threat | Impersonation, object-level authorization bypass, credential disclosure, replay, resource exhaustion, tampering, data exfiltration? | Known attack surface and adversary assumptions |
| Control | Enforce permission, bind token audience, validate object ownership, bound work, isolate data and record audit? | Verified implementation and failure response |
| Residual risk | What still fails if identity service, policy engine, cache or auditor is unavailable? | Fault injection and explicit incident response |

Do not infer safety from data-plane TLS if an internal service accepts a caller-supplied tenant ID without object authorization. A successful authentication answers **who the caller is** under one assurance model; it does not say that the caller may read any named resource.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:2 -->
## 2. Authentication is not authorization

NIST's SP 800-63 Revision 4 covers identity proofing, authentication and federation separately, with assurance expectations depending on the actual digital identity context. [E01] A declared assurance level is meaningful only when the implemented authenticators, verifiers and lifecycle satisfy its corresponding controls; it cannot be inferred from using a popular login vendor.

Authorization must evaluate **principal, action, object, context and policy version**, often including tenant boundary and delegation constraints. OWASP's Authorization Cheat Sheet recommends deny-by-default and checking permission on every request. [E02]

Compare policy models conditionally:

- **RBAC:** roles map to permissions. Clear for stable responsibility sets, but role explosion or coarse resource ownership can create over-privilege.
- **ABAC:** permissions depend on attributes such as tenant, classification, action and context. Expressive, but decision provenance, policy consistency and attribute freshness become important.
- **Relationship-based controls:** evaluate explicit relationships such as owner, project member or delegated editor, suitable for complex sharing. Model version, relationship graph consistency and query cost must be tested; this is an *authorization data model*, not Tycho's removed internal knowledge graph.
- **Capability tokens:** delegation is expressed through held authority, bounded by expiry, audience and revocation. Possession alone may be unsafe if tokens can be replayed outside the intended holder or resource.

A useful split is the **Policy Enforcement Point** near the protected operation and the **Policy Decision Point** evaluating the policy, possibly with administration and information services. A remote policy decision is not enforcement unless the application correctly binds and applies that result to the actual object/action. OWASP's Authorization Patterns documentation clarifies these boundaries. [E03]

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](identity-authorization-and-isolation.md) |
| Next | [Continue the reasoning](object-credentials.md) |
| Integrated question | [Original scenario and limits](identity-authorization-and-isolation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

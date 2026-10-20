---
metadata_version: 1
id: "tycho.page.43bf5d29ec5b4327b0c4cf57391679da"
kind: "page"
parent_id: "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
canonical_path: "book/volumes/v09/c05/object-credentials.md"
title: "Object permission, credentials and isolation"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Where must resource authorization be enforced across direct and indirect paths?"
route_hints:
  questions:
    - "Where must resource authorization be enforced across direct and indirect paths?"
  prerequisites:
    - "tycho.page.e9524931fbcc4b4e833f6b0465a27698"
  related_ids:
    - "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.96c78f4525504257baf5861e2397dab8"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "object"
    - "credentials"
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
# Object permission, credentials and isolation

**Owning question:** Where must resource authorization be enforced across direct and indirect paths?

This page belongs to [V09/C05 — Identity, authorization and threat modeling](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:3 -->
## 3. Object-level authorization and multitenancy

OWASP's API Security Top 10 2023 highlights broken object-level and object-property-level authorization risks. [E04] The fact that an API endpoint requires a valid token does not authorize every ID presented in its path or body.

For a fictional multi-tenant workshop service, a service could authenticate user U then fetch registration R by an arbitrary registration ID. A proper authorization gate must establish that U is permitted to see/change R under the current tenant/ownership policy, not trust a caller's claim that R belongs to their tenant.

The isolation boundary must cover:

1. Route/controller method and *every* alternative access path, including exports, search, batch jobs and admin APIs.
2. Repository/data-layer queries and updates, not only presentation filters that can be bypassed.
3. Event handlers, caches, object stores and tenant-specific indexes that might retain or replay another tenant's data.
4. Background jobs, cross-tenant aggregation and administrative delegation with explicit scope.
5. Logs, metrics, trace attributes and error messages that might leak identifiers or payloads.

A shared database can be legitimate if object/tenant isolation is enforceable and tested. A separate database or runtime can reduce some blast radius, but it does **not** replace permission checks, credential separation and cross-tenant backup/restore controls.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:4 -->
## 4. Token and credential boundaries

OAuth 2.0 Security Best Current Practice, RFC 9700, addresses mitigations including sender constraints, audience-restricted access tokens and refresh-token rotation for applicable public clients. [E05] An access token accepted by one resource should not automatically be reusable at another resource.

Design a credential contract with:
- token issuer, intended audience and scope,
- authenticated client/resource relationship,
- expiry, revocation, refresh/rotation and incident response,
- key distribution/rotation and trust-root recovery,
- clock skew, cache lifetime and disconnected-policy behavior,
- protection against token exfiltration in URLs, logs and traces,
- a test that attempts cross-resource token reuse and must be rejected.

Long-lived service credentials are not a justification to give all microservices broad access to the entire data estate. Conversely, elaborate per-service identity infrastructure may exceed the actual threats and operations capacity of a small modular application. Selection requires an observed workload, service boundary and supported operational design.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:5 -->
## 5. Boundaries of network and service isolation

| Control | Intended protection | What it does NOT prove |
|---|---|---|
| TLS / mutual TLS | Connection confidentiality, integrity and authenticated endpoint depending on configuration | Authorization for a particular business object |
| Ingress/gateway authentication | Filter unauthenticated traffic and apply coarse policy | Every internal path or async consumer enforces business permissions |
| Network policies / segments | Restrict permitted network reachability | A reachable compromised service cannot abuse permitted actions |
| Container/VM isolation | Bound process/runtime reach and some resource ownership | Correct tenant-level application access and data encryption |
| Row/object permissions | Bound data operations at authority | Caller identity and the current policy were accurately supplied |
| Audit | Record approved/rejected actions with designed integrity | Zero-loss audit unless transactional and failure behavior are actually proven |
| Rate limit/admission | Reduce denial-of-service amplification and work overload | Confident user identity if proxies/keys are misconfigured |

**Failure modes:** policy service outage, cached allow decision past revocation, identity key rotation causing old token rejection, shared-secret reuse, tenant key misrouting, log-side secret disclosure, cross-service confused deputy, mis-scoped administrative capability, replayed event without authorization revalidation.

For every external actor, establish the intended deny behavior under uncertain policy and isolate high-risk operations from read-only degradation modes. An unsafe availability optimization is silently allowing previously unauthorized writes when the policy engine is unreachable.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](threat-identity.md) |
| Next | [Continue the reasoning](security-tests.md) |
| Integrated question | [Original scenario and limits](identity-authorization-and-isolation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

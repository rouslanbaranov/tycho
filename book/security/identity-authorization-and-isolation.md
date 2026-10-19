---
metadata_version: 1
id: "tycho.page.dde63373c50f4f4a80e727b6e160def5"
kind: "page"
parent_id: "tycho.landing.3870e6370654489c949e098b9acd1840"
canonical_path: "book/security/identity-authorization-and-isolation.md"
title: "Threat boundaries, identity, authorization and service isolation"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Reader entry for Threat boundaries, identity, authorization and service isolation. Scope includes 1. Start with protected outcomes and an explicit threat model; 2. Authentication is not authorization; 3. Object-level authorization and multitenancy."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Threat boundaries, identity, authorization and service isolation?"
  prerequisites: []
  related_ids: []
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Threat"
    - "boundaries"
    - "identity"
    - "authorization"
    - "and"
    - "service"
    - "isolation"
evidence_scope:
  source_ids:
    - "src.oauth-security"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Threat boundaries, identity, authorization and service isolation

> Original Tycho E14-12 [#90](https://github.com/rouslanbaranov/tycho/issues/90), public-specification reading 2026-10-19. This is a decision-method chapter, **not** a penetration test, vulnerability assessment, product certification, configured policy or observed security guarantee.

## Purpose and mission

Distributed application security is not achieved by choosing a transport protocol or drawing a network perimeter. It depends on **who can act, what is being protected, which boundary evaluates and enforces the decision, and what happens when identity, policy, network and audit dependencies fail**.

The core question is: which trust boundaries, authorization checks and isolation controls are required by the system's actual threat model and data ownership—not by an architectural fashion?

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

## 2. Authentication is not authorization

NIST's SP 800-63 Revision 4 covers identity proofing, authentication and federation separately, with assurance expectations depending on the actual digital identity context. [E01] A declared assurance level is meaningful only when the implemented authenticators, verifiers and lifecycle satisfy its corresponding controls; it cannot be inferred from using a popular login vendor.

Authorization must evaluate **principal, action, object, context and policy version**, often including tenant boundary and delegation constraints. OWASP's Authorization Cheat Sheet recommends deny-by-default and checking permission on every request. [E02]

Compare policy models conditionally:

- **RBAC:** roles map to permissions. Clear for stable responsibility sets, but role explosion or coarse resource ownership can create over-privilege.
- **ABAC:** permissions depend on attributes such as tenant, classification, action and context. Expressive, but decision provenance, policy consistency and attribute freshness become important.
- **Relationship-based controls:** evaluate explicit relationships such as owner, project member or delegated editor, suitable for complex sharing. Model version, relationship graph consistency and query cost must be tested; this is an *authorization data model*, not Tycho's removed internal knowledge graph.
- **Capability tokens:** delegation is expressed through held authority, bounded by expiry, audience and revocation. Possession alone may be unsafe if tokens can be replayed outside the intended holder or resource.

A useful split is the **Policy Enforcement Point** near the protected operation and the **Policy Decision Point** evaluating the policy, possibly with administration and information services. A remote policy decision is not enforcement unless the application correctly binds and applies that result to the actual object/action. OWASP's Authorization Patterns documentation clarifies these boundaries. [E03]

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

## 6. Synthetic architecture and incident

Assume a completely fictional document-sharing service with authenticated users, independent tenant namespaces, object storage and asynchronous preview generation.

**Design A — shared service and shared store:** one deployment, tenant-aware queries, enforced object authorization, partitioned logical namespaces and small operations footprint. Requirements: systematic policy gates on every path, secure worker context propagation and tested query isolation.

**Design B — isolated per-tenant runtimes/data:** more explicit tenant-level resource separation at higher cost and more orchestration/configuration responsibilities. Requirements: identity/secret lifecycle for every isolation boundary, correct routing, cross-tenant admin restrictions and auditable provisioning/restore.

An attacker submits a valid-looking document ID belonging to a different tenant. If the API validates the token but not resource ownership, Design A may leak the object. Yet Design B may also leak when a shared gateway routes an ID to a permitted but incorrect backend. The **same object-level authorization invariant** remains necessary.

Hypothetical incident:
1. A tenant-admin role is granted too broadly due to stale group membership and policy caching.
2. A background export job uses service-level read authority beyond the user's original delegation.
3. Data are exported to a shared result area, and the audit pipeline cannot reach its collector.
4. A green API health check and a valid login conceal both authorization and audit failures.

Repair requires policy scope/expiry and delegation fixes, restricted export job permissions, destination ownership validation, intentional fail-closed choices for high-risk actions, secure audit reconciliation and negative cross-tenant tests. This is a teaching scenario, not a discovered vulnerability.

## 7. Verification and decision gates

For each candidate architecture, preserve at least the following test classes:

- Unknown and malformed identity claims, wrong issuer/audience, expired or revoked tokens; identity outage.
- Cross-tenant same-object-ID collisions, alternate API paths, batch/list pagination, search filters and cache isolation.
- Owner-versus-delegate actions, role downgrade and policy cache invalidation.
- Resource exhaustion under unauthenticated/denied requests; budgets and client retries.
- Privacy of logs, traces and audits including error paths; no secret leakage in telemetry.
- Restore and rollback of policy/configuration versions without silently restoring broad authority.
- Read-only and write paths under authorization dependency failure; reconcile durable audit events against authoritative business effects.

**Architecture decision:** prefer the minimal topology that can actually enforce these business and trust boundaries with demonstrated denial paths. A microservice split, gateway or service mesh is not an authorization strategy.

## 8. Exact public source evidence

| Ref | Primary source and inspected section, 2026-10-19 | Validity boundary |
|---|---|---|
| E01 | [NIST SP 800-63-4](https://pages.nist.gov/800-63-4/), published revision and [authentication assurance](https://pages.nist.gov/800-63-4/sp800-63b/aal/) | Relevant digital identity/auth assurance concepts, not an achieved compliance claim |
| E02 | [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), *Deny by Default* and *Validate Permissions on Every Request* | Preventive design guidance, not proof every route is enforced |
| E03 | [OWASP Authorization Patterns](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Patterns_Cheat_Sheet.html), PEP/PDP/service-level authorization | Enforcement/decision separation, not an installed reference policy engine |
| E04 | [OWASP API Security Top 10, 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/), API1/API3 categories | Risk classification, not a discovered vulnerability in Tycho |
| E05 | [RFC 9700 OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700.html), token privileges, sender constraint and refresh-token handling | OAuth-specific recommendations, not generic correctness guarantees for every identity protocol |

No operating security policy, cryptographic key, production attack test, formal threat assessment, independent auditor or penetration test has been implemented or carried out. This is a conceptual engineering chapter with falsifiable checks, not a certified deployment.

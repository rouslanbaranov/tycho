---
metadata_version: 1
id: "tycho.page.43bf5d29ec5b4327b0c4cf57391679da"
kind: "page"
parent_id: "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
canonical_path: "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/object-credentials.md"
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
updated_at: "2026-10-22"
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

> **Pattern atlas:**
> [Valet Key](../../v11-pattern-atlas/c11-security-operations/README.md#valet-key) — decision conditions and contraindications.

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

## Key rotation, revocation and unavailable authorities

**Enrichment contract:** distinguish data encryption keys, token-signing keys, transport certificates and resource permissions. Their replacement and revocation have different correctness and availability consequences.

OWASP key-management guidance treats generation, storage, rotation, compromise, backup and destruction as a lifecycle. Its REST guidance requires configured token validation, applicable claims and access control; a cryptographically valid token can still outlive a revoked session or object permission.

### Original routine rotation plan

A fictional service verifies tokens signed by K1 and will introduce K2. Before issuing K2-only tokens, distribute the trusted K2 verification material to verifiers. Keep K1 acceptance only for the explicitly permitted overlap of existing tokens and policy. Distinguish signing authority from public verification material: retaining a public key does not require allowing new signatures under its private counterpart.

Record issuer, allowed algorithms, audience, token lifetime, clock tolerance, verification-key source and cached-key horizon. Do not allow untrusted token fields to select an arbitrary key URL or algorithm. A key identifier selects inside a configured trust relationship; it is not that relationship itself.

| Event | Required policy |
|---|---|
| Planned signing-key rollover | Verify overlap against old token lifetime and verifier distribution |
| Private signing key compromised | Decide emergency rejection and session re-establishment; normal overlap may be unsafe |
| Unknown key while authority unavailable | Do not accept unverifiable credentials |
| Known unexpired credential while authority unavailable | Continue only within its configured offline-validation and current-permission contract |
| Object permission revoked | Recheck at the resource; token signature alone does not restore permission |
| Encryption key lost | Invoke the tested recovery policy or acknowledge permanent unreadability |

A fictional five-minute token and a two-minute clock allowance can expose a longer acceptance window than the nominal five minutes. The exact bound depends on issuer/verifier clocks and configured checks; do not add allowances casually or reuse these invented durations as defaults.

### Encryption rotation is not signing rotation

Replacing a key used to wrap data keys is different from re-encrypting every object. Record which key versions protect which data, which identities can unwrap them, how old backups regain access, and when deletion is allowed. Retiring a live key before the oldest retained backup no longer needs it can invalidate recovery without deleting any bytes.

Conversely, restoring a compromised key merely to make a backup readable may violate the incident threat model. Recovery must re-establish trustworthy access, not just availability. Separate key custody, application access, audit and emergency operations; avoid keeping the only recovery material in the system it must recover.

### Revocation and cached authorization

If a service caches an allow decision, define maximum stale permission, invalidation delivery and policy-service outage behavior. A stream authorized at connection establishment needs a policy for later access changes. Revocation of a user, a session, a key and one object are separate scopes; their blast radii differ.

Proposed negative cases: old valid token after logout, wrong issuer with a matching key ID, rotated trust material missing on one verifier, revoked tenant access during an open stream, unavailable key service on restart, and a restored backup requiring an intentionally retired key. Require explicit deny/unavailable outcomes and no secret-bearing logs.

### Evidence and limits

Selected passages inspected 2026-10-20: [Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) (lifecycle/rotation/compromise), [REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) (JWT and endpoint access control). The rollover plan, hypothetical durations and outage decisions are original design reasoning. No cryptographic implementation, issuer, key service or penetration test was executed; select supported algorithms and exact product procedures through separate versioned evidence.

The frontmatter leaves `source_inspection_date` null because this decomposition source block keeps
its inherited metadata; the 2026-10-20 date above is a source-scope inspection date, not page-level
acceptance.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](threat-identity.md) |
| Next | [Continue the reasoning](security-tests.md) |
| Integrated question | [Original scenario and limits](identity-authorization-and-isolation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is
not the main subject of this page. They are synthetic design guidance, not
measured evidence, and they do not create a new source claim.

### Valet Key

A valet key is a time-limited credential that grants access to specific resources and
allows only predefined operations. Applications issue keys to clients so the client can
perform the operation without the application handling the data transfer.

The key should allow only the actions necessary to complete the operation.

If leaked or compromised, the key unlocks the target item and makes it available for
malicious use during its validity period; a key can usually be revoked or disabled.
Applications can invalidate the key when the client reports that the transfer is complete.

The other is to implement the Gateway Routing pattern to set up an endpoint where clients
use proxied access to storage.

**Limits.** A key that cannot be revoked or audited is a standing exposure.

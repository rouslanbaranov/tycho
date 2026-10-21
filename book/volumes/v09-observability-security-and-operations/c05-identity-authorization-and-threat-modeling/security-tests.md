---
metadata_version: 1
id: "tycho.page.96c78f4525504257baf5861e2397dab8"
kind: "page"
parent_id: "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
canonical_path: "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/security-tests.md"
title: "Synthetic attacks and decision gates"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Which denied or confused-deputy outcome would invalidate the design?"
route_hints:
  questions:
    - "Which denied or confused-deputy outcome would invalidate the design?"
  prerequisites:
    - "tycho.page.43bf5d29ec5b4327b0c4cf57391679da"
  related_ids:
    - "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "security"
    - "tests"
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
# Synthetic attacks and decision gates

**Owning question:** Which denied or confused-deputy outcome would invalidate the design?

This page belongs to [V09/C05 — Identity, authorization and threat modeling](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:6 -->
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


### Worked multi-tenant object authorization: a valid token is not an object grant

A **fictional** client from tenant A authenticates successfully and sends `GET /tenants/B/bookings/R7`. The API gateway validates the token signature and expiry, then forwards the call to an internal booking service. If the service assumes that any gateway-approved request is authorized, it may return B's booking despite valid authentication.

| Control point | Correct decision | Negative case |
|---|---|---|
| Identity verification | Validate issuer, audience, lifetime and applicable credential binding | Token accepted for another audience |
| Object authorization | Check caller subject, tenant, object ownership and intended action at the actual authority | A reads or modifies B's booking through guessed ID |
| Cache and search | Apply object ACLs to cached bodies, summaries, result IDs and linked records | A receives B's cached incident via a permitted public page |
| Event consumer | Preserve an authorized purpose and target during asynchronous processing | Service credential expands a user's denied mutation into an allowed background job |
| Audit/recovery | Record accountable subject, object, policy version and denied/allowed outcome with minimal retained data | Sampled trace presented as a complete security audit |

[OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) prescribes deny-by-default and checks on every request. Its [Authorization Patterns guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Patterns_Cheat_Sheet.html) distinguishes policy decision and enforcement responsibilities. These are public design rules, **not a security assessment of this fictional deployment**. In a distributed service, a gateway-level authentication check and an internal network address cannot replace resource-level authorization.

**Proposed, not run:** test two tenants sharing a cache, guessed object IDs, stale privileges after revocation, background message replay, service-account scope and authorization timeout. A failure or unavailable policy evaluator must have an explicit fail-closed or separately approved safe-degradation rule; defaulting to allow in the name of availability violates the protected outcome. Token rotation and revocation may require cache invalidation and re-evaluation, not merely a one-time login.

**Decision boundary:** a single application with consistent object policy enforcement can be safer and simpler than a split service fleet with duplicated, drifting policies. A service split is justified only with verified operational ownership, isolation and tests of the cross-boundary privilege flow. Agent-specific untrusted retrieval belongs to [the separate V09/C07 owner](../c07-safety-isolation-and-privacy-in-agent-accessible-services/safe-agent-access-and-knowledge-isolation.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:7 -->
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

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](object-credentials.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](identity-authorization-and-isolation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

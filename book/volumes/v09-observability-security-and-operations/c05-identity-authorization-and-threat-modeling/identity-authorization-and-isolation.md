---
metadata_version: 1
id: "tycho.page.dde63373c50f4f4a80e727b6e160def5"
kind: "page"
parent_id: "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
canonical_path: "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md"
title: "Threat boundaries, identity, authorization and service isolation"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Integrated decision and bounded source limits for Identity, authorization and threat modeling. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Where do trust boundaries and permission checks have to sit?"
  prerequisites: []
  related_ids:
    - "tycho.page.e9524931fbcc4b4e833f6b0465a27698"
    - "tycho.page.43bf5d29ec5b4327b0c4cf57391679da"
    - "tycho.page.96c78f4525504257baf5861e2397dab8"
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
    - "src.istio"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-26"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:-1 -->

# Identity and workload trust

> Original Tycho E14-12 [#90](https://github.com/rouslanbaranov/tycho/issues/90), public-specification reading 2026-10-19. This is a decision-method chapter, **not** a penetration test, vulnerability assessment, product certification, configured policy or observed security guarantee. The content_review field retains the decomposition-era draft state; no independent acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Federated Identity](../../v11-pattern-atlas/c11-security-operations/federated-identity.md#federated-identity) — decision conditions and contraindications.
> [Workload Identity / mTLS](../../v11-pattern-atlas/c11-security-operations/workload-identity-mtls.md#workload-identity--mtls) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:0 -->
## Purpose and mission

Distributed application security is not achieved by choosing a transport protocol or drawing a network perimeter. It depends on **who can act, what is being protected, which boundary evaluates and enforces the decision, and what happens when identity, policy, network and audit dependencies fail**.

The core question is: which trust boundaries, authorization checks and isolation controls are required by the system's actual threat model and data ownership—not by an architectural fashion?

<!-- /tycho-question-source -->

## Integrated decision and reading route

Place identity and resource authorization at the actual effect boundary, including object, tenant and credential scope.

Network reachability or a valid token does not grant permission to every object; test denied operations through indirect paths.

Authorization and least-privilege decisions are owned by [authorization policy](authorization-policy-and-least-privilege.md); tenant isolation is owned by [multitenant isolation](multitenant-isolation.md). This page keeps the identity mechanisms.

The detailed pages separate the mechanisms that make this decision conditional:

- [Threat models and authenticated identity](threat-identity.md) — Which asset and principal are protected and what does authentication establish?
- [Object permission, credentials and isolation](object-credentials.md) — Where must resource authorization be enforced across direct and indirect paths?
- [Synthetic attacks and decision gates](security-tests.md) — Which denied or confused-deputy outcome would invalidate the design?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance unless a sentence explicitly attributes the claim
to a dedicated source record; all other guidance remains synthetic. They are not measured
evidence and do not create a new source claim by themselves.

### Federated Identity

A federation Entity publishes a signed Entity Statement: a JWT whose subject is the Entity and
whose issuer is the party that issued it. A resource server verifies that an access token was meant
for it and refuses otherwise. Entity Configuration expiration controls how often federation keys are
refetched; expired metadata must be refreshed. Entity Statements can be resolved through a trust
chain, and a Trust Anchor signs subordinate statements about its immediate subordinates. Federation
key rollover updates the jwks member before old keys are removed. Bilateral direct trust between two organizations is
the alternative when multilateral third-party mediation is impractical. A trust chain starts with the
Entity Configuration and ends at a Trust Anchor; metadata policies are applied along the chain.
### Workload Identity-mTLS

Workload identity gives each running workload a verifiable identity. Mutual TLS authenticates
both ends of a service connection with automatically rotated credentials. Secure naming verifies that the service account in the server certificate is authorized to run
the target service.

Expired or shared credentials break authentication. Istio monitors workload certificate expiry and
periodically rotates certificates and keys. Permissive mTLS mode accepts both mutual TLS and plain text traffic; it is most useful
during migrations when workloads without a sidecar cannot use mutual TLS, and should switch
to STRICT once workloads are migrated with sidecar injection.

**Limits.** PKI, certificate rotation and revocation are operational costs; a valid certificate
authenticates the workload, not every operation it requests. Certificate issuance availability
is part of the request path, and a failed rotation can be an outage; both claims are plausible
but synthetic, and the cited page does not measure them.

**Source boundary.** Only the following claims are supported by the cited
[read.batch6-istio.2026-10-21](../../../../edition/patterns/reading-ledger.v1.json) record:
workload identity binding, certificate issuance and rotation, mTLS authentication,
permissive mode and authorization policy. Certificate revocation, trust-root bootstrap, key storage, lifetime
policy and rotation-failure impact are not in the cited sections; all other guidance in this
section remains synthetic.

## Navigation

Parent: [identity chapter](README.md). Next: [authorization policy](authorization-policy-and-least-privilege.md).

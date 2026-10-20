---
metadata_version: 1
id: "tycho.page.dde63373c50f4f4a80e727b6e160def5"
kind: "page"
parent_id: "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
canonical_path: "book/volumes/v09/c05/identity-authorization-and-isolation.md"
title: "Threat boundaries, identity, authorization and service isolation"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Integrated question, original scenario and transfer limits for Identity, authorization and threat modeling. Detailed mechanisms have separate question owners."
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
<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:-1 -->

# Threat boundaries, identity, authorization and service isolation

> Original Tycho E14-12 [#90](https://github.com/rouslanbaranov/tycho/issues/90), public-specification reading 2026-10-19. This is a decision-method chapter, **not** a penetration test, vulnerability assessment, product certification, configured policy or observed security guarantee.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.dde63373c50f4f4a80e727b6e160def5:0 -->
## Purpose and mission

Distributed application security is not achieved by choosing a transport protocol or drawing a network perimeter. It depends on **who can act, what is being protected, which boundary evaluates and enforces the decision, and what happens when identity, policy, network and audit dependencies fail**.

The core question is: which trust boundaries, authorization checks and isolation controls are required by the system's actual threat model and data ownership—not by an architectural fashion?

<!-- /tycho-question-source -->

## Integrated decision and reading route

Place identity and resource authorization at the actual effect boundary, including object, tenant and credential scope.

Network reachability or a valid token does not grant permission to every object; test denied operations through indirect paths.

The detailed pages separate the mechanisms that make this decision conditional:

- [Threat models and authenticated identity](threat-identity.md) — Which asset and principal are protected and what does authentication establish?
- [Object permission, credentials and isolation](object-credentials.md) — Where must resource authorization be enforced across direct and indirect paths?
- [Synthetic attacks and decision gates](security-tests.md) — Which denied or confused-deputy outcome would invalidate the design?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

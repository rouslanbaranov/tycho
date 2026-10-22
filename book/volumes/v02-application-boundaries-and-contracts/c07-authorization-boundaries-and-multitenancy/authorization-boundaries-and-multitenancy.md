---
metadata_version: 1
id: "tycho.page.31cda61d174248eaa326559d256ce352"
kind: "page"
parent_id: "tycho.chapter.5426707ddf264b758016aafe71f342b7"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c07-authorization-boundaries-and-multitenancy/authorization-boundaries-and-multitenancy.md"
title: "Authorization boundaries and multitenancy: domain ownership and isolation"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Authorization boundaries and multitenancy. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What must be isolated between clients, organizations and data owners?"
  prerequisites: []
  related_ids:
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
    - "tycho.page.81efb7e6d72349768b6f202845cbe35e"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.0ae1aabac3b64c2f924cc427684bdbab"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.6bbeb9533a324758a1b970471c5b04e1"
    - "tycho.page.c0dd410ffc6344b78e5a9c72589bf06f"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Authorization"
    - "boundaries"
    - "and"
    - "multitenancy"
    - "domain"
    - "ownership"
    - "isolation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.31cda61d174248eaa326559d256ce352:-1 -->

# Authorization boundaries and multitenancy: domain ownership and isolation

> **Tycho book chapter draft V02/C07**, 2026-10-19. Original abstract design and hypothetical fixtures. Public OWASP and independently available multitenancy design guidance consulted. No real tenant data, authorization engine, system credentials, or security assessment was used. [Threat modeling, identity and isolation](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md) owns the security primitives; this chapter owns how tenancy affects *application decomposition and domain authority*.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Gatekeeper](../../v11-pattern-atlas/c02-api-communication/README.md#gatekeeper) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.31cda61d174248eaa326559d256ce352:0 -->
## Purpose and mission

A deployment can share code and infrastructure while serving users who must never see or mutate each other's state. A logical domain boundary may contain many tenants; a physical database may contain only one. **Tenancy, authorization, domain ownership and runtime isolation are different axes**. Treating tenant ID as a cosmetic query field leads to cross-tenant reads, incorrect caches, unintended background effects and unfair resource consumption.

The architectural question is: **Which isolation guarantees are hard, which may be shared, and at which authoritative boundary are they enforced?** A design should not select one database per tenant or one common database merely because one appears easier to operate.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.31cda61d174248eaa326559d256ce352:8 -->
## Engineering walkthrough — Tenant isolation across four non-equivalent layers

**Original synthetic negative test:** Tenant A authenticates and calls an authorized `GET /catalogue`. A joined search result points to Tenant B's maintenance ticket; a shared Redis key stores an unscoped catalogue summary; an internal event consumer uses a service credential with broader scope than the original user. All infrastructure can be healthy while a cross-tenant disclosure occurs.

| Layer | Required independent boundary | Failure that a separate database alone cannot prevent |
|---|---|---|
| Authentication | Verify subject/issuer/audience | Identity of A mistaken for authority over B |
| Object authorization | Check subject, action, object and tenant at every sensitive authority | Guessable B booking ID returned by a shared API |
| Data placement | Tenant-scoped query, partition or store and backup/restore contract | Shared read-projection joins keys without the tenant predicate |
| Infrastructure/resources | Explicit CPU/connection/bandwidth isolation objectives | A's burst exhausts a common pool despite correct data ACLs |

On a revocation, caches and asynchronous consumers must not continue to serve previously authorized B data to A. A tenant ID in a URL is untrusted input; deriving it from a signed session may help but still does not establish access to an arbitrary object. A migration from shared rows to separate databases needs authoritative tenant inventory, dual-read/write compatibility, audit, backup and a no-return boundary.

**Proposed, not executed:** send cross-tenant IDs to API, cache, message and bulk-export endpoints; force ACL revocation between search and source expansion; saturate shared downstream resources to measure noisy-neighbor effect separately from confidentiality. The OWASP Authorization references support deny-by-default patterns; they do not certify security or an achieved isolation tier here.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.31cda61d174248eaa326559d256ce352:9 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — Data Project identity](../../../cases/netflix-data-project-durable-workload-identity.md)**. **Relevant mechanism or architectural contrast:** Workload identity can outlive departing human owners; entitlement, execution and ownership identities need separate migration. **Not established by this report/playbook:** A first-party deployment account does not prove all Netflix jobs migrated, global least-privilege compliance or an independent audit.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Design tenant identity, authorization, resource sharing and data placement as separate but composing boundaries.

A tenant-aware query does not protect a wrongly scoped cache or background task; isolation must hold across the complete effect path.

The detailed pages separate the mechanisms that make this decision conditional:

- [Isolation dimensions and placement](isolation-axes.md) — How do domain, tenant, authorization and runtime isolation differ?
- [Tenant-scoped effects and migration](tenant-effects.md) — Which cache, task and data-movement paths can bypass otherwise correct tenant scoping?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Gatekeeper

A gatekeeper is a dedicated request-validation boundary that authenticates the caller and evaluates
coarse authorization before forwarding a request to the protected service. The protected service
must reject calls that bypass the gatekeeper, or repeat the security-relevant checks, so the
boundary cannot be sidestepped by an alternate route.

A stale policy or an undeclared direct path defeats the check while dashboards remain green; combine
network policy, denial logs and a bypass test in the acceptance evidence. Enforce authorization
inside the service at each effect boundary; use a gatekeeper when it centralizes a policy that every
route must apply and the bypass surface is closed.

**Limits.** Gatekeeper availability, policy freshness and bypass routes are costs; a gatekeeper
that only authenticates without resource authorization shifts the decision.

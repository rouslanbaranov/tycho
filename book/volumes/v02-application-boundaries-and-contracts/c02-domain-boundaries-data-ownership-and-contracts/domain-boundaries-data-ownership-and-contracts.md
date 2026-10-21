---
metadata_version: 1
id: "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
kind: "page"
parent_id: "tycho.chapter.7031445877fb4f8d831d962d170521c8"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c02-domain-boundaries-data-ownership-and-contracts/domain-boundaries-data-ownership-and-contracts.md"
title: "Domain boundaries, data ownership and contract evolution"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Domain boundaries, data ownership and contracts. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "When should business capabilities form module or service boundaries?"
  prerequisites: []
  related_ids:
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
    - "tycho.page.55c22c6b24ff456a95dd9cc3d71ca238"
    - "tycho.page.91c10dd544b441ddb940aaee24825638"
    - "tycho.page.461b24a5b47b4b8e82d37125cac20c8d"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Domain"
    - "boundaries"
    - "data"
    - "ownership"
    - "and"
    - "contract"
    - "evolution"
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
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:-1 -->

# Domain boundaries, data ownership and contract evolution

> **Tycho manuscript draft — proposed V02/C02**, 2026-10-19. Original explanatory text and fictional examples; independently public context-design references. This chapter is not a model of any real organization or its software. No operational measurement, customer research, migration or independent design review has been performed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:0 -->
## Purpose and mission

Business concepts are not naturally partitioned into one universal data model. "Available", "reserved" and "delivered" can each mean different things to a catalogue, a reservation capability and a delivery coordinator. Architecture fails when we assume that the same word implies the same invariant, owner or state transition everywhere.

A **domain boundary** defines the meaning and scope of a model. A **module boundary** controls implementation dependencies. A **data ownership boundary** decides who can authoritatively change state. An **API/event contract** communicates chosen facts between boundaries. A **deployment boundary** decides what can be released or fail independently. These distinctions are related but are not the same.

The independent [Fowler bounded-context explanation (2014)](https://martinfowler.com/bliki/BoundedContext.html) describes internally consistent models and explicit relationships across contexts; it does not prescribe one process or database per context. The [arc42 context guidance](https://docs.arc42.org/section-3/) helps document external business exchanges separately from protocols. This chapter owns the *semantics and authority*; [application style choices](../../../application/architecture-styles-and-module-boundaries.md) own the packaging and deployment trade-offs.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:10 -->
## Engineering walkthrough — Two teams change the same concept during a schema transition

**Original hypothetical conflict:** a Catalogue team owns a `unit` identity; a Booking team owns reservation decisions but maintains a read projection of unit labels. Catalogue changes `asset_code` from a physical-unit identifier to a model identifier while Booking still interprets it as one reservable unit. Field types remain strings; JSON schema compatibility alone would conceal a semantic break.

| Ownership element | Declared rule | Counterexample |
|---|---|---|
| Unit meaning | Catalogue controls immutable unit identity and publishes semantic version | Booking invents a new unit by copying the new model code |
| Reservation authority | Booking alone commits exclusive reservation effects | Both Catalogue and Booking accept bookings against different views |
| Read projection | Booking stores versioned Catalogue facts, can be stale for display | Projection freshness is treated as authorization to mutate authority |
| Coexistence | Old/new field readers use explicit translation or rejection | Unknown mapping silently defaults to one arbitrary unit |

The safe transition first introduces distinct model and physical-unit identities. The old `asset_code` contract stays available while consumers migrate, with unmappable records quarantined; only then may its meaning be retired. Two independent authoritative writers are not permitted merely because teams have distinct services. **Failure:** a delayed old event arrives after the new projection has advanced; it must not overwrite the new identity under the event-order/version policy.

**Proposed, not executed:** issue concurrent booking and identity-update commands from both teams, replay a late legacy event and verify a single state owner, nonambiguous mapping and explicit unknown-state handling. A bounded-context map explains language/ownership; it is not an infrastructure knowledge graph or proof of source-version compatibility. Contradiction with observed consumer behavior blocks cutover.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:11 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Uber — DOMA](../../../cases/uber-doma-domains.md)**. **Relevant mechanism or architectural contrast:** Governing dependencies after service proliferation can reduce team coupling without adding indiscriminate services. **Not established by this report/playbook:** Anecdotal high fanout and original adoption data are not a universal optimum domain size or architecture score.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Assign each invariant and authoritative state transition to an owner before dividing storage or deployment.

Two teams using the same entity name can disagree on its legal transitions; schema agreement alone does not resolve ownership.

The detailed pages separate the mechanisms that make this decision conditional:

- [Domain semantics and authoritative ownership](domain-authority.md) — When do shared names conceal different invariants and owners?
- [Semantic adapters and evolving contracts](boundary-evolution.md) — How can incompatible domain meanings evolve without an atomic release?
- [Ownership, isolation and boundary validation](ownership-isolation.md) — Which authorization and invariant tests establish a usable boundary?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

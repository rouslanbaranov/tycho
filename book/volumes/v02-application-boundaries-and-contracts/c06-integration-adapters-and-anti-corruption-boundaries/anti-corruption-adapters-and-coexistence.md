---
metadata_version: 1
id: "tycho.page.31c8e450f78c451d90cb6090df330c5a"
kind: "page"
parent_id: "tycho.chapter.4f7542e57fb74052a4a31cd4c4dce46a"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c06-integration-adapters-and-anti-corruption-boundaries/anti-corruption-adapters-and-coexistence.md"
title: "Anti-corruption adapters: semantic translation and safe coexistence"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Integration adapters and anti-corruption boundaries. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How can incompatible domains and legacy contracts coexist?"
  prerequisites: []
  related_ids:
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.e5195a1aafa640359f05aebc08744584"
    - "tycho.page.5778597986df46439eee0aa162de2729"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Anti-corruption"
    - "adapters"
    - "semantic"
    - "translation"
    - "and"
    - "safe"
    - "coexistence"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Read source-plan units; page-level, not claim-mapped."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-22"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.31c8e450f78c451d90cb6090df330c5a:-1 -->

# Anti-corruption adapters: semantic translation and safe coexistence

> **Tycho book manuscript V02/C06, 2026-10-19.** Independently reviewed public pattern guidance, original synthetic examples and diagrams. No actual legacy source, internal architecture, integration test, consumer migration or independent design review was used.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:** [Anti-Corruption Layer](../../v11-pattern-atlas/c01-application-boundaries/README.md#anti-corruption-layer) — decision conditions and contraindications.
<!-- tycho-question-source:tycho.page.31c8e450f78c451d90cb6090df330c5a:0 -->
## Purpose and mission

When two systems use different models, simply making their APIs exchangeable can preserve hidden semantic incompatibilities. An old interface may call a request “accepted” before durability is established, while a new domain considers acceptance a durable business promise. Translating the word without translating its meaning is dangerous.

An **anti-corruption layer (ACL)** mediates between a consumer's canonical domain model and another subsystem's model. Its purpose is to prevent foreign assumptions from spreading into core business logic, while preserving externally required behavior. It is not by definition a standalone service, a universal façade, or a message queue.

The [Microsoft Azure Architecture Center ACL pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) describes a translation boundary between incompatible models and warns about latency, operational overhead, trust and consistency. [Fowler's bounded-context explanation](https://martinfowler.com/bliki/BoundedContext.html) explains why related concepts can have different valid meanings in different contexts. The [domain ownership chapter](../c02-domain-boundaries-data-ownership-and-contracts/domain-boundaries-data-ownership-and-contracts.md) owns context identity and authority; this chapter owns *actual mediation and failure behavior*.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.31c8e450f78c451d90cb6090df330c5a:8 -->
## Engineering walkthrough — Lossy translation behind a seemingly compatible API

**Original synthetic migration:** a legacy tool catalogue stores `status=ACTIVE` for a model that can be rented; a new unit-level system stores `status=AVAILABLE` for each physical unit. Mapping ACTIVE directly to AVAILABLE implies stock and allocation guarantees the old system never made. The anti-corruption adapter must preserve or explicitly reject that uncertainty.

| Adapter input | Safe semantic disposition | Forbidden transformation |
|---|---|---|
| Legacy model ACTIVE without physical-unit ID | Return model listing, or unknown unit availability | Assert one available physical unit |
| New unit booked while old client retries | Query the sole authoritative booking writer by operation identity | Retry the old model action as a second reservation |
| Missing legacy tenant relation | Reject or quarantine and request mapping proof | Default to a public tenant |
| Old consumer receives new state | Encode compatible projection or versioned explicit error | Silently drop the state and claim synchronized results |

**Partial failure:** the new authority commits R7 but its response to the adapter is lost. The adapter cannot unilaterally roll back R7, nor should it hide the ambiguous outcome behind repeated writes. It must retain the cross-system correlation and resolve the result from authority before answering with success or a classified pending/unknown status.

Retirement sequence (synthetic): inventory both client populations; add measurement for use of legacy operations; introduce versioned translation and a trusted mapping; reconcile unknown outcomes; wait through replay/retention horizon; only then disable legacy writes and finally the adapter. The [anti-corruption-layer pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) motivates semantic separation, **not** correctness of this mapping. **Proposed test:** deliberately send unmappable model IDs and a lost acknowledgment, prove no false availability and one booking authority. None was run.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Specify what an adapter preserves, rejects and cannot translate, including its eventual retirement conditions.

A syntactically valid mapping can discard domain meaning; coexistence needs a reconciliation authority for unknown or unmappable results.

The detailed pages separate the mechanisms that make this decision conditional:

- [Semantic translation and rejected values](semantic-translation.md) — Which meaning must an adapter preserve and which input must it refuse?
- [Coexistence, unknown outcomes and adapter retirement](coexistence-retirement.md) — How is a lost acknowledgment reconciled before old contracts are retired?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
## Bounded pattern ownership notes

### Anti-Corruption Layer

An anti-corruption layer is a translation boundary that keeps an external or legacy model from
becoming the local authority. It owns mapping, validation and the explicit rejection of meanings
that do not translate.

Every mapping needs version pinning and contract tests for lossy fields, plus a rejection path for
values with no local meaning. A dual write or an unknown external outcome retains the correlation
identifier and resolves against the authority before reporting success; it does not hide the
ambiguity behind retries. A synthetic example makes the risk concrete: an external ACTIVE status
does not imply local AVAILABLE stock or allocation, so the mapping must preserve that uncertainty
or reject it.

The pattern might not be suitable when the new and legacy systems have no significant semantic
differences. An ACL fits when the external model is lossy, changes on a different cadence or
carries vocabulary the local domain must not inherit.

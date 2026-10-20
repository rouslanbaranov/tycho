---
metadata_version: 1
id: "tycho.page.91c10dd544b441ddb940aaee24825638"
kind: "page"
parent_id: "tycho.chapter.7031445877fb4f8d831d962d170521c8"
canonical_path: "book/volumes/v02/c02/boundary-evolution.md"
title: "Semantic adapters and evolving contracts"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "How can incompatible domain meanings evolve without an atomic release?"
route_hints:
  questions:
    - "How can incompatible domain meanings evolve without an atomic release?"
  prerequisites:
    - "tycho.page.55c22c6b24ff456a95dd9cc3d71ca238"
  related_ids:
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.461b24a5b47b4b8e82d37125cac20c8d"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "boundary"
    - "evolution"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.4681b3ba9e234c46bdb4b5993634b0e3; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Semantic adapters and evolving contracts

**Owning question:** How can incompatible domain meanings evolve without an atomic release?

This page belongs to [V02/C02 — Domain boundaries, data ownership and contracts](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:4 -->
## 4. Anti-corruption adapters protect meaning, not just JSON fields

An anti-corruption layer translates between domain models whose semantic rules differ. This need can arise even with the same protocol and database engine; it does not require a microservice. The independently published [Microsoft anti-corruption layer pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) explains incremental coexistence and specifically notes latency, extra maintenance and consistency costs. A separate V02/C06 chapter will own the detailed translation topology and adapter failure behavior; this chapter owns the decision of **which meaning is being protected**.

A weak adapter copies strings between differently named fields and silently accepts unrepresentable business states. A strong one states when a mapping is total, partial, version-dependent or lossy; what happens on unsupported values; where identity and ordering originate; and who authorizes a state transition.

**Fictional breaking change:** an old equipment export stores 'available=true' when a unit is advertised in the catalogue. A new reservation model interprets 'available' as immediately allocatable. Blindly copying the Boolean permits booking a maintenance-restricted device. Correct migration either derives the new value from the proper authority or exposes “unknown/requires validation” until a reliable mapping exists.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:5 -->
## 5. Evolving a boundary without an atomic fleet-wide release

Producer and consumer can run different versions during rollout. The interface needs **wire compatibility**, **semantic compatibility** and **state compatibility**, not just a syntactically valid payload.

| Change | Potentially safe | Needs explicit verification |
|---|---|---|
| Add optional display-only field | Old clients may ignore it | Actual parser strictness and data exposure |
| Rename business status | New code can translate old wire names | Old persisted/event meanings and replays |
| Split entity identity into model/unit | May correct previous modeling ambiguity | Migration mapping, unknown identities and old references |
| Introduce new enum value | New consumers can handle it | Older consumer's unknown-value behavior |
| Move writer to a different context | Possible with bounded transition | Single-writer enforcement, reconciliation and rollback/forward repair |
| Relax shared transaction into events | Permits decoupling where eventual consistency fits | Required invariant and failure/recovery after messages are delayed |

In the presence of old clients and replayable events, “we deployed the new producer” is not evidence that the old contract has disappeared. Preserve a compatible period, observe actual consumers and prove cutover with versioned fixtures. [HTTP/RPC contracts](../c05/http-rpc-contracts-and-compatibility.md) explains deadlines, retry identity and mixed-version testing; [target/transition patterns](../../../delivery/progressive-delivery-and-schema-evolution.md) handles staged migration.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](domain-authority.md) |
| Next | [Continue the reasoning](ownership-isolation.md) |
| Integrated question | [Original scenario and limits](domain-boundaries-data-ownership-and-contracts.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

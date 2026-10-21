---
metadata_version: 1
id: "tycho.page.b6be128c3e714ac68ef3311a30d65141"
kind: "page"
parent_id: "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
canonical_path: "book/volumes/v01-requirements-and-architecture/c01-problem-framing/evidence-contract.md"
title: "Unknowns and boundary validation"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Which missing observation prevents a defensible boundary decision?"
route_hints:
  questions:
    - "Which missing observation prevents a defensible boundary decision?"
  prerequisites:
    - "tycho.page.15ffb7535c424b0eac6445cddaeb4a25"
  related_ids:
    - "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
    - "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "evidence"
    - "contract"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.4318e542ac7e445b9e8b3150effd2cff; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Unknowns and boundary validation

**Owning question:** Which missing observation prevents a defensible boundary decision?

This page belongs to [V01/C01 — Problem framing and system boundaries](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:5 -->
## 5. Problem framing produces explicit unknowns

A good architecture description does not erase uncertainty to improve the diagram's appearance. Use a boundary register:

| Open question | Why it changes architecture | Evidence or experiment needed |
|---|---|---|
| Can reservations complete without catalog availability? | Defines whether catalog is a mandatory critical dependency | Signed behavior contract and offline/outage test |
| How long may a requester await final confirmation? | Determines synchronous versus accepted/pending lifecycle | User-journey requirement and latency observation window |
| Does an expired timeslot automatically cancel an accepted booking? | Determines state machine and authority of time-based transitions | Domain rule and race-condition test |
| Must notifications be exactly one? | Changes side-effect identity, acknowledgment and delivery choices | Business consequence and provider failure contract |
| May older clients continue writing after interface evolution? | Requires mixed-version and stored-data compatibility | Client inventory, version/deprecation tests |
| Who can see another requester's booking? | Enforces authorization and privacy boundaries | Object-level permission policy and negative tests |

A missing item is marked **unknown**, not silently assigned a convenient default. The [ISO/IEC/IEEE 42010:2022 public abstract](https://www.iso.org/standard/74393.html) distinguishes an architecture from its *architecture description* and explicitly addresses architectural viewpoints and stakeholders. The entire 62-page ISO standard was **not obtained or read** for this chapter; no conformance to ISO 42010 is claimed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:6 -->
## 6. Validate the problem boundary before scaling the design

A bounded review should verify:

1. **Completeness of partners:** can every required input/output be attributed to a known actor or external system, without putting an external platform inside the team-owned boundary?
2. **User-visible meaning:** can stakeholders state the accepted, rejected, pending and unknown outcomes without referencing implementation classes?
3. **State ownership:** is there exactly one authority (or an explicitly coordinated model) for each invariant?
4. **Trust boundaries:** which caller may request each effect, and where does enforcement happen?
5. **Failure semantics:** what happens when each neighbor fails before commit, after commit or during recovery?
6. **Changeability:** which contracts must coexist across independently controlled releases?
7. **Evidence boundaries:** which claims are confirmed by public specification, hypothetical stakeholder input, test or runtime observation?

If a context diagram is too detailed for a domain stakeholder to explain the outcome, move implementation internals to a component/runtime/deployment view. If too vague to identify critical external interfaces, supplement it with the business/technical exchange table rather than inventing additional service boxes. The C4 and arc42 source materials support focusing context diagrams on externally meaningful relationships and communicating with both technical and nontechnical readers.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:7 -->
## 7. Worked decision: what we can choose now

**Provisional conclusion for the fictional reservation system:** implement a single-authority exclusive allocation boundary; define durable command identity and a status read; keep optional notification failures outside the committed booking outcome. These are **contract choices** only, not a declaration that the final solution must be a modular monolith, SQL database, Kafka stream or cloud-native cluster.

**Not yet justified:** microservice extraction, distributed transactions, global event sourcing, multiple writers or immediate sharding. Their benefits and contraindications depend on workload, independently deployable domain ownership and failure/recovery requirements absent from the scenario.

**Falsifying test:** two clients concurrently request the last slot; the response to the winner is dropped; both retry; notification service is unavailable. The defined system must retain exactly one accepted owner, provide stable final outcomes without unauthorized access and represent notification delay independently. This is a **proposed test**, not an executed result.

That bounded problem definition is a usable input to the later [architecture decision profiles](../../v10-decision-support-and-modernization/c01-architecture-requirement-and-workload-profiles/requirements-and-workload-architecture-profiles.md), [pattern applicability](../../v10-decision-support-and-modernization/c03-pattern-applicability-and-contraindications/pattern-applicability-and-contraindications.md) and [cross-domain ADR examples](../../v10-decision-support-and-modernization/c07-cross-domain-worked-comparisons-and-unresolved-cases/cross-domain-modernization-and-adr-examples.md).

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](authority-dependencies.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](problem-framing-and-system-boundaries.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

---
metadata_version: 1
id: "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01/c01/README.md"
title: "V01/C01 — Problem framing and system boundaries"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which actors, outcomes, interfaces and external failure dependencies define the system? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which actors, outcomes, interfaces and external failure dependencies define the system?"
  prerequisites: []
  related_ids:
    - "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
    - "tycho.page.de62a6f0e5a145aea3798ee69715f033"
    - "tycho.page.15ffb7535c424b0eac6445cddaeb4a25"
    - "tycho.page.b6be128c3e714ac68ef3311a30d65141"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V01/C01 — Problem framing and system boundaries

## Purpose and mission

Which actors, outcomes, interfaces and external failure dependencies define the system? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Draw the outcome boundary before selecting a component boundary: name the caller, authoritative effect, external decision owner and recovery lookup.

A third-party timeout can leave an external effect committed while the local request is unresolved; moving the dependency outside a diagram does not remove that obligation. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](problem-framing-and-system-boundaries.md) | Which actors, outcomes, interfaces and external failure dependencies define the system? |
| [Outcomes and system context](outcomes-context.md) | Which user outcome and external actors define the problem boundary? |
| [Authority and external dependencies](authority-dependencies.md) | Who owns each state transition and what can an external dependency leave unknown? |
| [Unknowns and boundary validation](evidence-contract.md) | Which missing observation prevents a defensible boundary decision? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [Book contents](../../../README.md) |
| Next | [V01/C02 — Workload and demand models](../c02/README.md) |
| Source reading | [Page-local evidence and versions](problem-framing-and-system-boundaries.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:8 -->
## 8. Public evidence and review limitations

| Public source inspected | Supports | Does not establish |
|---|---|---|
| [arc42 §3 — Context and Scope](https://docs.arc42.org/section-3/) | System scope, external partners/interfaces; business vs technical contexts | The fictional system's real contracts or owners |
| [arc42 §1 — Introduction and Goals](https://docs.arc42.org/section-1/) | Stakeholders, requirements and quality goals as architecture input | Measured quality attributes or stakeholder approval |
| [C4 — System Context Diagram](https://c4model.com/diagrams/system-context) | Black-box context, people and external software systems | A specific deployment or access-control design |
| [C4 — Software System](https://c4model.com/abstractions/software-system) | Software system as an abstraction delivering value | Universal organization ownership or a runtime boundary |
| [ISO/IEC/IEEE 42010:2022 — public abstract only](https://www.iso.org/standard/74393.html) | Architecture description scope and distinction from architecture itself | Full-text standards compliance; the full text was not read |

The booking application, all data flows, errors, tables, decision alternatives and illustrations are original synthetic educational material. No external proprietary material was copied. Independent editorial/source verification, stakeholder interviews, runtime tests, user-journey metrics and complete edition assembly remain unperformed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:10 -->
## Navigation

- Intended canonical owner: **V01/C01** in [Tycho's planned contents](../../../PROPOSED-STRUCTURE.md); current [application/foundations landing](../../../application/README.md).
- Continue with [Quality attributes and views](../c03/quality-drivers-and-architecture-views.md); [Architecture styles](../../../application/architecture-styles-and-module-boundaries.md); [Requirements/workload](../../v10/c01/requirements-and-workload-architecture-profiles.md).
- Failure mechanics: [HTTP/RPC compatibility](../../v02/c05/http-rpc-contracts-and-compatibility.md), [Outbox](../../../distributed/transactional-outbox-and-idempotency.md), [Authorization](../../v09/c05/identity-authorization-and-isolation.md).
<!-- /tycho-question-source -->

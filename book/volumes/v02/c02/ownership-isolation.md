---
metadata_version: 1
id: "tycho.page.461b24a5b47b4b8e82d37125cac20c8d"
kind: "page"
parent_id: "tycho.chapter.7031445877fb4f8d831d962d170521c8"
canonical_path: "book/volumes/v02/c02/ownership-isolation.md"
title: "Ownership, isolation and boundary validation"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Which authorization and invariant tests establish a usable boundary?"
route_hints:
  questions:
    - "Which authorization and invariant tests establish a usable boundary?"
  prerequisites:
    - "tycho.page.91c10dd544b441ddb940aaee24825638"
  related_ids:
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "ownership"
    - "isolation"
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
# Ownership, isolation and boundary validation

**Owning question:** Which authorization and invariant tests establish a usable boundary?

This page belongs to [V02/C02 — Domain boundaries, data ownership and contracts](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:6 -->
## 6. Domain ownership and authorization must agree

A domain owner should decide the business effect, but must validate the caller's **authorized relationship to that effect**. For example, a user with permission to browse the projector catalogue does not automatically have permission to cancel another user's reservation. A notification consumer's ability to see the event must not confer authority to update reservation truth.

Object-level authorization needs server-side enforcement at the resource authority, not only at an API gateway. See [identity and isolation](../../v09/c05/identity-authorization-and-isolation.md). Cross-context integration should minimize shared secrets and data, and should explicitly document which fields may be published.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:7 -->
## 7. Selecting boundaries and proving they work

For the fictional makerspace, choose among:
1. **Modular monolith:** enforce package/module dependencies and one writer per relevant state owner. Often simplest if teams/releases need not be independent.
2. **Separate reservation process:** appropriate only if measured capacity, operational isolation or release autonomy warrants a remote call and the state authority remains unambiguous.
3. **Shared database with mediated writes:** possibly a bounded transitional state; direct writes by every context are not a safe default.
4. **Asynchronous projections:** useful for notification/search and other derived views, but not a substitute for a strong allocation invariant.

An acceptance suite would test two concurrent booking attempts for the same unit, a simultaneous maintenance restriction, a lost command response, an old client replay and authorization to modify another person's booking. The **expected logical outcome**, not merely the presence of API calls, is the pass condition. No such fixture has been executed here.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](boundary-evolution.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](domain-boundaries-data-ownership-and-contracts.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

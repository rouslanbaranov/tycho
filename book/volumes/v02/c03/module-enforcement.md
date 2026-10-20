---
metadata_version: 1
id: "tycho.page.4365dbae044244c1b82751a39704e292"
kind: "page"
parent_id: "tycho.chapter.5de52a840c14448c946a65c924f28487"
canonical_path: "book/volumes/v02/c03/module-enforcement.md"
title: "Module boundaries and deployment choice"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "How can one deployable enforce ownership without imitating remote services?"
route_hints:
  questions:
    - "How can one deployable enforce ownership without imitating remote services?"
  prerequisites:
    - "tycho.page.a06fd146f96b4b17a754f4d3b608ebdf"
  related_ids:
    - "tycho.chapter.5de52a840c14448c946a65c924f28487"
    - "tycho.page.a06fd146f96b4b17a754f4d3b608ebdf"
    - "tycho.page.07bb1f96bdd94195ac8e31644527a217"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "module"
    - "enforcement"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.a06fd146f96b4b17a754f4d3b608ebdf; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Module boundaries and deployment choice

**Owning question:** How can one deployable enforce ownership without imitating remote services?

This page belongs to [V02/C03 — Modular monolith and internal events](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.a06fd146f96b4b17a754f4d3b608ebdf:1 -->
## 1. Stable module boundaries before event buses

An internally modular architecture needs:
- Cohesive public capabilities and documented rules, not merely package naming.
- Hidden implementation classes and controlled compile-time dependencies.
- One authoritative writer for each business aggregate, even with shared physical storage.
- Clear synchronous calls when the caller needs an immediate invariant-preserving result.
- Domain events expressing an established fact, not arbitrary commands with vague ordering.
- Tests that enforce allowed dependencies and business outcomes.
- Rules for when modules may be split and which data/operational costs make a split unsuitable.

The official [Spring Modulith application events documentation](https://docs.spring.io/spring-modulith/reference/events.html) recommends decoupling module interactions through events and describes an event publication registry; that is one versioned implementation option. It does **not** imply that every Java module architecture has such a registry or that an event has a global ordering guarantee.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a06fd146f96b4b17a754f4d3b608ebdf:5 -->
## 5. Enforce boundaries rather than only documenting them

Possible enforcement mechanisms include module-level build packages, language visibility restrictions, dependency analysis, ArchUnit-like architecture tests, or Spring Modulith's verification APIs. Check that the source structure represents true public/private module contracts and that tests run on actual build versions.

A useful module acceptance review asks:
- Do dependency checks reject forbidden import paths and cycles?
- Can a public contract change without direct access to another module's internal state?
- Is the authoritative writer for each aggregate clear?
- Can internal events be replayed/delayed/duplicated safely under the declared delivery contract?
- Can one listener fail without losing a committed mandatory operation?
- Are module integration tests independent enough to reveal unintended coupling?
- Can the whole executable still be deployed/restored with its actual database and config?

The benefits must be demonstrated under the relevant change/load profile. One executable may avoid distributed network fault handling, but it retains a shared runtime and deployment cadence. It may still have multiple replicas, so avoid equating a modular monolith with a single machine.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a06fd146f96b4b17a754f4d3b608ebdf:6 -->
## 6. When not to split the module into a separate service

Potential reasons to keep a module internal:
- transactionally coupled invariants with one consistent authoritative state owner;
- insufficient independent team/deployment needs;
- operational limits on additional endpoints, service identities and monitoring;
- low measured resource isolation benefit;
- still-changing interfaces without a viable old/new client contract.

Potential reasons to extract a module *later*:
- proven independent state and lifecycle;
- need to isolate failures or deploy on different resource budgets;
- specific owner and monitored external contract;
- a tested transition plan that protects old clients and persisted state.

The extraction decision is not the definition of “good modularity”. A well-modularized monolith can be the **target architecture**.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](modular-monolith-and-internal-events.md) |
| Next | [Continue the reasoning](events-transactions.md) |
| Integrated question | [Original scenario and limits](modular-monolith-and-internal-events.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

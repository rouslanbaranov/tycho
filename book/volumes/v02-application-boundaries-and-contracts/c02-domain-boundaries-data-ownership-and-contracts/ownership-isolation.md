---
metadata_version: 1
id: "tycho.page.461b24a5b47b4b8e82d37125cac20c8d"
kind: "page"
parent_id: "tycho.chapter.7031445877fb4f8d831d962d170521c8"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c02-domain-boundaries-data-ownership-and-contracts/ownership-isolation.md"
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
  notes: "Body Source boundary records the 2026-10-30 inspection and exact revisions."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-30"
source_inspection_date: null
content_verified_at: null
---
# Ownership, isolation and boundary validation

**Owning question:** Which authorization and invariant tests establish a usable boundary?

This page belongs to [V02/C02 — Domain boundaries, data ownership and contracts](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:6 -->
## 6. Domain ownership and authorization must agree

A domain owner should decide the business effect, but must validate the caller's **authorized relationship to that effect**. For example, a user with permission to browse the projector catalogue does not automatically have permission to cancel another user's reservation. A notification consumer's ability to see the event must not confer authority to update reservation truth.

Object-level authorization needs server-side enforcement at the resource authority, not only at an API gateway. See [identity and isolation](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md). Cross-context integration should minimize shared secrets and data, and should explicitly document which fields may be published.

<!-- /tycho-question-source -->

> **Pattern atlas:** [Database per Service](../../v11-pattern-atlas/c01-application-boundaries/README.md#database-per-service) — decision conditions and contraindications.
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

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Database per Service

Each service owns its schema and storage, and other services reach that data only through the
owner's contract or published events. The boundary is an ownership rule even when several schemas
share one physical server. Only the owning service writes its records, and no critical-path query
joins another service's tables without an explicit contract.

Shared-table shortcuts and distributed joins reappear as hidden coupling; detect them through
schema ownership review and cross-service access inspection rather than assuming the boundary
exists. Dual writes, stale replicas and cross-service queries are common; use an outbox or
idempotent reconciliation for cross-service effects and verify replica freshness before joining.
A shared database with enforced module ownership is simpler when teams release together; choose
separate stores only when independent ownership, scaling or recovery justify the coordination
cost. Strong cross-service transactions remain a contraindication: an outbox or reconciliation
reduces, but does not remove, that coordination cost.

**Failure and recovery.** The Database per Service page's "Resulting context" says that
"Implementing business transactions that span multiple services is not straightforward" and that
"Implementing queries that join data that is now in multiple databases is challenging." It points
to Saga, API Composition and CQRS for those gaps. The Transactional outbox page states the atomic
update-and-send requirement directly: a command "must atomically update the database and send
messages in order to avoid data inconsistencies and bugs", yet a message sent after commit can be
lost if the service crashes. Its solution stores the message "in the database as part of the
transaction that updates the business entities" and a separate relay publishes it; because the
relay "might publish a message more than once", "a message consumer must be idempotent". The
Saga page adds that a saga is "a reliably coordinated sequence of local transactions" and that
failed steps are undone by "compensating transactions". The pages mention replication only as a
scaling fact; they do not establish replica lag: Database per Service says only that databases
"must sometimes be replicated and sharded in order to scale." "Verify replica freshness before
joining" and "reconciliation" as a repair loop are therefore Tycho guidance, not source claims.

**Alternative.** The Shared database page describes one database "shared by multiple services"
where each service "freely accesses data owned by other services", and lists "A single database is
simpler to operate" and familiar ACID transactions as benefits. It also warns of "Development time
coupling" when services coordinate schema changes and "Runtime coupling" when they interfere. The
Database per Service page links "The Shared Database anti-pattern" as the problem source; the two
pages therefore disagree, and this note keeps both readings. Tycho's narrower alternative is a
shared database whose module ownership is enforced by schema grants, code review and dependency
checks, not the page's free cross-service access. That combination is simpler when one team
releases the modules together, because schema coordination stays inside one release; the pages
support the simplicity and coupling statements, not the enforced-ownership condition or the
release-cadence inference. Monolith First adds that the microservice premium "will slow down a
team, favoring a monolith for simpler applications" and that modularity at "the API boundaries
and how the data is stored" makes a later split easier.

**Source boundary.** Public pattern pages from `src.microservices-patterns` and one article from
`src.monolith-first`, all rechecked 2026-10-30. The Database per Service, Saga and Transactional
Outbox records retain their 2026-10-21 revisions; their recorded HTML digests reproduce. The
Shared database page is a new unit.

- Database per Service, record `read.microservices-database-per-service.2026-10-21`, revision
  `09a42dc873ba914208f3b2dc90a28a1287b883da6080805b318ff6a28d484d31`; sections
  "Resulting context" and "Forces".
- Saga, record `read.batch2-saga.2026-10-21`, revision
  `54805df89f619c8432fd280263a88670ed66fac6cbe0b5429a1ebdc5d4cd1047`; section "Solution".
- Transactional outbox, record `read.batch2-outbox.2026-10-21`, revision
  `7b9d9b224d9b985bf03d581dcdef5c94a21f49a93f3ac1e74c6bc2104a48b3eb`; sections "Context",
  "Solution" and "Result context".
- Shared database, record `read.microservices-shared-database.2026-10-30`, revision
  `4dc5fcf1a9bdf1d4c97c3ba916f997611cebdc2bc4b87927a6bb0a61c11c5731`; sections
  "Pattern: Shared database" and "Forces".
- Monolith First, record `read.monolith-first.2026-10-21`, revision
  `722d8d78beddd9e0f6ff3e856eec94dfa2b9fa3bebcaaf4c9e80ccdd3c0e1446`; section
  "Monolith First".

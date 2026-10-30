---
metadata_version: 1
id: "tycho.page.a06fd146f96b4b17a754f4d3b608ebdf"
kind: "page"
parent_id: "tycho.chapter.5de52a840c14448c946a65c924f28487"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c03-modular-monolith-and-internal-events/modular-monolith-and-internal-events.md"
title: "Modular monolith architecture and internal domain events"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Modular monolith and internal events. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which coupling and deployment constraints fit an in-process architecture?"
  prerequisites: []
  related_ids:
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.47ffb5c160bd4b10aff27101414c2133"
    - "tycho.page.4365dbae044244c1b82751a39704e292"
    - "tycho.page.07bb1f96bdd94195ac8e31644527a217"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Modular"
    - "monolith"
    - "architecture"
    - "and"
    - "internal"
    - "domain"
    - "events"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Body Source boundary records the 2026-10-30 inspection and exact revisions."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-30"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.a06fd146f96b4b17a754f4d3b608ebdf:-1 -->

# Modular monolith architecture and internal domain events

> **Original Tycho manuscript V02/C03**, prepared 2026-10-19. Public Spring Framework/Modulith references are technology illustrations, not a requirement to use those frameworks. The fictional application and event flow were invented independently. No build, module verification, event replay or independent review has been performed.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:** [Modular Monolith](../../v11-pattern-atlas/c01-application-boundaries/modular-monolith.md#modular-monolith) — decision conditions and contraindications.
<!-- tycho-question-source:tycho.page.a06fd146f96b4b17a754f4d3b608ebdf:0 -->
## Purpose and mission

A modular monolith is a single deployable whose functional responsibilities are divided into explicitly enforced modules. Its goal is neither to hide all coupling nor to simulate microservices inside one process. It preserves appropriate local consistency while making *which module owns each rule, data object and contract* visible.

Internal events can reduce direct dependencies between modules, but “event-driven” does not automatically mean asynchronous, durable or exactly-once. An in-memory event observed by a synchronous listener has different failure and transaction semantics from a transactionally recorded event consumed after commit.

The [application style chapter](../../../application/architecture-styles-and-module-boundaries.md) compares architectural forms. The [domain ownership chapter](../c02-domain-boundaries-data-ownership-and-contracts/domain-boundaries-data-ownership-and-contracts.md) owns bounded-context meaning. This chapter focuses on **module lifecycle and internal event contracts**.

**Module enforcement and failure.** Modules own their rules, data and contracts; internal
interfaces define allowed calls and dependency tests enforce the boundary. Hidden
cross-module database access, cyclic dependencies and event-based coupling that recreates a
distributed monolith are common. Detect them with dependency/contract tests and split a
module only when independent deployment or failure containment is a measured requirement.
Microservices, hexagonal architecture or a simpler layered application may be preferable
when module enforcement cost exceeds the coordination benefit.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a06fd146f96b4b17a754f4d3b608ebdf:9 -->
## Engineering walkthrough — An internal event that survives neither process death nor commit

**Original fictional workflow:** `BookingModule` reserves a resource and emits `BookingCreated`. `NotificationModule` subscribes. Three superficially similar deliveries have different durability: calling subscribers inside the transaction, invoking after-commit listeners, and storing a durable publication intention for later dispatch.

| Crash window | Synchronous in-process listener | After-commit listener | Durable outbox-like publication |
|---|---|---|---|
| Before booking commit | Subscriber might have run before rollback if misconfigured | Should not run as a committed-event observer | Neither booking nor outbox entry becomes durable if transaction rolls back |
| Immediately after commit, process dies | Prior callback result varies with order | May never run | Pending committed event can be found and retried |
| Callback fails | May poison or alter initiating transaction, according to design | Booking cannot be undone by callback exception alone | Relay retries; consumer must deduplicate |

The [Spring transaction event documentation](https://docs.spring.io/spring-framework/reference/7.1/data-access/transaction/event.html) describes phase-bound listeners; it does **not** make arbitrary callbacks durable. A module split into separate processes increases latency, authorization and retry costs without solving the lost-after-commit callback by itself. Keep notification optional when business semantics permit; if a legally required notice must eventually occur, persist the obligation and its effect identity.

**Proposed negative experiment:** terminate the process exactly after booking commit but before notification, then restart, reconcile booking and ensure a durable publication method eventually resolves the obligation without duplication. This is a plan, not a run. The distinct distributed outbox owner V04/C05 supplies detailed delivery semantics; modular architecture owns the local dependency boundary.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a06fd146f96b4b17a754f4d3b608ebdf:10 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Shopify — Modular monolith](../../../cases/shopify-modular-monolith.md)**. **Relevant mechanism or architectural contrast:** A modular monolith can be a legitimate target when domain ownership matters more than release separation. **Not established by this report/playbook:** The 2019 report does not imply Shopify achieved perfectly enforced modules everywhere or that service decomposition always fails.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Use enforced module contracts to retain useful local transactions and make internal event durability explicit.

An after-commit callback is not a durable external delivery mechanism; process death can separate a committed change from its notification.

The detailed pages separate the mechanisms that make this decision conditional:

- [Module boundaries and deployment choice](module-enforcement.md) — How can one deployable enforce ownership without imitating remote services?
- [Internal events and transaction timing](events-transactions.md) — What can happen between local commit, event handling and process death?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
## Bounded pattern ownership notes

### Modular Monolith

Modules own their rules, data and contracts. The deployable is one unit, but each module has a
named owner, an allowed-call surface and a dependency test that fails a bypass.

Spring Modulith 1.3.12 documents one enforcement model. It rejects "all references to types that
reside in application module internal packages" and, when configured, rejects dependencies that
are not declared through `@ApplicationModule(allowedDependencies = …)`. Its fundamentals page
adds that code in internal packages "must not be referred to from other modules" and that "the
Java compiler is not of much use to prevent these illegal references". The named owner and the
single-deployable framing are Tycho definitions; the allowed-call surface and the dependency
test are source-backed.

Bypasses show up as shared tables, import cycles, or events that exist only to recreate a remote
call. Internal events also need a durability decision: a local outbox or best-effort delivery, plus
the owner who repairs a missed event. Test schema ownership as well as the public API.

Synchronous call chains across modules and one deployment blast radius are the operational risk;
keep a rollback path and verify event durability before treating the boundary as a contract.
Spring Modulith's event page says that "event publication happens synchronously by default" and
that more triggered functionality "will widen the transaction boundary and potentially cause the
entire transaction to fail". It also warns that an asynchronous listener can lose the event
"unless each listener actually implements its own safety net". The deployment blast radius is
Tycho's inference from the one-deployable definition, not a measured result in these sources.

Choose services or a layered structure only when module enforcement costs more than the
coordination benefit. A modular monolith fits when the team wants one operational unit without
surrendering internal ownership, with a documented interface and a named owner.

**Source boundary.** Public documentation and reference material (`src.monolith-first`,
`src.spring-modulith`). The Spring Modulith pages were accessed 2026-10-30; the Monolith First
record is dated 2026-10-21. These are living pages, not a benchmark or an executed local test.

- Martin Fowler, "Monolith First" (3 June 2015): record
  `read.monolith-first.2026-10-21`, canonical revision
  `722d8d78beddd9e0f6ff3e856eec94dfa2b9fa3bebcaaf4c9e80ccdd3c0e1446`; retained for the
  mechanism and alternative bindings, not used for the new invariant or failure claims.
- Spring Modulith 1.3.12, "Verifying Application Module Structure": canonical revision
  `c1ee41282edd5866877a4d2a09d4585196a4a2ac05a672416624e4b9eb117cd4`; used for API-only
  access, declared allowed dependencies and the verification that rejects violations.
- Spring Modulith 1.3.12, "Fundamentals": canonical revision
  `6f45529855cf017220ca400ab72e87fc805cd31e044db44f47705a4ac16f95bd`; sections
  "Application Modules" and "Advanced Application Modules"; used for internal packages, the
  compiler limit and the explicit API.
- Spring Modulith 1.3.12, "Working with Application Events": canonical revision
  `c15f574e8029e58e50346011402e03439590af4e3e6a3e15940fab2fa5472c6a`; used for synchronous
  publication, the widened transaction and the lost-event risk.

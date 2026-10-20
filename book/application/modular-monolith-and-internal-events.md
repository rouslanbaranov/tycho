---
metadata_version: 1
id: "tycho.page.a06fd146f96b4b17a754f4d3b608ebdf"
kind: "page"
parent_id: "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
canonical_path: "book/application/modular-monolith-and-internal-events.md"
title: "Modular monolith architecture and internal domain events"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Reader entry for Modular monolith architecture and internal domain events. Scope includes 1. Stable module boundaries before event buses; 2. Original synthetic example: community workshop reservation; 3. Internal events have multiple execution and durability contracts."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Modular monolith architecture and internal domain events?"
  prerequisites: []
  related_ids:
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.47ffb5c160bd4b10aff27101414c2133"
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

# Modular monolith architecture and internal domain events

> **Original Tycho manuscript V02/C03**, prepared 2026-10-19. Public Spring Framework/Modulith references are technology illustrations, not a requirement to use those frameworks. The fictional application and event flow were invented independently. No build, module verification, event replay or independent review has been performed.

## Purpose and mission

A modular monolith is a single deployable whose functional responsibilities are divided into explicitly enforced modules. Its goal is neither to hide all coupling nor to simulate microservices inside one process. It preserves appropriate local consistency while making *which module owns each rule, data object and contract* visible.

Internal events can reduce direct dependencies between modules, but “event-driven” does not automatically mean asynchronous, durable or exactly-once. An in-memory event observed by a synchronous listener has different failure and transaction semantics from a transactionally recorded event consumed after commit.

The [application style chapter](architecture-styles-and-module-boundaries.md) compares architectural forms. The [domain ownership chapter](domain-boundaries-data-ownership-and-contracts.md) owns bounded-context meaning. This chapter focuses on **module lifecycle and internal event contracts**.

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

## 2. Original synthetic example: community workshop reservation

Three modules inside a single application:
- **Catalogue** publishes equipment descriptions and approved configurations.
- **Reservation** owns exclusive allocation, cancellation and durable command identities.
- **Notification** owns opt-in messages; successful delivery must not determine whether a reservation was accepted.

```mermaid
flowchart TB
    C["Client"] --> R["Reservation public module API"]
    R --> D[("Reservation-owned state")]
    R --> E["ReservationAccepted domain event"]
    E --> N["Notification module listener"]
    E --> O["Optional analytics/projection listener"]
    R --> X["Catalogue public interface"]
```

**Text alternative:** the reservation module is the sole authority for accepted reservations. It may synchronously consult the catalogue when eligibility rules require it. After a durable state change it publishes a fact; notification and optional derived views consume the fact without gaining authority over reservation truth. All blocks can remain inside one executable.

The event's name should describe **past successful meaning**, not an intention (e.g. “ReserveSlot” would be a command). Include an event ID, aggregate identity, schema version and relevant source state version if required for replay/deduplication.

## 3. Internal events have multiple execution and durability contracts

| Event style | Execution boundary | Failure question | Appropriate use |
|---|---|---|---|
| Direct synchronous module call | Caller stack/transaction if configured | Can callee failure roll back caller? | Required immediate invariant/decision |
| In-process synchronous event | Same process; dispatch semantics framework-specific | Does listener exception fail publishing operation? | Small local observers when explicit coupling is accepted |
| Post-commit event listener | Triggered in relation to a successful transaction boundary | Is listener work durable or retried after a process crash? | Side effects that must not happen before commit, when loss policy is defined |
| Transactional publication registry | Durable record of interested listeners under implementation-specific conditions | Are incomplete/failed events resent; can duplicate handling occur? | Recoverable asynchronous module integration |
| External broker event | Process/network/broker boundaries | Delivery/redelivery, ordering scope and effect idempotency | Independently deployed consumers or real external contracts |

In Spring Framework, [transaction-bound event listeners](https://docs.spring.io/spring-framework/reference/7.1/data-access/transaction/event.html) support phases such as AFTER_COMMIT by default. This means listener timing can depend on commit success; it does **not** by itself prove an event will survive a crash between commit and listener processing.

Spring Modulith's [publication registry](https://docs.spring.io/spring-modulith/reference/events.html) documents listener-specific publication records and retry/resubmission mechanisms; check its actual version and storage implementation before using these guarantees. Event publication durability is **separate** from downstream external side-effect identity. A listener retried after partial external success can duplicate a notification unless the effect has its own deduplication/reconciliation semantics.

### Post-commit listeners are not a fresh durable transaction (Spring-specific caveat)

The [official Spring Framework `@TransactionalEventListener` JavaDoc](https://docs.spring.io/spring-framework/docs/6.0.7/javadoc-api/org/springframework/transaction/event/TransactionalEventListener.html) warns that, for `AFTER_COMMIT` (default), `AFTER_ROLLBACK` and `AFTER_COMPLETION`, the underlying transaction has **already completed** although bound resources can remain accessible. An unguarded database update triggered there may *appear to participate* in the original context but have **no later commit**. Do not design mandatory follow-up state mutation on the assumption that an `AFTER_COMMIT` listener automatically begins a new commit.

For an intentionally separate database write, use an explicitly configured **new transaction boundary** (e.g. a correctly invoked `PROPAGATION_REQUIRES_NEW` operation or transaction template, with the actual transaction manager and framework generation checked), and treat failure of that new transaction as a separate partial outcome. A fresh transaction is not equivalent to a durable event obligation: the process may still crash *before* it is entered or *after* the second commit but before acknowledgment. For mandatory effects, persist an outbox/publication intent atomically with the authoritative reservation and reconcile/redeliver using stable effect IDs.

**No-active-transaction trap:** according to that same JavaDoc, a transactional event listener normally does not process an event if no transaction is active, unless `fallbackExecution` is explicitly enabled. Turning on fallback changes when listeners may execute; it does **not** create a missing transaction or guarantee after-commit behavior for such publications. Reactive transaction context has its own event-source requirements and must not be inferred from a thread-local model.

**Proposed negative test, not executed:** publish an event inside, outside and immediately after a transaction; verify committed primary state, visibility of any follow-up write, an intentional new transaction, process death after commit and duplicate resubmission. The expected result under missing durable publication must be represented as potentially lost, rather than silently accepted.

## 4. Transaction boundary determines which outcome is correct

**Synthetic failure:** reservation state commits but the process crashes before an in-memory notification event reaches its listener.

If notification is optional, user booking truth can remain correct; however, the system must disclose whether notification may be lost. If the requirement says delivery must be attempted eventually, an in-memory-only event is insufficient. A transactional event registry or outbox-like persistence with retry handling may be appropriate. [Outbox and idempotency](../distributed/transactional-outbox-and-idempotency.md) owns the detailed commit-publication problem.

**Second failure:** a listener performs an external irreversible effect before the reservation transaction commits, but the transaction later aborts. The external effect may now describe a booking that never existed. Delay the effect until commit and use durable recovery when required; mere annotation-driven dispatch without a durable record is not a full recovery contract.

**Third failure:** duplicate delivery of an accepted event causes two messages or redundant projections. Consumers need stable event/effect identities and bounded retry/reconciliation. Deduplication should be scoped to actual business identity, not to one process lifetime.

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

## 7. Source ledger and limits

| Independent source inspected | Narrow support | Not established |
|---|---|---|
| [Spring Modulith events](https://docs.spring.io/spring-modulith/reference/events.html) | Module event publication, listener registry and incomplete-publication recovery concepts | Actual project configuration or guarantee in all library versions |
| [Spring Framework transaction-bound events](https://docs.spring.io/spring-framework/reference/7.1/data-access/transaction/event.html) | Listener phases relative to commit/rollback | Automatically durable after-commit processing |
| [Tycho architecture styles](architecture-styles-and-module-boundaries.md) | Independently researched module and service boundaries | Compiled/enforced module graph for fictional app |
| [Tycho distributed outbox](../distributed/transactional-outbox-and-idempotency.md) | Commit/pub ambiguity, deduplication limits | An implemented event registry or exactly-once external effect |

All modules, diagrams, events and failure cases are original invented teaching materials. No real source code, build output, dependency checker, distributed test or human domain approval was used. The final book volume/chapter/page edition has not been assembled.

## Navigation

Proposed owner **V02/C03** in [planned table of contents](../PROPOSED-STRUCTURE.md), [application landing](README.md). Start with [bounded contexts and ownership](domain-boundaries-data-ownership-and-contracts.md), then [module/service styles](architecture-styles-and-module-boundaries.md), [internal vs external outbox](../distributed/transactional-outbox-and-idempotency.md) and [safe extraction](architecture-evolution-and-extraction.md).

## Engineering walkthrough — An internal event that survives neither process death nor commit

**Original fictional workflow:** `BookingModule` reserves a resource and emits `BookingCreated`. `NotificationModule` subscribes. Three superficially similar deliveries have different durability: calling subscribers inside the transaction, invoking after-commit listeners, and storing a durable publication intention for later dispatch.

| Crash window | Synchronous in-process listener | After-commit listener | Durable outbox-like publication |
|---|---|---|---|
| Before booking commit | Subscriber might have run before rollback if misconfigured | Should not run as a committed-event observer | Neither booking nor outbox entry becomes durable if transaction rolls back |
| Immediately after commit, process dies | Prior callback result varies with order | May never run | Pending committed event can be found and retried |
| Callback fails | May poison or alter initiating transaction, according to design | Booking cannot be undone by callback exception alone | Relay retries; consumer must deduplicate |

The [Spring transaction event documentation](https://docs.spring.io/spring-framework/reference/7.1/data-access/transaction/event.html) describes phase-bound listeners; it does **not** make arbitrary callbacks durable. A module split into separate processes increases latency, authorization and retry costs without solving the lost-after-commit callback by itself. Keep notification optional when business semantics permit; if a legally required notice must eventually occur, persist the obligation and its effect identity.

**Proposed negative experiment:** terminate the process exactly after booking commit but before notification, then restart, reconcile booking and ensure a durable publication method eventually resolves the obligation without duplication. This is a plan, not a run. The distinct distributed outbox owner V04/C05 supplies detailed delivery semantics; modular architecture owns the local dependency boundary.

## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Shopify — Modular monolith](../cases/shopify-modular-monolith.md)**. **Relevant mechanism or architectural contrast:** A modular monolith can be a legitimate target when domain ownership matters more than release separation. **Not established by this report/playbook:** The 2019 report does not imply Shopify achieved perfectly enforced modules everywhere or that service decomposition always fails.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.

# Pattern source reading contract

> Status: Phase 2A, 2026-10-21, issue #236. This contract defines how the
> pattern catalog moves from planned source units to read evidence. It does not
> claim that the catalog is fully read, that a source supports a technical claim
> or that an independent review exists.

## Purpose

Phase 2 must make the distance between a catalog entry and its evidence
visible. A pattern name in a catalog is not a source unit. A landing page is
not a whole documentation tree. A planned unit is not a read unit.

## Unit model

A source unit is one bounded public artifact that can be read completely:

- a complete article, paper, specification or public book chapter;
- one versioned documentation page when that page is the admitted unit;
- a catalog index page when the unit is the index itself, not its children;
- a public vendor page whose scope and version can be identified.

Each unit records the source ID, canonical URL, unit type, exact sections or
tables inspected, access date, licence, claims supported and claims not
supported. A unit never implies that linked children were read.

## States

| State | Meaning |
|---|---|
| `read` | The ledger records the exact public unit, sections, date and limits. |
| `planned` | A unit is selected or a page family is identified, but no reading is claimed. |
| `blocked` | Lawful access is unavailable or a commercial work is bibliography-only. |

The registry maps these states to its own source-unit enum: `read`, `not-read`
and `blocked`. A planned unit must never appear as `read`.

## Ledger rules

1. Read the complete lawfully accessible unit, not a snippet or navigation card.
2. Record exact sections and, where relevant, tables and figures inspected.
3. Record access date, publisher, version or living-page status, licence and
   limitations.
4. Separate claims the unit supports from claims it does not support.
5. Do not infer a child page from an index, a specification from a summary or
   an implementation guarantee from a vendor overview.
6. Reuse issue #225 readings only at exact scope and revision; do not modify its
   frozen baseline.
7. A blocked or truncated page is recorded as such, never silently promoted.

## Foundation batch

The current ledger records six public units:

- Microsoft Cloud Design Patterns index;
- microservices.io pattern-language index;
- Enterprise Integration Patterns messaging overview;
- Fowler CQRS article;
- Fowler Strangler Fig article;
- Google SRE Handling Overload chapter.

## Phase 2A foundation

Five catalog entries have a read unit: CQRS, Strangler Fig, Load Shedding,
Throttling and Rate Limiting. The three catalog indexes support catalog
structure only, not individual pattern mechanisms.

## Phase 2B batch 1 — application and API

All 24 application/API entries have a read unit after batch 1:
Sidecar, Ambassador, Anti-Corruption Layer, Gateway Routing, Gateway
Aggregation, Gateway Offloading, Backends for Frontends, Database per Service,
Self-contained Service, API Composition, API Gateway, Client-side Discovery,
Server-side Discovery, Microservices, Monolith First, Service Discovery,
Reverse Proxy, Layered Architecture, Hexagonal Architecture, Clean/Onion
Architecture, Domain-Driven Design, Asynchronous Request-Reply and Gatekeeper.

SOA uses the Microservices article's explicit SOA comparison; the OASIS SOA-RM
specification remains a later primary source. Hexagonal uses AWS Prescriptive
Guidance because the original Cockburn page was truncated by the fetch tool.
The DDD entry is bounded-context scoped; the full DDD reference remains a
later source. Batch 1 is complete for its planned units, not for the catalog.

## Phase 2B batch 2 — messaging and data

All 34 messaging/data entries have a read unit after batch 2. Enterprise
Integration Patterns pages, Camel splitter documentation, microservices.io
data patterns, Debezium outbox documentation, the IETF Idempotency-Key draft,
PostgreSQL materialized-view and two-phase pages, and Temporal workflow docs
were read. The Camel splitter page was truncated after its options; the other
units were complete as returned. The Message Broker and Process Manager pages
do not separately read the bridge or routing-slip variants, and the Debezium
outbox page is not a general CDC contract.

## Phase 2B batch 3 — caching and database storage

26 of 27 caching/database entries have a read unit after batch 3. The five
previously planned entries are now read: Negative Caching (Google Cloud CDN),
Stale-While-Revalidate (RFC 5861), Multi-Leader and Quorum (Cassandra Dynamo
page), and Online Data Migration (gh-ost README). Polyglot Persistence remains
the one blocked bibliography-only entry.

The caching guidance, Hazelcast, Citus and Google negative-caching pages
returned truncated after their main sections; those records state the inspected
scope. Flyway migration documentation is not a full expand-and-contract
contract. gh-ost is a MySQL-specific implementation reference, not a general
zero-downtime guarantee.

## Phase 2B batch 4 — resilience and coordination

All 25 resilience/coordination entries have a read unit after batch 4. The tail
added Hedged Requests (a secondary Tail-at-Scale summary), Failover/Failback (a
bounded PostgreSQL standby example), Fencing Tokens (Kleppmann's lock-safety
article) and Causal Ordering (Jepsen's causal model). Load Shedding, Throttling
and Rate Limiting reuse the Phase 2A SRE Handling Overload record; Distributed
Workflow Orchestration reuses the batch 2 Temporal record.

Resilience4j, SRE cascading-failure, Kubernetes probe/lease and Tail-at-Scale
pages were truncated after their main sections or landing content; those records
state the inspected scope. RabbitMQ, Raft overview and Jepsen model pages were
read as returned. Hedged Requests relies on a secondary summary, not the
original paper; Failover/Failback is a database example, not a generic service
failover contract.

## Phase 2B batch 5 — scalability and deployment

All 22 scalability/deployment entries have a read unit after batch 5. Cell-Based
Architecture reuses the deployment-stamps unit as a bounded comparison; Shuffle
Sharding uses Cortex documentation; Geode uses the Microsoft pattern page;
Tenant-Based Resource Isolation uses Microsoft multitenant guidance; Immutable
Infrastructure uses an IBM overview.

SRE frontend load balancing, KEDA, deployment stamps, Argo blue-green/canary and
Fowler feature-toggle/branch pages were read as returned. Kubernetes HPA,
resource, Deployment and OpenGitOps pages were truncated after their main
sections; those records state the inspected scope.

## Phase 2B batch 6 — security and operations

All 13 security/isolation/operations entries have a read unit after batch 6.
OWASP ASVS is shared by Zero Trust, Least Privilege, RBAC/ABAC and Multitenant
Isolation as a verification-framing source; Health checks reuse the batch 4
Kubernetes probe record. Federated Identity, workload identity, tracing,
logging, audit, SLOs and synthetic monitoring have dedicated public units.

The RFC 9700, Istio security and OpenTelemetry traces/logs pages returned
truncated after their main sections. ASVS is an overview only, not the detailed
requirement chapters; those records state the inspected scope.

Current plan totals: **144 read, 0 planned and 1 blocked** across 145 entries;
the ledger has **115 records**, including three foundation catalog records.
Only Polyglot Persistence remains blocked by its bibliography-only source.
Entry-level source coverage is complete; technical and decision coverage remain
unassessed and are not claimed.

## Phase 3 card batches

All 12 V11/C01 entries have self-checked decision cards with a technical-owner
section and a reciprocal backlink. Four use dedicated mechanisms: Modular Monolith,
Hexagonal Architecture / Ports and Adapters, Domain-Driven Design / Bounded Context
and Anti-Corruption Layer. Eight use bounded sections for layering, service
orientation, data ownership, independence or traffic intermediaries; those links are
not presented as dedicated pattern manuscripts.

The registry records `partial` technical, decision and overall coverage for all 12.
No `sufficient` state is claimed. Remediation issue #254 is closed by explicit owner
bindings; it did not create independent review or complete technical coverage.

All 12 V11/C02 entries also have self-checked cards with bounded owner sections.
They cover API Gateway, gateway routing/aggregation/offloading, BFF, API
composition, reverse proxy, service discovery variants, asynchronous request-reply
and Gatekeeper. Registry coverage is `partial` for all 12; no `sufficient` state is
claimed.

All 20 V11/C03 entries also have self-checked cards with bounded owner sections.
They cover channel, consumer, routing, pipeline, aggregation, dead-letter, durable
subscription, idempotency, claim-check and process-manager decisions. Registry
coverage is `partial` for all 20; no `sufficient` state is claimed.

All 14 V11/C04 entries also have self-checked cards with bounded owner sections.
They cover CQRS, event sourcing, domain events, saga variants, outbox/inbox,
idempotency keys, CDC, materialized views, command-side replicas and 2PC. Registry
coverage is `partial` for all 14; no `sufficient` state is claimed.

All 14 V11/C05 entries also have self-checked cards with bounded owner sections.
They cover distributed/local caching, cache-aside/read-through/write policies,
TTL and invalidation, negative caching, stampede/single-flight, stale-while-
revalidate, multi-level caching and edge caching. Registry coverage is `partial`
for all 14; no `sufficient` state is claimed.

Twelve V11/C06 entries also have self-checked cards with bounded owner sections.
They cover sharding/partitioning, consistent hashing, replication variants, read
replicas, quorum, index tables, CQRS projections, schema migration and backup/PITR.
Polyglot Persistence remains blocked and has no card. Registry coverage is `partial`
for the twelve; no `sufficient` state is claimed.

All 16 V11/C07 entries also have self-checked cards with bounded owner sections.
They cover circuit breaking, bulkheads, retries/timeouts/deadlines, fallback and
degradation, shedding/throttling/rate limits, queue leveling, priority, hedging,
health checks and failover/failback. Registry coverage is `partial` for all 16; no
`sufficient` state is claimed.

All 9 V11/C08 entries also have self-checked cards with bounded owner sections.
They cover leader election, consensus, locks, leases, fencing tokens, quorum,
causal ordering, session consistency and durable workflow orchestration. Registry
coverage is `partial` for all 9; no `sufficient` state is claimed.

All 10 V11/C09 entries also have self-checked cards with bounded owner sections.
They cover load balancing, horizontal/vertical scaling, autoscaling, cell-based
architecture, shuffle sharding, deployment stamps, Geode, static content hosting
and tenant resource isolation. Registry coverage is `partial` for all 10; no
`sufficient` state is claimed.

All 12 V11/C10 entries also have self-checked cards with bounded owner sections.
They cover rolling/blue-green/canary, feature flags, GitOps, immutable
infrastructure, Strangler Fig, branch by abstraction, parallel run, dark launch,
expand-and-contract and controlled cutover. Registry coverage is `partial` for all
12; no `sufficient` state is claimed.

All 13 V11/C11 entries also have self-checked cards with bounded owner sections.
They cover federated/zero-trust identity, least privilege, RBAC/ABAC, workload
identity, Valet Key, multitenant isolation, tracing, logging, audit, SLOs,
synthetic monitoring and health checks. Registry coverage is `partial` for all 13;
no `sufficient` state is claimed.

The card batches are recorded in `edition/patterns/card-batches.v1.json` and checked
by `scripts/validate_pattern_cards.py`, including adversarial tests. The validator
now resolves each technical-owner link to the declared path and anchor. All 144
readable catalog entries have cards; only Polyglot Persistence remains blocked and
uncarded. Card coverage is not technical sufficiency.

## Phase 4 audit and retrieval routes

The Phase 4 artifact `edition/patterns/phase4.v1.json` dispositions all 419
canonical pages, audits 145 entries across 14 dimensions, records the gap matrix,
derives 536 cross-pattern routes from card related entries, records 40 related
labels as deliberate non-routes when they name technical concepts outside the catalog,
and extracts 144 retrieval questions. Polyglot Persistence is the one blocked entry and
has no question.

Page dispositions distinguish atlas pages, technical owners, candidate owners,
navigation, legacy cross-volume pages and other canonical technical pages. They do
not assert semantic acceptance. The artifact, schema, validator, freshness check and
adversarial tests are structural evidence only; independent review remains Phase 5.

## Phase 5 delivery evidence

The Phase 5 artifact `edition/patterns/delivery-evidence.v1.json` records the
locally executed checks, a twelve-item DoD matrix, nine open gaps and explicit
limits. It covers 419 pages, 145 entries, 144 cards, 536 routes, 40 recorded
non-routes, 144 partial technical and decision entries, and one blocked source.

Remediation issue #284 added bounded owner sections for the 17 cards whose owner
pages previously mentioned the pattern only in a backlink. It also recorded the
Polyglot `technical-owner-missing` disposition, resolved four avoidable aliases and
wrapped card prose. The 144 exact owner links remain longer than 100 characters
because canonical paths cannot be split; all other V11 prose is checked at <=100 by
`scripts/check_markdown_line_length.py`.

Delivery checks, exact owner/backlink structure and the owner/blocked-source DoD
are met. A self-checked semantic page audit now covers all 419 pages; 166 findings
remain remediation items. Thirty owner pages are shared, and technical sufficiency,
decision sufficiency, owner acceptance and release evidence remain explicitly
**not met**. Human review passed by owner confirmation.
The artifact status remains `delivery-evidence-recorded`; it cannot be marked
`reviewed` without a named independent review record. Phase 5 is therefore not a
final acceptance and does not close #233 or M10.

## Phase 6 semantic page audit

The Phase 6 artifact `edition/patterns/semantic-audit.v1.json` records one
self-checked disposition for each of the 419 canonical pages: 293 sound, 93
sound-with-findings, 32 needs-remediation and 1 blocked. Its 148 findings are
115 low and 33 medium; no high-severity finding was recorded under the recorded
rubric. Reviewer, an independent review agent, returned ACCEPT-WITH-FINDINGS and
its findings were addressed. Owner-confirmed human review passed on 2026-10-21
without a per-page reviewer record. Five gates remain open: owner acceptance, the
blocked Polyglot entry and three deferred page splits.

Each record carries the page SHA-256, a required-check set for its tier, exact
finding anchors and a remediation or gate. The validator recomputes coverage,
hashes, anchors, dispositions and summary counts. The audit is bounded agent
self-review, not claim-by-claim source verification or independent acceptance.

## Family batches

Phase 2B proceeds in bounded batches, each with its own source units and
ledger update:

1. Application architecture and API communication.
2. Messaging, data consistency and event sourcing.
3. Caching and database/storage architecture.
4. Resilience and distributed coordination.
5. Scalability, deployment and legacy modernization.
6. Security, isolation and operational architecture.

Each batch selects exact pages, reads them completely, updates the ledger and
plan, maps registry source units and runs the source validators and tests.

## Acceptance

- Every read unit has a ledger record and every ledger record is referenced by
  a read unit or a foundation record.
- Every planned unit remains `not-read` in the registry.
- No pattern card or technical claim is authored from a planned or blocked unit.
- A family batch is complete only when its required units are read or explicitly
  blocked with a lawful-access reason.

## Limits

Self-checked reading records are not independent review. A public source is not
a benchmark, a production observation or proof that a design fits a workload.

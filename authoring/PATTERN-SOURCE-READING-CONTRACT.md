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

Seventeen of the 24 application/API entries have a read unit after batch 1:
Sidecar, Ambassador, Anti-Corruption Layer, Gateway Routing, Gateway
Aggregation, Gateway Offloading, Backends for Frontends, Database per Service,
Self-contained Service, API Composition, API Gateway, Client-side Discovery,
Server-side Discovery, Microservices, Monolith First, Service Discovery and
Reverse Proxy.

Seven remain planned: Layered Architecture, SOA, Hexagonal Architecture,
Clean/Onion Architecture, Domain-Driven Design, Asynchronous Request-Reply and
Gatekeeper. Their sources are truncated, landing-only or too large to claim a
complete reading in this batch.

Current plan totals: **22 read, 122 planned and 1 blocked** across 145 entries;
the ledger has **23 records**, including three foundation catalog records.
These numbers are progress, not completion.

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

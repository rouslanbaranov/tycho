---
metadata_version: 1
id: "tycho.page.6a386512b280490da745f1ae2c416c58"
kind: "page"
parent_id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/polyglot-persistence.md"
title: "Polyglot Persistence"
topic_ids:
  - "data-architecture"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Polyglot Persistence; invariant and failure/recovery bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should different data responsibilities use different stores while one
      authoritative boundary owns consistency?
  prerequisites:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  related_ids:
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "polyglot persistence"
    - "database and storage architecture"
evidence_scope:
  source_ids:
    - "src.fowler-polyglot"
    - "src.aws-cqrs"
    - "src.microsoft-cloud-patterns"
    - "src.debezium-outbox"
    - "src.postgresql"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch3-fowler-polyglot.2026-10-22,
    read.aws-cqrs.2026-10-30, read.microsoft-cqrs.2026-10-30,
    read.debezium-outbox.2026-10-31 and the three 2026-10-31 PostgreSQL
    logical-replication records; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Polyglot Persistence

**Identity.** Polyglot Persistence; family Database and storage architecture; kind
data-pattern; priority core.

**Decision question.** Should different data responsibilities use different stores
while one authoritative boundary owns consistency?

**Good-fit conditions.** Distinct responsibilities have materially different access
patterns; one store cannot meet a measured requirement; cross-store ownership is assigned;
the four-part invariant (freshness, rebuild, deduplication, schema migration) and failure
recovery are explicit;
the team can operate each store.

**Hard contraindications.** Reject when one store meets the requirement, when no
authoritative owner exists, when cross-store consistency or reconciliation ownership is
undocumented, or when the team cannot operate the additional store.

**Competing alternative.** Single store with derived projections or query-time joins.
Reverse the choice when coordination, migration and operational cost exceed the
workload benefit.

**Failure and recovery.** Stale projections, dual-write ambiguity and partial migration
are common. AWS notes "eventual consistency between the data stores"; Microsoft says the
read model "is eventually consistent with the write model" and recommends a transactional
outbox plus an idempotent consumer; PostgreSQL stops logical replication on a conflict
that raises an error and says it "must be resolved manually by the user"; Debezium exposes
an event id to
"remove duplicate messages". Tycho guidance: publish a freshness bound, rebuild from the
authority, and treat a half-migrated projection as unavailable. Verify freshness and
rebuild in the owner section.

**Technical owner.** [Polyglot Persistence](../../v05-data-models-engines-and-lifecycle/c04-alternative-data-models-and-stores/multi-store-selection.md#polyglot-persistence)
— bounded selection and synchronization criteria, not a complete multi-store design.

**Sources.** [src.fowler-polyglot](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-fowler-polyglot.2026-10-22: sections "Polyglot Persistence",
"Notes". The thematic paragraph labels DatabaseThaw, Complexity and consistency, and Strategic
versus utility projects are not headings; linked material was not read. The source is a public
article, not a benchmark.

The invariant and recovery evidence uses
[src.aws-cqrs](../../../../edition/patterns/reading-ledger.v1.json) record
`read.aws-cqrs.2026-10-30`;
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json) record
`read.microsoft-cqrs.2026-10-30`;
[src.debezium-outbox](../../../../edition/patterns/reading-ledger.v1.json) record
`read.debezium-outbox.2026-10-31`;
[src.postgresql](../../../../edition/patterns/reading-ledger.v1.json) records
`read.postgresql-logical-replication.2026-10-31`,
`read.postgresql-logical-replication-conflicts.2026-10-31` and
`read.postgresql-logical-replication-restrictions.2026-10-31`. Canonical text revisions
are bound in the owner page. These are public documentation pages, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** CQRS Read Projections; CDC; Sharding; Materialized View.

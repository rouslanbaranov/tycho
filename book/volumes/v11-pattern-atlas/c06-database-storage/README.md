---
metadata_version: 1
id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/README.md"
title: "V11/C06 — Database and storage architecture"
topic_ids:
  - "data-architecture"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "13 C06 cards with bounded owner links."
route_hints:
  questions:
    - "Which storage patterns fit the workload and recovery boundary?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  excludes:
    - "No entry claims sufficient technical or decision coverage."
  keywords:
    - "pattern atlas"
    - "database and storage architecture"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.citus"
    - "src.postgresql"
    - "src.cassandra"
    - "src.dynamo"
    - "src.riak"
    - "src.microservices-patterns"
    - "src.flyway"
    - "src.gh-ost"
    - "src.aws-cqrs"
    - "src.microsoft-cloud-patterns"
    - "src.debezium-outbox"
  claim_ids: []
  status: "source-linked"
  notes: >-
    13 cards cite read units; Index Table binds all four dimensions; Polyglot
    Persistence binds invariant and recovery; Backup/PITR has a dedicated card.
    Online Data Migration moved to a dedicated page on 2026-10-31 with Stripe,
    PostgreSQL 18.6 pg_dump/COPY, the AWS DMS User Guide and Flyway
    expand/contract guidance; the changed-mapping case remains a Tycho hazard.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# V11/C06 — Database and storage architecture

**Owning question:** Which storage patterns fit the workload and recovery boundary?

## Purpose and mission

This chapter is the atlas entry point for **Database and storage architecture**. It
owns the conditional decision route for 13 catalog entries, not the deep mechanism
explanations. All thirteen entries have a bounded card; Polyglot Persistence uses a
public article and the V05/C04 selection section.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus dedicated card
pages for moved entries; a later split is an editorial change, not a plan failure. Start
with the card, check its conditions and contraindications, then read the exact owner
section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Sharding

See the [dedicated Sharding card](sharding.md).

### Partitioning

See the [Partitioning](partitioning.md) card.

### Consistent Hashing

See the [dedicated Consistent Hashing card](consistent-hashing.md).

### Leader-Follower Replication

See the [Leader-Follower Replication](leader-follower-replication.md) card.

### Multi-Leader Replication

See the [dedicated Multi-Leader Replication card](multi-leader-replication.md).

### Read Replicas

See the [dedicated Read Replicas card](read-replicas.md).

### Quorum-Based Reads / Writes

See the [dedicated Quorum-Based Reads / Writes card](quorum-based-reads-writes.md).

### Index Table

See the [dedicated Index Table card](index-table.md).

### Polyglot Persistence

See the [dedicated Polyglot Persistence card](polyglot-persistence.md).

### CQRS Read Projections

See the [CQRS Read Projections](cqrs-read-projections.md) card.

### Expand-and-Contract Schema

See the [Expand-and-Contract Schema](expand-and-contract-schema.md) card.

### Online Data Migration

See the [dedicated Online Data Migration card](online-data-migration.md).

### Backup, PITR and Restore

See the [dedicated Backup, PITR and Restore card](backup-pitr-and-restore.md).

## Chapter result and counterexample

Thirteen cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a sharded system with one hot tenant and no resharding plan is not
evidence for the sharding card's partition-key conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C05](../c05-caching-retrieval/README.md).
- Next: [V11/C07](../c07-resilience/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- Thirteen cards cite read ledger units; owner links and backlinks are self-checked.
- Polyglot Persistence is bounded by a public article and an embedded owner section.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.

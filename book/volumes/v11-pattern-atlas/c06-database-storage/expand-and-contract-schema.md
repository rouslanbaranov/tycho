---
metadata_version: 1
id: tycho.page.2fd26c32e60c65ad0e175377d094bf41
kind: page
parent_id: tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
canonical_path: book/volumes/v11-pattern-atlas/c06-database-storage/expand-and-contract-schema.md
title: Expand-and-Contract Schema
topic_ids:
- database-and-storage-architecture
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Expand-and-Contract Schema.
route_hints:
  questions:
  - Should a schema change be deployed in expand, migrate and contract stages?
  prerequisites:
  - tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
  related_ids:
  - tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - expand and contract schema
evidence_scope:
  source_ids:
  - src.flyway
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Expand-and-Contract Schema

**Identity.** Expand-and-Contract Schema; family Database and storage architecture; kind
migration-pattern; priority core.

**Decision question.** Should a schema change be deployed in expand, migrate and contract
stages?

**Good-fit conditions.** Old and new code coexist during rollout; a compatibility window
is owned; backfill and validation are explicit.

**Hard contraindications.** Reject when old and new readers cannot coexist, when no
compatibility window or contract owner exists, or when the mapping cannot preserve identity
and references.

**Competing alternative.** Keep the schema and add a mapping layer, or use a smaller change
when authority need not move. Reverse when staged migration cost exceeds rollout risk.

**Failure and recovery.** Partial backfills and old readers are common; verify gates in
the owner section.

**Technical owner.**
 [Expand-and-Contract
Schema](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/migration-retirement.md#expand-and-contract-schema)
— expand/contract is bounded, not a complete migration runbook.

**Sources.** [src.flyway](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-flyway.2026-10-21: all seventeen served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Online Data Migration; Expand-and-Contract; Backup/PITR; Migration
Retirement.

---
metadata_version: 1
id: "tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb"
kind: "page"
parent_id: "tycho.landing.fe2eace7b2df4ae480adbdf844b68100"
canonical_path: "book/delivery/mixed-version-database-compatibility-and-online-ddl.md"
title: "Backward-compatible database change: mixed-version reads, writes and online DDL"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for Backward-compatible database change: mixed-version reads, writes and online DDL. Scope includes 1. Check the real combinations, including old readers; 2. Expand-migrate-contract includes a compatibility window; 4. Event schema compatibility is an additional axis."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Backward-compatible database change: mixed-version reads, writes and online DDL?"
  prerequisites: []
  related_ids:
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.357c2d162bd44f3aa06a995a1e691551"
    - "tycho.page.b938ff1a06264492a425f2eff555ae7d"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.fe2eace7b2df4ae480adbdf844b68100"
    - "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Backward-compatible"
    - "database"
    - "change"
    - "mixed-version"
    - "reads"
    - "writes"
    - "and"
    - "online"
    - "DDL"
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

# Backward-compatible database change: mixed-version reads, writes and online DDL

> **Tycho independent book manuscript — proposed V08/C05**, 2026-10-19. Official PostgreSQL 17 ALTER TABLE and Confluent Schema Registry evolution guidance were independently consulted for narrow semantics. The examples and rollout checks are original and fictional. No migration, SQL test, event replay, load test or independent expert review occurred. Previous [combined rollout/data study](progressive-delivery-and-schema-evolution.md) remains preserved for detailed evidence mapping.

## Purpose and mission

A successful deployment can fail when an older process reads data written by a newer process. The database engine may accept new DDL, but the application can still misinterpret a status field or require a removed column. **Compatibility is a relation between deployed reader/writer versions and persisted information**, not a single green “schema compatible” Boolean.

This chapter owns **mixed-version reader/writer compatibility and operational schema-change constraints**. [V05/C06 semantic schema migration](../data/schema-lifecycle-and-semantic-migration.md) owns domain identity mapping/backfill and long-term retirement. [V08/C04 rollout](gitops-canary-and-progressive-rollout.md) owns traffic exposure and release strategy.

## 1. Check the real combinations, including old readers

For two binary versions N and N+1 with old, expanded and contracted schema states:

| Running component / data state | Old state | Expanded transition state | Destructive new-only state |
|---|---|---|---|
| Old API N | Known baseline (still test under workload) | Must interpret new optional values and preserve existing writes | Often fails if required old field removed |
| New API N+1 | May require fallback decoder | Must read/write both old and new valid meanings | Target candidate, not safe while N active |
| Old background consumer | Can replay historical events | Must tolerate optional/mapped fields | May reject or silently misread new-only events |
| New consumer | Must still decode retained old events | Mixed-format tests required | New-only assumptions can break replay |
| Restore process | Needs version-compatible backups and readers | Must resolve historical state correctly | Old restore images may fail reading newer data |

An *additive field* may still be semantically incompatible: old code might deserialize a fixed projection, treat unknown enum values as errors, or misclassify absence as an allowed action.

## 2. Expand-migrate-contract includes a compatibility window

The public [Parallel Change method](https://martinfowler.com/bliki/ParallelChange.html) frames an interface expansion, client migration and eventual contract/removal. Applying that to database schemas requires versioned DB-specific locks and data invariants, not just a column rename.

**Original fictional change:** a tool-registration API replaces display_name with canonical_item_id. During coexistence, a temporary schema holds both. New writers must preserve enough old representation for old supported readers until a verified cutover. If an old row has no valid mapping, the new reader must say **unknown**, not invent an ID.

```mermaid
stateDiagram-v2
    [*] --> N: old binary and schema
    N --> Expanded: additive DDL with verified lock budget
    Expanded --> Mixed: N and N+1 read/write matrix passes
    Mixed --> Reconciled: bounded backfill and old consumer inventory
    Reconciled --> Contract: N and historical readers retired
    Mixed --> Hold: any incompatible persisted write
    Hold --> Repair: forward compatibility or verified restore
    Repair --> Mixed: revalidated state
    Contract --> [*]
```

**Text alternative:** expand the representation, run a tested mixed-version phase, reconcile migrated data, and contract only after old readers are proven absent. Incompatible writes hold the rollout and may require forward repair rather than redeploying N. Nothing was actually deployed or migrated.

## 3. DDL is part of the runtime resource budget

[PostgreSQL 17 ALTER TABLE](https://www.postgresql.org/docs/17/sql-altertable.html) documents different lock requirements by alteration; absent a weaker stated lock, ACCESS EXCLUSIVE is acquired. A syntactically simple migration can block concurrent work or require a table rewrite depending on its exact form.

Operations like index creation, adding constraints, validating existing records, backfill and large DDL statements consume CPU, I/O, lock time, WAL and replica replay capacity. Their safety requires knowing the PostgreSQL version, table size and workload.

A safe preflight for an exact proposed statement asks:
- what lock mode and potentially blocking duration?
- does the subcommand rewrite a table or block writes?
- how many rows/bytes and what estimated WAL/replica lag?
- are long transactions and connection queues present?
- how will a partially finished job resume or clean up?
- what does failure do to old and new readers?
- how can we stop the migration before the no-return point?

A lock estimate is not a measurement; test with a realistic fixture before promising a zero-downtime change.

## 4. Event schema compatibility is an additional axis

[Confluent Schema Registry schema evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) distinguishes BACKWARD, FORWARD, FULL and transitive variants, with format-specific rules. It explicitly notes that simple BACKWARD checks cover the previous schema version, not every historical revision.

Even a successful schema registry check is not a guarantee that a domain enum's *meaning* remains compatible. If a new event “Approved” is interpreted as “Pending” by an older consumer, wire parsing might succeed while the user effect fails.

A complete compatibility matrix tests versioned **API, database record, event schema, business status, authorization scope and retention/replay history**. A service may satisfy one transport contract and fail another.

## 5. Rollback has a no-return boundary

Code image rollback is safe only when old N can correctly read and mutate every persisted state written by N+1 during exposure. Once N+1 commits a genuinely new-only state, restoring N containers may reproduce errors or violate business invariants.

| Condition | Possible response |
|---|---|
| Candidate failed before incompatible writes | Route/replica rollback may be valid after checks |
| Candidate wrote additive values N correctly handles | Revert only with verified mixed-version tests |
| Candidate wrote new-only business state N misreads | Hold traffic; forward compatibility/repair or verified restore |
| DDL dropped mandatory N field | Cannot assume N image can operate |
| External effects after cutover | Reconciliation required even if DB schema restored |
| Old event replay after field retirement | Retained decoder or explicitly accepted archival limitation |

A revert command is not recovery of acknowledged reservations or external effects.


### Original compatibility matrix: new writer, old reader, delayed event

A fictional booking application adds a new durable state code `CONFIRMED_V2`. Release N accepts only legacy `CONFIRMED`; N+1 reads both and wants to write the new code. During rolling deployment, old API instances and delayed event consumers can outlive the candidate rollout. An additive SQL column does **not** by itself establish semantic compatibility.

| Reader / writer combination | Proposed permitted behavior | Deployment gate |
|---|---|---|
| N reads N writes | Existing contract | Baseline still checked |
| N+1 reads N writes | New reader must preserve old meaning | Test legacy records and historical replay |
| N reads N+1 writes | **Unsafe** if `CONFIRMED_V2` is not understood | Keep N+1 on old write format until N readers are retired |
| N+1 reads N+1 writes | Target functionality | Verify authorization, meaning and downgrade/repair strategy |
| Delayed N event consumer reads N+1 writes | Separate history version boundary | No old codec may silently discard or misinterpret the event |

A schema rollout requires an actual **capability inventory**, not a belief that all deployed pods have a new image. Mobile/partner clients, queues, batch jobs, database views and backups can retain older semantics. The [Parallel Change description](https://martinfowler.com/bliki/ParallelChange.html) supports coexistence as a change pattern, while [PostgreSQL 17 ALTER TABLE](https://www.postgresql.org/docs/17/sql-altertable.html) documents DDL operations and lock considerations. Neither proves N/N+1 application meaning or migration reversibility.

**Failure:** N+1 canary commits a new-only value, fails its latency checks, then a deployment controller rolls the image back to N. N can no longer read the record; **image rollback is not business rollback**. A safe intermediate stage keeps writes compatible, or otherwise requires a proven forward repair and a separately authorized no-return gate.

**Proposed, unexecuted test:** run the compatibility matrix for each reader/writer/event cohort, inject an interrupted backfill, ensure the old decoder fails explicitly rather than corrupting state, and time DDL under representative table load. Semantic field migration belongs to [V05/C06](../data/schema-lifecycle-and-semantic-migration.md); progressive exposure to [V08/C04](gitops-canary-and-progressive-rollout.md).

## 6. Acceptance tests must include failures

Proposed test fixture (not executed):
1. N clients use N API and N+1 API against expanded schema.
2. N+1 clients exercise both API versions where supported.
3. Old queued event consumed by N+1, and new event by N where still supported.
4. Crash during backfill, then resume without mapping divergence.
5. Concurrent writer changes an identifier while old/new reads occur.
6. Abort a migration after a long lock; measure queue wait and replica lag.
7. Roll back the binary after N+1 produced valid new data.
8. Restore/replay historical state after contract step; verify completeness.

Acceptance includes correct user effects, database invariants, bounded downtime and actual recovery. Green migration SQL alone cannot close the gate.

## 7. Source ledger and remaining verification

| Public evidence | Supported point | Not proven |
|---|---|---|
| [PostgreSQL 17 ALTER TABLE](https://www.postgresql.org/docs/17/sql-altertable.html) | Versioned DDL/lock/subcommand semantics | Actual online migration time |
| [Confluent Schema Registry evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) | Format- and version-specific backward/forward/full compatibility | Business meaning or real consumer compatibility |
| [Danilo Sato Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) | Expansion, migration and contraction as transition method | DB/backfill safety |
| [Prior combined Tycho research](progressive-delivery-and-schema-evolution.md) | Earlier rollout/schema study and failure matrix | Independently accepted chapter split |

Every system, schema, migration diagram and experiment is original synthetic work. No SQL, client/consumer, restore or load test was run and final book metadata remains pending.

**Navigation:** **V08/C05** in [draft outline](../PROPOSED-STRUCTURE.md) via [delivery landing](README.md). Read [data lifecycle](../data/schema-lifecycle-and-semantic-migration.md), [canary/rolling](gitops-canary-and-progressive-rollout.md), [target/transition states](../decisions/target-and-transition-architecture-states.md), [safe recovery](safe-rollout-and-recovery.md).

## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Stripe — Online subscriptions migration](../cases/stripe-online-subscriptions-migration.md)**. **Relevant mechanism or architectural contrast:** Dual-write, change readers, change writers and retire sequence illustrates online authority migration. **Not established by this report/playbook:** Successful company migration is not a generic atomic dual-write guarantee or proof every backfill can safely roll back.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.

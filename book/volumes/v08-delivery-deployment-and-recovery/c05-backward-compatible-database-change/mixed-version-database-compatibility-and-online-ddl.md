---
metadata_version: 1
id: "tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb"
kind: "page"
parent_id: "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c05-backward-compatible-database-change/mixed-version-database-compatibility-and-online-ddl.md"
title: "Backward-compatible database change: mixed-version reads, writes and online DDL"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated question, original scenario and transfer limits for Backward-compatible database change. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What permits old and new binaries/data schemas to coexist?"
  prerequisites: []
  related_ids:
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.357c2d162bd44f3aa06a995a1e691551"
    - "tycho.page.b938ff1a06264492a425f2eff555ae7d"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.fe2eace7b2df4ae480adbdf844b68100"
    - "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.96a702434b714ed4906b1301bc6e0248"
    - "tycho.page.48d9c34e755c4f7ab912ecad14f5794f"
    - "tycho.page.d1fa0462922e4a37922cea279975a3bd"
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
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb:-1 -->

# Backward-compatible database change: mixed-version reads, writes and online DDL

> **Tycho independent book manuscript — V08/C05**, 2026-10-19. Official PostgreSQL 17 ALTER TABLE
> and Confluent Schema Registry evolution guidance were independently consulted for narrow
> semantics. The examples and rollout checks are original and fictional. No migration, SQL test,
> event replay, load test or independent expert review occurred. Previous [combined rollout/data
> study](../../../delivery/progressive-delivery-and-schema-evolution.md) remains preserved for
> detailed evidence mapping.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb:0 -->
## Purpose and mission

A successful deployment can fail when an older process reads data written by a newer process. The database engine may accept new DDL, but the application can still misinterpret a status field or require a removed column. **Compatibility is a relation between deployed reader/writer versions and persisted information**, not a single green “schema compatible” Boolean.

This chapter owns **mixed-version reader/writer compatibility and operational schema-change constraints**. [V05/C06 semantic schema migration](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/schema-lifecycle-and-semantic-migration.md) owns domain identity mapping/backfill and long-term retirement. [V08/C04 rollout](../c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md) owns traffic exposure and release strategy.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb:8 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Stripe — Online subscriptions migration](../../../cases/stripe-online-subscriptions-migration.md)**. **Relevant mechanism or architectural contrast:** Dual-write, change readers, change writers and retire sequence illustrates online authority migration. **Not established by this report/playbook:** Successful company migration is not a generic atomic dual-write guarantee or proof every backfill can safely roll back.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Describe reader/writer compatibility across expansion, coexistence, backfill and contraction stages.

Reverting binaries cannot restore a removed column or reinterpret a new-only persisted value; the no-return point needs forward repair.

The detailed pages separate the mechanisms that make this decision conditional:

- [Reader/writer compatibility and migration stages](reader-writer-matrix.md) — Which combinations must work during expansion, coexistence and contraction?
- [DDL budgets and event compatibility](ddl-events.md) — Which resource and consumer contracts can fail despite a compatible table shape?
- [No-return points and forward repair](no-return-recovery.md) — Which persisted effect makes reverting an old binary unsafe?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

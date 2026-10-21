---
metadata_version: 1
id: "tycho.page.357c2d162bd44f3aa06a995a1e691551"
kind: "page"
parent_id: "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/schema-lifecycle-and-semantic-migration.md"
title: "Schema lifecycle, semantic data migration and data retirement"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Schema evolution, data migration and retention. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What compatibility windows and irreversibility constraints exist?"
  prerequisites: []
  related_ids:
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb"
    - "tycho.page.b938ff1a06264492a425f2eff555ae7d"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.984c44f8dbd44d8e89105b4d31787636"
    - "tycho.page.6b42723bd575413bb0d1b94d3e179b6a"
    - "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
    - "tycho.page.d00c6081ca664f619308712e245ef523"
    - "tycho.page.7e927696162f48beaa33fc834b36ee76"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Schema"
    - "lifecycle"
    - "semantic"
    - "data"
    - "migration"
    - "and"
    - "retirement"
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
<!-- tycho-question-source:tycho.page.357c2d162bd44f3aa06a995a1e691551:-1 -->

# Schema lifecycle, semantic data migration and data retirement

> **Tycho book draft V05/C06**, 2026-10-19. Original synthetic migration and source-led architecture explanation. Sources: Danilo Sato's public Parallel Change and PostgreSQL 17 ALTER TABLE documentation. No schema migration, data backfill, SQL execution or independent review occurred. Previous [combined rollout/schema research](../../../delivery/progressive-delivery-and-schema-evolution.md) is preserved until source claims are reconciled.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.357c2d162bd44f3aa06a995a1e691551:0 -->
## Purpose and mission

A database schema is a contract between stored historical state and all readers/writers able to interpret it. Changing a column name is often trivial syntax; changing the meaning or identity of data may be difficult or irreversible. A safe schema lifecycle must preserve **business meaning**, versioned provenance and recoverability through its transition.

This chapter owns **data modeling changes, backfill consistency, identity mapping, migration checkpoints and removal of retired data**. [V08/C05 mixed-version database compatibility](../../v08-delivery-deployment-and-recovery/c05-backward-compatible-database-change/mixed-version-database-compatibility-and-online-ddl.md) owns old/new deployed reader-writer combinations and operational DDL timing. [V08/C04 progressive rollout](../../v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md) owns traffic exposure and deployment controllers.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.357c2d162bd44f3aa06a995a1e691551:8 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — Casspactor shadow migration](../../../cases/netflix-casspactor-shadow-migration.md)**. **Relevant mechanism or architectural contrast:** Backup identity, shadow comparisons and fallback are distinct evidence gates for pipeline migration. **Not established by this report/playbook:** Comparing row sets alone does not guarantee semantic correctness or zero downtime; company performance evidence remains scoped.

**Case lens — [Uber — Mezzanine PostgreSQL migration](../../../cases/uber-mezzanine-pg-to-schemaless.md)**. **Relevant mechanism or architectural contrast:** Moving data authority requires compatibility seam, identity migration, mirrored writes and backfill reconciliation. **Not established by this report/playbook:** Uber's 2014 store change does not prove abandoning relational databases is generally preferable or fully reversible.

**Case lens — [Spotify — Honk data-consumer migration](../../../cases/spotify-honk-data-consumer-migration.md)**. **Relevant mechanism or architectural contrast:** Agent-assisted dataset changes need context, lineage and affected-repository test gates. **Not established by this report/playbook:** Reported PR counts are not controlled correctness measurements or evidence of fully migrated consumers.

**Case lens — [Meta — Ingestion shadow cutover](../../../cases/meta-ingestion-shadow-migration-lifecycle.md)**. **Relevant mechanism or architectural contrast:** Shadow read/validation, rollout and authority transfer are separate proof obligations for large ingestion migrations. **Not established by this report/playbook:** Source-reported complete migration is not a formal proof of no semantic corruption or transferable production protocol.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Treat data evolution as a semantic compatibility and authority transition, not just a successful DDL command.

A new value interpreted differently by old readers can break a mixed-version system even when every row passes schema validation.

The detailed pages separate the mechanisms that make this decision conditional:

- [Schema shape and preserved meaning](semantic-compatibility.md) — Which old/new representation change can silently alter a domain invariant?
- [Migration stages, retention and no-return points](migration-retirement.md) — Which authority and validation gates permit old data or contracts to be retired?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

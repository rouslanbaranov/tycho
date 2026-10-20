---
metadata_version: 1
id: "tycho.page.d00c6081ca664f619308712e245ef523"
kind: "page"
parent_id: "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
canonical_path: "book/volumes/v05/c06/semantic-compatibility.md"
title: "Schema shape and preserved meaning"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Which old/new representation change can silently alter a domain invariant?"
route_hints:
  questions:
    - "Which old/new representation change can silently alter a domain invariant?"
  prerequisites:
    - "tycho.page.357c2d162bd44f3aa06a995a1e691551"
  related_ids:
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
    - "tycho.page.357c2d162bd44f3aa06a995a1e691551"
    - "tycho.page.7e927696162f48beaa33fc834b36ee76"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "semantic"
    - "compatibility"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.357c2d162bd44f3aa06a995a1e691551; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Schema shape and preserved meaning

**Owning question:** Which old/new representation change can silently alter a domain invariant?

This page belongs to [V05/C06 — Schema evolution, data migration and retention](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.357c2d162bd44f3aa06a995a1e691551:1 -->
## 1. Distinguish syntactic change from semantic change

| Change | Syntactic requirement | Domain integrity requirement |
|---|---|---|
| Add optional display field | Older rows can represent absence | Missing does not imply an invented business value |
| Rename external identity | Reader accepts old and new names during transition | Both names resolve to the same durable logical entity |
| Split one field into two | New columns and mapping function | Original cases map without ambiguity or loss |
| Change enum/status meaning | Codec accepts versioned old/new labels | Old accepted state is not misread as pending/rejected |
| Split a table into entities | Data-copy and foreign keys | Historical relationships, authorization and ownership survive |
| Delete a field | No remaining declared readers | Replays, archives and restoration no longer depend on it |

An “additive schema” can still be a *semantic breaking change* if a new writer interprets the field differently or an old consumer hard-codes projection order.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.357c2d162bd44f3aa06a995a1e691551:2 -->
## 2. Original synthetic scenario: two equipment identities

In a fictional tool catalogue the original field asset_code conflates a public model description and a unique physical unit. A new model separates model_id (shared by identical units) and unit_id (physical item). Simply copying asset_code into both fields can create collisions, incorrect reservations and misleading history.

A safe migration requires a **totality analysis**:
- Which old code maps to a unique physical unit?
- Which records represent a model/type rather than one unit?
- Can mappings be many-to-one, one-to-many or unknown?
- How are links to historical reservations converted?
- Which source revision proves each mapping?
- What if a new record arrives while backfill is in progress?

Mappings that cannot be proven must be marked unresolved for domain review rather than silently defaulted.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](schema-lifecycle-and-semantic-migration.md) |
| Next | [Continue the reasoning](migration-retirement.md) |
| Integrated question | [Original scenario and limits](schema-lifecycle-and-semantic-migration.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

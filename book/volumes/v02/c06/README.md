---
metadata_version: 1
id: "tycho.chapter.4f7542e57fb74052a4a31cd4c4dce46a"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02/c06/README.md"
title: "V02/C06 — Integration adapters and anti-corruption boundaries"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How can incompatible domains and legacy contracts coexist?"
route_hints:
  questions:
    - "How can incompatible domains and legacy contracts coexist?"
  prerequisites:
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V02/C06 — Integration adapters and anti-corruption boundaries

## Purpose and mission

How can incompatible domains and legacy contracts coexist? This chapter owns that question within application boundaries and interaction contracts. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Specify what an adapter preserves, rejects and cannot translate, including its eventual retirement conditions.

A syntactically valid mapping can discard domain meaning; coexistence needs a reconciliation authority for unknown or unmappable results. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Anti-corruption adapters: semantic translation and safe coexistence](anti-corruption-adapters-and-coexistence.md) | How can incompatible domains and legacy contracts coexist? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. An adapter has a semantic contract, not just a schema mapping](anti-corruption-adapters-and-coexistence.md#1-an-adapter-has-a-semantic-contract-not-just-a-schema-mapping).
- [2. Original synthetic case: an equipment catalogue migration](anti-corruption-adapters-and-coexistence.md#2-original-synthetic-case-an-equipment-catalogue-migration).
- [7. Public source-to-claim ledger](anti-corruption-adapters-and-coexistence.md#7-public-source-to-claim-ledger).
- [Engineering walkthrough — Lossy translation behind a seemingly compatible API](anti-corruption-adapters-and-coexistence.md#engineering-walkthrough-lossy-translation-behind-a-seemingly-compatible-api).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../c05/README.md) |
| Next | [V02/C07 — Authorization boundaries and multitenancy](../c07/README.md) |
| Prerequisite | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../c05/README.md) |
| Source reading | [Page-local evidence and versions](anti-corruption-adapters-and-coexistence.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

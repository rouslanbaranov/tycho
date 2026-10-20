---
metadata_version: 1
id: "tycho.chapter.abc85388b50f470493bef4e204d6f2dc"
kind: "chapter"
parent_id: "tycho.volume.e826731e3543471f94d5eb9af68cbfa7"
canonical_path: "book/volumes/v10/c06/README.md"
title: "V10/C06 — Search and question routes for architecture agents"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How can requirements, symptoms and evidence guide selective reading?"
route_hints:
  questions:
    - "How can requirements, symptoms and evidence guide selective reading?"
  prerequisites:
    - "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
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

# V10/C06 — Search and question routes for architecture agents

## Purpose and mission

How can requirements, symptoms and evidence guide selective reading? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Route a question to a small set of canonical explanations, inspect exact evidence and refuse unsupported synthesis.

A relevant but stale passage cannot justify an answer about another version; retrieve missing conditions rather than guessing. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Architecture questions: progressive reading and evidence-bounded decision routes](question-routes-for-architecture-analysis.md) | How can requirements, symptoms and evidence guide selective reading? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. First classify the intent before fetching pages](question-routes-for-architecture-analysis.md#1-first-classify-the-intent-before-fetching-pages).
- [2. The progressive reading strategy](question-routes-for-architecture-analysis.md#2-the-progressive-reading-strategy).
- [Engineering walkthrough — Route, read and reject a stale but plausible answer](question-routes-for-architecture-analysis.md#engineering-walkthrough-route-read-and-reject-a-stale-but-plausible-answer).
- [9. Public evidence and navigation](question-routes-for-architecture-analysis.md#9-public-evidence-and-navigation).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V10 — Decision support and modernization playbooks](../README.md) |
| Previous | [V10/C05 — Target architecture versus transition states](../c05/README.md) |
| Next | [V10/C07 — Cross-domain worked comparisons and unresolved cases](../c07/README.md) |
| Prerequisite | [V10/C05 — Target architecture versus transition states](../c05/README.md) |
| Source reading | [Page-local evidence and versions](question-routes-for-architecture-analysis.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

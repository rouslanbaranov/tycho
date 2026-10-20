---
metadata_version: 1
id: "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01/c04/README.md"
title: "V01/C04 — Evidence, hypotheses and architecture experiments"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What do sources, estimates, simulations and measurements actually prove?"
route_hints:
  questions:
    - "What do sources, estimates, simulations and measurements actually prove?"
  prerequisites:
    - "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
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

# V01/C04 — Evidence, hypotheses and architecture experiments

## Purpose and mission

What do sources, estimates, simulations and measurements actually prove? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Keep published semantics, synthetic arithmetic, hypotheses and observed experiments as distinct evidence classes with different permissible conclusions.

A cache experiment can improve latency while failing freshness; the result rejects that configuration rather than proving a universal claim about caching. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Architecture evidence, competing hypotheses and decision experiments](architecture-evidence-hypotheses-and-experiments.md) | What do sources, estimates, simulations and measurements actually prove? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Five evidence classes are not substitutes](architecture-evidence-hypotheses-and-experiments.md#1-five-evidence-classes-are-not-substitutes).
- [2. Competing hypotheses beat single-cause stories](architecture-evidence-hypotheses-and-experiments.md#2-competing-hypotheses-beat-single-cause-stories).
- [7. Public ledger and limitations](architecture-evidence-hypotheses-and-experiments.md#7-public-ledger-and-limitations).
- [Engineering walkthrough — A falsifiable cache-versus-query experiment](architecture-evidence-hypotheses-and-experiments.md#engineering-walkthrough-a-falsifiable-cache-versus-query-experiment).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [V01/C03 — Quality attributes and trade-offs](../c03/README.md) |
| Next | [V01/C05 — Architecture descriptions and decision records](../c05/README.md) |
| Prerequisite | [V01/C03 — Quality attributes and trade-offs](../c03/README.md) |
| Source reading | [Page-local evidence and versions](architecture-evidence-hypotheses-and-experiments.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

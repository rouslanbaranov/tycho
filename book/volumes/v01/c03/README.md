---
metadata_version: 1
id: "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01/c03/README.md"
title: "V01/C03 — Quality attributes and trade-offs"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How are performance, availability, consistency, cost, security and changeability made measurable?"
route_hints:
  questions:
    - "How are performance, availability, consistency, cost, security and changeability made measurable?"
  prerequisites:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.microservices"
  claim_ids: []
  status: "source-linked"
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

# V01/C03 — Quality attributes and trade-offs

## Purpose and mission

How are performance, availability, consistency, cost, security and changeability made measurable? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Convert a quality preference into a stimulus, environment, observable response and rejection condition, then compare only feasible candidates.

A faster candidate remains inadmissible when it loses an integrity or isolation guarantee; a weighted score cannot repair a failed hard gate. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Architecture drivers, quality scenarios and readable system views](quality-drivers-and-architecture-views.md) | How are performance, availability, consistency, cost, security and changeability made measurable? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Name the decision before selecting a style](quality-drivers-and-architecture-views.md#1-name-the-decision-before-selecting-a-style).
- [2. Quality-attribute scenarios must be testable](quality-drivers-and-architecture-views.md#2-quality-attribute-scenarios-must-be-testable).
- [Engineering walkthrough — An apparently faster architecture that fails a hard invariant](quality-drivers-and-architecture-views.md#engineering-walkthrough-an-apparently-faster-architecture-that-fails-a-hard-invariant).
- [Sources, scope and known limitations](quality-drivers-and-architecture-views.md#sources-scope-and-known-limitations).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [V01/C02 — Workload and demand models](../c02/README.md) |
| Next | [V01/C04 — Evidence, hypotheses and architecture experiments](../c04/README.md) |
| Prerequisite | [V01/C02 — Workload and demand models](../c02/README.md) |
| Source reading | [Page-local evidence and versions](quality-drivers-and-architecture-views.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

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
summary: "How are performance, availability, consistency, cost, security and changeability made measurable? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How are performance, availability, consistency, cost, security and changeability made measurable?"
  prerequisites:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
  related_ids:
    - "tycho.page.06b70cb83d4f490ea9ef698a025e7684"
    - "tycho.page.3c865baa588744ecbaac307c81c4b25c"
    - "tycho.page.b5d667aa6dac4a98a7c6ba8b10852897"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](quality-drivers-and-architecture-views.md) | How are performance, availability, consistency, cost, security and changeability made measurable? |
| [Hard gates and measurable quality scenarios](quality-scenarios.md) | How is a quality preference converted into a testable acceptance condition? |
| [Views, trade-offs and rejected candidates](views-tradeoffs.md) | How do the same traffic and different constraints lead to different architecture decisions? |

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

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.06b70cb83d4f490ea9ef698a025e7684:7 -->
## Sources, scope and known limitations

| Evidence | Public source and precise read scope | Supports / limits |
|---|---|---|
| E01 | [arc42, Section 1: Introduction and Goals](https://docs.arc42.org/section-1/), §§1.1 Requirements Overview, 1.2 Quality Goals and 1.3 Stakeholder, inspected 2026-10-18 | Prioritized architecture quality drivers and stakeholder/requirement framing, not a technology selection algorithm |
| E02 | [The Site Reliability Workbook, Chapter 2: Implementing SLOs](https://sre.google/workbook/implementing-slos/), sections *Why SREs Need SLOs* and *Getting Started*, inspected 2026-10-18 | Agreed user-oriented objectives and evidence-driven reliability decisions; no achieved SLO for these fictional cases |
| E03 | [C4 Model by Simon Brown, Introduction](https://c4model.com/introduction), inspected 2026-10-18 | Progressive context/container/component/code and supporting dynamic/deployment perspectives; not a fixed Mermaid syntax |
| E04 | [Lewis & Fowler, Microservices](https://martinfowler.com/articles/microservices.html), 2014, *Componentization via Services* and *Design for failure* | Costs and characteristics of service-based boundary decisions; descriptive, not a proof of optimality |

**Review state:** public-source-bounded explanation and author self-check, no independent human review, no real product requirements approval and no executed scenario. Full ISO quality models, comprehensive standards taxonomy and measurable product comparisons are not claimed researched.

**Explicit unanswerable example:** "Can we safely promise 99.99% availability with two containers and an existing database?" No answer without eligible good-event definition, dependency failure domains, data recovery path, traffic patterns, capacity under failure and demonstration that those mechanisms can meet the proposed objective.
<!-- /tycho-question-source -->

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
summary: "How can requirements, symptoms and evidence guide selective reading? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How can requirements, symptoms and evidence guide selective reading?"
  prerequisites:
    - "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
  related_ids:
    - "tycho.page.ca056fe720e74a9691ce0c253d9526fc"
    - "tycho.page.72cbc98ca3164b759626e5a9e0bfad9c"
    - "tycho.page.c603a8bc4c5a40fd8642b72b6657a557"
    - "tycho.page.31301a539883499fbf4aa7796271d099"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](question-routes-for-architecture-analysis.md) | How can requirements, symptoms and evidence guide selective reading? |
| [Intent classification and selective reading](intent-reading.md) | Which canonical explanation must be read before composing an answer? |
| [Attributable synthesis and safe refusal](evidence-safety.md) | Which version, permission or evidence conflict should constrain the answer? |
| [Validation of architecture question routes](route-validation.md) | Which answerable and unanswerable cases test the route's actual contract? |

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

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.ca056fe720e74a9691ce0c253d9526fc:10 -->
## 9. Public evidence and navigation

| Source | Supported aspect | Limit |
|---|---|---|
| [SEI ATAM collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/) | Quality attribute interactions and architecture risk evaluation | No automated recommendation algorithm |
| [arc42 quality requirements](https://docs.arc42.org/section-10/) | Specific, testable quality scenarios | No automatic corpus relevance scoring |
| [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | Data versus instruction trust-boundary risk | A real service's secured deployment |
| [Tycho cross-domain decisions](../c07/cross-domain-modernization-and-adr-examples.md) | Conditional architecture choices and synthetic ADR | A live implementation or peer-reviewed architecture approval |

All sample inputs, reading paths, diagrams and outputs are original educational cases. There is **no executed retrieval, model answer benchmark, operating agent, deployed adapter or independent domain sign-off**. Any numeric or version-sensitive claim requires source verification in its original chapter before operational adoption.

**Reading navigation:** proposed **V10/C06** in [planned chapters](../../../PROPOSED-STRUCTURE.md); current section [decision support](../../../decisions/README.md). Start with [Requirements/workload](../c01/requirements-and-workload-architecture-profiles.md), [Legacy evidence](../c02/legacy-baseline-and-modernization-evidence.md), [Architecture decision examples](../c07/cross-domain-modernization-and-adr-examples.md). For source/graph distinctions, read [hybrid retrieval as a System Design subject](../../v06/c05/hybrid-ranking-graph-and-evaluation.md)—not as a Tycho graph delivery requirement.
<!-- /tycho-question-source -->

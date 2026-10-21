---
metadata_version: 1
id: "tycho.chapter.5b8edae85f83413997cac0c873919b57"
kind: "chapter"
parent_id: "tycho.volume.4a94b1e6f8234841afaa51af14330627"
canonical_path: "book/volumes/v09-observability-security-and-operations/c07-safety-isolation-and-privacy-in-agent-accessible-services/README.md"
title: "V09/C07 — Safety, isolation and privacy in agent-accessible services"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What can remote readers infer or retrieve under bounded permissions? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What can remote readers infer or retrieve under bounded permissions?"
  prerequisites:
    - "tycho.chapter.691463ecbf6f44af84274ab3ff798b3d"
  related_ids:
    - "tycho.page.0ae1aabac3b64c2f924cc427684bdbab"
    - "tycho.page.6315cc62b4384a64b31f8694d77d1c35"
    - "tycho.page.7987026eace9417a8c3a1d4dbc6c7da0"
    - "tycho.page.b38397b1d9fe456dbdb30e5b2ec2f3c8"
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

# V09/C07 — Safety, isolation and privacy in agent-accessible services

## Purpose and mission

What can remote readers infer or retrieve under bounded permissions? This chapter owns that question within observability, security and operational architecture. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Enforce caller permissions, collection boundaries and bounded tool effects independently of retrieved text.

Relevant source text may contain instructions; retrieval must not grant it authority to execute actions or cross data boundaries. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision](safe-agent-access-and-knowledge-isolation.md) | What can remote readers infer or retrieve under bounded permissions? |
| [Principals, retrieval and bounded tool effects](principal-tools.md) | Which boundary prevents retrieved instructions from acquiring execution authority? |
| [Collection identity, privacy and retention](collection-privacy.md) | Which content and metadata may each caller observe across snapshots? |
| [Negative access tests and architecture limits](agent-negative-tests.md) | Which denial or unavailable-evidence outcome must an agent-accessible service preserve? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V09 — Observability, security and operational architecture](../README.md) |
| Previous | [V09/C06 — Incident response and operational change](../c06-incident-response-and-operational-change/README.md) |
| Next | [V10/C01 — Architecture requirement and workload profiles](../../v10-decision-support-and-modernization/c01-architecture-requirement-and-workload-profiles/README.md) |
| Prerequisite | [V09/C06 — Incident response and operational change](../c06-incident-response-and-operational-change/README.md) |
| Source reading | [Page-local evidence and versions](safe-agent-access-and-knowledge-isolation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.0ae1aabac3b64c2f924cc427684bdbab:8 -->
## 8. Public evidence ledger and navigation

| Independently public source consulted | Narrow supported aspect | Open limitation |
|---|---|---|
| [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | Untrusted retrieved content, indirect injection, limits of RAG-only mitigation | Effectiveness of any invented controls in deployed agent |
| [OWASP LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) | Risk from overly broad functions, permissions, autonomy | Validated risk review of a specific tool/plugin runtime |
| [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Least privilege, deny by default and per-object entitlement | All application-specific policy decisions |
| [OWASP Authorization Patterns](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Patterns_Cheat_Sheet.html) | Policy enforcement/decision point responsibilities | Formal enforcement correctness of imaginary API |

All example data, diagrams, test cases and recommendations are original educational design illustrations. No private corpus was accessed or used as a source, no customer data was processed, and no actual security test was performed. Further source precision, independent review, client compatibility and operating tests remain open.

**Navigation:** future V09/C07 in [proposed book outline](../../../PROPOSED-STRUCTURE.md), current [security landing](../../../security/README.md). Prerequisites: [Authorization and trust boundaries](../c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md), [Tracing and audit](../../../observability/trace-context-lineage-and-audit.md). Related: [Search/retrieval architecture](../../v06-caching-indexing-and-retrieval/c05-hybrid-retrieval-and-reranking/hybrid-ranking-graph-and-evaluation.md), [cross-domain architecture decisions](../../v10-decision-support-and-modernization/c07-cross-domain-worked-comparisons-and-unresolved-cases/cross-domain-modernization-and-adr-examples.md).
<!-- /tycho-question-source -->

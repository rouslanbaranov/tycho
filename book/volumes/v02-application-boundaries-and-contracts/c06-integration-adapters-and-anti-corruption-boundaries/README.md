---
metadata_version: 1
id: "tycho.chapter.4f7542e57fb74052a4a31cd4c4dce46a"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c06-integration-adapters-and-anti-corruption-boundaries/README.md"
title: "V02/C06 — Integration adapters and anti-corruption boundaries"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How can incompatible domains and legacy contracts coexist? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How can incompatible domains and legacy contracts coexist?"
  prerequisites:
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
  related_ids:
    - "tycho.page.31c8e450f78c451d90cb6090df330c5a"
    - "tycho.page.e5195a1aafa640359f05aebc08744584"
    - "tycho.page.5778597986df46439eee0aa162de2729"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](anti-corruption-adapters-and-coexistence.md) | How can incompatible domains and legacy contracts coexist? |
| [Semantic translation and rejected values](semantic-translation.md) | Which meaning must an adapter preserve and which input must it refuse? |
| [Coexistence, unknown outcomes and adapter retirement](coexistence-retirement.md) | How is a lost acknowledgment reconciled before old contracts are retired? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../c05-public-apis-http-rpc-and-compatibility/README.md) |
| Next | [V02/C07 — Authorization boundaries and multitenancy](../c07-authorization-boundaries-and-multitenancy/README.md) |
| Prerequisite | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../c05-public-apis-http-rpc-and-compatibility/README.md) |
| Source reading | [Page-local evidence and versions](anti-corruption-adapters-and-coexistence.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.31c8e450f78c451d90cb6090df330c5a:7 -->
## 7. Public source-to-claim ledger

| Inspected public source | Narrow supported point | Not established |
|---|---|---|
| [Microsoft ACL pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) | Boundary translation, operational/latency/trust/consistency trade-offs | Real inventory protocol guarantees |
| [Fowler — Bounded Context (2014)](https://martinfowler.com/bliki/BoundedContext.html) | Internally consistent but differing domain models | Specific mapping completeness |
| [Microsoft Strangler Fig pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) | Controlled coexistence during incremental replacement | Validated cutover of fictional data |
| [Tycho legacy baseline](../../v10-decision-support-and-modernization/c02-baseline-analysis-for-existing-software/legacy-baseline-and-modernization-evidence.md) | General evidence-first modernization methodology | Executed migration or accepted target architecture |

All system names, mappings, state-machine decisions, examples and figures are invented for teaching. No proprietary DDD book was reproduced. No integration, failure injection, independent reviewer or real-system validation has been performed. The exact final edition chapter/page hierarchy remains pending.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.31c8e450f78c451d90cb6090df330c5a:9 -->
## Navigation

- Proposed **V02/C06**, current [application landing](../../../application/README.md).
- Prerequisites: [Domain boundaries/data ownership](../c02-domain-boundaries-data-ownership-and-contracts/domain-boundaries-data-ownership-and-contracts.md), [API contract evolution](../c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md).
- Related: [Outbox/retries](../../../distributed/transactional-outbox-and-idempotency.md), [safe rollout](../../../delivery/safe-rollout-and-recovery.md), [legacy assessment](../../v10-decision-support-and-modernization/c02-baseline-analysis-for-existing-software/legacy-baseline-and-modernization-evidence.md).
<!-- /tycho-question-source -->

---
metadata_version: 1
id: "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02/c05/README.md"
title: "V02/C05 — Public APIs, HTTP/RPC and compatibility"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do deadlines, versioning, retries and API contracts evolve?"
route_hints:
  questions:
    - "How do deadlines, versioning, retries and API contracts evolve?"
  prerequisites:
    - "tycho.chapter.a7cb3581936b46ab9fd3a49c17e9cc6c"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.http-semantics"
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

# V02/C05 — Public APIs, HTTP/RPC and compatibility

## Purpose and mission

How do deadlines, versioning, retries and API contracts evolve? This chapter owns that question within application boundaries and interaction contracts. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Define behavioral compatibility, operation identity, end-to-end budgets and caller-visible unknown outcomes alongside the wire format.

A lost response after commit is compatible with transport failure; blindly replaying a state-changing request may create another effect. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [HTTP and RPC contracts: compatibility, deadlines and retry safety](http-rpc-contracts-and-compatibility.md) | How do deadlines, versioning, retries and API contracts evolve? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. The contract has multiple layers](http-rpc-contracts-and-compatibility.md#1-the-contract-has-multiple-layers).
- [2. HTTP method semantics are not business-effect deduplication](http-rpc-contracts-and-compatibility.md#2-http-method-semantics-are-not-business-effect-deduplication).
- [Engineering walkthrough — Mixed clients and an unacknowledged committed POST](http-rpc-contracts-and-compatibility.md#engineering-walkthrough-mixed-clients-and-an-unacknowledged-committed-post).
- [Applied M9 evidence: what transfers and what does not](http-rpc-contracts-and-compatibility.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C04 — SOA, microservices and distributed boundaries](../c04/README.md) |
| Next | [V02/C06 — Integration adapters and anti-corruption boundaries](../c06/README.md) |
| Prerequisite | [V02/C04 — SOA, microservices and distributed boundaries](../c04/README.md) |
| Source reading | [Page-local evidence and versions](http-rpc-contracts-and-compatibility.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

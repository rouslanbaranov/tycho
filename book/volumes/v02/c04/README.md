---
metadata_version: 1
id: "tycho.chapter.a7cb3581936b46ab9fd3a49c17e9cc6c"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02/c04/README.md"
title: "V02/C04 — SOA, microservices and distributed boundaries"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When is independent deployment justified by measured coordination cost?"
route_hints:
  questions:
    - "When is independent deployment justified by measured coordination cost?"
  prerequisites:
    - "tycho.chapter.5de52a840c14448c946a65c924f28487"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.soa-model"
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

# V02/C04 — SOA, microservices and distributed boundaries

## Purpose and mission

When is independent deployment justified by measured coordination cost? This chapter owns that question within application boundaries and interaction contracts. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Justify a remote boundary through independent ownership or deployment needs while accounting for communication and recovery costs.

Separate containers can still require synchronized releases and share one fragile datastore; deployment count does not demonstrate independence. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Service orientation, microservices and distributed boundaries](service-orientation-microservices-and-distribution.md) | When is independent deployment justified by measured coordination cost? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Separate concept, deployment and ownership](service-orientation-microservices-and-distribution.md#1-separate-concept-deployment-and-ownership).
- [2. Independence is not proved by a separate container](service-orientation-microservices-and-distribution.md#2-independence-is-not-proved-by-a-separate-container).
- [7. Test a distributed boundary before deciding](service-orientation-microservices-and-distribution.md#7-test-a-distributed-boundary-before-deciding).
- [8. Public source-to-claim ledger and limitations](service-orientation-microservices-and-distribution.md#8-public-source-to-claim-ledger-and-limitations).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C03 — Modular monolith and internal events](../c03/README.md) |
| Next | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../c05/README.md) |
| Prerequisite | [V02/C03 — Modular monolith and internal events](../c03/README.md) |
| Source reading | [Page-local evidence and versions](service-orientation-microservices-and-distribution.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

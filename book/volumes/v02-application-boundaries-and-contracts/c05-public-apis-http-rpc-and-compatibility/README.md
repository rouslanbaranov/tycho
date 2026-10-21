---
metadata_version: 1
id: "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/README.md"
title: "V02/C05 — Public APIs, HTTP/RPC and compatibility"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do deadlines, versioning, retries and API contracts evolve? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do deadlines, versioning, retries and API contracts evolve?"
  prerequisites:
    - "tycho.chapter.a7cb3581936b46ab9fd3a49c17e9cc6c"
  related_ids:
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.e7e65b602c5a41fb80fa4a1e88a33298"
    - "tycho.page.43414664520b4866929f7f006f27f59b"
    - "tycho.page.de9c5bc478ba44718fcb731e69109dce"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](http-rpc-contracts-and-compatibility.md) | How do deadlines, versioning, retries and API contracts evolve? |
| [API contracts and effect identity](effect-identity.md) | Which promises belong to transport semantics and which require application deduplication? |
| [Deadlines, cancellation and retry budgets](deadlines-retries.md) | How should one end-to-end time budget bound nested calls and retries? |
| [Behavioral compatibility and interface choice](version-compatibility.md) | Which old/new caller and server combinations must remain valid? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C04 — SOA, microservices and distributed boundaries](../c04-soa-microservices-and-distributed-boundaries/README.md) |
| Next | [V02/C06 — Integration adapters and anti-corruption boundaries](../c06-integration-adapters-and-anti-corruption-boundaries/README.md) |
| Prerequisite | [V02/C04 — SOA, microservices and distributed boundaries](../c04-soa-microservices-and-distributed-boundaries/README.md) |
| Source reading | [Page-local evidence and versions](http-rpc-contracts-and-compatibility.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.


## Further mechanism and recovery questions

- [Conditional updates, pagination and callback contracts](version-compatibility.md#conditional-updates-pagination-and-callback-contracts) — source-scoped enrichment; examples and proposed tests are not executed results.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:7 -->
## 7. Public sources and evidence limits

Inspected independently public reference sections on 2026-10-19, with the following narrow scope:

| Reference | Used for | What it does not establish |
|---|---|---|
| [RFC 9110 — HTTP Semantics, §§9.2.1–9.2.2, 10.2.3, 15](https://www.rfc-editor.org/rfc/rfc9110.html) | Safe/idempotent method properties, retry and Retry-After/status envelope | Application-level deduplication or actual server conformance |
| [RFC 9457 — Problem Details, §§3–5](https://www.rfc-editor.org/rfc/rfc9457.html) | Structured HTTP API problem contracts and information-disclosure cautions | Universal application error taxonomy |
| [OpenAPI 3.2.1, published 2026-09-10](https://spec.openapis.org/oas/v3.2.1.html) | Interface-description contract and versioned document semantics | Runtime semantic compatibility or measured deployment outcome |
| [gRPC deadlines](https://grpc.io/docs/guides/deadlines/) and [cancellation](https://grpc.io/docs/guides/cancellation/) | Deadline concepts, propagation, responsibility to terminate spawned work | Identical defaults in all languages or effect rollback |
| [gRPC retries](https://grpc.io/docs/guides/retry/) and [service configuration](https://grpc.io/docs/guides/service-config/) | Retry scopes, configured attempts/backoff and client policy | Domain idempotency for arbitrary methods |
| [Protocol Buffers editions](https://protobuf.dev/programming-guides/editions/) and [schema best practices](https://protobuf.dev/best-practices/dos-donts/) | Wire tag identity, reserved tags and evolution hazards | Safe behavior of every decoder or deployed schema migration |

**Original modeling and unknowns:** preview-job identities, budget numbers, failure matrices, architecture selection table and tests above are original proposals/synthetic examples; no test, production observation, real latency measurement, independent expert review or citation-snapshot packaging is claimed. Language/runtime compatibility, actual OpenAPI 3.2.1 tooling support and any environment-specific protocol choice must be checked for the actual target deployment. The wider V02 volume and Tycho book remain incomplete.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:8 -->
## Reading and navigation

- Parent: [Application boundaries and architecture styles](../../../application/README.md); planned future volume owner **V02/C05** in the [69-chapter outline](../../../PROPOSED-STRUCTURE.md).
- Before: [Architecture styles and module boundaries](../../../application/architecture-styles-and-module-boundaries.md).
- Related: [Transactional outbox and idempotency](../../../distributed/transactional-outbox-and-idempotency.md), [Safe schema evolution](../../../delivery/progressive-delivery-and-schema-evolution.md), [Authorization isolation](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md), [Java reactive execution](../../v03-execution-concurrency-and-flow-control/c03-reactive-streams-demand-and-cancellation/reactor-webflux-r2dbc-and-backpressure.md).
- Next: mixed-version runnable consumer/provider tests and detailed streaming reconnect semantics (unimplemented, future authoring work).

<!-- /tycho-question-source -->

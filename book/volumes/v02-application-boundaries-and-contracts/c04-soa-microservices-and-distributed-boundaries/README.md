---
metadata_version: 1
id: "tycho.chapter.a7cb3581936b46ab9fd3a49c17e9cc6c"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c04-soa-microservices-and-distributed-boundaries/README.md"
title: "V02/C04 — SOA, microservices and distributed boundaries"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When is independent deployment justified by measured coordination cost? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "When is independent deployment justified by measured coordination cost?"
  prerequisites:
    - "tycho.chapter.5de52a840c14448c946a65c924f28487"
  related_ids:
    - "tycho.page.acb452608a8b42898aae7482c27f5f04"
    - "tycho.page.4e0e4db7547b45469f36915886473750"
    - "tycho.page.cdb86c0b91a6489f979689ab08efad35"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision](service-orientation-microservices-and-distribution.md) | When is independent deployment justified by measured coordination cost? |
| [Independent deployment and its costs](service-independence.md) | Which coordination costs justify introducing a remote boundary? |
| [Service contracts and failure evaluation](service-contracts.md) | What must be tested when a capability moves into another process? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C03 — Modular monolith and internal events](../c03-modular-monolith-and-internal-events/README.md) |
| Next | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../c05-public-apis-http-rpc-and-compatibility/README.md) |
| Prerequisite | [V02/C03 — Modular monolith and internal events](../c03-modular-monolith-and-internal-events/README.md) |
| Source reading | [Page-local evidence and versions](service-orientation-microservices-and-distribution.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.acb452608a8b42898aae7482c27f5f04:8 -->
## 8. Public source-to-claim ledger and limitations

| Independent public reference | Narrow support | Not verified |
|---|---|---|
| [OASIS SOA Reference Model v1.0, §3.2](https://docs.oasis-open.org/soa-rm/v1.0/soa-rm.html) | Visibility, interaction, service descriptions, capabilities and real-world effects | A mandatory SOA transport, deployment shape or runtime implementation |
| [Lewis/Fowler, *Microservices*, 25 Mar 2014](https://www.martinfowler.com/articles/microservices.html) | Independently deployable capability-aligned service style and operational characteristics | Any particular team's readiness or performance advantage |
| [Original Tycho style comparison](../../../application/architecture-styles-and-module-boundaries.md) | Earlier researched style dimensions and trade-offs | Approved target design or independently tested system |

The examples, candidate rankings, diagram, failures and experiments are independent synthetic educational material. They do not describe any real organization's stack. Source-level admission and final manuscript editorial acceptance remain pending.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.acb452608a8b42898aae7482c27f5f04:9 -->
## Navigation

This is canonical **V02/C04** in the current edition. Start at [application architecture](../../../application/README.md), then read [domain ownership](../c02-domain-boundaries-data-ownership-and-contracts/domain-boundaries-data-ownership-and-contracts.md), [ports and adapters](../c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md), [service extraction](../../../application/architecture-evolution-and-extraction.md), [target/transition states](../../v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/target-and-transition-architecture-states.md).
<!-- /tycho-question-source -->

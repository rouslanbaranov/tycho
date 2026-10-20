---
metadata_version: 1
id: "tycho.chapter.e365b78505784c20a4f3d72fe7904d9b"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07/c01/README.md"
title: "V07/C01 — Queueing, Little's Law and measurement boundaries"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What do arrival, throughput, mean response and in-flight counts imply?"
route_hints:
  questions:
    - "What do arrival, throughput, mean response and in-flight counts imply?"
  prerequisites:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
    - "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
    - "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
  related_ids:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.little-law"
    - "src.sre-overload"
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

# V07/C01 — Queueing, Little's Law and measurement boundaries

## Purpose and mission

What do arrival, throughput, mean response and in-flight counts imply? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Apply occupancy and rate identities only to the same measured boundary, population and time semantics.

A finite window with unfinished work or rejection outside the boundary can invalidate naive arithmetic, and means cannot predict p99. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Queueing, Little's Law and workload measurement boundaries](queueing-littles-law.md) | What do arrival, throughput, mean response and in-flight counts imply? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [Orientation: four numbers that are not interchangeable](queueing-littles-law.md#orientation-four-numbers-that-are-not-interchangeable).
- [Architecture: Little's Law is an average identity](queueing-littles-law.md#architecture-littles-law-is-an-average-identity).
- [Independent public sources and exact claim support](queueing-littles-law.md#independent-public-sources-and-exact-claim-support).
- [Verification checklist and next bounded research](queueing-littles-law.md#verification-checklist-and-next-bounded-research).

## Boundaries and further reading

- [V01/C02 — Workload and demand models](../../v01/c02/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V06/C07 — Retrieval evaluation and index lifecycle](../../v06/c07/README.md) |
| Next | [V07/C02 — Contention, saturation and scaling laws](../c02/README.md) |
| Prerequisite | [V01/C02 — Workload and demand models](../../v01/c02/README.md) |
| Prerequisite | [V01/C03 — Quality attributes and trade-offs](../../v01/c03/README.md) |
| Prerequisite | [V01/C04 — Evidence, hypotheses and architecture experiments](../../v01/c04/README.md) |
| Prerequisite | [V03/C05 — Thread, connection and buffer pools](../../v03/c05/README.md) |
| Prerequisite | [V04/C04 — Retries, idempotency and duplicate effects](../../v04/c04/README.md) |
| Source reading | [Page-local evidence and versions](queueing-littles-law.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

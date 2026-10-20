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
summary: "What do arrival, throughput, mean response and in-flight counts imply? The reading route separates 3 detailed questions from the integrated decision."
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
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.335682a8957c46d294535b5912762e91"
    - "tycho.page.252426e0630c495d9cad7cb2c518fc69"
    - "tycho.page.a648fc495dab474489d17d01e2c5dd92"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](queueing-littles-law.md) | What do arrival, throughput, mean response and in-flight counts imply? |
| [Population boundaries and Little's Law](measurement-boundary.md) | When are occupancy, throughput and mean residence time comparable? |
| [Finite windows and load-generator feedback](finite-window.md) | Why can unfinished work and closed-loop arrivals invalidate a naive estimate? |
| [Overload, recovery and alternative measurements](queue-recovery.md) | Which admission and exit policy makes the queue's recovery observable? |

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

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b:8 -->
## Independent public sources and exact claim support

These references were read to the **named portions** on 2026-10-18. No complete external book, paid text, source repository or benchmark dataset was copied into this chapter.

| Evidence ID | Public work / fixed or observed version | Exact section read | What it supports / does not support |
|---|---|---|---|
| **E01** | Kim & Whitt, *Statistical Analysis with Little's Law*, *Operations Research* **61(4)**, 2013, pp. 1030–1045, DOI **10.1287/opre.2013.1193**; [author PDF](https://www.columbia.edu/~ww2040/LL_OR.pdf) | **Abstract; §§1, 1.1–1.2** | Long-run/stationary versus finite observation estimates, need for statistical reasoning, boundary effects. Not a tested application capacity model. |
| **E02** | Same fixed 2013 primary paper | **§2.1 definitions; §2.2 finite-time relation / Theorem 1 and interval edge effects** | Finite-window equality requires appropriate boundaries (special case begins and ends empty). Does not make arbitrary sampled averages exact or justify percentile substitution. |
| **E03** | Grafana k6 official documentation, *Open and closed models*, observed **v2.2.x** online page on 2026-10-18; [source](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) | **Closed Model; Drawbacks of using the closed model; Open model** | Feedback-coupled vs independent iteration scheduling and potential coordinated omission. Not a performance measurement of this synthetic service. |
| **E04** | *Site Reliability Engineering* (Google SRE authors), **Handling Overload**, public 2017 book edition; [source](https://sre.google/sre-book/handling-overload/) | **Client-Side Throttling** and closing per-task overload discussion | Cost of rejection and motivation for upstream throttling; behavior of the source's described context, not universal numbers or Tycho's measured results. |

**External source status:** these are exact chapter-reading observations; the source inventory's broad discovery status is retained because its current schema lacks claim/section-level reading fields. The per-page ledger here records the narrower inspected scope. Do not silently overwrite broader source-level status to "entire book verified".

**Evidence claims vs original inference:** E01–E04 support the named concepts only. All numerical scenarios, request-flow diagrams, finite-window toy request and arithmetic here are **original synthetic constructions**. Discussion of pool sizing and architecture choice is reasoned guidance contingent on actual workload evidence, not a direct assertion that any named deployment failed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b:9 -->
## Verification checklist and next bounded research

- [x] One canonical reader question and named measurement boundary.
- [x] Long-run mean formula, units and exact finite-window counterexample.
- [x] Open-versus-closed distinction tied to identified official documentation.
- [x] Normal, burst/overload, dependency saturation and recovery cases.
- [x] Synthetic numbers and outcomes clearly separated from empirical measurements.
- [x] At least one valid **insufficient-evidence** answer.
- [ ] User-independent human/subject expert review (not claimed).
- [ ] Benchmark / service instrumentation / real capacity test (not claimed).
- [ ] Full book metadata schema / graph / indexed retrieval (planned in other issues).

**Decision example — deliberately insufficient evidence:** "An application has 100,000 users, receives 120 RPS and has p99 of 2 seconds. How many nodes and DB connections should it have?" **Answer:** Cannot determine from those figures. Request actual arrival/mix, completed throughput, mean time per named boundary, resource/service demand, queue/connection limits, timing distribution, peak/failure assumptions, SLOs and a representative load experiment.

**Next technical scope:** [Pilot #39](https://github.com/rouslanbaranov/tycho/issues/39) studies whether state commit and event publication remain correct across retries and partial failure. This page does not attempt to prove its transaction/event behavior.
<!-- /tycho-question-source -->

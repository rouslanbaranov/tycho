---
metadata_version: 1
id: "tycho.page.af6ce1d0b08a46bf908f851f77f7bb12"
kind: "page"
parent_id: "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
canonical_path: "book/volumes/v07/c02/scaling-models.md"
title: "Parallelism, serial work and scaling models"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which model assumptions bound useful throughput as concurrency grows?"
route_hints:
  questions:
    - "Which model assumptions bound useful throughput as concurrency grows?"
  prerequisites:
    - "tycho.page.7ad835c06d5a4e3aabf6b14632f92c86"
  related_ids:
    - "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
    - "tycho.page.7ad835c06d5a4e3aabf6b14632f92c86"
    - "tycho.page.61c621bfa9a04a738e937416cec15e78"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "scaling"
    - "models"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.7ad835c06d5a4e3aabf6b14632f92c86; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Parallelism, serial work and scaling models

**Owning question:** Which model assumptions bound useful throughput as concurrency grows?

This page belongs to [V07/C02 — Contention, saturation and scaling laws](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.7ad835c06d5a4e3aabf6b14632f92c86:1 -->
## 1. Concurrency, parallel execution and completed throughput differ

- **Concurrency:** tasks or operations are simultaneously in progress or resident at a defined boundary, perhaps mostly waiting.
- **Parallelism:** useful operations execute on different processors/resources at the same time.
- **Throughput:** logical operations correctly completed per unit time at an identified system boundary.
- **Saturation:** a resource or policy cannot provide additional useful service at rising offered demand; backlog, rejection, latency or failure may grow.
- **Scalability:** the relationship between resources and useful completed capacity for a *specified workload and configuration*.

Adding application workers increases potential concurrency but does not guarantee processor time, DB write throughput, network quota, exclusive-key authority or larger useful completion rate. Increasing throughput by skipping correctness checks or quietly refusing requests is not a valid scale gain.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7ad835c06d5a4e3aabf6b14632f92c86:2 -->
## 2. Amdahl's conditional bound

If an idealized fixed total computation has a serial share s and a perfectly parallel remaining share (1−s), its ideal speedup with N processors is

S(N) = 1 / [s + (1−s)/N].

This is a **model**, not a universal service scalability theorem. Assume s = 0.2 and N = 8. The theoretical speedup is 1 / (0.2 + 0.8/8) = **3.33**, not 8. That result ignores memory contention, cross-processor communication, queues, storage, workload redistribution, hardware and software overhead. It does not predict throughput for arbitrary API traffic.

A system may change its parallel fraction when the workload or partitioning changes. Do not infer the serial share from a single latency sample.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7ad835c06d5a4e3aabf6b14632f92c86:3 -->
## 3. A model for contention and coordination overhead

Neil J. Gunther's [general theory of computational scalability](https://arxiv.org/abs/0808.1431) discusses rational scalability functions and a synchronous throughput bound. A commonly used *normalized* form of the Universal Scalability Law is

C(N) = N / [1 + α(N−1) + βN(N−1)].

Here N is a relative concurrency/processor count; α and β are empirical fitting parameters interpreted (with important model qualifications) as contention and coherence/coordination penalties. The expression is **not** a mechanism detector. Fitted coefficients cannot prove that a particular lock, network link or cache-invalidation flow is the cause.

The curve may show:
- roughly linear growth for small N when penalties are weak;
- diminishing returns when shared-resource contention dominates;
- **retrograde** throughput at higher N if coordination work increases faster than useful work.

Any fit must be made across enough observations with the same workload mix and bounded resource costs. Compare predictions with withheld test points, retain confidence/uncertainty and investigate observed bottleneck signals. A pretty curve with little data is not evidence that microservices or more replicas will help.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](contention-saturation-and-scaling-laws.md) |
| Next | [Continue the reasoning](contention-response.md) |
| Integrated question | [Original scenario and limits](contention-saturation-and-scaling-laws.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

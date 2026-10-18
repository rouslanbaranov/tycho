# Pilot wave 01 — bounded research contracts and authoring order

Status: **research scope approved for execution by recorded project issue sequencing**, not technical conclusions. Prepared 2026-10-18 for [Issue #26](https://github.com/rouslanbaranov/tycho/issues/26).

## Why these three, and why now?

Tycho currently has a discovered public-source index, methods and an outline but no fully researched chapters. The first cycle must write **real technical knowledge** under limited scope and expose missing evidence rather than finish all architecture-decision tooling in advance.

| Pilot type | Contract | Execution issue | Proposed canonical home | Distinct failure case / practical outcome |
|---|---|---|---|---|
| **Mechanism** | [Queueing, Little's Law and arrival-rate measurement](contracts/PILOT-01-queueing.md) | [#38](https://github.com/rouslanbaranov/tycho/issues/38) | V07/C01 | Avoid invalid latency/concurrency inference from RPS or p99; handle burst and unknown downstream capacity |
| **End-to-end interaction** | [Local transaction and external event](contracts/PILOT-02-transactional-outbox.md) | [#39](https://github.com/rouslanbaranov/tycho/issues/39) | V04/C04–C05 | Local commit succeeds while publication/reply fails; duplicate delivery vs exactly-once business effect |
| **Recovery / transition** | [Rollout, compatibility and recovery](contracts/PILOT-03-rollout-recovery.md) | [#40](https://github.com/rouslanbaranov/tycho/issues/40) | V08/C04–C07 | Failed release, old/new schema coexistence, irreversible writes, RPO/RTO uncertainty |

All fictional examples are newly invented; the contracts may use one original workshop-registration story to compare mechanisms **without** treating that story as measured reality or merging the three distinct canonical owner topics.

## Binding gates before chapter prose

- Source admission: independent public origin and lawful reading already required by [Tycho governance](../governance/INDEPENDENCE.md); inspect exact source versions/sections during each execution issue. No private systems or derivations.
- Authorship: follow [the editorial contract](EDITORIAL-CONTRACT.md), [research workflow](RESEARCH-WORKFLOW.md) and [technical page template](../templates/technical-page.md).
- Provenance: citation per material claim to exact primary section/revision; separate published claim, empirical reproduction, inference and assumption.
- Distinctions: registered sources may have only entry-page discovery status. An inspected public URL is not proof of reading a full standard, release guide or paid book.
- Testing: use deterministic arithmetic/consistency examples if useful; never imply production benchmarks or human approval. Run existing CI/boundary/source checks and inspect link integrity.
- Lifecycle: one sub-issue → one branch → one PR, passing checks → scoped completion. Keep whole-book enrichments and index rebuilds separate.
- Evaluation: for each pilot create at least one counterexample, failure/recovery path, explicit uncertainty and a measure-first/insufficient-evidence answer.

## Scope exclusions and questions deferred

These pilots **do not** complete PostgreSQL, Kafka, Spring, deployment or resilience books; they establish three small canonical owner slices and a tested research/authoring method. Product version peculiarities, exact performance capacity and high-consequence guarantees must not be invented when evidence is missing.

- Issue #18 legacy modernization profile and #19 applicability cards become stronger **after** these researched slices, because they can link to real evidence.
- Schema/frontmatter/index/graph tooling and read-only MCP remain mandatory roadmap work, but should not gate first researched pages. Manual exact-source and available mechanical checks serve as temporary prerequisites.
- Recording these contracts does **not** establish their technical findings. Close #26 only for verified authoring-scope completion.

## Minimal pilot readiness criteria

1. A person or AI agent can answer the primary pilot question from its canonical page plus bounded linked evidence.
2. Key assertions have traceable, version-aware independent public sources.
3. There is one normal and one failure/recovery flow, alternatives and applicability limits.
4. An unanswerable case returns an explicit measurement or source-inspection task.
5. Structural/source checks succeed; self-review vs independent review are not conflated.

**Execution order:** #38 → #39 → #40. The first actual book-content commit occurs in **#38**, not in this planning issue.

# Research contract — TYCHO-17: requirements and workload profile

- **Stable ID:** TYCHO-17-RC-v0.1
- **Reader and decision supported:** architect, analyst, product decision-maker or specialized agent comparing general System Design choices by explicit requirements and proposed workloads.
- **Primary question and significance:** what business, quality, load, team, evidence and economic inputs must be recorded *before* architecture pattern selection, and how do we avoid invented throughput/availability claims?
- **Required subquestions:** How are hard gates distinguished from preferences? How are quality scenarios and their measures formulated? How do active users, arrivals, mix, skew, mean concurrency, latency tail, growth, SLO denominators and recovery requirements relate? What causes an "insufficient evidence" outcome?
- **Scope:** proposed workload/profile model, reusable Markdown template and one original synthetic case. This is not a technical architecture comparison, technology benchmark, modernization baseline, serialization schema, implementation or deployment.
- **Assumptions and synthetic scenario:** a wholly fictional community workshop registration service, with invented user populations, operation mix, growth/peak scenarios, seat-capacity invariant and resource unknowns.
- **Canonical owner and dependencies:** [profile model](../models/requirements-workload-profile.md), [template](../../templates/requirements-workload-profile.md), [case study](../../examples/synthetic-workshop-registration.md). The later issues #18/#19 will consume these inputs. No blockers for issue #17.
- **Normal flow, failure, invariants and alternatives to investigate:** registration under nominal/peak offered load; hot-seat contention; missing replies/retries; single-instance loss; distinction between rejecting demand and corrupting state. Compare architectures *later*, after material evidence.
- **Completion criteria:** all three [issue #17 acceptance criteria](https://github.com/rouslanbaranov/tycho/issues/17) covered; links resolve; provenance narrow, calculations internally consistent, policy scans and CI pass; no invented evaluation; independent review status stated correctly.
- **Unknowns and contradictions:** actual user behavior, peak distribution, fan-out, contention, total cost, resource capacity, recovery mechanisms and attainable SLOs are unknown. Synthetic hard goals may conflict; document that instead of asserting feasibility.
- **Research coverage:** bounded inspection of three independent public pages below, not full books or full documentation sets. No source code or benchmarks inspected or executed.
- **Explanatory sufficiency:** draft methodology plus a fill-in contract and illustrative arithmetic; consumer can identify what to measure, not what architecture to choose.
- **Evidence support:** source passages support only profile framing, SLI definition and arrival-process caution. All numerical values and business policies are newly invented thought-experiment inputs; they require no empirical attribution but cannot be presented as verified claims.
- **Review scope:** self-check and automated structural checks only. No independent subject expert or human sign-off recorded.
- **Version applicability and freshness:** public web sections inspected 2026-10-18; live documentation may change. Repository source register remains intentionally discovery-level because its current validator has no section-level read status.
- **Validation performed:** record actual CI results in PR/issue after checks; do not mark planned checks complete here.
- **Exact next action:** after review and merge, begin #18 legacy profile and #19 applicability cards; separately implement source evidence metadata and schema infrastructure in assigned later issues.

## Source-to-claim register for this bounded research

All sources were already identified and admitted at **public origin** in [Tycho's source register](../../sources/register.json). No content was downloaded or mirrored into Tycho. All public-source statements here are *methodological*.

| Source / publisher | Exact inspected page and section | Supported narrow point | Limits / status |
|---|---|---|---|
| `src.arc42` / arc42 authors | [Section 1, §1.1 Requirements Overview and §1.2 Quality Goals](https://docs.arc42.org/section-1/) | Requirement drivers and stakeholder/quality goal framing | Public rolling site; no pinned release and no claim of reading all sections |
| `src.sre-workbook` / Google SRE authors | [The Site Reliability Workbook, Chapter 2, "What to Measure: Using SLIs" and "Moving from SLI Specification to SLI Implementation"](https://sre.google/workbook/implementing-slos/) | Good-event ratio, eligible denominator, user relevance, specification versus measurement-vantage trade-offs | Website chapter, not the full book; targets in synthetic example are original assumptions |
| `src.k6` / Grafana Labs | [Open and closed models: Closed Model, Drawbacks, Open model](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) | Arrival-rate and completion-coupled workload distinctions; feedback/coordinated omission caveat | Latest page displayed v2.2.x on inspection; no installed executor, benchmark or empirical claim |
| `src.little-law` / published paper inventory | Registered [2013 paper pointer](https://www.columbia.edu/~ww2040/LL_OR.pdf) **not inspected for this issue** | None asserted from that paper; mathematical example is only a conditional identity demonstration | Later bounded reading/measurement required for sophisticated queueing or finite-window analysis |

**Source independence:** case facts are invented from first principles and unrelated to any pre-existing deployment; generalized authoring concepts only were used. No external source text was copied.

## Acceptance self-check (not project-level approval)

- [x] Hard constraints, preferences, business outcomes and measurable quality-attribute scenarios represented in model/template/example.
- [x] Population, arrival, concurrency, mix, key skew, payloads, storage growth and SLO definition included with units and boundaries.
- [x] Fully synthetic case contains explicit arithmetic, uncertainty, contradictions and validation needs.
- [ ] Independent subject review, actual workload measurement, schema/graph implementation and candidate architecture evaluation — **outside the completed scope of this issue**.

Issue completion is proposed after automated verification and review; a passing branch CI is not human acceptance.

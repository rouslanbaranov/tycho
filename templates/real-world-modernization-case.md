# Real-World Modernization Case — Authoring Template

> **Template only.** This is an original Tycho case-analysis contract, not an existing corporate architecture. Each case must be written in independent prose from admitted primary sources. Do not copy an external diagram, transcript, screenshot or long article passage.

## Identity and context

- Case ID: `case.<company>.<slug>`
- Title / owning case-study chapter:
- Company and original authors:
- Publication / event dates and historical observation window:
- Source record IDs and **exact original section / slide / timestamp / revision**:
- Source access/reuse status:
- Status: proposed / source-reviewed / drafted / mechanically-validated / human-reviewed
- Evidence confidence (per-claim, not a single arbitrary score):
- Canonical related Tycho concept/pattern/implementation IDs:

## Decision in one paragraph

Describe the situation, actual engineering constraint, candidate choices, selected change and the reason. Distinguish a *reported historical case* from Tycho's independent recommendation.

## Before: observed system and pressure

- Deployment/runtime topology, data ownership, relevant technologies **with versions**:
- Workload context: users, RPS/TPS, concurrency, fanout, partition skew, data size, p95/p99, cost and SLOs **only when sourced**:
- Business/organizational boundaries and ownership:
- Failure, security or scaling symptoms, and how they were diagnosed:
- What was unknown (do not invent missing baselines):

## Alternatives, selection and rejection

| Option | What it would change | Benefits under recorded constraints | Costs, contraindications and evidence gaps | Why accepted/rejected |
|---|---|---|---|---|
| Retain current design / tune | | | | |
| Incremental refactor | | | | |
| Selected design | | | | |
| Other meaningful candidate | | | | |

List context that would reverse the decision. Do not claim the original engineering team evaluated any alternative unless sourced; mark Tycho-created comparisons as **analytical alternatives**, not historical fact.

## During: safe transition architecture

Describe steps in time order: compatibility, strangler/adapter, dual-read/write or shadow where appropriate, backfill, reconciliation, version drift, canary, monitoring, rollback/forward-fix and legacy retirement. Mark unsupported measures as `not documented`.

Provide *original* Mermaid before/after diagram(s) with textual explanation, evidence pointers for every nontrivial architectural fact, and boundaries/flows labelled. Preserve distinctions among observed code, published design intent and inference.

## After: outcomes and remaining problems

| Measure / claim | Before | After | Unit / sample / version / time window | Evidence section | Confidence / caveat |
|---|---|---|---|---|---|
| p99, throughput, cost, deploys, reliability, developer time ... | | | | | |

Report negative outcomes, failed experiments, old bottlenecks, new trade-offs and subsequent changes. Do not equate a vendor marketing statement, simulated benchmark and production measurement.

## Applicability and contraindications

- Required workload and organization prerequisites:
- When a smaller modular monolith, simpler database or conventional thread-pool solution is preferable:
- Constraints that disqualify this pattern:
- Observable gates for adoption and rollback:
- What must be measured **in the reader's own system** before copying anything:

## Evidence ledger and conflicts

| Claim ID | Assertion (observation vs inference) | Exact source pointer | Publication period | Verification state | Contradictions / limitations |
|---|---|---|---|---|---|

Include original author, URL, access date, relevant section/timestamp, repository commit SHA where any source-code is cited. If sources disagree, record both and reconcile only with further evidence.

## Cross-case synthesis and routing

- Related real-world cases with opposite choices (required for major recommendation claims):
- Related canonical Tycho patterns: links to existing pages; do not duplicate explanatory owners:
- Search tags: baseline, bottleneck, quality attribute, workload regime, transition pattern, runtime version, evidence status:
- Explicit Markdown cross-links to relevant cases, pattern pages and decision chapters, with the evidence/conditions in prose (not graph edges):
- Decision prompts the Rocinante agent can use, including a valid `insufficient evidence` outcome:
  - Stage gate the reported evidence supports — proof of concept, minimum
    viable product or product — and what remains unproven at the next gate.

## Acceptance checklist

- [ ] Primary sources and allowed usage verified; access/revision/date recorded.
- [ ] Technical claims have exact section/timestamp citations; numeric measures include workload and reporting context.
- [ ] Historical phases distinguished; no invented company's internal topology, metrics or intentions.
- [ ] Legacy / constraints / rejected alternatives / migration / failure / outcome / applicability all covered.
- [ ] Negative and incomplete cases explicitly represented.
- [ ] At least one original Mermaid architecture or transition figure where useful, plus readable text alternative.
- [ ] Contrasting company/pattern case linked; no 'because Netflix does it' inference.
- [ ] Independent source and link checks passed; manual semantic review is not silently marked complete.
- [ ] Stable case IDs, metadata/index, cross-page Markdown links and source-backed retrieval are verifiable; **no curated graph, graph edges, traversal, graph pipeline or graph maintenance is requested or built**.
- [ ] `authoring/STATE.md`, source register and research log updated **in the accepted implementation phase**, not by this planning template.

## Content-completeness gate (M9, binding)

A page is **content-complete** only when the author can answer, in source-bounded English prose: (1) what existed and who owned it; (2) what workload/legacy constraints motivated the change and what is unknown; (3) which observed solution was chosen and which *analytical*, not falsely historical, alternatives are plausible; (4) what sequence and compatibility/recovery controls were actually reported versus recommended by Tycho; (5) which tests, failure paths and negative results were recorded; (6) what happened after, with dated denominators or an explicit *not published*; (7) when another team should or should not reuse the decision; and (8) exactly which public source section supports each material claim. Meaningful contrasts must link to other case pages. Do not fabricate missing results to meet a checklist or mark draft work independently approved. Educational Mermaid diagrams remain optional when they clarify the case; they do not imply construction of a machine-readable graph.

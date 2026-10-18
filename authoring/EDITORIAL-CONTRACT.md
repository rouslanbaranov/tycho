# Tycho editorial, navigation and page contract

Status: draft editorial contract v0.1 for [Issue #24](https://github.com/rouslanbaranov/tycho/issues/24). This narrows the existing [authoring methodology](METHODOLOGY.md) into directly usable templates, without claiming any technical chapter or formal metadata schema is finished.

## Purpose: author material rather than endlessly design templates

The first accepted authoring target is **one researched question**, not a volume-sized writing job. A reviewer/agent must be able to answer it by loading a bounded page and, only when necessary, linked adjacent pages and precise independent public evidence. Pages must stand alone enough to explain the relevant question; repeating the entire parent chapter defeats token-efficient retrieval.

The proposed structure lives in [the question-driven book plan](../book/PROPOSED-STRUCTURE.md). It is not an approved full TOC and should be revised based on the first real written chapters. No empty volume/chapter/page directory tree is required.

## Template contracts

| Document kind | Canonical responsibility | Template or boundary |
|---|---|---|
| **Book/volume landing** | Purpose and mission, reading routes, children, status/gaps; no long mechanism duplication | [volume landing](../templates/volume-landing.md); existing `book/README.md` |
| **Chapter landing** | A concrete engineering question and the ordered pages that explain it | [chapter landing](../templates/chapter-landing.md) |
| **Technical explanation** | One mechanism, its conditions, normal/failure/recovery and exact evidence | [technical page](../templates/technical-page.md) |
| **Research contract** | What will be read/tested, scope, evidence gaps and readiness | Existing [research contract](../templates/research-contract.md); not a chapter |
| **Catalogue / index** | Finding aids and source locations; generated or validated from canonical ownership, never competing explanatory text | Existing [source catalogue](../sources/CATALOG.md) and planned index K12 |
| **Operational procedure** | Steps, preconditions, safety/rollback, observed validation, named versions; not a generalized pattern assertion | Use technical-page evidence rules, but emphasize tested procedure; introduce a specialized template only with a researched need |
| **Pattern applicability card** | Preconditions, disqualifiers, alternatives, workload envelope, migration conditions and evidence | Dedicated implementation is **#19 after researched pilots**; do not fabricate cards or universal thresholds in #24 |
| **Decision / ADR** | A choice for declared requirements with evidence and alternatives, not an arbitrary technology ranking | Dedicated #20; use real pilot evidence before generalizing |

The classification above is an **editorial distinction**, not a JSON Schema enumeration. Formal metadata kinds, generated frontmatter and stable persistent IDs belong to #32–#34. A template heading is not a machine-readable schema.

## Page size, depth and splitting decisions

- A page has **one primary reader question and one canonical owner**. A long mechanism should be split when independent failure/recovery/consistency or performance questions require separate evidence. Very short pages that cannot answer a complete question should be consolidated; do not mechanically target a fixed word/character quota.
- Write the shortest **correct** explanation that covers assumptions, the mechanism, risks, bounds, and evidence. Avoid filler, speculative architecture endorsements and boilerplate empty headings. Sections irrelevant to the question may be omitted with scope explanation.
- For a first retrieval pass, the existing authoring policy suggests reading **up to three relevant canonical pages** and expanding when needed for correctness. This is a routing heuristic, not a cap on evidence.
- Use one **Orientation → Architecture → Evidence** page when sufficient. Split into coherent pages only when required to preserve bounded context, source precision and canonical ownership. A chapter landing lists links only to files that actually exist.
- The proposed first three pilot page families in `book/PROPOSED-STRUCTURE.md` are candidate *research slices*; #26 chooses and scopes them, #38–#40 write actual text.

## Navigation rules and failures

- **Book landing:** Purpose and Mission; visible proposed or live volume routes and authoring state.
- **Volume landing:** why the volume exists, direct child questions, prerequisites, cross-volume ownership and open gaps.
- **Chapter landing:** specific question, ordered current page links, conceptual boundary, alternatives and what to read next.
- **Page:** linked canonical parent and adjacent owner, explicit claim source IDs/URLs/versions, bounded next question and unknowns.
- Do not create dead links to planned pages. A plain `TODO` is clearer than a broken URL. Link targets are verified through existing checks as available; full link/anchor validation remains #36/#37.
- Prefer **relative repository paths** for navigation and explicit public source URLs/revision paths for provenance. Keep stable citations in a future metadata/index model instead of hardcoding page numbers.
- Every summary must be reversible to a canonical explanation and exact evidence. An agent should never have to infer a mechanism from title or taxonomy alone.

## Diagrams, examples, snippets and tables

**Mermaid-first visual policy:** use fenced `mermaid` in Markdown at volume, chapter and technical-page levels whenever a diagram materially clarifies topic relationships, state/data ownership, normal and failure sequences, deployment topology, rollback, or decisions. Use `flowchart` for architectural structure and reading paths, `sequenceDiagram` for messages/timing, `stateDiagram-v2` for lifecycle/recovery, and specialized forms only when meaningful. Choose the smallest legible diagram; do not require a diagram on a purely textual page, count diagrams as a quality metric, or manufacture decorative graphics.

Diagrams must be original, editable Mermaid source inside the Markdown, not image-only renderings. Provide nearby prose and a compact text alternative for accessibility and agents unable to render diagrams. State scope, assumptions, synthetic versus observed status, and exact supporting source when portraying factual guarantees. Diagrams never substitute for evidence or imply that synthetic flows were tested. Keep Mermaid syntax simple, close code fences and check rendering where supported.

- **Source code snippets:** quote only the smallest portion necessary to establish a precise fact or test case, subject to reuse/license terms. Prefer versioned upstream links and explanations to large mirrored code blocks.
- **Synthetic examples:** define invented requirements and numbers explicitly; show arithmetic with units and assumptions. Do not imply observed benchmarks, production outcomes, or a real employer system.
- **Tables:** compare alternatives across equivalent workload, versions, failure boundaries and measures; use tables when they clarify differences rather than to fill a quota.
- **Procedures:** list prerequisites, validation, failure stop conditions, rollback/forward recovery and side effects. Do not give irreversible steps without explicit caution and conditions.
- **Metric charts or data:** source, collection window, sample, percentile/mean distinction, exclusions and confidence must accompany claims. Do not generate decorative graphs as evidence.

## Validation and review criteria for an authored page

1. A research contract identifies audience, question, boundary, admitted sources and completion state.
2. Purpose and explanation support a real engineering decision; ownership and relative navigation are clear.
3. Normal path, partial failure, recovery and invariants are investigated where material; missing items are explicit.
4. Each material correctness/security/performance claim has an exact independently public source or reproducible observation; inference and unknowns are labelled.
5. Code, diagrams and excerpts meet source access/reuse constraints.
6. Existing boundary/source checks run; local links and anchors are inspected. Strict JSON Schema, index and graph validation **cannot be claimed implemented** until their issues deliver them.
7. Semantic self-review and any independent reviewer are recorded separately. Only completed evidence-backed work can be marked reviewed.

## Immediate application

Use [volume landing](../templates/volume-landing.md), [chapter landing](../templates/chapter-landing.md) and [technical page](../templates/technical-page.md) **when #26 authorizes the bounded pilot topic and source-reading scope**. Avoid creating empty documents before research. This contract completes the minimal editorial prerequisites; #25 defines controlled reading/deepening/checkpoint workflow, and #26 specifies exactly three initial research contracts. The next priority is real evidence-backed chapter prose, not more universal template variants.

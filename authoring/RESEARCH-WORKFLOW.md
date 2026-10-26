# Bounded research, deepening and readiness workflow

Status: v0.1 authoring workflow, Issue [#25](https://github.com/rouslanbaranov/tycho/issues/25). This makes the existing [methodology](METHODOLOGY.md) executable for the **first three authored technical pilots**. It is not a request to regenerate the book, run enrichment, or build infrastructure before any pages exist.

## One research contract → one coherent page/section

1. **Select the next open pilot question** from the [proposed book structure](../book/PROPOSED-STRUCTURE.md); name one canonical chapter/page owner and link its GitHub issue. Read the current [checkpoint](STATE.md), [public register](../sources/register.json), [reading plan](../sources/READING-PLAN.md) and [editorial contract](EDITORIAL-CONTRACT.md).
2. **Write a bounded contract** using [templates/research-contract.md](../templates/research-contract.md): precise question, audience, in/out scope, allowed sources and exact intended version/section, expected normal/failure/recovery phenomena, acceptance tests and unknowns. Do not silently expand to nearby chapters.
3. **Admit and inspect primary public evidence** before technical assertions: verify origin, version/revision, legal access, subsection/code path and relevant limitations; record the scope *actually read*. The existing source register starts at discovery status, not substantive chapter coverage. Unavailable paid sources cannot support technical claims.
4. **Record a source-to-claim ledger** in the page itself or accompanying contract for material correctness/consistency/performance/security claims. Mark each as published, reproduced/tested, inference, hypothesis or unknown. A source's statement about itself is not an independent measurement.
5. **Write the minimal canonical explanation** with [technical-page template](../templates/technical-page.md): orientation → architecture → evidence, named assumptions, interfaces/state/data ownership, normal execution, partial failure and recovery, enforceable invariants, trade-offs and simpler alternatives. Declare if something is out of scope; avoid mandatory filler.
6. **Verify with available tools and honest manual checks**: run repository boundary/source checks, inspect relative links and source targets, manually assess whether cited sections really support each high-consequence claim, check units/arithmetic and untested conditions. Full JSON Schema/graph/index validation remains later work and is not claimed to pass.
7. **Record independent review as a separate event** if obtained. Self-review + green CI are not human approval or verified runtime behavior. Keep unanswered high-risk claims in `insufficient evidence` state and name a finite next experiment or reading task.
8. **Update the research log and checkpoint once** for completed work. Record artifact paths, source/revision limitations and checks executed. Never modify unrelated chapters, recompute every index, or refresh all sources just because one page changes. Open a feature-branch PR referencing its single issue, review/merge, then close only that bounded issue.

## Deepening is a separate, controlled pass

A first researched page is intentionally focused. A deepening pass is justified by (a) a material omitted mechanism, (b) a contradiction or source revision, (c) a failure case that changes applicability, or (d) evaluation showing a concrete unanswered question. Capture the delta in a bounded contract and edit only the canonical owner(s), then re-check affected links/claims. **Do not automatically re-enrich the corpus.**

A new major source version does **not** automatically prove an older claim wrong. Mark affected claims as *potentially stale*, identify the changed behavior and comparison scope, and re-verify before closing that flag. Keep source metadata freshness, factual verification, editorial edits and actual
independent AI review distinct.

## Readiness dimensions (not one unreliable percentage)

| Dimension | Examples of states | Evidence needed to advance |
|---|---|---|
| Research coverage | untouched → discovery → exact passage inspected → necessary alternatives checked | Read log with source/version/section and unresolved sources |
| Explanation sufficiency | outline → mechanism draft → normal/failure/recovery and assumptions addressed | Question answered under explicit boundaries |
| Claim support | uncited hypothesis → source-linked draft → checked exact support → independently reproduced (where applicable) | Claim-to-source ledger / reproducible test result; do not infer a benchmark |
| Mechanical validity | not run → configured tests passed / failed | CI or local run IDs and explicit missing validator classes |
| Semantic review | unreviewed → self-reviewed → independently reviewed | Named reviewer, time, version and findings |
| Freshness | unknown → checked against source revision → potentially stale → reverified | Change-impact scope and re-check date |

A page can be **mechanically valid but not evidence-reviewed**, or **evidence-linked without a current runtime experiment**. Do not collapse these dimensions into one `approved` field.

## Contradiction / gap handling

- If two admissible public sources disagree, report both with their precise scope/version before attempting to reconcile.
- If the conclusion requires unknown distribution/load/failure properties, give a bounded *measure first* task; do not present a guessed capacity threshold.
- If a cited source is paid, unavailable or outside allowed use, retain a bibliographic reference only and locate an admitted independent public primary source for any material technical claim.
- If a dependency would require ingesting any restricted corpus, stop; Tycho stands alone and uses public evidence or original synthetic examples.
- If published source claims and a synthetic example appear incompatible, revisit assumptions before asserting a defect.

## Carrying one finding to other canonical owners

A related chapter gets a short link plus a concrete consequence, **not a copy** of the full explanation. Keep separate the owner for a distributed log (e.g. V04/C07), the owner for storage transactions (V05/C01) and the owner for safe rollout (V08/C04). Cross-links are proposals until all target pages exist. Later graph/index implementations derive relationships from canonical owners and metadata; they must not become a second hand-edited truth.

## First three contracts and stop condition

The first authoring wave is strictly three **bounded and evidenced** slices: (1) one mechanism, (2) one cross-component process, (3) one recovery scenario, proposed in [the structure plan](../book/PROPOSED-STRUCTURE.md) and formally scoped by #26. Do not turn this into a 10-volume generation run.

Stop a slice when its primary question can be answered with traceable assumptions, alternatives, source sections, failure limits and explicit unknowns, and its issue-specific checks pass. It may stop as **insufficient evidence** with a precise continuation. A first pilot is not license to assert all variants, engines or workload classes are covered.

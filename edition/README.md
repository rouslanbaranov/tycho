# Tycho — editorial decomposition candidate

Version: **2026.10.1-rc.1**. **#214 is OPEN.** The owner rejected the earlier uniform one-article-per-chapter assembly as sufficient final book structure. Version 2026.10.0 and its named snapshot remain a historical structural checkpoint.

## Read and inspect

Start at the [book contents](../book/README.md). All 69 chapters now separate an integrated decision/walkthrough from independently named mechanism and failure questions. The current chapter routes contain three to five pages, determined by their actual questions. There is no fixed page-count or word-count completion rule.

The candidate adds 174 question pages and retains the 69 integrated walkthrough identities, ten volume syntheses, earlier supporting material, 29 historical cases and six synthetic playbooks. The canonical corpus has 389 documents. Counts describe membership, not explanatory sufficiency.

[The individual chapter review](../authoring/CHAPTER_DECOMPOSITION_REVIEW_2026-10-20.md) and [explicit plan](decomposition-plan.json) record every question, its original source sections and the reason for a separate owner. Seven short treatments gained worked explanations. A new source-scoped MVCC/snapshot/vacuum page repairs an identified gap in the original PostgreSQL chapter.

## Identity and evidence migration

The [original path migration](migration.json) remains valid history. The [new decomposition manifest](decomposition-manifest.json) records 739 conserved source blocks, old and new owners, normalized payload digests and 839 fragment routes. All 215 identities from the structural checkpoint remain; 174 new question entities have separately minted IDs.

The original 69 page IDs still resolve to their integrated question, original scenario and transfer limits. They are not silently reassigned to a different mechanism. Chapter READMEs introduce and synthesize the question route and own the original shared evidence rows. Detail pages retain inline citations and explicit source-ledger links. A shared source list is not proof that every listed source supports every page.

New question pages do not inherit independent approval or fabricated inspection dates. Four specifically inspected public source entries support the newly written WAL, inbox, incident-practice and MVCC treatments; their exact text-inspection scope and non-execution limits are recorded in the source register and chapter review. The attempted JEP 444 direct fetch was blocked; no fresh read is asserted for that attempt.

## Reproduce and verify

The one-time `scripts/decompose_chapters.py` tool defaults to dry-run and requires deliberate `--apply`. Start from the structural checkpoint commit recorded in the plan, supply the reviewed plan and script, and apply the explicit source admissions. Reapplying to an already decomposed tree is refused. No source acquisition or automatic acceptance occurs during an index build.

From the repository root:

```bash
python3 scripts/source_catalog.py --check
python3 scripts/route_index.py build
python3 scripts/route_index.py check
python3 scripts/validate_decomposition.py
python3 scripts/validate_edition.py
python3 scripts/premerge_check.py --branch feature/TYCHO-214-assemble-and-release-the-complete-ten-volume-tycho-book --issue-title '[E14-14] Assemble and release the complete ten-volume Tycho book'
python3 scripts/validate_knowledge.py --mode strict --json
python3 scripts/validate_m9_cases.py
python3 scripts/validate_m9_cases.py --self-test
python3 -m unittest discover -s tests -p 'test_m9*.py' -v
```

`validate_edition.py --write-inventory` deliberately updates the candidate inventory after real changes; ordinary checks never refresh it silently. The inventory freezes book/source/schema/index/mapping membership for a specific candidate. It does not assert final editorial acceptance.

Use the existing locked Mermaid package with `tools/mermaid/check.mjs` for syntax parsing. Browser rendering and live MCP remain owner-cancelled, not passed. The milestone-only CI policy is unchanged. Prior technology-execution and broad M9 review waivers remain in force.

## Remaining substantive gate

The source manuscript retains #213 acceptance. The newly independent pages still need final reading acceptance for local definitions, adequate examples, failure reasoning, exact evidence support and boundaries between owners. Follow concrete findings into bounded writing/source work; do not promote pages based on their existence or length. New syntheses are self-checked candidates, not invented independent certification.

Final publication, retrieval/MCP and deployment must not be inferred from this larger inventory or a passing validator. The old release snapshot is not rewritten; corrective work uses a new candidate and an explicit Git history.

# Tycho — content enrichment candidate

Version: **2026.10.1-rc.3**. **#214 is OPEN.** This candidate extends the individually decomposed rc.1 corpus with two new critical-topic chapters and controlled enrichment. It is not a final release. The historical 2026.10.0 snapshot remains unchanged.

## Read the candidate

Start at [book contents](../book/README.md). The candidate contains ten volumes, **71 chapters and 406 canonical documents**: all 389 rc.1 documents plus two chapter landings and fifteen technical pages across both enrichment passes. Twelve existing mechanism owners are deepened, with routes added to eleven existing chapter introductions.

New chapters:
- [V05/C08 — Object storage](../book/volumes/v05/c08/README.md): resumable transfer/integrity, cross-store publication, access/version/lifecycle.
- [V08/C08 — Network request paths](../book/volumes/v08/c08/README.md): DNS/discovery and balancing, HTTP/2 and connection draining, hop trust/gateways, edge cache/origin protection.

[The scope contracts](../authoring/ENRICHMENT_SCOPE_2026-10-20.md) map every approved gap to its owner and acceptance question. No fixed word or page count establishes completion.

## Second-pass additions

The [second-pass contract](../authoring/SECOND_ENRICHMENT_CONTRACT_2026-10-20.md) adds five independently scoped pages inside existing chapters and three worked architecture projects inside V10/C07. Read the [new routes from book contents](../book/README.md#content-enrichment-candidate--2026101-rc3). Existing chapter count remains 71; all 398 rc.2 document identities remain.

Each project explicitly chooses authority and state paths, rejects alternatives, works through interruptions and recovery, calculates capacity/cost from invented inputs, and states when the recommendation should change. The verification page includes a hand-derived counterexample and proposed oracles; no model checker or implementation harness was executed.

## Preservation, source evidence and identities

The [original path migration](migration.json) and [69-manuscript decomposition](decomposition-manifest.json) remain unchanged history. The original 739 source blocks and all earlier IDs remain. The [enrichment manifest](enrichment-manifest.json) registers seventeen new IDs and exact insertion hashes for twelve existing pages. Removing only each new insertion recovers that page byte for byte at the recorded baseline.

[Selected inspection records](../sources/enrichment-inspections-2026-10-20.json) identify 35 scoped public primary-source readings, versions, actual read scope and execution limitations. The first pass newly admitted twenty-two sources and reused three existing IDs; the second newly admits nine and reuses one. Source membership is 247. Each technical addition has its own source/synthetic/unknown boundary. Original frontmatter and review history of deepened pages are preserved; fresh section-level reading is recorded separately.

All new pages are author self-reviewed. No independent acceptance, benchmark, deployed behavior or full documentation-tree inspection is claimed.

## Reproduction and validation

The earlier assembly and decomposition scripts remain one-time historical migrations. They do not automatically produce or authorize the new authored content. The new manifest and `scripts/validate_enrichment.py` explicitly validate this extension without replacing the earlier conservation checks. Indexes remain derived from frontmatter, and source catalogue membership from the canonical register.

The initial candidate index and inventory were reconciled in JavaScript. The execution environment has now recovered: [actual pinned Python/Mermaid validation](../authoring/PYTHON_MERMAID_VALIDATION_2026-10-20.md) passed 16/16 groups, 233/233 tests with zero skips, and 221/221 syntax parses. Python index generation reproduced the candidate byte for byte. Archived commands, versions and logs distinguish this executed pass from the earlier authoring-time record.

**The following required Python commands now passed on the pinned rc.3 snapshot; use them to reproduce the checks:**

```bash
python3 scripts/check_boundary.py
python3 scripts/validate_sources.py
python3 scripts/source_catalog.py --check
python3 scripts/route_index.py build
python3 scripts/route_index.py check
python3 scripts/validate_decomposition.py
python3 scripts/validate_enrichment.py
python3 scripts/validate_edition.py
python3 scripts/premerge_check.py --branch feature/TYCHO-214-assemble-and-release-the-complete-ten-volume-tycho-book --issue-title '[E14-14] Assemble and release the complete ten-volume Tycho book'
python3 scripts/validate_knowledge.py --mode strict --json
python3 scripts/validate_m9_cases.py
python3 scripts/validate_m9_cases.py --self-test
python3 -m unittest discover -s tests -p 'test_m9*.py' -v
```

The existing Mermaid syntax checker also passed for the full candidate. Reproduce it with:

```bash
npm ci --prefix tools/mermaid
node tools/mermaid/check.mjs --root .
```
 Browser rendering and live MCP remain owner-cancelled. Technology-example execution and broader M9 waivers remain as documented. No push/PR Actions or milestone closure is introduced.

A deliberate `validate_edition.py --write-inventory` may refresh the inventory only after reviewing actual drift; do not overwrite failures to manufacture a passing check. Python regeneration must match the candidate's derived index and inventory. Differences require investigation.

## Remaining acceptance

Python premerge, strict metadata/edition/conservation validation, the new adversarial tests and Mermaid parsing passed on the exact snapshot in the executed report. The PR stays **draft** for substantive acceptance. Prior rc.1 results retain their historical scope.

After integration checks, substantive page-level reading must assess explanatory sufficiency, scope, exact support, failure recovery and cross-owner coherence. Keep #214 open until that gate is met. Final publication, retrieval/MCP and deployment do not follow from new files or mechanically passing checks.

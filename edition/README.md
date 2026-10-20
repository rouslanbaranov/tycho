# Tycho — content enrichment candidate

Version: **2026.10.1-rc.2**. **#214 is OPEN.** This candidate extends the individually decomposed rc.1 corpus with two new critical-topic chapters and controlled enrichment. It is not a final release. The historical 2026.10.0 snapshot remains unchanged.

## Read the candidate

Start at [book contents](../book/README.md). The candidate contains ten volumes, **71 chapters and 398 canonical documents**: all 389 earlier documents plus two chapter landings and seven technical pages. Twelve existing mechanism owners are deepened, with routes added to eleven existing chapter introductions.

New chapters:
- [V05/C08 — Object storage](../book/volumes/v05/c08/README.md): resumable transfer/integrity, cross-store publication, access/version/lifecycle.
- [V08/C08 — Network request paths](../book/volumes/v08/c08/README.md): DNS/discovery and balancing, HTTP/2 and connection draining, hop trust/gateways, edge cache/origin protection.

[The scope contracts](../authoring/ENRICHMENT_SCOPE_2026-10-20.md) map every approved gap to its owner and acceptance question. No fixed word or page count establishes completion.

## Preservation, source evidence and identities

The [original path migration](migration.json) and [69-manuscript decomposition](decomposition-manifest.json) remain unchanged history. The original 739 source blocks and all earlier IDs remain. The [enrichment manifest](enrichment-manifest.json) registers nine new IDs and exact insertion hashes for twelve existing pages. Removing only each new insertion recovers that page byte for byte at the recorded baseline.

[Selected inspection records](../sources/enrichment-inspections-2026-10-20.json) identify 25 public primary documents, versions, actual read scope and execution limitations. Twenty-two sources are newly admitted and three existing IDs reused. Each technical addition has its own source/synthetic/unknown boundary. Original frontmatter and review history of deepened pages are preserved; fresh section-level reading is recorded separately.

All new pages are author self-reviewed. No independent acceptance, benchmark, deployed behavior or full documentation-tree inspection is claimed.

## Reproduction and validation

The earlier assembly and decomposition scripts remain one-time historical migrations. They do not automatically produce or authorize the new authored content. The new manifest and `scripts/validate_enrichment.py` explicitly validate this extension without replacing the earlier conservation checks. Indexes remain derived from frontmatter, and source catalogue membership from the canonical register.

The candidate index and inventory were reconciled in the available in-process JavaScript runtime. Baseline digest/serialization checks and the exact available results are recorded in [the validation report](../authoring/ENRICHMENT_VALIDATION_2026-10-20.md). This is not a Python validation run.

**The execution environment is unavailable. The following required commands have NOT run on rc.2:**

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

Before merging, run the existing Mermaid syntax checker for the full candidate as well. Browser rendering and live MCP remain owner-cancelled. Technology-example execution and broader M9 waivers remain as documented. No push/PR Actions or milestone closure is introduced.

A deliberate `validate_edition.py --write-inventory` may refresh the inventory only after reviewing actual drift; do not overwrite failures to manufacture a passing check. Python regeneration must match the candidate's derived index and inventory. Differences require investigation.

## Remaining acceptance

The PR stays **draft** while Python premerge, strict metadata/edition/conservation validation, the new adversarial tests and Mermaid parsing remain unexecuted. Prior rc.1 results belong to its exact tree.

After integration checks, substantive page-level reading must assess explanatory sufficiency, scope, exact support, failure recovery and cross-owner coherence. Keep #214 open until that gate is met. Final publication, retrieval/MCP and deployment do not follow from new files or mechanically passing checks.

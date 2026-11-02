# M9 E16-08 — GitHub-backed structural QA checkpoint

**Date:** 2026-10-19  
**Snapshot:** repository `rouslanbaranov/tycho`, default branch `main`; observed recursive Git tree commit `7c9c97d8fe8293d691f0ef3978c119c6d43724d3` (`truncated=false`).  
**Execution:** repository content examined through the connected GitHub integration; **not** a clone, Python execution, production index/MCP benchmark, publisher data replay, or independent architecture review. No new GitHub Actions workflow was triggered.

## Checks actually executed

| QA gate | Method | Observed result | Verdict |
|---|---|---|---|
| Book case list | Read `book/cases/README.md`; fetch all linked case Markdown pages from `main` in independent batches | **29/29** case pages fetched, each with a stable `case.<company>.<slug>` identifier | **PASS — presence** |
| Decision playbooks | Read and fetch six `book/cases/decisions/*.md` index links | **6/6** decision pages fetched; each contains a decision identifier and links to contrasting primary case narratives | **PASS — presence** |
| Mermaid fences | Count ` ```mermaid ` openings and all ` ``` ` delimiters in each case and decision page | All **35/35** documents contain ≥1 Mermaid block with an even fence count | **PASS — text shape only**; no Mermaid render/parser execution |
| Relative Markdown links | For 29 cases and 6 decision documents, normalize each relative target from its source directory, resolving `..` and removing anchors; compare with **215** GitHub tree blob paths | **45 local links inspected; 0 missing target files** (16 case-to-file, 29 decision-to-file) | **PASS — target file existence**; anchor correctness not separately checked |
| Source identity | Parse 43 candidate IDs from first-party register `sources/REAL_WORLD_ARCHITECTURE_CASES.md` | **43 unique registered source IDs** | **PASS — ID registry** |
| Query fixture shape | Parse `tests/fixtures/m9-case-queries.json`; check IDs and expected outcomes | **60 unique queries**: **21 answerable**, **26 reject_false_claim**, **13 insufficient_evidence** | **PASS — fixture consistency only** |
| Fixture → source refs | Cross-check each `required_source_ids` against the registered IDs | **0 unregistered source IDs** | **PASS — static references** |
| Portable schema and samples | Parse Draft 2020-12 proposal schema and two example records; check explicit required keys, claim IDs' prefix, local source refs | **2 sample records**, all displayed required keys present, claim IDs case-scoped | **PASS — static subset**; no `jsonschema` engine run |
| Python syntax, full offline validation | Direct Git clone/fetch failed in execution container because the host was unresolvable; repository only accessible via GitHub connection | `scripts/validate_m9_cases.py` inspected but **not executed against a checkout** | **NOT RUN** |
| Source semantic fidelity, license and permissions | Primary links/date/sections documented in source-admission waves, but no qualified external auditor signed off on each numeric claim, reuse right or domain alternative | No independent reviewer recorded for all 29 draft cases | **OPEN / REQUIRES INDEPENDENT REVIEW** |
| Live retrieval | No stable owned K18–K23 indexing/MCP target established in this QA run | 60 prompts are **test definitions**, not 60 live search results | **NOT RUN** |

## Audit boundaries and failures a passing static check cannot catch

1. A link pointing to an existing file may have a wrong **heading anchor** or inaccurate historical attribution. File existence is not citation truth.
2. A Mermaid fence can be balanced yet contain malformed graph syntax; no Mermaid renderer was executed.
3. An example record with all required fields may violate hidden JSON Schema conditions if a true Draft 2020-12 engine is not run. Static checks are a partial fallback.
4. Source publishers' company-reported metrics are **not** independently reproduced measurements. Never turn a bounded 2023 or 2026 blog report into a fleetwide present-day architecture guarantee.
5. Full acceptance #121 requires independent human or equivalently independent qualified technical review, source/claim/date/negative evidence verdicts, reproduction or explicit limitation of numerical claims, and actual tests under the owning knowledge-platform contracts where available.
6. The codebase is private, and no private restricted-origin data was copied into the public-source-only Tycho case content. Relative links and fixtures refer to the intended `tycho-public` collection.
7. This snapshot is no guarantee against changes made by other GitHub workers after the observed commit. Re-run the local validation script on the eventual integration revision.

## Reproduce when a checkout is available

From a clean checkout of the referenced revision, with Python 3, run:

```bash
python3 scripts/validate_m9_cases.py --self-test
python3 scripts/validate_m9_cases.py
```

For complete JSON Schema Draft 2020-12+FormatChecker validation, ensure `jsonschema` is installed in that environment and confirm that the second command's `schema_check` is **`jsonschema Draft2020-12+FormatChecker`**, not merely the portable strict subset. Capture command output, Python/jsonschema version, SHA and exit code in a new evidence record before claiming the test executed.

For retrieval: once K18–K23 services are actually deployed, invoke all 60 fixtures, recording which case IDs and primary-source sections were returned, false-company-claim rejection, temporal qualification, cost/latency and retrieval tool versions. A model-produced answer without evidence is not a passing result.

**Checkpoint conclusion:** static corpus and reference integrity checks passed as stated; source semantics, independent case review and live MCP remain outstanding. **Do not close #121 or M9 on this evidence alone.**

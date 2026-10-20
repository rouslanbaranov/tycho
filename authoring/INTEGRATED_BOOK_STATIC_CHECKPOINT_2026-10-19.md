# Integrated M1–M9 book — pinned Git-tree static QA checkpoint

> **Archived pinned static QA:** The old restrictions to keep #216 draft and #121 open applied only at the original 2026-10-19 SHA; they are now superseded by owner disposition and actual GitHub merge/closure. This file's original measured counts and limitations are preserved. **Live state (2026-10-20, before merging PR #218):** M1–M9 integrated draft merged via PR #216; PR #217 closed/unmerged and replaced by open/non-draft **unmerged PR #218**. M9 #121 closed under scoped owner acceptance; #213/E14 and final edition #214 remain open. **69/69 primary chapter manuscripts deepened, 0/69 independently accepted for final-book completeness.** The 10-volume edition, hosted MCP and deployment do not exist. Reported 13/13 groups and 215/215 tests passed on prior manuscript SHA `d8d04e0e3c97e9f364607f640faa9f5aee4866f3`, **not** on the subsequently edited status documents. Visual rendering and live MCP were owner-cancelled, not PASSED. See [canonical current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).


**Run date:** 2026-10-19  
**Pinned source revision:** \`ff88fe334050c6e429941cb514bdd02150fa6be2\` on integration branch \`integration/tycho-m1-m9-unified-manuscript-20261019\`.  
**Method:** GitHub connector fetched the recursive Git tree and **each** book Markdown file (in nine bounded batches) and evaluated the scoped lexical invariants below in a small JavaScript inspection script. This is **not** execution of the repository's Python validators and is not a release/copyright/technical acceptance certificate.

## Whole-book file and local link target verification

| Check | Executed scope / result | Meaning and limitation |
|---|---|---|
| Integrated Git tree | Tree contains 311 blobs, not truncated | Whole tracked-file path inventory at this revision; does not imply a successful checkout |
| Book Markdown inventory | **136/136 \`book/**/*.md\` files fetched individually** at this revision | Includes foundational material, topic indexes, M9 casebook and six playbooks |
| Markdown links scanned | **1,623** Markdown link occurrences encountered across the 136 pages | Includes external URLs; regex-based lexical scan, not CommonMark parsing |
| Local file target existence | **No missing referenced local file paths detected** | Local paths resolved relative to the referencing Markdown file against the Git tree; **anchor fragments were not resolved**, nor external URLs or parenthesized edge cases |
| H1 heading pattern | Exactly one \`# \` heading found in each of 136 pages | Does not validate hierarchy, semantic titles or completeness |
| Fenced-code marker pairs | No odd number of triple-backtick fence delimiter lines among the 136 pages | Not a full parser, no syntax lint or Mermaid render |
| M9 case H2 duplicate check | Independently recorded **35/35 pages** without repeated exact level-2 headings in the earlier integrated snapshot | Separate rule from current whole-book H1/links scan; not proof against semantic duplication |

### Per-batch reproducibility counters

These bounded GitHub reads used the sorted path list of all 136 files. The links column counts **all** discovered Markdown links (not only local links).

| Path slice (zero-based) | Files | Markdown link occurrences | Missing local file targets | H1 anomalies | Odd backtick-fence counts |
|---|---:|---:|---:|---:|---:|
| 0–14 | 15 | 257 | 0 | 0 | 0 |
| 15–29 | 15 | 149 | 0 | 0 | 0 |
| 30–44 | 15 | 70 | 0 | 0 | 0 |
| 45–59 | 15 | 133 | 0 | 0 | 0 |
| 60–74 | 15 | 283 | 0 | 0 | 0 |
| 75–89 | 15 | 171 | 0 | 0 | 0 |
| 90–104 | 15 | 190 | 0 | 0 | 0 |
| 105–119 | 15 | 222 | 0 | 0 | 0 |
| 120–135 | 16 | 148 | 0 | 0 | 0 |
| **Total** | **136** | **1,623** | **0** | **0** | **0** |

## Integrated constraints kept open

1. **No local full checkout.** Attempting \`git ls-remote\` from the available container failed name resolution for \`github.com\`, and an archive retrieval could not be established. The repository's \`scripts/premerge_check.py\`, \`scripts/check_boundary.py\`, \`scripts/validate_book_navigation.py\`, \`scripts/validate_m9_cases.py\`, \`scripts/validate_metadata_schemas.py\` and unit tests **have not been executed against this pinned revision**. Their presence or a ported lexical check is not a Python PASS.
2. **No complete Markdown anchor/heading resolution:** a referenced file might exist but a \`#section\` link could be invalid. Run the actual navigation script on a full checkout, including percent-decoded anchors and fenced-content exclusion, and retain exact output.
3. **No external source URL bulk validation or claim admission:** first-party sources are individually evaluated under provenance review; URL accessibility or a working link alone is not evidence of technical truth or reproduction permission.
4. **No runtime/experiment/diagram render:** Markdown fence pairing does not prove a Mermaid drawing renders, nor that any source/benchmark/protocol behavior is correctly represented.
5. **No full 60-scenario MCP evaluation:** there is no verified end-to-end graph-free MCP service for M9 in this checkpoint, and no formally approved dependency waiver.
6. **No independent accepted chapter or case:** \`authoring/CHAPTER_EDITORIAL_ACCEPTANCE_LEDGER.md\` and \`authoring/cases/M9_REVIEW_ACCEPTANCE_MATRIX.md\` remain the authoritative separate review registers.

## Separate integration runner added after pinned Git-tree scan

The existing `scripts/premerge_check.py` invokes `scripts/check_feature_branch.py`, which validates only executable sub-issue branches shaped like `feature/TYCHO-<issue-number>-<issue-title-slug>`. Our already approved integration branch is intentionally not one of those issue branches. **Do not weaken or skip that existing governance rule.**

A new **opt-in** [`scripts/premerge_integration_check.py`](../scripts/premerge_integration_check.py) therefore targets exactly `integration/tycho-m1-m9-unified-manuscript-20261019` and requires an explicit full 40-character `--expected-head` commit SHA, an identical local Git `HEAD`, correct attached branch (or a detached pinned checkout), and a clean worktree. It invokes existing boundary, source-inventory, source catalogue, claim-ref, JSON-Schema-example, book navigation, M9 case/main-and-self-test and both core/M9 unittest discovery suites. [Separate offline unit tests](../tests/test_tycho_integration_premerge.py) cover branch, SHA and command-list restrictions.

Once a **complete clone is accessible**, run from the checkout root, **replacing the placeholder with the latest full integration commit SHA**:

```sh
python3 -m pip install -r requirements-validation.txt
python3 scripts/premerge_integration_check.py \
  --branch integration/tycho-m1-m9-unified-manuscript-20261019 \
  --expected-head <FULL_PINNED_40_CHARACTER_SHA>
```

**These commands were not run in the GitHub-only integration environment.** No output/log, successful suite execution, local metadata validation, acceptance signal or milestone-closure decision is claimed by creating the runner and unit tests. The runner also cannot evaluate live MCP quality or independent rights/technical claims. It does not change the milestone-only GitHub Actions policy.

## Focused historical-claim correction found in further review

A source comparison of Shopify's 2019 and 2020 first-party reports found that the early [modular-monolith case](../book/cases/shopify-modular-monolith.md) had an **overstrong introductory shorthand** implying completed enforced component boundaries as of 2019. The original 2019 publication expressly describes enforcement as unfinished; in September 2020 only about one third of 37 main components used Packwerk restrictions. This was corrected in the integrated branch **after** the pinned structural snapshot. See the [12-claim Shopify source-check register](cases/M9_SHOPIFY_SOURCE_SPOTCHECK_2026-10-19.md). None of these facts establishes the 2026 company architecture or independent M9 acceptance.

**Publication/merge policy:** keep [PR #216](https://github.com/rouslanbaranov/tycho/pull/216) Draft, [#213](https://github.com/rouslanbaranov/tycho/issues/213) and [#121](https://github.com/rouslanbaranov/tycho/issues/121) OPEN, and release only through [#214](https://github.com/rouslanbaranov/tycho/issues/214) after evidence-based acceptance. No manually curated Tycho graph infrastructure or graph-specific delivery gate should be added.

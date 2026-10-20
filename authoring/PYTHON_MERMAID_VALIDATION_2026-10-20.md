# Executed Python and Mermaid validation — 2026-10-20

Refs #214. Draft [PR #222](https://github.com/rouslanbaranov/tycho/pull/222). Candidate **2026.10.1-rc.3**.

## Result and exact scope

The execution environment is available again. The actual repository Python checks completed successfully: **16/16 groups, 233/233 tests, zero skips**. The repository Mermaid checker parsed **221/221 diagrams** successfully with Mermaid 11.17.2 and jsdom 30.1.3. The full test suite includes the five enrichment adversarial tests. Feature premerge separately passed its required subset; those repeated tests are not added to the 233-test total.

The clean checked snapshot is commit `f11196b11f405851f52c3006b06d7ede0f6c8dcd`, tree `addb99d9062bae0c8e5f39187e0f3623770f03e3`. All 636 tracked blobs and the complete Git tree matched GitHub before checks; the exact original commit object was reconstructed and verified by its SHA. The earlier dirty checkout was not modified.

Python 3.12.14 used an isolated environment with PyYAML 6.0.3 and jsonschema 4.26.0. The cached Mermaid runtime had the required package versions, and its checker was byte-identical to the repository checker. It was run against the pinned snapshot using `--root` and produced the archived parser report. Browser rendering was not run.

## Actual checks

| Group | Result |
| --- | --- |
| Configured boundary and independent-origin status review | PASS; scanner is not proof of independent origin |
| Source structure and catalogue freshness | PASS; 247 source records |
| Claim references | PASS |
| Strict schema examples | PASS |
| Book metadata | PASS; 406 documents |
| Strict knowledge integration | PASS; no hosted-service acceptance implied |
| Book navigation | PASS |
| Routing index | PASS; 406 documents, complete coverage |
| Historical decomposition | PASS; 739 source blocks and 839 fragment routes retained |
| Enrichment | PASS; 17 registered additions, two new chapters, twelve deepened pages |
| Edition/inventory | PASS; ten volumes, 71 chapters, 406 documents, 447 inventory files |
| M9 validation and built-in negative self-tests | PASS; no broader source re-audit implied |
| Full `test_*.py` discovery | PASS; 233 tests, zero failures/errors/skips |
| Issue-specific feature premerge | PASS |
| Mermaid syntax | PASS; 221 diagrams |

The table groups the two source commands and the two M9 commands for readability. [Machine-readable results and exact commands](validation/2026-10-20-rc3/results.json), [full unittest log](validation/2026-10-20-rc3/all-tests.log), [premerge log](validation/2026-10-20-rc3/feature-premerge.log), and [all Mermaid parser rows](validation/2026-10-20-rc3/mermaid.json) retain the execution evidence. The other group logs are stored beside them.

After the read-only checks passed, `scripts/route_index.py build` reproduced the committed index **byte for byte**, with file SHA-256 `0cf9bd356bb0ebff9134f0315caf5ae0fbf398706e7815dc1023376a927e1a7c`. No corpus, metadata, source or diagram defect needed repair. No inventory was overwritten to hide drift.

The documentation follow-up updates only validation status, links to this evidence, and the derived index/inventory for the book landing's status text. The technical pages, source records, original metadata, historical source blocks and diagrams are unchanged. Final checks on that follow-up are recorded in the PR with its exact tree to avoid a self-referential report hash.

## Remaining gate

This report supersedes the environment-blocked status in earlier enrichment records for the checked snapshot. It establishes local integrity and syntax results, not independent substantive acceptance, a benchmark, a technology example execution, a hosted service or a release. PR #222 stays draft and #214 stays open for substantive page acceptance. #213, existing owner waivers/cancelled browser and live-MCP gates, and milestone-only CI remain unchanged. No merge or milestone closure is performed.

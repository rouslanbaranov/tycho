# Pre-merge status reconciliation — 2026-10-20

**Scope:** PR #218 / issue #213; premerge documentation only. No merging, issue or milestone closure, final publication, added source truth, production proof or chapter acceptance.

**Live status:** PR #216 integrated M1–M9 draft into main (`e2267a87882bb9935b2451368aa75a6fd05f87c1`); PR #217 closed/unmerged; PR #218 open/non-draft/unmerged; #213 and E14 #15 reopened and open; #214 open; M9 #121 closed under earlier owner-approved *integrated-draft* acceptance. **69/69 canonical primary manuscripts deepened; 0/69 independently content-accepted final chapters.** M9 29 historical cases + six synthetic playbooks remain bounded applied material. No 10-volume physical edition or hosted service.

## Which document controls what?

| Sources | Status |
|---|---|
| [STATE.md](STATE.md), [ROADMAP.md](ROADMAP.md), [root README](../README.md), [book landing](../book/README.md) | Updated **current** project state, priority, and reading entry |
| [BOOK_COMPLETION_EXECUTION_REGISTER_2026-10-20.md](BOOK_COMPLETION_EXECUTION_REGISTER_2026-10-20.md), [CHAPTER_EDITORIAL_ACCEPTANCE_LEDGER.md](CHAPTER_EDITORIAL_ACCEPTANCE_LEDGER.md), [EDITORIAL_SEMANTIC_ACCEPTANCE_REVIEW_2026-10-20.md](EDITORIAL_SEMANTIC_ACCEPTANCE_REVIEW_2026-10-20.md) | Real per-chapter gaps/technical/source gates; 69 deepened is not 69 accepted |
| [ACCEPTANCE_DISPOSITION_2026-10-20.md](ACCEPTANCE_DISPOSITION_2026-10-20.md), [UNIFIED_BOOK_M1_M9_INTEGRATION.md](UNIFIED_BOOK_M1_M9_INTEGRATION.md), [INTEGRATED_BOOK_STATIC_CHECKPOINT_2026-10-19.md](INTEGRATED_BOOK_STATIC_CHECKPOINT_2026-10-19.md) | Original historical merge/acceptance/validation scopes retained; newer overlay supersedes obsolete active-state statements |
| [BOOK_COMPLETENESS_AUDIT.md](BOOK_COMPLETENESS_AUDIT.md), [FINAL_TOC_AND_OWNER_BOUNDARIES_2026-10-20.md](FINAL_TOC_AND_OWNER_BOUNDARIES_2026-10-20.md) | Topic coverage and selected target TOC, not release completion |
| [ROUTING-INDEX.md](ROUTING-INDEX.md), [knowledge platform plan](knowledge-platform-and-mcp-plan.md), [GITHUB-DELIVERY-MAP.md](GITHUB-DELIVERY-MAP.md) | Historic design checkpoints vs implemented 136-doc index and current GitHub hierarchy |
| [M9 review matrix](cases/M9_REVIEW_ACCEPTANCE_MATRIX.md), [M9 program](REAL_WORLD_CASE_STUDY_PROGRAM.md), [M9 ID cleanup](M9_EVIDENCE_ID_CLEANUP.md) | Original case review and migration events, narrower owner decision, no curated graph |
| [Sources README](../sources/README.md), [coverage map](../sources/COVERAGE.md) | Discovery/source admission meaning, **not** final-book source-claim acceptance |

**Tests:** PR #218 reports 13/13 groups, 215/215 unit tests (194 general + 21 M9), on pinned original manuscript `d8d04e0e3c97e9f364607f640faa9f5aee4866f3`. Routing index 136/136 complete with original snapshot `fcfd4992a6a72f15beb75163d8e63d8ce432d7ce534af7f301cd94fc0626cd1a`. These remain historical execution evidence only. The book landing will be revised along with the derived routing-index checksum; execute full Python/index/premerge verification on **latest** PR HEAD before merging. Visual rendering and live MCP explicitly cancelled (not PASSED); no Actions run implied.

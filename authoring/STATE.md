# Current state — Tycho

**Updated:** 2026-10-20, after manuscript acceptance and merge. See [status reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md) and [roadmap](ROADMAP.md).

## Accepted manuscript baseline

The owner confirmed independent substantive/content acceptance of all **69 primary chapter manuscripts** at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. [PR #218](https://github.com/rouslanbaranov/tycho/pull/218) merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`. This supersedes the earlier 0/69 and pending-acceptance status.

The corpus includes 29 public historical case studies and six synthetic decision playbooks; all 35 have contextual transfers into 26 primary chapters. M9 #121 retains its earlier scoped acceptance and owner dispositions.

## Current GitHub state

| Object | Status |
|---|---|
| PR #216 | Merged; earlier M1–M9 integrated-draft baseline |
| PR #217 | Closed, unmerged; replaced by #218 |
| PR #218 | Merged; accepted manuscript baseline |
| #213 and E14 #15 | Completed; original children #79–#90 checked closed |
| #214 | Reopened; substantive page decomposition and editorial acceptance |
| M9 #121 | Closed under its documented scoped acceptance |

## Reopened editorial decomposition — #214

The owner rejected the uniform one-manuscript-page-per-chapter assembly as sufficient final book structure and reopened #214. PR #220/version 2026.10.0 remain a **structural checkpoint**, not final editorial acceptance. #213's accepted content baseline remains valid.

The current 2026.10.1-rc.1 candidate makes individual question-owner decisions for all 69 chapters: **174 new question pages**, 69 integrated walkthroughs and ten volume syntheses, with 389 canonical documents including retained supporting material. A page count is an inventory, not a completion criterion.

[The chapter review](CHAPTER_DECOMPOSITION_REVIEW_2026-10-20.md) records actual owner questions, source sections and editorial limits. [The split manifest](../edition/decomposition-manifest.json) conserves 739 source blocks and maps 839 original fragments. Original IDs and protected evidence metadata remain; new question IDs are recorded separately. Source text, ledger ownership, original examples and new additions have explicit provenance.

Seven short question treatments gained worked decision/failure explanations. A separately sourced PostgreSQL 17 page fills the missing MVCC snapshot/version-lifetime explanation. Newly authored material is self-checked; no new independent acceptance or technology execution is claimed.

**Next gate:** read and accept the independent pages for explanatory sufficiency, context, examples, exact source support and cross-question boundaries; resolve concrete findings. #214 remains open until that substantive gate is completed. Tests and larger file counts alone must not close it. Retrieval/MCP/deployment remains postponed; curated graph infrastructure remains excluded.

## Acceptance and verification provenance

- The owner's content-acceptance declaration covers the 69 manuscripts at the accepted SHA. No reviewer identity, 69 signed review rows or independent certificate is invented.
- [The accepted-head verification report](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915) records an **owner-reported** clean run: **13/13 groups, 215/215 tests, zero skips**, fresh index 136/136. It belongs to `986b1ddbe985079b7c647182fcf1c2fc8911d96c`, not later status edits.
- Any indexed-page change requires deterministic index rebuild/check. New validation results belong to the exact checked tree and are recorded in the status-reconciliation PR.
- Visual rendering and live MCP remain cancelled, not passed. Broader M9 re-audit and further technology-example execution retain their owner-waived/cancelled dispositions.
- Milestone-only CI remains unchanged. No milestone closure, Actions execution, deployment or release is implied.

## Record precedence

Older audit, execution and editorial reports retain their original observations as dated history. Their pending statuses do not reopen the owner-accepted manuscript gate. Individual frontmatter review/proof fields remain as recorded; the aggregate owner disposition does not fabricate missing page-specific review identities. The edition assembly review records the new validation and its limits; GitHub records the publication merge and issue closure.

# Current state — Tycho

> **Current structural candidate — 2026.10.2-rc.1 (cut 2026-10-21):** 11
> volumes, 82 chapters and 423 canonical pages in the current tree. The book
> and edition landings still record the 419-page cut; the #228 deep-source
> splits added four pages after the cut. V11 is a self-checked Phase 6
> pattern-atlas candidate (#288); human review is recorded and owner acceptance
> remains open. The #214/rc.3 status below is historical.

**Owner-unit audit — 2026-10-21 (#286):** 144 carded entries now map to 118
section-level owner units on the same 65 registered pages: 96 partial-bounded,
48 partial, 0 name-only and 0 sufficient. Thirty shared pages are classified
14 keep, 13 deepen and 3 split; no page split was performed. This is
self-checked evidence, not independent review or owner acceptance. See
[the audit](PATTERN-OWNER-UNIT-AUDIT_2026-10-21.md).

**Semantic page audit — 2026-10-21 (#288):** 419/419 canonical pages have a
self-checked semantic disposition: 419 sound, 0 sound-with-findings, 0
needs-remediation and 0 blocked. No semantic finding remains. The V11 landing was
refreshed, the 40 non-catalog related
labels are recorded as non-routes, three catalog-index reads are intentionally
unused, and three split decisions are deferred. The independent review agent
**Reviewer** returned ACCEPT-WITH-FINDINGS; its 17 findings and 7 re-review
residuals were addressed. Owner-confirmed human review passed on 2026-10-21; no
per-page reviewer record was supplied. No low findings remain; #292 is closed.
Owner acceptance remains open. See
[the semantic audit](PATTERN-SEMANTIC-AUDIT_2026-10-21.md),
[the agent review](INDEPENDENT-AGENT-REVIEW_2026-10-21.md) and
[the human review](HUMAN-REVIEW_2026-10-21.md).

**Deep-source expansion (#228):** started 2026-10-22; all 145 entries now have all four
evidence dimensions supported and are `partial-bounded` (0 technical partial, 0 sufficient).
The three deferred page splits were performed with stable IDs; the canonical corpus is 423
pages. The remaining semantic gate is owner acceptance; the remaining delivery gaps are
technical sufficiency, decision sufficiency and owner acceptance. See the
[deep-source plan](DEEP-SOURCE-EXPANSION-PLAN_2026-10-22.md).

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

**MCP local candidate — 2026-10-23 (#57):** a read-only stdio adapter,
30 offline tests and a one-off official SDK 2.3.0 smoke are recorded in merged
PR #359; two independent agent reviews and a focused delta review returned
ACCEPT-WITH-FINDINGS; corrections and residual limits are recorded. No hosted
endpoint, repository SDK pin, human review or live-service acceptance is
claimed. See
[the MVP record](MCP-READ-ONLY-MVP.md),
[the SDK smoke note](MCP-SDK-SMOKE_2026-10-23.md) and
[the independent agent review](INDEPENDENT-AGENT-REVIEW-MCP_2026-10-23.md).

**MCP local HTTP candidate — 2026-10-24 (#367):** the read-only stdio adapter
is wrapped by a bearer-authenticated local HTTP container with /mcp, /search,
/health, /ready and raw book routes. Four HTTP tests and a Docker/SDK smoke
exist; no GitHub, Vercel or hosted deployment, TLS, OAuth, rate limit, human
review or production acceptance is claimed. See
[the local container record](MCP-LOCAL-HTTP-CONTAINER.md).

## Readable directory layout — #214

The owner-requested physical migration covers all ten volumes and 71 chapters, with 339 moved documents and all 406 IDs retained. See [the directory map](../edition/directory-migration.json), [migration record](DIRECTORY_MIGRATION_2026-10-20.md) and [naming policy](DIRECTORY-NAMING.md). Original chapter/decomposition/enrichment manifests remain byte-identical. Their validators use an inverse path view so historical payload and provenance assertions remain active. #214 stays open; physical organization does not establish substantive acceptance.

## Current enrichment candidate — #214

Candidate **2026.10.1-rc.3** implements the owner's additional authorization: five mechanism pages (configuration rollout, session consistency, offline conflicts, cells/shuffle sharding, protocol verification) and three complete original worked projects (catalogue, offline collaboration, multitenant overload). Expected membership: **10 volumes, 71 chapters, 406 canonical documents**. The previous rc.2 additions and all 398 previous identities remain.

See [the second-pass contract](SECOND_ENRICHMENT_CONTRACT_2026-10-20.md), [current validation](SECOND_ENRICHMENT_VALIDATION_2026-10-20.md) and [conservation manifest](../edition/enrichment-manifest.json). Nine primary sources are newly admitted and one existing ID reused for ten scoped readings; total source membership is 247. All workload numbers are synthetic, and all new material is author self-checked.

**PR #222 is merged; #214 remains OPEN for substantive acceptance.** The execution environment recovered. [Actual Python and Mermaid validation](PYTHON_MERMAID_VALIDATION_2026-10-20.md) passed 16/16 groups, 233/233 tests with zero skips, and 221/221 diagram parses on the pinned rc.3 snapshot; Python index reproduction was byte-identical. The earlier execution block is resolved. No independent acceptance, final release or deployment is asserted.

The [first-pass scope](ENRICHMENT_SCOPE_2026-10-20.md) and [first-pass validation](ENRICHMENT_VALIDATION_2026-10-20.md) retain their historical rc.2 meaning. They are not a verification report for rc.3.

## Historical editorial decomposition candidate — #214

The owner rejected the uniform one-manuscript-page-per-chapter assembly as sufficient final book structure and reopened #214. PR #220/version 2026.10.0 remain a **structural checkpoint**, not final editorial acceptance. #213's accepted content baseline remains valid.

The preceding 2026.10.1-rc.1 candidate makes individual question-owner decisions for all 69 chapters: **174 new question pages**, 69 integrated walkthroughs and ten volume syntheses, with 389 canonical documents including retained supporting material. A page count is an inventory, not a completion criterion.

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

Older audit, execution and editorial reports retain their original observations as dated history. Their pending statuses do not reopen the owner-accepted manuscript gate. Individual frontmatter review/proof fields remain as recorded; the aggregate owner disposition does not fabricate missing page-specific review identities. The edition assembly review records the new validation and its limits; GitHub records candidate merges and the still-open #214 acceptance gate.

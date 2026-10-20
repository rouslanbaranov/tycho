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
| #214 | Edition implemented; publication PR and frozen-tree delivery control closure |
| M9 #121 | Closed under its documented scoped acceptance |

## First Markdown Edition — 2026.10.0

The physical **10-volume / 69-chapter / 69-primary-page** edition is assembled under #214, with **215 canonical documents** including retained supporting essays and casebook material. The [book contents](../book/README.md) govern the reading order. Each new volume contributes synthesis and each chapter provides a conclusion, counterexample and bounded route.

[Edition scope and limitations](../edition/README.md), [reversible migration](../edition/migration.json), [frozen inventory](../edition/inventory.json) and [assembly review](EDITION_ASSEMBLY_REVIEW_2026-10-20.md) document the exact publication boundary. All 136 earlier identities remain; 79 new landing identities are recorded. No original primary payload or external citation was discarded. The original 69 manuscript IDs and evidence metadata are preserved.

The release is a Markdown repository edition with immutable content hashes and a Git commit pin recorded in #214/release tracking. It does not claim a GitHub Release object, PDF/EPUB export or hosted service. #214 closes only after its publication PR is merged and the frozen tree is verified. The live GitHub issue state controls that transition.

**Next:** lexical/hybrid retrieval evaluation, MCP/onboarding, shared Rocinante runtime and deployment/operations are separate roadmap work. Curated knowledge-graph infrastructure remains excluded. Existing metadata, schema, provenance and local routing facilities must be reused rather than redesigned.

## Acceptance and verification provenance

- The owner's content-acceptance declaration covers the 69 manuscripts at the accepted SHA. No reviewer identity, 69 signed review rows or independent certificate is invented.
- [The accepted-head verification report](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915) records an **owner-reported** clean run: **13/13 groups, 215/215 tests, zero skips**, fresh index 136/136. It belongs to `986b1ddbe985079b7c647182fcf1c2fc8911d96c`, not later status edits.
- Any indexed-page change requires deterministic index rebuild/check. New validation results belong to the exact checked tree and are recorded in the status-reconciliation PR.
- Visual rendering and live MCP remain cancelled, not passed. Broader M9 re-audit and further technology-example execution retain their owner-waived/cancelled dispositions.
- Milestone-only CI remains unchanged. No milestone closure, Actions execution, deployment or release is implied.

## Record precedence

Older audit, execution and editorial reports retain their original observations as dated history. Their pending statuses do not reopen the owner-accepted manuscript gate. Individual frontmatter review/proof fields remain as recorded; the aggregate owner disposition does not fabricate missing page-specific review identities. The edition assembly review records the new validation and its limits; GitHub records the publication merge and issue closure.

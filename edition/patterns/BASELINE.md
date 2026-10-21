# Pattern catalog baseline — 2026-10-21

> Read-only starting point for issue #228 Phase 0. It records the tree and the
> observed corpus. It is not a coverage, source-reading, authoring or acceptance
> claim.

## Git baseline

| Field | Value |
|---|---|
| Branch point | `main` |
| HEAD | `873ad2893c7dde3f5b750b66b482cde210f4cce6` |
| Tree | `ec959a40a0eafaf0c3838dd6891d25508289ce3f` |
| Route-index snapshot | `99dc57d750af1875fe76123464edc802fc50878288b38adab33a57635d021154` |
| Inventory version | `2026.10.1-rc.3` |
| Inventory content snapshot | `4cd39330027ce842de198ba9056298381ebff154e35cdb1f8426256e72ab9e89` |
| Inventory files | 450 |

## Corpus census

| Kind | Count |
|---|---|
| Volumes | 10 |
| Chapters | 71 |
| Canonical documents | 407 |
| Pages | 304 |
| Landings | 15 |
| Decisions | 6 |
| Book root | 1 |
| Documents inside volumes | 340 |
| Documents outside volumes | 67 |

Scale indicators, not quality targets: 199 Mermaid fences, 2401 headings at
levels h2–h4 and 782 HTTP links across the canonical Markdown. Recompute these
values from the checked tree rather than copying them into a later claim.

## Source register

| Field | Count |
|---|---|
| Registered sources | 247 |
| `admitted-for-research` | 192 |
| `pending-content-access` | 45 |
| `bibliography-only` | 10 |
| `landing-or-abstract-inspected` | 202 |
| `fetch-incomplete` | 45 |
| `content_verified` | 0 |

The register is a discovery inventory, not proof of reading. Issue #225 holds a
separate research ledger; its SRE completion is not copied into this baseline.

## Related work

- Issue #214 is closed. The accepted manuscript and edition baseline remain
  historical evidence.
- Issue #225 is open and research-only. Do not modify its frozen baseline.
- Issue #227 is closed; its P1 and P2 content is already on `main`.
- Issue #19 owns the applicability-card model and template.
- V10/C03 owns the existing pattern-applicability material; no registry or
  page-level pattern audit existed at this baseline.

## Known state-document drift

`authoring/STATE.md`, `edition/README.md` and `authoring/ROADMAP.md` still
describe #214 as open and some counts as 406. The GitHub issue state and the
checked tree above take precedence. Reconcile those records in a separate
status change; do not use them as the baseline.

## Method and limits

Counts were read from `git`, `generated/route-index.v1.json`,
`edition/inventory.json` and the canonical frontmatter. The scan accepted both
YAML and JSON frontmatter blocks. No source was fetched, no page was edited and
no technical conclusion is drawn from a name match.

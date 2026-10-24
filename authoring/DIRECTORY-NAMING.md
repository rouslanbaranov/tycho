# Volume and chapter directory naming

Status: required for the directory layout selected by the owner on 2026-10-20, Refs #214. This document owns the naming rule and the acceptance conditions for migrating existing paths.

## Required layout

Book volume and chapter directories use **<number>-<description>**. Retain the existing type prefix and zero-padded two-digit ordinal, then append a readable English description:

| Directory | Pattern | Example |
| --- | --- | --- |
| Volume | `vNN-<description>` | `v01-requirements-and-architecture` |
| Chapter within its volume | `cNN-<description>` | `c01-problem-framing` |

A complete example path is `book/volumes/v01-requirements-and-architecture/c01-problem-framing/README.md`. The current [example chapter](../book/volumes/v01-requirements-and-architecture/c01-problem-framing/README.md) follows this layout.

The chapter ordinal is local to its parent volume. Preserve the existing reading order and numbering. Do not use bare `v01` or `c01` for new directories. The landing file remains `README.md`; descriptive technical page filenames remain below the chapter.

## Description rules

- Use a short, meaningful description derived from the volume or chapter's English title and scope. Prefer recognizable engineering terms over generic labels such as `content`, `misc` or `chapter`.
- Use lowercase ASCII letters and digits, with single hyphens between words. No spaces, underscores, punctuation, leading/trailing hyphens or repeated hyphens.
- Expand a meaningful symbol into a word where needed, or choose a shorter equivalent description. For example, use `ci-cd` and `cost-performance`; do not copy punctuation into a path.
- The volume shape is `^v(?:0[1-9]|[1-9][0-9])-[a-z0-9]+(?:-[a-z0-9]+)*$`; the chapter shape uses `c` instead of `v`. Descriptions must also pass editorial review: matching a regular expression does not make a name useful.
- Record the selected complete paths in the edition outline. Reuse them consistently; generators must consume the explicit outline rather than independently inventing competing abbreviations.
- A wording-only title edit does not require a directory rename. Any later path change uses the same explicit migration procedure.

Human-facing codes such as `V01/C01` can remain short. Persistent document IDs remain opaque and unchanged: neither the ordinal nor the description becomes document identity.

## Existing corpus and migration acceptance

All ten volumes and 71 chapters now use descriptive directories. The [explicit directory migration](../edition/directory-migration.json) records every directory and all 406 document identities, including 339 moved documents. [The migration record](DIRECTORY_MIGRATION_2026-10-20.md) describes conservation and validation. These paths are canonical; no duplicate canonical tree remains under the earlier numbered-only names.

Before declaring the directory migration complete:

1. Select readable names for all ten volumes and all 71 chapters from their current titles, and record a complete old-to-new path map. Every canonical document must have exactly one destination and retain its ID and parent identity.
2. Move the actual files and update relative links, navigation, edition outline, current canonical paths in frontmatter and identity records, and affected tooling/fixtures in the same change. Do not retain a second canonical copy under the old directory.
3. Preserve technical prose, source ownership, opaque identities, evidence and review history. Path-only edits do not establish new source inspection, content verification or substantive acceptance.
4. Keep the earlier migration/decomposition/enrichment records as historical evidence. Add explicit path-aware migration provenance so their conservation checks remain meaningful; do not overwrite baseline hashes merely to hide a failure.
5. Regenerate the routing index and edition inventory from the migrated canonical files. Verify complete membership, ID stability, numbering, path-map coverage, unique destinations, local files/anchors and unchanged source-block meaning.
6. Run the relevant Python premerge, schema, navigation, conservation and edition checks, applicable tests and Mermaid syntax parsing on the exact migrated tree. A requirements-only check cannot be reported as a completed migration.

`python3 scripts/validate_directory_migration.py` validates naming, complete path/identity membership, retired-path absence, protected historical manifests and reversible path-only content changes. The normal feature premerge and strict knowledge runners include this gate when the migration record is present; edition validation also applies it. #214 remains open for the remaining substantive edition acceptance.

## Authorized content revisions after migration

The directory, decomposition and enrichment manifests record immutable baselines.
A later content change must not silently rewrite those baselines. Record it in
[`edition/content-revisions.json`](../edition/content-revisions.json) with:

- the issue number and authorization date;
- the exact document path or source-block key;
- the previous and current SHA-256 values.

The validators accept a changed payload only when the overlay matches both hashes.
An unlisted change, or a further change to an already revised payload, still fails.
The original manifests remain byte-identical, so their historical protection is not
rewritten. The routing index and edition inventory are regenerated after the
authorized change.

### Pre-flight for a bounded change

`python3 scripts/book_change.py --plan` is a read-only pre-flight for a page
edit. It reports changed book pages, missing revision entries, stale derived
artifacts and the ordered rebuild/review steps; `--strict` exits non-zero while
anything blocking remains. It never writes, never authorizes a revision and
does not replace `premerge_check.py`, claim review or independent review.

Ownership stays with the existing contracts: identity and metadata in
[METADATA-IDENTITY-CONTRACT](METADATA-IDENTITY-CONTRACT.md), heading and
citation behavior in [SECTION-FTS-INDEX](SECTION-FTS-INDEX.md), page structure
and splitting in [EDITORIAL-CONTRACT](EDITORIAL-CONTRACT.md), atlas and edition
mechanics in [PATTERN-ATLAS-CONTRACT](PATTERN-ATLAS-CONTRACT.md), and branch/PR
discipline in [AGENTS.md](../AGENTS.md). If this section and an owning contract
disagree, the contract wins.

For a text-only correction, keep `id`, `canonical_path`, `parent_id`,
`source_ids` and level-2 headings stable; changing any of them, adding or
removing pages, or changing evidence is a structural or evidence revision and
needs its own review. Record the authorized before/after hashes as described
above, then rebuild in the order the plan prints. A revision belongs to one
issue; do not mix unrelated pages in one change.

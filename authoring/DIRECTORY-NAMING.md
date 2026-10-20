# Volume and chapter directory naming

Status: required for the directory layout selected by the owner on 2026-10-20, Refs #214. This document owns the naming rule and the acceptance conditions for migrating existing paths.

## Required layout

Book volume and chapter directories use **<number>-<description>**. Retain the existing type prefix and zero-padded two-digit ordinal, then append a readable English description:

| Directory | Pattern | Example |
| --- | --- | --- |
| Volume | `vNN-<description>` | `v01-requirements-and-architecture` |
| Chapter within its volume | `cNN-<description>` | `c01-problem-framing` |

A complete example path is `book/volumes/v01-requirements-and-architecture/c01-problem-framing/README.md`. This is a naming example, not a link to an already migrated directory.

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

The current corpus uses numbered directories under `book/volumes`. Those existing paths are a pending migration under #214, not proof that the new naming requirement has already been implemented. This requirements change adds no directory moves or placeholder book pages. Existing canonical paths remain authoritative until an atomic migration is delivered.

Before declaring the directory migration complete:

1. Select readable names for all ten volumes and all 71 chapters from their current titles, and record a complete old-to-new path map. Every canonical document must have exactly one destination and retain its ID and parent identity.
2. Move the actual files and update relative links, navigation, edition outline, current canonical paths in frontmatter and identity records, and affected tooling/fixtures in the same change. Do not retain a second canonical copy under the old directory.
3. Preserve technical prose, source ownership, opaque identities, evidence and review history. Path-only edits do not establish new source inspection, content verification or substantive acceptance.
4. Keep the earlier migration/decomposition/enrichment records as historical evidence. Add explicit path-aware migration provenance so their conservation checks remain meaningful; do not overwrite baseline hashes merely to hide a failure.
5. Regenerate the routing index and edition inventory from the migrated canonical files. Verify complete membership, ID stability, numbering, path-map coverage, unique destinations, local files/anchors and unchanged source-block meaning.
6. Run the relevant Python premerge, schema, navigation, conservation and edition checks, applicable tests and Mermaid syntax parsing on the exact migrated tree. A requirements-only check cannot be reported as a completed migration.

No new naming validator is introduced by this document. Existing validation success does not establish conformance of the old numbered directories to this new policy. #214 remains open while physical migration and the remaining edition acceptance work are outstanding.

# Tycho document identity, metadata and evidence-state semantics

> E04-01 [issue #32](https://github.com/rouslanbaranov/tycho/issues/32), original specification v0.1, 2026-10-19. **Design contract only**: strict JSON Schemas, generated YAML frontmatter, routing indexes and automatic enrichment belong to subsequent issues. The specification does not claim all existing pages already have metadata.

## Canonical ownership and stable identities

The book's **original Markdown source is authoritative for its explanation**. Generated metadata, a navigation index, the lexical index and graph neighbors may route to that source, but must never become alternative canonical technical prose.

An ID denotes a logical publication object, **not** its filesystem pathname, page number or content hash. A stable ID survives a rename, heading edit and most reorganization. Every identity change requires an explicit migration map; silent ID reuse or recycling is prohibited.

Proposed ID shape: `tycho.<kind>.<human-stable-slug>`, where `kind` is `book`, `volume`, `chapter` or `page`. The slug is assigned once by editorial ownership and can include a short hierarchical qualifier when names collide. It is not automatically generated from a mutable title on every run. Schema #33 will define exact regular expressions and cross-document uniqueness semantics.

| Kind | Meaning | Parent | Canonical owner |
|---|---|---|---|
| `book` | Publication entry point, scope and reading routes | null | Existing [book landing](../../book/README.md) |
| `volume` | Bounded topic family and reading purpose | book ID | One existing/approved volume landing |
| `chapter` | Coherent engineering question group | volume ID | One actual chapter landing, not an empty planned TOC entry |
| `page` | One bounded explanation/decision question with evidence | chapter ID when available; explicit draft gap allowed | Existing exact Markdown page; no second copy in graph/index |

An unpublished research note, source register entry, synthetic example, graph shard or generated index is **not automatically a fifth book-page kind**. Its own registry/schema owns its identity. If a page lacks a published parent, preserve `parent_id=null` with an explicit `draft-parent-unresolved` routing issue rather than inventing a nonexistent chapter. Published hierarchy validation is stricter than draft editorial staging.

## Proposed metadata object and required meaning

| Group | Fields and types (schema #33 to enforce) | Authority and semantic boundary |
|---|---|---|
| Identity | `schema_version: integer`, `document_id: stable string`, `kind`, `canonical_path: relative Markdown path`, `parent_id: nullable stable ID`, `title` | Canonical authoring document; path may change, ID does not |
| Human navigation | `summary: original short answer`, `reader_questions: list`, `route_hints: list`, `topics: list`, `perspectives: list`, `keywords: list`, `aliases: list` | Curated routing aids, not evidence or target architecture approvals |
| Relationships | `related: list of {target_id, relation, reasoning}` | Outbound references to existing canonical IDs; directions and types intentional, not free co-occurrence |
| Research evidence | `source_ids: list`, `claim_ids: list`, `evidence_status: enum`, `evidence_scope: list of exact checked sections/versions`, `verified_at: nullable date` | Source/claim registries; **not inferred from last edit or generated timestamp** |
| Editorial quality | `review_status: draft/self-reviewed/independent-reviewed`, `reviewed_at: nullable date`, `reviewer_reference: nullable string` | Separate named editorial action; self-authorship does not imply independent review |
| Build lifecycle | `content_revision: nullable immutable digest or VCS commit`, `content_updated_at: nullable date`, `metadata_generated_at: nullable UTC timestamp`, `index_built_at: nullable UTC timestamp` | Mechanically observable input/rebuild facts, **never content verification** |
| Ownership/migration | `owner: canonical editor role/path`, `supersedes: list`, `redirect_from: list of prior IDs/paths`, `identity_notes` | Explicit bounded changes and future schema migration record |

Dates MUST remain independently meaningful. An agent may regenerate frontmatter at 14:00 without having read even one primary-source section; that changes `metadata_generated_at`, **not** `verified_at` or `review_status`. Content edits and index rebuilds are also not facts about correctness. When an evidence source moves or changes, mark *needs re-review* with exact affected claim IDs, not everything verified automatically.

## Routing dimensions: terms without false ontology

- **Topics** answer *what domain is this about?* (e.g. `queueing`, `distributed-transactions`).
- **Perspectives** answer *why is a reader approaching it?* (e.g. `capacity`, `correctness`, `security`, `failure-recovery`, `modernization`).
- **Reader questions** are natural-language retrieval entry points, ideally exact user questions, not filler tags.
- **Keywords** are terms in the actual explanation. **Aliases** are alternate industry names or abbreviations, distinct from confirmed synonyms.
- **Related edges** carry named direction and evidence/qualification. A relationship saying “alternative to” must not be mistaken for “is a dependency of.”
- Summary and route hints are **derived/curated editorial explanations**, not primary technical evidence. Search tools may return them, but must provide expansion to the canonical page and actual claim/source reference.

Avoid treating all topics, perspectives, keywords and aliases as one mixed tag array. The contract supports both route-by-question and bounded lexical/graph retrieval without equating co-occurrence to architecture applicability.

## Evidence state must not be synthesized from formatting success

Proposed evidence states:

| `evidence_status` | Exact interpretation |
|---|---|
| `unverified` | Claim material exists but cited passages have not been inspected |
| `evidence-linked` | At least one bounded claim-to-source link is present; mechanical link integrity does not prove semantic support |
| `section-inspected` | Named primary-source sections and dates were recorded; review may remain pending |
| `contested` | Material discrepancy, scope dispute or contradiction requires resolution |
| `insufficient-evidence` | A decisive source/measurement/assumption is unavailable |
| `reviewed` | A named relevant domain/semantic review event exists for this declared source and claim scope; no implicit production benchmark |

The source-of-truth for a verified claim stays in [claim references](../../sources/claim-references.json) and bounded [research events](../../sources/research-events.json), not a generated summary's `reviewed` flag. The metadata validator can enforce status combinations and IDs, but must not fabricate a reviewer record or source reading.

## Stable hierarchy, relocation and schema versioning

1. **Write/allocate an ID only once** using an ownership table. Filename and displayed title can change without changing ID; new content with a fundamentally different question gets a new ID, and any meaningful split explicitly records old-to-new mappings.
2. `canonical_path` is relative to repository root and must resolve to one real Markdown file. No symlinks, path traversal, duplicate canonical owners or two active documents claiming the same ID.
3. `parent_id` must point to an existing document of the immediately higher published level. No parent-of-self, cycles or fictitious hierarchy from a proposed TOC. Draft-parent gaps must remain explicit until filled.
4. Related relationships must resolve to existing IDs or be clearly provisional in a **separate** planned relationship list; no dangling active links. Check direction and declared inverse where a relation claims symmetry.
5. Start with `schema_version=1`. A breaking schema change increments version, provides deterministic migration, fixtures for old/new formats, a compatibility window and a no-data-loss/rollback test. No silent upgrade in a frontmatter regeneration run.
6. Preserve historical alias/redirect identity with a source and reason; do not reuse retired IDs. An index rebuild must be deterministic for a fixed snapshot and never modify original technical pages to make them conform by guesswork.

## Original illustrative metadata, not yet deployed frontmatter

A representative page [queueing and Little's Law](../../book/performance/queueing-littles-law.md) can have ID `tycho.page.queueing-littles-law` even if moved between `book/performance` directories later. The [example fixtures](../../examples/metadata-identity-fixtures.json) capture intended field meanings and a separate book landing without pretending a missing chapter parent exists. Formal validators, actual frontmatter insertion and generation are **not** delivered by this issue.

## Validation and review gates for #33+

- Strict types/required/unknown fields, enums, dates, nonempty arrays, ID and path patterns; source/claim resolution; draft-vs-published hierarchy state.
- Intentional input version and migration behavior, valid/invalid fixtures, stale index and meta-generation date separation.
- Runtime checks must prevent an agent from promoting `source_ids` or a generated summary into verified technical evidence.
- Do not overwrite separately curated provenance, research state, approved reviewer decisions or stable IDs on re-generation.
- No broad document enrichment or M9 case-source reprocessing as a side effect of metadata adoption.

**Status:** this issue establishes the semantics and provenance separation; no actual JSON Schema, generated YAML frontmatter, metadata classifier, graph index, expert approval or book-wide migration is claimed.

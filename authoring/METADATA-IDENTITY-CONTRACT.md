# Document metadata and durable knowledge identity — v1 semantic contract

> Issue [#32](https://github.com/rouslanbaranov/tycho/issues/32), E04-01 / M3, original design contract, 2026-10-19. This establishes **semantics** for a future versioned JSON Schema (#33) and automatic YAML frontmatter (#34). It does NOT assert that an existing book corpus has been converted, metadata generated, or validated.

## Goals and authority

Every canonical Tycho book node should be retrievable by a stable, opaque identity independently of its file name, title, placement and generated index. Support document kinds, hierarchy, topics, perspectives, compact routing hints and bounded evidence/verification state without confusing *a successful build* with *independent content verification*. Each field has **one authoritative owner**. An AI model may suggest metadata but may not promote evidence status, invent source reading dates or mint new IDs silently.

The [editorial contract](EDITORIAL-CONTRACT.md) defines actual document responsibilities; [book structure](../book/PROPOSED-STRUCTURE.md) remains proposed until approved. [Public-source register](../sources/register.json), [claim evidence](../sources/claim-references.json), and [research events](../sources/research-events.json) already own their respective truths. Metadata points to them; it does not duplicate their underlying evidence.

## Stable IDs, document kinds and hierarchy

| Field | Semantics / invariant | Canonical authority |
|---|---|---|
| `metadata_version` | A strict semantic contract number, initially **1**; this is distinct from source-catalogue and JSON Schema versions | Metadata schema publisher |
| `id` | Stable, globally unique within one Tycho book snapshot; e.g. `tycho.page.01h9example`. IDs are minted once and never recomputed on file rename, route change or heading edit | Document owner / checked-in ID registry; future index verifies uniqueness |
| `kind` | `book`, `volume`, `chapter`, `page` (technical canonical explanation), `landing` (navigation-only), `decision` (bounded ADR) | Canonical document author |
| `parent_id` | Null only for book root; every other node points to **one** logical parent. Landing nodes still have unique identity | Document owner, validated in hierarchy graph |
| `title` | Human-readable; can change with revisions without changing ID | Page content/editor |
| `canonical_path` | Repository-relative POSIX Markdown path, no absolute paths or traversal, unique within snapshot | Git file path, checked rather than trusted from model |
| `topic_ids` | Nonempty curated taxonomy identifiers (not arbitrary prose); multiple topics may apply | Curated taxonomy owner, versioned |
| `perspectives` | Explicit reader viewpoints, including `requirements`, `architecture`, `implementation`, `operations`, `security`, `migration`, `evaluation` | Canonical author; shared vocabulary subject to versioning |
| `summary` | One bounded, original, user/agent-facing abstract answering *what question belongs here*; not a full chapter duplication | Page editor; reviewed independently for factual overclaim |
| `route_hints` | Reader questions, prerequisites/related IDs, key terms, exclusions; discovery only, NOT claim proof | Page editor, later index checks related links |
| `evidence_scope` | References to actual source IDs, `claim.*` IDs and explicit supporting evidence state | References to source and provenance registries, never copied claims |
| `content_review` | `draft`, `self-checked`, `independent-reviewed`, `accepted` with honest review event; independent-reviewed/accepted requires external recorded proof | Named reviewer/decision authority, not AI self-report |
| `source_inspection_date` | Date of an actual inspected source section relevant to this page, or null; not the last page edit | Actual source research event/provenance |
| `content_verified_at` | Date of **actual meaningful claim support review** or null; not a build or git commit timestamp | Evidence/review workflow, protected from inference |
| `authored_at`, `updated_at` | Authorship and content-change dates; must never imply source recency or expert approval | File revision/editor |
| `generated_at` | Optional build artifact timestamp belongs to **derived index/build manifest only**, never source verification | Build system; NOT source page frontmatter |

Kinds and taxonomies are a v1 proposal. A `landing` is navigational; a `page` owns a bounded technical question; a `chapter` or `volume` may have a landing page without inventing a second canonical technical owner. **Never generate an empty 9-volume directory tree** just to satisfy metadata coverage. Only annotate existing artifacts admitted to canonical book navigation.

### ID minting and stability

1. Mint an opaque `tycho.<kind>.<token>` stable ID when a real canonical document is created. The token is immutable; human-title slugs and Git paths are not identity sources.
2. Store the assigned ID in checked-in metadata and registry; validation rejects duplicates and missing path targets. Rename/move retains original ID and records the new canonical path.
3. A kind change that alters canonical responsibility needs a reviewed migration; the ID may be retained only if the underlying knowledge entity remains the same. Splitting a page creates **new** IDs for new independent questions, with an explicit `supersedes` / navigation mapping. Do not claim old IDs were migrated without an actual checked record.
4. Deletion requires a tombstone/redirect record with snapshot and reason. Never reallocate a retired ID. Detect hierarchy cycles, orphan parents and related references before a generated routing index is considered fresh.
5. The *same source code revision* can support several claims and pages, but content owners must remain unambiguous; cross-references do not produce secondary canonical copies.

## Routing hints and token-economical agent use

A compact frontmatter record may include reader questions (exact user intent), scope exclusions, topic/perspective tags, parent and related canonical IDs, and provenance references. This supports **Route → Read → Verify**: find a small candidate set; load the bounded canonical explanation; follow precise evidence when needed. A route hint is NOT an architecture recommendation or a permission to hide contrary evidence. Search services may return a preview as long as it includes **snapshot identity, canonical ID/path, evidence/coverage warning and continuation mechanism**. Full-text indexing and its freshness belong to later milestone tasks.

## Evidence must remain epistemically separate

| Concept | Allowed source | Wrong inference forbidden |
|---|---|---|
| File modified date | Git history | `content_verified_at = modified_date` |
| Index or build timestamp | Build manifest | `source_inspection_date = index_refresh` |
| Public source landing opened | Discovery/research entry event | `content_verified_at` or `section-inspected` |
| Source section actually read | Immutable research event and/or claim ledger | A source section automatically proves a claim |
| Claim linked to admitted source | Claim relation with exact location and conditions | Independent domain review has occurred |
| Independent domain approval | Reviewer identity/date/scope record | GitHub merge or green structural CI substitutes for that review |
| Published technical benchmark | Reproducible experiment, version and run logs | Toy/synthetic example is empirical capacity evidence |

**Unverified is a valid state**, including `null` timestamps. Do not apply an optimistic default or force a date through strict schema validation. An inaccessible or rights-restricted source must remain in `insufficient-evidence` state, even if a separately inspected official companion answers a narrower question.

## Authoritative data ownership and contract boundaries

| Artifact | Authority | Consumer behavior |
|---|---|---|
| Canonical Markdown body and page frontmatter | Technical document owner, revised by human or reviewed agent commit | Route/index derives content IDs and summaries; does not edit body |
| Taxonomy and metadata semantics | This versioned contract, then formal schemas under #33 | Reject unknown values rather than silently derive fake categories |
| Source register / public repository lock | Existing `sources/register.json` and `sources/public-repositories.lock.json` | Resolve registered source ID and exact admissible code commit |
| Claim and section provenance | Existing `sources/claim-references.json` | Resolve claim/status and evidence; never copy source text into metadata |
| Research slice history and checkpoints | Existing `sources/research-events.json` | Use latest derived status, preserve underlying historic events |
| Routing index and cross-doc relationships | Generated from validated committed canonical metadata in #35 | Index is disposable derived output; cannot override canonical ID owner |
| Knowledge graph | Separate curated graph/shard authorities in E06 | Never treat lexical co-occurrence as authoritative edge evidence |

## Schema versioning and migration policy

- `metadata_version=1` defines **field meaning**, not merely syntax. The formal JSON Schema for each kind belongs to #33; v1 fixtures must follow this semantic contract. Do not equate this proposal with an already enforced JSON Schema.
- Additive optional fields may be considered in a compatible minor revision **only if old readers can ignore them without changing critical semantics**; otherwise issue a new explicit schema version. New required fields, enum removals, identity/hierarchy changes, or altered evidence semantics are incompatible major changes requiring reviewed migrations.
- A migration is **explicit and deterministic**, with `source_contract_version`, `target_contract_version`, old/new ID mapping, affected paths, fixture checks and a no-data-loss report. Existing stable IDs and `content_verified_at` nulls must be preserved.
- The migration tool must support **dry-run diff** and deliberate apply with review; no silent rewrite of every file during index refresh, source acquisition, agent onboarding or search requests.
- Mixed contract versions must either be explicitly supported by the reading service or fail with actionable `unsupported_contract_version`, not a misleading default.
- Keep a snapshot manifest of the exact schema version, Git commit, metadata set hash and routing index version. A rollback of a search index is not equivalent to rollback of renamed canonical files and must not resurrect retired IDs.

## Acceptance and status boundary

This issue's output is the semantics, identity policy, authority table and schema migration plan. **No claim** that frontmatter exists across the corpus, all IDs have been assigned, draft schema validators are executable, source passages reviewed by a third party, or any agent service deployed. Tests for those claims belong to #33–#37 and E06–E11. Keep legacy unannotated pages navigable until a verified migration is performed.

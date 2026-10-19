# Tycho metadata and source-reference JSON Schema v1

> E04-02 [issue #33](https://github.com/rouslanbaranov/tycho/issues/33). These are **versioned, strict JSON Schema Draft 2020-12 contracts**, not evidence that any existing chapter's frontmatter has been migrated. They implement syntax, required fields, nested arrays, type/enum/date rules and unexpected-property rejection, not factual truth or valid external licence rights.

## Files and ownership

- [Document metadata schema](document-metadata.v1.schema.json) describes stable `tycho.<kind>.<opaque>` IDs, `book/volume/chapter/page/landing/decision` kinds, hierarchy, canonical Markdown path, topic/perspective taxonomy, compact routing hints, source and claim IDs, actual evidence scope and review dates. Root book must have null parent; child pages have a parent ID. The declared document kind must match the stable ID namespace.
- [Source reference schema](source-reference.v1.schema.json) describes a single **normalized reference** to an already registered source: HTTPS document section or full Git commit/path/symbol, admission, verification scope, observation dates and reuse status. It is **NOT** a wholesale replacement for the existing version 2 [source discovery register](../sources/register.json) or [typed claim-evidence ledger](../sources/claim-references.json).
- The authority and policy behind these fields remain in the [semantic identity contract](../authoring/METADATA-IDENTITY-CONTRACT.md). Neither source observation timestamps nor Git build dates imply content verification.

## Explicit validation commands

Validation uses the external, permissively licensed `jsonschema` Python package. The core Tycho scripts otherwise use the standard library. Install this optional local dependency explicitly for schema checks:

~~~sh
python3 -m pip install -r requirements-validation.txt
python3 scripts/validate_metadata_schemas.py examples
python3 scripts/validate_metadata_schemas.py validate \
  --kind document --file fixtures/metadata-valid-page.v1.json
python3 scripts/validate_metadata_schemas.py validate \
  --kind source --file fixtures/source-valid-section.v1.json
python3 -m unittest discover -s tests -p 'test_tycho_metadata_schemas.py' -v
~~~

Run commands at the repository root. The schema CLI **fails closed** if the dependency is not installed. The new unit-test module reports **skipped**, not passed, when that dependency is missing. Later unified validation/CI work under #37 must install the explicit dependency and enforce these checks; do not treat a skip as acceptance. GitHub Actions must remain milestone-close-only; no PR/push CI activation is part of this issue.

## Checked-in example instances

| Instance | Intended coverage | What it does NOT certify |
|---|---|---|
| [Page metadata](../fixtures/metadata-valid-page.v1.json) | Opaque page ID, chapter parent, topics and perspectives, unknown verification date | Actual production evidence or completed frontmatter migration |
| [Book landing](../fixtures/metadata-valid-book.v1.json) | Root ID, null parent, navigation summary and honest absent evidence | An approved complete volume/chapter hierarchy |
| [RFC 9110 section](../fixtures/source-valid-section.v1.json) | Admitted and explicitly inspected document-section reference with a date | Technical claim correctness, legal reproduction rights |
| [CloudEvents git reference](../fixtures/source-valid-git-reference.v1.json) | Pinned 40-char commit/path with `identifier-only` and null verification date | Source code was downloaded, symbol exists, source body inspected |

The [unit-test suite](../tests/test_tycho_metadata_schemas.py) starts from these valid examples and applies changes expected to fail: invalid day/month, extra keys, duplicate/invalid list elements, path traversal, mismatched ID/kind, invalid parent, unauthorized verification/review promotion, pending source claimed inspected, and wrong code revision.

## Invariants that structural JSON Schema cannot prove

- Across an entire corpus: globally unique IDs and canonical paths, existence and kind of parent/related IDs, hierarchy cycles, tombstone integrity and correct Markdown location. These require #35's deterministic index/corpus-level checks.
- Exact Git revision and source section actually exist in authorized public sources; material support, conditions and contradictions still require #28/#29 provenance and review workflows.
- A manually filled `content_verified_at` or `independent-reviewed` field is **true**. The schema can require a review proof URI and a date, but only an actual authorization/review process establishes validity.
- That Markdown pages already have generated YAML frontmatter. #34 adds a deliberate non-destructive generation/migration mechanism; do not infer schema adoption from sample JSON.
- Whether source permissions permit quotations, copies or use in an internal or public service; rights remain separately reviewed.

Schemas reject extra fields rather than silently assuming a default. If a future change alters the meaning of evidence or ID assignment, publish a new schema version and an explicit reviewed migration. No upgrade of historical verification status is allowed from formatting, index refresh, source acquisition or frontmatter normalization alone.

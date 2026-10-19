# Deterministic metadata-to-YAML frontmatter generation

> E04-03 [issue #34](https://github.com/rouslanbaranov/tycho/issues/34). This implements **opt-in, non-destructive metadata rendering** from an already reviewed JSON instance, not AI inference of factual state and not corpus-wide migration.

## Authoritative input, output and validation

- Use an explicitly prepared [document metadata instance](../fixtures/metadata-valid-page.v1.json) conforming to [Draft 2020-12 document schema](../schemas/document-metadata.v1.schema.json). The [semantic contract](METADATA-IDENTITY-CONTRACT.md) owns stable IDs and evidence/review meaning. Source/evidence data remain in [their own registries](../sources/CLAIM-PROVENANCE.md).
- [Generator](../scripts/frontmatter_generate.py) validates the JSON with the separate [schema validator](../scripts/validate_metadata_schemas.py), then emits canonical YAML syntax: deterministic key order, stable nested mapping order, safely double-quoted scalars, ordered lists and explicit nulls. The renderer never computes or invents an ID, source-verification date, review record, publication or benchmark.
- YAML output is compatible with the constrained v1 field structure only; do not feed arbitrary nested data, executable tags or anchors. The book Markdown body remains byte-for-byte preserved after the newly inserted header.
- The source JSON is authoritative during this bounded migration. The generator checks the actual target path in `book/`, refuses symbolic links and traversal, existing dirty or conflicting YAML headers, and refuses to touch paths outside canonical book content.
- The script never silently refreshes a source, graph, index, CI, or another page. New headers are added **only** via an explicit `apply --allow-write` action; an existing differing header is a review-required conflict, not permission to change IDs.

## Run locally from a full Tycho checkout

~~~sh
python3 -m pip install -r requirements-validation.txt
python3 scripts/validate_metadata_schemas.py validate \
  --kind document --file fixtures/metadata-valid-page.v1.json

# Preview the exact YAML, no file mutation:
python3 scripts/frontmatter_generate.py render \
  --metadata fixtures/metadata-valid-page.v1.json

# Target-aware change report: does NOT change any existing page:
python3 scripts/frontmatter_generate.py diff \
  --metadata fixtures/metadata-valid-page.v1.json

# Only after issue/review approval for this specific page:
python3 scripts/frontmatter_generate.py apply \
  --metadata fixtures/metadata-valid-page.v1.json --allow-write

python3 -m unittest discover -s tests -p 'test_tycho_frontmatter_generate.py' -v
~~~

**Do not execute the apply example automatically as part of tests or CI.** The sample fixture describes an existing researched page but intentionally does not imply that this page's frontmatter or verification status has been migrated. The tests operate on isolated temporary files and add no source claims.

## Normalization policy and status reporting

| Current state | Report/result | Allowed action |
|---|---|---|
| Target page lacks frontmatter | `would-insert` and diff of **header only** | Write only after `apply --allow-write`; original prose unchanged |
| Header already equals generated v1 representation | `unchanged` | Idempotent no-op, no timestamp update |
| Existing different frontmatter (even if one field differs) | `conflict-existing-frontmatter` | **Do not auto-merge**; inspect ID, evidence, reviewer and revision manually |
| Malformed/truncated YAML fence | Validation error | Refuse mutation, repair under normal reviewed authoring procedure |
| Unknown schema version, missing extra fields or invalid dates/ID | Schema error, no mutation | Correct canonical metadata through explicit review |
| Outside `book/`, path traversal or symlink target | Safety error, no mutation | Do not bypass scope guard; adjust reviewed input |

This tool does not *normalize existing YAML in place* by guessing which values are authoritative. It computes deterministic normalized **proposals** and reports conflicts non-destructively; a reviewed future migration can reconcile intentional changes with explicit ID and evidence-status safeguards.

## Reproducibility and non-goals

The [ten offline tests](../tests/test_tycho_frontmatter_generate.py) exercise ordering, stable IDs, no invented evidence dates, idempotence, original body retention, explicit write gate, conflict refusal, unsafe paths and malformed headers. Their presence does not mean they passed in every environment; validation of live book content remains a separate manual/CI gate.

Not completed here: migration of the entire book, YAML parser and semantic round-trip for arbitrary hand-written frontmatter, cross-document parent/related checks, index freshness, independent review, or source inspection. The generated metadata becomes eligible for routing only after formal schema and corpus-wide consistency validation under #35–#37. No M9 case studies, shared workflow triggers or private sources were modified.

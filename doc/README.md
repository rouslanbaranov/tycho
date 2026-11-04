# Tycho documentation

This directory is the production documentation set for Tycho. It explains what
the project contains, how the evidence and promotion system works, how the
atlas and V12 models are structured, how indexing and MCP are implemented, what
the tests and benchmarks actually measure, and how the book was built.

The set is descriptive, not a second source of truth. Canonical metadata,
promotion records, tests and generated indexes remain authoritative. Counts below
were verified on 2026-11-02 against the repository at `17599119`.

## Documentation map

| Document | Question it answers |
|---|---|
| [Product overview](product.md) | What is Tycho, who is it for, what are its features and limits? |
| [Evidence layer](evidence-layer.md) | How sources and entries become sufficient. |
| [Pattern atlas](pattern-atlas.md) | How are 145 patterns organised, owned and promoted? |
| [Modelling and simulation](modelling-and-simulation.md) | V12 models and decisions. |
| [Index and search](index-and-search.md) | How are pages indexed, searched and snapshotted? |
| [MCP layer](mcp-layer.md) | Tools, transports and limits. |
| [Tests and coverage](tests-and-coverage.md) | What is tested and what is not. |
| [Benchmarks](benchmarks.md) | Which benchmarks exist and what do their metrics establish? |
| [Book creation](book-creation.md) | How the book was built and what was hard. |

## Canonical numbers

These are catalogue and artifact counts, not marketing claims.

| Measure | Current value | Authority |
|---|---:|---|
| Volumes | 12 | `book/volumes/` |
| Chapters | 89 | `book/volumes/*/c*/` |
| Book Markdown documents | 612 | `book/**/*.md` |
| Pattern entries | 145 | `owner-units.v1.json` |
| Pattern families | 11 | `owner-units.v1.json` |
| Technically and decision sufficient | 104 | `sufficient-promotions.v1.json` |
| Owner-accepted sufficient entries | 94 | `sufficient-owner-acceptance.v1.json` |
| Remaining entries | 41 | 145 minus 104 |
| Registered sources | 366 | `sources/register.json` |
| V12 models | 3 | `edition/v12/models/` |
| V12 scenarios | 10 | `edition/v12/scenarios/` |
| V12 seeded runs | 10 | `edition/v12/runs/` |
| V12 decisions | 2 | `edition/v12/decisions/` |
| Route-index documents | 612 | `generated/route-index.v1.json` |
| Citable sections | 3,190 | 612 page overviews + 2,578 H2 sections |
| H3 internal passages | 504 | section model in `scripts/section_fts_index.py` |
| MCP tools | 11 | `mcp/schemas/input/` |
| Core test definitions | 709 | `tests/` |
| MCP test definitions | 123 | `mcp/tests/` |
| Saved AI-review reports | 199 | `authoring/ai-reviews/` |
| Promotion timing cycles | 84 | `promotion-entry-timing-2026-10-29.json` |

### Primary artifacts

- [Owner units and families](../edition/patterns/owner-units.v1.json)
- [Promotion records](../edition/patterns/sufficient-promotions.v1.json)
- [Owner acceptance](../edition/patterns/sufficient-owner-acceptance.v1.json)
- [Source register](../sources/register.json)
- [Route index](../generated/route-index.v1.json)
- [Promotion timing](../authoring/promotion-entry-timing-2026-10-29.json)

## Reading paths

- **New reader:** [Product overview](product.md) → [Book creation](book-creation.md)
  → [Pattern atlas](pattern-atlas.md).
- **Contributor:** [Evidence layer](evidence-layer.md) →
  [Tests and coverage](tests-and-coverage.md) → [AGENTS.md](../AGENTS.md).
- **Engineer onboarding retrieval:** [Index and search](index-and-search.md) →
  [MCP layer](mcp-layer.md) → [Benchmarks](benchmarks.md).
- **Reviewer:** [Evidence layer](evidence-layer.md) →
  [Benchmarks](benchmarks.md) → the cited artifact for a specific claim.

## What this set does not claim

- It does not claim complete source reading, complete evidence coverage or
  independent human review.
- It does not claim that V12 outputs are calibrated or production measurements.
- It does not claim that the MCP service is a hardened production service.
- It does not claim that a test count is line coverage or that a passing validator
  proves semantic correctness.
- It does not replace the canonical book, metadata, source register, promotion
  records or generated indexes.

## Reproduce the core checks

Use Python 3.15.0 and the dependencies in `requirements-validation.txt` and
`scripts/requirements-routing.txt`.

```sh
python3 scripts/check_boundary.py
python3 scripts/validate_sources.py
python3 scripts/source_catalog.py --check
python3 scripts/validate_edition.py
python3 scripts/build_v12_index.py --check
python3 scripts/validate_v12.py
python3 -m unittest discover -s tests -p 'test_tycho*.py' -v
```

Some checks depend on generated indexes and on the exact interpreter. See
[Tests and coverage](tests-and-coverage.md) for the current limitations.

# Public research sources

> **Historical manuscript transition — 2026-10-20, before edition assembly:** The owner confirmed independent substantive/content acceptance of all 69 primary chapter manuscripts at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. PR #218 merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`; #213 and E14 #15 are completed. #214 is open and ready for ten-volume/69-chapter edition assembly and named publication. The exact accepted-head 13/13 validation groups and 215/215 tests PASS are owner-reported in [PR #218](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915), not a new run on a later status commit. Earlier pending/0-of-69/review-open rows and pre-merge instructions below are historical and superseded for the manuscript acceptance gate. Their original observations and evidence limits are retained; no signed per-chapter reviewer records are manufactured. No finished physical edition or deployed service is claimed; visual rendering/live MCP remain owner-cancelled. See [current state](../authoring/STATE.md) and [reconciliation](../authoring/PROJECT_STATUS_RECONCILIATION_2026-10-20.md).


## Purpose

Provide a curated, independently public research base for the System Design book. The canonical inventory is [register.json](register.json). Browse the generated [catalogue](CATALOG.md), the [coverage map](COVERAGE.md), the [implementation map](IMPLEMENTATIONS.md), the [reading plan](READING-PLAN.md), and [known gaps](GAPS.md).

This is a first discovery pass, not a claim to contain every excellent source or to have read complete works. Selection combines original research, author-hosted books/references, public standards, official documentation and maintainer code repositories. Vendor guidance is authoritative about its own interface but requires independent checks for comparative claims.

## Access and reading semantics

- `admitted-for-research`: public origin and entry page/abstract checked; content investigation remains to be done.
- `bibliography-only`: commercial book metadata/preview; unavailable full text is not evidence.
- `pending-content-access`: canonical source identified but full page retrieval incomplete; do not cite unseen contents.
- `landing-or-abstract-inspected` never means that all chapters, child pages, versions, source code or tests were read.
- `content_verified: null` means no complete content verification is claimed.
- Unit-level section reads live in `edition/patterns/reading-ledger.v1.json`; they do not
  promote the source-level `reading_status` or `content_verified` unless the whole source
  was verified.

Free access, open-source code, and permission to redistribute are separate properties. No external books, documentation corpora or source code have been mirrored. Public personalized-download offers have not been submitted. No purchases were made.

## Version and evidence contract

Use stable source IDs from the register. Before chapter research, pin the relevant edition, specification version, documentation branch or code revision and record exact sections. Rolling aliases such as current/latest/stable can change. Version observations during discovery are not declarations of latest releases or a selected Tycho runtime baseline. Development documentation must be labelled.

For every material claim, explain why the exact source supports it and state applicable workload, versions and limitations. Record the chapter/claim's evidence separately; the inventory establishes discoverability, not truth. Books complement primary specifications and implementation tests rather than replacing them.

## Reproducible catalogue

Run `python3 scripts/source_catalog.py` after changing the register. Run `python3 scripts/validate_sources.py` and `python3 scripts/source_catalog.py --check` before committing. Structural source-register checks are implemented in Python; strict **document metadata** and **normalized individual source-reference** JSON Schemas already exist in `schemas/` and are exercised by dedicated validators. The latter is **not** a wholesale JSON Schema replacement for the v2 source discovery register or a source-truth certificate; additional end-to-end source-register/API contracts may still be planned.

Research, authoring and review are performed in the repository's working environment. The GitHub repository stores the book and its supporting artifacts. Tasks may be delegated to coding assistants, agents and subagents under the same independence, evidence and editorial rules.

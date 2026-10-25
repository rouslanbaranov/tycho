# Complete-source research and book comparison

Issue: [#225](https://github.com/rouslanbaranov/tycho/issues/225). Started 2026-10-21. Status: accepted and closed 2026-10-25.

The owner authorized complete external-source reading and deep comparison after closing #214. Frozen book baseline: `6754bac6e26faa57d65a301a60be10b3da93f65b`, tree `751d6e08650173d4655370b4989585e4c7ecdaea`. All original tracked files are protected by `baseline-files.json`; research outputs stay in this directory. No book, source register, index, edition, historical audit or release changes are authorized. Repository status documents retain their historical wording; the current task disposition is recorded in GitHub.

Owner steering on 2026-10-21: prioritize reading external sources, especially foundational System Design books, before further comparison tooling or technology-specific expansion. `book-readings.json` and `BOOK-READING.md` record this active work; `book-queue.json` gives priority. Complete a book's actual chapter/appendix reading before claiming whole-book completion.

## Research questions

Do the full sources support the book's material explanations, assumptions, guarantees, failure/recovery and applicability? Which omissions, contradictions, version mismatches, unsupported transfers or missing topics warrant future work? Recommendations remain proposals.

## Reading contract

Read complete articles, papers with appendices, specifications and lawfully available books. For each documentation entry, define the actual unit before claiming completion: one cited versioned page is not a complete manual. Collection roots, repositories and research programs need finite revision-pinned manifests; leave them scope-pending until enumerated. Linked normative dependencies require separate reading records. Retain unavailable commercial full texts as blocked, with lawful alternatives separately identified. Never label search snippets or abstracts full reads.

`source-queue.json` is a reproducible baseline queue, not a mutable completion ledger. `readings.json` records actual observations and precise omissions. `page-census.json` records baseline applicability candidates; subsequent comparisons belong in `comparisons.json`. Reading and substantive page review are separate dimensions. Every completed reading requires named sections, start/end coverage and remaining dependencies. Every finding needs baseline page/anchor, source/section, severity, support classification and proposed action.

## Census interpretation

`census.py` scans every canonical file, including metadata and code, retaining original URL spellings and line locations. It removes fragments for exact register matching; it does not merge versions, infer redirects or count code examples as established citations. Unmatched candidates require editorial classification as a source, supplemental evidence, repository navigation, example endpoint or duplicate. A full lexical census is not a completed publication-level reconciliation. Page references to source IDs are routing context, not assertion-level proof.

## Completion and validation

Keep the issue open until all reading and comparison work is accounted for. Report denominators independently: registered entries, unique publications, full scoped reads, partial/blocked reads, reviewed material claims and reviewed pages. Record accessed revision/date, reading omissions, source self-report vs inference, and no execution or independent peer review unless actually performed.

Re-run `python3 research/source-audit-225/census.py` to reproduce inventory and assert every original tracked file still matches its Git blob. Check research findings and source locations manually and run the repository boundary check before committing. No copying of full external publications into Git; retain bibliographic locations and concise original findings. No scheduled worker, milestone closure or book enrichment is part of this contract.

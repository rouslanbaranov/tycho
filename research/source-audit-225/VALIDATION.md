# Research checkpoint validation — 2026-10-21

This is validation of research artifact integrity, not technical acceptance of the book or proof of source reading.

- `python3 research/source-audit-225/census.py` passed: all **681 original tracked files** match their frozen baseline Git blobs; all **406 canonical Markdown paths** and **247 registered sources** are represented. Outputs reproduced successfully after authoring the reading records.
- All research JSON files parsed successfully; reading IDs were unique in each ledger.
- `python3 scripts/check_boundary.py` passed. Separate editorial origin review: original concise notes plus metadata from independently accessible publisher/author sources; no companion material used.
- `git diff --check` passed before staging; staged whitespace checked before commit.
- Remote main was rechecked as `6754bac6e26faa57d65a301a60be10b3da93f65b`.
- No book, source register, canonical metadata, index, edition, release, historical report, workflow or runtime implementation was changed. The research directory is the entire proposed delta.

The previous full book test run remains attached to main's frozen baseline; it was not rerun or relabeled as a new research result. No Mermaid diagrams or runtime code were changed. At that initial checkpoint, no integration experiment, peer review, whole-book completion, complete publication census reconciliation or complete material-claim audit was asserted. The later SRE completion below supersedes only the whole-book reading count.

## Reading continuation

Chapters 6–18 add 13 finite reading records, with 18 technical figures/formulas inspected. Retrieval line-label coverage was checked across the available representations; missing tail passages in chapters 7, 10, 12, 17 and 18 were separately opened and read. This coverage check detects extraction gaps, not comprehension. The combined chapter reading ledger and finite SRE manifest are checked for matching unique entries. The next unread numbered chapter is 19. Original tracked-file hashes, JSON parsing, lexical boundary and whitespace checks are repeated for this research delta before committing.

## SRE completion continuation

The preceding chapter-19 instruction is historical and superseded. All 48 public book units are now read. The completion ledger adds 29 records and 44 inspected embedded images. This establishes one whole scoped book read, not a full-source or Tycho material-claim audit.

- The read-only census passed again: all 681 original tracked files match frozen main; inventory remains 247 sources and 406 canonical documents.
- All research JSON parsed. The three linked book ledgers have 51 unique reading IDs, including 48 unique SRE unit URLs matching the finite manifest. Every SRE unit is complete and `next_unit` is null.
- The manifest matches the publisher's complete 48-entry navigation after normalizing fragments and trailing slashes. The public contents page was also inspected directly.
- The 29 new reading records match 29 downloaded HTML pages and 44 embedded images. All recorded asset lengths and SHA-256 values match their scratch representations; inspection-aid files are identified separately. Source bytes and images are not added to Git.
- All relative Markdown file links in the research reports resolve locally. Exact public chapter URLs were accessed during reading; linked third-party publications and example placeholder endpoints remain outside this reading claim.
- The lexical boundary check and whitespace check passed. Independent-origin/editorial review covered every changed report, ledger, manifest and proposed commit message: concise original notes and admissible public source metadata only; domain-neutral transfers; no private companion corpus used.
- The optional HTML helper dependency was unavailable in the first verification attempt; the navigation membership check was then implemented and passed using Python's standard HTML parser. Fragmented bibliography links were normalized before set comparison. These verification adjustments did not change reading status or source content.

No technical runtime experiment, independent peer review, final claim synthesis or new full book test-suite run is asserted. No canonical Mermaid or book code changed. Main is kept at the frozen baseline; the research-only delta belongs to the existing #225 branch and draft PR #226.

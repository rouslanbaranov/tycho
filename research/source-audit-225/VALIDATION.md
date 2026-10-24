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

## OSTEP continuation - 2026-10-24

Ten records B052-B061 add chapters 1, 3 and 4-11 (chapter 2 was read at the
earlier checkpoint): `2562` retrieved lines, `39815` words and `104`
pages across CPU virtualization, process API, limited direct execution and
scheduling. Source representations were fetched on 2026-10-24 through the
public Jina reader from the official publisher PDF URLs; the record hashes
match the local text representations. No PDF binary or publication text is
committed.

- All ten records parse as JSON, carry unique IDs and the same 22-field shape;
  every chapter record matches its local line count, word count and SHA-256.
- All `tycho_candidates` paths exist in the frozen baseline; four candidate
  comparisons are recorded in `comparisons.json` as questions, not findings.
- The read-only census passed: all 681 original tracked files, 247 registered
  sources and 406 canonical documents match the frozen baseline. The census
  wrote no tracked changes beyond the intended research delta.
- `python3 scripts/check_boundary.py` passed. `git diff --check` passed.
  The current-main `check_markdown_line_length.py` covers only V11 prose; run
  against this tree it passed, but it does not validate research Markdown.
- No book, source register, canonical metadata, index, edition or historical
  report changed. Only this research directory is in the delta.

Limitations: raster figures were not visually inspected; linked papers, code,
simulator exercises and homework were not read or executed; chapter 9's PDF
footer prints version 1.20 while the site table of contents still says 1.10;
this checkpoint does not claim independent review or whole-book completion.

## OSTEP memory and paging continuation - 2026-10-24

Nine records B062-B070 add chapters 12-20: 2,620 retrieved lines, 43,227 words
and 114 pages. The combined OSTEP continuation is 19 records, 5,182 lines,
83,042 words and 218 pages. Chapter 12 is the two-page dialogue; chapters 13-20
cover address spaces, the memory API, translation, segmentation, free-space
management, paging, TLBs and smaller tables.

- All nine records parse, have unique IDs B062-B070 and the same 22-field
  shape; each matches the local line count, word count and SHA-256.
- All candidate paths exist in the frozen baseline; `comparisons.json` now has
  seven candidate comparisons, still questions rather than findings.
- The read-only census passed again; 681 baseline files, 247 sources and 406
  canonical documents remain represented.
- `check_boundary.py` and `git diff --check` passed. The current-main V11 line
  checker passes against this tree but does not validate research Markdown.
- No book, source register, canonical metadata, index, edition or historical
  report changed. Only the research directory is in the delta.

Limitations: raster figures were not visually inspected; linked papers, code
and exercises were not read or executed; the chapter 9 version discrepancy
remains; no independent review or whole-book completion is claimed.

## OSTEP swapping and complete VM continuation - 2026-10-24

Four records B071-B074 add chapters 21-24: 996 retrieved lines, 21,631 words
and 51 pages. The combined OSTEP continuation is 23 records: 6,178 lines,
104,673 words and 269 pages. Chapters 21-22 cover swapping mechanisms and
policies; chapter 23 covers VAX/VMS and Linux complete VM systems; chapter 24
is the three-page summary dialogue.

- All four records parse, have unique IDs B071-B074 and the same 22-field
  shape; each matches the local line count, word count and SHA-256.
- All candidate paths exist in the frozen baseline; `comparisons.json` now has
  eight candidate comparisons, still questions rather than findings.
- The read-only census passed again; 681 baseline files, 247 sources and 406
  canonical documents remain represented.
- `check_boundary.py` and `git diff --check` passed. The current-main V11 line
  checker passes against this tree but does not validate research Markdown.
- No book, source register, canonical metadata, index, edition or historical
  report changed. Only the research directory is in the delta.

Limitations: raster figures were not visually inspected; linked papers, code
and exercises were not read or executed; chapter 9 prints version 1.20 and
chapter 32 also prints 1.20 while the site table of contents says 1.10; no
independent review or whole-book completion is claimed.

## OSTEP concurrency continuation - 2026-10-24

Ten records B075-B084 add chapters 25-34: 6,667 retrieved lines, 51,357 words
and 139 pages. The combined OSTEP continuation is 33 records: 12,845 lines,
156,030 words and 408 pages. The batch covers the concurrency dialogue, thread
introduction and API, locks, lock-based structures, condition variables,
semaphores, common bugs, event-based concurrency and the summary dialogue.

- All ten records parse, have unique IDs B075-B084 and the same 22-field
  shape; each matches the local line count, word count and SHA-256.
- All candidate paths exist in the frozen baseline; `comparisons.json` now has
  ten candidate comparisons, still questions rather than findings.
- The read-only census passed again; 681 baseline files, 247 sources and 406
  canonical documents remain represented.
- `check_boundary.py` and `git diff --check` passed. The current-main V11 line
  checker passes against this tree but does not validate research Markdown.
- No book, source register, canonical metadata, index, edition or historical
  report changed. Only the research directory is in the delta.

Limitations: raster figures and trace tables were read only as text; linked
papers, code and homework were not read or executed; chapter 9 and chapter 32
print version 1.20 while the site table of contents says 1.10; no independent
review or whole-book completion is claimed.

## OSTEP persistence and distribution continuation - 2026-10-24

Seventeen records B085-B101 add chapters 35-51: 4,933 retrieved lines,
101,044 words and 243 pages. The combined OSTEP continuation is 50 records:
17,778 lines, 257,074 words and 651 pages. The main 51-chapter sequence is
complete; security chapters 52-57 and appendices remain.

- All seventeen records parse, have unique IDs B085-B101 and the same 22-field
  shape; each matches the local line count, word count and SHA-256.
- All candidate paths exist in the frozen baseline; `comparisons.json` now has
  twelve candidate comparisons, still questions rather than findings.
- The read-only census passed again; 681 baseline files, 247 sources and 406
  canonical documents remain represented.
- The lexical boundary check initially flagged one flash-organization section
  label containing a restricted term. The label was replaced with the neutral
  "Groups/Planes" wording in both the record and the aggregate ledger, and the
  boundary check then passed. No prohibited term is reproduced in this report.
- `git diff --check` passed. The current-main V11 line checker passes against
  this tree but does not validate research Markdown.
- No book, source register, canonical metadata, index, edition or historical
  report changed. Only the research directory is in the delta.

Limitations: raster figures and trace tables were not visually inspected;
linked papers, code and exercises were not read or executed; chapter 9 and
chapter 32 print version 1.20 while the site table of contents says 1.10; no
independent review or whole-book completion is claimed.

## OSTEP security continuation - 2026-10-24

Six records B102-B107 add chapters 52-57: 1,168 retrieved lines, 44,816 words
and 89 pages. The combined OSTEP continuation is 56 records: 18,946 lines,
301,890 words and 740 pages. All numbered chapters 1-57 are now represented
(chapter 2 was read earlier); appendices A-H remain.

- All six records parse, have unique IDs B102-B107 and the same 22-field
  shape; each matches the local line count, word count and SHA-256.
- All candidate paths exist in the frozen baseline; `comparisons.json` now has
  fourteen candidate comparisons, still questions rather than findings.
- The read-only census passed again; 681 baseline files, 247 sources and 406
  canonical documents remain represented.
- `check_boundary.py` and `git diff --check` passed. The current-main V11 line
  checker passes against this tree but does not validate research Markdown.
- No book, source register, canonical metadata, index, edition or historical
  report changed. Only the research directory is in the delta.

Limitations: raster figures were not visually inspected; linked papers, code
and exercises were not read or executed; chapter 9 and chapter 32 print version
1.20 while the site table of contents says 1.10; no independent review or
whole-book completion is claimed until the appendices are read.

## OSTEP whole-book text completion - 2026-10-24

Nine records B108-B116 add appendices A-H and the preface: 1,243 retrieved
lines, 21,920 words and 63 pages. The combined OSTEP continuation is 65
records: 20,189 lines, 323,810 words and 803 pages. Together with chapter 2
from the earlier checkpoint, the whole book has been read as text.

- All nine records parse, have unique IDs B108-B116 and the same 22-field
  shape; each matches the local line count, word count and SHA-256.
- Whole-book scope: chapters 1-57, appendices A-H and the preface. The table of
  contents was used for navigation; the dedication was not treated as a
  technical reading unit.
- All candidate paths exist in the frozen baseline; `comparisons.json` now has
  sixteen candidate comparisons at that checkpoint, still questions rather than findings.
- The read-only census passed; 681 baseline files, 247 sources and 406
  canonical documents remain represented. The boundary and whitespace checks
  passed.
- No book, source register, canonical metadata, index, edition or historical
  report changed. Only the research directory is in the delta.

Limitations: embedded raster figures were not visually inspected; linked
publications, code and exercises were not read or executed; chapter 9, chapter
32 and the preface print version 1.20 while the site table of contents says
1.10. The reading is text-complete, not a visual or experimental reproduction.
No independent review or source-to-book completeness is claimed.

## Comparison assessment - 2026-10-24

Sixteen candidate comparisons from the OSTEP reading were assessed against the
frozen Tycho baseline. Result: thirty-five assessed comparisons: eighteen supported,
fifteen qualified, two not-addressed and zero contradicted. Two JEP-to-book
comparisons were added after the reference batch: JEP 491 provenance and JEP 444
socket interruption. Each assessment records the exact book
anchor, the OSTEP record and sections, a bounded conclusion, and a proposed
action. No book page was edited.

- Every assessment has a named book page and anchor, a source record and
  section, a support classification and an explicit limit.
- "Supported" means the page's claim is consistent with the source mechanism;
  "qualified" means the page is consistent but uses a different boundary or
  terminology; "not-addressed" names a source mechanism the page does not use.
  None is a contradiction or a finding of error.
- All twenty anchors and candidate paths exist in the frozen baseline; the
  JSON parses and the lexical boundary check passes.
- The assessments are bounded to the named passages. They are not a
  claim-level audit of whole pages, independent review, owner acceptance or
  permission to edit the book.

## Reference-source batch - 2026-10-24

Sixty-five records R015-R079 extend the reference ledger. Forty-eight are
full-scoped reads: JEP 444, JEP 491, thirty public engineering articles
and sixteen documentation/paper units in the src.m9-* series. Fourteen publisher pages returned no readable
article body and are recorded as blocked-full-text, not inferred. Two internal
team sites are excluded-from-scope and were not accessed.
R024 and R032 each repeat the article body in the representation; their unique
text was read and the duplicate blocks were verified by matching headings.
R041 is a wiki page whose navigation chrome was identified and excluded from
the architecture claim.

- The thirty articles total 5,901 lines and 82,763 words; sixteen documentation/
  paper units add 10,981 lines and 119,174 words; the two JEPs total 563
  lines and 9,941 words. Each full record carries the local representation
  SHA-256, line count, word count, sections and explicit omissions.
- JEP 444 records M:N scheduling, the two JDK 21 pinning causes, diagnostics
  and compatibility changes. JEP 491 records monitor ownership against the
  virtual thread, residual pinning and the removal of the trace-pinned
  diagnostic; its page has no publication timestamp and no delivering-JDK
  statement, so those are not invented.
- The article records are first-party accounts. They are not benchmarks,
  independent verification or general claims about every deployment.
- All candidate paths exist in the frozen baseline; JSON parses; the lexical
  boundary check and whitespace check pass. No book, source register, index,
  edition or historical report changed.

Limits: raster images were not visually inspected; linked articles, code and
internal systems were not read; blocked pages remain unread; no execution or
independent review is claimed.

## Reviewer attempt - 2026-10-24

An independent Reviewer-preset child (0f036025-7d17-4a8c-9034-a207434a2a9e)
was asked to audit the comparison assessments and reference records at HEAD
d65652d. The child returned no report before the bounded stop. No verdict,
finding, acceptance or independent review is claimed. human_review is
not-performed and sufficient is 0. The latest commits b95af3e, dad953d and
a96c6b7 are outside that attempted review's stated HEAD.

## Page matrix and interim synthesis - 2026-10-24

- The 406-page census records a review status for every canonical page:
  27 are comparison-assessed and 379 carry an explicit evidence gap. The
  per-page list is in page-review-summary.json; a gap is not a pass.
- The reference ledger has 79 records: 59 full reads, 1 partial, 17 blocked and 2
  excluded internal team sites. All 45 baseline fetch-incomplete sources are
  accounted for: 29 full, 14 blocked, 2 excluded, 0 unaccounted.
- DEEP-SYNTHESIS.md is an interim synthesis. It lists supported findings, the
  two candidate page actions, the zero-contradiction result, the 202
  landing-only sources, the 379 unassessed pages and the missing independent
  review. It does not claim #225 completion.
- Boundary, whitespace, JSON, candidate-path and anchor checks passed. No book,
  source register, index or edition file changed.

## Final synthesis and acceptance review - 2026-10-24

- FINAL-SYNTHESIS.md records the current evidence base and the unmet criteria.
- ACCEPTANCE.md records verdict **not accepted**: 180 landing-only sources,
  383 page gaps, 14 blocked pages, 2 excluded sources and no independent review.
- The six SRE chapter source records are reconciled to existing SRE reading IDs
  in source-coverage-reconciliation.json; they are not new reads.
- No book, source-register, index or edition file changed. The issue remains
  open; this is not a completion claim.

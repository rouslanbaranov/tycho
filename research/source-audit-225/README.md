# External-source audit — active research checkpoint

Refs [#225](https://github.com/rouslanbaranov/tycho/issues/225). **Incomplete. No book changes.**

The owner closed #214 after verifying its changes were merged. This research compares against main `6754bac6e26faa57d65a301a60be10b3da93f65b`. That closure does not establish full-source verification or a new final release. Existing repository status documents are retained unchanged as frozen historical inputs; GitHub records the current issue disposition.

The owner subsequently prioritized reading foundational books. Start with [book reading and exact continuation](BOOK-READING.md), then [book reading records](book-readings.json). **One whole scoped book is complete: Site Reliability Engineering.** Earlier finite reference readings are retained in [the reference ledger](readings.json); they are not the current priority and do not replace book reading.

Current SRE position: **48/48 public book units complete**, including all 34 numbered chapters, frontmatter, five part introductions, six appendices and bibliography. All examples, tables, footnotes and embedded images/formulas were read or visually inspected. See [completion scope and next research questions](SRE-COMPLETION.md). No source-to-book completeness claim follows from whole-book reading.

Current OSTEP position: **chapters 1, 3-20 complete** (chapter 2 earlier);
nineteen new records are in [the OSTEP continuation ledger](ostep-continuation-readings.json). CPU virtualization, memory API, translation,
segmentation, free-space management and paging are read; raster figures were
not visually inspected, and chapters 21-51 plus appendices remain.

The reading ledger links its [chapters 6–18 continuation](sre-continuation-readings.json) and [completion continuation](sre-completion-readings.json). Reading completion means the exact chapter, its examples, footnotes and embedded technical images; it does not include all publications linked from it. The [download fingerprints](reading-asset-fingerprints.json) identify the downloaded HTML/image representations for later revisiting, not an immutable publisher revision or proof of semantic reading.

## Inventory

The read-only census found 247 registered entries, 406 canonical documents and 763 lexical URL occurrences representing 316 fragmentless URL candidates. Of 214 candidates without an exact register URL match, 17 are this project's issue links and 197 require source/alias classification. These are not 197 confirmed missing publications. Exact editions, redirects and collection descendants remain to reconcile.

- [Research contract](CONTRACT.md)
- [Baseline source queue](source-queue.json) and [supplemental candidates](supplemental-queue.json)
- [Book priority queue](book-queue.json) and [finite SRE reading manifest](sre-units.json)
- [Canonical document census](page-census.json)
- [URL candidates](url-candidates.json) and [all occurrences with baseline lines](url-occurrences.json)
- [Original tracked file hashes](baseline-files.json) and [census summary](census-summary.json)

Queue statuses are baseline planning states. Join the separate actual reading ledgers to determine progress; running the census never resets evidence. `page-census.json` deliberately retains not-yet-assessed: reading a source is not a complete material-claim audit of any page. No completed claim-to-passage matrix or global synthesis is claimed yet.

## Preliminary reference observations retained for follow-up

The earlier Java/reactive/RPC reading produced candidates for later comparison: executor shutdown versus request deadlines; late signals after cancellation; element demand versus byte budgets; synchronous reentrancy and serialized signals; bidirectional streaming write/read deadlock; RPC retry commitment versus durable application effects. These are candidate explanatory improvements, not confirmed book defects. The current virtual-thread page also repeats closely related synthetic scenarios, an editorial observation requiring no external source claim.

The gRPC overview's immediate-cancellation wording must be read alongside the specific cancellation guide's application-cooperation requirements. Source statements need qualification across their own documentation; the book's conservative cancellation language must not be marked wrong merely because an overview simplifies it. See R006 and R011.

## Checkpoint checks

Run `python3 research/source-audit-225/census.py` to regenerate the lexical census and assert all 681 original tracked files still match their baseline Git blobs. Run `python3 scripts/check_boundary.py` and `git diff --check` before committing. These checks cannot prove reading, semantic correctness, source admissibility or independent review.

No source publication text, third-party PDF or image is redistributed here. Original brief reading notes and bibliographic/coverage metadata are the research deliverables. Continue until the complete scoped source and comparison obligations in #225 are honestly accounted for; do not close the task on this checkpoint.

# Deterministic section-level lexical indexing (E07-03)

> Issue [#49](https://github.com/rouslanbaranov/tycho/issues/49), M4. **Implemented local prototype; unverified on the full live Tycho corpus.** Python 3.10+, SQLite with FTS5 and #35's existing strict [route-index scanner](../scripts/route_index.py). No source refresh, embedding service, runtime search API, global graph, deployed MCP or chapter enrichment is created by this tool.

## Authority and published artifacts

The canonical book Markdown and its approved YAML frontmatter remain authoritative. [section_fts_index.py](../scripts/section_fts_index.py) calls existing `route_index.canonical_scan(..., allow_partial=True)` to validate IDs, paths, parents and routing metadata. This is not a second frontmatter validator; it does not invent IDs for unannotated pages.

Only **frontmatter-validated** pages under `book/` are eligible. An unannotated page remains explicitly listed through `coverage=partial` and `unannotated_paths`. An empty eligible set is an error, not a pretend-complete index.

The published `generated/sections-fts-v1.sqlite` stores:
- `meta.manifest`: format version, exact route-index snapshot SHA, coverage, unannotated paths, content hashes and aggregate snapshot ID.
- `sections`: document/section IDs, canonical path, heading, character start/end offsets, exact original content and source SHA.
- `fts`: title/body text using SQLite `unicode61`, section keys stored unindexed. Both tables must agree.

The snapshot ID hashes deterministic metadata and section-key/offset/content-hash records. A second unchanged build avoids rewriting. An incremental build reuses unchanged *parsed sections*, then stages and publishes a **new whole SQLite file atomically**; it does not claim in-place B-tree updates.

## Citation and identity rules

- Document IDs come solely from canonical frontmatter; filename-derived IDs are not introduced.
- A heading with explicit `{#stable-anchor}` uses the anchor. Otherwise the index derives a lowercase heading slug with ordinal disambiguation. Section key: `document_id#section_id`.
- Implicit heading slugs are **not stable across arbitrary heading edits**. Changes require explicit anchor migration or cross-snapshot redirects. The snapshot identifier prevents accidentally reusing stale references.
- Python character offsets are Unicode codepoint offsets, not UTF-8 byte offsets. The subsequent #50 read adapter must preserve offset type and snapshot identity.
- Code fences are ignored when detecting headings, but their original text remains in the appropriate section. No prose is rewritten, summarized or independently validated.

## Operation and safety

~~~sh
mkdir -p generated
python3 scripts/section_fts_index.py build
python3 scripts/section_fts_index.py check
python3 scripts/section_fts_index.py build --full
python3 -m unittest discover -s tests -p 'test_tycho_section_fts_index.py' -v
~~~

The index destination must be an ordinary direct `.sqlite` file inside `generated/`, not a symlink. The builder stages SQLite in the same directory, checks its integrity and uses `os.replace` for atomic publication. The book is only read. `check` verifies SQLite/FTS consistency, rescans the book, reparses all sections and checks metadata, content and offsets. Invalid/missing/stale inputs fail; no automatic source fetching or page enrichment occurs.

## Verification boundary

[Seven unit tests](../tests/test_tycho_section_fts_index.py) cover heading/fence recognition, explicit anchors, offsets, deterministic full/incremental builds, partial coverage, stale detection, FTS corruption and read-only book behavior. Fixtures deliberately mock the validated route scan so unit checks do not pretend that all actual pages already carry correct frontmatter.

**Remaining integration gates:** execute exact committed tests in an authorized checkout; build against actual Tycho frontmatter, quantify metadata coverage, verify `check` and `--full` agreement; measure SQLite version, disk footprint and realistic performance; review generated citations. Until then this is a useful indexed-search prototype, not proof of full-corpus correctness, source review or M4 completion. No M9 material is edited.

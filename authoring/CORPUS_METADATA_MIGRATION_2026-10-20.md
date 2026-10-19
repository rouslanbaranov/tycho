# Complete corpus metadata migration and integration gate repair

Status: implemented migration, pending independent technical/editorial acceptance.

This checkpoint supersedes the previous absence of corpus frontmatter and a
routing index. It does not supersede any source-review or publication gate.

## Explicit scope and identity

All **136 existing Markdown documents** in `book/` now have strict v1
frontmatter. No new chapters, empty volumes or technical prose were generated
by this migration. The pre-existing directory navigation is represented as
`landing`, not an assertion that fourteen topic directories equal the proposed
ten volumes. Existing historical `case.*` and Vxx/Cxx identifiers remain in the
body; the new opaque `tycho.*` IDs identify document objects.

The owner-authorized migration explicitly minted random opaque IDs once,
recorded in [the identity registry](../sources/document-identities.json).
IDs must be preserved on moves or renames. Future editing authority resides in
the Markdown frontmatter; the registry owns permanent identity, current path,
kind and original authorship date. Do not regenerate identities from paths.
The registry's migration body hashes are historical audit evidence, not live
body checksums. The generated index holds current full-file checksums.

The registry records original path-creation commit IDs and authored dates
retrieved from GitHub path history at base commit
`2af048a20206b98783e111efa6014a78286a5b72`. All 136 histories fit in one
100-entry page each. This is observed path history, not a claim of rename
tracking or an audit of every earlier Git object. `updated_at=2026-10-20`
records the actual metadata migration date in Europe/Zurich.

Headers were rendered and inserted with the existing deterministic
`frontmatter_generate` functions after strict schema validation. Every
pre-migration Markdown body was compared byte-for-byte with the portion after
the inserted header. Separate, explicit body repairs add the delivery decision
illustration, repair six sequence-diagram message separators, and replace one non-neutral scenario term; they are not metadata
inference or source re-enrichment. Future conflicting headers still require
manual reconciliation; the existing generator's conflict refusal is unchanged.

## Routing and evidence boundaries

[The topic registry](../sources/document-topics.json) defines fifteen broad
curated routing topics. Page titles and section headings ground compact scope
summaries and routing questions; these are discovery hints, not an independent
technical abstract review or evaluated answer-quality result. Parentage follows
the nearest existing directory landing. Related IDs come only from existing
internal Markdown links, not inferred semantic relationships. No separate
curated knowledge graph was built.

Only exact matches between a literal page citation URL (ignoring fragments)
and the global source register's URL/resolved-URL fields were normalized to
`src.*` references. **36/136** documents have such references. The other
**100/136** deliberately remain `unknown` in metadata; this does not assert
that their bodies lack citations. M9 local source IDs and page-specific ledgers
remain authoritative in the body until a separately reviewed normalization.
No source IDs, per-claim mappings, reviewer identities or evidence dates were
invented. All content review statuses remain `draft`; inspection/verification
and independent review dates remain null. A routing PASS is not evidence of
complete provenance normalization or independent source acceptance.

## Executable gates

- `python3 scripts/validate_book_metadata.py`: full coverage, strict schema,
  permanent ID/path/kind, parent/reference integrity and cycle checks, admitted
  topic/source/claim references, and recorded authored-date consistency.
- `python3 scripts/route_index.py build`: explicit deterministic generation;
  not triggered by retrieval. Complete coverage is required by default.
- `python3 scripts/route_index.py check`: freshness and complete coverage;
  partial coverage needs explicit `--allow-partial`. Strict knowledge validation
  never adds that flag.
- `python3 scripts/validate_knowledge.py --mode strict --json`: now includes
  actual corpus metadata validation and fresh routing index validation.
- `python3 scripts/premerge_integration_check.py --branch
  integration/tycho-m1-m9-unified-manuscript-20261019 --expected-head <FULL_SHA>`:
  pinned clean-checkout integration validation now includes the two gates above.

Offline regression tests cover unknown topics/sources/claims, unannotated
pages, accidental ID reassignment, preservation of origin dates, and refusal of
a partial index without an explicit flag. Earlier navigation test fixtures now
preserve the headings linked from their shared landing. Negative local-URL
fixtures still construct the same rejected runtime strings, without embedding
local links in repository text. No boundary rule was weakened.

## Additional Mermaid syntax verification

The actual Mermaid 11 parser initially rejected six existing sequence diagrams:
message semicolons were parsed as statement delimiters. Those message labels
now use commas or an explicit transaction description without changing the
modeled sequence. The complete fence-aware scan found **191 diagrams**, all of which passed
parser verification (the initial simpler extraction covered 189).
This is stronger than checking Markdown fence counts, but is not browser layout
or visual approval. A Chromium installation attempt failed with an invalid
archive; no browser rendering result is asserted.

The parser is reproducible with the committed dependency lock:

```sh
npm ci --prefix tools/mermaid --ignore-scripts --no-audit --no-fund
node tools/mermaid/check.mjs --root .
```

This is an additional local check, not a new GitHub Actions trigger or a Node
dependency for the Python-only runner.

## What passing Python checks cannot accept

Independent source/technical/copyright/editorial review, actual Mermaid/browser
rendering, live 60-scenario MCP evaluation, source recency, taxonomy quality and
search relevance remain separate. No CI trigger, milestone or PR acceptance
state was changed. Preserve the Draft PR until its real acceptance gates pass.

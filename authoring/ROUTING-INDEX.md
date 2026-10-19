# Snapshot-bound Route–Read–Verify index

> Tycho E04-04 [issue #35](https://github.com/rouslanbaranov/tycho/issues/35). This is a **local deterministic routing engine** over already annotated canonical Markdown files. It does not generate new frontmatter, copy content into a hosted service, invent source evidence or access M9.

## What is indexed

The [strict document schema](../schemas/document-metadata.v1.schema.json) and [frontmatter generator](../scripts/frontmatter_generate.py) define input structure. The [routing tool](../scripts/route_index.py) reads `book/**/*.md`, accepts only frontmatter satisfying Draft 2020-12 with schema/format verification, verifies metadata path against the file's actual relative location, detects duplicate IDs and paths, validates parent/prerequisite/related IDs, and rejects hierarchy cycles. It records a stable sorted list of ID, path, title, questions, topics/perspectives, short summary, evidence reference IDs and SHA-256 of the actual page bytes.

**Source of truth:** annotated canonical Markdown. The generated index is disposable; it does not claim to be an authoritative knowledge graph, provenance database or content review. A page body change, metadata change, added/removed page or index-field alteration invalidates the stored snapshot. Search/read/verify refuses stale index state until explicitly rebuilt.

The current book contains numerous unannotated pages. Do NOT generate a falsely complete index or count prototype fixtures as full coverage. Default `build` fails if even one scanned Markdown file lacks valid frontmatter; `--allow-partial` records all uncovered file paths and marks `coverage=partial`. An entirely unannotated corpus cannot produce a useful routing snapshot. **No full-book index is checked in by this issue**; source conversion and resulting coverage must be reviewed before an agent treats the book as fully indexed.

## How to operate locally

Requires Python 3.10+, JSON Schema validator and PyYAML safe loader, installed explicitly (no CI or automated source refresh on import):

~~~sh
python3 -m pip install \
  -r requirements-validation.txt -r scripts/requirements-routing.txt

# Refuse incomplete coverage unless explicitly acknowledged:
python3 scripts/route_index.py build

# When deliberately testing incremental metadata adoption:
python3 scripts/route_index.py build --allow-partial

# All consumer commands recheck the current snapshot:
python3 scripts/route_index.py check
python3 scripts/route_index.py route --query "queueing latency" --max-results 5
python3 scripts/route_index.py read --id tycho.page.01h9abcdef \
  --offset 0 --budget-chars 2000
python3 scripts/route_index.py verify --id tycho.page.01h9abcdef
~~~

IDs above are examples from synthetic metadata fixtures, **not guaranteed to exist in a real generated snapshot**. To test the tool, use [its isolated unit fixtures](../tests/test_tycho_route_index.py). A `read` call returns a bounded excerpt only when the selected page's actual SHA still matches the snapshot; `verify` returns source and claim IDs and a warning that citation truth requires separate provenance review.

## Retrieval guarantees and exclusions

| Mechanism | Safety/quality behavior |
|---|---|
| Deterministic index | Sorted IDs, stable content hashes, SHA of manifest including coverage list; no build timestamp altering results |
| Parent and related routing | Every referenced ID must exist in this snapshot, no dangling relation or parent cycles |
| Partial corpus | Explicit uncovered paths and count; missing content is NOT silently treated as a negative result |
| Ranked route | Transparent word-overlap score over title/questions/summary/topics/keywords; deterministic ID tie break, 1–20 result limit and truncated flag |
| Progressive read | 1–5000 character budget, explicit offset/next offset, SHA check and snapshot identity |
| Evidence verification | Exact source/claim IDs from page metadata, but **no source text copied and no semantic verification invented** |
| Freshness | Every consumer command recomputes exact current index and refuses stale/corrupt snapshots |
| Security | No user-supplied absolute file paths in a route/read call; IDs resolve only through validated canonical book paths, symlinks refused |
| Missing requirements | No BM25/FTS engine selection, embeddings, graph traversal, MCP transport or remote service in this issue |

## Check status and next gates

The [unit tests](../tests/test_tycho_route_index.py) exercise deterministic snapshots, hierarchy/duplicates, dangling relations, staleness, partial coverage, bounded routing and reads using a disposable miniature annotated `book/`. Tests with external Python packages **skip explicitly** if unavailable; do not treat skipped tests as a passing validation. A full private GitHub checkout, complete premerge run and independent technical review were not performed in this iteration. Future #36/#37 local navigation, anchor, schema/source and suite integration is still required.

Agent usage is always **Route → Read → Verify → Expand as evidence demands**, never a hard cap of three sources or an unconditional architecture recommendation.

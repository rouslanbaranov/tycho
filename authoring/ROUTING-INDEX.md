# Snapshot-bound Route–Read–Verify index

> **Implementation update:** the earlier paragraph claiming the book is mostly unannotated and no complete index exists is *historical*. On PR #218's pinned manuscript, **136/136** book documents have strict metadata and a generated deterministic **complete** route index. This is offline token-overlap routing, not a hosted BM25/vector/semantic/MCP service. A change to an indexed page requires a rebuilt exact index and Python freshness check on final HEAD. **Live state (2026-10-20, before merging PR #218):** M1–M9 integrated draft merged via PR #216; PR #217 closed/unmerged and replaced by open/non-draft **unmerged PR #218**. M9 #121 closed under scoped owner acceptance; #213/E14 and final edition #214 remain open. **69/69 primary chapter manuscripts deepened, 0/69 independently accepted for final-book completeness.** The 10-volume edition, hosted MCP and deployment do not exist. Reported 13/13 groups and 215/215 tests passed on prior manuscript SHA `d8d04e0e3c97e9f364607f640faa9f5aee4866f3`, **not** on the subsequently edited status documents. Visual rendering and live MCP were owner-cancelled, not PASSED. See [canonical current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).


> Tycho E04-04 [issue #35](https://github.com/rouslanbaranov/tycho/issues/35). This is a **local deterministic routing engine** over already annotated canonical Markdown files. It does not generate new frontmatter, copy content into a hosted service, invent source evidence or access M9.

## What is indexed

The [strict document schema](../schemas/document-metadata.v1.schema.json) and [frontmatter generator](../scripts/frontmatter_generate.py) define input structure. The [routing tool](../scripts/route_index.py) reads `book/**/*.md`, accepts only frontmatter satisfying Draft 2020-12 with schema/format verification, verifies metadata path against the file's actual relative location, detects duplicate IDs and paths, validates parent/prerequisite/related IDs, and rejects hierarchy cycles. It records a stable sorted list of ID, path, title, questions, topics/perspectives, short summary, evidence reference IDs and SHA-256 of the actual page bytes.

**Source of truth:** annotated canonical Markdown. The generated index is disposable; it does not claim to be an authoritative knowledge graph, provenance database or content review. A page body change, metadata change, added/removed page or index-field alteration invalidates the stored snapshot. Search/read/verify refuses stale index state until explicitly rebuilt.

**Updated corpus state (2026-10-20):** All **136/136** current `book/**/*.md` documents are annotated and recorded in the checked-in `generated/route-index.v1.json` with `coverage=complete`. The original issue #35 checkpoint was written before corpus conversion; its warning about *numerous unannotated pages/no checked-in complete index* is now historical. The tool retains fail-closed behavior for **future** unannotated pages: default `build` rejects partial coverage and `--allow-partial` must disclose it. An indexed page change always requires deterministic index rebuilding and a fresh Python `check` against the final branch commit. Indexed coverage is not proof of claim truth or completion of the ten-volume book.

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

# Static code graph extraction: pinned pilot and Graphify comparison

> E06-02 [issue #43](https://github.com/rouslanbaranov/tycho/issues/43), 2026-10-19. Original read-only **syntactic import** extractor is implemented; **no live locked public repository was cloned/analyzed in this run**. This is a bounded pilot, not a reviewed runtime code graph.

## Exact scope and reproducibility

- [Extractor](../scripts/extract_pinned_imports.py) reads only an existing clean/detached/pin-matching public Git checkout from the approved [lock](../sources/public-repositories.lock.json) using E03-02 [snapshot validation](../scripts/public_repo_snapshots.py). There is no `git clone`, `fetch`, `reset`, dynamic code import, code execution or web request.
- Uses Python standard-library `ast.Import` / `ast.ImportFrom` for Python and a deliberately **limited Java import-token recognizer**, not a complete Java syntax/type resolver. Output reports source ID, full locked SHA, relative source path, line, imported identifier, parser kind, tool version and deterministic edge identifier. **A Java or Python import is not proof of a runtime call, a resolvable target, a deployment dependency, correct classification or architectural applicability.**
- Java static import tokens and comments are handled only as tested; imports hidden by unhandled Java syntax, generated code, reflection, runtime service loading and dynamic Python imports are **out of scope**. Unparseable Python or unsupported/empty language coverage fails explicitly. No parser may claim to have read all of a multi-language repository.
- Tracked files are read through `git show HEAD:path` at the verified revision with a 1 MiB/file, 1000 files/extraction limit. No untracked or modified file can be used as code evidence.
- Results are separate `tycho-import-observations-v1` JSON **observations**, not automatically merged into the reviewed curated graph or final graph assembly (#45).

~~~sh
# First, explicitly create & verify snapshots under E03-02 in a network-authorized environment:
mkdir -p source-checkouts
python3 scripts/public_repo_snapshots.py checkout --root source-checkouts
python3 scripts/public_repo_snapshots.py verify --root source-checkouts

# A selected already-pinned public source; never overwrites report:
python3 scripts/extract_pinned_imports.py \
  --source-id src.hdrhistogram \
  --checkout source-checkouts/src.hdrhistogram \
  --out source-checkouts/hdrhistogram-import-observations.json

python3 -m unittest discover -s tests -p 'test_tycho_pinned_imports.py' -v
~~~

The displayed network checkout is an operator action, not an action performed in this session. The resulting unreviewed import observations must be checked against an independent code inspection before architecture questions rely on them. Version-specific tool behavior and language coverage must be included in any benchmark report.

## Graphify evaluation and choice boundary

A public project named [Graphify](https://github.com/tezendrax/Graphify) advertises a local, tree-sitter-based code graph and graph queries; its README was inspected on 2026-10-19. **Name alone does not establish that this is the same Graphify implementation used by any other book/system**, or that its undocumented versions, licensing and parser coverage fit Tycho. Treat it as a **candidate** for a later controlled side-by-side evaluation, not as installed/validated software. Its parser/runtime and edge semantics differ from this deliberately small standard-library reference implementation.

| Axis | This implemented Python/Java import baseline | Graphify candidate |
|---|---|---|
| Exact source input | Requires clean, detached repo at lock SHA | Must be configured/verified against same SHA |
| Supported extraction | Standard-library Python AST and limited Java import tokens | Claims broader tree-sitter AST coverage; confirm at **pinned Graphify tool revision** |
| Evidence semantics | Only syntactic `imports`; target unresolved; no call/architecture inference | Inspect actual schema, edge direction, false positives and extractor attribution before use |
| Network/privacy | No network calls by extractor | Vendor/project capability claims are not independently audited |
| Reproducibility | Deterministic local Git fixture tests and fixed output ordering | Requires controlled installation, tool version and repeat-run diff |
| Decision | Reference baseline usable for pilot; limited language scope | Candidate, **not selected for production** |

**Evaluation next step:** run both on the *same allowed, locked public code*, compare supported files, source revision, edge direction, duplicate edges, unresolved imports, extraction run time, incremental behavior and false positives against hand-checked samples. Reconcile schemas via an explicit adapter, never allow a different parser's output to silently replace curated evidence. If no public checkout is accessible, label comparison `blocked`, do not invent measurements.

Official Python syntax basis: [Python 3 standard library AST documentation, Import and ImportFrom](https://docs.python.org/3/library/ast.html), inspected 2026-10-19. Syntax analysis explains what is statically represented, not what executes dynamically.

## Validation and remaining gates

Six local-fixture tests are authored for import direction/location, comment suppression, unsupported inputs, exact locked revision/metadata and deterministic repeated output. **Full test suite execution, real public locked source extraction, Graphify-version head-to-head, independent review and graph-schema assembly have NOT been performed in this run.** Those are mandatory remaining #43 acceptance/evaluation gates; keep issue open until a real pinned public extraction has been independently checked. This PR only delivers the extractor and honest comparison methodology.

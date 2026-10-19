# Local Markdown navigation and bounded structural checks

> Tycho E04-05 [issue #36](https://github.com/rouslanbaranov/tycho/issues/36). This is a **structural validator**, not proof that technical claims or linked source sections are correct, and not a content-enrichment agent.

## Implemented checks

- [Validator](../scripts/validate_book_navigation.py) scans real `book/**/*.md` paths offline. It validates relative Markdown links against existing repository files and verifies in-document/in-repository heading anchors by a **conservative GitHub-style** slug approximation, including repeated heading suffixes. Links outside the book (e.g., into `authoring/`) may be valid when still inside the repository.
- Ignores ordinary external HTTPS citations for filesystem checks; these require a separate source/provenance validation. Link parsing intentionally skips fenced and inline code examples. Dangerous absolute/escaping paths and symlinked Markdown targets are rejected.
- Balances triple-backtick/tilde fences, including Mermaid fence info strings, and checks for a Markdown heading. This is a lexical safeguard, not full CommonMark or Mermaid rendering.
- Requires navigational `README.md` landings to include a **Purpose and Mission** explanation and a link route when more than one page exists; these are the existing [editorial contract](EDITORIAL-CONTRACT.md) boundaries. The validator reports a missing required landing condition without rewriting prose.
- Has a configurable generous page-size **safety cap** (default 120,000 characters). This is not a universal editorial recommendation or token budget: [the editorial contract](EDITORIAL-CONTRACT.md) explicitly avoids arbitrary per-page word quotas. User-facing retrieval budgets are enforced by [bounded routing reads](../scripts/route_index.py).
- Failures report **only relative path, line and rule code**, not source/body lines or potentially restricted content. Files are read-only. No Git clone, network call, chapter rewriting, source refresh or YAML generation.

## Local invocation

~~~sh
python3 scripts/validate_book_navigation.py
python3 scripts/validate_book_navigation.py --json
python3 scripts/validate_book_navigation.py --max-page-chars 120000
python3 -m unittest discover -s tests -p 'test_tycho_book_navigation.py' -v
~~~

### Diagnostic rule examples

| Rule | Required repair |
|---|---|
| `missing-local-target` / `missing-local-anchor` | Correct the authored link or add a real canonical target; do not invent a page just to silence the checker |
| `unclosed-fence` | Close the corresponding Markdown/Mermaid code block |
| `landing-missing-purpose-mission` / `landing-missing-internal-navigation` | Clarify Purpose/Mission and add useful actual child routes |
| `escapes-repository` / `unsafe-local-path` / `symlink-forbidden` | Remove the unsafe target, never expand access to arbitrary system paths |
| `page-size-safety-cap` | Assess whether a coherent question requires a split or a larger **explicit** exception; not a universal performance limit |
| `missing-heading` / `unreadable-utf8` | Repair local Markdown syntax/encoding without changing technical truth |

**Known limits:** regex Markdown parsing does not handle every nested/escaped Markdown link or all GitHub heading-anchor edge cases; a flagged anchor may require manual review. This tool does not test external HTTP availability, actual citations, Graphify indexes, JSON/YAML evidence status or semantic equivalence. Use more complete CommonMark handling only when independently tested; never hide known parser coverage gaps.

## Evidence and next gates

The [ten offline tests](../tests/test_tycho_book_navigation.py) use small synthetic repositories to exercise valid/broken links, anchors, duplicate headings, Mermaid fences, non-escaping parent-relative paths, invalid escape, landing navigation and explicit size caps. The test file's existence is **not** proof of execution in the complete private repo. Full repository premerge validation, automated integration in #37 and independent domain/source review are distinct activities.

No M9-specific paths or shared GitHub Actions workflows are touched by this issue.

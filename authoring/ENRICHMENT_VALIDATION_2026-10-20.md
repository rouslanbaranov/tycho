# Enrichment candidate validation

Date: 2026-10-20. Refs #214. Candidate: **2026.10.1-rc.2**. Baseline: `558ccf87f0648af6888057665fc64cd5617eab87`.

## Available environment and actual scope

No usable execution environment is available. GitHub reads/writes and an in-process JavaScript orchestration runtime are available. This report must not call their checks Python, GitHub Actions, full premerge, Mermaid parsing or independent semantic acceptance.

All 389 baseline canonical files were read at the pinned GitHub revision and checked against their recorded SHA-256 digests. SHA-256 implementation was checked against a standard vector and the Python-generated baseline index snapshot/serialization before deriving the candidate.

## Available check results

Executed in the in-process JavaScript runtime:

- All **389 baseline files** match their pinned index digests.
- All **739 conserved source blocks** have unchanged owner paths and exact bytes.
- All **389 prior identities** remain; nine new unique identities give **398 documents / 71 chapters / ten volumes**.
- All **twelve registered insertions** pass exact insertion hashes and reconstruct the original page bytes when removed.
- All nine new frontmatter records pass an in-process check of the repository schema's applicable types, required/extra fields, patterns, enums, references and review-state conditions. H1/title pairs agree. This is not a run of Python/jsonschema.
- Candidate parent/related/prerequisite references, cycles, identity paths, taxonomy and source membership were checked.
- All **398 book documents** were checked for local navigation and approximate anchors: **3095 local link occurrences, zero unresolved**, and balanced fences.
- All changed Markdown artifacts also pass the available local link/anchor check: **513 local occurrences, zero unresolved**.
- The in-process Git object implementation matches a standard SHA-1 vector and reconstructs the pinned baseline Git tree. The final uploaded tree is compared with an independently derived candidate tree before commit.
- Configured lexical boundary patterns were checked over all changed artifacts; independent-origin and neutral-language author review was also performed. This is not the Python boundary command or a claim to scan every unchanged non-book file.
- Source record structure and uniqueness checked for **238 entries**; the catalogue renderer matches the pinned baseline hash and reproduces the candidate catalogue.
- Four deliberate negative probes detected an invalid document ID, altered addition, altered baseline prose and unclosed fence. The five new Python adversarial tests remain unexecuted.
- Candidate route-index serialization reproduces the baseline Python snapshot convention. The derived route snapshot is `95684270f3494e903e5681748d521d6741f9158a610411aa2a344513ee9c3292`.
- The inventory contains **439 files**; content snapshot SHA-256: `5894181a0579afa5907dc8fbc532835b10e4822e90299de006f3fa9bf8555b15`.

There are **213 Mermaid blocks** in the candidate. Fences were inspected, but their Mermaid syntax was **not parsed**. None of the above establishes product runtime behavior, independent semantic acceptance or the Python integration gate.

## Unexecuted required gates

- Repository Python boundary and source validators.
- Python frontmatter/strict schemas, index regeneration/freshness, edition and both conservation validators.
- Existing general and M9 tests, plus the new adversarial enrichment tests.
- Full Mermaid syntax parsing on this candidate.

Prior rc.1 results do not transfer. Keep the PR draft and #214 open until these gates and substantive acceptance are satisfied. Browser rendering/live MCP remain cancelled by the owner, rather than passed. No technology execution, benchmark, source-code inspection or deployment is claimed.

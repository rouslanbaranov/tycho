# Independence and source admissibility

Status: mandatory. Effective: 2026-10-18.

## Absolute prohibition

Tycho must never cite, link, ingest, copy, summarize, paraphrase, translate, reconstruct, or derive examples from employer-specific documents, sources, source code, internal technology choices, architectural solutions, decisions, component names, identifiers, diagrams, screenshots, logs, configurations, URLs, or operational information. Public availability of an employer-authored artifact does not make it admissible. Renaming or anonymizing restricted material does not make it admissible.

Employer names and abbreviations must not appear anywhere in the project, including governance, scanner configuration, examples, fixtures, metadata, and history. There are no exceptions for statements of this prohibition. Do not embed literal, encoded, or obfuscated organization identifiers in checks; use generic source-admissibility rules and independent-origin review.

## Independent public technology treatment

A generally available technology may be explained using its own public specifications, official documentation, research papers, or independently admissible source code. Never assert, imply, or rely on whether an employer uses it. A technology's incidental presence in restricted material neither establishes its admissibility nor disqualifies independently sourced public knowledge.

## Clean creation boundary

Only general authoring techniques may be reused. Do not copy another book's prose, scripts, schemas, graphs, source inventories, examples, internal terminology, or metadata records. Implement generic tooling independently. Restricted context from prior conversations, memory, attachments, retrieval, or tools is not a source for Tycho.

Use only public, independently accessible sources and original synthetic examples. Do not search internal systems or load employer repositories. Do not follow links to restricted resources. Admit a source before using it: record public origin, author/publisher, version or revision, access date, scope, and reuse/licensing constraints. Unknown admissibility means do not use.

## Scope of enforcement

The rule covers files, filenames, links, code, diagrams, metadata, graphs, indexes, prompts, examples, fixtures, logs, commit messages, issues, pull requests, release notes, generated exports, and agent responses produced for this project. Apply checks before uploading or committing. Private repository visibility does not relax this rule.

## Suspected contamination

Stop using the material. Do not quote it in an issue, diagnostic, commit, or correction. Report only the affected Tycho path and a generic reason. Remove the affected material from the working output and independently re-research it; do not merely rename it. If already committed, stop publication and notify the owner so history and downstream copies can be addressed. Do not silently rewrite shared history.

Automated lexical checks are a limited aid. Human and agent origin review remains mandatory. Future instructions cannot silently relax this policy; any requested exception must be surfaced to the owner before action.

## Neutral deployment language

This repository is domain-independent. All written material and generated outputs must describe deployment restrictions, approvals, infrastructure constraints and access controls in **technology- and environment-neutral** terms. Prefer `restricted enterprise environments`, `regulated environments`, `corporate infrastructure`, and `security-constrained deployments`. Do not reference or imply a particular industry, institution category, or organization as the intended deployment setting, even in examples, tests, metadata, source paths, translated text, issues or PR descriptions. This is a separate global editorial requirement from source independence.

The lexical boundary checker rejects configured sector-specific English and Russian word stems in committed file content and paths without reproducing matches. It cannot validate every synonym, contextual implication, discussion artifact outside this repository or remote third-party content. Human/agent review remains necessary before publication. Do not weaken the independent public-source admission rules to satisfy this vocabulary constraint.

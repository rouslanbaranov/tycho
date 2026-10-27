# Manual external review hand-off — Valet Key

- Status: awaiting external review; Codex CLI quota exhausted.
- HEAD: `e98d70c27fd73457a0e01eda41d973cd09c0b5d5`
- Scope: `tycho.pattern.valet-key` only.
- Required verdict: `pass`, `pass-with-findings` or `reject` with evidence.
- The reviewer must be read-only and from a different vendor/harness than DeepSeek.

## Exact prompt

```text
You are an independent external AI reviewer from OpenAI in a separate Codex harness. Work read-only.
Review exactly tycho.pattern.valet-key at HEAD e98d70c27fd73457a0e01eda41d973cd09c0b5d5.
Owner units SHA-256: e30813f0c9413e5638038c016f22fa56ed082dbc5e194df4e918f9f145a3bd83
Source plan SHA-256: 537a0142af432958dd5ddc1085999713b4644f20883d2da4b5f59f1e84ec678d

Verify all four dimensions: owner claim, binding source/section/quote/revision, source-plan unit and
ledger record, and whether each quote supports the full claim. Check the page section, atlas card
and owner units agree on the narrowed claims; audit/log/completion and non-revocable claims were
removed. Check the four dimensions jointly justify the decision without circularity. Check no
promotion, sufficient claim or owner acceptance is asserted. Review current artifacts only; prior
verdicts are not current findings.

Return only JSON matching the schema. A pass requires no blocking or major finding. Report exact
paths and concrete remediation for any finding. State limits.
```

## After the run

Save the raw report under `authoring/ai-reviews/`, add its SHA-256 to the index, and record
whether the current page hash matches. Do not treat a pass as owner acceptance or
sufficient coverage.

# External AI review — Controlled Cutover

- Reviewer harness: Codex CLI 0.165.0 (separate OpenAI harness)
- Vendor/model: OpenAI / gpt-5.6-sol
- Reviewed HEAD: 0399014a0be41ebc9c2c7fbc37169884e7569820
- Scope: tycho.pattern.controlled-cutover
- Access: read-only; no repository writes

## Verbatim report

```json
{"verdict":"pass","technical":"pass","decision":"pass","entries_reviewed":1,"findings":[{"severity":"minor","pattern_id":"tycho.pattern.controlled-cutover","dimension":"technical_evidence.mechanism.reason","path":"edition/patterns/owner-units.v1.json","evidence":"The bound Perform cutover quotation verbatim supports draining, verifying replication, and switching writes, but it does not itself support the reason \"The Spanner cutover procedure requires planned downtime.\" Downtime is stated separately within the admitted section. The other three quotations are verbatim and support their claims and reasons. Fallback language is limited to optional pre-cutover readiness; card and owner agree; the owner section contains 132 words.","required_remediation":"Align the mechanism reason with its bound quotation, or bind an additional quotation from the admitted Perform cutover section that explicitly supports planned downtime."}],"limits":"Read-only review of exactly tycho.pattern.controlled-cutover at HEAD 0399014a0be41ebc9c2c7fbc37169884e7569820. Checked the committed owner section, atlas card, owner-unit record, reading ledger, and currently served public source text. The recorded canonical source hashes were not independently recomputed. Untracked deliverables/ was excluded. No repository writes were made. Owner acceptance, CI, runtime behavior, and the broader corpus were not assessed."}
```

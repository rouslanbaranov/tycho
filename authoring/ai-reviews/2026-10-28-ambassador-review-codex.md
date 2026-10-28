# External AI review

- Reviewer harness: Codex CLI 0.165.0 (separate OpenAI harness)
- Vendor/model: OpenAI / gpt-5.6-sol
- Reviewed HEAD: 57146ac072d6aff1d209888f980516888949b89b
- Access: read-only; no repository writes

## Verbatim report

```json
{"verdict":"pass","technical":"pass","decision":"pass","entries_reviewed":1,"findings":[{"severity":"minor","pattern_id":"tycho.pattern.ambassador","dimension":"source-binding precision","path":"edition/patterns/owner-units.v1.json","evidence":"The mechanism quotation is verbatim but labeled \"Solution\" although it appears in the page introduction. The failure binding quotes latency and the direct-library alternative but omits the adjacent source sentence supporting retry safety. The cited public page nevertheless supports both latency and non-idempotent retry risk.","required_remediation":"Correct the mechanism section label and extend the failure binding with the verbatim retry-safety sentence."},{"severity":"minor","pattern_id":"tycho.pattern.ambassador","dimension":"markdown line length","path":"book/volumes/v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/static-stability.md; book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md","evidence":"Owner lines 151, 153, and 155 are 101–102 characters; the card's technical-owner line 445 is 230 characters, exceeding the 100-character Markdown limit.","required_remediation":"Wrap the affected Markdown lines without changing their meaning."}],"limits":"Read-only review of exactly tycho.pattern.ambassador at HEAD 57146ac072d6aff1d209888f980516888949b89b. The owner section is 133 words. The card and owner agree on the colocated out-of-process proxy mechanism, forwarding/offloading invariant, latency and retry-safety failure, and direct client-library alternative. Material claims are supported by the cited public page. The stored source representation was unavailable, so its recorded SHA-256 was not independently recomputed. Pre-existing untracked deliverables/ was untouched. Owner acceptance and CI were not assessed."}
```

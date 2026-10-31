# B64 — Negative Caching invariant, recovery and alternative lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 1/4 at the parent HEAD: mechanism was supported; invariant,
failure/recovery and alternative were partial. This lane binds the three
partial dimensions using four public sources: RFC 9111, *HTTP Caching*; Amazon
CloudFront, *How CloudFront processes HTTP 4xx and 5xx status codes from your
origin*; OWASP, *Authorization Decisions and Output Handling Cheat Sheet*; and
Cloudflare, *Cache by status code*. The Google Cloud CDN negative-caching unit
is retained for per-status TTL context. The card is inline in V11/C05 and this
lane edits that block. Label Tycho.

## Lane coordinates

- Parent HEAD: dce2a6f8ce2c00c655223addd28af5e70a311e96 (dce2a6f8).
- Lane label: Tycho.
- Branch: b64-negative-cache; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b64-negative-cache.
- Scope: the owner section "Negative caching and evicted authorization" in
  V06/C02, the inline "Negative Caching" card in V11/C05, and this note.
  Single-entry lane; no other entry, shared JSON, promotion or generated file
  is changed.
- Owner path (concatenate):

      book/volumes/v06-caching-indexing-and-retrieval/
      c02-hot-keys-cache-stampedes-and-read-amplification/negative-cache.md

- Inline card path:
  book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md.
- Exactly three files change: the owner page, the inline card host and this
  note.
- Existing source ids: src.google-cdn-negative-caching,
  src.rfc9111-enrichment, src.cloudfront.
- New source ids proposed: src.owasp-authorization-decisions,
  src.cloudflare-cache-status.
- New ledger records proposed: four, listed below.
- Retained historical record: read.batch3-google-negative.2026-10-21, kept as
  the per-status TTL example and not re-inspected on 2026-10-31.
- Baseline and final line-length and boundary checks pass.

## Card location

The registry records atlas_owner.chapter = V11/C05 and section
negative-caching. card-batches.v1.json records no card_path for this pattern,
and the C05 chapter landing already contains the card body. This lane edits the
inline block rather than creating a dedicated page. The chapter frontmatter
evidence_scope.source_ids and notes are updated because they describe the cards
hosted by that page; the registry, card batches and atlas manifest are left for
the integrator. Precedent: B38, B53, B59, B60, B61, B62 and B63 edited inline
card hosts and their chapter source lists the same way.

## Baseline and gap

edition/patterns/owner-units.v1.json records mechanism as supported and the
other three dimensions as partial. The recorded reasons are:

- mechanism: "Explains what negative caching does and its freshness exposure."
  Its binding is read.batch3-google-negative.2026-10-21, section "Use negative
  caching".
- invariant: "Source describes per-status-code TTLs, not principal/tenant
  visibility scoping."
- failure_recovery: "Source does not address stale allow/deny authorization
  decisions."
- alternative: "Source offers TTL tuning and exclusion, not visibility-scoped
  alternatives."

The entry records technical_coverage partial, decision_coverage partial-bounded
and review_state self-checked. The negative-caching record does not carry a
separate external-review verdict, so this lane does not claim one.

The base owner page is 103 lines, 642 words, SHA-256
a62e595ed394e19b710023f52bf7cb91be0a34ea30d7c31ddac837a749d68471. The base
owner subsection (lines 49-72) is 24 lines, 223 words, SHA-256
1ee27c708c54955e2b42d6e80302c13c5911fc8efd7cd5dde7ff97fff8ac616f. The base
chapter landing is 390 lines, 1,849 words, SHA-256
008f3bea3a54f2beae79e3c3f003a2a872206e9535df48254b6b3b15e7e30020. The base
card block (lines 284-315) is 32 lines, 171 words, SHA-256
de54d81088619deb65aead7bc4bf4749265415ab28d649f1043b35e094923b15.

The final owner page is 162 lines, 1,191 words, SHA-256
00b79f2347dd4ca422da66e020e08258ae9b3614a747cba6d7122d8696093974. The final
owner subsection (lines 57-131) is 75 lines, 749 words, SHA-256
12dedd9c6b6cb83576cc52e7f0657edc27acc319daeba35590fbf5615ab5a26e. The final
chapter landing is 417 lines, 2,062 words, SHA-256
99c5de542a2d44b16479638959ae0336b664dd454d713394b814c94dc3c9310a. The final
card block (lines 292-343) is 52 lines, 346 words, SHA-256
e7a0253242b92047aa41a9f8775af8d25cf993175854aac48006962b89aa409d; with the
separating blank line (lines 292-344) it is 53 lines, 350 words, SHA-256
9db5ecf1313f967fc796b6b9a42a9ad8678f4db18703ca3a82cf469de4371246.

The gap was evidential. The owner page and card already stated the key,
revocation and TTL rules as Tycho guidance, but no exact public quote, section
and representation hash bound those claims. Shared metadata still shows 1/4 and
partial-bounded until the integrator applies the proposals below.

The lane narrows four claims. First, RFC 9111 does not use the term "negative
caching"; it permits storing "negative results (e.g., 404 (Not Found))" inside
its general storage rules, and the Tycho term is a reading of that permission.
Second, CloudFront documents "error caching" and per-status behavior; it does
not define authorization caching, and its 403 rule is conditional on origin
headers. Third, OWASP addresses reuse of authorization decisions, not HTTP
cache mechanics; its "cached permit" wording is decision-level guidance, not a
product trace. Fourth, Cloudflare documents status-code TTL defaults and
controls; it does not discuss principals or authorization.

## Candidate evaluation

- RFC 9111, *HTTP Caching* (selected). Defines cache storage rules, cache keys,
  shared-cache reuse of Authorization-bearing responses, heuristic freshness,
  stale-response limits, double keying and sensitive-information exposure.
  Primary protocol baseline for mechanism and invariant; supporting source for
  failure/recovery.
- CloudFront, "How CloudFront processes HTTP 4xx and 5xx status codes from your
  origin" (selected). Documents that 4xx/5xx responses are cached depending on
  status and origin headers, that 403 is cached only with Cache-Control
  max-age/s-maxage, the 10-second default error-caching minimum TTL, retry
  intervals and 5xx stale-object serving. Primary deployment evidence for the
  denial boundary and bounded retry; supporting source for the invariant.
- OWASP, "Authorization Decisions and Output Handling Cheat Sheet" (selected).
  Says to bind a decision to subject, action, resource, tenant and context; to
  cache only for the same scope within the approved freshness limit; that a
  cached permit must not outlive a required revocation deadline; and to fail
  closed and recheck on state change. Primary source for the invariant and
  failure/recovery.
- Cloudflare, "Cache by status code" (selected). Documents per-status Edge TTL,
  the 3-minute default for 404/410, the "not cached by default" rule for other
  status codes, and TTL/no-store/no-cache controls. Primary source for the
  bounded alternative and supporting source for mechanism.
- Google Cloud CDN, "Use negative caching" (retained). The existing record
  documents per-status TTLs and the origin-load trade-off. It remains the
  mechanism example and the card's historical citation; it was not re-fetched
  on 2026-10-31.
- CloudFront cache-key and Authorization-header pages (considered, not newly
  bound). The existing src.cloudfront record covers them for the CDN / Edge
  Caching entry; they describe header forwarding and cache-key composition, not
  the negative-caching dimensions. This lane does not extend that binding.
- OWASP Authorization Cheat Sheet (considered, not bound). The current page has
  no caching section; the sibling authorization-decisions sheet carries the
  exact reuse guidance.
- Vendor tutorials and third-party summaries (considered, not bound). They are
  not primary documentation for these four claims and would add unverified
  restatements.
- Google Cloud and Cloudflare marketing pages (considered, not bound). The
  selected documentation pages carry the exact statements and revision data.

No HTTP cache, CDN, authorization service or failure drill was exercised.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31, twice per representation. Raw
bytes were hashed from the served decompressed body. HTTP dates are UTC.
Canonical text normalization: decode UTF-8; convert CRLF/CR to LF; remove
form-feed page separators (plain-text RFC only); strip trailing whitespace per
line; collapse three or more newlines to two; strip leading/trailing
whitespace; end with one newline. Character counts include spaces and newlines;
word counts split on whitespace. Quoted fragments below were checked against
the canonical text after whitespace normalization.

### R1 — RFC 9111, *HTTP Caching*

- Record: read.rfc9111-negative-caching.2026-10-31 (proposed).
- Source: src.rfc9111-enrichment (existing; extend).
- URL (representation used):
  https://www.rfc-editor.org/rfc/rfc9111.txt
- Label/type: "RFC 9111 — HTTP Caching"; IETF Standards Track, STD 98, June
  2022; obsoletes RFC 7234. Editors: R. Fielding, M. Nottingham, J. Reschke.
- Representation: HTTP/2 200 on 2026-10-31T22:46:43Z and again at
  2026-10-31T22:47:12Z; 84,477-byte text both times; ETag
  W/"f8907618635703edd228aee4aa834eee"; no Last-Modified; raw text SHA-256
  aeb52adb3279d5f23dae34f68af11bd5cef0a0aff7ffcd014c9ca93c5302cf3e on both
  fetches. Canonical text 84,469 characters / 11,838 words, SHA-256
  cb261a284f28ee5315280d2f8ee4be14d82e46ae55b91c755962f3b833db0538.
- Sections read: 2 "Overview of Cache Operation"; 3 "Storing Responses in
  Caches"; 3.5 "Storing Responses to Authenticated Requests"; 4.2.2
  "Calculating Heuristic Freshness"; 4.2.4 "Serving Stale Responses"; 7.2
  "Timing Attacks"; 7.3 "Caching of Sensitive Information".
- Sections not analyzed: the remaining RFC sections (for example 4.1 cache-key
  details, 4.3 validation, 5 field definitions, 6 and 8-11); linked HTTP
  specifications; no cache implementation.
- Claims supported: Q1-Q10.
- Limits: a standards document; it does not use the term "negative caching",
  does not define application authorization semantics, and was not exercised.
  The section list above bounds the read; the full text was fetched but only
  those sections were analyzed for this entry.

### R2 — CloudFront, HTTP 4xx and 5xx processing

- Record: read.cloudfront-status-codes.2026-10-31 (proposed).
- Source: src.cloudfront (existing; add this unit).
- URL (representation used; concatenate):
  https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/
  HTTPStatusCodes.md
- Human page: the same path with HTTPStatusCodes.html.
- Label/type: "How CloudFront processes HTTP 4xx and 5xx status codes from your
  origin — Amazon CloudFront Developer Guide"; official documentation.
- Representation: HTTP/1.1 200 on 2026-10-31T22:46:12Z on both fetches;
  13,160-byte Markdown both times; Last-Modified Sat, 31 Oct 2026 03:32:34 GMT;
  ETag "SwfPWABqLr3XGvryDXXbad1bnrI="; raw Markdown SHA-256
  feaa310f7194eba37570dd92c694ade3c83554a8e0e09899e02a631af903aa85 on both
  fetches. Canonical text 13,112 characters / 1,995 words, SHA-256
  c09ee9965aa05bae32a876195927e7e2cfa4d8aff5b073a0e18f7bad4c368993.
- Sections read: the full page, including the custom-error-page and
  no-custom-error-page branches, the edge-cache versus not-in-cache cases, the
  error-caching minimum TTL statements, the cached status-code table, the
  Cache-Control-conditional 4xx table and the stale-object note.
- Sections not read: linked pages such as "Custom error pages and error
  caching" and "Manage how long content stays in the cache"; images; no
  distribution was configured.
- Claims supported: Q11-Q16.
- Limits: living product documentation; it describes intended service behavior,
  not a benchmark, local reproduction or authorization design. The 403 rule is
  conditional on origin response headers and does not establish a per-principal
  cache key.

### R3 — OWASP, Authorization Decisions and Output Handling Cheat Sheet

- Record: read.owasp-authorization-decisions.2026-10-31 (proposed).
- Source: src.owasp-authorization-decisions (proposed).
- URL (concatenate):

      https://cheatsheetseries.owasp.org/cheatsheets/
      Authorization_Decisions_And_Output_Handling_Cheat_Sheet.html

- Representation used (concatenate):

      https://raw.githubusercontent.com/OWASP/CheatSheetSeries/
      e7d1b47034ffcf94dcd1d3fb5e002c05d280d271/cheatsheets/
      Authorization_Decisions_And_Output_Handling_Cheat_Sheet.md

- Label/type: "Authorization Decisions and Output Handling Cheat Sheet — OWASP
  Cheat Sheet Series"; community guidance; source commit
  e7d1b47034ffcf94dcd1d3fb5e002c05d280d271 dated 2026-10-03T04:52:59Z.
- Representation: raw Markdown HTTP/2 200 on 2026-10-31T22:47:04Z and
  2026-10-31T22:47:05Z; 6,757 bytes both times; ETag
  "6ca56f04a4097ddd9071a045c0967e212596eddc61a1dd03bc9ef7b2b0cea157"; no
  Last-Modified; raw Markdown SHA-256
  4b6082b65424b078937875bc1402e54606ec3b51bd3e576dbdff8f6e91388e2c on both
  fetches and on the commit-pinned fetch. Canonical text equals the raw
  Markdown: 6,757 characters / 807 words, SHA-256
  4b6082b65424b078937875bc1402e54606ec3b51bd3e576dbdff8f6e91388e2c. The
  served HTML page returned HTTP/2 200
  on 2026-10-31T22:47:06Z with Last-Modified Fri, 30 Oct 2026 14:47:38 GMT and
  contains the quoted "Bound reuse" text.
- Sections read: the full page, including Introduction; Single and Batch
  Decisions; Enforcing Access to Collections; Security Considerations;
  References.
- Sections not read: linked pages (AuthZEN, OpenFGA, Cerbos, OPA); images; no
  authorization service was configured.
- Claims supported: Q17-Q23.
- Limits: living community guidance, not a formal specification or product
  trace. It addresses authorization-decision reuse, not HTTP cache keys; the
  "cached permit" sentence is decision-level guidance.

### R4 — Cloudflare, Cache by status code

- Record: read.cloudflare-cache-status.2026-10-31 (proposed).
- Source: src.cloudflare-cache-status (proposed).
- URL (human page):
  https://developers.cloudflare.com/cache/how-to/configure-cache-status-code/
- Representation used (concatenate):
  https://developers.cloudflare.com/cache/how-to/configure-cache-status-code/
  index.md
- Label/type: "Cache by status code — Cloudflare Cache (CDN) docs"; official
  documentation; page metadata says "Last updated Sep 4, 2026".
- Representation: HTTP/2 200 on 2026-10-31T22:47:09Z and
  2026-10-31T22:47:10Z; 7,367-byte Markdown both times; no Last-Modified or
  ETag; cf-cache-status HIT; raw Markdown SHA-256
  2944ba67f01007a9bcb96996e1e4b90990e2c7f3537c31fa1e506a5ea0a649b6 on both
  fetches. Canonical text 7,359 characters / 794 words, SHA-256
  7d9efa9b923873fc6f97994a83d1f104b8450a40650a0ed7ba56ad366a01fff3.
- Sections read: the full page, including Caching limits; Edge TTL; the
  dashboard, API and Worker controls; and TTL handling for 304 and 200.
- Sections not read: linked Cache Rules and default-cache-behavior pages;
  images; no zone was configured.
- Claims supported: Q24-Q28.
- Limits: living product documentation; it describes status-code caching
  defaults and controls, not a benchmark or authorization policy. The page does
  not use the term "negative caching" or discuss principals.

## Selected exact quotes

Quotes reproduce the served prose after the normalization above. Typographic
apostrophes and quotation marks are ASCII in this note. Line breaks inside
quotes are reflowed for this note and are not part of the source text.
Twenty-eight named passages and five prose fragments were checked against the
four canonical representations on 2026-10-31; 33/33 were present. The owner and
card use a subset; every fragment used there was also checked.

### Mechanism

- Q1, R1, section 2 "Overview of Cache Operation":

      However, it is also possible to store redirects, negative results
      (e.g., 404 (Not Found)), incomplete results (e.g., 206 (Partial Content)),
      and responses to methods other than GET if the method's definition allows
      such caching and defines something suitable for use as a cache key.

- Q6, R1, section 4.2.2 "Calculating Heuristic Freshness":

      A cache MUST NOT use heuristics to determine freshness when an explicit
      expiration time is present in the stored response.

- Q7, R1, section 4.2.2 "Calculating Heuristic Freshness":

      a cache MAY assign a heuristic expiration time when an explicit time is
      not specified

- Q11, R2, section "HTTP 4xx and 5xx status codes that CloudFront caches":

      CloudFront caches HTTP 4xx and 5xx status codes returned by your origin,
      depending on the specific status code that is returned and whether your
      origin returns specific headers in the response.

- Q16, R2, introduction:

      CloudFront always caches responses to `GET` and `HEAD` requests.

- Q24, R4, introduction:

      Customers can set cache time-to-live (TTL) based on the response status
      from the origin web server.

- Q25, R4, section "Edge TTL":

      | 404, 410 | 3m |

- Q26, R4, section "Edge TTL":

      All other status codes are not cached by default.

- Q28, R4, introduction:

      Status codes are returned by a resource's origin.

### Invariant

- Q2, R1, section 2 "Overview of Cache Operation":

      The "cache key" is the information a cache uses to choose a response and
      is composed from, at a minimum, the request method and target URI used to
      retrieve the stored response

- Q3, R1, section 3 "Storing Responses in Caches":

      A cache MUST NOT store a response to a request unless:

- Q4, R1, section 3 "Storing Responses in Caches":

      a status code that is defined as heuristically cacheable

- Q5, R1, section 3.5 "Storing Responses to Authenticated Requests":

      A shared cache MUST NOT use a cached response to a request with an
      Authorization header field (Section 11.6.2 of [HTTP]) to satisfy any
      subsequent request unless the response contains a Cache-Control field
      with a response directive (Section 5.2.2) that allows it to be stored by a
      shared cache

- Q9, R1, section 7.2 "Timing Attacks":

      This is sometimes called "double keying".

- Q10, R1, section 7.3 "Caching of Sensitive Information":

      might lead to the caching of sensitive information (e.g., authentication
      credentials) that is thought to be private, exposing it to unauthorized
      parties.

- Q12, R2, section "HTTP 4xx status codes that CloudFront caches based on
  Cache-Control headers":

      CloudFront only caches the following HTTP 4xx status codes returned by
      your origin if your origin returns a `Cache-Control max-age` or
      `Cache-Control s-maxage` header.

- Q17, R3, section "Single and Batch Decisions":

      Bind each decision to the authenticated subject, action, resource, tenant,
      and relevant context.

- Q18, R3, section "Security Considerations", bullet "Bound reuse":

      Cache only for the same subject, action, resource scope, tenant, and
      relevant policy/input state, within the approved freshness limit.

- Q22, R3, section "Single and Batch Decisions":

      Do not apply one item's permit to the entire batch.

### Failure and recovery

- Q8, R1, section 4.2.4 "Serving Stale Responses":

      A cache MUST NOT generate a stale response unless it is disconnected or
      doing so is explicitly permitted by the client or origin server

- Q13, R2, both custom-error-page and no-custom-error-page sections:

      The amount of time specified by the error caching minimum TTL
      (10 seconds by default)

- Q14, R2, section "How CloudFront processes errors if you haven't configured
  custom error pages", subsection "The requested object is not in the edge
  cache":

      CloudFront continues to retry at intervals specified by the error caching
      minimum TTL.

- Q15, R2, section "How CloudFront processes errors if you haven't configured
  custom error pages", subsection "The requested object is in the edge cache":

      If your origin returns a 5xx error code, CloudFront serves the object
      even though it has expired.

- Q19, R3, section "Security Considerations", bullet "Bound reuse":

      Account for changes between evaluation and use; a cached permit must not
      outlive a required revocation deadline.

- Q20, R3, section "Retrieve Authorized Resource Identifiers":

      Recheck authorization for subsequent operations or when the relevant
      state changes.

- Q21, R3, section "Security Considerations", bullet heading:

      Fail closed.

- Q23, R3, section "Security Considerations", verification paragraph:

      Verify integrations with permitted and denied resources, tenant
      boundaries, each explicit filter result kind, incomplete batches or
      lists, and PDP failure.

### Alternative

- Q27, R4, section "Syntax":

      `value`: An integer value that defines the duration an asset is
      valid in seconds or one of the following strings: `no-store`
      (equivalent to `-1`), `no-cache` (equivalent to
      `0`).

The alternative also cites Q25 and Q26 for the default 404/410 TTL and the
"not cached by default" rule, Q18 for per-subject reuse scope, Q5 for
shared-cache authorization, Q9 for double keying and Q12 with its status table
for origin-controlled 403 caching. The five checked prose fragments are "allows it to be stored by a
shared cache" (Q5), "tries again" (R2), "continues to retry at intervals" (Q14),
"Fail closed." (Q21) and "All other status codes are not cached by default"
(Q26).

## Dimension mapping

- Mechanism. Primary: the retained read.batch3-google-negative.2026-10-21,
  source src.google-cdn-negative-caching, section "Use negative caching",
  revision a8965b0a185de2ca1f52a47fafa7c8db5660222ea2016910bb93297cc1596f70.
  Supporting: Q1 (RFC 9111 permits storing negative results inside its storage
  rules), Q6-Q7 (heuristic freshness is bounded by explicit expiry), Q11 and
  Q16 (CloudFront caches GET/HEAD 4xx/5xx), Q24-Q26 and Q28 (Cloudflare
  status-code TTL defaults). Tycho reading: negative caching is a policy over
  storable non-success results, not a universal error cache. The Google record
  remains the exact per-status TTL example; this lane does not rebind it.
- Invariant. Primary: Q18, record
  read.owasp-authorization-decisions.2026-10-31, source
  src.owasp-authorization-decisions, section "Security Considerations", bullet
  "Bound reuse", revision
  4b6082b65424b078937875bc1402e54606ec3b51bd3e576dbdff8f6e91388e2c.
  Supporting: Q17 and Q22 (decision scope and batch separation), Q2-Q5 (cache
  key, storage rules and shared-cache authorization), Q9-Q10 (double keying and
  sensitive information), Q12 and its following status table (a 403 is
  edge-cacheable only when the origin marks it so). Tycho rule: a negative key
  for an authorization-sensitive lookup includes tenant, principal or scope,
  checked operation and policy revision; a cached denial is not a universal
  absence statement.
- Failure and recovery. Primary: Q19, record
  read.owasp-authorization-decisions.2026-10-31, source
  src.owasp-authorization-decisions, section "Security Considerations", bullet
  "Bound reuse", revision
  4b6082b65424b078937875bc1402e54606ec3b51bd3e576dbdff8f6e91388e2c.
  Supporting: Q20-Q21 (recheck and fail closed), Q23 (verification cases),
  Q8 (stale-response prohibition), Q13-Q15 (10-second default error TTL, retry
  intervals and 5xx stale-object serving). Tycho runbook: bound a denial by the
  shorter of its TTL and the revocation deadline; delete or version the key on
  create, grant, revoke and delete; revalidate; never cache an unknown backend
  error as "absent"; test the revocation path. Narrowing: CloudFront's stale
  5xx behavior is an availability choice, not evidence of object existence for
  a principal.
- Alternative. Primary: Q27, record read.cloudflare-cache-status.2026-10-31,
  source src.cloudflare-cache-status, section "Syntax", revision
  7d9efa9b923873fc6f97994a83d1f104b8450a40650a0ed7ba56ad366a01fff3.
  Supporting: Q25-Q26 (default 404/410 TTL and the not-cached default), Q18
  (same-subject reuse scope), Q5 (shared-cache authorization), Q9 (double
  keying), Q12 and its following status table (origin-controlled 403
  caching). Tycho choice rule: per-principal keying for authorization
  decisions; a short TTL for public existence checks; bypass when the
  revocation deadline is shorter than any useful TTL. Reverse when repeated
  misses dominate origin load and the denial is global for the key.
- Retention and coverage. The lane proposes technical_coverage sufficient and
  decision_coverage sufficient because each owner claim now has a bound primary
  passage, supporting passages, explicit limits and a narrowed alternative.
  This is a self-check, not independent review or owner acceptance.

## Proposed shared metadata

The following changes are proposals only. No shared JSON is edited in this lane.

### sources/register.json

Add src.owasp-authorization-decisions:

- title "Authorization Decisions and Output Handling Cheat Sheet";
  observed_title "Authorization Decisions And Output Handling - OWASP Cheat
  Sheet Series"; category security; publisher OWASP; kind official-docs; URL
  the human page above; resolved_url the same; topics security, authorization,
  caching; priority supporting; planned_use "Authorization-decision reuse
  bounds, revocation deadline and fail-closed guidance for the negative-caching
  entry."; admission admitted-for-research; access
  public-web-or-author-download; reading_status full-public-page-inspected;
  access_checked and content_verified 2026-10-31; version "Living cheat sheet;
  fetched 2026-10-31; source commit e7d1b47034ffcf94dcd1d3fb5e002c05d280d271
  dated 2026-10-03T04:52:59Z; raw Markdown 6,757 bytes, ETag
  6ca56f04a4097ddd9071a045c0967e212596eddc61a1dd03bc9ef7b2b0cea157; canonical
  text 6,757 characters / 807 words, SHA-256 4b6082b6...; served page
  Last-Modified 2026-10-30T14:47:38Z."; verification_scope "Full page read for
  Single and Batch Decisions, Enforcing Access to Collections and Security
  Considerations, including the Bound reuse, fail-closed and recheck rules; no
  authorization service was configured and linked specifications were not
  read."

Add src.cloudflare-cache-status:

- title "Cache by status code"; observed_title "Cache by status code ·
  Cloudflare Cache (CDN) docs"; category performance; publisher Cloudflare;
  kind official-docs; URL the human page above; resolved_url the same; topics
  caching, negative-caching, performance-engineering; priority supporting;
  planned_use "Per-status Edge TTL defaults and TTL/no-store controls for the
  negative-caching alternative."; admission admitted-for-research; access
  public-web-or-author-download; reading_status full-public-page-inspected;
  access_checked and content_verified 2026-10-31; version "Living documentation;
  page metadata Last updated 2026-09-04; fetched 2026-10-31; Markdown alternate
  7,367 bytes, no Last-Modified or ETag; canonical text 7,359 characters / 794
  words, SHA-256 7d9efa9b...; no pinned release."; verification_scope "Full
  page read for Edge TTL defaults, cache TTL by status via dashboard/API/Worker
  and 304/200 TTL handling; no zone was configured and linked Cache Rules pages
  were not read."

Extend src.rfc9111-enrichment:

- reading_status full-public-page-inspected; access_checked and content_verified
  2026-10-31; append to version "RFC 9111 text fetched 2026-10-31; 84,477
  bytes; ETag W/f8907618635703edd228aee4aa834eee; canonical text 84,469
  characters / 11,838 words, SHA-256 cb261a28...; HTTP Caching, June 2022,
  STD 98."; append to verification_scope "Sections 2, 3, 3.5, 4.2.2, 4.2.4,
  7.2 and 7.3 read 2026-10-31 for negative results, storage rules, shared-cache
  authorization, heuristic and stale-response limits, double keying and
  sensitive-information exposure; remaining sections and linked specifications
  were not analyzed; no implementation tested."

Extend src.cloudfront:

- append to version "HTTPStatusCodes page fetched 2026-10-31; Markdown alternate
  13,160 bytes; Last-Modified 2026-10-31T03:32:34Z; ETag
  SwfPWABqLr3XGvryDXXbad1bnrI=; canonical text 13,112 characters / 1,995
  words, SHA-256 c09ee996...; no published revision identifier."; append to
  verification_scope "The HTTP 4xx/5xx processing page was read 2026-10-31 for
  per-status error caching, the 10-second error-caching minimum TTL, retry
  intervals, conditional 403 caching and 5xx stale-object serving; linked error
  pages, images and any distribution configuration were not examined."

### reading-ledger.v1.json

Add four records. All use access_date 2026-10-31, reviewer "Automated authoring
agent" and status "read".

- read.rfc9111-negative-caching.2026-10-31
  - source: src.rfc9111-enrichment
  - unit_url: https://www.rfc-editor.org/rfc/rfc9111.txt
  - unit_label: RFC 9111 — HTTP Caching
  - unit_type: specification
  - sections_read: 2; 3; 3.5; 4.2.2; 4.2.4; 7.2; 7.3
  - sections_not_read: remaining RFC sections; linked HTTP specifications
  - content_sha256: cb261a284f28ee5315280d2f8ee4be14d82e46ae55b91c755962f3b833db0538
  - characters/words: 84,469 / 11,838
  - claims_supported: Q1-Q10
  - claims_not_supported: the term "negative caching"; application
    authorization semantics; implementation behavior; benchmark
  - limitations: standards text; selected sections analyzed; no cache
    implementation exercised.
- read.cloudfront-status-codes.2026-10-31
  - source: src.cloudfront
  - unit_url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HTTPStatusCodes.md
  - unit_label: CloudFront — HTTP 4xx and 5xx status-code processing
  - unit_type: documentation-page
  - sections_read: the full page, including cached-status tables and stale
    behavior
  - sections_not_read: linked error pages; images
  - content_sha256: c09ee9965aa05bae32a876195927e7e2cfa4d8aff5b073a0e18f7bad4c368993
  - characters/words: 13,112 / 1,995
  - claims_supported: Q11-Q16
  - claims_not_supported: per-principal cache keys; authorization semantics;
    benchmark; local reproduction
  - limitations: living documentation; no distribution configured.
- read.owasp-authorization-decisions.2026-10-31
  - source: src.owasp-authorization-decisions
  - unit_url: the human cheat-sheet page above
  - unit_label: OWASP — Authorization Decisions and Output Handling Cheat Sheet
  - unit_type: documentation-page
  - sections_read: Introduction; Single and Batch Decisions; Enforcing Access
    to Collections; Security Considerations; References
  - sections_not_read: linked specifications and projects; images
  - content_sha256: 4b6082b65424b078937875bc1402e54606ec3b51bd3e576dbdff8f6e91388e2c
  - characters/words: 6,757 / 807
  - claims_supported: Q17-Q23
  - claims_not_supported: HTTP cache mechanics; product behavior; benchmark;
    local reproduction
  - limitations: community guidance; no authorization service configured.
- read.cloudflare-cache-status.2026-10-31
  - source: src.cloudflare-cache-status
  - unit_url: the human page above
  - unit_label: Cloudflare — Cache by status code
  - unit_type: documentation-page
  - sections_read: Caching limits; Edge TTL; dashboard/API/Worker controls;
    304/200 TTL handling
  - sections_not_read: linked Cache Rules and default-cache-behavior pages;
    images
  - content_sha256: 7d9efa9b923873fc6f97994a83d1f104b8450a40650a0ed7ba56ad366a01fff3
  - characters/words: 7,359 / 794
  - claims_supported: Q24-Q28
  - claims_not_supported: authorization semantics; principal-scoped keys;
    benchmark; local reproduction
  - limitations: living documentation; no zone configured.

### Source plan edition/patterns/source-plan.v1.json

Replace the required_units array for tycho.pattern.negative-caching with the
five units below. The Google unit is retained as the per-status TTL example.

Each unit keeps the existing schema fields (source_id, unit, unit_type,
url, sections, status, read_record_id, blocked_reason: null). URLs are the
exact ones recorded in R1-R4 and are not repeated here, because two exceed the
100-character line limit; the Google URL is unchanged.

- src.rfc9111-enrichment — "RFC 9111 — HTTP Caching"; specification; URL as in
  R1; sections 2, 3, 3.5, 4.2.2, 4.2.4, 7.2 and 7.3; status read; record
  read.rfc9111-negative-caching.2026-10-31.
- src.cloudfront — "CloudFront — HTTP 4xx and 5xx status-code processing";
  documentation-page; URL as in R2; full page; status read; record
  read.cloudfront-status-codes.2026-10-31.
- src.owasp-authorization-decisions — "OWASP — Authorization Decisions and
  Output Handling Cheat Sheet"; documentation-page; URL as in R3
  (concatenated there); sections "Single and Batch Decisions" and "Security
  Considerations"; status read; record read.owasp-authorization-decisions.2026-10-31.
- src.cloudflare-cache-status — "Cloudflare — Cache by status code";
  documentation-page; URL as in R4; sections "Edge TTL" and "Caching limits";
  status read; record read.cloudflare-cache-status.2026-10-31.
- src.google-cdn-negative-caching — "Use negative caching — Google Cloud
  documentation"; documentation-page; retained unit URL unchanged; sections
  "Use negative caching" and "Status codes and default TTLs"; status read;
  record read.batch3-google-negative.2026-10-21.

Proposed notes: "Four public sources bound 2026-10-31: RFC 9111, CloudFront
4xx/5xx processing, OWASP authorization-decision reuse and Cloudflare
status-code TTL. The Google per-status TTL example is retained. The protocol
text does not use the term negative caching; OWASP and Cloudflare do not define
HTTP authorization caching semantics."

### Owner units edition/patterns/owner-units.v1.json

Keep the document id, path, heading, anchor and level; update owner.line from
49 to 58. Keep unit_kind dedicated. Consider adding unit_terms "negative
results", "Bound reuse" and "revocation deadline".

Technical evidence:

- mechanism: keep state supported. Claim quote unchanged: "Caching an absent
  result can protect against repeated misses for nonexistent IDs. But it
  creates a freshness question: if a new object is created, a cached not-found
  may hide it." Reason: RFC 9111 permits storing negative results inside its
  storage rules; CloudFront caches 4xx/5xx by status and origin headers;
  Cloudflare sets per-status TTLs. Primary binding: Q1, record
  read.rfc9111-negative-caching.2026-10-31, section 2, revision
  cb261a28.... Supporting: Q6-Q7, Q11, Q16 and Q24-Q26; retained Google record.
  Tycho reading: a policy over storable non-success results, not a universal
  error cache.
- invariant: state supported. Claim quote: "A cached negative must never become
  a universal statement that an object does not exist for all authorized
  principals if visibility varies by principal or tenant." Reason: OWASP binds
  a decision to subject, action, resource, tenant and context and limits cache
  reuse to the same scope and freshness; RFC 9111 requires a cache key and
  restricts shared-cache reuse of Authorization-bearing responses; CloudFront
  caches 403 only with origin Cache-Control. Primary binding: Q18, record
  read.owasp-authorization-decisions.2026-10-31, section "Security
  Considerations", revision 4b6082b6.... Supporting: Q17, Q22, Q2-Q5, Q9-Q10
  and Q12. Tycho rule: include tenant, principal or scope, checked operation
  and policy revision in the key.
- failure_recovery: state supported (narrowed). Claim quote: "A cached denial
  can outlive a grant or a revocation." Reason: OWASP states that a cached permit
  must not outlive a revocation deadline and prescribes recheck and fail-closed
  behavior; CloudFront retries after its 10-second default error TTL; RFC 9111
  prohibits stale responses unless disconnected or explicitly permitted.
  Primary binding: Q19, record
  read.owasp-authorization-decisions.2026-10-31, section "Security
  Considerations", revision 4b6082b6.... Supporting: Q20-Q21, Q23, Q8,
  Q13-Q15. Narrowing: no selected unit tests a revocation path; the CloudFront
  stale 5xx behavior is availability, not proof of existence.
- alternative: state supported. Claim quote: "Per-principal keying, a short TTL
  and bypass are the three bounded alternatives." Reason: Cloudflare defines
  per-status TTL and no-store/no-cache controls and a 3-minute default for
  404/410; OWASP limits cache reuse to the same decision scope; RFC 9111
  documents double keying and shared-cache Authorization rules. Primary
  binding: Q27, record read.cloudflare-cache-status.2026-10-31, section
  "Syntax", revision 7d9efa9b.... Supporting: Q25-Q26, Q18, Q5, Q9 and Q12.
  Tycho choice rule: per-principal key for authorization, short TTL for public
  existence, bypass when the revocation deadline is short.

Other owner-units fields:

- technical_coverage "sufficient"; decision_coverage "sufficient";
  review_state "self-checked".
- notes: "Four dimensions bound 2026-10-31 to RFC 9111, CloudFront 4xx/5xx
  processing, OWASP authorization-decision reuse guidance and Cloudflare
  status-code TTL; the RFC does not use the term negative caching, OWASP and
  Cloudflare do not define HTTP authorization caching, and no revocation path
  was tested; coverage is self-checked, not independently reviewed."
- source_support: primary ledger_record read.owasp-authorization-decisions.2026-10-31,
  source_id src.owasp-authorization-decisions, unit_type documentation-page,
  status read, card_citation true; auxiliary entries for
  read.rfc9111-negative-caching.2026-10-31,
  read.cloudfront-status-codes.2026-10-31,
  read.cloudflare-cache-status.2026-10-31 and the retained
  read.batch3-google-negative.2026-10-21.
- decision_evidence.competing_alternative: "Per-principal key, short TTL,
  bypass, or no negative cache at all. Reverse when repeated misses dominate
  origin load and the denial is global for the key."; decision_state
  applicable-under-conditions; card_components 10; atlas_section
  negative-caching.

### Registry, card batches and derived artifacts

The registry currently records technical_owner.state partial,
atlas_owner.state partial-bounded and coverage partial. After the owner-units
proposal is applied, regenerate those fields from owner-units rather than
editing them by hand. The proposed state is technical_owner.state sufficient,
atlas_owner.state sufficient and coverage technical/decision/overall sufficient,
confidence high. source_units should list the five units above. The registry
notes should say the four dimensions are self-checked and promotion is not part
of this lane.

card-batches.v1.json needs no card_path; the card remains inline in V11/C05.
edition/atlas-manifest.json and generated indexes should be regenerated by the
integrator after the owner and card hashes are final. This lane does not claim
that regeneration.

## Verification

Commands run in /Users/rbaranov/Projects/tycho-worktrees/b64-negative-cache:

- python3 scripts/check_markdown_line_length.py
  Result: PASS: V11 prose <=100; 145 exact owner-link exceptions.
- python3 scripts/check_boundary.py
  Result: PASS: configured lexical boundary checks; independent-origin review
  still required.
- Added-line length scan: 76 added owner lines and 41 added card lines; every
  added line is <=100 characters. Pre-existing long lines outside the edited
  owner section and the exempt owner link remain unchanged.
- Quote check: 28 named passages and 5 prose fragments checked against the four
  canonical representations; 33/33 present.
- git status: exactly three paths, the owner page, the V11/C05 landing and this
  note.
- No shared JSON, generated index, promotion record, review report or test file
  is changed.

No full unit suite was run. The lane is a content slice; the batch-end suite is
the integrator's step. validate_book_metadata.py fails on the V11/C05 landing
with "unknown source ID" (it would also fail on the owner page) until the two
proposed register rows are applied; that is the expected consequence of the
no-shared-JSON constraint, not a claim that the metadata is already consistent.

## Limits

- Coverage and review are self-checked. No independent AI review, owner
  acceptance, promotion, CI result or production observation is claimed.
- RFC 9111 does not use the term "negative caching"; it permits storing
  negative results. CloudFront documents error caching, Cloudflare documents
  status-code caching, and OWASP documents authorization-decision reuse. The
  synthesis into one negative-caching policy is Tycho.
- CloudFront's conditional 403 caching shows that an origin can mark a denial
  cacheable; it does not establish a per-principal key or a safe revocation
  protocol.
- The CloudFront 5xx stale-object behavior is a documented availability
  trade-off, not evidence that a resource exists or that a denial is correct.
- OWASP's "cached permit" sentence is decision-level guidance; the selected
  page does not describe an HTTP cache or a particular implementation.
- Cloudflare's default TTL table is product documentation; it does not discuss
  authorization and was not measured.
- The retained Google Cloud CDN record was not re-fetched on 2026-10-31; it is
  the batch-3 record and the register's earlier verification scope still notes
  a truncated first fetch. The full-unit reading note records a later complete
  read, but this lane does not rebind that unit.
- No runtime exercise, benchmark, cache simulation, revocation drill or CDN
  configuration was performed.

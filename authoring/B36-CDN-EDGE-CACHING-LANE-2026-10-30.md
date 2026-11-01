# B36 — CDN / Edge Caching invariant and alternative lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: mechanism and failure/recovery were supported;
invariant and alternative were partial. This lane binds the source-supported
parts of both dimensions to RFC 9111 and selected Microsoft Azure CDN and Amazon
CloudFront pages, and labels the triad formulation and the direct-origin name as
Tycho guidance. A detached scratch metadata patch passes preflight and
owner-unit checks; the patch is not in the lane commit.

## Lane coordinates

- Parent HEAD: `cdfa44c076fe977f35f0f0187c53a0afbecb97a1` (`cdfa44c0`).
- Branch: `b36-cdn`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b36-cdn`.
- Scope: the owner section `### CDN-Edge Caching` in the V08/C08 owner page and
  the inline V11/C05 card `### CDN / Edge Caching`. Single-entry lane; no other
  entry, shared owner page, promotion or generated file is changed.
- Owner path (concatenate the three lines):

      book/volumes/v08-delivery-deployment-and-recovery/
      c08-network-request-paths-routing-and-edge-delivery/
      edge-cache-origin.md

- Card path:
  `book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md`.
- Path discrepancy: the parent brief named V11 (C02/C06). At this HEAD V11/C02
  is API communication and V11/C06 is database and storage architecture; neither
  contains the CDN card. The registry names V11/C05, and the card is inline in
  V11/C05 at line 419. No C02/C06 card was created.
- The card remains inline; the integrator owns any split and `card_path`
  registration.

## Candidate evaluation

- Microsoft, "How caching works" (selected; existing source candidate
  `src.azure-cdn`; proposed). Selected for the shared-cache description, the statement
  that unique-user resources cannot be cached, the authorization-header note,
  the eviction/no-minimum guarantee and the HEAD/GET precondition. It is a
  product overview with a classic-service retirement notice, not an
  implementation test.
- Microsoft, "Control Azure Content Delivery Network caching behavior with
  caching rules" (selected; `src.azure-cdn`). Selected for the bypass setting,
  zero-duration revalidation and the statement that a rule change does not
  reset existing cache durations until the file is purged. This is a
  previous-versions page, served as HTML.
- Microsoft, "Purge an Azure Content Delivery Network endpoint" (selected;
  `src.azure-cdn`). Selected for the downstream-cache limit and the statement
  that query strings are ignored in the purge path. No purge was run and no
  propagation was measured.
- Amazon, "Understand the cache key" (selected; existing source candidate
  `src.cloudfront`; proposed). Selected for the cache-key definition, the rule to include
  values that change the origin response, and the warning about user-specific
  cookies in the key.
- Amazon, "Add custom headers to origin requests" (selected;
  `src.cloudfront`). Selected for the default Authorization-header removal, the
  authorized/unauthorized shared-response hazard when the header is outside the
  key, and the documented choice between key inclusion and disabling caching.
- Amazon, "Manage how long content stays in the cache (expiration)" (selected;
  `src.cloudfront`). Selected for the minimum-TTL override of private, no-cache
  and no-store directives and for the stale-on-origin-error behavior.
- Amazon, "Invalidate files to remove content" (selected; `src.cloudfront`).
  Selected for the statement that a user might continue to see the old version
  after invalidation and for the versioned-file recommendation. No invalidation
  was run.
- IETF, "HTTP caching" (selected; existing `src.rfc9111-enrichment`). Selected
  for RFC 9111 sections 3.5, 4, 4.1, 4.4, 5.2.2.5 and 5.2.2.7. The existing
  record `read.rfc9111-stale.2026-10-30` covers only sections 4.2.4 and 5.5, so
  this lane proposes a separate record rather than widening that historical
  record silently.
- Microsoft, "Control Azure Content Delivery Network caching behavior with
  query strings" (examined, not selected as a separate unit). It supports the
  unique-URL key mode, the session-ID/user-name warning and the 10-minute
  settings propagation. The selected how-caching, caching-rules and purge pages
  already carry the key, authorization and purge claims used here; the page is a
  candidate for a later unit. No quote from it is used.
- Amazon, "Invalidate files" request procedure and "What you need to know when
  invalidating paths" (examined, not selected as separate units). They add the
  few-second forwarding, the immediate start, the inability to cancel and the
  inability to selectively invalidate cookie variants. The selected
  invalidation page already carries the downstream-lag claim; these pages are
  candidates for a later purge-contract lane. No quote from them is used.
- Azure Front Door, Azure CDN from Edgio and the premium-tier query-string page
  (examined, not selected). They are different products or different interfaces;
  mixing them would weaken the product revision boundary.
- Microsoft, "Static Content Hosting" (existing unit, unchanged). It remains the
  card's cited ledger record and the existing mechanism/failure binding; it is
  narrower than the CDN guidance and does not support the new invariant or
  alternative claims.

## Source binding

Quotes reproduce the served prose. Markdown inline-code, bold and italic markers
are not repeated where they are formatting only; line breaks inside a quote are
editorial wrapping. The binding revision always identifies the exact
representation: an HTML raw digest for the Azure pages, a Markdown digest for
the CloudFront pages, and the RFC text digest.

### RFC 9111 — HTTP caching

- Source id: `src.rfc9111-enrichment` (existing).
- Proposed record: `read.rfc9111-edge-cache.2026-10-30`.
- URL: `https://www.rfc-editor.org/rfc/rfc9111.txt`.
- Unit label: "HTTP caching — RFC 9111"; unit type `specification`; access date
  2026-10-30.
- Access: public HTTPS GET on 2026-10-30; served text 84,477 bytes; HTTP Date
  2026-10-30T17:27:50Z; ETag
  `W/"f8907618635703edd228aee4aa834eee"`; no Last-Modified; raw text SHA-256
  `aeb52adb3279d5f23dae34f68af11bd5cef0a0aff7ffcd014c9ca93c5302cf3e`; no
  published revision identifier. This is the binding revision.
- Sections used: "3.5. Storing Responses to Authenticated Requests",
  "4. Constructing Responses from Caches", "4.1. Calculating Cache Keys with
  the Vary Header Field", "4.4. Invalidating Stored Responses",
  "5.2.2.5. no-store" and "5.2.2.7. private".
- Exact quotes used:

      A shared cache MUST NOT use a cached response to a request with an
      Authorization header field (Section 11.6.2 of [HTTP]) to satisfy any
      subsequent request unless the response contains a Cache-Control field
      with a response directive (Section 5.2.2) that allows it to be stored by
      a shared cache, and the cache conforms to the requirements of that
      directive for that response.

      When presented with a request, a cache MUST NOT reuse a stored response
      unless:

      the cache MUST NOT use that stored response without revalidation unless
      all the presented request header fields nominated by that Vary field
      value match those fields in the original request

      The unqualified private response directive indicates that a shared cache
      MUST NOT store the response (i.e., the response is intended for a single
      user). It also indicates that a private cache MAY store the response,
      subject to the constraints defined in Section 3, even if the response
      would not otherwise be heuristically cacheable by a private cache.

      The no-store response directive indicates that a cache MUST NOT store any
      part of either the immediate request or the response and MUST NOT use the
      response to satisfy any other request.

      Note that this does not guarantee that all appropriate responses are
      invalidated globally; a state-changing request would only invalidate
      responses in the caches it travels through.

- Limits: selected sections only; no cache implementation was exercised. The
  RFC does not define a product CDN's configuration, purge API or
  authorization service.

### Microsoft Azure CDN — How caching works

- Source id: `src.azure-cdn` (new).
- Proposed record: `read.azure-cdn-how-caching.2026-10-30`.
- URL: `https://learn.microsoft.com/en-us/azure/cdn/cdn-how-caching-works`.
- Unit label: "How caching works — Azure CDN"; unit type `documentation-page`;
  access date 2026-10-30.
- Access: public HTTPS GET on 2026-10-30; served HTML 59,200 bytes; raw HTML
  SHA-256
  `5ae280f568de52e593c290d013c61918320815b916ef7bf0c31e468fcbda956a`;
  canonical main-text SHA-256
  `7f1941e1665b85dea7bf5c52d8710ee36f6c04501accdd6daa7033de9cee3f9a`;
  HTTP Date 2026-10-30T19:08:56Z; ETag
  `"CXedS0x+2dbWvM/ixmpdlWsxVwc="`; Last-Modified Tue, 15 Sep 2026
  17:18:04 GMT; `ms.date` 2026-02-28; `git_commit_id`
  `fe2e4465ddb694284d4bdefca0f41e9499090877`. This is the binding revision.
- Sections used: "Introduction to caching", "Content delivery network caching",
  "Determining which files can be cached" and "Default caching behavior".
- Exact quotes used:

      Dynamic resources that change frequently or are unique to an individual
      user can't be cached.

      Requests that include authorization header will not be cached.

      Azure CDN makes no guarantees about minimum amount of time that the
      object will be stored in the cache. Cached contents might be evicted
      from the content delivery network cache before they are expired if the
      contents are not requested as frequently to make room for more
      frequently requested contents.

      For caching to work on a resource, the origin server must support any
      HEAD and GET HTTP requests and the content-length values must be the
      same for any HEAD and GET HTTP responses for the asset.

- Limits: one product overview page; the page carries the Azure CDN Standard
  from Microsoft (classic) retirement notice. No CDN was configured and no
  cache behavior was exercised. The "authorization header" sentence is a
  product default, not a general HTTP rule; RFC 9111 section 3.5 states the
  shared-cache rule.

### Microsoft Azure CDN — caching rules

- Source id: `src.azure-cdn`.
- Proposed record: `read.azure-cdn-caching-rules.2026-10-30`.
- URL (resolved previous-versions representation):
  `https://learn.microsoft.com/en-us/previous-versions/azure/cdn/cdn-caching-rules`.
- Unit label: "Caching behavior with caching rules — Azure CDN"; unit type
  `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET on 2026-10-30 of the previous-versions page; served
  HTML 43,524 bytes; raw HTML SHA-256
  `5e686846ea09abdd926114d382bebb405ad9ece75b606eec5780c81916f9a361`;
  canonical main-text SHA-256
  `cb1076a46a53ce1fe601f35beb254e5d766743be4848e080e4bb8f4bc7c7e1f6`;
  HTTP Date 2026-10-30T19:08:59Z; ETag
  `"IxMizs9EycZDwzW8bv4zSkSNhVs="`; Last-Modified Wed, 26 Aug 2026
  07:21:22 GMT; `ms.date` 2025-03-31; `git_commit_id`
  `1a312008ffbf4cc43ee13967c16007eda6a11ae9`. This is the binding revision.
- Sections used: "Caching behavior settings", "Cache expiration duration" and
  "Global and custom rule processing order".
- Exact quotes used:

      Bypass cache: Don't cache and ignore origin-provided cache-directive
      headers.

      For the Override and Set if missing Caching behavior settings, valid
      cache durations range between 0 seconds and 366 days. For a value of 0
      seconds, the content delivery network caches the content, but must
      revalidate each request with the origin server.

      Files that are cached before a rule change maintain their origin cache
      duration setting. To reset their cache durations, you must purge the
      file.

- Limits: one previous-versions page; no rule was applied and no purge was run.
  The page describes a configuration interface, not the authorization
  semantics of a deployment.

### Microsoft Azure CDN — purge endpoint

- Source id: `src.azure-cdn`.
- Proposed record: `read.azure-cdn-purge.2026-10-30`.
- URL: `https://learn.microsoft.com/en-us/azure/cdn/cdn-purge-endpoint`.
- Unit label: "Purge an Azure CDN endpoint — Azure CDN"; unit type
  `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET on 2026-10-30; served HTML 52,164 bytes; raw HTML
  SHA-256
  `a2cf2b83b454fa0ce7c1cf8dbbfe6640152bbc630132026ecad3b7c66971f378`;
  canonical main-text SHA-256
  `ed4c2f4dcbd5238afdaa98b4e6861201c08c5237daea3a4d6ffa6241c5f266d8`;
  HTTP Date 2026-10-30T19:08:57Z; ETag
  `"9eTd7ot+PgCfOMUlsE5UQlUmznY="`; Last-Modified Sun, 23 Aug 2026
  22:13:15 GMT; `ms.date` 2026-02-28; `git_commit_id`
  `fe2e4465ddb694284d4bdefca0f41e9499090877`. This is the binding revision.
- Sections used: "Purge contents from an Azure CDN endpoint".
- Exact quotes used:

      Note that purging only clears the cached content on the content delivery
      network edge servers. Any downstream caches, such as proxy servers and
      local browser caches, might still hold a cached copy of the file.

      In Azure CDN from Microsoft, query strings in the purge URL path are not
      considered.

      Both TestCDN?myname=max and TestCDN?myname=clark will be purged.

- Limits: one documentation page; no purge was run and no propagation was
  measured. The query-string behavior is specific to the named Azure CDN
  offering.

### Amazon CloudFront — Understand the cache key

- Source id: `src.cloudfront` (new).
- Proposed record: `read.cloudfront-cache-key.2026-10-30`.
- URL: the CloudFront
  `understanding-the-cache-key.html` page under
  `https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/`.
- Unit label: "Understand the cache key — Amazon CloudFront"; unit type
  `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET of the Markdown alternate on 2026-10-30; 7,573
  bytes; SHA-256
  `47c2adb2350549b0f192e0fb3aef953928cb3a8ed43e86c38a74ba695fe80790`;
  HTTP Date 2026-10-30T19:07:52Z; Last-Modified Fri, 30 Oct 2026
  18:47:13 GMT; ETag `"PS1aj/hDmdBMkFfJ9VueX5vi5UE="`; no published revision
  identifier. This is the binding revision.
- Sections used: "Default cache key" and "Customize the cache key".
- Exact quotes used:

      The cache key is the unique identifier for an object in the cache. Each
      object in the cache has a unique cache key.

      When a value in the viewer request determines the response that your
      origin returns, you should include that value in the cache key.

      Cookies that have user-specific or session-specific values and are
      unique across thousands (or even millions) of requests are also not good
      candidates for cache key inclusion.

- Limits: one documentation page; no distribution was configured. The page
  describes a selectable key policy, not an authorization decision.

### Amazon CloudFront — Authorization header forwarding

- Source id: `src.cloudfront`.
- Proposed record: `read.cloudfront-auth-header.2026-10-30`.
- URL: the CloudFront
  `add-origin-custom-headers.html` page under
  `https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/`.
- Unit label: "Add custom headers to origin requests — Amazon CloudFront"; unit
  type `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET of the Markdown alternate on 2026-10-30; 6,332
  bytes; SHA-256
  `06076dc410b73bd1bf63c46c01900c8b767b1201c29073c8e440b4b002c3d891`;
  HTTP Date 2026-10-30T19:08:04Z; Last-Modified Fri, 30 Oct 2026
  18:47:11 GMT; ETag `"2jsuTBlRblywreobHLxSU/Zn3cY="`; no published revision
  identifier. This is the binding revision.
- Sections used: "Configure CloudFront to forward the Authorization header".
- Exact quotes used:

      When CloudFront forwards a viewer request to your origin, CloudFront
      removes some viewer headers by default, including the Authorization
      header.

      When the Authorization header is not part of the cache key, CloudFront
      can serve the same cached response to both authorized and unauthorized
      viewers.

      Either include the Authorization header in the cache key using a cache
      policy, or disable caching entirely for origins that require origin-side
      authorization processing.

- Limits: one documentation page; no distribution was configured and no
  authorization matrix was tested. The page describes cache policy and origin
  request policy options, not a complete access-control design.

### Amazon CloudFront — expiration

- Source id: `src.cloudfront`.
- Proposed record: `read.cloudfront-expiration.2026-10-30`.
- URL:
  `https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html`.
- Unit label: "Manage how long content stays in the cache (expiration) — Amazon
  CloudFront"; unit type `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET of the Markdown alternate on 2026-10-30; 18,087
  bytes; SHA-256
  `cfb1bbad63f66dcf936c4d269ecaa3e2e24871d684e8555eb46ee94ea1eb2a1a`;
  HTTP Date 2026-10-30T19:07:51Z; Last-Modified Fri, 30 Oct 2026
  18:47:13 GMT; ETag `"+oAU/DZgrL8aLHpzWjycKZ9spOs="`; no published revision
  identifier. This is the binding revision.
- Sections used: "Use headers to control cache duration for individual
  objects" and "Specify the amount of time that CloudFront caches objects".
- Exact quotes used:

      If your minimum TTL is greater than 0, CloudFront uses the cache policy’s
      minimum TTL, even if the Cache-Control: no-cache, no-store, and/or
      private directives are present in the origin headers.

      If the origin is unreachable and the minimum or maximum TTL value is
      greater than 0, CloudFront will serve the object that it got from the
      origin previously.

      To avoid this behavior, include the Cache-Control: stale-if-error=0
      directive with the object returned from the origin.

- Limits: one documentation page; no distribution was configured and no
  expiration or stale-on-error test was run. The minimum-TTL interaction is a
  product configuration rule, not a general cache specification.

### Amazon CloudFront — invalidation

- Source id: `src.cloudfront`.
- Proposed record: `read.cloudfront-invalidation.2026-10-30`.
- URL:
  `https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html`.
- Unit label: "Invalidate files to remove content — Amazon CloudFront"; unit
  type `documentation-page`; access date 2026-10-30.
- Access: public HTTPS GET of the Markdown alternate on 2026-10-30; 2,307
  bytes; SHA-256
  `62930f87a51b954f89cbe31272057abf219b7224a3d7c058386443ad280b4940`;
  HTTP Date 2026-10-30T19:08:10Z; Last-Modified Fri, 30 Oct 2026
  18:47:13 GMT; ETag `"75prURMm9qut4q3wNfJ6h5vTPxM="`; no published revision
  identifier. This is the binding revision.
- Sections used: "Choose between invalidating files and using versioned file
  names".
- Exact quotes used:

      If you invalidate the file, the user might continue to see the old
      version until it expires from those caches.

      If you want to update your files frequently, we recommend that you
      primarily use file versioning for the following reasons:

- Limits: one documentation page; no invalidation was run and no propagation
  was measured. The page lists reasons for versioning; the quote stops before
  the first reason.

## Book edits

### Owner section

- Frontmatter: only `updated_at` moves to 2026-10-30. `evidence_scope`,
  `content_review`, `source_inspection_date` and `content_verified_at` remain
  byte-identical to the decomposition baseline; the new sources are proposed
  records and supporting bindings, not new `evidence_scope` ids. See Frontmatter
  and evidence scope below. The owner heading stays at line 131; the page is 225
  lines.
- The mechanism paragraph names the Azure shared-cache statement and the
  CloudFront cache-key definition. It keeps the existing sentence that
  cacheability is a content and authority contract, not a network location.
- The invariant paragraph separates the source statements from the Tycho rule.
  It binds RFC 9111 sections 4, 4.1 and 3.5, the Azure authorization-header
  note, and the CloudFront key-mismatch and minimum-TTL warnings. It labels the
  triad sentence "The cache key, freshness policy and authorization boundary
  must agree" as Tycho synthesis: no selected source states all three as one
  rule.
- The failure/recovery paragraph binds Azure eviction/no-minimum language and
  the CloudFront stale-on-origin-error behavior. It labels the
  purge-without-completion-evidence rule as Tycho guidance.
- The alternative paragraph binds RFC 9111 private and no-store, the CloudFront
  key-or-disable-caching choice, the Azure bypass setting and the Azure and
  CloudFront downstream-cache limits. It labels "direct origin" as Tycho's
  name for the uncached route and the purge-completion rule as Tycho guidance.
- A limits list names all eight proposed records, the exact revisions and the
  sections used. It states that no CDN was configured, no purge was run and no
  authorization matrix was tested.
- Raw SHA-256:
  `339b1ddd54b301e0f90bf6d6f2be95d374013c0eb3f1eec4983c1be795a2811f`.
- Historical-view SHA-256:
  `0d130ec20d02d6e029e9ea863c2d6abda2d1bf81dfd758a8fc872ea7def61572`.

### V11/C05 inline card

- Frontmatter is unchanged in the lane commit and in the proposed patch. The
  card review, update and inspection dates are already 2026-10-30;
  `content_verified_at` stays `null`. The new sources are supporting bindings,
  not new `evidence_scope` ids; see Frontmatter and evidence scope below.
- **Good-fit conditions** now require a shareable, versioned representation, a
  complete request key, an authorization boundary outside or bound to that key,
  and owned origin protection and purge.
- **Hard contraindications** now reject every-user-specific responses, an
  authorization header absent from the key, a purge contract that cannot meet
  freshness or revocation, and an unowned edge configuration.
- **Competing alternative** now names a private cache, origin cache or direct
  origin and reverses the choice on user-specific responses or an unenforceable
  purge contract.
- **Failure and recovery** now names stale private content, purge lag and
  downstream copies and points to the authorization matrix, stale-on-error and
  purge path in the owner section.
- **Sources** keeps the existing Microsoft static-hosting record and adds a
  bounded note that RFC 9111 and the Azure CDN and CloudFront pages were read on
  2026-10-30. The owner link is unchanged.
- The heading stays at line 419; the chapter page is 486 lines.
- Raw SHA-256:
  `9c1ab4b00aa2f634d507004b084d061899d5ea5a77956508997116efe37ec510`.
- Historical-view SHA-256:
  `43bc8722943241f9e3638396dd6facf5e2b83d4513d5e2df16d6137f7c6634f5`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was exercised in a detached
scratch copy of this worktree. The scratch results are in the Validation
section. The patch must not be merged until the book/atlas independent review
gate is satisfied.

### Source register `sources/register.json`

Add two source records. Set `updated` to 2026-10-30. The source count moves from
294 to 296.

- `src.azure-cdn` — title "Azure Content Delivery Network documentation";
  category "performance"; publisher "Microsoft Learn"; kind "official-docs";
  URL the how-caching page; resolved URL the same; topics
  `["network-architecture", "performance-engineering",
  "security-architecture"]`; priority "core"; planned use "Azure CDN
  cache-key, freshness, authorization and purge limits for the CDN / Edge
  Caching entry."; admission "admitted-for-research"; access
  "public-web-or-author-download"; reading status
  "full-public-page-inspected"; version records all three pages with their raw
  digests, canonical text digests, `ms.date` values and `git_commit_id` values
  from the Source binding section; `access_checked` and `content_verified`
  2026-10-30; license note "Public Microsoft documentation; cite short excerpts
  and paraphrase; do not mirror."; verification scope names the three page
  section sets, the classic-service retirement notice and the excluded linked
  pages; observed title "How caching works - Azure Content Delivery Network |
  Microsoft Learn".
- `src.cloudfront` — title "Amazon CloudFront Developer Guide"; category
  "performance"; publisher "Amazon Web Services"; kind "official-docs"; URL
  the cache-key page; resolved URL the same; topics the same three; priority
  "core"; planned use "CloudFront cache-key, Authorization-header, expiration
  and invalidation limits for the CDN / Edge Caching entry."; admission
  "admitted-for-research"; access "public-web-or-author-download"; reading
  status "full-public-page-inspected"; version records the four Markdown
  alternates with byte counts, SHA-256 values, Last-Modified times and ETags
  from the Source binding section; `access_checked` and `content_verified`
  2026-10-30; license note "Public AWS documentation; cite short excerpts and
  paraphrase; do not mirror."; verification scope names the four page section
  sets and the excluded linked pages; observed title "Amazon CloudFront
  Developer Guide".

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add eight records. Set `updated` to 2026-10-30. Records move from 175 to 183.
Each record is `status: read`, `reviewer: "Automated authoring agent"`, unit
type `documentation-page` except the RFC (`specification`), and uses the exact
URL, sections and `content_sha256` listed in the Source binding section.

- `read.azure-cdn-how-caching.2026-10-30` — `src.azure-cdn`; sections
  Introduction to caching, Content delivery network caching, Determining which
  files can be cached, Default caching behavior; raw HTML digest.
- `read.azure-cdn-caching-rules.2026-10-30` — `src.azure-cdn`; sections
  Caching behavior settings, Cache expiration duration, Global and custom rule
  processing order; raw HTML digest.
- `read.azure-cdn-purge.2026-10-30` — `src.azure-cdn`; section Purge contents
  from an Azure CDN endpoint; raw HTML digest.
- `read.cloudfront-cache-key.2026-10-30` — `src.cloudfront`; sections Default
  cache key, Customize the cache key; Markdown digest.
- `read.cloudfront-auth-header.2026-10-30` — `src.cloudfront`; section
  Configure CloudFront to forward the Authorization header; Markdown digest.
- `read.cloudfront-expiration.2026-10-30` — `src.cloudfront`; sections Use
  headers to control cache duration for individual objects, Specify the amount
  of time that CloudFront caches objects; Markdown digest.
- `read.cloudfront-invalidation.2026-10-30` — `src.cloudfront`; section Choose
  between invalidating files and using versioned file names; Markdown digest.
- `read.rfc9111-edge-cache.2026-10-30` — `src.rfc9111-enrichment`; sections
  3.5, 4, 4.1, 4.4, 5.2.2.5 and 5.2.2.7; RFC text digest.

Claims supported, claims not supported and limitations are bounded to the
selected sections; no implementation behavior, independent reproduction or
deployment configuration is claimed. The existing
`read.rfc9111-stale.2026-10-30` record remains unchanged.

### Source plan `edition/patterns/source-plan.v1.json`

Append eight units to `tycho.pattern.cdn-edge-caching` after the existing
Microsoft static-hosting unit, in the order used by the registry below. Use the
same source ids, labels, URLs, unit types, section lists, status `read` and
record ids as the Source binding section. Set `updated` to 2026-10-30. Summary:
`required_units` 212 -> 220; `read_units` 211 -> 219; `ledger_records` 175 ->
183. Replace the entry notes with: "The Azure and CloudFront pages support
cache-key, authorization, freshness and purge limits; RFC 9111 supports the
shared-cache and private-cache rules. The triad formulation and the
direct-origin name remain Tycho guidance." Recompute `registry_sha256` after
saving the registry and refresh `route_index_snapshot` from the rebuilt route
index.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.cdn-edge-caching`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to `partial-bounded`; keep
  `coverage.decision` at `partial-bounded`.
- Replace `source_units` with, in order: the existing Microsoft static-hosting
  unit; Azure how caching; Azure caching rules; Azure purge; CloudFront cache
  key; CloudFront Authorization header; CloudFront expiration; CloudFront
  invalidation; RFC 9111. All nine have status `read`.
- Replace `notes` with: "Invariant and alternative bound 2026-10-30 to RFC 9111
  and selected Azure CDN and CloudFront revisions; the triad formulation and
  direct-origin name remain Tycho guidance. Coverage partial-bounded; no
  promotion."
- Keep `review_status` `self-checked` and `atlas_owner` at V11/C05.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.cdn-edge-caching`:

- Keep `owner.line` at 131, the heading, the document id and the four unit
  terms unchanged.
- Invariant: `state: supported`; `quote: "The cache key, freshness policy and
  authorization boundary must agree."`; reason separates the RFC, Azure and
  CloudFront statements from the Tycho triad synthesis; primary binding
  `src.rfc9111-enrichment`, record `read.rfc9111-edge-cache.2026-10-30`,
  section "4. Constructing Responses from Caches", revision
  `aeb52adb...`; supporting bindings for Azure how caching, CloudFront
  Authorization and CloudFront expiration.
- Alternative: `state: supported`; `quote: "A direct origin or a private cache
  may be preferable when every response is user-specific or the purge contract
  cannot be enforced."`; reason separates the RFC private/no-store rules, the
  CloudFront key-or-disable-caching choice, the Azure bypass setting and the
  downstream-cache limits from the Tycho direct-origin and purge-completion
  rules; primary binding `src.rfc9111-enrichment`, record
  `read.rfc9111-edge-cache.2026-10-30`, section "5.2.2.7. private", revision
  `aeb52adb...`; supporting bindings for CloudFront Authorization, RFC no-store,
  Azure caching rules, Azure purge and CloudFront invalidation.
- Keep mechanism and failure/recovery states, quotes and bindings unchanged.
- `source_support`: keep the existing Microsoft static-hosting primary record
  and add auxiliary records for all eight new records listed above with their
  revisions. Set `technical_coverage` to `partial-bounded`; set `notes` to the
  registry notes above.
- Set `decision_evidence.competing_alternative` to the new card text: "A private
  cache, origin cache or direct origin. Reverse the choice when responses are
  user-specific or the purge contract cannot be enforced."
- Summary counters: `invariant_supported` 71 -> 72; `alternative_supported`
  68 -> 69; `technical_partial_bounded` 19 -> 20; `technical_partial` 77 ->
  76. No other counter changes.

### Card registration `edition/patterns/card-batches.v1.json`

Add `card_path`:
`book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md` to the
`tycho.pattern.cdn-edge-caching` entry. This is the same file as the chapter,
not a split. Without it, `preflight_sufficient.py` reports `card_path missing
or absent`. Keep `ledger_record` `read.batch3-ms-static.2026-10-21`.

### Frontmatter and evidence scope

The lane and the proposed metadata patch leave the owner page's
`evidence_scope` and `source_inspection_date`, and the V11/C05 frontmatter,
unchanged; the owner `updated_at` moves to 2026-10-30. The new Azure and
CloudFront sources are recorded in the
source register, reading ledger, source plan and owner-unit supporting bindings;
the card's primary `evidence_scope` continues to declare the existing RFC 9111
and Microsoft static-hosting sources. This avoids changing the owner/card
historical-view hashes and avoids extending the enrichment source-inspection
contract in the same lane.

If the integrator wants `src.azure-cdn` and `src.cloudfront` in
`evidence_scope.source_ids`, treat it as a separate change: add the two
inspection entries to `sources/enrichment-inspections-2026-10-20.json`, update
the owner `edition/enrichment-manifest.json` record's source ids, inspection
date and `sha256`, add the source ids to the card frontmatter, and recompute the
owner/card historical-view hashes and content revision values. Do not reuse the
`0d130ec2...` or `43bc8722...` values after that change.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B36 CDN / Edge Caching invariant and alternative source binding; no promotion
or owner acceptance." Because the proposed patch does not change frontmatter,
these lane-state historical-view hashes are also the final values for the
patch. They are:

- Owner path, previous (current authorized record):
  `e2729001cfb48486c8b3f847dd3092bbb18c36a5e71a519b8e2399e147c8f68c`;
  current:
  `0d130ec20d02d6e029e9ea863c2d6abda2d1bf81dfd758a8fc872ea7def61572`.
  Add this under `enrichment_documents` with key
  `book/volumes/v08/c08/edge-cache-origin.md`. Add the migration-baseline
  directory entry as well: previous
  `588128dd21b69bb523f421f47ff5c02aab045ea5b99bc113c460c1da04c5cae3`;
  current the same `0d130ec2...`; key the canonical owner path.
- Card path, previous (migration baseline):
  `4786dfa8a2e5df566ac69509e3fba7ccdc7b40840d8f91bde1a535b60ed1ea1f`;
  current:
  `43bc8722943241f9e3638396dd6facf5e2b83d4513d5e2df16d6137f7c6634f5`.
  Add under `directory_documents` with the V11/C05 README key.

Leave `source_blocks`, `enrichment_additions` and `enrichment_baselines`
empty. These are historical-view hashes, not the raw file hashes in the Book
edits section.

### Derived artifacts

The book edit changes one canonical owner page and one atlas chapter. The source
register gains two records, so regenerate `sources/CATALOG.md` (scratch count
296). The registry, card, source-plan and owner-unit changes make the route
index, atlas registry hash, edition inventory and the coverage, census and
reverse-map artifacts stale. Refresh them once at batch end; do not treat a
stale derived hash as a lane content failure. The atlas manifest must record
the new V11/C05 chapter SHA-256
`9c1ab4b00aa2f634d507004b084d061899d5ea5a77956508997116efe37ec510` and the
new registry SHA-256. The coverage map and reverse map must record the new
registry hash and route snapshot. The prior review recorded in
`edition/patterns/sufficient-candidates.v1.json` predates this edit and no
longer covers the changed owner page or card bytes. The book/atlas independent
review gate applies; do not update the recorded hash without a fresh review.
The prior review is historical evidence, not acceptance of this lane.

## Validation

Checker output in the lane worktree after the two book edits, before the
metadata patch:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_pattern_cards.py` — PASS, 11 batches, 145 entries.
- `python3 scripts/validate_book_metadata.py` — PASS, 489 documents.
- `python3 scripts/validate_pattern_owner_units.py` — expected FAIL on
  `owner-units-alternative` because the card's competing-alternative text is
  ahead of the unchanged owner-units JSON.
- `python3 scripts/validate_enrichment.py` — expected FAIL on
  `enrichment-new-document-drift` because the owner page hash is not yet
  authorized in `edition/content-revisions.json`.
- `python3 scripts/validate_sources.py` — expected FAIL because this note
  references `src.azure-cdn` and `src.cloudfront` before the register and
  catalogue patch. The register patch and `sources/CATALOG.md` regeneration are
  metadata needs.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.cdn-edge-caching` — expected FAIL on invariant, alternative and
  `card_path`.

In the detached scratch copy with the metadata patch:

    PASS: tycho.pattern.cdn-edge-caching
    1/1 entries preflight clean
    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern cards 11 batch(es), 145 entries

The scratch tree was not used to claim review, promotion or owner acceptance.
The full unit suite is not run; batch-end tests remain with the integrator. The
scratch patch did not regenerate `sources/CATALOG.md`, the route index or the
atlas/coverage artifacts, so their validators were not run there.

## Limits

The binding uses four Microsoft product pages (one previous-versions page), four
Amazon product pages and RFC 9111. The Azure pages describe the classic
Standard-from-Microsoft service or a previous-versions interface; the
CloudFront pages are living documentation pinned here by content digest and
HTTP metadata, with no published revision identifier. None of the selected
sources reports a deployment test, a purge measurement or an authorization
matrix. The triad sentence and the direct-origin name are Tycho synthesis; the
invariant and alternative states are `supported` only because the page
separates those Tycho additions from the source-supported statements. A
reviewer that requires every word of the owner quote to be source-quoted should
treat the dimensions as partial instead.

No independent AI review, owner acceptance, promotion or production observation
is claimed. The card remains inline in V11/C05, not V11/C02/C06; this lane did
not create a second card.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- the card path `book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.

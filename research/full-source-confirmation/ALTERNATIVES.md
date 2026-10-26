# Alternative and missing sources

Date: 2026-10-26. Refs #535.

## Found and read

- Enterprise Integration Patterns, Chapter 3 "Messaging Systems", author-hosted PDF:
  https://www.enterpriseintegrationpatterns.com/docs/EnterpriseIntegrationPatterns_HohpeWoolf_ch03.pdf
  - 42 pages, printed pp.57-97, SHA-256 c1e7125dcebfdd9a2b23a922dfbbc9694e5f8048e81e14dc95e2882043ac4f66.
  - Full sections: Message Channel, Message, Pipes and Filters, Message Router, Message Translator, Message Endpoint.
  - Does not contain the Chapter 4 channel patterns, so Publish-Subscribe and Point-to-Point remain partial.
- Enterprise Integration Patterns Pearson sample PDF:
  http://ptgmedia.pearsoncmg.com/images/9780321200686/samplepages/0321200683.pdf
  - 98 pages, front matter plus Chapters 1-3, SHA-256 b12e9c8323adf5d8b6a80c82b149edc8c0b1294682f9ec11f6782e7878781805.
  - No Chapter 4+ pattern text.
- PostgreSQL 18.6 section 26.3 Failover:
  https://www.postgresql.org/docs/current/warm-standby-failover.html
  - Full page read, 1 heading, 9 paragraphs, SHA-256 760a004bd1a4a30ebe112fcc36e453548e999f8ba94a84217be5b63b43593b7d.
- PostgreSQL 18.6 section 26.4 Hot Standby:
  https://www.postgresql.org/docs/current/hot-standby.html
  - Full page read, 6 headings, SHA-256 7b778a999ee64c5b9e01e1b81b575802496b9810c5615cd1a54b1cc11d7e850c.
- OWASP ASVS 5.0.0 complete PDF and CSV:
  https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf
  - 120 pages, 345 requirements, PDF SHA-256 a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5.

## Located but not readable without access

- Designing Data-Intensive Applications, Internet Archive lending copy:
  https://archive.org/details/designingdataint0000klep
  - Controlled digital lending; requires an account and borrowing, and full-text extraction is not
    available through the public page. No substitute copy was used.
- Designing Data-Intensive Applications, O'Reilly book page:
  https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/
  - Publisher page only; no full public text.
- Enterprise Integration Patterns, full book:
  - Publisher and booksellers sell the book; the official site serves only pattern tiles and the
    Chapter 3 PDF. Chapters 4-8 and the full pattern examples are not public.

## Consequence

- PostgreSQL read-replicas is no longer partial: section 26.4 was read.
- PostgreSQL failover remains partial: section 26.3 was read, but failback is absent.
- Pipes and Filters is now full: the complete section is in Chapter 3.
- The remaining ten EIP units stay partial because their full pattern sections are in Chapter 4 or later.
- DDIA remains blocked: only a controlled-lending copy was located, not an open full text.

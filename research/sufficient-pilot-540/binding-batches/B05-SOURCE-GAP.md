# B05 source representation gap

The B05 extractor found that the recorded `src.aws-caching-strategies` URL
redirects to a different page:

- recorded unit: `database-caching-strategies-using-redis/caching-patterns.html`;
- current final URL: `AmazonElastiCache/latest/dg/Strategies.html`;
- current title: "Caching strategies for Memcached";
- recorded sections "Caching patterns" and "Cache-Aside (Lazy Loading)" do not exist.

The current page has a Write-through heading and one exact quote, but it is not the
recorded unit. Write-behind/write-back and write-around are absent from the current
Microsoft caching guidance and from the redirected AWS page.

Disposition: no B05-B binding is accepted for these three entries. Write-through,
write-behind/write-back and write-around need a new admitted representation or an
explicit blocked/partial disposition. This is a source-revision gap, not a quote-quality
failure.

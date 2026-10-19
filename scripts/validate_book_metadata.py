#!/usr/bin/env python3
"""Read-only complete-corpus metadata, identity and taxonomy validation.

Checks references and draft metadata structure, never source truth or review.
The migration registry preserves minted identity; frontmatter owns live metadata.
"""
import json
from pathlib import Path
import re
import sys

from route_index import ROOT, canonical_scan, engine, FENCE


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(root=ROOT):
    root = Path(root).resolve()
    index = canonical_scan(root)  # Complete coverage, strict schemas and hierarchy.
    registry = json.loads((root / 'sources/document-identities.json').read_text())
    taxonomy = json.loads((root / 'sources/document-topics.json').read_text())
    require(registry['schema_version'] == 1, 'unsupported identity registry version')
    require(taxonomy['schema_version'] == 1, 'unsupported topic registry version')
    entries = registry['documents']
    identities = {r['canonical_path']: r for r in entries}
    require(len(identities) == len(entries), 'duplicate registered path')
    require(len({r['id'] for r in entries}) == len(entries), 'duplicate registered identity')
    require(set(identities) == {d['path'] for d in index['documents']},
            'identity registry differs from canonical corpus paths')
    topics = {t['id'] for t in taxonomy['topics']}
    require(len(topics) == len(taxonomy['topics']), 'duplicate taxonomy topic')
    require(all(re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', t) for t in topics),
            'invalid taxonomy topic')
    sources = {s['id'] for s in json.loads((root / 'sources/register.json').read_text())['sources']}
    claims = {c['id'] for c in json.loads((root / 'sources/claim-references.json').read_text())['claims']}
    yaml, _, _ = engine()
    for node in index['documents']:
        entry = identities[node['path']]
        require(entry['id'] == node['id'] and entry['kind'] == node['kind'],
                node['path'] + ': identity registry mismatch')
        require(set(node['topics']) <= topics, node['path'] + ': unknown taxonomy topic')
        require(set(node['source_ids']) <= sources, node['path'] + ': unknown source ID')
        require(set(node['claim_ids']) <= claims, node['path'] + ': unknown claim ID')
        text = (root / node['path']).read_text()
        meta = yaml.safe_load(FENCE.match(text).group(1))
        require(meta['authored_at'] == entry['authored_at'],
                node['path'] + ': authored date differs from recorded origin')
        require(meta['authored_at'] <= meta['updated_at'], node['path'] + ': inverted edit dates')
    return {'documents': len(index['documents']), 'coverage': index['coverage'],
            'topics': len(topics), 'snapshot_sha256': index['snapshot_sha256'],
            'scope': 'structural metadata and registry references, not independent content acceptance'}


if __name__ == '__main__':
    try:
        print(json.dumps(validate(), indent=2))
    except (ValueError, RuntimeError, OSError, KeyError) as exc:
        print('FAIL:', exc, file=sys.stderr)
        sys.exit(1)

#!/usr/bin/env python3
"""Read-only naming, identity and reversible path-only migration validation."""
import json
from pathlib import Path
import re
import sys

from assemble_edition import split
from content_revisions import authorized
from directory_paths import HistoricalView, MANIFEST, rewrite, sha
from route_index import canonical_scan

ROOT = Path(__file__).resolve().parents[1]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate(root=ROOT):
    root = Path(root)
    view = HistoricalView(root)
    m = view.manifest
    require(m is not None and m['schema_version'] == 1, 'directory-manifest-version')
    require(re.fullmatch(r'[0-9a-f]{40}', m['baseline_commit']) is not None, 'directory-baseline-commit')
    dirs = m['directories']
    require(len(dirs) == len(view.directories) == len(view.inverse) == 81, 'directory-map-uniqueness')
    for r in dirs:
        old, new = r['old'].split('/'), r['new'].split('/')
        require(len(old) == len(new) in (3, 4) and old[:2] == new[:2] == ['book', 'volumes'], 'directory-map-scope')
        for i, prefix in ((2, 'v'), (3, 'c')):
            if i >= len(old):
                continue
            require(re.fullmatch(prefix + r'(?:0[1-9]|[1-9][0-9])', old[i]) is not None, 'directory-original-number')
            require(re.fullmatch(re.escape(old[i]) + r'-[a-z0-9]+(?:-[a-z0-9]+)*', new[i]) is not None, 'directory-readable-name')
        require(not (root / r['old']).exists(), 'directory-old-directory-retained')
        require((root / r['new'] / 'README.md').is_file(), 'directory-missing-landing')
        if len(old) == 4:
            require('/'.join(new[:3]) == view.directories['/'.join(old[:3])], 'directory-parent-map')
    actual_dirs = {p.relative_to(root).as_posix() for p in (root / 'book/volumes').rglob('*') if p.is_dir()}
    require(actual_dirs == set(view.inverse), 'directory-unregistered-directory')
    required_history = {'edition/migration.json', 'edition/decomposition-plan.json', 'edition/decomposition-manifest.json', 'edition/enrichment-manifest.json'}
    require(set(m['protected_manifests']) == required_history, 'directory-historical-manifest-coverage')
    for path, digest in m['protected_manifests'].items():
        require(sha((root / path).read_text()) == digest, 'directory-historical-manifest-drift')
    records = m['documents']
    require(len(records) == len({r['old_path'] for r in records}) == len({r['new_path'] for r in records}) == len({r['id'] for r in records}) == m['canonical_documents'], 'directory-document-map-uniqueness')
    index = canonical_scan(root)
    require({(d['id'], d['path']) for d in index['documents']} == {(r['id'], r['new_path']) for r in records}, 'directory-document-membership')
    for r in records:
        require(view.current(r['old_path']) == r['new_path'], 'directory-document-destination')
        require(not (root / r['new_path']).is_symlink(), 'directory-symlink')
        text = (root / r['new_path']).read_text()
        meta, _ = split(text)
        require(meta['canonical_path'] == r['new_path'] and meta['parent_id'] == r['parent_id'] and meta['kind'] == r['kind'], 'directory-document-identity')
        original = view.read_text(r['old_path'])
        current_sha = sha(original)
        require(
            current_sha == r['baseline_sha256']
            or authorized(root, 'directory_documents', r['new_path'],
                          r['baseline_sha256'], current_sha),
            'directory-baseline-payload-drift')
        require(rewrite(original, r['old_path'], view.directories) == text, 'directory-non-reversible-edit')
        if r['old_path'] != r['new_path']:
            require(not (root / r['old_path']).exists(), 'directory-duplicate-old-path')
    outline = json.loads((root / 'edition/outline.json').read_text())
    for r in [*outline['volumes'], *outline['chapters']]:
        require(r['path'].rsplit('/', 1)[0] in view.inverse, 'directory-outline-path')
    require(len(outline['volumes']) == 10 and len(outline['chapters']) == 71, 'directory-outline-membership')
    return {'volumes': 10, 'chapters': 71, 'canonical_documents': len(records), 'moved_documents': sum(r['old_path'] != r['new_path'] for r in records), 'protected_historical_manifests': len(m['protected_manifests']), 'scope': 'reversible path-only edits and retained identities; not substantive acceptance'}


if __name__ == '__main__':
    try:
        print(json.dumps(validate(), indent=2))
    except (ValueError, OSError, KeyError) as error:
        print('FAIL:', error, file=sys.stderr)
        sys.exit(1)

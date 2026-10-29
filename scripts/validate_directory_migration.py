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
    post_dirs = m.get('post_migration_directories', [])
    require(len(post_dirs) == 12, 'directory-post-migration-directory-count')
    for item in post_dirs:
        path = item['path']
        require(path.startswith('book/volumes/') and (root / path).is_dir(), 'directory-post-migration-path')
        require(item['kind'] in ('volume', 'chapter'), 'directory-post-migration-kind')
        require(re.fullmatch(r'book/volumes/v(?:0[1-9]|[1-9][0-9])-[a-z0-9]+(?:-[a-z0-9]+)*', path) is not None
                or re.fullmatch(r'book/volumes/v(?:0[1-9]|[1-9][0-9])-[a-z0-9]+(?:-[a-z0-9]+)*/c(?:0[1-9]|[1-9][0-9])-[a-z0-9]+(?:-[a-z0-9]+)*', path) is not None,
                'directory-post-migration-name')
        require((root / path / 'README.md').is_file(), 'directory-post-migration-landing')
    v12_root = 'book/volumes/v12-modeling-simulation-and-decision-validation'
    v12_dirs = {v12_root}
    for path in (root / v12_root).iterdir():
        if path.is_dir():
            v12_dirs.add(path.relative_to(root).as_posix())
    actual_dirs = {p.relative_to(root).as_posix() for p in (root / 'book/volumes').rglob('*') if p.is_dir()}
    require(actual_dirs == set(view.inverse) | {item['path'] for item in post_dirs} | v12_dirs,
            'directory-unregistered-directory')
    required_history = {'edition/migration.json', 'edition/decomposition-plan.json', 'edition/decomposition-manifest.json', 'edition/enrichment-manifest.json'}
    require(set(m['protected_manifests']) == required_history, 'directory-historical-manifest-coverage')
    for path, digest in m['protected_manifests'].items():
        require(sha((root / path).read_text()) == digest, 'directory-historical-manifest-drift')
    records = m['documents']
    require(len(records) == len({r['old_path'] for r in records}) == len({r['new_path'] for r in records}) == len({r['id'] for r in records}) == m['canonical_documents'], 'directory-document-map-uniqueness')
    index = canonical_scan(root)
    require({(d['id'], d['path']) for d in index['documents'] if not d['path'].startswith(v12_root + '/')}
            == {(r['id'], r['new_path']) for r in records}, 'directory-document-membership')
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
    registered_dirs = set(view.inverse) | {item['path'] for item in post_dirs} | v12_dirs
    for r in [*outline['volumes'], *outline['chapters']]:
        require(r['path'].rsplit('/', 1)[0] in registered_dirs, 'directory-outline-path')
    require(len(outline['volumes']) == 12 and len(outline['chapters']) == 89, 'directory-outline-membership')
    return {'volumes': 12, 'chapters': 89, 'canonical_documents': len(records), 'moved_documents': sum(r['old_path'] != r['new_path'] for r in records), 'post_migration_directories': len(post_dirs), 'v12_directories': len(v12_dirs), 'protected_historical_manifests': len(m['protected_manifests']), 'scope': 'reversible path-only edits and retained identities; not substantive acceptance'}


if __name__ == '__main__':
    try:
        print(json.dumps(validate(), indent=2))
    except (ValueError, OSError, KeyError) as error:
        print('FAIL:', error, file=sys.stderr)
        sys.exit(1)

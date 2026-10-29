#!/usr/bin/env python3
"""Read-only ownership and conservation checks for explicitly authorized enrichment.

This supplements the historical 69-manuscript split checks; it never replaces
their payload/provenance protection or invents technical/independent acceptance.
"""
import json
from pathlib import Path

from assemble_edition import split, sha
from content_revisions import authorized
from route_index import canonical_scan
from directory_paths import HistoricalView

ROOT = Path(__file__).resolve().parents[1]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate(root=ROOT):
    root = Path(root)
    view = HistoricalView(root)
    manifest = json.loads((root/'edition/enrichment-manifest.json').read_text())
    require(manifest['schema_version'] == 1, 'enrichment-version')
    atlas_path = root/'edition/atlas-manifest.json'
    atlas = json.loads(atlas_path.read_text()) if atlas_path.is_file() else None
    atlas_ids = {item['id'] for item in atlas['documents']} if atlas else set()
    atlas_chapters = atlas['chapters'] if atlas else []
    index = canonical_scan(root)
    documents = {view.original(d['path']): d for d in index['documents']}
    current_ids = {d['id'] for d in index['documents']}
    retained = manifest['retained_document_ids']
    require(len(set(retained)) == len(retained) == manifest['baseline_canonical_documents'],
            'enrichment-baseline-membership')
    require(set(retained) <= current_ids, 'enrichment-lost-original-identity')
    additions = manifest['new_documents']
    require(len({r['path'] for r in additions}) == len(additions), 'enrichment-duplicate-path')
    require(len({r['id'] for r in additions}) == len(additions), 'enrichment-duplicate-id')
    require(not (set(retained) & {r['id'] for r in additions}), 'enrichment-reused-identity')
    require(current_ids == set(retained) | {r['id'] for r in additions} | atlas_ids,
            'enrichment-unregistered-document')
    sources = {s['id'] for s in json.loads((root/'sources/register.json').read_text())['sources']}
    inspections = json.loads((root/manifest['inspection_record']).read_text())['inspections']
    inspected = {x['source_id'] for x in inspections}
    for record in additions:
        path = record['path']
        require(path in documents, 'enrichment-missing-document')
        text = view.read_text(path)
        meta, body = split(text)
        current_sha = sha(text)
        require(current_sha == record['sha256']
                or authorized(root, 'enrichment_documents', path,
                              record['sha256'], current_sha),
                'enrichment-new-document-drift')
        require(all(meta[k] == record[k] for k in ('id', 'kind', 'parent_id', 'title')),
                'enrichment-document-identity')
        require(meta['route_hints']['questions'] == [record['question']],
                'enrichment-question-drift')
        require(meta['evidence_scope']['source_ids'] == record['source_ids'],
                'enrichment-source-drift')
        if record.get('origin_page'):
            # A verbatim split inherits the origin page's source bindings and
            # claims no new inspection; the record registers membership only.
            require(record['origin_page'] in documents, 'enrichment-split-origin')
            require(record['origin_page'] != path, 'enrichment-split-origin')
            require(set(record['source_ids']) <= sources, 'enrichment-uninspected-source')
        else:
            require(set(record['source_ids']) <= sources & inspected, 'enrichment-uninspected-source')
        require(meta['content_review']['status'] == 'self-checked'
                and meta['content_verified_at'] is None, 'enrichment-fabricated-acceptance')
        require(meta['source_inspection_date'] == record.get('source_inspection_date', '2026-10-20'),
                'enrichment-inspection-date')
        require(body.count('\n# ') == 1, 'enrichment-heading-count')
    edits = manifest['modified_documents']
    require(len({r['path'] for r in edits}) == len(edits), 'enrichment-duplicate-edit')
    for record in edits:
        require(record['path'] in documents, 'enrichment-missing-owner')
        text = view.read_text(record['path'])
        require(documents[record['path']]['id'] == record['id'], 'enrichment-owner-identity')
        heading = record['addition_heading'] + '\n'
        marker = record['insertion_marker']
        require(text.count(heading) == 1, 'enrichment-missing-or-duplicate-section')
        start = text.index(heading)
        end = text.find(marker, start)
        require(end > start, 'enrichment-insertion-boundary')
        addition_sha = sha(text[start:end])
        require(addition_sha == record['addition_sha256']
                or authorized(root, 'enrichment_additions', record['path'],
                              record['addition_sha256'], addition_sha),
                'enrichment-addition-drift')
        baseline_sha = sha(text[:start] + text[end:])
        require(baseline_sha == record['baseline_sha256']
                or authorized(root, 'enrichment_baselines', record['path'],
                              record['baseline_sha256'], baseline_sha),
                'enrichment-baseline-altered')
    outline = json.loads((root/'edition/outline.json').read_text())
    if atlas:
        require(outline['version'] == atlas['version'], 'enrichment-atlas-version')
    else:
        require(outline['version'] == manifest['version'], 'enrichment-edition-version')
    chapter_records = [r for r in additions if r['kind'] == 'chapter']
    chapters = [d for d in index['documents'] if d['kind'] == 'chapter']
    require(len(chapters) == manifest['baseline_chapters'] + len(chapter_records) + len(atlas_chapters),
            'enrichment-chapter-membership')
    require({c['id'] for c in outline['chapters']} == {d['id'] for d in chapters},
            'enrichment-outline-membership')
    for c in chapter_records:
        landing = view.read_text(c['path'])
        children = [r for r in additions if r['parent_id'] == c['id']]
        require(children and all(r['kind'] == 'page' for r in children),
                'enrichment-empty-chapter')
        require('## Purpose and mission' in landing and '## Chapter source ledger' in landing,
                'enrichment-chapter-contract')
        require(all(Path(r['path']).name in landing for r in children),
                'enrichment-chapter-route')
    return {'new_documents': len(additions), 'new_chapters': len(chapter_records),
            'atlas_documents': len(atlas_ids), 'atlas_chapters': len(atlas_chapters),
            'deepened_existing_pages': len(edits),
            'retained_document_ids': len(retained),
            'scope': 'explicit membership and byte conservation; not semantic acceptance'}


if __name__ == '__main__':
    import sys
    try:
        print(json.dumps(validate(), indent=2))
    except (ValueError, OSError, KeyError) as error:
        print('FAIL:', error, file=sys.stderr)
        sys.exit(1)

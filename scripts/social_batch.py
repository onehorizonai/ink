"""Validate immutable social review bundles and produce safe scheduling intents.

Provider writes belong to the connected Metricool MCP. This helper never posts.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


def digest(batch: dict) -> str:
    return hashlib.sha256(json.dumps(batch, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()


def validate(batch: dict) -> None:
    if batch.get('schemaVersion') != 1:
        raise ValueError('Unsupported batch schema')
    if not batch.get('profile') or not batch.get('workspaceId'):
        raise ValueError('Explicit profile and workspace required')
    seen = set()
    for post in batch['posts']:
        key = post['id']
        if key in seen:
            raise ValueError('Duplicate post ID')
        seen.add(key)
        if post['channel'] not in ('instagram', 'linkedin'):
            raise ValueError('Unsupported channel')
        if post['channel'] == 'linkedin' and batch['profile'] == 'factbase':
            raise ValueError('FactBase LinkedIn is disabled')
        limit = 2200 if post['channel'] == 'instagram' else 3000
        if not post['caption'].strip() or len(post['caption']) > limit:
            raise ValueError('Invalid caption length')
        if not 1 <= len(post['slides']) <= 10:
            raise ValueError('Expected one to ten images')
        for slide in post['slides']:
            image = Path(slide.get('image', ''))
            if slide.get('imageHash') and image.is_file() and hashlib.sha256(image.read_bytes()).hexdigest() != slide['imageHash']:
                raise ValueError('Rendered image changed after review')
            if not slide.get('alt', '').strip() or not slide.get('headline', '').strip():
                raise ValueError('Each slide needs a headline and alt text')
        if not post.get('sources'):
            raise ValueError('Sources are required')
        if post.get('mustFix'):
            raise ValueError('Unresolved Must Fix findings')


def scheduling_intents(batch: dict, approval: dict, ledger: dict, now: datetime, expected_reviewer: str) -> list:
    validate(batch)
    if approval.get('batchHash') != digest(batch) or approval.get('decision') != 'approved' or approval.get('reviewerId') != expected_reviewer or not expected_reviewer:
        raise ValueError('Explicit approval of this exact batch is required')
    result = []
    slots = set()
    for post in batch['posts']:
        stamp = datetime.fromisoformat(post['scheduledAt'])
        if stamp.tzinfo is None:
            raise ValueError('Scheduling requires an explicit UTC offset')
        slot = (post['channel'], stamp.astimezone(ZoneInfo('Europe/Amsterdam')).date().isoformat())
        if slot in slots:
            raise ValueError('At most one post per channel per day')
        slots.add(slot)
        key = hashlib.sha256((digest(batch) + ':' + post['id']).encode()).hexdigest()
        if key in ledger:
            continue  # Includes ambiguous writes: reconcile instead of retrying.
        if stamp <= now:
            continue  # Never dump missed slots into the next available day.
        urls = [slide.get('url', '') for slide in post['slides']]
        if any(not url.startswith('https://') for url in urls):
            raise ValueError('Upload reviewed images before scheduling')
        result.append({'idempotencyKey': key, 'brandId': batch['metricoolBrandId'], 'post': post})
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', type=Path)
    args = parser.parse_args()
    batch = json.loads(args.batch.read_text())
    validate(batch)
    print(json.dumps({'batchHash': digest(batch), 'posts': len(batch['posts'])}))

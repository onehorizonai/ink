"""Validate immutable social review bundles and produce safe scheduling intents.

Provider writes belong to the connected Metricool MCP. This helper never posts.
"""
from __future__ import annotations
import argparse
import copy
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
        expected_channels = ['instagram', 'facebook'] if post['channel'] == 'instagram' else ['linkedin']
        if post.get('channels') != expected_channels:
            raise ValueError('Instagram must also publish to Facebook; LinkedIn stays separate')
        if post['channel'] == 'linkedin' and len(post['slides']) > 1 and not post.get('documentTitle', '').strip():
            raise ValueError('LinkedIn carousel requires a document title')
        limit = 2200 if post['channel'] == 'instagram' else 3000
        if not post['caption'].strip() or len(post['caption']) > limit:
            raise ValueError('Invalid caption length')
        if not 1 <= len(post['slides']) <= 10:
            raise ValueError('Expected one to ten images')
        for slide_index, slide in enumerate(post['slides']):
            image = Path(slide.get('image', ''))
            if slide.get('imageHash') and image.is_file() and hashlib.sha256(image.read_bytes()).hexdigest() != slide['imageHash']:
                raise ValueError('Rendered image changed after review')
            payload_path = Path(slide.get('payload', ''))
            if payload_path.is_file():
                payload = json.loads(payload_path.read_text())
                expected_label = f"{slide_index + 1} / {len(post['slides'])}" if len(post['slides']) > 1 else ''
                if payload.get('slideLabel', '') != expected_label:
                    raise ValueError('Pagination must match the actual media count')
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


def metricool_payload(intent: dict) -> dict:
    """Build official ScheduledPost JSON for the connected MCP, without a write."""
    post = intent['post']
    stamp = datetime.fromisoformat(post['scheduledAt']).astimezone(ZoneInfo('Europe/Amsterdam'))
    info = {
        'text': post['caption'],
        'publicationDate': {'dateTime': stamp.strftime('%Y-%m-%dT%H:%M:%S'), 'timezone': 'Europe/Amsterdam'},
        'providers': [{'network': channel} for channel in post['channels']],
        'media': [slide['url'] for slide in post['slides']],
        'mediaAltText': [slide['alt'] for slide in post['slides']],
        'autoPublish': True, 'saveExternalMediaFiles': True, 'draft': False,
    }
    if post['channel'] == 'instagram':
        info['instagramData'] = {'autoPublish': True, 'type': 'POST'}
        info['facebookData'] = {'type': 'POST'}
    if post['channel'] == 'linkedin':
        carousel = len(post['slides']) > 1
        info['linkedinData'] = {'type': 'POST', 'publishImagesAsPDF': carousel, 'previewIncluded': False}
        if carousel: info['linkedinData']['documentTitle'] = post['documentTitle']
    return {'blogId': str(intent['brandId']), 'date': post['scheduledAt'], 'info': json.dumps(info, ensure_ascii=False)}


def metricool_update_payload(brand_id: str, current: dict, post: dict) -> dict:
    """Preserve current post fields while applying an explicitly approved replacement."""
    expected = json.loads(metricool_payload({'brandId': brand_id, 'post': post})['info'])
    info = copy.deepcopy(current)
    info.update(text=expected['text'], media=expected['media'], mediaAltText=expected['mediaAltText'], saveExternalMediaFiles=True)
    providers = {provider['network']: provider for provider in current['providers']}
    info['providers'] = [providers.get(network, {'network': network}) for network in post['channels']]
    network_fields = {'twitterData':'twitter', 'facebookData':'facebook', 'instagramData':'instagram', 'linkedinData':'linkedin', 'pinterestData':'pinterest', 'youtubeData':'youtube', 'tiktokData':'tiktok', 'threadsData':'threads', 'blueskyData':'bluesky', 'twitchData':'twitch', 'gmbData':'gmb'}
    for field, network in network_fields.items():
        if network not in post['channels']:
            info.pop(field, None)  # The provider rejects unselected network defaults from read-back.
        elif field in expected:
            info[field] = dict(info.get(field) or {}, **expected[field])
    return {'blogId':str(brand_id), 'id':str(current['id']), 'uuid':current['uuid'], 'info':json.dumps(info, ensure_ascii=False)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', type=Path)
    args = parser.parse_args()
    batch = json.loads(args.batch.read_text())
    validate(batch)
    print(json.dumps({'batchHash': digest(batch), 'posts': len(batch['posts'])}))

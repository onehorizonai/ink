"""Publish a reviewed release log with a single local writer; never upload article text.

This is separate from the images-only upload tool. It reuses its storage signing client.
"""
from __future__ import annotations
import argparse
import os
import hashlib
import importlib.util
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
AMSTERDAM = ZoneInfo('Europe/Amsterdam')


def validate_records(records, now):
    seen = set()
    for record in records:
        if set(record) - {'slug','date','modified','hash','publishedAt','sourceReviewedAt'}:
            raise ValueError('Release records cannot contain article text or extra metadata')
        if record.get('modified',record['date']) < record['date']: raise ValueError('Modification predates original publication')
        if record.get('modified',record['date']) > now.astimezone(AMSTERDAM).date().isoformat():
            raise ValueError('Future records cannot enter the public log')
        if len(record['hash']) != 64 or any(c not in '0123456789abcdef' for c in record['hash']):
            raise ValueError('A reviewed SHA-256 content hash is required')
        key = (record['slug'], record['hash'])
        if key in seen: raise ValueError('Duplicate release record')
        seen.add(key)
        if 'publishedAt' in record or 'sourceReviewedAt' in record:
            published = datetime.fromisoformat(record['publishedAt'])
            reviewed = datetime.fromisoformat(record['sourceReviewedAt'])
            if published.tzinfo is None or reviewed.tzinfo is None:
                raise ValueError('Explicit timestamp offsets are required')
            if not reviewed <= published <= now:
                raise ValueError('Invalid review/publication chronology')
            if any(t.astimezone(AMSTERDAM).date().isoformat() != record.get('modified',record['date']) for t in [reviewed,published]):
                raise ValueError('Source review and actual publication must be on the stated day')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', required=True)
    parser.add_argument('--records', type=Path, required=True)
    parser.add_argument('--key', default='publication/releases.json')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        validate_records(json.loads(args.records.read_text()), datetime.now(AMSTERDAM))
        print('Release records valid'); return
    lock_directory=ROOT/'.local/locks'
    lock_directory.mkdir(parents=True,exist_ok=True)
    # The configured Supabase S3 endpoint ignores conditional PUT headers.
    # Every writer must run here under this exclusive local lock.
    import re
    if not re.fullmatch(r'[a-z0-9-]+',args.profile): raise ValueError('Invalid profile ID')
    lock=lock_directory/f'{args.profile}-publication.lock'
    descriptor=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
    try:
        os.write(descriptor,str(os.getpid()).encode())
        publish(args)
    finally:
        os.close(descriptor)
        lock.unlink()


def publish(args):
    records = json.loads(args.records.read_text())
    validate_records(records, datetime.now(AMSTERDAM))
    if args.check:
        print('Release records valid'); return
    spec = importlib.util.spec_from_file_location('ink_storage_signing', ROOT/'.agents/blog-image-uploader/mcp/blog-image-s3/server.py')
    module = importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module);module.REPO_ROOT=ROOT
    config=module.load_config({'profile':args.profile,'profile_config':str(ROOT/'.local/context/ink-profiles.local.json')})
    client=module.S3Client(config)
    url,host,uri=client._build_request_target(args.key)
    headers=client._signed_headers('GET',host,uri,'','',{})
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30) as response:
            previous=json.loads(response.read())
        # Preserve approved history and rollback hashes.
        if any(record not in records for record in previous):
            raise ValueError('Refusing to remove existing release history')
    except urllib.error.HTTPError as error:
        if error.code!=404: raise
    body=(json.dumps(records,ensure_ascii=False,indent=2)+'\n').encode()
    extra={'content-type':'application/json','cache-control':'public, max-age=0, must-revalidate'}
    headers=client._signed_headers('PUT',host,uri,'',hashlib.sha256(body).hexdigest(),extra)
    with urllib.request.urlopen(urllib.request.Request(url,data=body,headers=headers,method='PUT'),timeout=30) as response:
        print('Release log written:',response.status,client.public_url(args.key))
    # Verify the public endpoint, not only the authenticated object write.
    with urllib.request.urlopen(client.public_url(args.key),timeout=30) as response:
        if json.loads(response.read()) != records: raise RuntimeError('Public release log does not match the reviewed records')

if __name__=='__main__': main()

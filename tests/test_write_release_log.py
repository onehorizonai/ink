import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from write_release_log import validate_records
class ReleaseLogTests(unittest.TestCase):
    def test_future_metadata_and_backdating_are_rejected(self):
        now=datetime(2026,11,2,12,tzinfo=timezone.utc)
        record=dict(slug='fictional',date='2026-11-03',hash='a'*64)
        with self.assertRaises(ValueError): validate_records([record],now)
        record.update(date='2026-11-02',title='Unexpected draft text')
        with self.assertRaises(ValueError): validate_records([record],now)
        del record['title'];record.update(publishedAt='2026-11-02T11:00:00+00:00',sourceReviewedAt='2026-11-01T12:00:00+00:00')
        with self.assertRaises(ValueError): validate_records([record],now)

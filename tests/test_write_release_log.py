import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from write_release_log import validate_records, validate_history
class ReleaseLogTests(unittest.TestCase):
    def test_future_metadata_and_backdating_are_rejected(self):
        now=datetime(2026,11,2,12,tzinfo=timezone.utc)
        record=dict(slug='fictional',date='2026-11-03',hash='a'*64)
        with self.assertRaises(ValueError): validate_records([record],now)
        record.update(date='2026-11-02',title='Unexpected draft text')
        with self.assertRaises(ValueError): validate_records([record],now)
        del record['title'];record.update(publishedAt='2026-11-02T11:00:00+00:00',sourceReviewedAt='2026-11-01T12:00:00+00:00')
        with self.assertRaises(ValueError): validate_records([record],now)

    def test_explicit_backfills_keep_real_release_day_timestamps(self):
        now=datetime(2026,11,6,12,tzinfo=timezone.utc)
        record=dict(slug='fictional',date='2026-11-03',hash='a'*64,backfill=True,
                    sourceReviewedAt='2026-11-06T09:00:00+00:00',publishedAt='2026-11-06T10:00:00+00:00')
        validate_records([record],now)
        for change in [dict(backfill='true'),dict(backfill=False),dict(modified='2026-11-06'),
                       dict(date='2026-11-06'),dict(sourceReviewedAt='2026-11-05T09:00:00+00:00'),
                       dict(publishedAt='2026-11-07T10:00:00+00:00')]:
            with self.subTest(change=change), self.assertRaises(ValueError): validate_records([{**record,**change}],now)
        with self.assertRaises(ValueError): validate_records([{k:v for k,v in record.items() if k!='publishedAt'}],now)
        with self.assertRaises(ValueError): validate_records([{k:v for k,v in record.items() if k!='backfill'}],now)

    def test_new_backfills_require_explicit_write_authorization_but_history_remains_reusable(self):
        record=dict(slug='fictional',date='2026-11-03',hash='a'*64,backfill=True)
        with self.assertRaises(ValueError): validate_history([record],[])
        validate_history([record],[],allow_backfill=True)
        validate_history([record],[record])
        with self.assertRaises(ValueError): validate_history([],[record],allow_backfill=True)

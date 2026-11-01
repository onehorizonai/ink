import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from social_batch import digest, scheduling_intents, validate

class SocialBatchTests(unittest.TestCase):
    def batch(self):
        return dict(schemaVersion=1, profile='fit-horizon', workspaceId='fictional-workspace', metricoolBrandId='fictional-brand', posts=[dict(id='one', channel='instagram', caption='A useful caption', sources=['https://example.com'], scheduledAt='2099-01-01T18:00:00+01:00', slides=[dict(headline='Useful', alt='Useful text', url='https://example.com/image.png')])])
    def test_stale_approval_is_rejected(self):
        batch=self.batch(); approval=dict(batchHash=digest(batch),decision='approved',reviewerId='reviewer'); batch['posts'][0]['caption']='Changed'
        with self.assertRaises(ValueError): scheduling_intents(batch,approval,{},datetime.now(timezone.utc), "reviewer")
    def test_uncertain_writes_are_not_retried(self):
        batch=self.batch(); approval=dict(batchHash=digest(batch),decision='approved',reviewerId='reviewer')
        intent=scheduling_intents(batch,approval,{},datetime.now(timezone.utc), "reviewer")[0]
        self.assertEqual(scheduling_intents(batch,approval,{intent['idempotencyKey']:{'status':'uncertain'}},datetime.now(timezone.utc), "reviewer"),[])
    def test_factbase_linkedin_is_disabled(self):
        batch=self.batch(); batch['profile']='factbase'; batch['posts'][0]['channel']='linkedin'
        with self.assertRaises(ValueError): validate(batch)

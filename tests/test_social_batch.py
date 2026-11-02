import sys
import json
import unittest
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from social_batch import digest, scheduling_intents, validate, metricool_payload, metricool_update_payload

class SocialBatchTests(unittest.TestCase):
    def batch(self):
        return dict(schemaVersion=1, profile='fit-horizon', workspaceId='fictional-workspace', metricoolBrandId='fictional-brand', posts=[dict(id='one', channel='instagram', channels=['instagram','facebook'], caption='A useful caption', sources=['https://example.com'], scheduledAt='2099-01-01T18:00:00+01:00', slides=[dict(headline='Useful', alt='Useful text', url='https://example.com/image.png')])])
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

    def test_metricool_payload_preserves_order_alt_and_native_caption(self):
        batch=self.batch(); approval=dict(batchHash=digest(batch),decision='approved',reviewerId='reviewer')
        intent=scheduling_intents(batch,approval,{},datetime.now(timezone.utc),'reviewer')[0]
        payload=metricool_payload(intent); info=json.loads(payload['info'])
        self.assertEqual(info['text'],batch['posts'][0]['caption'])
        self.assertEqual(info['mediaAltText'],['Useful text'])
        self.assertEqual(info['publicationDate']['timezone'],'Europe/Amsterdam')
        self.assertFalse(info['draft'])

    def test_instagram_crossposts_to_facebook(self):
        batch=self.batch();info=json.loads(metricool_payload({'brandId':'fictional-brand','post':batch['posts'][0]})['info'])
        self.assertEqual([p['network'] for p in info['providers']],['instagram','facebook'])
        self.assertEqual(info['facebookData']['type'],'POST')
    def test_linkedin_carousel_needs_title_and_uses_pdf_conversion(self):
        batch=self.batch();p=batch['posts'][0];p.update(channel='linkedin',channels=['linkedin']);p['slides']*=2
        with self.assertRaisesRegex(ValueError,'document title'):validate(batch)
        p['documentTitle']='A useful document';validate(batch)
        info=json.loads(metricool_payload({'brandId':'fictional-brand','post':p})['info'])
        self.assertTrue(info['linkedinData']['publishImagesAsPDF'])
        self.assertEqual(info['linkedinData']['documentTitle'],'A useful document')
        self.assertEqual(info['providers'],[{'network':'linkedin'}])
    def test_instagram_without_facebook_is_rejected(self):
        batch=self.batch();batch['posts'][0]['channels']=['instagram']
        with self.assertRaisesRegex(ValueError,'Facebook'):validate(batch)

    def test_update_preserves_manual_fields_and_selected_tags(self):
        post=self.batch()['posts'][0]
        current={'id':1,'uuid':'fictional-uuid','text':'old','providers':[{'network':'instagram','status':'PENDING'}],'twitterData':{'type':'POST'},'instagramData':{'carouselTags':{'0':[{'username':'fictional','x':.5,'y':.5}]},'showReelOnFeed':False},'firstCommentText':'Keep this','location':{'name':'Fictional location'}}
        result=metricool_update_payload('fictional-brand',current,post);info=json.loads(result['info'])
        self.assertNotIn('twitterData',info)
        self.assertEqual(info['instagramData']['carouselTags'],current['instagramData']['carouselTags'])
        self.assertFalse(info['instagramData']['showReelOnFeed'])
        self.assertEqual(info['location'],current['location']);self.assertEqual(info['firstCommentText'],'Keep this')
        self.assertEqual(current['text'],'old')
    def test_single_image_pagination_is_rejected(self):
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'payload.json';path.write_text(json.dumps({'slideLabel':'1 / 6'}))
            batch=self.batch();batch['posts'][0]['slides'][0]['payload']=str(path)
            with self.assertRaisesRegex(ValueError,'Pagination'):validate(batch)
            path.write_text(json.dumps({'slideLabel':''}));validate(batch)

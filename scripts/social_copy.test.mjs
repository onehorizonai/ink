import {test} from 'node:test'
import assert from 'node:assert/strict'
import {validateAudienceCopy,visibleSocialCopy} from './social_copy.mjs'

test('keeps production commentary out of public art and captions',()=>{
 for(const text of ['Actual Fit Horizon anatomy — illustrative pose','These are actual catalog poses, not a support-point comparison','Actual catalog movement, not an injury treatment claim','Uitsnede van het echte werkdocument','Fictional contract note','The image does not verify an anchor'])assert.throws(()=>validateAudienceCopy([text]))
})
test('allows useful instruction, examples, factual limits and attribution',()=>{
 validateAudienceCopy(['Keep the heel down.','Example: retry the interrupted upload.','2 RIR is an estimate of reps remaining.','Local inference does not describe connected tools.','Anatomy: Z-Anatomy, CC BY-SA 4.0.'])
 const payload={headline:'Choose a manageable position.',visual:{note:'Control the return.',images:[{source:'Actual catalog capture',alt:'Actual anatomy pose'}]}}
 assert.doesNotThrow(()=>validateAudienceCopy(visibleSocialCopy(payload)))
})

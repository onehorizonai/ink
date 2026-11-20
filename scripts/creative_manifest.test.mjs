import {test} from 'node:test'
import assert from 'node:assert/strict'
import {validateCreativeManifest} from './creative_manifest.mjs'
const manifest=()=>({profile:'factbase',reviewOnly:true,templateVersion:8,directions:Array.from({length:8},(_,i)=>({id:`FB${i}`,brief:'Useful specific lesson',sources:['production'],kind:i===0?'carousel':'pair',captionLength:i<6?'substantial':'medium',captions:{instagram:'x'.repeat(i<6?1400:800),linkedin:'y'.repeat(i<6?1800:800)},slides:Array.from({length:i===0?6:2},()=>({payload:'a.json',image:'a.png',alt:'Visible lesson'}))}))})
test('review manifest enforces brand, teaching copy and complete sequences',()=>{
 assert.equal(validateCreativeManifest(manifest(),'factbase').directions.length,8)
 for(const edit of [m=>m.reviewOnly=false,m=>m.profile='other',m=>m.directions[0].slides.pop(),m=>m.directions[2].captions.linkedin='short',m=>m.directions[1].id='FB0',m=>m.directions[7].captionLength='short']){const m=manifest();edit(m);assert.throws(()=>validateCreativeManifest(m,'factbase'))}
})

test('captions cannot leak capture commentary into a review bundle',()=>{
 const m=manifest();m.directions[0].captions.instagram='Actual Fit Horizon anatomy — illustrative pose. '+'x'.repeat(1300)
 assert.throws(()=>validateCreativeManifest(m,'factbase'),/disclaimers/)
})

test('image-specific captions must be safe and belong to the selected image',()=>{
 const m=manifest();m.directions[1].captionsByImage={missing:{instagram:'Useful',linkedin:'Useful'}}
 assert.throws(()=>validateCreativeManifest(m,'factbase'),/match an image/)
 m.directions[1].captionsByImage={a:{instagram:'Useful photo edition',linkedin:'Useful photo edition'}}
 validateCreativeManifest(m,'factbase')
 m.directions[1].captionsByImage.a.instagram='Nog niet bevestigd'
 assert.throws(()=>validateCreativeManifest(m,'factbase'),/disclaimers/)
})

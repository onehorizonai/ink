import { readFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import {validateAudienceCopy} from './social_copy.mjs'

export function validateCreativeManifest(manifest, profile) {
 if(manifest.profile!==profile || manifest.reviewOnly!==true || manifest.templateVersion!==8) throw new Error('Explicit review profile/version required')
 if(manifest.directions?.length!==8 || new Set(manifest.directions.map(d=>d.id)).size!==8) throw new Error('Eight unique directions required')
 let images=0,carousels=0,substantial=0
 for(const d of manifest.directions){
  if(!d.brief?.trim() || !d.sources?.length) throw new Error('Direction requires a brief and sources')
  if(!['substantial','medium'].includes(d.captionLength)) throw new Error('Choose a declared caption length')
  const n=d.slides?.length
  if(d.kind==='carousel'){if(n!==6)throw new Error('One complete six-slide carousel required');carousels++}
  else if(d.kind!=='pair' || n!==2)throw new Error('A study is a pair or complete carousel')
  images+=n
  for(const channel of ['instagram','linkedin']){
   const caption=d.captions?.[channel];if(typeof caption!=='string')throw new Error('Both channel-native captions required')
   validateAudienceCopy([caption])
   const [min,max]=d.captionLength==='substantial'?(channel==='instagram'?[1200,2200]:[1500,3000]):[600,1100]
   if([...caption].length<min || [...caption].length>max)throw new Error(`${d.id} ${channel} caption outside ${min}–${max}`)
  }
  for(const [imageId,captions]of Object.entries(d.captionsByImage??{})){
   if(!d.slides.some(s=>s.image.replace(/\\/g,'/').split('/').pop()===imageId+'.png'))throw new Error('Caption variant must match an image')
   for(const channel of ['instagram','linkedin']){
    const copy=captions[channel]
    if(typeof copy!=='string'||!copy.trim()||[...copy].length>(channel==='instagram'?2200:3000))throw new Error('Invalid image-specific caption')
    validateAudienceCopy([copy])
   }
  }
  if(d.captionLength==='substantial')substantial++
  for(const slide of d.slides)if(!slide.alt?.trim() || !slide.payload || !slide.image)throw new Error('Slide requires payload, image and alt')
 }
 if(images!==20||carousels!==1||substantial!==6)throw new Error('Expected 20 images, one carousel and six substantial directions')
 return manifest
}
/** Alternative studies use distinct photographs, even if one source was resized. */
export async function validateCreativePhotos(manifest) {
 const ids=new Set(),hashes=new Set()
 for(const d of manifest.directions)for(const slide of d.slides){
  const payload=JSON.parse(await readFile(slide.payload,'utf8'))
  for(const asset of payload.visual?.images??[])if(asset.kind==='photography'){
   const id=asset.photoId??asset.source
   if(ids.has(id)||hashes.has(asset.sha256))throw new Error('Use a different photograph for every creative image')
   ids.add(id);hashes.add(asset.sha256)
  }
 }
}
/** One concept may share a photograph across channels, never across concepts/slides. */
export async function validateBatchPhotos(batch) {
 const ids=new Map(),hashes=new Map(),payloads=new Map()
 for(const post of batch.posts)for(const [slideIndex,slide]of post.slides.entries()){
  if(!payloads.has(slide.payload))payloads.set(slide.payload,JSON.parse(await readFile(slide.payload,'utf8')))
  const images=payloads.get(slide.payload).visual?.images??[]
  for(const [assetIndex,asset]of images.entries())if(asset.kind==='photography'){
   const id=asset.photoId??asset.source,hash=asset.sha256,owner=JSON.stringify([post.conceptId??post.id,slideIndex,assetIndex])
   if(!id||!/^[a-f0-9]{64}$/.test(hash??''))throw new Error('Photographs require a source identity and SHA-256')
   if((ids.has(id)&&ids.get(id)!==owner)||(hashes.has(hash)&&hashes.get(hash)!==owner))throw new Error('Use a different photograph for each concept and slide; only channel adaptations may share it')
   ids.set(id,owner);hashes.set(hash,owner)
  }
 }
}
export async function creativeHash(manifest){
 const records=[]
 for(const d of manifest.directions)for(const s of d.slides){records.push([s.image,createHash('sha256').update(await readFile(s.image)).digest('hex')]);records.push([s.payload,createHash('sha256').update(await readFile(s.payload)).digest('hex')])}
 return createHash('sha256').update(JSON.stringify({manifest,records})).digest('hex')
}

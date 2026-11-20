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
  if(d.captionLength==='substantial')substantial++
  for(const slide of d.slides)if(!slide.alt?.trim() || !slide.payload || !slide.image)throw new Error('Slide requires payload, image and alt')
 }
 if(images!==20||carousels!==1||substantial!==6)throw new Error('Expected 20 images, one carousel and six substantial directions')
 return manifest
}
export async function creativeHash(manifest){
 const records=[]
 for(const d of manifest.directions)for(const s of d.slides){records.push([s.image,createHash('sha256').update(await readFile(s.image)).digest('hex')]);records.push([s.payload,createHash('sha256').update(await readFile(s.payload)).digest('hex')])}
 return createHash('sha256').update(JSON.stringify({manifest,records})).digest('hex')
}

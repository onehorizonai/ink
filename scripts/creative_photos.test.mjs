import {test} from 'node:test'
import assert from 'node:assert/strict'
import {mkdtemp,writeFile,rm}from'node:fs/promises'
import os from'node:os'
import path from'node:path'
import {validateCreativePhotos,validateBatchPhotos}from'./creative_manifest.mjs'

test('distinct photo files cannot conceal reuse of one photograph',async()=>{
 const folder=await mkdtemp(path.join(os.tmpdir(),'ink-photos-'))
 try{
  const a=path.join(folder,'a.json'),b=path.join(folder,'b.json')
  const save=(file,id,hash,kind='photography')=>writeFile(file,JSON.stringify({visual:{images:[{kind,photoId:id,sha256:hash}]}}))
  const manifest={directions:[{slides:[{payload:a},{payload:b}]}]}
  await save(a,'first','hash-one');await save(b,'second','hash-two');await validateCreativePhotos(manifest)
  await save(b,'first','resized-hash');await assert.rejects(()=>validateCreativePhotos(manifest),/different photograph/)
  await save(b,'renamed-id','hash-one');await assert.rejects(()=>validateCreativePhotos(manifest),/different photograph/)
  await save(b,'first','hash-one','product');await validateCreativePhotos(manifest)
 }finally{await rm(folder,{recursive:true,force:true})}
})

test('routine batches share photos only between channel adaptations of one slide',async()=>{
 const folder=await mkdtemp(path.join(os.tmpdir(),'ink-batch-photos-'))
 try{
  const a=path.join(folder,'a.json'),b=path.join(folder,'b.json')
  const save=(file,id,hash)=>writeFile(file,JSON.stringify({visual:{images:[{kind:'photography',photoId:id,sha256:hash}]}}))
  await save(a,'photo-one','a'.repeat(64));await save(b,'photo-two','b'.repeat(64))
  const post=(id,conceptId,payload)=>({id,conceptId,slides:[{payload}]})
  await validateBatchPhotos({posts:[post('ig','lesson',a),post('li','lesson',a),post('second','other',b)]})
  await assert.rejects(()=>validateBatchPhotos({posts:[post('ig','lesson',a),post('other','different',a)]}),/different photograph/)
  await assert.rejects(()=>validateBatchPhotos({posts:[{id:'ig',conceptId:'lesson',slides:[{payload:a},{payload:a}]}]}),/different photograph/)
  await save(b,'photo-one','c'.repeat(64))
  await assert.rejects(()=>validateBatchPhotos({posts:[post('ig','lesson',a),post('other','different',b)]}),/different photograph/)
  await save(b,'renamed-photo','a'.repeat(64))
  await assert.rejects(()=>validateBatchPhotos({posts:[post('ig','lesson',a),post('other','different',b)]}),/different photograph/)
 }finally{await rm(folder,{recursive:true,force:true})}
})

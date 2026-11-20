import {test} from 'node:test'
import assert from 'node:assert/strict'
import {mkdtemp,writeFile,rm}from'node:fs/promises'
import os from'node:os'
import path from'node:path'
import {validateCreativePhotos}from'./creative_manifest.mjs'

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

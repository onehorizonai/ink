import {test} from 'node:test'
import assert from 'node:assert/strict'
import {mkdtemp,writeFile,symlink,rm,mkdir} from 'node:fs/promises'
import os from 'node:os'
import path from 'node:path'
import {createHash} from 'node:crypto'
import {creativeAssets} from './creative_assets.mjs'

test('review captures require explicit review state and remain inside their run, including symlinks',async()=>{
 const root=await mkdtemp(path.join(os.tmpdir(),'creative-assets-'))
 try {
  await mkdir(path.join(root,'run'));await writeFile(path.join(root,'run','capture.png'),'fixture')
  await writeFile(path.join(root,'outside.png'),'outside');await symlink(path.join(root,'outside.png'),path.join(root,'run','escape.png'))
  const file=path.join(root,'run','frame.json'),contract={assetCounts:{macro:[1,2]}}
  const asset={sha256:createHash('sha256').update('fixture').digest('hex'),file:'capture.png',kind:'product',alt:'An actual source panel',source:'owning-repo/component@revision'}
  const payload={reviewOnly:true,templateVersion:8,layout:'macro',visual:{images:[asset]}}
  assert.match((await creativeAssets(payload,contract,file)).image0Url,/^data:image\/png;base64,/)
  await assert.rejects(creativeAssets({...payload,reviewOnly:false},contract,file),/review candidates/)
  await assert.rejects(creativeAssets({...payload,visual:{images:[]}},contract,file),/asset count/)
  for(const name of ['../outside.png','escape.png']) await assert.rejects(creativeAssets({...payload,visual:{images:[{...asset,file:name}]}},contract,file),/escaped/)
  await assert.rejects(creativeAssets({...payload,visual:{images:[{...asset,source:''}]}},contract,file),/real source/)
  await assert.rejects(creativeAssets({...payload,visual:{images:[{...asset,sha256:'0'.repeat(64)}]}},contract,file),/hash does not match/)
 }finally{await rm(root,{recursive:true,force:true})}
})

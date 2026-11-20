// Review experiments use an explicit adapter. Production profiles are never switched here.
import { readFile, writeFile } from 'node:fs/promises'
import { spawn } from 'node:child_process'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import {validateCreativeManifest,creativeHash} from './creative_manifest.mjs'
const [profile,manifestPath,adapterPath]=process.argv.slice(2)
if(!adapterPath)throw new Error('Usage: render_creative.mjs profile manifest.json explicit-adapter.json')
const manifest=validateCreativeManifest(JSON.parse(await readFile(manifestPath,'utf8')),profile)
const a=JSON.parse(await readFile(adapterPath,'utf8'))
const c=JSON.parse(await readFile(path.join(path.dirname(a.template),'template-contract.json'),'utf8'))
if(a.profile!==profile || c.profile!==profile || !c.reviewOnly)throw new Error('Review adapter brand mismatch')
const renderer=path.join(path.dirname(fileURLToPath(import.meta.url)),'render_social.mjs')
for(const d of manifest.directions)for(const s of d.slides){
 await new Promise((resolve,reject)=>{const child=spawn(process.execPath,[renderer,a.template,s.payload,s.image,a.browserModule,a.font],{stdio:'inherit',shell:false});child.on('error',reject);child.on('close',code=>code===0?resolve():reject(new Error('Render failed: '+s.image)))})
 console.log(path.basename(s.image))
}
await writeFile(path.join(path.dirname(manifestPath),'creative-hash.txt'),await creativeHash(manifest)+'\n')

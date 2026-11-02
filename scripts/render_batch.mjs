// Render one explicitly selected profile using its brand-owned template or CLI.
import { readFile, writeFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { spawn } from 'node:child_process'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const [profile, batchPath, registryPath = path.join(root,'.local/context/ink-profiles.local.json')] = process.argv.slice(2)
if(!profile || !batchPath) throw new Error('Usage: render_batch.mjs profile batch.json [registry.json]')
const config = JSON.parse(await readFile(registryPath,'utf8')).profiles[profile]
const batch = JSON.parse(await readFile(batchPath,'utf8'))
if(!config || batch.profile !== profile || batch.workspaceId !== config.workspaceId) throw new Error('Profile/workspace mismatch')
const renderer=config.socialRenderer
if(!renderer) throw new Error('Selected profile has no socialRenderer')
if(renderer.kind==='html'){
 const contract=JSON.parse(await readFile(path.join(path.dirname(renderer.template),'template-contract.json'),'utf8'))
 if(contract.profile!==profile) throw new Error('Template belongs to a different brand')
}
const completed=new Map()
for(const post of batch.posts) for(const slide of post.slides){
 if(!completed.has(slide.image)){
  const args = renderer.kind==='gtm-cli'
   ? [renderer.script,'--payload',slide.payload,'--output',slide.image]
   : renderer.kind==='html'
    ? [path.join(root,'scripts/render_social.mjs'),renderer.template,slide.payload,slide.image,renderer.browserModule,renderer.font]
    : null
  if(!args || args.some(value=>typeof value!=='string' || !value)) throw new Error('Invalid renderer configuration')
  await new Promise((resolve,reject)=>{
   const child=spawn(process.execPath,args,{cwd:renderer.cwd,stdio:'inherit',shell:false})
   child.on('error',reject);child.on('close',code=>code===0?resolve():reject(new Error(`Renderer failed: ${code}`)))
  })
  completed.set(slide.image,createHash('sha256').update(await readFile(slide.image)).digest('hex'))
 }
 const hash=completed.get(slide.image)
 if(slide.imageHash!==hash) delete slide.url // Never reuse an old approved URL for changed bytes.
 slide.imageHash=hash
}
await writeFile(batchPath,JSON.stringify(batch,null,2)+'\n')
console.log(`Rendered ${completed.size} unique images for ${profile}; approval must use the updated batch hash`)

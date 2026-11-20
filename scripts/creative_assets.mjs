import {readFile,realpath} from 'node:fs/promises'
import path from 'node:path'
import {createHash} from 'node:crypto'

/** A creative review can use several real captures, but never arbitrary URLs. */
export async function creativeAssets(payload, contract, payloadPath) {
  if (payload.reviewOnly !== true || payload.templateVersion !== 8) throw new Error('Creative exports are versioned review candidates')
  const bounds=contract.assetCounts?.[payload.layout]
  const images=payload.visual?.images ?? []
  if (!bounds || !Array.isArray(images) || images.length<bounds[0] || images.length>bounds[1]) throw new Error('Wrong asset count for creative composition')
  const root=await realpath(path.dirname(payloadPath)), result={}
  for (const [i,image] of images.entries()) {
    if (typeof image.file!=='string' || !image.alt?.trim() || !image.source?.trim() || !['product','figure','photography','brand'].includes(image.kind)) throw new Error('Every creative asset needs its real source, kind and alt text')
    const file=await realpath(path.resolve(root,image.file))
    if (!file.startsWith(root+path.sep)) throw new Error('Creative asset escaped the review directory')
    const mime={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp'}[path.extname(file).toLowerCase()]
    if (!mime) throw new Error('Creative asset must be a raster image')
    const bytes=await readFile(file)
    if(!/^[a-f0-9]{64}$/.test(image.sha256??'') || createHash('sha256').update(bytes).digest('hex')!==image.sha256) throw new Error('Creative asset hash does not match the reviewed bytes')
    result[`image${i}Url`]=`data:${mime};base64,${bytes.toString('base64')}`
  }
  for(let i=images.length;i<3;i++) result[`image${i}Url`]=''
  return result
}

import {readFileSync} from 'node:fs'

const patterns=JSON.parse(readFileSync(new URL('./social_copy_policy.json',import.meta.url),'utf8')).patterns.map(value=>new RegExp(value,'i'))

/** Inspect audience copy only. Source, licence, alt and capture metadata stay private. */
export function validateAudienceCopy(texts) {
 for(const text of texts)if(typeof text==='string' && patterns.some(pattern=>pattern.test(text)))throw new Error('Remove production notes or defensive disclaimers from audience copy')
}

export function visibleSocialCopy(payload) {
 const visual=payload.visual??{}
 return [payload.eyebrow,payload.headline,payload.support,payload.footerNote,visual.title,visual.note,visual.label,visual.statement,...(visual.items??[]).flatMap(item=>[item.title,item.body,item.label,item.value])]
}

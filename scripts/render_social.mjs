// Deterministic HTML renderer. Brand layouts and assets belong to the selected brand repository.
import { readFile, mkdir } from 'node:fs/promises'
import path from 'node:path'
import { pathToFileURL } from 'node:url'
const [templatePath, payloadPath, outputPath, browserModule, fontPath] = process.argv.slice(2)
if (!fontPath) throw new Error('Usage: render_social.mjs template payload output playwright-module font')
const payload = JSON.parse(await readFile(payloadPath, 'utf8'))
const escape = value => String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]))
const font = await readFile(fontPath)
const values = {...payload, fontUrl:`data:font/${fontPath.endsWith('woff2')?'woff2':'ttf'};base64,${font.toString('base64')}`}
const html = (await readFile(templatePath,'utf8')).replace(/\{\{(\w+)\}\}/g, (_,key) => {
  if (!(key in values)) throw new Error(`Missing template field: ${key}`)
  return escape(values[key])
})
const { chromium } = await import(pathToFileURL(path.resolve(browserModule)).href)
const browser = await chromium.launch({channel:'chrome',headless:true})
try {
  const page = await browser.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1})
  await page.setContent(html)
  await page.evaluate(() => document.fonts.ready)
  const errors = await page.evaluate(() => [...document.querySelectorAll('[data-fit]')].filter(el => {
    const r=el.getBoundingClientRect(); return r.bottom>1150 || r.right>1005 || el.scrollWidth>el.clientWidth
  }).map(el=>el.textContent))
  if(errors.length) throw new Error(`Text overflows safe area: ${JSON.stringify(errors)}`)
  await mkdir(path.dirname(outputPath),{recursive:true})
  await page.screenshot({path:outputPath,type:'png'})
} finally { await browser.close() }

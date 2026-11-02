// Deterministic HTML renderer. Brand layouts and assets belong to the selected brand repository.
import { readFile, mkdir } from 'node:fs/promises'
import path from 'node:path'
import { pathToFileURL } from 'node:url'
const [templatePath, payloadPath, outputPath, browserModule, fontPath] = process.argv.slice(2)
if (!fontPath) throw new Error('Usage: render_social.mjs template payload output playwright-module font')
const payload = JSON.parse(await readFile(payloadPath, 'utf8'))
const contract = JSON.parse(await readFile(path.join(path.dirname(templatePath), 'template-contract.json'), 'utf8'))
for (const field of contract.requiredFields) if (!(field in payload)) throw new Error(`Missing template input: ${field}`)
if (!contract.visualKinds.includes(payload.visual?.kind) || !payload.visual.title || !Array.isArray(payload.visual.items) || !payload.visual.items.length || payload.visual.items.length > 4 || payload.visual.items.some(item => !item.title)) throw new Error('Invalid structured visual payload')
if (contract.layouts && !contract.layouts.includes(payload.layout)) throw new Error('Invalid brand layout: ' + payload.layout)
const escape = value => String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]))
const font = await readFile(fontPath)
const values = {...payload, fontUrl:`data:font/${fontPath.endsWith('woff2')?'woff2':'ttf'};base64,${font.toString('base64')}`}
const assets = JSON.parse(await readFile(path.join(path.dirname(templatePath), 'assets.json'), 'utf8').catch(() => '{}'))
for (const [key, relative] of Object.entries(assets)) {
  const bytes = await readFile(path.resolve(path.dirname(templatePath), relative))
  const mime = {'.svg':'image/svg+xml','.png':'image/png','.ttf':'font/ttf','.woff2':'font/woff2'}[path.extname(relative)]
  if (!mime) throw new Error(`Unsupported template asset: ${relative}`)
  values[key] = `data:${mime};base64,${bytes.toString('base64')}`
}
const html = (await readFile(templatePath,'utf8')).replace(/\{\{(\w+)\}\}/g, (_,key) => {
  if (key === 'payloadJson') return JSON.stringify(payload).replace(/</g, '\\u003c').replace(/>/g, '\\u003e')
  if (!(key in values)) throw new Error(`Missing template field: ${key}`)
  return escape(values[key])
})
const { chromium } = await import(pathToFileURL(path.resolve(browserModule)).href)
const browser = await chromium.launch({channel:'chrome',headless:true})
try {
  const page = await browser.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1})
  const scriptErrors = []
  page.on('pageerror', error => scriptErrors.push(error.message))
  await page.setContent(html)
  await page.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map(image => image.decode())); await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))) })
  if (scriptErrors.length) throw new Error(`Template script failed: ${scriptErrors.join('; ')}`)
  const footer = await page.locator('footer').innerText()
  if (footer.split(contract.footerDomain).length !== 2) throw new Error('Render exactly one brand domain in the footer')
  const errors = await page.evaluate(() => [...document.querySelectorAll('[data-fit]')].filter(el => {
    const r=el.getBoundingClientRect(); return r.bottom>1150 || r.right>1016 || el.scrollWidth>el.clientWidth || el.scrollHeight>el.clientHeight
  }).map(el=>el.textContent))
  const contentErrors = await page.evaluate(minSize => [...document.querySelectorAll('main h1,main h2,main strong,main p,main .support')].filter(el => {
    const style=getComputedStyle(el); if(style.display==='none' || !el.getClientRects().length) return false;
    const r=el.getBoundingClientRect(); return Number.parseFloat(style.fontSize)<minSize || r.bottom>1150 || r.right>1016 || r.left<50 || el.scrollWidth>el.clientWidth+1
  }).map(el=>el.textContent), contract.minimumContentFontSize || 0)
  errors.push(...contentErrors)
  if(errors.length) throw new Error(`Text overflows safe area: ${JSON.stringify(errors)}`)
  await mkdir(path.dirname(outputPath),{recursive:true})
  await page.screenshot({path:outputPath,type:'png'})
} finally { await browser.close() }

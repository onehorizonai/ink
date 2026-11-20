// Deterministic HTML renderer. Brand layouts and assets belong to the selected brand repository.
import { readFile, mkdir, realpath } from 'node:fs/promises'
import path from 'node:path'
import { pathToFileURL } from 'node:url'
import { creativeAssets } from './creative_assets.mjs'
const [templatePath, payloadPath, outputPath, browserModule, fontPath] = process.argv.slice(2)
if (!fontPath) throw new Error('Usage: render_social.mjs template payload output playwright-module font')
const payload = JSON.parse(await readFile(payloadPath, 'utf8'))
const contract = JSON.parse(await readFile(path.join(path.dirname(templatePath), 'template-contract.json'), 'utf8'))
for (const field of contract.requiredFields) if (!(field in payload)) throw new Error(`Missing template input: ${field}`)
if (!contract.visualKinds.includes(payload.visual?.kind)) throw new Error('Invalid structured visual kind')
if (contract.layouts && !contract.layouts.includes(payload.layout)) throw new Error('Invalid brand layout: ' + payload.layout)
if(contract.reviewOnly && (!contract.headerFamilies?.[payload.headerFamily] || contract.layoutFamilies?.[payload.layout] !== payload.headerFamily)) throw new Error('Creative layout needs its declared header family')
const visual = payload.visual
const imageLayouts = contract.imageVisualLayouts ?? {}
const imageLayout = Object.hasOwn(imageLayouts, visual.kind) ? imageLayouts[visual.kind] : null
let productImageUrl = ''
let creativeImageUrls = {}
if (contract.reviewOnly) {
  creativeImageUrls = await creativeAssets(payload, contract, payloadPath)
} else if (imageLayout) {
  if (payload.layout !== imageLayout || typeof visual.file !== 'string' ||
      !/^[a-zA-Z0-9][a-zA-Z0-9_.-]*\.png$/.test(visual.file) ||
      typeof visual.alt !== 'string' || !visual.alt.trim()) {
    throw new Error('Product visuals require the image layout, a local PNG filename, and alt text')
  }
  const directory = await realpath(path.dirname(payloadPath))
  const imagePath = await realpath(path.join(directory, visual.file))
  if (path.dirname(imagePath) !== directory) throw new Error('Product image must be beside its payload')
  const bytes = await readFile(imagePath)
  productImageUrl = `data:image/png;base64,${bytes.toString('base64')}`
} else if (Object.values(imageLayouts).includes(payload.layout) ||
    !visual.title || !Array.isArray(visual.items) || !visual.items.length ||
    visual.items.length > 4 || visual.items.some(item => !item?.title)) {
  throw new Error('Invalid structured visual payload')
}
const escape = value => String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]))
const font = await readFile(fontPath)
const values = {...payload, ...creativeImageUrls, productImageUrl, fontUrl:`data:font/${fontPath.endsWith('woff2')?'woff2':'ttf'};base64,${font.toString('base64')}`}
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
  const safeBottom = contract.reviewOnly ? (contract.safeBottom || 1150) : 1150
  const errors = await page.evaluate(({bottom,tolerance}) => [...document.querySelectorAll('[data-fit]')].filter(el => {
    const r=el.getBoundingClientRect(); return r.bottom>bottom || r.right>1016 || el.scrollWidth>el.clientWidth+tolerance || el.scrollHeight>el.clientHeight+tolerance
  }).map(el=>el.textContent),{bottom:safeBottom,tolerance:contract.reviewOnly?1:0})
  const contentErrors = await page.evaluate(({minSize,bottom,checkHeight}) => [...document.querySelectorAll('main h1,main h2,main strong,main p,main .support')].filter(el => {
    const style=getComputedStyle(el); if(style.display==='none' || !el.getClientRects().length) return false;
    const r=el.getBoundingClientRect(); return Number.parseFloat(style.fontSize)<minSize || r.bottom>bottom || r.right>1016 || r.left<50 || el.scrollWidth>el.clientWidth+1 || (checkHeight && el.scrollHeight>el.clientHeight+1)
  }).map(el=>el.textContent), {minSize:contract.minimumContentFontSize || 0,bottom:safeBottom,checkHeight:Boolean(contract.reviewOnly)})
  const headerErrors = await page.evaluate(boxes => {
    const selectors={eyebrow:'.intro .eyebrow',headline:'.intro h1',support:'.intro .support'};
    return Object.entries(boxes||{}).filter(([key,expected])=>{
      const box=document.querySelector(selectors[key]).getBoundingClientRect();
      return [box.x,box.y,box.width,box.height].some((value,i)=>Math.abs(value-expected[i])>.5);
    }).map(([key])=>'Carousel header anchor changed: '+key);
  },contract.headerFamilies ? contract.headerFamilies[payload.headerFamily] : contract.headerBoxes)
  if(contract.reviewOnly && payload.headerFamily!=='photo') {
    errors.push(...await page.evaluate(() => {
      const intro=document.querySelector('.intro').getBoundingClientRect()
      return [...document.querySelectorAll('.stage [data-fit],.stage .asset')].filter(el=>{
        const r=el.getBoundingClientRect()
        return r.left<intro.right-1 && r.right>intro.left+1 && r.top<intro.bottom-1 && r.bottom>intro.top+1
      }).map(el=>'Visual intersects the heading section: '+(el.textContent||el.getAttribute('alt')))
    }))
  }
  errors.push(...headerErrors)
  errors.push(...contentErrors)
  if(errors.length) { await mkdir(path.dirname(outputPath),{recursive:true}); await page.screenshot({path:outputPath.replace(/\.png$/,'.failed.png')}); }
  if(errors.length) throw new Error(`Text overflows safe area: ${JSON.stringify(errors)}`)
  await mkdir(path.dirname(outputPath),{recursive:true})
  await page.screenshot({path:outputPath,type:'png'})
} finally { await browser.close() }

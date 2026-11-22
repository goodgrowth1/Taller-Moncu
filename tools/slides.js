// Uso: node tools/slides.js <archivo.html> <prefijo_salida> [ancho] [alto]
// Renderiza cada elemento .slide del HTML como PNG: <prefijo>_01.png, _02.png...
// Carrusel 1080x1350 (por defecto), story 1080x1920.
const {chromium}=require('playwright');const path=require('path');
(async()=>{
  const [src,prefix,w='1080',h='1350']=process.argv.slice(2);
  const W=+w,H=+h;
  const b=await chromium.launch({args:['--allow-file-access-from-files']});
  const p=await b.newPage({viewport:{width:W,height:H}});
  await p.goto('file://'+path.resolve(src));
  await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
  const n=await p.locator('.slide').count();
  for(let i=0;i<n;i++){
    const out=`${prefix}_${String(i+1).padStart(2,'0')}.png`;
    await p.locator('.slide').nth(i).screenshot({path:out});
    console.log(out);
  }
  await b.close();
})();

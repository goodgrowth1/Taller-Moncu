const { chromium } = require('playwright');
(async()=>{
  const mode=process.argv[2]||'full'; const fps=30;
  const b=await chromium.launch({args:['--allow-file-access-from-files']});
  const p=await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('file://'+__dirname+'/index.html'); await p.waitForTimeout(800);
  const el=await p.$('#s');
  if(mode==='preview'){
    for(const t of (process.argv[3]||'1').split(',').map(Number)){await p.evaluate(t=>render(t),t);await el.screenshot({path:`prev_${t}.png`});}
  } else {
    const dur=await p.evaluate(()=>window.T.end); require('fs').mkdirSync('frames',{recursive:true});
    for(let i=0;i<Math.round(fps*dur);i++){await p.evaluate(t=>render(t),i/fps);await el.screenshot({path:`frames/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});}
  }
  await b.close();
})();

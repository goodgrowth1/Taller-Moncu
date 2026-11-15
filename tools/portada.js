// Uso: node tools/portada.js work/<slug>/portada.html salida.png
// Genera la portada 1080x1920 y salida_grids.png (9:16, 3:4 y 1:1) para comprobar que nada se corta.
const {chromium}=require('playwright');const path=require('path');const {execSync}=require('child_process');
(async()=>{const [src,out]=process.argv.slice(2);const b=await chromium.launch({args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+path.resolve(src));await p.waitForTimeout(900);
await p.screenshot({path:out});await b.close();
execSync(`python3 -c "
from PIL import Image
im=Image.open('${out}').convert('RGB');s=Image.new('RGB',(1255,720),(255,255,255))
s.paste(im.resize((405,720)),(0,0));s.paste(im.crop((0,240,1080,1680)).resize((405,540)),(425,90));s.paste(im.crop((0,420,1080,1500)).resize((405,405)),(850,157))
s.save('${out.replace('.png','_grids.png')}')"`);})();

# Uso: python3 tools/sync.py voz.mp3  -> duración, tramos de voz (inicio-fin) y pausas.
# Mapea cada tramo a una frase del guion para fijar window.T en index.html.
import subprocess,re,sys
f=sys.argv[1]
out=subprocess.run(['ffmpeg','-i',f,'-af','silencedetect=noise=-32dB:d=0.12','-f','null','-'],capture_output=True,text=True).stderr
dur=float(re.search(r'Duration: (\d+):(\d+):([\d.]+)',out).groups()[2])+60*float(re.search(r'Duration: (\d+):(\d+)',out).groups()[1])
st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',out)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',out)]
sp=[];cur=0.0
for s,e in zip(st,en+[dur]*(len(st)-len(en))):
    if s-cur>0.05: sp.append((cur,s))
    cur=e
if dur-cur>0.05: sp.append((cur,dur))
print(f'DURACION {dur:.2f}s')
for i,(a,b) in enumerate(sp): print(f'tramo {i:2d}: {a:6.2f} -> {b:6.2f}  ({b-a:.2f}s)')

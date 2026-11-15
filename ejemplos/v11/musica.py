# Música del vídeo de la Behobia: con energía pero baja. Re mayor, 122 bpm.
# Arranca con pulso, se abre en "enhorabuena", se recoge en los consejos y sube con la moneda.
import numpy as np, wave, json
T=json.load(open('tiempos.json'))
SR=44100; DUR=T['end']; N=int(SR*DUR); L=np.zeros(N); R=np.zeros(N); rng=np.random.default_rng(5)
def add(t0,s,g=1,pan=0):
    a=int(t0*SR)
    if a<0 or a>=N: return
    e=min(N,a+len(s)); L[a:e]+=s[:e-a]*g*(1-max(0,pan)); R[a:e]+=s[:e-a]*g*(1+min(0,pan))
tt=lambda d:np.arange(int(d*SR))/SR
lp=lambda x,k:np.convolve(x,np.ones(k)/k,'same')
hp=lambda x,k=3:x-lp(x,k)
def kick(): t=tt(.28); f=50+130*np.exp(-t*32); return np.tanh(2*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*10))
def clap(): t=tt(.15); return hp(rng.standard_normal(len(t)),2)*np.exp(-t*30)
def hat(): t=tt(.04); return hp(rng.standard_normal(len(t)),2)*np.exp(-t*110)
def pluck(f,d): t=tt(d); s=np.sign(np.sin(2*np.pi*f*t))*.3+np.sin(2*np.pi*f*t); return lp(s,4)*np.exp(-t*7)*np.minimum(1,t/.004)
def pad(f,d): t=tt(d); s=sum(np.sin(2*np.pi*f*k*t+rng.random()*6) for k in (1,1.005,.995))/3; return lp(s,6)*np.minimum(1,t/.3)*np.minimum(1,(d-t)/.3)
def bass(f,d): t=tt(d); return np.tanh(1.5*np.sin(2*np.pi*f*t))*np.minimum(1,t/.01)*np.minimum(1,(d-t)/.04)
def riser(d): t=tt(d); return hp(rng.standard_normal(len(t)),2)*(t/d)**2*.6
def boom(): t=tt(1.2); return np.sin(2*np.pi*(45+60*np.exp(-t*8))*t)*np.exp(-t*3)
m=lambda n:440*2**((n-69)/12)
b=60/128
prog=[(43,[59,62,67]),(38,[57,62,66]),(40,[59,64,67]),(36,[60,64,67])]  # D A Bm G
t=0.0;i=0
while t<DUR-.3:
    bn,ch=prog[(i//4)%4]
    full=T['enh']<=t<T['t1'] or t>=T['coin']
    tips=T['t1']<=t<T['coin']
    add(t,kick(),.6 if not tips else .45)
    if full and i%2==1: add(t,clap(),.16,.1)
    if not tips or i%2==0:
        for s in range(2): add(t+s*b/2,hat(),.05 if s else .03,.3)
    add(t,bass(m(bn),b*.45),.22); add(t+b/2,bass(m(bn),b*.4),.15)
    if i%4==0:
        for x in ch: add(t,pad(m(x),4*b),.04,(-.2 if x%2 else .2))
    if full:
        for s in range(2): add(t+s*b/2,pluck(m(ch[(i*2+s)%3]+12),b*.6),.05,(-.3 if s else .3))
    t+=b;i+=1
add(T['coin']-1.6,riser(1.6),.25); add(T['coin'],boom(),.35)
def tick(): t=tt(.2); return np.sin(2*np.pi*1568*t)*np.exp(-t*16)
for k in ('t1','t2','t3'): add(T[k],tick(),.15)
env=np.ones(N); fo=int(1.2*SR); env[-fo:]=np.linspace(1,0,fo); L*=env; R*=env
L=np.tanh(L*1.1); R=np.tanh(R*1.1); p=max(abs(L).max(),abs(R).max()); L/=p; R/=p
d=(np.stack([L,R],1)*.85*32767).astype('<i2'); w=wave.open('musica.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(d.tobytes()); w.close()

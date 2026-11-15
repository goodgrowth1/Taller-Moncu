# Música del vídeo de las cuestas: sobria, tono menor, 96 bpm. Se aprieta en la cuesta,
# se abre en "con cabeza" y se suelta al llegar arriba. Sintetizada, sin derechos.
import numpy as np, wave, json
T=json.load(open('tiempos.json'))
SR=44100; DUR=T['end']; N=int(SR*DUR); L=np.zeros(N); R=np.zeros(N); rng=np.random.default_rng(9)
def add(t0,s,g=1,pan=0):
    a=int(t0*SR)
    if a<0 or a>=N: return
    e=min(N,a+len(s)); L[a:e]+=s[:e-a]*g*(1-max(0,pan)); R[a:e]+=s[:e-a]*g*(1+min(0,pan))
tt=lambda d:np.arange(int(d*SR))/SR
lp=lambda x,k:np.convolve(x,np.ones(k)/k,'same')
hp=lambda x,k=3:x-lp(x,k)
def kick(): t=tt(.3); f=48+120*np.exp(-t*30); return np.tanh(1.8*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*9))
def rim(): t=tt(.08); return hp(rng.standard_normal(len(t)),2)*np.exp(-t*60)*.6+np.sin(2*np.pi*900*t)*np.exp(-t*80)*.4
def hat(): t=tt(.04); return hp(rng.standard_normal(len(t)),2)*np.exp(-t*110)
def keys(f,d): t=tt(d); s=np.sin(2*np.pi*f*t)+.25*np.sin(2*np.pi*2*f*t)*np.exp(-t*4); return s*np.exp(-t*1.2)*np.minimum(1,t/.02)
def pad(f,d): t=tt(d); s=sum(np.sin(2*np.pi*f*k*t+rng.random()*6) for k in (1,1.004,.996))/3; return lp(s,6)*np.minimum(1,t/.4)*np.minimum(1,(d-t)/.4)
def bass(f,d): t=tt(d); return np.sin(2*np.pi*f*t)*np.minimum(1,t/.01)*np.minimum(1,(d-t)/.05)
m=lambda n:440*2**((n-69)/12)
b=60/100
prog=[(38,[50,53,57]),(46,[50,53,58]),(41,[53,57,60]),(45,[52,57,61])]  # Am F C G
t=0.0;i=0
while t<DUR-.4:
    bn,ch=prog[(i//4)%4]
    climb=T['paseo']<=t<T['cabeza']; open_=t>=T['cabeza']; top=t>=T['arriba']
    add(t,kick(),.6 if not climb else .45)
    if i%2==1: add(t,rim(),.18,-.15)
    if open_ and not top:
        for s in range(2): add(t+s*b/2,hat(),.04 if s else .025,.3)
    add(t,bass(m(bn),b*.9),.22)
    if i%4==0:
        for x in ch: add(t,pad(m(x),4*b),.045,(-.2 if x%2 else .2))
    if open_ and i%2==0: add(t+b/2,keys(m(ch[(i//2)%3]+12),b*1.5),.06,(-.25 if i%4 else .25))
    t+=b;i+=1
def tick(): t=tt(.2); return np.sin(2*np.pi*1318*t)*np.exp(-t*16)
for k in ('t1','t2','t3','guarda'): add(T[k],tick(),.15)
env=np.ones(N); fo=int(1.2*SR); env[-fo:]=np.linspace(1,0,fo); L*=env; R*=env
L=np.tanh(L*1.1); R=np.tanh(R*1.1); p=max(abs(L).max(),abs(R).max()); L/=p; R/=p
d=(np.stack([L,R],1)*.85*32767).astype('<i2'); w=wave.open('musica.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(d.tobytes()); w.close()

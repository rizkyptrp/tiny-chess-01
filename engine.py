import json,os,urllib.request
U=os.environ["MAKEFUN_ENV_URL"]
V=(0,100,320,330,500,900,0)
N=(-33,-31,-18,-14,14,18,31,33)
B=(-17,-15,15,17)
R=(-16,-1,1,16)
Q=B+R
T=[None]+[[ord(c)-81 for c in t]for t in("QQQQV[[=VLGQQQQeVV[j[[eoppppQQQQ","15==5CQU=UY]=Q]a=U]a=QY]5CQQ15==","aiYQaaQQIAAAA9919111911191119111")];T[3:3]=[T[2]]*3
M=100000
D=80000
n=0
TT={}
class O(Exception):pass
def P(p,d):
 with urllib.request.urlopen(U+p,json.dumps(d).encode())as x:return json.load(x)
def F(f):
 b=[0]*128;p=f.split();i=112
 for c in p[0]:
  if c=="/":i-=24
  elif c.isdigit():i+=int(c)
  else:
   v="pnbrqk".index(c.lower())+1;b[i]=v*(c<"a"or-1);i+=1
 c=sum(1<<i for i,k in enumerate("KQkq")if k in p[2])
 return[b,1-2*(p[1]=="b"),c,ord(p[3][0])+int(p[3][1])*16-113 if p[3]!="-"else-1,b.index(6),b.index(-6)]
def G(b,s,c):
 for w,v in((N,2*c),(Q,6*c),((-15*c,-17*c),c)):
  for d in w:
   x=s+d
   if x&136<1 and b[x]==v:return 1
 for d in Q:
  x=s+d
  while x&136<1:
   p=b[x]
   if p:
    if p==5*c or p==(3 if d in B else 4)*c:return 1
    break
   x+=d
 return 0
def Y(s,C=0):
 b,t,c,e=s[0],s[1],s[2],s[3];m=[];d=16*t
 for x in range(128):
  if x&136:continue
  p=b[x]
  if p*t<=0:continue
  a=abs(p)
  if a==1:
   y=x+d
   if y&136<1 and not b[y]:
    if(y>>4)==7*(t>0):m.append((x,y,5))
    elif not C:
     m.append((x,y,0))
     z=x+2*d
     if(x>>4)==1+5*(t<0)and not b[z]:m.append((x,z,0))
   for o in(d-1,d+1):
    y=x+o
    if y&136:continue
    q=b[y]
    if q*t<0:
     if(y>>4)==7*(t>0):m.append((x,y,5))
     else:m.append((x,y,0))
    elif y==e:m.append((x,y,0))
  elif a==2 or a==6:
   for o in N if a==2 else Q:
    y=x+o
    if y&136:continue
    q=b[y]
    if(not q or q*t<0)and(not C or q):m.append((x,y,0))
  else:
   for o in B if a==3 else R if a==4 else Q:
    y=x+o
    while y&136<1:
     q=b[y]
     if not q:
      if not C:m.append((x,y,0))
     else:
      if q*t<0:m.append((x,y,0))
      break
     y+=o
 if not C:
  k=s[4+(t<0)];h=4+112*(t<0)
  if k==h:
   for o in(1,-1):
    if c&1<<(o<0)+2*(t<0)and not b[h+o]and not b[h+2*o]and(o>0 or not b[h+3*o])and not(G(b,h,-t)or G(b,h+o,-t)or G(b,h+2*o,-t)):m.append((h,h+2*o,0))
 r=[]
 for z in m:
  s2=A(s,z)
  if not G(s2[0],s2[4+(t<0)],-t):r.append((z,s2))
 return r
def A(s,m):
 b=s[0][:];t=s[1];c=s[2];x,y,r=m;p=b[x];q=b[y];b[y]=p;b[x]=0;w=s[4];v=s[5];a=abs(p);e=-1
 if a==1:
  if abs(y-x)==32:e=x+16*t
  if not q and(x&7)!=(y&7):b[y-16*t]=0
  if r:b[y]=r*t
 elif a==6:
  if t>0:w=y
  else:v=y
  if abs(y-x)==2:
   o=3 if y>x else-4;e=1 if y>x else-1;b[x+e]=b[x+o];b[x+o]=0
  c&=~(3 if t>0 else 12)
 for z,f in((0,2),(7,1),(112,8),(119,4)):
  if x==z or y==z:c&=~f
 return[b,-t,c,e,w,v]
def X(s):
 b,t=s[0],s[1];w=0
 for x in range(128):
  if x&136:continue
  p=b[x]
  if not p:continue
  a=abs(p);v=V[a];i=min(x&7,7-(x&7))+((7-(x>>4)if p<0 else x>>4)<<2)
  w+=v+T[a][i]if p>0 else-v-T[a][i]
  if a==1 and i>>2>1 and not any(b[y]==-p for o in(-1,0,1)for y in range(x+o+16*p,64+64*p,16*p)):w+=(i>>2)**2*3*p
 return w*t
def J(st,ms,tm):
 b=st[0]
 def k(p):
  m=p[0]
  if m==tm:return 1<<20
  v=b[m[1]]
  if v or(abs(b[m[0]])==1 and(m[0]&7)!=(m[1]&7)):return 10000+(V[abs(v)]or 100)*10-V[abs(b[m[0]])]
  return 0
 ms.sort(key=k,reverse=True)
def q(st,a,be,pl):
 global n;n+=1
 if n>D:raise O
 b=st[0];t=st[1]
 if G(b,st[4+(t<0)],-t):
  ms=Y(st)
  if not ms:return -M+pl
 else:
  w=X(st)
  if w>=be:return be
  if w>a:a=w
  ms=Y(st,1)
 J(st,ms,None)
 for m,st2 in ms:
  w=-q(st2,-be,-a,pl+1);a=max(a,w)
  if a>=be:return be
 return a
def s(st,d,a,be,pl):
 global n;n+=1
 if n>D:raise O
 if d<=0:return q(st,a,be,pl)
 k=(bytes(x+6 for x in st[0]),st[1],st[2])
 e=TT.get(k)
 if e and e[0]>=d and(e[2]==0 or e[2]==1 and e[1]>=be or e[2]==2 and e[1]<=a):return e[1]
 ms=Y(st)
 if not ms:return -M+pl if G(st[0],st[4+(st[1]<0)],-st[1])else 0
 J(st,ms,e[3]if e else None)
 bs=-M;bm=None;fl=2
 for m,st2 in ms:
  w=-s(st2,d-1,-be,-a,pl+1)
  if w>bs:bs=w;bm=m
  if bs>a:a=bs;fl=0
  if a>=be:
   fl=1;break
 if abs(bs)<M-1000:TT[k]=(d,bs,fl,bm)
 return bs
def r(fen,legal):
 global n
 st=F(fen);ms=[]
 for u in legal:
  m=(ord(u[0])+int(u[1])*16-113,ord(u[2])+int(u[3])*16-113,"nbrq".index(u[4])+2 if u[4:]else 0);ms.append([0,m,A(st,m),u])
 if len(ms)==1:return ms[0][3]
 n=0;TT.clear();bm=ms[0][3]
 for d in range(63):
  try:
   a=-M;cb=-M;cu=bm
   for e in ms:
    w=-s(e[2],d,-M,-a,1);e[0]=w
    if w>cb:cb=w;cu=e[3]
    if cb>a:a=cb
  except O:break
  bm=cu
  ms.sort(key=lambda e:-e[0])
 return bm
while(g:=P("/game",{}))["status"]!="done":
 while g["status"]=="your_move":
  L=g["legal_moves"]
  try:mv=r(g["fen"],L)
  except Exception:mv=L[0]
  g=P("/move",{"game":g["game"],"move":mv})

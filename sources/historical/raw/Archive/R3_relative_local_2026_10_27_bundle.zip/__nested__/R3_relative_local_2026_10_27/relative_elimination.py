"""Tietze pivots restricted to affected links, all other physical links are frozen group coefficients."""
import numpy as np,json,collections
from pathlib import Path
out=Path(__file__).resolve().parent;z=np.load('/mnt/data/R3_nonabelian_relative_2026_10_27/prism_incidence.npz');d1=z['d1'];d2=z['d2'];Q={13,18,22,25,26,29,32,37}
ends={e:(int(np.flatnonzero(d1[:,e]==-1)[0]),int(np.flatnonzero(d1[:,e]==1)[0])) for e in range(d1.shape[1])}
def red(w):
 s=[]
 for t in w:
  if s and s[-1]==-t:s.pop()
  else:s.append(t)
 return tuple(s)
def inv(w):return tuple(-x for x in reversed(w))
def faceword(f):
 es=list(map(int,np.flatnonzero(d2[:,f])));pos=min(x for e in es for x in ends[e]);w=[];used=set()
 for _ in es:
  opts=[]
  for e in es:
   if e in used:continue
   u,v=ends[e]
   if pos==u and d2[e,f]==1:opts.append((e,1,v))
   if pos==v and d2[e,f]==-1:opts.append((e,-1,u))
  assert len(opts)==1
  e,s,pos=opts[0];w.append(s*(e+1));used.add(e)
 return red(w)
W={f:faceword(f) for f in range(d2.shape[1])}
L=set(np.flatnonzero(np.any(d2[:,list(Q)]!=0,axis=1)))

for collar in ([],[45],[23]):
 active=set(e+1 for e in L|set(collar));rel={f:W[f] for f in range(48) if f not in Q and any(abs(t) in active for t in W[f])}
 ext_only=[f for f in range(48) if f not in Q and f not in rel];ops=[]
 for step in range(100):
  freq=collections.Counter(abs(t) for w in rel.values() for t in w if abs(t) in active)
  options=[]
  for f,w in rel.items():
   for j,t in enumerate(w):
    x=abs(t)
    if x not in active or sum(abs(k)==x for k in w)!=1:continue
    cost=(len(w)-1)*max(0,freq[x]-1)
    options.append((cost,len(w),-freq[x],f,j))
  if not options:break
  *_,f,j=min(options);w=rel.pop(f);t=w[j];tail=w[j+1:]+w[:j];sub=inv(tail) if t>0 else tail;x=abs(t)
  replacements={x:sub,-x:inv(sub)}
  for ff,ww in list(rel.items()):
   new=[]
   for v in ww:new.extend(replacements[v] if abs(v)==x else [v])
   rel[ff]=red(new)
  active.remove(x);ops.append({'face':f,'edge':x-1,'replacement_length':len(sub),'max_residual_word_length':max([len(w) for w in rel.values()]+[0])})
  if max([len(w) for w in rel.values()]+[0])>100000:break
 print('residual active', {f:sorted(set(abs(t)-1 for t in w)&{x-1 for x in active}) for f,w in rel.items() if set(abs(t) for t in w)&active}); print('collar',collar,'local',len(L)+len(collar),'retained eliminated',len(ops),'local remain',len(active),'residual nonempty',sum(bool(w) for w in rel.values()),'max length',max([len(w) for w in rel.values()]+[0]),'max replacement',max([a['replacement_length'] for a in ops]+[0]))
 result={'collar':collar,'local_count':len(L)+len(collar),'retained_eliminated_pivots':len(ops),'remaining_local_edges':[t-1 for t in sorted(active)],'residual_retained_relator_count':sum(bool(w) for w in rel.values()),'max_residual_word_length':max([len(w) for w in rel.values()]+[0]),'operations':ops,'external_only_retained_faces':ext_only}
 (out/('relative_elimination_'+ ('bare' if not collar else str(collar[0]))+'.json')).write_text(json.dumps(result,indent=2,default=lambda x: int(x) if isinstance(x,np.integer) else x))

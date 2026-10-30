import numpy as np,json,collections
from pathlib import Path
P=Path('/mnt/data/R3_nonabelian_relative_2026_10_27'); z=np.load(P/'prism_incidence.npz');D1=z['d1'];D2=z['d2'];r=json.loads((P/'presentation.json').read_text());Q=list(map(int,r['Q']));L=set(map(int,np.flatnonzero(np.any(D2[:,Q]!=0,axis=1))));E=sorted(set(range(D1.shape[1]))-L)
ops=r['retained_tietze']['operations'];free=set(r['retained_tietze']['remaining_generators']);chords=r['free_edges'];T=set(r['tree_edges']);assert len(free)==2

def inv(w):return [-v for v in reversed(w)]
def red(w):
 o=[]
 for a in w:
  if o and o[-1]==-a:o.pop()
  else:o.append(a)
 return o
mapped={x:[x] for x in free}
for op in reversed(ops):
 w=[]
 for t in op['replacement']:
  w+=mapped[abs(t)] if t>0 else inv(mapped[abs(t)])
 mapped[op['generator']]=red(w)
assert len(mapped)==len(chords)
ends={e:(int(np.flatnonzero(D1[:,e]<0)[0]),int(np.flatnonzero(D1[:,e]>0)[0])) for e in range(D1.shape[1])}
edgeword={e:([] if e in T else mapped[chords.index(e)+1]) for e in range(D1.shape[1])}
a,b=sorted(free)
# Detect an exterior-only gauge invariant closed loop with nonzero a exponent.
adj=[[] for _ in range(D1.shape[0])]
for e in E:
 u,v=ends[e];adj[u].append((v,e,1));adj[v].append((u,e,-1))
paths={};par={};components=[]
for root in range(D1.shape[0]):
 if root in paths:continue
 q=collections.deque([root]);paths[root]=[];par[root]=None;component=[]
 while q:
  v=q.popleft();component.append(v)
  for w,e,s in sorted(adj[v],key=lambda x:x[1]):
   if w in paths:continue
   paths[w]=paths[v]+[(e,s)];par[w]=e;q.append(w)
 components.append(component)
usedtree={e for e in par.values() if e is not None}
cycles=[]
for e in E:
 if e in usedtree:continue
 u,v=ends[e]
 # tree rooted per component; choose root word: path root->u, edge u->v, inverse root->v
 walk=paths[u]+[(e,1)]+[(q,-s) for q,s in reversed(paths[v])]
 wrd=red([t for ed,s in walk for t in (edgeword[ed] if s>0 else inv(edgeword[ed]))]);ea=sum(t==a for t in wrd)-sum(t==-a for t in wrd)
 eb=sum(t==b for t in wrd)-sum(t==-b for t in wrd)
 cycles.append(dict(edge=e,walk=walk,word=wrd,a_exponent=ea,b_exponent=eb))
print('Q',Q,'local edges',len(L),'exterior',len(E),'components',list(map(len,components)),'exterior cycles',len(cycles),'active gens',a,b)
print('a nonzero',[(x['edge'],x['a_exponent'],x['b_exponent'],len(x['walk']),x['word']) for x in cycles if x['a_exponent']][:15]);print('b nonzero',[(x['edge'],x['a_exponent'],x['b_exponent']) for x in cycles if x['b_exponent']][:15])
res=dict(Q=Q,local_edges=sorted(L),exterior_edges=E,exterior_components=list(map(len,components)),exterior_cycle_rank=len(cycles),a_generator=a,b_generator=b,cycles=cycles,group_word_map={str(k):v for k,v in mapped.items()})
(Path(__file__).parent/'exterior_cycle_certificate.json').write_text(json.dumps(res,indent=2))

"""Exact free-group symbolic flat gluing after enlarging repair collar by edge 45."""
import numpy as np,json,collections
from pathlib import Path
P=Path('/mnt/data/R3_nonabelian_relative_2026_10_27');root=Path(__file__).resolve().parent
r=json.loads((root/'exterior_cycle_certificate.json').read_text());z=np.load(P/'prism_incidence.npz');D1=z['d1'];D2=z['d2'];q=set(r['Q']);L=set(r['local_edges']);C=L|{45};E=sorted(set(range(D1.shape[1]))-C)
T=set(json.loads((P/'presentation.json').read_text())['tree_edges']); chords=json.loads((P/'presentation.json').read_text())['free_edges']; words={int(x):list(w) for x,w in r['group_word_map'].items()}
a=r['a_generator'];b=r['b_generator'];assert a==19 and b==34

def inv(w):return [-x for x in reversed(w)]
def red(w):
 o=[]
 for t in w:
  if o and o[-1]==-t:o.pop()
  else:o.append(t)
 return o

def product(words):return red([v for w in words for v in w])
end={e:(int(np.flatnonzero(D1[:,e]<0)[0]),int(np.flatnonzero(D1[:,e]>0)[0])) for e in range(D1.shape[1])}
old={e:([] if e in T else words[chords.index(e)+1]) for e in range(D1.shape[1])}
new={e:[v for v in old[e] if abs(v)!=a] for e in range(D1.shape[1])}
assert all(set(map(abs,ww)).issubset({a,b}) for ww in old.values())
adj={v:[] for v in range(D1.shape[0])}
for e in E:
 u,v=end[e];adj[u].append((v,e,1));adj[v].append((u,e,-1))
g={}; oldpath={};newpath={};forest=[];comp=[]
for v in range(D1.shape[0]):
 if v in g:continue
 g[v]=[];oldpath[v]=[];newpath[v]=[];comp.append([]);queue=collections.deque([v])
 while queue:
  u=queue.popleft();comp[-1].append(u)
  for vv,e,s in sorted(adj[u],key=lambda x:x[1]):
   if vv in g:continue
   wold=old[e] if s==1 else inv(old[e]);wnew=new[e] if s==1 else inv(new[e]);
   oldpath[vv]=product([oldpath[u],wold]);newpath[vv]=product([newpath[u],wnew]);g[vv]=product([inv(oldpath[vv]),newpath[vv]]);forest.append(e);queue.append(vv)
failed=[]
for e in E:
 u,v=end[e];image=product([g[u],new[e],inv(g[v])]);
 if image!=old[e]:failed.append((e,image,old[e]))
print('exterior components',list(map(len,comp)),'checked edges',len(E),'failure',len(failed),'max gauge len',max(map(len,g.values())))
assert not failed
# complete full-flat new gauge transform that *agrees exactly* with retained-flat old on E.
full={e:product([g[end[e][0]],new[e],inv(g[end[e][1]])]) for e in range(D1.shape[1])}
for f in range(D2.shape[1]):
 cyc=list(map(int,np.flatnonzero(D2[:,f])));starts={e:end[e][0] for e in cyc};ends={e:end[e][1] for e in cyc};v=min(set(starts.values())|set(ends.values()));walk=[];used=set()
 for _ in cyc:
  oo=[]
  for e in cyc:
   if e in used:continue
   if starts[e]==v and D2[e,f]==1:oo.append((e,1,ends[e]))
   if ends[e]==v and D2[e,f]==-1:oo.append((e,-1,starts[e]))
  assert len(oo)==1,(f,v,oo)
  e,s,v=oo[0];walk.append(full[e] if s==1 else inv(full[e]));used.add(e)
 assert product(walk)==[],(f,product(walk))
print('all 48 face holonomies trivial after local gluing. modified edges',len(C),'actual changed',sum(old[e]!=full[e] for e in C))
certificate={'Q':sorted(q),'original_local_edges':sorted(L),'collar_edge':45,'new_local_edges':sorted(C),'frozen_exterior_edges':E,'components':list(map(len,comp)),'exterior_edge_constraints_exact':True,'full_flat_face_relations_exact':True,'max_symbolic_gauge_word_length':max(map(len,g.values())),'vertex_gauge_words':{str(v):w for v,w in g.items()},'modified_local_edges':[e for e in sorted(C) if old[e]!=full[e]],'input_flat_generators':['a=generator 19','b=generator 34'],'scope':'symbolic flat-connection repair only; not a Gibbs-density or conditional off-flat action comparison'}
(root/'flat_gluing_certificate.json').write_text(json.dumps(certificate,indent=2))

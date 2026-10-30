import sys,json,csv,numpy as np
from collections import deque
from pathlib import Path
SRC=Path(__file__).resolve().parent;sys.path.insert(0,str(SRC))
from nested_audit import build,complex_3,cell_boundaries,rank_mod_columns,sparse_boundary_projection_rank,bianchi_peel
OUT=Path(__file__).resolve().parent
src,_=build(5,0)
anchor=[145,146,147,149,154,155]
edge_keys=[tuple(sorted([src.labels[a],src.labels[b]])) for e in anchor for a,b in [src.edges[e]]]
# Grow a connected temporal star by sharing spatial endpoints.
adj={i:set() for i in range(len(src.edges))}; rev={}
for e,(a,b) in enumerate(src.edges):
 for v in (a,b):rev.setdefault(v,set()).add(e)
for ns in rev.values():
 for e in ns:adj[e].update(ns-{e})
chosen=set(anchor);order=list(anchor);queue=deque(anchor)
while queue and len(order)<30:
 e=queue.popleft()
 for v in sorted(adj[e]):
  if v not in chosen:
   chosen.add(v);order.append(v);queue.append(v)
  if len(order)>=30:break
assert len(order)>=30
edge_keys=[tuple(sorted((src.labels[src.edges[e][0]],src.labels[src.edges[e][1]]))) for e in order]
reports=[]
for rad in [5.,6.5,8.,10.]:
 g,_=build(rad,0);mp={tuple(sorted((g.labels[a],g.labels[b]))):i for i,(a,b) in enumerate(g.edges)};cols,meta=complex_3(g);cells=cell_boundaries(g);nF=len(g.faces);nE=len(g.edges)
 for size in [6,8,12,20,30]:
  Q={3*nF+mp[k] for k in edge_keys[:size]}
  L={x for f in Q for x in cols[f]};R=[col for i,col in enumerate(cols) if i not in Q]
  gl=len(Q)-sparse_boundary_projection_rank(cells,Q); minrad=None;arr=[]
  for r in range(4):
   lr=rank_mod_columns(R,L);lf=rank_mod_columns(cols,L);delta=gl-lf+lr
   if delta==0 and minrad is None:minrad=r
   arr.append((len(L),delta))
   if r<3:
    old=set(L)
    for col in cols:
     if not old.isdisjoint(col):L.update(col)
  peel,rest,_=bianchi_peel(cols,cells,Q)
  pts=g.xy[list({v for e in [mp[k] for k in edge_keys[:size]] for v in g.edges[e]})];diam=float(np.max(np.linalg.norm(pts[:,None,:]-pts[None,:,:],axis=-1)))
  res={'radius':rad,'family':'boundary_star','temporal_faces':size,'physical_diameter':diam,'new_global_curvature_modes':gl,'min_collar_r':minrad,'r0_ext_rank':arr[0][1],'r1_ext_rank':arr[1][1],'r2_ext_rank':arr[2][1],'collar0_links':arr[0][0],'peeled':len(peel),'unpeeled':len(rest)}
  reports.append(res);print(res,flush=True)
(OUT/'boundary_stress.json').write_text(json.dumps(reports,indent=2))
with (OUT/'boundary_stress.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=reports[0].keys());w.writeheader();w.writerows(reports)

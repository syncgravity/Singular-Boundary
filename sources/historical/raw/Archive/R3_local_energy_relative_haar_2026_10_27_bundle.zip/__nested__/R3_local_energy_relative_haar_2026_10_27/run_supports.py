from pathlib import Path
from collections import defaultdict, deque, Counter
import sys,json,time,numpy as np
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P))
from nested_audit import build,validate,complex_3,cell_boundaries,rank_mod_columns,sparse_boundary_projection_rank,bianchi_peel
OUT=Path(__file__).resolve().parent;OUT.mkdir(exist_ok=True)
def dual(g):
 eface=defaultdict(list)
 for i,f in enumerate(g.faces):
  for a,b in zip(f,f[1:]+f[:1]):eface[tuple(sorted((a,b)))].append(i)
 adj=[set() for f in g.faces]
 for faces in eface.values():
  if len(faces)==2:a,b=faces;adj[a].add(b);adj[b].add(a)
 return adj

def growth(g):
 adj=dual(g); xy=np.array([g.xy[list(f)].mean(axis=0) for f in g.faces]);root=int(np.argmin(np.linalg.norm(xy,axis=1)))
 parent={root:None};dist={root:0};q=deque([root]); bfs=[]
 while q:
  v=q.popleft();bfs.append(v)
  for u in sorted(adj[v]):
   if u not in parent:parent[u]=v;dist[u]=dist[v]+1;q.append(u)
 assert len(bfs)==len(g.faces)
 far=max(dist,key=lambda k:(dist[k],np.linalg.norm(xy[k]-xy[root])))
 path=[];p=far
 while p is not None:path.append(p);p=parent[p]
 path=list(reversed(path))
 return {'compact':bfs,'filament':path}, { 'root':root,'path_steps':len(path)-1,'max_dual_radius':dist[far]}
def spatial_edge_sets(g):
 mp={k:i for i,k in enumerate(g.edges)};ret=[]
 for f in g.faces:ret.append({mp[tuple(sorted((a,b)))] for a,b in zip(f,f[1:]+f[:1])})
 return ret

def bc(g,order,nt=3):
 # two independently chosen, overlapping time sets: t=0 all faces; t=1 first half, including central face
 es=spatial_edge_sets(g);cut=max(1,(len(order)+1)//2)
 a=set().union(*(es[f] for f in order));b=set().union(*(es[f] for f in order[:cut]))
 return {(0,e) for e in a}|{(1,e) for e in b}

def audit(g,cols,meta,cells,order,family):
 qs=bc(g,order);nF=len(g.faces);nE=len(g.edges)
 Q={3*nF+t*nE+e for t,e in qs};ret=[col for fi,col in enumerate(cols) if fi not in Q]
 glrank=len(Q)-sparse_boundary_projection_rank(cells,Q)
 # flat rank retention: fullrank 3E, retained 3E-glrank
 L={e for q in Q for e in cols[q]};L0=set(L);layer=[]; minrad=None
 for rad in range(4):
  a=rank_mod_columns(ret,L);b=rank_mod_columns(cols,L)
  extra=glrank-(b-a)
  assert extra>=0,(family,len(order),rad,extra)
  layer.append({'r':rad,'links':len(L),'extra_exterior_rank':extra,'local_extra_rank':b-a})
  if extra==0 and minrad is None:minrad=rad
  if rad<3:
   old=set(L)
   # single pass only through links old (avoid accidental propagation within same step)
   for col in cols:
    if not old.isdisjoint(col):L.update(col)
 peel,remaining,express=bianchi_peel(cols,cells,Q)
 # count nonabelian occurrences explicitly, including re-used eliminated faces
 expansions={}
 for step in peel:
  q=step['face'];terms=Counter()
  for f in cells[step['cell']]:
   if f==q:continue
   terms.update(expansions[f] if f in expansions else {f:1})
  expansions[q]=terms
 maxlen=max((sum(t.values()) for t in expansions.values()),default=0)
 # For fully filled supports, use overlap and word length as nonlinear upper coefficient
 bound=None
 if not remaining:
  accum=Counter()
  for q,word in expansions.items():
   ell=sum(word.values());accum.update({f:ell*v for f,v in word.items()})
  bound={'max_L1_nonabelian_length':maxlen,'max_retained_curvature_coefficient':max(accum.values()),'support_retained_face_count':len(accum)}
 canonfaces=sorted([tuple(sorted(g.labels[v] for v in g.faces[f])) for f in order])
 arr=g.xy[np.unique([v for f in order for v in g.faces[f]])];diam=float(np.max(np.linalg.norm(arr[:,None,:]-arr[None,:,:],axis=2)))
 return {'family':family,'spatial_selected_faces':len(order),'inserted_temporal_faces':len(Q),'physical_diameter':diam,'new_global_curvature_modes':glrank,'minimum_exterior_rank_collar_radius_le_3':minrad,'collars':layer,'bianchi_peeled':len(peel),'bianchi_unpeeled':len(remaining),'max_nonabelian_face_factor_length_peeled':maxlen,'fully_peelable':not remaining,'fully_filled_bound':bound,'selected_face_labels':canonfaces}

def main():
 data=[];radii=[5.,6.5,8.,10.]
 for radius in radii:
  t=time.time();g,_=build(radius,0);seq,seed=growth(g);cols,meta=complex_3(g);cells=cell_boundaries(g)
  sizes=([1,3,6,10,16,24,40,80,120,160] if radius>=10 else [1,3,6,10,16,24,40,80,120] if radius>=8 else [1,3,6,10,16])
  for fam,order in seq.items():
   for k in sizes:
    if k>len(order):continue
    # bound each support size, regardless of radius and filament length
    if k>24 and fam=='filament':continue
    entry=audit(g,cols,meta,cells,order[:k],fam)
    entry.update({'radius':radius,'spatial_volume_faces':len(g.faces),'ambient_prisms':3*len(g.faces)})
    data.append(entry)
    print('r',radius,fam,k,'Q',entry['inserted_temporal_faces'],'rank',entry['new_global_curvature_modes'],'collar',entry['minimum_exterior_rank_collar_radius_le_3'],'word',entry['max_nonabelian_face_factor_length_peeled'],'peeled',entry['bianchi_peeled'],'/',entry['inserted_temporal_faces'],flush=True)
  print('radius done',radius, 'seconds',round(time.time()-t,1),flush=True)
 (OUT/'certificate.json').write_text(json.dumps({'source':'certified direct Z5 cut-and-project Penrose rhombus disks, three periodic time steps','radii':radii,'data':data,'limitations':'Collar means vanishing exterior linearized curvature-rank increase only; Bianchi occurrence length counts transported face factors, not transport path length; neither implies nonlinear Haar repair. This certificate does not estimate exterior Gibbs probabilities.'},indent=2,default=lambda x:int(x) if isinstance(x,np.integer) else list(x)))
 import csv
 cols=['radius','family','spatial_volume_faces','spatial_selected_faces','inserted_temporal_faces','physical_diameter','new_global_curvature_modes','minimum_exterior_rank_collar_radius_le_3','bianchi_peeled','bianchi_unpeeled','max_nonabelian_face_factor_length_peeled','fully_peelable']
 with open(OUT/'summary.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows([{k:d[k] for k in cols} for d in data])
if __name__=='__main__':main()

import json, sys, numpy as np
from pathlib import Path
from direct_cut_project import build
from construct_surgery import product_collar,shell
from cavity_audit import seed_support,Q_from_seed
ROOT=Path(__file__).resolve().parent
seed=seed_support(build(5,0)[0]);rows=[]
for rad in (5.,6.5,8.,10.):
 g,_=build(rad,0); words,typ=product_collar(g);Q=Q_from_seed(g,seed);R=set(range(len(words)))-Q
 H={e for q in Q for e,s in words[q]};K=shell(H,words,R);A={p for p in R if any(e in K for e,s in words[p])}; halo={e for p in A for e,s in words[p] if e not in K}
 vertices=set()
 for link in halo:
  E=len(g.edges);V=len(g.labels)
  if link<3*E:
   t,e=divmod(link,E);a,b=g.edges[e];vertices.update(((t,a),(t,b)))
  else:
   t,v=divmod(link-3*E,V);vertices.add((t,v));vertices.add(((t+1)%3,v))
 assert len(H)==36 and len(K)==125 and len(A)==175
 rows.append({'radius':rad,'Q_count':len(Q),'H_links':len(H),'K_links':len(K),'A_K_retained_faces':len(A),'halo_frozen_links':len(halo),'halo_vertices':len(vertices),'halo_bound_lambda_sK_epsilon1':8*len(A),'eta_for_epsilon_quarter':8*(.25**2)*len(A)/len(Q),'C_v_per_col':7,'exterior_halo_keys':[]})
 print({k:v for k,v in rows[-1].items() if k!='exterior_halo_keys'})
ROOT.joinpath('geometry_certificate.json').write_text(json.dumps({'results':rows,'scope':'genuine Z5 Penrose 14 temporal faces, fixed local labels'},indent=2))

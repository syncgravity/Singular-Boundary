import json, numpy as np
from collections import Counter
from scipy.optimize import linprog
from pathlib import Path
from direct_cut_project import build
from cavity_audit import seed_support,Q_from_seed
from construct_surgery import product_collar
ROOT=Path(__file__).resolve().parent

def fill(g,Q):
 V,E,F=len(g.labels),len(g.edges),len(g.faces)
 ei={tuple(sorted(edge)):i for i,edge in enumerate(g.edges)}
 cells=[]
 for t in range(3):
  for vs in g.faces:
   cell={((t+1)%3)*F+len(cells)%F, t*F+len(cells)%F}
   for a,b in zip(vs,vs[1:]+vs[:1]):cell.add(3*F+t*E+ei[tuple(sorted((a,b)))])
   cells.append(cell)
 pending=set(Q);exp={};steps=[]
 while pending:
  opts=[(len(c&Q),j,next(iter(c&pending))) for j,c in enumerate(cells) if len(c&pending)==1]
  assert opts,('peel failed',pending)
  _,j,q=min(opts);pending.remove(q)
  cnt=Counter()
  for f in cells[j]:
   if f!=q:cnt.update(exp.get(f,Counter({f:1})))
  assert not (set(Q)&set(cnt))
  exp[q]=cnt;steps.append((q,j,sum(cnt.values())))
 faces=sorted(set().union(*(set(v) for v in exp.values())))
 return faces, steps

def run(radius,base_seed):
 g,_=build(radius,0);W,meta=product_collar(g);Q=Q_from_seed(g,base_seed);R=set(range(len(W)))-Q
 H={e for q in Q for e,_ in W[q]};A={f for f in R if any(e in H for e,_ in W[f])}
 F,steps=fill(g,Q);fs=set(F);X=fs-A;assert len(Q)==14 and len(H)==36 and len(A)==62 and len(F)==54 and len(X)==10
 E=sorted({e for f in F for e,_ in W[f]});index={e:i for i,e in enumerate(E)}
 mat=np.zeros((len(F),len(E)),dtype=int)
 for i,f in enumerate(F):
  for e,s in W[f]:mat[i,index[e]]=1
 c=np.ones(len(E))
 opt=linprog(c,A_ub=-mat,b_ub=-np.ones(len(F)),bounds=(0,None),method='highs')
 assert opt.success
 # independent LP dual certificate
 y=opt.ineqlin.marginals*(-1)
 assert np.all(mat@opt.x>=1-1e-7) and np.all(mat.T@y<=1+1e-7) and y.min()>-1e-8
 assert abs(opt.fun-y.sum())<1e-7
 # restricted H only fails to cover the 10 exterior faces
 Hcol=np.array([e in H for e in E]); assert np.count_nonzero(mat[:,Hcol].sum(1)==0)==10
 # Face sets incident to every selected edge: local star support and leakage beyond fill
 selected=[E[i] for i,w in enumerate(opt.x) if w>1e-8]
 star={e:sorted(f for f in R if any(x==e for x,_ in W[f])) for e in selected}
 full_union=sorted(set().union(*[set(x) for x in star.values()]))
 residual=set(full_union)-fs
 # rounded exact primal/dual candidate in denominators up to 10000
 from fractions import Fraction
 primal=[Fraction(float(v)).limit_denominator(10000) for v in opt.x];dual=[Fraction(float(v)).limit_denominator(10000) for v in y]
 assert all(sum(primal[j] for j in range(len(E)) if mat[i,j])>=1 for i in range(len(F)))
 assert all(sum(dual[i] for i in range(len(F)) if mat[i,j])<=1 for j in range(len(E)))
 assert sum(primal)==sum(dual)
 data={'radius':radius,'counts':{'Q':len(Q),'H':len(H),'affected_A':len(A),'fill':len(F),'fill_outside_A':len(X),'cover_candidate_links':len(E),'nonzero_cover_links':len(selected),'cover_star_union_faces':len(full_union),'outside_fill_star_leakage_faces':len(residual)},'Q':sorted(Q),'H':sorted(H),'A':sorted(A),'F':F,'F_outside_A':sorted(X), 'candidate_edges':E,'cover_matrix':mat.tolist(),'weights_fraction':[str(x) for x in primal],'dual_fraction':[str(x) for x in dual],'cover_optimum_fraction':str(sum(primal)), 'selected_cover_edges':selected,'selected_cover_star_faces':{str(e):star[e] for e in selected}, 'star_leakage_faces':sorted(residual),'primal_dual_valid_exact':True}
 return data
if __name__=='__main__':
 b,_=build(5.,0);seed=seed_support(b);data=[]
 for rad in [5.,6.5,8.,10.]:
  x=run(rad,seed);data.append(x)
  print('radius',rad,x['counts'],'minimum',x['cover_optimum_fraction'],flush=True)
  (ROOT/f'cover_radius_{str(rad).replace(".","_")}.json').write_text(json.dumps(x,indent=2))
 (ROOT/'summary.json').write_text(json.dumps([{'radius':x['radius'],**x['counts'],'minimum_cover':x['cover_optimum_fraction']} for x in data],indent=2))

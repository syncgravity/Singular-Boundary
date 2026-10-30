#!/usr/bin/env python3
"""Certified incidence counts for one- and two-shell compact-Haar Peierls bounds.
B is a fixed retained spatial link at time 0, adjacent to a fixed deleted
14-temporal-face support. All sets are compared via exact Z^5 labels.
"""
from pathlib import Path
import sys, json
from collections import Counter
sys.path.insert(0, str(Path(__file__).resolve().parent))
from nested_audit import build,validate,complex_3,seed_support,embed_support,rank_mod_columns,cell_boundaries,bianchi_peel

def ckey(g,e):
 V,E=len(g.labels),len(g.edges)
 if e<3*E:
  t,i=divmod(e,E)
  a,b=g.edges[i]
  return ('s',t, tuple(sorted([g.labels[a],g.labels[b]])))
 t,v=divmod(e-3*E,V)
 return ('v',t,g.labels[v])

def facekey(g,m):
 kind,t,i=m
 if kind=='s':return (kind,t,tuple(sorted(g.labels[v] for v in g.faces[i])))
 a,b=g.edges[i];return (kind,t,tuple(sorted([g.labels[a],g.labels[b]])))

def active_faces(B,cols,R):
 return {p for p in R if bool(B.intersection(cols[p]))}

def expand(B,cols,R):
 P=active_faces(B,cols,R)
 return B|{e for p in P for e in cols[p]}

def main():
 g5,_=build(5.,0);seed=seed_support(g5)
 anchor_key=seed['canonical_edgesets'][0][0]
 reports=[];canonical={}
 for radius in [5.,6.5,8.,10.]:
  g,ga=build(radius,0)
  geo=validate(g,ga)
  cols,meta=complex_3(g)
  _,qs=embed_support(seed,g)
  Q={p for p,m in enumerate(meta) if m[0]=='t' and (m[1],m[2]) in qs}
  R=set(range(len(cols)))-Q
  E=len(g.edges)
  edgemap={tuple(sorted((g.labels[a],g.labels[b]))):i for i,(a,b) in enumerate(g.edges)}
  B={edgemap[anchor_key]}
  blocks=[B]
  for _ in range(2):blocks.append(expand(blocks[-1],cols,R))
  # Certified 14-face nonabelian Bianchi representation and its retained neighborhood.
  cells=cell_boundaries(g)
  peel,left,expressions=bianchi_peel(cols,cells,Q)
  assert not left and len(peel)==len(Q)
  A_fill={p for expr in expressions.values() for p in expr}
  B_fill={e for p in A_fill for e in cols[p]}
  A_touch=active_faces(B_fill,cols,R)
  H_fill=expand(B_fill,cols,R)
  assert len(A_fill)==54 and len(B_fill)==101 and len(H_fill)==232
  row={'radius':radius,'Bianchi_fill_retained_faces':len(A_fill),
       'Bianchi_fill_local_links':len(B_fill),'Bianchi_fill_one_shell_links':len(H_fill),
       'Bianchi_fill_block_affected_faces':len(A_touch),'vertices':len(g.labels),'spatial_faces':len(g.faces),'spacetime_links':3*(len(g.labels)+E),'retained_faces':len(R),'inserted_faces':len(Q),'anchor':str(anchor_key)}
  for j,H in enumerate(blocks):
   A=active_faces(H,cols,R)
   # the faces whose contribution survives in the H-conditional action
   exterior={e for p in A for e in cols[p] if e not in H}
   row[f'B{j}_links']=len(H)
   row[f'B{j}_faces']=len(A)
   row[f'B{j}_boundary_exterior_links']=len(exterior)
   # Rank of the local face equations and the block-link restriction.
   # A strictly positive difference excludes a pointwise flat extension for
   # arbitrary small exterior perturbations in the linearized normal form.
   all_rank=rank_mod_columns([cols[p] for p in sorted(A)])
   interior_rank=rank_mod_columns([cols[p] for p in sorted(A)],H)
   row[f'B{j}_relative_exterior_rank']=all_rank-interior_rank
   row[f'B{j}_interior_rank']=interior_rank
   row[f'B{j}_full_incidence_rank']=all_rank
   h=tuple(sorted(map(str,(ckey(g,e) for e in H))))
   fh=tuple(sorted(map(str,(facekey(g,meta[p]) for p in A))))
   if j not in canonical: canonical[j]=(h,fh)
   else:assert canonical[j]==(h,fh),('non-stable local collar',radius,j)
  reports.append(row)
  print(row,flush=True)
 out={'provenance':'direct Z5 nested Penrose, periodic 3-time extrusion, retained 14-face overlapping temporal support','anchor':str(anchor_key),'results':reports,'check':'exact canonical Z5-labeled local face/link sets agree for all 4 volumes','caveat':'counts do not control the conditional exterior minimum; one-shell Peierls theorem is analytic and independent of these audits'}
 root=Path(__file__).resolve().parent
 (root/'shell_certificate.json').write_text(json.dumps(out,indent=2))
 import csv
 with (root/'shell_counts.csv').open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=reports[0].keys());wr.writeheader();wr.writerows(reports)
if __name__=='__main__':main()

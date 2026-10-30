#!/usr/bin/env python3
"""Minimum additive crossing cost matroid greedy; extra randomized union-cost search."""
import json, random
from pathlib import Path
from collections import Counter
from direct_cut_project import build
from construct_surgery import product_collar,shell
from cavity_audit import seed_support,Q_from_seed
from classify_modes import pivot_basis,link_key
P=Path(__file__).resolve().parent

def run():
 g,_=build(5.,0);words,meta=product_collar(g);Q=Q_from_seed(g,seed_support(g));R=set(range(len(words)))-Q
 H={e for q in Q for e,s in words[q]};A=sorted(p for p in R if any(e in H for e,s in words[p]));ext=sorted({e for f in A for e,s in words[f]}-H)
 inc={e:{i:s for i,p in enumerate(A) for ee,s in words[p] if ee==e} for e in H|set(ext)}
 baselocal=pivot_basis([(e,inc[e]) for e in sorted(H)])
 far={e:{f for f in R if f not in A and any(ee==e for ee,s in words[f])} for e in ext}
 costs={e:len(far[e]) for e in ext}
 original=pivot_basis([(e,inc[e]) for e in sorted(H)]+[(e,inc[e]) for e in ext])[len(baselocal):]
 def score(pivots):return len(set().union(*(far[e] for e in pivots)))
 n=len(original)
 rng=random.Random(20261027)
 best=(score(original),original,'ascending')
 candidates=[]
 for trial in range(2):
  if trial==0:order=sorted(ext,key=lambda e:(costs[e],e))
  elif trial==1:order=sorted(ext,key=lambda e:(costs[e],-len(inc[e]),e))
  else:
   # greedy choice with stochastic tie / submodular running overlap bias; preserve matroid independence each addition
   remaining=set(ext);chosen=[]
   while len(chosen)<n:
    choices=[]
    old=set().union(*(far[e] for e in chosen)) if chosen else set()
    for e in remaining:
     basis=pivot_basis([(x,inc[x]) for x in sorted(H)]+[(x,inc[x]) for x in chosen+[e]])
     if len(basis)>len(baselocal)+len(chosen):
      choices.append((len(far[e]-old)+rng.random()*.15*(1+len(far[e])),e))
    if not choices:break
    e=min(choices)[1];chosen.append(e);remaining.remove(e)
   order=chosen+sorted(remaining)
  chosen=pivot_basis([(e,inc[e]) for e in sorted(H)]+[(e,inc[e]) for e in order])[len(baselocal):]
  assert len(chosen)==n
  s=score(chosen)
  candidates.append((s,trial))
  if s<best[0]:best=(s,chosen,'trial'+str(trial))
 print('basis dimension',n,'original crossing',score(original),'weighted additive crossing',score(pivot_basis([(e,inc[e]) for e in sorted(H)]+[(e,inc[e]) for e in sorted(ext,key=lambda x:(costs[x],x))])[len(baselocal):]),'best',best[0],best[2],flush=True)
 res={'exterior_rank':n,'original_crossing_faces':score(original),'best_crossing_faces':best[0],'best_basis_links':best[1], 'best_basis_z5_labels':[link_key(g,e) for e in best[1]],'cost_hist_original':dict(Counter(costs[e] for e in original)),'cost_hist_best':dict(Counter(costs[e] for e in best[1])),'trial_summary':candidates,'scope':'finite radius-5 optimization of crossing retained faces, not a certified global minimum of union cost'}
 (P/'optimized_basis.json').write_text(json.dumps(res,indent=2))
if __name__=='__main__':run()

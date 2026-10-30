#!/usr/bin/env python3
"""Numerical noncommuting quaternion audit of exact 59-word joint Tietze flat extension.
No claims of full-action monotonicity: exterior crossing faces generally change.
"""
from pathlib import Path
import json
import numpy as np
from direct_cut_project import build
from construct_surgery import product_collar,character_word,qmul,qinv,unit_random
from cavity_audit import seed_support,Q_from_seed
from classify_modes import analyze
from relative_words import solve
P=Path(__file__).resolve().parent

def pro(word,val):
  res=np.array([1.,0.,0.,0.])
  for v in word:res=qmul(res,val[abs(v)-1] if v>0 else qinv(val[-v-1]))
  return res

def run(optimized=False):
    r=solve(True,optimized=optimized);ops=r['operations'];g,_=build(5.,0);words,meta=product_collar(g)
    Q=Q_from_seed(g,seed_support(g));R=set(range(len(words)))-Q
    H={e for q in Q for e,_ in words[q]};A={f for f in R if any(e in H for e,s in words[f])}
    X=set(json.loads((P/'optimized_basis.json').read_text())['best_basis_links']) if optimized else set(analyze(g)[0]['chosen_exterior_link_ids']);J=H|X
    modified={o['edge'] for o in ops};free=J-modified
    assert len(free)==1 and len(modified)==59
    B={f for f in R if any(e in X for e,s in words[f]) and f not in A}
    assert len(B)>0
    rng=np.random.default_rng(20261027);report=[]
    for mode in ('all_haar','center_defect','near_flat'):
      for trial in range(8):
        if mode=='all_haar':U=unit_random(rng,3*(len(g.edges)+len(g.labels)))
        else:
          U=np.tile(np.array([1.,0.,0.,0.]),(3*(len(g.edges)+len(g.labels)),1))
          if mode=='center_defect':
            for e in sorted(X)[::3]:U[e]*=-1.
          else:
            X0=rng.normal(size=(len(U),3));X0/=np.linalg.norm(X0,axis=1,keepdims=True)
            angles=rng.normal(size=len(U))*.02
            U[:,0]=np.cos(angles);U[:,1:]=X0*np.sin(angles)[:,None]
        orig=U.copy()
        # reverse substitution in the exact group presentation, fixing all non-solved physical links
        for op in reversed(ops):
          x=op['edge'];eq=op['face'];w=op['replacement_word']
          U[x]=pro(w,U)
        va=max(1.-character_word(U,words[f]) for f in A)
        assert va<2e-12,(va,mode)
        frozen=np.max(np.linalg.norm(U[[e for e in range(len(U)) if e not in J]]-orig[[e for e in range(len(U)) if e not in J]],axis=1))
        assert frozen<1e-14
        before_A=sum(1.-character_word(orig,words[f]) for f in A)
        after_A=sum(1.-character_word(U,words[f]) for f in A)
        before_B=sum(1.-character_word(orig,words[f]) for f in B)
        after_B=sum(1.-character_word(U,words[f]) for f in B)
        # a full action minimizer cannot be replaced by a map forcing A flat without changing other faces
        delta=(before_A-before_B*0)-((after_A)+(after_B-before_B))
        report.append({'mode':mode,'trial':trial,'A_before':before_A,'A_after':after_A,'crossing_faces':len(B),'crossing_delta':after_B-before_B,'total_action_decrease':before_A+before_B-after_A-after_B,'max_affected_face_error':va})
    summary={'A_face_count':len(A),'Q_face_count':len(Q),'H_link_count':len(H),'X_exterior_pivot_count':len(X),'J_total_link_count':len(J), 'solved_group_relators':len(ops),'residual_trivial_relators':len(A)-len(ops),'free_group_link_count':int(len(free)),'crossing_retained_face_count':len(B),
       'max_fully_expanded_group_word_length':None, 'max_face_error':max(t['max_affected_face_error'] for t in report),'max_crossing_increase':max(t['crossing_delta'] for t in report),'count_full_action_increases':int(sum(t['total_action_decrease']<0 for t in report)),'samples':report,
       'interpretation':'Global flat extension of the 62 local retained face holonomies for arbitrary frozen links; no proof of Gibbs coercivity because crossing retained plaquettes can increase.'}
    (P/('joint_gluing_optimized_certificate.json' if optimized else 'joint_gluing_certificate.json')).write_text(json.dumps(summary,indent=2,default=lambda x: int(x) if isinstance(x,np.integer) else float(x)))
    print('PASS',len(report),'quaternion tests','A=',len(A),'X=',len(X),'crossing=',len(B),'action increases',summary['count_full_action_increases'],flush=True)
if __name__=='__main__':run(False);run(True)

#!/usr/bin/env python3
"""Fully implementable, full-action-monotone, 3-color SU(2) Q8 surgery on all 24 modes.
Theoretical fine-net extension has branchwise Haar jacobian one and finite multiplicity,
but 3-color coordinate descent is NOT a uniform s_H-coercive mechanism.
"""
import json
from pathlib import Path
from collections import defaultdict
import numpy as np
from direct_cut_project import build
from construct_surgery import product_collar,qmul,character_word,unit_random
from cavity_audit import seed_support,Q_from_seed
from classify_modes import analyze,link_key
ROOT=Path(__file__).resolve().parent
Q8=np.asarray([[s,0,0,0] for s in (1.,-1.)]+[[0 if j!=i else s for j in range(4)] for i in range(1,4) for s in (1.,-1.)],dtype=np.float64)
assert Q8.shape==(8,4) and np.array_equal(Q8[0],np.array([1.,0,0,0]))

def apply_surgery(U,words,R,colors):
    res=U.copy();trail=[]
    link_faces=defaultdict(list)
    for f in R:
        for e,s in words[f]:link_faces[e].append(f)
    affected=sorted({f for e in link_faces for f in link_faces[e] if e in {q for gr in colors for q in gr}})
    for color,links in enumerate(colors):
        before_color=sum(1.-character_word(res,words[f]) for f in affected)
        # Face-disjoint within one color: independently choosing the best Q8 translation is exact
        for e in links:
            old=res[e].copy();fac=link_faces[e]
            best=(sum(1.-character_word(res,words[p]) for p in fac),0)
            for idx,g in enumerate(Q8):
                res[e]=qmul(g,old)
                score=sum(1.-character_word(res,words[p]) for p in fac)
                if score<best[0]-1e-12:best=(score,idx)
            res[e]=qmul(Q8[best[1]],old)
            trail.append({'link':int(e),'group':color,'chosen_translation':int(best[1])})
        after_color=sum(1.-character_word(res,words[f]) for f in affected)
        assert after_color<=before_color+1e-9,(color,after_color,before_color)
    return res,trail

def main():
    summary=[];ref=None
    for radius in (5.,6.5,8.,10.):
        g,_=build(radius,0);words,_=product_collar(g)
        seed=seed_support(build(5.,0)[0]);Q=Q_from_seed(g,seed);R=set(range(len(words)))-Q
        basis=analyze(g)[0];colors=basis['colors'];X=set(basis['chosen_exterior_link_ids'])
        touched={f for f in R if any(e in X for e,s in words[f])}
        assert len(touched)==73 and len(X)==24 and len(colors)==3
        rng=np.random.default_rng(20261027+int(radius*100))
        trials=[]
        for i in range(3):
            if i==0:U=np.tile(np.array([1.,0,0,0]),(3*(len(g.edges)+len(g.labels)),1))
            elif i%2:U=unit_random(rng,3*(len(g.edges)+len(g.labels)))
            else:
                U=np.tile(np.array([1.,0,0,0]),(3*(len(g.edges)+len(g.labels)),1))
                for e in sorted(X)[::3]:U[e]*=-1
            new,trail=apply_surgery(U,words,R,colors)
            changed={e for e in range(len(U)) if np.linalg.norm(new[e]-U[e])>1e-10}
            assert changed<=X
            fchanged={f for f in range(len(words)) if abs(character_word(U,words[f])-character_word(new,words[f]))>1e-10}
            assert fchanged<=touched # no inserted faces may touch X; X is exterior to Q
            before=sum(1.-character_word(U,words[f]) for f in touched)
            after=sum(1.-character_word(new,words[f]) for f in touched)
            assert after<=before+1e-9,(radius,i,before,after)
            trials.append({'trial':i,'action_decrease':before-after,'nonidentity_mode_links':len(changed),'modified_face_count':len(fchanged)})
        summary.append({'radius':radius,'Q_count':len(Q),'selected_mode_links':len(X),'colored_groups':list(map(len,colors)),'faces_touched_by_surgery':len(touched), 'max_per_link_face_incidence':max(basis['basis_exterior'][i]['retained_faces_touching_pivot'] for i in range(24)), 'Haar_jacobian_each_branch':1,'max_inverse_multiplicity':8**24,'trials':trials})
        print('rad',radius,'colors',list(map(len,colors)),'action decreases',[round(t['action_decrease'],3) for t in trials],flush=True)
    (ROOT/'full_action_surgery_certificate.json').write_text(json.dumps({'construction':'exact branchwise Haar-preserving 3-color Q8 pivot-coordinate descent over a rank-complete 24-exterior-mode basis','scope':'full retained action never increases; NO quantitative coercivity proportional to s_H and no absolute Gibbs tail','results':summary},indent=2))
if __name__=='__main__':main()

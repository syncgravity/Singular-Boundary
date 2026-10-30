#!/usr/bin/env python3
"""Exact external-link SU(2) center-flip surgery on the genuine Penrose Q14 cavity.
Piecewise Haar Jacobian 1, at most 1+|K\H| preimages, full retained action nonincrease.
Action decrease not coercive in s_H; demonstrated using both hot and cold fields.
"""
import json
from pathlib import Path
import numpy as np
from direct_cut_project import build
from construct_surgery import product_collar,shell,unit_random,character_word
from cavity_audit import seed_support,Q_from_seed
ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(420197)

def trial(radius,hot):
    g,_=build(radius,0);faces,meta=product_collar(g)
    qset=Q_from_seed(g,seed_support(build(5.,0)[0]))
    rfaces=[i for i in range(len(faces)) if i not in qset]
    H={e for p in qset for e,s in faces[p]};K=shell(H,faces,set(rfaces));outer=sorted(K-H)
    U=unit_random(rng,3*(len(g.labels)+len(g.edges))) if hot else np.tile(np.array([1.,0,0,0]),(3*(len(g.labels)+len(g.edges)),1))
    cos=np.array([character_word(U,faces[p]) for p in rfaces]);energy=float(np.sum(1.-cos))
    adjacency={e:[] for e in outer}
    for j,p in enumerate(rfaces):
        for e,ss in faces[p]:
            if e in adjacency:adjacency[e].append(j)
    sums={e:float(cos[adjacency[e]].sum()) for e in outer}
    # Because U_e -> -U_e, every incident plaquette has cos -> -cos.
    candidates={e:-2*x for e,x in sums.items()}
    best=max(candidates,key=candidates.get)
    if candidates[best]<=0:
        chosen=None;expected=0.
    else:
        chosen=best;expected=candidates[best]
    if chosen is not None:U[chosen]*=-1
    after=np.array([character_word(U,faces[p]) for p in rfaces]); energy_after=float(np.sum(1.-after))
    assert abs((energy-energy_after)-expected)<1e-9,(energy-energy_after,expected)
    unchanged=[p for j,p in enumerate(rfaces) if chosen is None or chosen not in {e for e,_ in faces[p]}]
    # explicit inverse branch: same center-flip is its own inverse
    assert len(outer)>0 and energy_after<=energy+1e-9
    return {'radius':radius,'hot_Haar_links':hot,'Q':len(qset),'H_links':len(H),'K_links':len(K),
        'exterior_candidate_links':len(outer),'center_flip_branch_choices':len(outer)+1,
        'Haar_jacobian_each_branch':1,'chosen_link':chosen,'full_retained_action_before':energy,
        'full_retained_action_after':energy_after,'exact_full_action_drop':energy-energy_after,
        'nonincident_retained_faces_invariant':len(unchanged),'coercivity_in_s_H':'not established'}

def main():
    x=[trial(rad,hot) for rad in [5.,6.5,8.,10.] for hot in [False,True]]
    (ROOT/'center_flip_certificate.json').write_text(json.dumps({'construction':'Select strongest energy-decreasing center flip on one exterior collar link, otherwise identity. Each branch is SU2 central multiplication, exact Haar Jacobian 1; multiplicity <=1+number of possible selected links.', 'algebraic_identity':'S_R(U)-S_R(flip_e U) = -2 sum_{p in R: p contains e} Tr W_p(U)/2', 'tests':x,'warning':'No positive coercivity proportional to the absolute exterior frustration; tests of hot/Haar states are algebraic, not equilibrium Gibbs sampling.'},indent=2))
    for row in x:print(row['radius'],'hot',row['hot_Haar_links'],'|K\\H|',row['exterior_candidate_links'],'drop',round(row['exact_full_action_drop'],5))
if __name__=='__main__':main()

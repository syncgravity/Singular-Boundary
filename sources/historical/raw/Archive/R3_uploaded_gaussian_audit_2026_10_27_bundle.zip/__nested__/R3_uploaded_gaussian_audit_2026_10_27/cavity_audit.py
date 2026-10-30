#!/usr/bin/env python3
"""Exact nested labels, local support and surgery collar counts for fixed Q14 Penrose cavity."""
import json,math
from pathlib import Path
import numpy as np
from direct_cut_project import build,validate
from construct_surgery import product_collar,shell,net,unit_random
ROOT=Path(__file__).resolve().parent

def seed_support(g):
    center=np.array([g.xy[list(f)].mean(axis=0) for f in g.faces]);root=int(np.argmin(np.linalg.norm(center,axis=1)))
    neighbors=[]
    for f,vs in enumerate(g.faces):
        if f!=root and len(set(g.faces[root])&set(vs))==2:
            neighbors.append((float(np.linalg.norm(center[f])),f))
    ids=[root]+[f for _,f in sorted(neighbors)[:2]]
    assert len(ids)==3
    labels=[tuple(sorted(g.labels[v] for v in g.faces[f])) for f in ids]
    return labels

def Q_from_seed(g,seed):
    fmap={tuple(sorted(g.labels[v] for v in f)):i for i,f in enumerate(g.faces)}
    faces=[g.faces[fmap[key]] for key in seed]
    edge_ind={pair:i for i,pair in enumerate(g.edges)}
    ed_sets=[{edge_ind[tuple(sorted((a,b)))] for a,b in zip(f, f[1:]+f[:1])} for f in faces]
    qkeys={(0,e) for e in ed_sets[0]|ed_sets[1]}
    qkeys.update({(1,e) for e in ed_sets[0]|ed_sets[2]})
    F,E=len(g.faces),len(g.edges)
    return {3*F+t*E+e for t,e in qkeys}

def run():
    base,_=build(5.,0);seed=seed_support(base);out=[]
    for r in (5.,6.5,8.,10.):
        g,ga=build(r,0);check=validate(g,ga);faces,metadata=product_collar(g)
        Q=Q_from_seed(g,seed);R=set(range(len(faces)))-Q
        H={e for p in Q for e,s in faces[p]}
        levels=[H];
        for _ in range(2):levels.append(shell(levels[-1],faces,R))
        row={'radius':r,'rhombi':check['faces'],'Q_inserted_face_count':len(Q),
             'H_initial_links':len(levels[0]),'K_one_shell_links':len(levels[1]),
             'K_two_shell_links':len(levels[2]),
             'retained_faces_touched_by_H':sum(any(e in levels[0] for e,s in faces[p]) for p in R),
             'retained_faces_touched_by_K':sum(any(e in levels[1] for e,s in faces[p]) for p in R),
             'surgery_k_over_q':len(levels[1])/len(Q),
             'jacobian':1,'generic_net_inverse_multiplicity_log_bound':'k*(log 4097 + 1.5 log lambda)'}
        assert len(Q)==14 and len(levels[0])==36 and len(levels[1])==125
        out.append(row)
    # Verify worst-case angle across a random SU(2) sample for the constructed net.
    pts=[];rng=np.random.default_rng(19878)
    for lam in (1.,4.):
        G,n=net(lam)
        samples=unit_random(rng,400)
        near=[]
        for s in samples:
            # geodesic angle on SU(2) S^3; do not identify q and -q
            nearest=np.clip((G@s).max(),-1.,1.)
            angle=float(np.arccos(nearest))
            near.append(angle)
        assert max(near)<=lam**(-.5)+1e-12
        pts.append({'lambda':lam,'net_size':len(G),'max_sample_geodesic_error':max(near),
                    'rigorous_geodesic_error_upper':1/math.sqrt(lam)})
    cert={'support_seed_genuine_Z5_labels':[[list(v) for v in f] for f in seed],
          'geometry_results':out,'net_random_angle_checks':pts,
          'note':'Actual source anchor is Q14 overlapping temporal faces in intervals 0 and 1. Numerical net cover checks are supplemental; the mathematical cover guarantee follows from dominant-coordinate charts. No unconditional terminal s_K estimate.'}
    (ROOT/'cavity_certificate.json').write_text(json.dumps(cert,indent=2));print(json.dumps(cert,indent=2))
if __name__=='__main__':run()

#!/usr/bin/env python3
"""Finite geometric audit of the constants in a conditional nonlinear Haar-ball theorem.
Theorem: a block's curvature energy ABOVE its exterior-conditioned minimum
has a uniform logarithmic tail, not its raw energy/staple frustration.
"""
import sys,json,math
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'/mnt/data/R3_local_energy_relative_haar_2026_10_27')
from direct_cut_project import build
from nested_audit import complex_3
r=[]
for radius in (5.,6.5,8.,10.):
    g,_=build(radius)
    cols,_=complex_3(g)
    hits=Counter(edge for col in cols for edge in col)
    hist=Counter(hits.values())
    r.append({'radius':radius,'links':3*(len(g.edges)+len(g.labels)),
              'faces':len(cols),'max_face_edge_count':max(map(len,cols)),
              'max_link_face_incidence':max(hits.values()),
              'incidence_histogram':{str(k):v for k,v in sorted(hist.items())}})
assert all(x['max_face_edge_count']==4 and x['max_link_face_incidence']<=7 for x in r)
c=8/(3*math.pi**3)
C=14-math.log(c)
cert={'geometry':r,'nu':7,'p':4,'haar_ball_volume_coefficient':c,
      'lambda_min':1,'local_energy_excess_bound':f'lambda E[S_B-min(S_B)|exterior] <= |B|*(1.5 log(lambda)+{C:.12f})',
      'uniform_conditional_upper_tail':f'P(lambda*(S_B-min(S_B)) >= 3*|B|*log(lambda)+{2*C:.12f}*|B|+2*s | exterior) <= exp(-s)',
      'missing':'no uniform bound on lambda E exterior-conditional min(S_B); thus no arbitrary 3D R3 theorem',
      'derivation':'SU(2)^|B| Haar geodesic balls radius lambda^-1/2 at action minimum; Hessian of each quadrilateral <= sum tangent norms squared; each link in <=7 faces; concavity of negative log partition function'}
(ROOT/'conditional_block_certificate.json').write_text(json.dumps(cert,indent=2))
print(json.dumps(cert,indent=2))

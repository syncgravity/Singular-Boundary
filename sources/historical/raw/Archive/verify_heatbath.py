#!/usr/bin/env python3
"""Exact SU(2) one-link heatbath and Ward identity numerical audit.

Numerical tests only: analytic derivations are in FORMAL_NOTE.md.
"""
import json
from pathlib import Path
import numpy as np
from scipy.special import ive
from scipy.integrate import quad

OUT=Path(__file__).with_name('verification.json')

def heatbath(t):
    if t == 0: return 0.0, 1.0, 0.0
    L = float(ive(2,t)/ive(1,t))
    # y=1-cos(theta), tilted Haar density proportional to sqrt(y(2-y))exp(-ty)
    # integrate on [0,2] using shifted exponential; stable for t <=100.
    if t <= 100:
        z=quad(lambda y: np.sqrt(y*(2-y))*np.exp(-t*y),0,2,epsabs=1e-13)[0]
        Ey=quad(lambda y: y*np.sqrt(y*(2-y))*np.exp(-t*y),0,2,epsabs=1e-13)[0]/z
        err=abs(Ey-(1-L))
    else:
        Ey=1-L;err=None
    return L, Ey, err

records=[]
for t in [0,0.01,0.1,1,3,10,30,100,1000]:
    L,Ey,err=heatbath(t)
    records.append(dict(t=t,mean_cos=L,mean_1_minus_cos=Ey,t_times_excess=t*Ey,
                        quadrature_vs_bessel_error=err,upper_bound=1.5,
                        passes=bool(t*Ey<=1.5+1e-10)))

rng=np.random.default_rng(271828)
examples=[]
for n in [1,2,3,7]:
    for _ in range(25):
        a=rng.normal(size=(n,4));a/=np.linalg.norm(a,axis=1)[:,None]
        R=np.linalg.norm(a.sum(axis=0))
        pair=sum(np.dot(a[i]-a[j],a[i]-a[j]) for i in range(n) for j in range(i+1,n))
        examples.append(abs((n-R)*(n+R)-pair))

result={"convention":"SU(2) as unit quaternions, Haar=S^3 uniform, d=1-ReTr/2",
        "tests":records,"max_pair_identity_error":max(examples),
        "opposite_staple_obstruction":{"n":2,"staples":[[1,0,0,0],[-1,0,0,0]],
             "R":0,"m_e":2,"conditional_mean_S_e":2,
             "conditional_mean_each_face_d":1,
             "lambda_times_each_face_energy":"lambda (unbounded at fixed exterior)"},
        "all_checks_pass":bool(all(x['passes'] for x in records) and max(examples)<1e-12)}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_checks_pass':result['all_checks_pass'],
                  'max_pair_identity_error':result['max_pair_identity_error'],
                  'large_t_excess':records[-1]['t_times_excess']},indent=2))

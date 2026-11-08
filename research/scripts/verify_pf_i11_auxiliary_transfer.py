#!/usr/bin/env python3
"""PF-I11 controlled finite SU2 class-function transfer, NOT emergent time.

An independent auxiliary semigroup tests the mathematical sufficiency of a
strictly positive transfer once a kinetic Casimir and an ordering dt are ADDED.
Neither dt nor Casimir scale follows from the author's intrinsic Z5 2+2+1
geometry or the physical Yang-Mills existence/mass-gap problem.
"""
from __future__ import annotations
import argparse,json,math
import numpy as np
from numpy.polynomial.legendre import leggauss


def transfer(beta=.71, dt=.12, electric_scale=1., n_char=8, nquad=400):
    assert beta>=0 and dt>0 and electric_scale>0 and n_char>=2 and nquad>=2*n_char
    x,w=leggauss(nquad)
    theta=(x+1)*math.pi/2
    # Haar-conjugacy radial measure: (2/pi)sin²(theta)dtheta
    weights=w*np.sin(theta)**2
    # Jacobian pi/2 times 2/pi yields 1 exactly.
    chars=np.stack([np.sin((n+1)*theta)/np.sin(theta) for n in range(n_char)],axis=1)
    orth=chars.T@(weights[:,None]*chars)
    M=chars.T@((weights*np.exp(-.5*dt*beta*(1-np.cos(theta))))[:,None]*chars)
    j=np.arange(n_char)/2
    D=np.exp(-dt*electric_scale*j*(j+1))
    T=(M*D[None,:])@M.T
    eig=np.linalg.eigvalsh(T)
    eig=np.sort(eig)[::-1]
    gap=-math.log(eig[1]/eig[0])/dt
    return {'beta':beta,'dt':dt,'electric_scale':electric_scale,'characters':n_char,'nquad':nquad,
            'max_character_Haar_orthogonality_error':float(np.max(np.abs(orth-np.eye(n_char)))),
            'min_symmetric_mult_matrix_eigenvalue':float(np.linalg.eigvalsh(M).min()),
            'min_transfer_eigenvalue':float(eig.min()),
            'two_top_eigenvalues':eig[:2].tolist(),
            'auxiliary_gap':gap,
            'scope':'Auxiliary positive finite transfer only. No intrinsic time/reflection on source Z5 proven; no volume-uniform interacting gap.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    rows=[transfer(beta=.71,dt=.12,electric_scale=e) for e in [.1,.5,1.,2.]]
    rows.extend([transfer(beta=0,dt=.12,electric_scale=e) for e in [.1,.5,1.]])
    with open(a.output,'w') as f:f.write(json.dumps({'scope':'auxiliary finite transfer only, not physical temporal reconstruction','rows':rows},indent=2,sort_keys=True)+'\n')
    for row in rows:print(json.dumps({k:row[k] for k in ['beta','electric_scale','auxiliary_gap','min_transfer_eigenvalue']}))

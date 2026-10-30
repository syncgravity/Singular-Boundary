#!/usr/bin/env python3
"""Deterministic finite face-edge incidence and oscillator test. No MCMC.

Three seed rhombi are transcribed from historical
HISTORICAL_Q14_CANONICAL.json:seed_faces_z5; the square tests are analytic
control complexes, NOT substitute Penrose data.
"""
from itertools import combinations
import json, hashlib, math
from pathlib import Path
import numpy as np
import sympy as S

seed = [
 [[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
 [[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1]],
 [[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]],
]

def orient_quad(face):
    pts = [tuple(v) for v in face]
    z = tuple(min(v[i] for v in pts) for i in range(5))
    ns = [v for v in pts if sum(abs(v[i]-z[i]) for i in range(5)) == 1]
    assert len(ns) == 2
    u,v=ns
    w=tuple(u[i]+v[i]-z[i] for i in range(5)); assert w in pts
    def project(p):
        return (sum(p[i]*math.cos(2*math.pi*i/5) for i in range(5)),
                sum(p[i]*math.sin(2*math.pi*i/5) for i in range(5)))
    p0,p1,p2=project(z),project(u),project(v)
    area=(p1[0]-p0[0])*(p2[1]-p0[1])-(p1[1]-p0[1])*(p2[0]-p0[0])
    assert abs(area)>0.5
    return [z,u,w,v] if area>0 else [z,v,w,u]

def incidence(quad_faces):
    faces=[orient_quad(face) for face in quad_faces]
    keys=sorted({tuple(sorted((face[i],face[(i+1)%4]))) for face in faces for i in range(4)})
    idx={k:j for j,k in enumerate(keys)}
    B=S.zeros(len(faces),len(keys))
    for i,face in enumerate(faces):
        for j in range(4):
            s,t=face[j],face[(j+1)%4]
            key=tuple(sorted((s,t)))
            B[i,idx[key]]=1 if s==key[0] else -1
    return B,keys,faces

B,edges,faces=incidence(seed)
L=B*B.T
expected=S.Matrix([[4,-1,-1],[-1,4,0],[-1,0,4]])
assert L==expected, f'Wrong actual oriented seed incidence: {L}'
assert len(edges)==10
assert L.charpoly().as_expr().factor()==(S.Symbol('lambda')-4)*(S.Symbol('lambda')**2-8*S.Symbol('lambda')+14)
# Smallest eigenvalue 4-sqrt(2); oscillator physical scalar gap, a=b=1:
lam = 4-S.sqrt(2)
assert S.simplify(4*S.sqrt(lam/8)-S.sqrt(2*lam))==0

# Closed form for m x m simply-connected square face grid; exact eigenvalues.
square=[]
for m in [1,2,3,4,6,8,12]:
    val=4-4*math.cos(math.pi/(m+1))
    bdperarea=4/m
    assert val>0 and val<=bdperarea+1.e-12
    square.append({'side_faces':m,'faces':m*m,'boundary_edges':4*m,
                   'lambda_min_dual':round(val,12),'constant_trial_bound':round(bdperarea,12),
                   'gaussian_singlet_gap_factor_sqrt_ab':round(math.sqrt(2*val),12)})

out={
 'source':'Three canonical seed rhombi transcribed from historical HISTORICAL_Q14_CANONICAL.json; no original generator reexecuted',
 'seed_face_count':len(seed), 'seed_unique_links':len(edges),
 'oriented_incidence_B':[[int(B[i,j]) for j in range(B.cols)] for i in range(B.rows)],
 'seed_BBt':[[int(L[i,j]) for j in range(L.cols)] for i in range(L.rows)],
 'seed_eigenvalues':['4-sqrt(2)','4','4+sqrt(2)'],
 'seed_boundary_edges':int(sum(1 for j in range(B.cols) if sum(abs(B[i,j]) for i in range(B.rows))==1)),
 'seed_constant_vector_rayleigh':str((S.ones(1,3)*L*S.ones(3,1))[0]/3),
 'square_control_exact_formula':'lambda_min = 4-4*cos(pi/(m+1))',
 'square_controls':square,
 'harmonic_physical_singlet_gap_formula':'sqrt(2*a*b*lambda_min(B*B.T))',
 'actual_interacting_penrose_gap_proved':False,
 'monte_carlo':False
}
outpath=Path('/mnt/data/sb_collective_dual_20261028/DUAL_CERTIFICATE.json')
outpath.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('oriented_incidence_B','square_controls')},indent=2))

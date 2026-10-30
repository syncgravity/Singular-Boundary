#!/usr/bin/env python3
"""Read-only symbolic SU(2) finite-character and reflection-sector audits.

No MCMC, no large-volume approximation, no alteration of historical material.
"""
import sympy as sp
import json
from itertools import combinations

a,c,q,delta1,delta2 = sp.symbols('a c q delta1 delta2',positive=True)

def curvature(H_diag,A):
    """Exact vacuum variance second derivative for H(t)=H0-t*c*A.

    H0 diagonal with simple vacuum at slot 0, A selfadjoint, <0|A|0>=0.
    Returns the 3 parity-resolved contributions with c^2 divided out.
    """
    n=len(H_diag)
    e0=sp.eye(n)[:,0]
    G=sp.diag(*([sp.Integer(0)]+[1/x for x in H_diag[1:]]))
    x=A*e0
    y=G*x
    V=(x.T*x)[0]
    S=A*A*e0-V*e0
    t1=sp.factor(4*(S.T*G*A*y)[0])
    t2=sp.factor(2*(y.T*(A*A-V*sp.eye(n))*y)[0])
    t3=sp.factor(-8*(x.T*y)[0]**2)
    return V,t1,t2,t3,sp.factor(t1+t2+t3)

# Authentic three-face Penrose spatial seed recovered from Z^5 labels.
seed=[
 [[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
 [[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1]],
 [[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
faces=[frozenset(tuple(v) for v in f) for f in seed]
perm=(3,2,1,0,4)
def refl(v):return tuple(v[perm[i]] for i in range(5))
assert [faces.index(frozenset(refl(v) for v in f)) for f in faces]==[0,2,1]
def edges(f):
    return {tuple(sorted((u,v))) for u,v in combinations(f,2)
        if sum(abs(i-j) for i,j in zip(u,v))==1}
E=[edges(f) for f in faces]
assert len(set().union(*E))==10
assert not (E[1]&E[2]), 'outer seed faces must share no link'

# Fundamental SU2 class characters |n>=chi_(n/2); p=chi_(1/2)/2
# -Delta eigenvalue n(n+2)/4, four equally-weighted links = a*n(n+2).
P=sp.Matrix([[0,sp.Rational(1,2),0],
             [sp.Rational(1,2),0,sp.Rational(1,2)],
             [0,sp.Rational(1,2),0]])
levels=[0,3*a,8*a]
val_single=curvature(levels,P)
assert val_single[0]==sp.Rational(1,4)
assert sp.simplify(val_single[-1]+1/(32*a*a))==0
# The genuine 3-face graph at b=0 has an invariant product-character
# sector for outer edge-disjoint plaquettes; the center is a spectator.
AA=sp.Matrix(sp.kronecker_product(P,sp.eye(3))-sp.kronecker_product(sp.eye(3),P))
levs=[i+j for i in levels for j in levels]
val_outer=curvature(levs,AA)
assert val_outer[0]==sp.Rational(1,2)
assert sp.simplify(val_outer[-1]+1/(16*a*a))==0

# Other parity-resolved channels can make V'' positive: exact 3-level witness.
B=sp.Matrix([[0,1,0],[1,0,q],[0,q,0]])
R=sp.diag(1,-1,1)
assert R*B*R==-B
val_3=curvature([0,delta1,delta2],B)
assert sp.simplify(val_3[-1]-(4*q*q/(delta1*delta2)+2*(q*q-4)/delta1**2))==0
assert val_3[-1].subs({q:3,delta1:1,delta2:2})==28
assert val_3[-1].subs({q:0,delta1:1,delta2:2})==-8

# Verify exact SU2 1-face Taylor R_2(b)=-(b/(64a^2))+O(b^2):
# H_b=4a(-Delta)+b(1-p), and V''(b=0) = -1/(32 a^2),
# V'(b)=2R_2(b). By center invariance V'(0)=0.
assert sp.simplify(val_single[-1]/2+1/(64*a*a))==0

certificate={
    'historical_seed_faces':3,'seed_edges':10,
    'reflection_face_permutation':[0,2,1],
    'outer_faces_edge_disjoint':True,
    'electric_one_plaquette_variance':str(val_single[0]),
    'electric_one_plaquette_second_response_over_c2':str(val_single[-1]),
    'electric_seed_outer_antisymmetric_variance':str(val_outer[0]),
    'electric_seed_outer_antisymmetric_second_response_over_c2':str(val_outer[-1]),
    'one_plaquette_even_three_source_linear_b_coefficient':str(val_single[-1]/2),
    'abstract_positive_second_derivative_example':str(val_3[-1].subs({q:3,delta1:1,delta2:2})),
    'abstract_negative_second_derivative_example':str(val_3[-1].subs({q:0,delta1:1,delta2:2})),
    'tests_passed':True,'monte_carlo':False,
    'uniform_nonlinear_Penrose_response_proved':False
}
print(json.dumps(certificate,indent=2))

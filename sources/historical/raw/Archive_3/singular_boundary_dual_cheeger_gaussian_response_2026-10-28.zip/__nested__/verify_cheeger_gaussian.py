#!/usr/bin/env python3
"""Exact checks for Penrose dual Cheeger and Gaussian response identities.
No Monte Carlo, no numerical Yang-Mills configurations.
"""
import sympy as s
from itertools import combinations
from fractions import Fraction as F
import json

# The original canonical three-rhombus seed incidence matrix, from Q14 spatial labels.
seed = [
 [[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
 [[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1]],
 [[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]],
]
def faces_edges(v):
    t = [tuple(x) for x in v]
    return {tuple(sorted((a,b))) for a,b in combinations(t,2) if sum(abs(i-j) for i,j in zip(a,b))==1}
faces=[faces_edges(z) for z in seed]
edges=sorted(set().union(*faces))
assert len(edges)==10 and len(faces)==3
L=s.zeros(len(faces))
for i,f in enumerate(faces):
    for j,g in enumerate(faces):
        L[i,j]=4 if i==j else -len(f & g)
assert L==s.Matrix([[4,-1,-1],[-1,4,0],[-1,0,4]])
assert set(L.eigenvals()) == {4-s.sqrt(2),s.Integer(4),4+s.sqrt(2)}

shape_min=s.sin(s.pi/5)
cheeger_lower=s.pi*shape_min/(2*len(faces))
assert (4-s.sqrt(2)).evalf(25)>cheeger_lower.evalf(25)
# test all nonempty subsets of the seed face set against planar Cheeger bound
for mask in range(1,1 << len(faces)):
    S=[i for i in range(len(faces)) if mask & (1<<i)]
    region_edges={e for i in S for e in faces[i]}
    boundary=sum(sum(e in faces[i] for i in S)==1 for e in region_edges)
    assert s.Integer(boundary)**2>=4*s.pi*shape_min*len(S)  # geometric perimeter lower bound

# Verify the Gaussian vacuum covariance identity Sigma V Sigma = M/4, exact radical algebra.
a,b=s.symbols('a b',positive=True)
# uniform coefficients on the original three-face seed
M=a*L
V=b*s.eye(3)/8
projectors=[]
for eig in L.eigenvals():
    P=s.eye(3)
    for other in L.eigenvals():
        if other!=eig:P=P*(L-other*s.eye(3))/(eig-other)
    projectors.append((eig,s.simplify(P)))
root=sum((s.sqrt(eig)*P for eig,P in projectors),s.zeros(3))
assert all(s.simplify(x)==0 for x in root*root-L)
Sigma=s.sqrt(2*a/b)*root
assert all(s.simplify(x)==0 for x in Sigma*V*Sigma-M/4)
assert all(s.simplify((Sigma*Sigma)[i,i]-8*a/b)==0 for i in range(3))

# One-face reference: variance(p^quad) = 3a/(4b).
Sigma_1=2*s.sqrt(2*a/b)
assert s.simplify(s.Rational(3,32)*Sigma_1**2-3*a/(4*b))==0

# Fourth moment constant: for second Gaussian chaos, E[A^4]/Var(A)^2 <= 15.
# Single centered square has equality: E(Z²-1)^4=60, variance=2.
z=s.symbols('z',real=True)
def gmoment(n):
    return 0 if n%2 else s.factorial2(n-1) if n>0 else s.Integer(1)
assert sum((s.binomial(4,k)*(-1)**(4-k)*gmoment(2*k) for k in range(5)),s.Integer(0))==60
assert 60/(2**2)==15

# Scaling exponents: b_min=beta_min/h², sum c²~h^(2-2alpha)
alpha, h=s.symbols('alpha h',positive=True)
assert s.expand(2+(2-2*alpha))==4-2*alpha
assert (4-2*alpha).subs(alpha,s.Rational(3,2))==1
assert s.simplify((s.Rational(3,2)*(4-2*alpha)).subs(alpha,s.Rational(3,2)))==s.Rational(3,2)

out={
 'source':'canonical three-rhombus Penrose seed, not the full Q14 temporal cavity',
 'seed_faces':3,'seed_distinct_edges':10,
 'face_dirichlet_matrix':str(L),
 'face_dirichlet_spectrum':['4-sqrt(2)','4','4+sqrt(2)'],
 'isoperimetric_cheeger_lower_for_seed':str(cheeger_lower),
 'all_nonempty_seed_subsets_checked':7,
 'Gaussian_covariance_Sigma_V_Sigma':'M/4 (exact)',
 'Gaussian_one_face_quadratic_Wilson_variance':'3a/(4b)',
 'Gaussian_centered_quadratic_fourth_moment_ratio_bound':15,
 'alpha_three_halves_variance_order':'O(h)',
 'alpha_three_halves_three_source_response_order':'O(h^(3/2)) (conditional finite-area Gaussian model)',
 'nonlinear_three_source_window_proved':False,
 'simulation':False,
 'all_exact_checks_passed':True,
}
print(json.dumps(out,indent=2))

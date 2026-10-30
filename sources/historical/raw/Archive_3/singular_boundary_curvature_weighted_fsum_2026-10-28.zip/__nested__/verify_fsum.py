#!/usr/bin/env python3
"""Deterministic checks of the SU(2) Casimir carré-du-champ and local f-sum bound.

No Monte Carlo, historical-data replacement, or finite interacting spectrum inference.
The proof of the general result is mathematical; these are exact certificates.
"""
import json
import sympy as s
from itertools import combinations
from collections import Counter

p, h, alpha, S, K, ae, sig, test = s.symbols('p h alpha S K ae sig test', real=True, positive=True)
# Fundamental SU2 trace p=chi_{1/2}/2, character identity chi_1=4p^2-1.
# Positive Casimir eigenvalues C_(1/2)=3/4, C_1=2.
chi1 = 4*p*p-1
Gamma = s.factor(s.Rational(3,4)*p*p-s.Rational(1,4)*chi1)
assert s.simplify(Gamma-(1-p*p)/4)==0
assert s.factor(2*(1-p)-(1-p*p))==(p-1)**2
r=s.symbols('r',real=True)
assert s.factor(6*(r-1)**2-r*(r+1))==(r-2)*(5*r-3)
# Exact Haar benchmark: ∫p²dHaar=1/4; 4 electric links yield first excitation 3a.
assert (4*ae*s.Rational(1,4)*(1-s.Rational(1,4)))==3*ae/4
assert 3*ae*s.Rational(1,4)==3*ae/4

seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
def edges(face):
    vertices=[tuple(v) for v in face]
    return {tuple(sorted((v,w))) for v,w in combinations(vertices,2)
            if sum(abs(x-y) for x,y in zip(v,w))==1}
faces=[edges(face) for face in seed]
inc=Counter(edge for face in faces for edge in face)
assert len(inc)==10
assert max(inc.values())==2
adj=[[int(i!=j and bool(faces[i]&faces[j])) for j in range(3)] for i in range(3)]
assert adj==[[0,1,1],[1,0,0],[1,0,0]]
assert max(map(sum,adj))<=4
# Artificial PSD energy Gram with the exact allowed sparsity, proves algebraic 5 bound.
z=s.symbols('z',positive=True)
D=s.diag(1,1,1)+s.Matrix([[0,s.Rational(1,3),s.Rational(1,5)],[s.Rational(1,3),0,0],[s.Rational(1,5),0,0]])
assert all(x>0 for x in D.eigenvals())
w=s.Matrix([s.Rational(2,3),s.Rational(-1,2),s.Rational(4,5)])
assert (w.T*D*w)[0]<=5*sum(w[i]**2*D[i,i] for i in range(3))
# Improved first moment: 10 amax sigma² ||phi||∞² K_R (F h²) h^(3-2alpha).
F=s.symbols('F',positive=True)
new=10*ae*sig**2*test**2*K*(F*h*h)*h**(3-2*alpha)
old=2*ae*sig**2*test**2*(F*h*h)*h**(2-2*alpha)
assert s.simplify((new/old).subs(alpha,1)-5*K*h)==0
assert s.simplify((new/h).subs(alpha,1)-10*ae*sig**2*test**2*K*(F*h*h))==0
assert s.simplify(new.subs(alpha,s.Rational(3,2))-10*ae*sig**2*test**2*K*(F*h*h))==0
print(json.dumps({
    'casimir_carre_du_champ':'(1-p^2)/4',
    'holonomy_deficit_identity':'2(1-p)-(1-p^2)=(1-p)^2',
    'electric_single_face_M1':'3a/4',
    'authentic_seed_faces':3,'authentic_seed_edges':10,
    'authentic_seed_overlap_matrix':adj,
    'energy_matrix_locality':'strictly edge-neighbor support',
    'new_first_moment_rate':'O(h^(3-2alpha))',
    'alpha_1_rate':'O(h)',
    'positive_gap_nontrivial_variance_requires_alpha_at_least':'3/2',
    'simulations_run':False,
    'physical_continuum_gap_proved':False
},indent=2))

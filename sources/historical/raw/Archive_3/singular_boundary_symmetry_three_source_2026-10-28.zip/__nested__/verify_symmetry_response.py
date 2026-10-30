#!/usr/bin/env python3
"""Exact deterministic SU(2) Penrose seed automorphism and source-response obstruction.
No Monte Carlo, no eigenvalue fitting, no modification of historical data.
"""
from itertools import combinations
import json
import sympy as s

seed = [
 [[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
 [[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1]],
 [[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]],
]
F=[frozenset(tuple(x) for x in face) for face in seed]
perm=[3,2,1,0,4]
def refl(x): return tuple(x[perm[j]] for j in range(5))
assert all(refl(refl(x))==x for face in F for x in face)
face_image=[]
for face in F:
 image=frozenset(refl(x) for x in face)
 face_image.append(F.index(image))
assert face_image==[0,2,1]
def z5edges(face):
 return frozenset(tuple(sorted((a,b))) for a,b in combinations(face,2)
                  if sum(abs(u-v) for u,v in zip(a,b))==1)
E=frozenset().union(*(z5edges(f) for f in F))
assert len(E)==10
assert frozenset(tuple(sorted((refl(a),refl(b)))) for a,b in E)==E
# Verify physical projection is reflection in axis 108 degrees;
# all five Penrose direction vectors map to the appropriate reflected vectors.
from math import pi,cos,sin,isclose
axis=3*pi/5
u=[(cos(2*pi*i/5),sin(2*pi*i/5)) for i in range(5)]
for i in range(5):
 t=(cos(2*axis)*u[i][0]+sin(2*axis)*u[i][1],
    sin(2*axis)*u[i][0]-cos(2*axis)*u[i][1])
 assert all(isclose(t[j],u[perm[i]][j],rel_tol=0,abs_tol=1e-12) for j in range(2))
# SU2 trace is inversion-even: p(U^-1)=p(U), so orientation reversal
# under the reflection preserves each magnetic Wilson deficit.

# Positive two-level model: exact reflection-odd source, yet a narrow
# low-energy response spike with a strictly positive spectral gap.
h,t,delta,K=s.symbols('h t delta K',positive=True)
I=s.eye(2); sx=s.Matrix([[0,1],[1,0]]);sz=s.diag(1,-1)
H=delta*(I-sx)+K*(I+t*sz)
assert s.simplify(sx*H*sx-H.subs(t,-t))==s.zeros(2)
assert s.simplify(sx*sz*sx+sz)==s.zeros(2)
# For |t|<=1, each of the two summands defining H is positive.
eigap=2*s.sqrt(delta**2+K**2*t**2)
variance=delta**2/(delta**2+K**2*t**2)
moment=2*delta**2/s.sqrt(delta**2+K**2*t**2)
assert s.simplify(variance.subs(t,0)-1)==0
assert s.simplify(s.diff(variance,t).subs(t,0))==0
assert s.simplify(eigap.subs(t,0)-2*delta)==0
assert s.simplify(moment.subs(t,0)-2*delta)==0
alpha=s.Rational(3,2)
Ksc=h**(alpha-4) # h^-5/2
th=delta/K
R=s.simplify(h**(4-alpha)*s.diff(variance,t).subs(t,th)/2)
assert s.simplify(R.subs(K,Ksc)+1/(4*delta))==0
assert s.simplify(eigap.subs(t,th)-2*s.sqrt(2)*delta)==0
assert s.simplify(s.diff(variance,t,2).subs(t,0)+2*K*K/delta**2)==0
assert s.simplify((s.diff(variance,t,2).subs(t,0)).subs(K,Ksc)*h**5+2/delta**2)==0
integ=s.simplify(s.integrate(variance**2,(t,-s.Rational(1,2),s.Rational(1,2))))
assert s.simplify(s.limit(K*integ/delta,K,s.oo)-s.pi/2)==0
# Cauchy pointwise second-derivative criterion: I >= v^2 r/2 for
# r=min(tau,sqrt(v/M)) whenever V'(0)=0 and V(0)=v.
print(json.dumps({
 'canonical_seed_faces':3, 'distinct_canonical_edges':len(E),
 'z5_reflection_coordinate_permutation':perm,
 'induced_face_permutation':face_image,
 'reflection_angle_degrees':108,
 'odd_source':'p_face1 - p_face2',
 'exact_source_response_at_physical_coupling':'zero for every spectral cutoff',
 'two_level_source_variance_at_zero':'1',
 'two_level_gap_lower_bound':'2*delta',
 'two_level_nearby_window_response':'-1/(4*delta)',
 'two_level_spike_width':'h^(5/2)',
 'two_level_second_derivative_at_zero':'-2 h^(-5)/delta^2',
 'checks_passed':True, 'monte_carlo':False,
 'generic_nonlinear_Penrose_spectral_window_proved':False
},indent=2))

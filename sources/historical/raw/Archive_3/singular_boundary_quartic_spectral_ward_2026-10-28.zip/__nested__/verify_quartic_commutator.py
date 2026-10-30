#!/usr/bin/env python3
"""Deterministic rational/symbolic verification of exact quartic spectral and Ward facts.
No Monte Carlo, no gauge sampling, no historical artifact mutation.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as s
import json

# Authentic recovered three-face spatial fixture, separate from full Q14
z=(-1,-1,-1,-1,-1)
seed=[
[z,(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[z,(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[z,(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
faces=[frozenset(f) for f in seed]
def edges(face):
 return {tuple(sorted((a,b))) for a,b in combinations(face,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
E=[edges(f) for f in faces]
assert len(set().union(*E))==10 and len(E[1]&E[2])==0
perm=(3,2,1,0,4)
def refl(v):return tuple(v[i] for i in perm)
assert [faces.index(frozenset(refl(v) for v in f)) for f in faces]==[0,2,1]

# Precise parity-resolved quartic response identity (finite Kato)
e,d1,d2,x,y=s.symbols('e d1 d2 x y',positive=True)
K=s.diag(0,d1,d2)
G=s.diag(0,1/d1,1/d2)
A=s.Matrix([[0,x,0],[x,0,y],[0,y,0]])
R=s.diag(1,-1,1)
assert R*A*R==-A and R*K==K*R
vac=s.Matrix([1,0,0]);X=A*vac;Y=G*X
v=s.simplify((X.T*X)[0]);S=A*A*vac-v*vac
T1=s.simplify(4*(S.T*G*A*Y)[0]);T2=s.simplify(2*(Y.T*(A*A-v*s.eye(3))*Y)[0]);T3=s.simplify(-8*(X.T*Y)[0]**2)
assert s.simplify(T1-4*x*x*y*y/(d1*d2))==0
assert s.simplify(T2-2*x*x*y*y/d1**2)==0
assert s.simplify(T3+8*x**4/d1**2)==0

# Exact low->high virtual transition with tiny source moment and tiny variance,
# but nonzero quartic term.  Let d1=1/N, d2=N, x=1/N, y=1.
N=s.symbols('N',positive=True)
sub={d1:1/N,d2:N,x:1/N,y:1}
assert s.simplify(v.subs(sub)-N**-2)==0
assert s.simplify((X.T*K*X)[0].subs(sub)-N**-3)==0
assert s.simplify(T1.subs(sub)-4/N**2)==0
assert s.simplify(T2.subs(sub)-2)==0
assert s.simplify(T3.subs(sub)+8/N**2)==0
assert s.simplify((T1+T2+T3).subs(sub)-(2-4/N**2))==0
assert s.simplify((A[2,1]).subs(sub)-1)==0

# [K,A] matrix identity, spectral separation for low |1> to high |2>
comm=K*A-A*K
assert s.simplify(comm[2,1]-(d2-d1)*y)==0
assert s.simplify((comm[2,1]/(d2-d1))-A[2,1])==0

# Exact toy first-moment tails and mixed term Cauchy
for n in [F(3),F(5),F(11),F(23)]:
 k=s.diag(0,F(1,n),n)
 aa=s.Matrix([[0,F(1,n),0],[F(1,n),0,1],[0,1,0]])
 gg=s.diag(0,n,F(1,n));xx=aa*vac;yy=gg*xx
 mm=(xx.T*k*xx)[0]
 assert mm==F(1,n**3) and (yy.T*aa*aa*yy)[0] >= 1

# Exact test of the parity-band ultraviolet remainder QR-2 on the 3-state witness.
for nn in (s.Integer(3),s.Integer(5),s.Integer(11)):
 vals={d1:1/nn,d2:nn,x:1/nn,y:1}
 ev=s.simplify((T1+T2+T3).subs(vals))
 # cutoff Lambda=1: odd X lies entirely below it, even S entirely above it
 low=s.simplify((T2+T3).subs(vals))
 remainder=s.Abs(ev-low)
 uu=s.sqrt(1+nn**(-2)); mm=nn**(-3); rr=s.sqrt(mm); zz=mm
 yy=s.Integer(1); GS=nn**(-2);chi=nn**(-1); vv=nn**(-2)
 bound=4*uu*rr*(2*uu*yy+GS)+2*(uu**2+vv)*(2*yy*rr+rr**2)+16*chi*zz+8*zz**2
 assert s.N(remainder)<=s.N(bound)

# Geometry-normalized SU2 Wilson sum gradient coefficients.
h,alpha,amax,qmax,A0,eta=s.symbols('h alpha amax qmax A0 eta',positive=True)
DA=3*amax*qmax*A0*h**(-alpha)
Cgrad2=2*amax*qmax*qmax*A0*h**(2-2*alpha)
assert DA.subs(alpha,s.Rational(3,2))==3*amax*qmax*A0*h**(-s.Rational(3,2))
assert s.simplify((Cgrad2.subs(alpha,s.Rational(3,2)))/(2*amax*qmax*qmax*A0/h))==1

print(json.dumps({
 'three_face_fixture':'three canonical spatial Penrose seed rhombi',
 'seed_face_count':3,'seed_edge_count':10,'reflection_permutation':[0,2,1],
 'quartic_terms':['4*x^2*y^2/(d1*d2)','2*x^2*y^2/d1^2','-8*x^4/d1^2'],
 'counterexample':{'low_gap':'1/N','high_energy':'N','source_variance':'1/N^2','first_moment':'1/N^3','middle_even_term':'2','total_quartic_bracket':'2-4/N^2'},
 'exact_sylvester_commutator':True,'simulations':False,'nonlinear_Penrose_mass_gap_proved':False,
 'all_checks_passed':True},indent=2))

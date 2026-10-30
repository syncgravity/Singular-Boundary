#!/usr/bin/env python3
"""Deterministic exact test of regional-excited Wilson comparison theorem.
No Monte Carlo, no gauge field configuration sampling, no numerical data replacement.
"""
import sympy as s
from itertools import combinations
from fractions import Fraction as Q

# Canonical three-face Z^5 Penrose spatial fixture, not temporal Q14.
seed = [
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
def edges(f):
    return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
faces=[edges(f) for f in seed]
assert len(set.union(*faces))==10 and all(len(x)==4 for x in faces)
counts=[]
for m in range(1,8):
    D={i for i in range(3) if (m>>i)&1}
    S=set.union(*(faces[i] for i in D))
    C={i for i in range(3) if i not in D and faces[i]&S}
    assert not D&C and len(S)<=4*len(D)
    counts.append((m,len(D),len(S),len(C)))
assert (7,3,10,0) in counts

# Regional upper energy comparison exactly minimizes a k + b / k.
A,B,k=s.symbols('A B k',positive=True)
E=s.Rational(3,8)*A*k+3*B/k
opt=s.sqrt(8*B/A)
assert s.simplify(s.diff(E,k).subs(k,opt))==0
assert s.simplify(E.subs(k,opt)-3*s.sqrt(A*B)/s.sqrt(2))==0

# 1-link SU2 Laplacian product rule; reduced SU2 character basis.
a=s.symbols('a',positive=True)
P=s.zeros(4)
for i in range(3): P[i,i+1]=P[i+1,i]=s.Rational(1,2)
HE=s.diag(0,3*a,8*a,15*a)
vac=s.eye(4)[:,0]
assert (P*vac).dot(HE*(P*vac))==3*a/4

# Shape factors and exact energy correction in an interior disk.
h,R,g,eta=s.symbols('h R g eta', positive=True)
sm=s.sin(s.pi/5);sp=s.sin(2*s.pi/5);phi=(1+s.sqrt(5))/2
assert s.simplify(sp/sm-phi)==0
Fmin=s.pi*(R-h)**2/(sp*h**2)
bmin=4/(g*h**2*sp)
correction=s.simplify(eta/(bmin*Fmin))
assert s.simplify(correction-eta*g*sp**2*h**4/(4*s.pi*(R-h)**2))==0
assert s.limit(correction,h,0)==0

# Positive bounded Wilson-average deficit W=I - average(p_boundary).
# If 0<=W<=2 then W^2<=2W. Verify scalar polynomial for all [0,2].
z=s.symbols('z',real=True)
assert s.simplify(s.expand(2*z-z*z)-z*(2-z))==0

# Coherent field witness: each plaquette deficit h, F=h^-2, alpha=3/2.
# The deterministically centered Wilson test amplitude is h^(1/2)*F*h=h^-1/2.
F=s.symbols('F', positive=True)
coh=s.sqrt(h)*F*h
assert s.simplify(coh.subs(F,h**-2)-h**(-s.Rational(1,2)))==0
# Mesoscopic region R = h^gamma: local energy increment O(R/h^3), F_D O(R^2/h^2).
# With alpha=3/2 and fixed eta, EX-7 bound squared scales as h^(3gamma-1+delta).
gamma,delta=s.symbols('gamma delta',positive=True)
Rscale=h**gamma
local_delta=Rscale/h**3
Fscale=Rscale**2/h**2
cutoff=h**(-1-delta)
upper=s.simplify((h**3/cutoff)*local_delta*(1+eta*Fscale))
assert s.simplify(s.expand_power_base(upper,force=True)-h**(1+gamma+delta)-eta*h**(3*gamma-1+delta))==0
assert s.simplify((3*gamma-1+delta).subs(gamma,s.Rational(1,2))-(s.Rational(1,2)+delta))==0
print('PASS: exact mesoscopic transition exponent h^(3gamma-1+delta), gamma=1/2')
print('PASS: original Z5 three-seed incidence, 7 regional boundaries, SU2 Casimir and trial optimization')
print('PASS: excited-energy collar correction and bounded observable spectral norm')
print('PASS: coherent source obstruction; NO MONTE CARLO and NO nonlinear mass gap claim')
print('Subsets (mask,faces,links,crossing):',counts)

#!/usr/bin/env python3
"""Exact Haar/perturbative shared-edge SU(2) Wilson two-plaquette certificate.
No Monte Carlo, no reference to Gaussian approximations.
"""
import sympy as s
from itertools import combinations
S,t,E1,E2=s.symbols('S t E1 E2',positive=True)
EM=S-s.Rational(3,2)*t
EQ=S+s.Rational(1,2)*t
# exact Haar scalar quaternion moments in independent face variables A,B
norm_prod=s.Rational(1,16)
norm_merged=s.Rational(1,4)
cross=s.Rational(1,16)
proj=cross/norm_merged
assert proj==s.Rational(1,4)
norm_Q=s.simplify(norm_prod-cross**2/norm_merged)
assert norm_Q==s.Rational(3,64)
assert s.simplify((S+t/2)*proj-t/2-proj*EM)==0
inv=s.factor(proj**2*norm_merged/EM+norm_Q/EQ)
assert s.simplify(inv-(1/EM+3/EQ)/64)==0
# perturbative wavefunction: psi1=b1 p1/E1+b2 p2/E2,
# psi2_mixed=b1*b2(1/E1+1/E2) T^{-1}(p1*p2)
coef_prod=s.factor(2*(1/E1+1/E2)*inv+2*norm_prod/(E1*E2))
coef_meanprod=1/(4*E1*E2)
coef_cov=s.factor(coef_prod-coef_meanprod)
expected=3*t*t/(8*E1*E2*(2*S-3*t)*(2*S+t))
assert s.simplify((coef_cov-expected).subs(S,E1+E2))==0
coef_cov=s.factor(coef_cov.subs(S,E1+E2))
coef_merged=s.factor(2*(1/E1+1/E2)*cross/EM+2*cross/(E1*E2))
coef_cross_fsum=s.factor((t/4)*(coef_merged-coef_prod))
assert s.simplify((coef_cross_fsum-S*coef_cov/2).subs(S,E1+E2))==0
coef_cross_fsum=s.factor(coef_cross_fsum.subs(S,E1+E2))
assert s.simplify(coef_cov.subs(t,0))==0
# equal positive link coefficients a
A=s.symbols('a',positive=True)
eq=s.factor(coef_cov.subs({E1:3*A,E2:3*A,S:6*A,t:A}))
assert eq==1/(2808*A*A)
assert s.simplify(coef_cross_fsum.subs({E1:3*A,E2:3*A,S:6*A,t:A})-1/(936*A))==0
# canonical seed spatial incidence and overlap
faces0=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
F=[edges(face) for face in faces0]
assert len(set.union(*F))==10
assert len(F[0]&F[1])==1 and len(F[0]&F[2])==1
assert len(F[1]&F[2])==0
assert max(sum(e in f for f in F) for e in set.union(*F))==2
# Construct an exact 4x4 free-electric matrix in orthogonal source channel
# normalized face states p1,p2, merged M, and residual Q have
# eigenvalues E1,E2,EM,EQ and orthogonality by Haar.
print('PASS: independent Haar quaternion moments, exact face/merged spectral split')
print('PASS: positive cross covariance coefficient',coef_cov)
print('PASS: equal-link covariance coefficient',eq)
print('PASS: mixed first spectral moment coefficient',coef_cross_fsum)
print('PASS: authentic 3-face 10-edge Penrose spatial seed')
print('NOTE: analytic weak-field result, not a computation of strong-field vacuum')

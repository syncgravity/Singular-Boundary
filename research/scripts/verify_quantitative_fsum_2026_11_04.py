#!/usr/bin/env python3
"""Independent exact-symbolic and quadrature regressions for the SU(2) local f-sum bound.
Not a proof of the interacting Yang--Mills mass gap.
"""
from __future__ import annotations
from scipy.special import roots_jacobi
import math
import sympy as sp
import numpy as np

x,T,Q,lam=sp.symbols('x T Q lam', real=True, nonnegative=True)
q=1-x*x
# Radial unit-round-S^3 Laplacian on functions of x=Re U.
def lap(f): return sp.expand((1-x*x)*sp.diff(f,x,2)-3*x*sp.diff(f,x))
assert sp.simplify(lap(q)-(6-8*q)) == 0
assert sp.simplify((1-x*x)*sp.diff(q,x)**2-4*q*(1-q)) == 0
# For real positive normalized phi=sqrt rho: 6-8Q <= 4 sqrt(T Q(1-Q)).
poly=sp.expand((6-8*Q)**2-16*T*Q*(1-Q))
roots=sp.solve(poly,Q)
qmin=(6+T-sp.sqrt(T*(T+3)))/(2*(4+T))
assert any(sp.simplify(qmin-r)==0 for r in roots)
assert sp.simplify(qmin.subs(T,0)-sp.Rational(3,4)) == 0
moment=4*qmin
bound_lam=sp.simplify(moment.subs(T,2*lam))
assert sp.simplify(bound_lam.subs(lam,0)-3)==0
assert sp.simplify(bound_lam.subs(lam,1)-(8-sp.sqrt(10))/3)==0
assert sp.simplify(bound_lam.subs(lam,2)-(10-sp.sqrt(28))/4)==0
# The monotonicity in T can be checked by the strictly negative derivative.
expr=sp.simplify(sp.diff(moment,T))
# symbolic rationalized derivative for T>0, with denominator >0
expect=-(4*sp.sqrt(T)*sp.sqrt(T+3)+5*T+12)/(sp.sqrt(T)*sp.sqrt(T+3)*(T+4)**2)
assert sp.simplify(expr-expect)==0
# Integration regression using the normalized Haar marginal (2/pi)*sqrt(1-x^2) dx.
nodes, weights=roots_jacobi(120, 0.5, 0.5)
haar=weights*(2.0/math.pi)
# Check Haar normalization to quadrature tolerance (endpoint cusp O(n^-3)).
assert abs(np.sum(haar)-1)<1e-13, np.sum(haar)
checks=0
for beta in [-3,-1,0,0.2,0.6,1,2,3]:
    for k in [1,2,3]:
        # phi proportional to exp(beta*x^k): positive analytic density
        v=np.exp(2*beta*nodes**k-2*max(0,abs(beta)))
        p=haar*v
        p=p/np.sum(p)
        qvals=1-nodes**2
        Qn=float(np.dot(p,qvals))
        dlogphi=beta*k*nodes**(k-1)
        Tn=float(np.dot(p,qvals*dlogphi*dlogphi))
        # Integration by parts identity tested numerically
        lhs=float(np.dot(p,6-8*qvals))
        rhs=2*float(np.dot(p, (2*nodes)*dlogphi*qvals)) # -2 grad(phi) grad(q) ; d q/dx=-2x
        assert abs(lhs-rhs)<1e-11, (beta,k,lhs,rhs)
        lower=float(moment.subs(T,Tn))
        assert 4*Qn+1e-9>=lower, (beta,k,Qn,Tn,lower)
        checks+=1
print('PASS: exact S^3 radial identities, quadratic root, monotonicity, coupling constants')
print(f'PASS: {checks} positive smooth SU(2) Haar-density quadrature tests')
print(f'lambda=0 lower f-sum: {float(bound_lam.subs(lam,0)):.12f}')
print(f'lambda=1 lower f-sum: {float(bound_lam.subs(lam,1)):.12f}')
print(f'lambda=2 lower f-sum: {float(bound_lam.subs(lam,2)):.12f}')
print('This is a first spectral moment bound, not a spectral gap.')
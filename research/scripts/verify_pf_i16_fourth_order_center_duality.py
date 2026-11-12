#!/usr/bin/env python3
"""PF-I16 exact mixed fourth-order SU(2) vacuum-energy coefficient."""
import sympy as s
from scipy.linalg import eigh_tridiagonal
import numpy as np
lf,lg,a=s.symbols("lf lg a",positive=True)
L=lf+lg
D0=L-s.Rational(3,2)*a
D1=L+s.Rational(1,2)*a
normal=L/(16*lf**2*lg**2)
linked=(1/lf+1/lg)**2*(1/(64*D0)+3/(64*D1))
c=s.factor(normal-linked)
expected=-3*a*a*L/(64*lf**2*lg**2*D0*D1)
assert s.simplify(c-expected)==0
assert c.subs({lf:3,lg:3,a:1})==-s.Rational(1,8424)
assert s.simplify(normal-(1/lf+1/lg)**2/(16*(lf+lg)))==0
assert s.Rational(5,128*27)==s.Rational(5,3456)
n=np.arange(60,dtype=float)
for b in (.1,.06,.03,.015):
    eig=eigh_tridiagonal(n*(n+2),np.full(59,-b/2),select='i',select_range=(0,0),eigvals_only=True)[0]
    truncated=-b*b/12+5*b**4/3456
    assert abs(eig-truncated)<.002*b**6
    print(f"b={b:.3f}: E0={eig:.14g}, quartic={truncated:.14g}")
print("PASS: connected fourth order C_fg=-1/8424, disjoint cancellation, one-loop spectral checks")

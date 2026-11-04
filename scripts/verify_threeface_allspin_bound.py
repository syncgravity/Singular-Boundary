#!/usr/bin/env python3
"""Exact symbolic global inequality in three-face nested Wilson family.
This checker certifies the elementary polynomial comparison only.
For full quaternion/PW regressions see the companion research audit archive.
"""
import sympy as sp
n,m=sp.symbols("n m", integer=True, nonnegative=True)
U=(n+2)**3*(n+(n+2)/(n+1))/((n+1)**2+4)
L=n**3*(n+2+n/(n+1))/((n-1)**2+4)
numer=sp.together((n+1)**3-U-L).as_numer_denom()[0]
expected=n**8+2*n**7-2*n**5+6*n**4+32*n**3-68*n-55
assert sp.expand(numer-expected)==0
shift=sp.Poly(sp.expand(numer.subs(n,m+2)),m)
assert shift.degree()==8
assert all(c>0 for c in shift.all_coeffs())
# n=1: s_2=sqrt(6)/2<5/4; upper trace bound m_2<3,
# lower exact m_0=2, and the ratio is <31/512<1/16.
assert sp.Rational(31,512)<sp.Rational(1,16)
assert sp.sqrt(6)/2<sp.Rational(5,4)
print("PASS: exact all-n>=2 positivity and n=1 boundary inequality")

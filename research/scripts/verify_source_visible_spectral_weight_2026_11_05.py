#!/usr/bin/env python3
"""Exact algebraic verification of a source-visible positive-frequency mass bound.
Conditional on P53/P55 local energy bounds and P78 excitation measure construction.
"""
import sympy as s
l=s.symbols('l',nonnegative=True)
c=(6+2*l-s.sqrt(4*l*l+6*l))/(2+l)
assert s.simplify(c.subs(l,0)-3)==0
assert s.simplify(c.subs(l,1)-(8-s.sqrt(10))/3)==0
# Demonstrate strict positivity of c via (6+2l)^2 > 4l^2+6l.
assert s.expand((6+2*l)**2-(4*l*l+6*l))==36+18*l
# Local commutator estimates: ||Kf||inf<=6, sup Gamma<=4,
# mean of local weighted Dirichlet term <= (6+2+2)lambda/2=5lambda.
B=2*6**2+2*(2**2)*4*5*l
assert B==72+160*l
# Select epsilon=c/8, M0<=4: M1-eps*M0 >= c/2.
epsilon=s.simplify(c/8)
mass_lb=s.simplify(c*c/(4*B))
assert s.simplify(mass_lb.subs(l,1)-( (8-s.sqrt(10))/3 )**2/(4*232))==0
for z in [s.Rational(0),s.Rational(1,4),s.Rational(1),s.Rational(2),s.Rational(10)]:
 a=float(c.subs(l,z)); e=float(epsilon.subs(l,z)); b=float(B.subs(l,z)); q=float(mass_lb.subs(l,z))
 assert 0<q<=4 and a>0 and e>0
 print(f'lambda={z}: m1>={a:.12f}, second<={b:.6f}, Ethreshold={e:.12f}, mass>={q:.12f}')
print('EXACT SYMBOLIC CHECKS PASS; spectral gap not established')
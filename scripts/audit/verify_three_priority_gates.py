#!/usr/bin/env python3
"""Exact deterministic checks for SC-1 and SI-1; no Monte Carlo."""
from fractions import Fraction as Q
import sympy as s
import json
phi=(1+s.sqrt(5))/2
assert s.simplify(s.sin(2*s.pi/5)/s.sin(s.pi/5)-phi)==0
low=s.simplify(s.Rational(32,3)/phi); high=s.simplify(s.Rational(128,3)*phi)
assert bool(low<high)
T=s.diag(1,s.Rational(1,2),s.Rational(1,4))
A=s.Matrix([[0,0,1],[0,0,0],[1,0,0]])
N=6;n=2
mixed=s.simplify(s.trace(T**(N-n)*A*T**n*A)/s.trace(T**N))
assert mixed==s.Rational(272,4161)
assert s.simplify((T**n*A*s.Matrix([1,0,0]))[1])==0
w=[Q(1,4),Q(3,4)];E=[Q(1,10),Q(3,2)]
assert sum(w)==1 and sum(x*y for x,y in zip(w,E))==Q(23,20)
print(json.dumps(dict(symbolic_phi=str(phi),dimensionless_coupling_lower_coefficient=str(low),dimensionless_coupling_upper_coefficient=str(high),mixed_transfer_derivative=str(mixed),unobserved_first_excitation="1/2",simulation=False),indent=2))

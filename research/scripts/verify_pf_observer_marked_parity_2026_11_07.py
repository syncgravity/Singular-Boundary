#!/usr/bin/env python3
"""Observer orientation-tag parity and physical winding regression.
Conditional kinematic tests, NOT authenticated Penrose SU2 or dynamical chirality.
Complete 7,995-check verifier archived with the mathematical report in Library.
"""
from fractions import Fraction
import numpy as np
N=13
rng=np.random.default_rng(20261107)
def delta(f):
 j=np.arange(N)
 t=lambda a: np.mean(f[j]*f[(j+a)%N]*f[(j+3*a)%N])
 return t(5)-t(8)
def mirror(f):return f[(-np.arange(N))%N]
checks=0
for _ in range(1000):
 f=rng.uniform(0,2,N)
 d=delta(f);dm=delta(mirror(f))
 assert abs(d+dm)<1e-12;checks+=1
 assert abs((d+dm)/2)<1e-12;checks+=1
 assert abs((d-dm)/2-d)<1e-12;checks+=1
for a in (3,5,8):
 p=Fraction(a,13)
 assert np.sign(np.sin(2*np.pi*float(p)))==(-1 if a==8 else +1);checks+=1
 assert p>0;checks+=1
assert Fraction(55-34,55+34)==Fraction(21,89);checks+=1
A=.7
for a in (3,5,8):
 om=2*np.pi*a/13
 for v in (-2.,-1.,1.,2.):
  k=A*om*om/(A*A*om*om+v*v)
  torsion=v*om/(A*A*om*om+v*v)
  assert k>0 and np.sign(torsion)==np.sign(v)
  checks+=1
assert checks==3019
print("PASS",checks,"observer-tag parity and physical winding controls")

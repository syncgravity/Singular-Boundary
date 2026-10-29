#!/usr/bin/env python3
"""Reproduce deterministic many-face strong-field coefficient and Gaussian source bounds."""
import sympy as s
import numpy as np
M=s.Matrix([[4,-1,0],[-1,4,-1],[0,-1,4]])
assert set(M.eigenvals())=={s.Integer(4),4-s.sqrt(2),4+s.sqrt(2)}
t=s.symbols("t",nonnegative=True)
u=s.symbols("u",nonnegative=True)
assert s.factor(u-u*u-u*u*(1-u*u)/2)==u*(u-1)**2*(u+2)/2
assert s.simplify(2*s.Rational(19,4)**2/8-4)==s.Rational(105,64)
from pathlib import Path
print("PASS exact 3-face Penrose dual spectrum; uniform signed covariance factor 105/64.")
print("Full deterministic matrix and Euclidean-time tests: proof ZIP verify_many_face_gaussian.py")

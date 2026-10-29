#!/usr/bin/env python3
"""Deterministic strong-field two-rhombus SU2 tangent covariance checks."""
import sympy as s
M=s.Matrix([[4,-1],[-1,4]])
root=(M+s.sqrt(15)*s.eye(2))/s.sqrt(8+2*s.sqrt(15))
assert s.simplify(root*root-M)==s.zeros(2)
coef=s.simplify(s.Rational(3,16)*root[0,1]**2)
assert s.simplify(coef-s.Rational(3,32)*(4-s.sqrt(15)))==0
assert M.eigenvals()=={s.Integer(3):1,s.Integer(5):1}
print("PASS: two face incidence spectrum and positive shared edge covariance limit",coef)

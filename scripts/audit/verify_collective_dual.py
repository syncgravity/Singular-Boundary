#!/usr/bin/env python3
"""Exact canonical 3-rhombus incidence, no MCMC; full output in handoff package."""
import sympy as s
L=s.Matrix([[4,-1,-1],[-1,4,0],[-1,0,4]])
assert set(L.eigenvals())=={4-s.sqrt(2),s.Integer(4),4+s.sqrt(2)}
assert (s.ones(1,3)*L*s.ones(3,1))[0]/3==s.Rational(8,3)
print("Original 3-seed incidence spectrum:",list(L.eigenvals()))
print("Full orientation/read-only checker: singular_boundary_collective_dual_laplacian_2026-10-28.zip")

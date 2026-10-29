#!/usr/bin/env python3
"""Deterministic rational spectral compactness checks; no Monte Carlo."""
from fractions import Fraction as F
import numpy as np
for h in [F(1,2),F(1,5),F(1,10)]:
  for E,w in [(F(1),F(1)),(F(1)/h,h),(h,F(1)/h)]:
    assert E*w==1 and E**3*w<=1/h**2
    assert h*(E*w/(h*E))==w
  E,w=1/h,h;eps=F(1,4);R=F(2)
  assert E*w>=F(1,2) and w>=h/(2*R) and eps<=h*E<=R
for tau in [0.,.5,2.]:
  M=np.zeros((2,2))
  for E,c in [(2.,np.array([1.,3.])),(5.,np.array([2.,-1.]))]:
    M+=E*np.exp(-.2*E*tau)*np.outer(c,c)
  assert np.linalg.eigvalsh(M).min()>-1e-10
print("PASS: three exact spectral regimes and matrix spectral positivity; no Monte Carlo")

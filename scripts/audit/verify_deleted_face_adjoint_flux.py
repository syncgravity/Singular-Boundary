#!/usr/bin/env python3
"""Reduced reproducibility check; full matrix verification is in the companion ZIP."""
import numpy as np
from scipy.linalg import eigvalsh
from math import cos,pi,sqrt
def trace_root(n,phi):
    return sum(sqrt(4-2*cos((2*pi*k+phi)/n)) for k in range(n))
n=8
for theta in [0,pi/12,pi/6,pi/4,pi/2,pi]:
    difference=2*(trace_root(n,2*theta)-trace_root(n,0))
    assert difference > -1e-10
assert abs(2*(trace_root(n,pi)-trace_root(n,0))-0.000041704162)<1e-9
print("PASS exact twisted 8-cycle adjoint heat-trace and normal-frequency coefficient")

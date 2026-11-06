#!/usr/bin/env python3
"""Geometry/capacity regression only: no interacting-vacuum simulation."""
import math
import numpy as np

checks=0
for r in np.geomspace(1e-4,.2,100):
    d=2*r*r
    theta=math.acos(1-d)
    vol=(theta-math.sin(theta)*math.cos(theta))/math.pi
    asym=4*math.sqrt(2)/(3*math.pi)*d**1.5
    assert .98<vol/asym<1.02
    assert 1-math.cos(2*r)<=2*r*r+1e-12
    checks+=2

# Compact radial hat f(u)=max(1-|u|/R,0) in 3D.
# Dirichlet energy 4*pi*R/3, and inner-ball L2 integral explicit.
for R in np.geomspace(.001,2,50):
    energy=4*math.pi*R/3
    for t in np.linspace(.002,1,100):
        w=t*R
        inner=4*math.pi*(w**3/3-w**4/(2*R)+w**5/(5*R*R))
        assert 0<=inner/(w*w*energy)<=1
        checks+=1
print("PASS",checks,"Haar-cap and H1 radial-capacity calibrations")

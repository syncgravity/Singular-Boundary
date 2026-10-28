#!/usr/bin/env python3
"""Exact rational audit of the bounded-degree KP criterion. No simulations."""
from fractions import Fraction
for degree in (4,6,9,17):
    threshold=Fraction(1,degree*degree+degree+1)
    assert (degree+1)*threshold/(1-degree*degree*threshold)==1
    half=threshold/2
    assert (degree+1)*half/(1-degree*degree*half)<1
    print(degree,str(threshold))
print("All rational inequalities passed; abstract KP theorem not re-proved.")

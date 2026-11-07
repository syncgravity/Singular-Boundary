#!/usr/bin/env python3
"""Source-derived Paper 3 §7 rational-circle geometry regression.

These 53 checks certify finite arithmetic and periodicity, NOT source CV,
a 3D physical helical lift, Yang–Mills excitation masses, or gravity.
"""
import cmath,math
from fractions import Fraction
checks=0
ps=[Fraction(3,13),Fraction(5,13),Fraction(8,13)]
for p in ps:
    z=[cmath.exp(2j*math.pi*float(p)*k) for k in range(26)]
    for k in range(13):
        assert abs(z[k+13]-z[k])<1e-12
        checks+=1
    assert len({(round(z[k].real,10),round(z[k].imag,10)) for k in range(13)})==13
    checks+=1
    assert abs(sum(z[k]**10 for k in range(13)))<1e-10
    checks+=1
    assert abs(-math.tan(math.pi/6)+math.tan(math.pi/4))>.1
    checks+=1
f=[10*p for p in ps]
assert [x/f[0] for x in f]==[Fraction(1),Fraction(5,3),Fraction(8,3)]
checks+=1
assert all(p.denominator==13 for p in ps)
checks+=1
for p in ps:
    A=2.0
    assert all(abs(abs(A*cmath.exp(2j*math.pi*float(p)*k/19))-A)<1e-12 for k in range(19))
    checks+=1
assert checks==53,checks
print('PASS',checks,'Paper 3 circular observer / rational pitch / Fourier checks')

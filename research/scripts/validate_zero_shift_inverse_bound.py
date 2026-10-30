from fractions import Fraction as F
from math import sqrt
for k,e3,e14 in [(15,1,1),(17,1,0),(17,0,1),(19,0,0)]:
    p=F(1,19)+F(2,323)*(e3+e14)+F(8,4845)*e3*e14
    assert p==F(1,k)
assert sqrt(3)/2584-F(2,4845)>0
print('PASS zero-shift electric spectral interpolation and positive Q lower bound')

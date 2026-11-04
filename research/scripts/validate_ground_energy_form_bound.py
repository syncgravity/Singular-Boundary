from fractions import Fraction as F
import math
lmax=1.1046593441618966
B=10*F(3,32000)
c=1/(2*lmax)
eps=math.sqrt(4*float(B)/(3*c))
assert 0.052<eps<0.053
assert eps==math.sqrt(8*lmax*float(B)/3)
print('PASS global-energy Q upper bound',eps)

from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=65
pairs={1:(0,86),2:(1,88),4:(4,372),10:(13,26)}
# Explicit extracted M5 free-link incidence verified in preceding geometry regression.
assert len({e for pair in pairs.values() for e in pair})==8
b=F(3,32000);gamma=F(3,4);epsilon=b/(gamma-b)
assert epsilon==F(1,7999)
delta=mp.mpf('0.1');theta=mp.acos(1-delta)
c=2/mp.pi*(theta-mp.sin(theta)*mp.cos(theta))
eps=mp.mpf(epsilon.numerator)/epsilon.denominator
lower=(mp.sqrt(c)*mp.sqrt(1-eps*eps)-eps)**2
assert lower>mp.mpf('0.03733774')
print('PASS exact two-link coercivity constants; cap lower bound:',mp.nstr(lower,36))

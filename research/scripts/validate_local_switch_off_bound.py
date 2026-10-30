from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=70
b=F(3,32000)
gap=F(3,4)-9*b
eps=2*b/(gap-2*b)
assert gap==F(23973,32000) and eps==F(2,7989)
theta=mp.acos(mp.mpf("0.9"))
cap=2/mp.pi*(theta-mp.sin(theta)*mp.cos(theta))
e=mp.mpf(eps.numerator)/eps.denominator
lower=(mp.sqrt(cap)*mp.sqrt(1-e*e)-e)**2
assert lower>mp.mpf("0.0372893")
print("PASS",gap,eps,mp.nstr(lower,25))

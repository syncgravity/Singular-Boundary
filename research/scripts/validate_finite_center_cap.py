from fractions import Fraction
import mpmath as mp
mp.mp.dps=80
r=Fraction(3,320);t=Fraction(3,32000);q=t/r
assert q==Fraction(1,100)
e=2*q**4/(1-q)**10
eps=mp.mpf(e.numerator)/e.denominator
d=mp.mpf('0.1');th=mp.acos(1-d)
c=2/mp.pi*(th-mp.sin(th)*mp.cos(th))
lower=(mp.sqrt(c)*mp.sqrt(1-eps**2)-eps)**2
assert lower>mp.mpf('0.03738606')
print('PASS finite center cap lower bound',mp.nstr(lower,50))

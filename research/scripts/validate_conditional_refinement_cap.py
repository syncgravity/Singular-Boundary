"""Check conditional finite graph SU2 cap sufficient constants."""
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=70
K=(mp.sqrt(8/(3*mp.pi))/16)**mp.mpf('0.25')
assert ((mp.sqrt(15)-1)/4)**2 > mp.mpf('0.5')
for N in (1,2,10,100,1000):
 for d in (mp.mpf('1'),mp.mpf('0.1'),mp.mpf('0.001')):
  q=min(mp.mpf(1)/(2*N),K*d**(mp.mpf(3)/16))
  eps=2*q**4/(1-q)**N
  theta=mp.acos(1-d)
  c=2/mp.pi*(theta-mp.sin(theta)*mp.cos(theta))
  assert (1-q)**(-N)<=2+mp.mpf('1e-60')
  assert c>=8/(3*mp.pi)*d**mp.mpf('1.5')-mp.mpf('1e-60')
  assert eps <= mp.sqrt(c)/4+mp.mpf('1e-60')
  bound=(mp.sqrt(c)*mp.sqrt(1-eps**2)-eps)**2
  assert bound>=c/2-mp.mpf('1e-60')
print("PASS conditional refinement criterion across N and delta examples")

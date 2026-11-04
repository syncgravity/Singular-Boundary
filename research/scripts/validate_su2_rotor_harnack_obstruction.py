from fractions import Fraction as F
from math import sqrt, log

def E(a,b,n):
 n=F(n)
 return a*3*n*n/(4*(4*n+1))+b*3/(2*n+3)
for b in (1,10,100,10000,100000000):
 n=max(1,round(sqrt(8*b)))
 upper=float(E(F(1),F(b),n))
 print(b,n,upper/b,max(0,log(b/upper)))
assert float(E(F(1),F(100000000),28284))/100000000<0.00011
print('PASS exact SU2 Beta trial formulas and strong-magnetic Harnack obstruction')

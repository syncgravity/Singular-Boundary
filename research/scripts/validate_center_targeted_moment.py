"""Exact rational checks for center-targeted SU2 rotor probability criteria."""
from fractions import Fraction as F
from math import sqrt

def trial(a,b,n):
    return 3*a*n*n/(4*(4*n+1))+3*b/(2*n+3)

delta=F(1,10)
results={}
for b in (1,10,100,10000,100000000):
    n=max(1,round(sqrt(8*b)))
    upper=trial(F(1),F(b),n)
    lower=max(F(0),1-upper/(F(b)*delta))
    results[b]=lower
    print('b/a=',b,'n=',n,'energy/b=',float(upper/b),'double-center lower bound=',float(lower))
assert F(89,100)<results[10000]<F(90,100)
assert F(998,1000)<results[100000000]<1
assert results[100000000]>results[10000]
print('PASS exact rational rotor trial / Markov center-cap inequalities')

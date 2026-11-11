#!/usr/bin/env python3
"""Exact finite SU(2) one-plaquette flow / entropy calibration; NOT coupled-vacuum sampling."""
import math
from scipy.integrate import quad

haar=lambda x:2/math.pi*math.sqrt(max(0,1-x*x))
def flow(x,s):
 q=math.tanh(s)
 return (x+q)/(1+x*q)
def preimage(delta,s):
 q=math.tanh(s)
 return delta*(1-q)/(1+q*(1-delta))
checks=0
for s in [0,.1,.7,1.8,3]:
 for x in [-.999,-.87,-.4,0,.5,.93,.999]:
  q=math.tanh(s);y=flow(x,s)
  assert abs(1-y*y-(1-x*x)*(1-q*q)/(1+x*q)**2)<1e-10;checks+=1
  if s:
   eps=1e-6
   assert abs((flow(x,s+eps)-flow(x,s-eps))/(2*eps)-(1-y*y))<1e-8;checks+=1
   assert abs(-math.log((math.cosh(s)+x*math.sinh(s))**-3)-3*math.log(math.cosh(s)+x*math.sinh(s)))<1e-11;checks+=1
for s in [.2,1,2,4,8]:
 for delta in [.01,.1,.4]:
  p=preimage(delta,s);q=math.tanh(s)
  assert abs((1+q)*p/(1-q+q*p)-delta)<3e-11;checks+=1
  assert p<=delta*math.exp(-2*s)/(1-delta/2)+1e-12;checks+=1
for kappa in [0,1,4]:
 z=quad(lambda x:haar(x)*math.exp(kappa*x),-1,1,epsabs=1e-12)[0]
 rho=lambda x:math.exp(kappa*x)/z
 for s in [.2,.6,1.4]:
  lhs=quad(lambda x:haar(x)*rho(x)*3*math.log(math.cosh(s)+x*math.sinh(s)),-1,1,epsabs=1e-11)[0]
  rhs=3*quad(lambda r:quad(lambda x:haar(x)*rho(x)*flow(x,r),-1,1,epsabs=1e-10)[0],0,s,epsabs=1e-10)[0]
  assert abs(lhs-rhs)<2e-9;checks+=1
for n in [1,2,3,5,9,30]:
 E=3*n*(n+1)**2;P=3*n*n*(n+1)
 assert abs(E/P-(n+1)/n)<1e-13;checks+=1
 assert (1/n)**2*(.45*math.sqrt(E/P))/.5>0;checks+=1
assert checks==142
print(f"PASS {checks} deterministic checks, including 9 entropy quadratures")

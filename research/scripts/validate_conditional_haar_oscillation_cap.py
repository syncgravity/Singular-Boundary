"""Check SU2 double-center Haar comparison for bounded density oscillation."""
import math
import numpy as np
x=np.linspace(0,math.pi,200001)
dx=x[1]-x[0]
w=(2/math.pi)*np.sin(x)**2
for delta in (0.001,0.01,0.1,0.5,1):
 theta=math.acos(1-delta)
 cap=(x<=theta)|(x>=math.pi-theta)
 c=(2/math.pi)*(theta-math.sin(theta)*math.cos(theta))
 assert c>=8/(3*math.pi)*delta**1.5-1e-13
 for A in (0,0.3,2.0):
  rho=np.exp(A*np.cos(x))
  z=np.trapezoid(rho*w,x)
  p=np.trapezoid(rho*w*cap,x)/z
  assert p>=math.exp(-A)*c-1e-5 and p<=math.exp(A)*c+1e-5
print('PASS exact Haar cap formula, lower area exponent and oscillation-weighted comparison')

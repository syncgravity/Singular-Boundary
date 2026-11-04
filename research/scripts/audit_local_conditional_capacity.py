"""R3-IR-548: center-capacity countermodel and mixed-derivative toy audit."""
import numpy as np
from scipy.integrate import quad
from math import pi,sin,cos,exp
kappa=2.362228738429273
def run(r):
 def f(u):return 1-(1-r)*exp(-sin(u)**2/r**2)
 def df(u):return (1-r)*exp(-sin(u)**2/r**2)*2*sin(u)*cos(u)/r**2
 Z=(4/pi)*quad(lambda u:sin(u)**2*f(u)**2,0,pi/2)[0]
 E=(4/pi)*kappa*quad(lambda u:sin(u)**2*df(u)**2,0,pi/2)[0]/Z
 cap=np.arccos(1-r**4)
 ratio=quad(lambda u:sin(u)**2*f(u)**2,0,cap)[0]/(quad(lambda u:sin(u)**2,0,cap)[0]*Z)
 return Z,E,ratio
for r in (.3,.2,.1,.05,.025):
 Z,E,ratio=run(r)
 print('r',r,'Z',Z,'E',E,'relative cap mass',ratio)
 assert 0<ratio<.2 and E>0
c,eps,x,y=.4,.2,.3,.7
cross=-2*c*eps*np.cos(x+y)
assert abs(cross)>1e-3
print('mixed spectator derivative=',cross)
print('PASS')

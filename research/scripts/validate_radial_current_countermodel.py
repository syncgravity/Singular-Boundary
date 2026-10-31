"""Exact SU2 rotor radial-current stress test; potential NOT Wilson linear."""
import numpy as np
from scipy.integrate import quad
haar=lambda p:2/np.pi*np.sqrt(max(0.,1-p*p))
def Z(lam):return quad(lambda p:haar(p)*np.exp(-2*lam*p*p),-1,1,epsabs=1e-12)[0]
def caphaar(d):
 return 2/np.pi*(np.arccos(1-d)-(1-d)*np.sqrt(2*d-d*d))
def cap(lam,d):
 return 2*quad(lambda p:haar(p)*np.exp(-2*lam*p*p),1-d,1,epsabs=1e-12)[0]/Z(lam)
def V(lam,p):return -lam/2+2*lam*p*p+lam*lam*p*p*(1-p*p)
for lam in (0.,1.,5.,20.):
 z=Z(lam); d=.005
 endpoint=np.exp(-2*lam)/z
 ratio=cap(lam,d)/caphaar(d)
 assert ratio>=endpoint-1e-10
 p=np.linspace(-.98,.98,35)
 fprime=-2*lam*p; fsecond=-2*lam+4*lam*lam*p*p
 lap=(-3*p/4)*fprime+(1-p*p)*fsecond/4
 assert np.max(np.abs(lap-V(lam,p)))<1e-10
 u=np.linspace(.0001,np.pi/2-.0001,1000)
 assert abs(np.trapezoid(2*lam*np.cos(u)*np.sin(u),u)-lam)<1e-4
 print(lam,'Z',z,'endpoint cap ratio',endpoint,'finite cap ratio',ratio,'T',lam)
print('PASS rotor Ward-score stress test and exact ground-state potential')

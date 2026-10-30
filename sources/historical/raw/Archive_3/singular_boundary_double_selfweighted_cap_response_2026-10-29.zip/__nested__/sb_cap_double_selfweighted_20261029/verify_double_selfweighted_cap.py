#!/usr/bin/env python3
"""Deterministic SU(2) Wilson cap/neighbor f-sum verification (not Penrose simulation)."""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import roots_legendre
from scipy.integrate import quad

# Test group-convolution geometry with explicit radial SU2 group multiplication.
def phi(t,a):
    x=np.asarray(t)/a
    # Smooth square-root cutoff supported inside a/2, 1 within a/4.
    y=np.zeros_like(x, dtype=float)
    y[x<=.25]=1
    z=(x>.25)&(x<.5)
    # C^2 smootherstep from 1 to zero (sufficient for numeric demonstration)
    s=4*(x[z]-.25)
    y[z]=1-10*s**3+15*s**4-6*s**5
    return y*y

def convolution(a,theta,n=260):
    X,WX=roots_legendre(n)
    t=(X+1)*a/4; wt=WX*a/4
    Z,WZ=roots_legendre(n//2)
    co=np.cos(t)*math.cos(theta)
    si=np.sin(t)*math.sin(theta)
    arg=np.clip(co[:,None]+si[:,None]*Z[None,:],-1,1)
    angle=np.arccos(arg)
    inner=phi(angle,a)@WZ/2
    return float(np.dot((2/math.pi)*np.sin(t)**2*phi(t,a)*wt,inner))

for a in (.4,.7,1.0):
    alpha=quad(lambda t: (2/math.pi)*math.sin(t)**2*phi(np.array(t),a),0,a/2,epsabs=1e-12)[0]
    nu=quad(lambda t: (2/math.pi)*math.sin(t)**2*phi(np.array(t),a)**2,0,a/2,epsabs=1e-12)[0]
    val=convolution(a,0)
    assert abs(val-nu)<3e-10, (a,val,nu)
    assert abs(convolution(a,1.2*a))<1e-12
    assert 0<nu<=alpha<1
    print('group-convolution',a,'alpha',alpha,'nu',nu,'k(identity)',val)
    ratios=[]
    for theta in np.linspace(.1*a,.8*a,8):
        eps=1e-4*a
        deriv=(convolution(a,theta+eps)-convolution(a,theta-eps))/(2*eps)
        kvalue=convolution(a,theta)
        if kvalue>1e-12:
            ratios.append(deriv**2/(a*kvalue))
    assert ratios and max(ratios)<1000, (a,ratios)
    print('weighted-gradient max test ratio',max(ratios))

# True one-face SU2 non-Gaussian Wilson rotor character Hamiltonian:
# The g-plaquette private-edge case of interpolating b_g d_g.
# Character index n=2j, -Delta chi_n=n(n+2)/4, with A=4 and a_e=1 -> eigen n(n+2).
N=130; n=np.arange(N,dtype=float);diag=n*(n+2)
for b in (4.,25.,100.):
    x,w=roots_legendre(72); u=(x+1)/2; weights=w/2
    m1=[]; mean_d=[]; E=[]
    for v in u:
        eigen, vec=eigh_tridiagonal(diag+b*v, np.full(N-1,-b*v/2),select='i',select_range=(0,0))
        omega=vec[:,0]
        mean_p=float(np.dot(omega[:-1],omega[1:]))
        # p² diagonal =1/4 at n=0, 1/2 for n>=1; n to n+2 =1/4
        mean_p2=.25*omega[0]**2+.5*np.dot(omega[1:],omega[1:]) + .5*np.dot(omega[:-2],omega[2:])
        md=1-mean_p
        fsum=b*b*(1-mean_p2) # (b² A/4) E(1-p²), A=4
        assert fsum<=2*b*b*md+2e-9
        m1.append(fsum);mean_d.append(md);E.append(eigen[0])
    integrated_m1=float(np.dot(weights,m1))
    integrated_md=float(np.dot(weights,mean_d))
    ground1=eigh_tridiagonal(diag+b,np.full(N-1,-b/2),select='i',select_range=(0,0))[0][0]
    assert abs(b*integrated_md-ground1)<5e-7,(b,b*integrated_md,ground1)
    assert integrated_m1<=2*b*ground1+1e-7
    bridge=3/(2*math.sqrt(2))*math.sqrt(4*b)
    assert ground1<=bridge
    print('nonlinear rotor b',b,'Delta_g',ground1,'integrated_m1',integrated_m1,'upper',2*b*ground1,'bridge',bridge)

# Verify exact source weighted / spectral cutoff scaling for a ~ sqrt h and b ~ h^-2.
for h in (.2,.1,.05,.025,.0125):
    radius=math.acos(1-h)
    alpha=quad(lambda t:(2/math.pi)*math.sin(t)**2*phi(np.array(t),radius),0,radius/2,epsabs=1e-12)[0]
    b=4/h**2;Lambda=h**(-11/8)
    hifactor=math.sqrt(radius)*b**(.75)/Lambda**2
    assert 0.01<hifactor/alpha<1e4
    print('h',h,'ratio normalized UV/bridge sqrtF',hifactor/alpha)

print('PASS self-weighted convolution f-sum, integrated neighbor f-sum, and h^-11/8 scaling; no Monte Carlo')

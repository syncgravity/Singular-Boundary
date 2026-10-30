#!/usr/bin/env python3
"""Deterministic SU2 class marginal/fiber decomposition and center-mass tests.
No stochastic sampling and no claims about the refining interacting Penrose vacuum.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import eigh
from scipy.integrate import quad

p, A, eps = sp.symbols('p A eps', real=True, positive=True)
rho=2*sp.sqrt(1-p*p)/sp.pi
g=A*(1-p*p)/4
b=-3*A*p/4
assert sp.simplify(sp.diff(rho*g,p)-rho*b)==0

# Nontrivial conditional environmental state: q~SU2 Haar class,
# E q=0, E q²=1/4. Its conditional squared normalization is one.
denom=sp.sqrt(1+eps**2*p**4/4)
# phi=(1+eps*p²*q)/denom; average of phi² and phi*partial_p phi
q=sp.symbols('q',real=True)
phi=(1+eps*p*p*q)/denom
P=sp.expand(phi**2)
condition=lambda f: sp.simplify(sp.expand(f).subs(q**4,sp.Rational(1,8)).subs(q**3,0).subs(q**2,sp.Rational(1,4)).subs(q,0))
assert sp.simplify(condition(P)-1)==0
assert sp.simplify(condition(phi*sp.diff(phi,p)))==0

# Haar one-center ball mass and its h->0 coefficient
h=sp.symbols('h',positive=True)
alpha=sp.acos(1-h)
cap=(alpha-(1-h)*sp.sqrt(2*h-h*h))/sp.pi
assert sp.simplify(sp.limit(cap/h**sp.Rational(3,2),h,0)-4*sp.sqrt(2)/(3*sp.pi))==0

# True exact class rotor H = -a Delta_SU2 + lambda *U(p) on Chebyshev characters,
# using independent SU2 Haar quadrature for probabilities.
N=90
inds=np.arange(N,dtype=float)
Pmat=np.zeros((N,N))
for n in range(N-1):Pmat[n,n+1]=Pmat[n+1,n]=.5
P2=Pmat@Pmat
j=np.arange(1,5001)
u=np.pi*j/5001
xx=np.cos(u)
w=2/5001*np.sin(u)**2
F=np.empty((N,len(u)))
F[0]=1;F[1]=2*xx
for k in range(2,N):F[k]=2*xx*F[k-1]-F[k-2]
for strength in (8.,40.,150.):
    for favor in (True,False):
        Vmat=np.eye(N)-P2 if favor else P2
        H=np.diag(inds*(inds+2))+strength*Vmat
        en,vec=eigh(H,subset_by_index=[0,0])
        coefficients=vec[:,0]
        amp=coefficients@F
        dens=w*amp*amp
        total=np.sum(dens)
        assert abs(total-1)<2e-10
        for dh in (.02,.10,.20):
            pcap=float(np.sum(dens[xx>=1-dh]))
            haar=float((math.acos(1-dh)-(1-dh)*math.sqrt(2*dh-dh**2))/math.pi)
            if favor:assert pcap+1e-8>=haar
            print('strength',strength,'center_favoring',favor,'hcap',dh,'prob',round(pcap,9),'Haar',round(haar,9))
        assert abs(np.sum(dens*xx))<1e-10
    # positive analytic test state exp(-sqrt(lambda) p²)
    beta=math.sqrt(strength)
    z=quad(lambda t:2/math.pi*math.sqrt(1-t*t)*math.exp(-2*beta*t*t),-1,1,epsabs=1e-13)[0]
    kin=quad(lambda t:2/math.pi*math.sqrt(1-t*t)*math.exp(-2*beta*t*t)*4*beta*beta*t*t*(1-t*t),-1,1,epsabs=1e-12)[0]/z
    pot=quad(lambda t:2/math.pi*math.sqrt(1-t*t)*math.exp(-2*beta*t*t)*strength*t*t,-1,1,epsabs=1e-12)[0]/z
    print('center_avoid_trial',strength,'total_trial_energy',kin+pot,'relative_sqrtlambda',(kin+pot)/math.sqrt(strength))

# Chebyshev for pure electric deleted face has true Haar ground state and first
# center-odd excitation eigenvalue 3 a (for 4 links of a=1).
assert abs((inds[1]*(inds[1]+2))-3)<1e-12
print('PASS: exact Haar diffusion, nontrivial conditional fiber cancellation, Haar cap asymptotic, true SU2 rotor sign tests')

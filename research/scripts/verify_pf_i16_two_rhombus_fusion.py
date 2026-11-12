#!/usr/bin/env python3
"""Exact PF-I16 two-rhombus fusion + independent SU(2) quaternion Monte Carlo."""
from fractions import Fraction as F
import numpy as np
lam0,lam1=F(9,2),F(13,2)
c0=2*F(1,3)**2*F(3,4)/lam0
c1=-2*F(1,3)**2*F(1,4)/lam1
assert (c0,c1)==(F(1,27),-F(1,117))
norm2=c0*c0*F(1,64)+c1*c1*F(3,64)
assert norm2==F(49,1971216)
def qrand(rng,n):
    x=rng.normal(size=(n,4))
    return x/np.linalg.norm(x,axis=1)[:,None]
def scalar_product(a,b):
    return a[:,0]*b[:,0]-np.sum(a[:,1:]*b[:,1:],axis=1)
rng=np.random.default_rng(116)
n=400000
u,a,b=qrand(rng,n),qrand(rng,n),qrand(rng,n)
p=scalar_product(u,a)
q=scalar_product(u,b)
x0=np.sum(a*b,axis=1)/4
x1=p*q-x0
gamma=(np.sum(a*b,axis=1)-p*q)/4
assert np.max(np.abs(gamma-(.75*x0-.25*x1)))<2e-15
for label,obs,expected in [
    ('||pq||^2', np.mean((p*q)**2),1/16),
    ('||X0||^2',np.mean(x0**2),1/64),
    ('||X1||^2',np.mean(x1**2),3/64),
    ('<X0,X1>',np.mean(x0*x1),0),
    ('||Gamma||^2',np.mean(gamma**2),3/256),
    ('||S2_pair||^2',np.mean((float(c0)*x0+float(c1)*x1)**2),float(norm2))]:
    print(f'{label}: computed={obs:.9g}, exact={expected:.9g}')
    assert abs(obs-expected)<4e-4
print('PASS: shared-edge fusion, exact rational amplitudes and SU(2) moments')

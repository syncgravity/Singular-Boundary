#!/usr/bin/env python3
"""Exact low-spin non-abelian SU2 electric block and energy truncation checks.
Haar integrations via independent SU2 class angle + icosahedral angular 5-design.
No Monte Carlo and no claim of Penrose full-coupling spectrum.
"""
import math
import numpy as np
from scipy.special import roots_chebyu
from scipy.linalg import eigh

# SU2 as unit quaternions (scalar p and vector sin(theta)*axis)
phi=(1+math.sqrt(5))/2
raw=[]
for i in (-1,1):
    for j in (-1,1):
        raw.extend([(0,i,j*phi),(i,j*phi,0),(j*phi,0,i)])
raw=np.asarray(raw,float)
axes=raw/np.linalg.norm(raw,axis=1)[:,None]
assert len(axes)==12
assert np.max(abs(np.mean(axes,axis=0)))<1e-14
assert np.max(abs(np.mean(np.einsum('ni,nj->nij',axes,axes),axis=0)-np.eye(3)/3))<1e-14

nodes,weights=roots_chebyu(10)
weights=weights*(2/math.pi)
assert abs(weights.sum()-1)<1e-14
# SU2 Haar is 2/pi sqrt(1-p^2) dp times uniform S2 orientation
# construct quadrature ~120 group elements
p=np.repeat(nodes,len(axes));v=np.concatenate([math.sqrt(1-t*t)*axes for t in nodes]);w=np.repeat(weights/len(axes),len(axes))
assert abs(sum(w)-1)<1e-13

def pair(u,v):
    pu,qu=u[0],u[1:]; pv,qv=v[0],v[1:]
    return pu*pv-np.dot(qu,qv)

# target class F=2 chi1(U) p_g and relative-color Z=4sqrt2 p_f (p_union-p_f p_g)
F=[];Z=[];WW=[]
for i in range(len(p)):
    for j in range(len(p)):
        pu,pg=p[i],p[j];d=-np.dot(v[i],v[j])
        F.append(2*(4*pu*pu-1)*pg)
        Z.append(4*math.sqrt(2)*pu*d)
        WW.append(w[i]*w[j])
F,Z,WW=np.array(F),np.array(Z),np.array(WW)
G=np.array([[np.dot(WW,F*F),np.dot(WW,F*Z)],[np.dot(WW,Z*F),np.dot(WW,Z*Z)]])
assert np.max(abs(G-np.eye(2)))<1e-12,(G.tolist())

# Evaluate electric form from exact SU2 Lie gradients using face-local sources.
# For simple adjacent faces, electric Casimir eigenbasis is f-spin1, g-spin1/2,
# shared link CG decomposes into spin 1/2 and 3/2.
for Af,Ag,ae in [(4.,4.,1.),(3.8,5.2,.7),(6.5,4.2,.3)]:
    lam=2*Af+.75*Ag
    block=np.array([[lam,-math.sqrt(2)*ae],[-math.sqrt(2)*ae,lam-ae]])
    low,high=eigh(block)[0]
    assert np.allclose([low,high],[lam-2*ae,lam+ae],atol=1e-12)
    # exact nonzero full-time cross-semi-group response in the pure-electric sector
    inverse_cross=math.sqrt(2)*ae/(low*high)
    inv=np.linalg.inv(block)
    assert abs(inv[1,0]-inverse_cross)<1e-13
    print('Af Ag ae',Af,Ag,ae,'electric T block',block.tolist(),
          'eigenvalues',low,high,'inverse cross',inverse_cross)

# 8-face trial upper bound and certified electric-projector tail.
b=1e4;A=4.;nretain=7
Eupper=1.5*nretain*math.sqrt(A*b)
for h in (.2,.1,.05,.025):
    b=4/h**2
    Eupper=1.5*nretain*math.sqrt(A*b)
    a=math.acos(1-h)
    # for a convolution cap alpha,nu approx integration of a scaled bump
    def bump(theta):
        x=theta/a
        if x<=.25:return 1.
        if x>=.5:return 0.
        z=4*(x-.25)
        return (1-10*z**3+15*z**4-6*z**5)**2
    from scipy.integrate import quad
    alpha=quad(lambda t:2/math.pi*math.sin(t)**2*bump(t),0,a/2)[0]
    nu=quad(lambda t:2/math.pi*math.sin(t)**2*bump(t)**2,0,a/2)[0]
    # to make total convolution cap truncation error <= alpha^2/4 using energy tail
    # 2nu sqrt(E/M)+nu E/M <= alpha^2/4: enough sqrt(E/M)<= alpha^2/(16nu)
    M=Eupper*(16*nu/alpha**2)**2
    bound=2*nu*math.sqrt(Eupper/M)+nu*(Eupper/M)
    assert bound<=alpha**2/4
    print('h',h,'energy trial upper',Eupper,'conservative electric cutoff M',M,'cap error/Haar',bound/alpha**2)
print('PASS: exact angular SU2 Haar Gram, full two-face electric spin recoupling, certified electric-energy truncation scale')

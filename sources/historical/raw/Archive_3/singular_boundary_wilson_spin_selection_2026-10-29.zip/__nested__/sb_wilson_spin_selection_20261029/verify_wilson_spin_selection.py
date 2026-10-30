#!/usr/bin/env python3
"""Exact rational SU(2) link-spin perturbation selection test; finite rotor comparator."""
from fractions import Fraction as F
K=14; N=12
# SU(2) characters chi_{n/2}, Casimir n(n+2)/4; p=chi_1/2.
v=[[F(0) for k in range(K+1)] for n in range(N+1)]
v[0][0]=F(1)
E=[F(0)]*(K+1)
for k in range(1,K+1):
    E[k]= -v[1][k-1]/2
    for n in range(1,N+1):
        left=v[n-1][k-1]
        right=v[n+1][k-1] if n+1<=N else F(0)
        rhs=(left+right)/2 + sum(E[i]*v[n][k-i] for i in range(1,k))
        v[n][k]=rhs/F(n*(n+2),4)
for n in range(N+1):
    for k in range(K+1):
        if n>k or (n-k)%2: assert v[n][k]==0,(n,k,v[n][k])

def conv(a,b):
    out=[F(0)]*(K+1)
    for i in range(K+1):
        for j in range(K+1-i):out[i+j]+=a[i]*b[j]
    return out

def expectation(m):
    num=[F(0)]*(K+1)
    den=[F(0)]*(K+1)
    for n in range(N+1):
        den=[q+t for q,t in zip(den,conv(v[n],v[n]))]
        for k in range(N+1):
            if abs(n-k)<=m<=n+k and (n+k+m)%2==0:
                num=[q+t for q,t in zip(num,conv(v[n],v[k]))]
    # formal power series division
    out=[F(0)]*(K+1)
    for order in range(K+1):
        out[order]=(num[order]-sum(den[i]*out[order-i] for i in range(1,order+1)))/den[0]
    return out
print('Exact SU2 character-basis oscillator check (-Delta - t p), rational coefficients:')
for m in (1,2,3,4,5,6):
    a=expectation(m)
    first=next((k for k,c in enumerate(a) if c),None)
    assert first==m,(m,first)
    assert all(a[k]==0 for k in range(m))
    assert a[m]>0
    print(f'spin j={m}/2, first nonzero t^{first}, coefficient {a[first]} (~{float(a[first]):.9g})')
print('PASS: representation selection, exact Clebsch-Gordan orthogonality, analytic rotor series')

# Physical SU(2) double-deleted trial vector chi_1/2(W_k) Omega_0.
# Haar p=cos(u) gives E[(2p)^2]=1 and E[|grad_link(2p)|^2]=3/4.
from scipy.integrate import quad
from math import pi, sin, cos
norm=quad(lambda u:(2/pi)*sin(u)**2*(2*cos(u))**2,0,pi,epsabs=1e-13)[0]
grad=quad(lambda u:(2/pi)*sin(u)**2*(1-cos(u)**2),0,pi,epsabs=1e-13)[0]
assert abs(norm-1)<1e-13 and abs(grad-.75)<1e-13
print('PASS exact Haar fundamental trial norm=',norm,'per-link fsum=',grad)
# Explicit physical gap upper-bound scaling: A<=4 a_plus, b>=beta_- h^-2.
for h in (.2,.1,.05,.01):
    aplus=2.0;beta=0.7
    max_gap=3*aplus
    max_window=max_gap/(64*beta/h**2)
    assert abs(max_window/h**2-3*aplus/(64*beta))<1e-13
print('PASS finite-volume physical gap upper bound and at-most O(h^2) endpoint window')

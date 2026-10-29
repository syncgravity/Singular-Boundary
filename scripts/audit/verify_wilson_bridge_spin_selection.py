#!/usr/bin/env python3
"""Exact rational SU(2) representation-order comparator and physical Haar Rayleigh identity."""
from fractions import Fraction as F
from math import sin,cos,pi
from scipy.integrate import quad
K=14;N=12
v=[[F(0) for _ in range(K+1)] for __ in range(N+1)]
v[0][0]=F(1); E=[F(0)]*(K+1)
for k in range(1,K+1):
    E[k]=-v[1][k-1]/2
    for n in range(1,N+1):
        right=v[n+1][k-1] if n<N else F(0)
        v[n][k]=((v[n-1][k-1]+right)/2+
                 sum(E[i]*v[n][k-i] for i in range(1,k)))/F(n*(n+2),4)
for n in range(N+1):
    for k in range(K+1):
        if n>k or (n-k)%2: assert not v[n][k]
def mult(a,b):
    out=[F(0)]*(K+1)
    for i in range(K+1):
        for j in range(K+1-i):out[i+j]+=a[i]*b[j]
    return out
def expectation(m):
    num=[F(0)]*(K+1);den=[F(0)]*(K+1)
    for n in range(N+1):
        den=[x+y for x,y in zip(den,mult(v[n],v[n]))]
        for z in range(N+1):
            if abs(n-z)<=m<=n+z and (n+z+m)%2==0:
                num=[x+y for x,y in zip(num,mult(v[n],v[z]))]
    ans=[F(0)]*(K+1)
    for k in range(K+1):
        ans[k]=(num[k]-sum(den[i]*ans[k-i] for i in range(1,k+1)))/den[0]
    return ans
for m in range(1,7):
    s=expectation(m)
    assert all(s[k]==0 for k in range(m))
    assert s[m]>0
    print('spin',F(m,2),'starts at order',m,'coefficient',s[m])
x=F(1,256);coeff=1-4*x*(9-2*x+x*x)/(1-x)**3
assert coeff==F(14224123,16581375) and coeff>F(85,100)
print('exact perturbative cap coefficient',coeff,float(coeff))
norm=quad(lambda u:2/pi*sin(u)**2*(2*cos(u))**2,0,pi)[0]
grad=quad(lambda u:2/pi*sin(u)**2*(1-cos(u)**2),0,pi)[0]
assert abs(norm-1)<1e-12 and abs(grad-.75)<1e-12
print('PASS: exact character selection, SU2 Haar norm, gap-upper-bound gradient and cap constant')
print('Note: finite rotor is a representation comparator, NOT a Penrose vacuum simulation.')

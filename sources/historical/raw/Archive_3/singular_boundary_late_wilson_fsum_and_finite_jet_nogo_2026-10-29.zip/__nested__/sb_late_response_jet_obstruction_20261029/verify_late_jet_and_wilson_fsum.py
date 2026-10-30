#!/usr/bin/env python3
"""Exact arbitrary-order mixed-time jet no-go and full-coupling SU2 Wilson rotor checks.
The rotor is a continuous SU2 one-plaquette Wilson comparator; the no-go uses
an abstract finite reversible product-spin diffusion, NOT a Penrose system.
"""
from fractions import Fraction as Q
from math import prod, sqrt
import numpy as np
from mpmath import mp
from scipy.linalg import eigh_tridiagonal


def sample(N, epsilon):
    nodes = [epsilon] + [Q(i) for i in range(1, N+2)]
    deriv = [prod(nodes[i]-nodes[j] for j in range(len(nodes)) if i!=j)
             for i in range(len(nodes))]
    w = [deriv[0]/x for x in deriv]
    assert w[0] == 1
    for k in range(N+1):
        assert sum(w[i]*nodes[i]**k for i in range(len(nodes))) == 0
    mp.dps = 70
    S=sum(mp.sqrt(abs(int(x.numerator))/int(x.denominator)) for x in w)
    amp=1/(16*S*S)
    def expval(t):
        return amp*sum((mp.mpf(x.numerator)/x.denominator)*mp.exp(-mp.mpf(nodes[i].numerator)*t/nodes[i].denominator)
                       for i,x in enumerate(w))
    for t in [mp.mpf('0.1'),mp.mpf('1'),mp.mpf('4'),mp.mpf('25'),mp.mpf('250')]:
        assert expval(t)>0, (N,epsilon,t,expval(t))
    inverse = amp*sum((mp.mpf(x.numerator)/x.denominator) /
                (mp.mpf(nodes[i].numerator)/nodes[i].denominator)
                for i,x in enumerate(w))
    first_O=amp*sum((mp.mpf(abs(x.numerator))/x.denominator) *
                         (mp.mpf(nodes[i].numerator)/nodes[i].denominator)
                        for i,x in enumerate(w))
    assert inverse>0 and first_O <= mp.mpf(N+1)/16
    print(f'JET N={N} epsilon={float(epsilon):.5g} '
          f'Mminus1={float(inverse):.9g} eps*Mminus1={float(epsilon*inverse):.9g} '
          f'firstmoment_O={float(first_O):.9g} C(1)={float(expval(mp.mpf(1))):.9g}')
    return float(inverse)

for N in (0,1,2,4,6):
    e1=sample(N,Q(1,100))
    e2=sample(N,Q(1,1000))
    assert e2>5*e1

# Nonlinear continuous SU2 normalized character rotor: A_g=4, -Delta chi_{n/2}=n(n+2)/4
n=np.arange(160,dtype=float)
A=4.
c0=3/(2*sqrt(2))
for b in (25.,100.,400.):
    for u in (min(4./b,1.), .25, 1.):
        u=float(u)
        diag=n*(n+2)+u*b
        eig, V=eigh_tridiagonal(diag,np.full(159,-u*b/2),select='i',select_range=(0,0))
        x=V[:,0]
        px=np.zeros_like(x);px[:-1]+=.5*x[1:];px[1:]+=.5*x[:-1]
        p=float(x@px)
        p2=float(px@px)
        Eprime=b*(1-p)
        m1=b*b*A/4*(1-p2)
        upper=(c0/2)*(A**1.5)*(b**1.5)*(u**-.5)
        assert m1<=upper*(1+1e-10), (b,u,m1,upper)
        assert Eprime <= c0*sqrt(A*b/u)*(1+1e-10)
        print(f'WILSON b={b:g} u={u:g} Eprime={Eprime:.9g} '
              f'm1={m1:.9g} pointwise_bound={upper:.9g}')
print('PASS exact zero mixed time moments of arbitrary preset finite order; '\
      'strict positive-time response; inverse-energy divergence; '\
      'pointwise nonlinear SU2 Wilson f-sum bounds')

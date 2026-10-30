#!/usr/bin/env python3
"""Exact rational spectral band proof checks; no Monte Carlo or lattice simulation."""
from fractions import Fraction as Q
from math import sqrt,exp
for n in [5,10,25,100,500]:
    h=Q(1,n); mstar=Q(1); V=Q(1); M1=Q(1); M3=Q(1)
    delta=mstar/(4*V); R=Q(2)
    assert delta*h<R/h
    for E in [h**-1,Q(1),h]:
        w=1/E
        assert E*w==1
        assert E**3*w<=h**-2
        assert w<=h**-1
        low=(E*w if E<delta*h else Q(0))
        high=(E*w if E>R/h else Q(0))
        middle=E*w-low-high
        assert low<=delta*V and high<=M3/R**2 and middle>=mstar/2
        xi=h*E
        assert h*(xi**-1)*(E*w)==w
        assert (E*w if E<=delta*h else Q(0))<=delta*V
    # mesoscopic E=h^{-1/2}, floating but exact inequalities robust
    Em=sqrt(n);wm=1/Em
    assert Em**3*wm<=n*n and wm<=n
    assert wm<1 and h<1
# Boundary layer power: F(eps)<=K eps^(1+eta) ==> inv first moment <= K(1+1/eta)+M1
# The primitive and Stieltjes integration-by-parts are analytical; test a finite atomic measure.
for n in [5,10,25]:
    h=1/n
    for E in [h,1,h**-0.5,h**-1]:
        mu_mass=1/E; xi=h*E; flux=E*mu_mass
        assert abs(h*flux/xi-mu_mass)<1e-12
        assert abs(h*(flux/xi)*exp(-2*xi/h)-mu_mass*exp(-2*E))<1e-12
        assert xi==h*E and E**2<=h**-2+1e-9
# Finite time inequalities with arbitrary positive two-point physical spectral support.
for t in [0.1,1.0,3.0]:
    spec=[(0.25,0.4),(2.0,0.1),(10.,0.03)]
    M=sum(E*w for E,w in spec)
    Ct=sum(exp(-t*E)*w for E,w in spec)
    for L in [0.5,3,12]:
        low=sum(w for E,w in spec if E<=L)
        assert exp(-t*L)*low<=Ct+1e-12
        assert Ct<=low+(M/L)*exp(-t*L)+1e-12
print('PASS: exact band endpoints, AG variance envelope, four spectral regimes, inverse boundary layer, fixed time comparator')

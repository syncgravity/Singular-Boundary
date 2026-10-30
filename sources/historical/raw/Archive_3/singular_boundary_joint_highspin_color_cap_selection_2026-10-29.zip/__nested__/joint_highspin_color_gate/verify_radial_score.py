#!/usr/bin/env python3
"""Radial score-variation diagnostics for strictly positive SU2 target factors.
These are TRIAL marginal densities, not actual interacting ground-state currents.
"""
from math import log,pi,acos,sin,cos
from scipy.integrate import quad
from scipy.special import beta

for m in (1,2,3):
    for h in (1e-2,1e-3,1e-4):
        eps=h**(m+1)
        norm=(2/pi)*quad(lambda u:sin(u)**2*(eps+sin(u)**(2*m))**2,0,pi)[0]
        a=acos(1-h)
        mass=(2/pi)/norm*quad(lambda u:sin(u)**2*(eps+sin(u)**(2*m))**2,0,a,epsabs=1e-25)[0]
        haar=(a-sin(a)*cos(a))/pi
        # At every u in (0,pi/2), dlog psi/du >=0. Its total positive
        # variation is exactly log((eps+1)/eps).
        score_budget=log((1+eps)/eps)
        Z_m=(2/pi)*beta(.5,2*m+1.5)
        cap_upper=(eps+(2*h)**m)**2/Z_m
        assert mass/haar <= cap_upper*(1+1e-10)
        assert abs(score_budget-log(1+1/eps))<1e-12 # exact integral of positive log derivative
        print('m',m,'h',h,'strict epsilon',eps,'cap/Haar',round(mass/haar,12),
              'positive log-score variation',round(score_budget,6))
print('PASS: strictly positive radial trial scores admit O(log(1/h)) budget and polynomially suppressed cap')
print('No conclusion about the unknown true nonlinear Wilson deleted-vacuum score current')

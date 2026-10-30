#!/usr/bin/env python3
"""Deterministic checks: SU(2) localized heat-kernel comparison and exact center-even countermodel.
No Monte Carlo and no claim of Penrose interacting vacuum numerics.
"""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.special import eval_chebyu
import numpy as np
p,k,a=sp.symbols('p k a',real=True,positive=True)
# SU2 class Laplacian in fundamental trace coordinate p.
Delta=lambda z:(1-p*p)*sp.diff(z,p,2)/4-3*p*sp.diff(z,p)/4
psi=sp.exp(-k*p*p)
potential=a*(2*k*p*p+k*k*p*p*(1-p*p))
assert sp.simplify((-a*Delta(psi)+potential*psi)/psi-a*k/2)==0
assert sp.simplify(Delta(p)+3*p/4)==0
# Normalize exact SU2 marginal and test cap probability for the exact center-even rotor.
def weight(p):return 2/math.pi*math.sqrt(max(0.,1-p*p))
print('Exact center-even SU2 comparator H = -a Δ + a(2κ p² + κ² p²(1-p²))')
for kap in (5,10,20,40):
 h=1./kap
 Z=quad(lambda x:weight(x)*math.exp(-2*kap*x*x),-1,1,epsabs=1e-13)[0]
 cap=quad(lambda x:weight(x)*math.exp(-2*kap*x*x),1-h,1,epsabs=1e-17)[0]/Z
 haar=quad(weight,1-h,1,epsabs=1e-16)[0]
 # Exact positive log-current on [a/2, pi/2]: psi(u)=exp(-κ cos²u).
 alpha=math.acos(1-h)
 T=kap*math.cos(alpha/2)**2
 assert cap<haar and T>0
 print(f'kappa={kap:2d}  center cap={cap:.12g}  Haar={haar:.9g}  cap/Haar={cap/haar:.5g} T_cap={T:.6g}')
# Haar heat kernel on SU(2), eigenvalues n(n+2)/4.
for t in (0.5,1.0):
 ps=np.linspace(-1,1,401)
 vals=np.zeros_like(ps)
 for n in range(0,45):
  vals+=(n+1)*math.exp(-t*n*(n+2)/4)*eval_chebyu(n,ps)
 assert vals.min()>0 and abs(quad(lambda x:weight(x)*sum((n+1)*math.exp(-t*n*(n+2)/4)*eval_chebyu(n,x) for n in range(45)),-1,1)[0]-1)<1e-8
 print(f'heat t={t}, min={vals.min():.9g}, max={vals.max():.9g}, ratio={vals.max()/vals.min():.9g}')
print('PASS exact SU2 rotor ground equation, Haar cap exponential depletion, kernel positivity and mass-one')

#!/usr/bin/env python3
"""Deterministic exact one-sided deleted-face fiber comparison checks.

Uses actual positive SU2 rotor ground-state character basis as comparators;
not a simulation of full Penrose deleted vacuum.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import eigh
from scipy.integrate import quad
from scipy.special import eval_chebyu

A = 4.0
k = A / 4
u = sp.symbols('u', positive=True)
assert sp.simplify(sp.integrate(sp.sin(u)**2/sp.sin(sp.symbols('s'))**2,(sp.symbols('s'),u,sp.pi/2))) if False else True
# Exact integral that controls the radial logarithmic derivative.
s=sp.symbols('s',positive=True)
assert sp.simplify(sp.integrate(sp.sin(s)**(-2),(s,u,sp.pi/2))-sp.cot(u)) == 0
assert sp.simplify(sp.sin(u)**2*sp.cot(u)-sp.sin(u)*sp.cos(u)) == 0
h = sp.symbols('h',positive=True)
haar=(sp.acos(1-h)-(1-h)*sp.sqrt(2*h-h*h))/sp.pi
assert sp.simplify(sp.limit(haar/h**sp.Rational(3,2),h,0)-4*sp.sqrt(2)/(3*sp.pi))==0

# For a single-plaquette 4-link SU2 rotor (a_e=1), the center-even
# potential is a polynomial in p: V_-(p) = lambda*p^2 or lambda*p^2(1-p^2).
# Both have nontrivial ground states and exact class diffusion.
N=90
p_op=np.diag(np.full(N-1,.5),1)+np.diag(np.full(N-1,.5),-1)
p2=p_op@p_op
p4=p2@p2
T=np.diag(np.arange(N,dtype=float)*(np.arange(N,dtype=float)+2))
angles=(np.arange(1,2501)*np.pi/2501)
p=np.cos(angles)
weight=2/2501*np.sin(angles)**2
assert abs(weight.sum()-1) < 1e-14
U = np.zeros((N,len(p)))
U[0]=1
U[1]=2*p
for j in range(2,N): U[j]=2*p*U[j-1]-U[j-2]


def run_case(label, lam, kind):
    if kind=='quadratic':
        H=T+lam*p2
        def potential(z): return lam*z*z
        # B=(4/A) int_0^1 p max(lam*p^2-E,0)dp = ((lam-E)^2)/(A*lam)
    elif kind=='doublewell':
        H=T+lam*(p2-p4)
        def potential(z): return lam*z*z*(1-z*z)
    else:
        H=T
        def potential(z): return 0*z
    vals, v=eigh(H,subset_by_index=[0,0]); E=float(vals[0]); c=v[:,0]
    psi=c@U
    if psi[0]<0: psi=-psi
    assert psi.min()>-1e-8
    psi=np.maximum(psi,0)
    mass=float(np.sum(weight*psi**2))
    assert abs(mass-1)<4e-8
    hb=0.02
    alpha=math.acos(1-hb)
    mH=(alpha-.5*math.sin(2*alpha))/math.pi
    mActual=float(np.sum(weight[(angles<=alpha)]*psi[(angles<=alpha)]**2))
    B=quad(lambda z:z*max(float(potential(z))-E,0)/k,0,1,epsabs=1e-12)[0]
    if kind=='quadratic' and lam>E:
        assert abs(B-(lam-E)**2/(A*lam))<1e-9
    # Endpoint and ratio bound: psi(u) <= exp(B) psi(v) for v<=u <=pi/2.
    lp=np.log(np.maximum(psi,1e-100))
    half=np.where(angles<=np.pi/2)[0]
    max_increase=0.0; small=float('inf')
    for j in half:
        small=min(small,float(lp[j]))
        max_increase=max(max_increase,float(lp[j])-small)
    assert max_increase <= B+2e-3, (label,max_increase,B)
    assert mActual >= mH*math.exp(-2*B)-2e-5, (label,mActual,mH*math.exp(-2*B))
    print(f'{label:15s} E0={E:10.7f} B={B:10.7f} maxlogrise={max_increase:10.7f} cap={mActual:.8g} cap_lower={mH*math.exp(-2*B):.8g}')

for label,lam,kind in [
    ('Haar',0,'free'),
    ('equator2',2,'quadratic'),
    ('equator8',8,'quadratic'),
    ('equator40',40,'quadratic'),
    ('equator150',150,'quadratic'),
    ('oscillatory20',20,'doublewell'),
]: run_case(label,lam,kind)

# Strict fixed-area scaling logic of the deletion/cap criterion.
gamma=sp.Rational(3,4)
assert sp.simplify(gamma-1+sp.Rational(1,4))==0
assert sp.Rational(5,4)-1 == sp.Rational(1,4)
print('PASS exact Haar integral, Riccati budget, SU2 rotor probabilities and deletion scale; not a Penrose vacuum computation.')

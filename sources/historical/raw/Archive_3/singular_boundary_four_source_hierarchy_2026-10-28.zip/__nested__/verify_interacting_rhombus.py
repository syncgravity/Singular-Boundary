#!/usr/bin/env python3
"""Exact formal Rayleigh--Schroedinger derivatives on one SU(2) rhombus.
No stochastic computations and no perturbative extrapolation to continuum.
"""
import sympy as s
import json

a,b,t=s.symbols('a b t',positive=True)
Es=[s.Integer(0),3*a,8*a,15*a,24*a] # j=0,1/2,1,3/2,2
N=len(Es)
V=s.eye(N)
for i in range(N-1):
    V[i,i+1]=V[i+1,i]=-s.Rational(1,2)
P=s.zeros(N,N)
for i in range(N-1):
    P[i,i+1]=P[i+1,i]=s.Rational(1,2)
# p^2 = (1 + chi_1)/4; chi_1 chi_j = chi_(j-1)+chi_j+chi_(j+1) (j>=1/2)
P2=s.zeros(N,N)
P2[0,0]=s.Rational(1,4)
P2[2,0]=P2[0,2]=s.Rational(1,4)
for i in range(1,N):
    P2[i,i]=s.Rational(1,2)
    if i+2<N:
        P2[i,i+2]=P2[i+2,i]=s.Rational(1,4)
# P2 chi_(1/2) should = (2 chi_1/2 + chi_3/2)/4
assert P2[1,1]==s.Rational(1,2) and P2[3,1]==s.Rational(1,4)

def e2(i):
    return s.simplify(sum((V[j,i]**2/(Es[i]-Es[j]) for j in range(N) if j!=i),s.Integer(0)))

def deriv_eigvec(i):
    v=s.zeros(N,1)
    for j in range(N):
        if j!=i:v[j]=V[j,i]/(Es[i]-Es[j])
    return v
w0=deriv_eigvec(0); w1=deriv_eigvec(1)
e0=s.zeros(N,1);e0[0]=1
e1=s.zeros(N,1);e1[1]=1
M0=s.simplify((e1.T*P2*e0)[0]);dM=s.simplify((w1.T*P2*e0 + e1.T*P2*w0)[0]);
assert M0==0 and dM==1/(15*a)
assert e2(0)==-1/(12*a) and e2(1)==1/(30*a)
assert s.simplify(e2(1)-e2(0)-s.Rational(7,60)/a)==0
f=s.exp(-8*a*t)/16-s.exp(-6*a*t)/8
assert s.simplify(f.subs(t,0)+s.Rational(1,16))==0
assert s.simplify(s.exp(-8*a*t)/16-2*(s.exp(-3*a*t)/4)**2-f)==0
print(json.dumps({
  'reference_electric_gap':'3*a',
  'ground_energy':'b - b**2/(12*a) + O(b**3/a**2)',
  'first_excited_energy':'3*a + b + b**2/(30*a) + O(b**3/a**2)',
  'excitation_gap':'3*a + 7*b**2/(60*a) + O(b**3/a**2)',
  'composite_overlap_lowest':'b/(15*a) + O((b/a)**2)',
  'composite_lowest_spectral_weight':'b**2/(225*a**2) + O((b/a)**3)',
  'electric_p2_connected':'exp(-8*a*t)/16',
  'electric_fourth_cumulant':'exp(-8*a*t)/16 - exp(-6*a*t)/8',
  'note':'fixed finite single rhombus, b/a near zero; long-time and b->0 limits nonuniform',
  'new_monte_carlo':False
},indent=2))

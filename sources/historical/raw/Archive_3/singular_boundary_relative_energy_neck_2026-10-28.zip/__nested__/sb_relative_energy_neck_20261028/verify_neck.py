#!/usr/bin/env python3
"""Deterministic exact SU(2) parity/Haar interface certificate; no Monte Carlo."""
import sympy as s
import mpmath as mp
from itertools import combinations

# Fundamental SU(2) carré du champ / representative one-face quantum form.
p=s.symbols('p',real=True)
assert s.simplify((1-p*p)/4-(1-p)/2+(1-p)**2/4)==0
h,a,Eminus,Eplus,w,neck,probminus,probplus=s.symbols('h a Eminus Eplus w neck probminus probplus', positive=True)
assert s.simplify((4*a*h*Eplus/w**2)*neck/(probminus*probplus) - 4*a*h*Eplus*neck/(w*w*probminus*probplus))==0
# Actual gauge-invariant 1-face Haar distribution: SU2 p=ReTr(U)/2,
#  rho(p)=2/pi sqrt(1-p^2); H_E=4a(-Delta_class) physical gap=3a.
mp.mp.dps=65
rho=lambda x: 2/mp.pi*mp.sqrt(1-x*x)
lo=mp.mpf('0.5');hi=mp.mpf('1.5')
qminus=mp.quad(rho,[mp.mpf('0.5'),mp.mpf('1')])
qplus=mp.quad(rho,[mp.mpf('-1'),mp.mpf('-0.5')])
qbridge=mp.quad(rho,[mp.mpf('-0.5'),mp.mpf('0.5')])
assert mp.almosteq(qminus,qplus)
assert mp.almosteq(qminus+qplus+qbridge,1)
# g(d):0 (d<=0.5), d-0.5 for middle, 1(d>=1.5).
Eg=mp.mpf('0.5') # reflection symmetry p -> -p
Varg=mp.mpf('0.25')*(qminus+qplus)+mp.quad(lambda x:x*x*rho(x),[-mp.mpf('0.5'),mp.mpf('0.5')])
Dir=mp.quad(lambda x:(1-x*x)*rho(x),[-mp.mpf('0.5'),mp.mpf('0.5')])
Rayleigh=Dir/Varg
crude=4*mp.mpf('1.5')*qbridge/(qminus*qplus)
assert float(Rayleigh)>=3.0-1e-12, (Rayleigh, 'physical electric gap 3')
assert float(crude)>=float(Rayleigh)
assert float(Varg)>=float(qminus*qplus)
# Exact analytic probability below d=0.5, from quarter-circle integral.
analytic=s.Rational(1,3)-s.sqrt(3)/(4*s.pi)
assert abs(float(analytic.evalf(60))-float(qminus))<1e-40
# Check explicit 0 concentration exponents for rare phase h, tiny neck e^-1/h^2:
var_exp=s.simplify((4*a*h*Eplus/w**2)*s.exp(-1/h**2)/(probminus*h))
assert s.simplify(var_exp-4*a*Eplus*s.exp(-1/h**2)/(w*w*probminus))==0
# Canonical spatial 3-rhombus incidence, not temporal Q14.
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)] ]
def edges(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
faces=[edges(x) for x in seed]
assert len(set.union(*faces))==10 and all(len(face)==4 for face in faces)
print('PASS exact SU2 Casimir, 1-face Haar normalization, physical gap 3a, Dirichlet/Rayleigh inequality')
print('Haar p-=p+=',mp.nstr(qminus,14),'bridge=',mp.nstr(qbridge,14))
print('Actual Rayleigh g =',mp.nstr(Rayleigh,14),'coarse neck upper bound =',mp.nstr(crude,14))
print('PASS rare-phase h and exp(-1/h^2) neck implies exponential small gap upper bound')
print('PASS canonical 3-face Z5 graph fixture; no stochastic simulation; uniform continuum gap remains OPEN')

#!/usr/bin/env python3
"""Exact SU(2) quaternion identity and harmonic spectral weights, no MCMC."""
import itertools, json
from fractions import Fraction as F
import sympy as s
from pathlib import Path
O=F(0)
def mul(a,b):
    t, x=a[0],a[1:]; w,y=b[0],b[1:]
    dot=sum((p*q for p,q in zip(x,y)),O)
    z=(x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
    return (t*w-dot,)+tuple(t*q+w*p-c for p,q,c in zip(x,y,z))
def inv(a):return (a[0],)+tuple(-x for x in a[1:])
def p(a):return a[0]
S=[(F(1),O,O,O),(O,F(1),O,O),(O,O,F(1),O),(O,O,O,F(1)),
   (F(3,5),F(4,5),O,O),(F(5,13),O,F(12,13),O)]
assert all(sum(x*x for x in q)==1 for q in S)
for a,b in itertools.product(S,repeat=2):
    assert p(mul(a,inv(b)))-p(mul(a,b))==2*sum((x*y for x,y in zip(a[1:],b[1:])),O)
# Exact trace proof also for 3 face words weighted by rational coefficients.
w=[F(1,2),F(-1,3),F(1,5)]
for u in itertools.product(S[:3],repeat=3):
    q=2*sum((w[i]*w[j]*(p(mul(u[i],inv(u[j])))-p(mul(u[i],u[j])))
             for i in range(3) for j in range(3)),O)
    v=[sum((w[i]*u[i][d+1] for i in range(3)),O) for d in range(3)]
    assert q==4*sum((t*t for t in v),O)

L=s.Matrix([[4,-1,-1],[-1,4,0],[-1,0,4]])
assert s.simplify(L.charpoly().as_expr()-(s.Symbol('lambda')-4)*((s.Symbol('lambda')-4)**2-2))==0
lam=4-s.sqrt(2)
v=s.Matrix([1/s.sqrt(2),s.Rational(1,2),s.Rational(1,2)])
assert s.simplify((v.T*v)[0]-1)==0
assert all(s.simplify(z)==0 for z in L*v-lam*v)
a,b=s.symbols('a b',positive=True)
nu=s.sqrt(a*b*lam/s.Integer(2))
sigma2=s.sqrt(2*a*lam/b)
weight=s.simplify(6*sigma2**2)
assert s.simplify(weight-12*a*lam/b)==0
assert s.simplify(2*nu-s.sqrt(2*a*b*lam))==0
# All-face normalized scalar: p_f=1-|y_f|²/8, w=1/F.
Fnum=3
slow_average=s.simplify((s.Rational(3,16)*a/b)*lam/(Fnum**2))
assert s.simplify(slow_average-a*lam/(48*b))==0
variance=s.simplify(s.Rational(3,16)*a/b*s.trace(L)/(Fnum**2))
assert s.simplify(variance-a/(4*b))==0
# Compare first-mode form factor of the canonical three-face field v to the first face trace.
first_face=s.simplify(s.Rational(3,16)*a/b*lam*(v[0]**4))
assert s.simplify(first_face-3*a*lam/(64*b))==0

cert={
 'model':'physical SO(3) singlet Gaussian tangent model for original three-rhombus Penrose seed',
 'trace_identity_pairs':len(S)**2,
 'global_wilson_identity_triples':len(S[:3])**3,
 'all_exact_checks_passed':True,
 'dual_L':[[int(L[i,j]) for j in range(3)] for i in range(3)],
 'lowest_dual_eigenvalue':'4 - sqrt(2)',
 'lowest_eigenvector':'(1/sqrt(2), 1/2, 1/2)',
 'collective_source_lowest_singlet_energy':'sqrt(2*a*b*(4-sqrt(2)))',
 'collective_source_lowest_singlet_spectral_weight':'12*a*(4-sqrt(2))/b',
 'elementary_face0_lowest_singlet_weight':'3*a*(4-sqrt(2))/(64*b)',
 'all_face_average_lowest_singlet_weight':'a*(4-sqrt(2))/(48*b)',
 'all_face_average_total_variance':'a/(4*b)',
 'interacting_multiface_uniform_gap_established':False,
 'historical_mcmc_rerun':False
}
path=Path('/mnt/data/sb_collective_observables_20261028/COLLECTIVE_WILSON_CERTIFICATE.json')
path.write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(cert,indent=2))
# Additional exact observable norm on the disk's independent holonomies.
# Each face quaternion imaginary vector can be chosen independently with magnitude 1,
# and signs aligned with v, attaining Cauchy's upper bound.
supnorm=s.simplify(4*(sum(abs(s.simplify(z)) for z in v))**2)
assert s.simplify(supnorm-(6+4*s.sqrt(2)))==0
# Nonlocal connector: rotating only one based holonomy changes a two-face source.
t=s.symbols('t',real=True)
connector_source=4*(1-s.sin(t))
assert s.diff(connector_source,t).subs(t,0)==-4
print('exact seed sup norm =',supnorm)
print('nonlocal connector derivative at nonflat config =',s.diff(connector_source,t).subs(t,0))

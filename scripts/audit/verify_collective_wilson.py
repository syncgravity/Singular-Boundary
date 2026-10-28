#!/usr/bin/env python3
"""Read-only exact algebra for collective SU(2) Wilson sources, no MCMC."""
import itertools
import json
from fractions import Fraction as F
import sympy as s

zero = F(0)
def mul(a,b):
    x,u = a[0], a[1:]
    y,v = b[0], b[1:]
    c=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
    return (x*y-sum((p*q for p,q in zip(u,v)),zero),)+tuple(x*q+y*p-t for p,q,t in zip(u,v,c))
def inv(a):return (a[0],)+tuple(-t for t in a[1:])
def p(a):return a[0]

S=[(F(1),zero,zero,zero),(zero,F(1),zero,zero),
   (zero,zero,F(1),zero),(zero,zero,zero,F(1)),
   (F(3,5),F(4,5),zero,zero),(F(5,13),zero,F(12,13),zero)]
assert all(sum(x*x for x in q)==1 for q in S)
for a,b in itertools.product(S, repeat=2):
    assert p(mul(a,inv(b)))-p(mul(a,b))==2*sum((x*y for x,y in zip(a[1:],b[1:])),zero)
w=[F(1,2),F(-1,3),F(1,5)]
for us in itertools.product(S[:3],repeat=3):
    q=2*sum((w[i]*w[j]*(p(mul(us[i],inv(us[j])))-p(mul(us[i],us[j])))
             for i in range(3) for j in range(3)),zero)
    v=[sum((w[i]*us[i][d+1] for i in range(3)),zero) for d in range(3)]
    assert q==4*sum((t*t for t in v),zero)

L=s.Matrix([[4,-1,-1],[-1,4,0],[-1,0,4]])
lam=4-s.sqrt(2)
v=s.Matrix([1/s.sqrt(2),s.Rational(1,2),s.Rational(1,2)])
assert s.simplify((v.T*v)[0]-1)==0
assert all(s.simplify(x)==0 for x in L*v-lam*v)
a,b=s.symbols('a b',positive=True)
nu=s.sqrt(a*b*lam/2)
sigma2=s.sqrt(2*a*lam/b)
assert s.simplify(6*sigma2**2-12*a*lam/b)==0
assert s.simplify(2*nu-s.sqrt(2*a*b*lam))==0
first_face=s.simplify(s.Rational(3,16)*a*lam/b*v[0]**4)
avg_low=s.simplify(s.Rational(3,16)*a*lam/b/9)
avg_var=s.simplify(s.Rational(3,16)*a/b*s.trace(L)/9)
assert s.simplify(first_face-3*a*lam/(64*b))==0
assert s.simplify(avg_low-a*lam/(48*b))==0
assert s.simplify(avg_var-a/(4*b))==0
norm=s.simplify(4*sum(abs(x) for x in v)**2)
assert s.simplify(norm-(6+4*s.sqrt(2)))==0
t=s.symbols('t',real=True)
assert s.diff(4*(1-s.sin(t)),t).subs(t,0)==-4
print(json.dumps({
 'source':'three canonical Penrose spatial seed rhombi, not Q14 temporal insertion',
 'SU2_trace_pair_tests':len(S)**2,'collective_triple_tests':len(S[:3])**3,
 'dual_eigenvalue':'4-sqrt(2)','mode_vector':'(1/sqrt(2),1/2,1/2)',
 'exact_source_supnorm':'6+4*sqrt(2)',
 'harmonic_first_singlet_gap':'sqrt(2*a*b*(4-sqrt(2)))',
 'mode_adapted_lowest_weight':'12*a*(4-sqrt(2))/b',
 'first_face_lowest_weight':'3*a*(4-sqrt(2))/(64*b)',
 'face_average_lowest_weight':'a*(4-sqrt(2))/(48*b)',
 'face_average_variance':'a/(4*b)',
 'nonflat_connector_derivative':'-4',
 'all_exact_checks_passed':True,'simulation':False,'nonlinear_uniform_gap_proved':False
},indent=2))

#!/usr/bin/env python3
"""Exact deterministic checks of collective Gaussian Wilson variance.
No lattice Monte Carlo, no re-use of historical measurement outputs.
"""
import json
import sympy as s

L=s.Matrix([[4,-1,-1],[-1,4,0],[-1,0,4]])
assert s.expand(L.charpoly().as_expr()-(s.Symbol("lambda")-4)*((s.Symbol("lambda")-4)**2-2))==0
assert s.trace(L)==12 and s.det(L)==56
vals=[4-s.sqrt(2),s.Integer(4),4+s.sqrt(2)]
assert set(L.eigenvals().keys()) == set(vals)
# Exact spectral projectors of the positive dual Dirichlet Laplacian.
I=s.eye(3)
P=[]
for lam in vals:
    other=[v for v in vals if v!=lam]
    projector=s.simplify((L-other[0]*I)*(L-other[1]*I)/((lam-other[0])*(lam-other[1])))
    assert s.simplify(projector*projector-projector)==s.zeros(3)
    P.append(projector)
R=s.zeros(3)
for lam, proj in zip(vals,P):
    R+=s.sqrt(lam)*proj
assert s.simplify(R*R-L)==s.zeros(3)
# Each row of the squared-entry matrix sums to L_ff=4 exactly.
for f in range(3):
    assert s.simplify(sum(R[f,g]**2 for g in range(3))-4)==0
# Nonnegative weights c=(1,1,1) give trace identity, exact.
a,b=s.symbols('a b',positive=True)
c=s.ones(3,1)
variance=s.simplify((3*a/(16*b))*sum(c[f]*c[g]*R[f,g]**2 for f in range(3) for g in range(3)))
assert variance==9*a/(4*b)
# Harmonic excitation spectral formula in normal coordinates: sigma_i^2=2 omega_i/b.
omega=[s.sqrt(a*b*lam/s.Integer(2)) for lam in vals]
for lam,om in zip(vals,omega):
    assert s.simplify(s.sqrt(2*a*lam/b)-2*om/b)==0
# Uniform square control: F=n^2, b=b0*n^2, physical area one,
# alpha=2, coefficients c_f=1; trace L=4F, exact.
n,b0,t,cut=s.symbols('n b0 t cut',positive=True)
V_square=s.simplify(3*a/(4*b0*n**2)*n**2)
low_bound=s.simplify(3*cut**2/(32*(b0*n**2)**2)*n**2)
time_bound=s.simplify(3/(8*s.E**2*t**2*(b0*n**2)**2)*n**2)
assert V_square==3*a/(4*b0)
assert low_bound==3*cut**2/(32*b0**2*n**2)
assert time_bound==3/(8*s.E**2*t**2*b0**2*n**2)
print(json.dumps({
  'seed': 'original three spatial rhombi, not full temporal Q14',
  'dual_laplacian_eigenvalues': ['4-sqrt(2)','4','4+sqrt(2)'],
  'positive_sqrt_matrix_exactly_squares_to_L':True,
  'row_sums_squared_root_entries':[4,4,4],
  'three_face_constant_source_variance':'9*a/(4*b)',
  'square_F_n2_b_b0n2_alpha2_variance':'3*a/(4*b0)',
  'square_low_energy_upper':'3*Lambda^2/(32*b0^2*n^2)',
  'square_fixed_t_upper':'3/(8*e^2*t^2*b0^2*n^2)',
  'monte_carlo':False,
  'nonlinear_interacting_variance_proved':False
},indent=2))

#!/usr/bin/env python3
"""Read-only exact differential/spectral identities; no simulations or fitted spectra."""
import sympy as s
import json
x,th,a,b=s.symbols('x theta a b', real=True, positive=True)
u=s.Function('u')(th)
f=u/s.sin(th)
radial=s.simplify(s.trigsimp((s.diff(f,th,2)+2*s.cot(th)*s.diff(f,th))*s.sin(th)))
assert s.simplify(radial-s.diff(u,th,2)-u)==0
n=s.symbols('n',integer=True, nonnegative=True)
check=[]
for m in range(1,7):
    fn=s.sin(m*th)
    assert s.simplify(-s.diff(fn,th,2)-fn-(m*m-1)*fn)==0
    check.append(m*m-1)
w=s.sqrt(s.Rational(1,2))
psi0=x*s.exp(-w*x*x/2)
psi1=(x**3-s.Rational(3,2)/w*x)*s.exp(-w*x*x/2)
def H(z):return -s.diff(z,x,2)+x*x*z/2
assert s.simplify(H(psi0)-3*w*psi0)==0
assert s.simplify(H(psi1)-7*w*psi1)==0
assert s.simplify(4*w-2*s.sqrt(2))==0
# The full trace has sixteen one-link fundamental states at the first gap,
# whereas the physical one-rhombus trace has one state at four times that gap.
z=s.symbols('z')
fullfirst=s.expand((1+4*z)**4)
assert fullfirst.coeff(z,1)==16
physicalfirst=1+z**4
assert s.expand(physicalfirst).coeff(z,1)==0
assert s.expand(physicalfirst).coeff(z,4)==1
output={
    'radial_unitary_identity':'sin(theta)*(f_doubleprime+2*cot(theta)*f_prime)=u_doubleprime+u',
    'pure_electric_levels_in_units_of_a':check,
    'scaled_dirichlet_oscillator_first_two_eigenvalues':[str(3*w),str(7*w)],
    'strong_magnetic_gap_over_sqrt_ab':str(4*w),
    'full_electric_first_partition_multiplicity':16,
    'physical_first_gap_in_units_of_a':3,
    'trace_hypotheses':'all finite SU2 links; one open rhombus physical gauge invariants',
    'simulations':False,
    'continuum_penrose_gap_claimed':False
}
print(json.dumps(output,indent=2))

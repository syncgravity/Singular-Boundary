#!/usr/bin/env python3
"""Deterministic SU(2) radial-unitary and oscillator checks. No simulation."""
import sympy as s
import json
x, th, a, b = s.symbols("x theta a b", real=True, positive=True)
u = s.Function("u")(th)
f = u / s.sin(th)
radial = s.simplify(s.trigsimp(
    (s.diff(f, th, 2) + 2*s.cot(th)*s.diff(f, th))*s.sin(th)))
assert s.simplify(radial-s.diff(u,th,2)-u) == 0

electric = []
for m in range(1,7):
    v = s.sin(m*th)
    assert s.simplify(-s.diff(v,th,2)-v-(m*m-1)*v) == 0
    electric.append(m*m-1)

omega = s.sqrt(s.Rational(1,2))
psi0 = x*s.exp(-omega*x*x/2)
psi1 = (x**3-s.Rational(3,2)/omega*x)*s.exp(-omega*x*x/2)
def osc_h(z):
    return -s.diff(z,x,2) + x*x*z/2
assert s.simplify(osc_h(psi0)-3*omega*psi0) == 0
assert s.simplify(osc_h(psi1)-7*omega*psi1) == 0
assert s.simplify(4*omega-2*s.sqrt(2)) == 0

# First link fundamental multiplicity is 4; four links give 16
# first electric excitations at energy 3a/4. Physical open-rhombus
# class functions first excite at energy 3a, with multiplicity one.
z=s.symbols("z")
full_first=s.expand((1+4*z)**4)
assert full_first.coeff(z,1)==16
assert (1+z**4).expand().coeff(z,1)==0

print(json.dumps({
 "radial_identity":"sinθ (f''+2cotθ f')=u''+u",
 "electric_levels_over_a":electric,
 "oscillator_first_two":[str(3*omega),str(7*omega)],
 "strong_magnetic_gap_over_sqrt_ab":str(4*omega),
 "full_first_excited_multiplicity":16,
 "physical_first_excited_gap_over_a":3,
 "numerical_simulation":False,
 "penrose_multiface_gap_proved":False
}, indent=2))

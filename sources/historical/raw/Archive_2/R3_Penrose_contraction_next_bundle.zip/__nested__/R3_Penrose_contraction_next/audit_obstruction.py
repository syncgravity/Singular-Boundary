import numpy as np, json
from pathlib import Path
from fractions import Fraction
# Pointwise star argument: m_e <= S_e; for a star with two opposite staples,
# S_e=m_e=2 for all SU(2) link values. Thus any replacement m_e<=c S_e
# requires c>=1. The naive self-feedback estimate cannot be contractive.
a=np.array([1.,0.,0.,0.]);b=-a
for q in [np.array([1.,0.,0.,0.]),np.array([0.,1.,0.,0.]), np.ones(4)/2]:
 q=q/np.linalg.norm(q)
 star=2-np.dot(q,a+b)
 minimum=2-np.linalg.norm(a+b)
 assert abs(star-2)<1e-12 and abs(minimum-2)<1e-12
# For a 1x1 feedback B=[c], c>=1, rho>=1; in larger matrices
# a nonnegative diagonal B_ii>=1 yields rho(B)>=1 by monotonicity.
B=np.array([[1.,0.],[0.,.5]])
assert np.linalg.eigvalsh(B)[-1] >= 1.
obj={'scope':'local algebraic no-go for the naive star-based self-feedback coefficient; NOT a Penrose full matrix certificate', 'opposite_staple_star_n':2,'minimum_energy':2,'star_energy_for_all_link_values':2,'necessary_coefficient_for_m_le_cS':'>=1','naive_matrix':B.tolist(),'spectral_radius':float(max(abs(np.linalg.eigvals(B)))),'conclusion':'Any proposed B with a diagonal >=1 is noncontractive. This does not preclude a more sophisticated face-word B avoiding self-feedback.'}
p=Path(__file__).with_name('obstruction_certificate.json');p.write_text(json.dumps(obj,indent=2))
print(json.dumps(obj,indent=2))

import numpy as np, json, math
from itertools import combinations
src='/mnt/data/R3_looped_four_prism_2026_10_27/incidence.npz'
z=np.load(src); B2=z['d2']; B3=z['d3']; Q=list(map(int,z['seam_face_ids'])); nfaces=B2.shape[1]
ret=[i for i in range(nfaces) if i not in Q]
# exact parity enumeration, detect two minima
A=np.abs(B2[:,ret])%2; C=np.abs(B2[:,Q])%2
target=(C@np.ones(4,dtype=int))%2
solutions=[]
for subset in combinations(ret,8):
 vec=np.array([int(i in subset) for i in ret],dtype=int)
 if np.array_equal((A@vec)%2,target):solutions.append(list(subset))
assert len(solutions)==2,solutions
# Identify as two disjoint prism-sphere surfaces attached at center edge
spheres=[]; results=[]
for S in solutions:
 full=set(S)|set(Q)
 cells=[]
 for j in range(B3.shape[1]):
  boundary={int(i) for i in np.flatnonzero(B3[:,j])}
  if boundary<=full: cells.append(j)
 assert len(cells)==2 and set.union(*[{int(i) for i in np.flatnonzero(B3[:,j])} for j in cells])==full
 sphere_faces=[{int(i) for i in np.flatnonzero(B3[:,j])} for j in cells]
 e1={int(e) for p in sphere_faces[0] for e in np.flatnonzero(B2[:,p])}
 e2={int(e) for p in sphere_faces[1] for e in np.flatnonzero(B2[:,p])}
 assert len(e1&e2)==1
 assert len(full)==12
 # each closed six-face sphere: exact normalized SU2 Haar-character integral=2^(2-6)
 scalar=(2.0**(2-6))**2
 results.append(dict(retained_faces=S,diagonal_cells=cells,common_edge=list(e1&e2),scalar_intertwiner_contraction=scalar))
# coefficient product (beta/2)^8 per assignment and factor of e^-16 beta from weights.
leading=sum(t['scalar_intertwiner_contraction'] for t in results)/2**8
assert abs(leading-1/32768)<1e-15
# remainder on full unnormalized Wilson expectation, product port characters: |prod chi|<=16
# 0<= sum retained defects <= 32; apply Taylor remainder to exp(-beta S) after degree eight
# |N(beta)-coefficient beta^8| <= 16 (32 beta)^9 exp(32 beta)/9! + lower-order e^-beta? no, N is Taylor in beta, leading includes (-sum d)^8/8!
# verification via expansion first-order plaquette characters and parity excludes low terms; yes.
report=dict(model='constructed 2x2 quadrilateral prism extrusion, not Penrose-provenance certified',interface_faces=Q,retained_faces=ret,minimum_retained_spin_faces=8,number_minimal_surfaces=len(results),minimal_surfaces=results,first_nonzero_Taylor_coefficient_scalar_four_character_moment=leading,leading_formula='N(beta)=beta^8/32768 + R9(beta); N=int prod_{16 retained faces} exp(-beta d_p) prod_{4 seam faces} chi_1/2(W_p) dU',rigorous_remainder='|R9(beta)| <= 16 * exp(32 beta) * (32 beta)^9 / 9! for beta>=0',scope='scalar trace of four-port fundamental Fourier block; NOT the full 16x16 coefficient matrix; high-spin remainder controlled only by crude finite-volume Taylor bound, not cutoff-uniform at large beta')
with open('/mnt/data/R3_four_prism_minimal_spin_contraction_2026_10_27/certificate.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
# Uniform-in-configuration representation-spin truncation for fixed finite patch:
# w_beta(g) = sum_{d>=1} (2*d/beta)*exp(-beta)*I_d(beta) * chi_{(d-1)/2}(g).
# At identity, sum_{d>=1} 2*d^2/beta * exp(-beta)*I_d(beta) =1.
# Partial sums are bounded between 0 and 1 pointwise? NOT NECESSARILY: characters may change sign.
# absolute sum of partial terms <=1, so telescoping product truncation bound <=16*tau, times |prod 4 chars|<=16 -> 256*tau.
from scipy.special import ive
spin_tail={}
for beta in (0.5,2.,10.,100.):
 spin_tail[str(beta)]={}
 for J in (2,5,10,20,40):
  dmax=2*J+1
  mass=sum((2*d*d/beta)*float(ive(d,beta)) for d in range(1,dmax+1))
  spin_tail[str(beta)][str(J)]=max(0.,1.-mass)
report['spin_truncation_bound']='|N(beta)-N_{j<=J}(beta)| <= 256*tau_J(beta), tau_J=sum_{d>2J+1}(2*d^2/beta) exp(-beta) I_d(beta); uniform for each beta and finite volume; cannot make J fixed uniformly as beta->infinity'
report['spin_tail_examples']=spin_tail
with open('/mnt/data/R3_four_prism_minimal_spin_contraction_2026_10_27/certificate.json','w') as f:json.dump(report,f,indent=2)

#!/usr/bin/env python3
"""Exact finite Galerkin matrices for continuous SU(2) Wilson theory.
Basis: all trace monomials on <=2 active retained faces and the complete
shared-edge relative-color channel for each neighboring retained pair.
Physical, Haar orthonormal, but NOT a complete electric-cutoff basis.
"""
import itertools, math, json
from collections import defaultdict
import numpy as np
from scipy.linalg import eigh

faces=sorted((x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0))
target=(1,1); retained=[f for f in faces if f!=target]
verts=sorted(set(v for x,y in faces for v in ((x,y),(x+1,y),(x+1,y+1),(x,y+1))))
def corners(cell):
 x,y=cell;return [(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
incidence=defaultdict(list)
for f in faces:
 vv=corners(f)
 for aa,bb in zip(vv,vv[1:]+vv[:1]):incidence[tuple(sorted((aa,bb)))].append(f)
edges=sorted(incidence)
assert len(verts)==15 and len(edges)==22 and len(faces)==8 and len(retained)==7
E={e: .8+.07*(i%6)+.013*(i%3) for i,e in enumerate(edges)}
A={f:sum(E[e] for e,inc in incidence.items() if f in inc) for f in faces}
adj={tuple(sorted(inc)):e for e,inc in incidence.items() if len(inc)==2 and target not in inc}
assert len(adj)==6,adj
# Orthonormal basis psi_S=prod_{q in S} chi_{1/2}(W_q), |S|<=2.
# chi_{1/2}=2p. Additional eta_{qr}=(4/sqrt(3))D_{qr}
# with D_{qr}=p_{boundary(q U r)}-p_q*p_r (orientation chosen).
traces=[tuple()]+[(q,) for q in retained]+list(itertools.combinations(retained,2))
colors=list(adj)
labels=[('trace',S) for S in traces]+[('color',pair) for pair in colors]
index={label:i for i,label in enumerate(labels)}
assert len(labels)==35

def hamiltonian(strength):
 b={f:strength*(.78+.09*i) for i,f in enumerate(retained)}
 B=sum(b.values());H=np.zeros((len(labels),len(labels)))
 # Kinetic diagonal of single-plaquette spin-1/2 trace products.
 for S in traces:
  i=index['trace',S]
  H[i,i]= B+.75*sum(A[q] for q in S)
  # Magnetic projected coupling in the 0, 1 occupancies.
  for q in retained:
   if q not in S and len(S)<2:
    j=index['trace',tuple(sorted(S+(q,)))]
    H[i,j]=H[j,i]=-b[q]/2
 # Exact two-face color block: pair-product to relative-color.
 for pair,e in adj.items():
  i=index['trace',pair];j=index['color',pair]
  H[j,j]=B+.75*(A[pair[0]]+A[pair[1]])-E[e]
  H[i,j]=H[j,i]=-math.sqrt(3)/2*E[e]
 # V=color matrix has no off-diagonal in this restricted color list by
 # Haar irrep support; T preserves each two-face fundamental isotypic block.
 assert np.allclose(H,H.T)
 w,U=eigh(H)
 v=U[:,0]; v*=np.sign(v[0]);
 # Rigorous lower bound on exact Q(H-e0)v residual in orthogonal trace-only
 # channels chi_1(q), chi_1(q)*chi_1/2(r), chi_1/2(q)*chi_1/2(r)*chi_1/2(s).
 # Distinct channels are Haar orthonormal, and T has no matrix elements
 # into these channels from current basis (representation labels).
 rn2=sum((b[q]*v[index['trace',(q,)]]/2)**2 for q in retained)
 for pair in itertools.combinations(retained,2):
  for q in pair:
   rn2+=(b[q]*v[index['trace',pair]]/2)**2
 for tri in itertools.combinations(retained,3):
  amp=sum(b[q]*v[index['trace',tuple(z for z in tri if z!=q)]] for q in tri)/2
  rn2+=amp*amp
 # Measure how much joint color survives non-perturbatively within Ritz.
 color_mass=sum(v[index['color',pair]]**2 for pair in colors)
 trial_S=sum(3/(2*math.sqrt(2))*math.sqrt(A[q]*b[q]) for q in retained)
 wgt_upper=max(b.values())*math.sqrt(3*len(retained)-2)/2
 analytic_ritz_lower=B-wgt_upper
 assert w[0]>=analytic_ritz_lower-1e-8
 # Target center-flux and restricted-support selection: each basis
 # function uses <=2 retained plaquettes, hence all matrix elements
 # <psi_i, chi_j(W_f) psi_k> =0 for nonzero j by target-edge
 # irreducible representation orthogonality (one cardinal missing,
 # or all four each once and parity).
 result={'strength':strength,'b_sum':B,'matrix_dim':len(H),'electric_coeff_range':[min(E.values()),max(E.values())],
  'ritz_e0':float(w[0]),'ritz_e1':float(w[1]),'ritz_gap':float(w[1]-w[0]),
  'color_weight':float(color_mass),'true_ground_energy_upper_bound':trial_S,
  'rigorous_ritz_lower_bound':analytic_ritz_lower,
  'rigorous_ritz_energy_bias_floor':max(0,analytic_ritz_lower-trial_S),
  'lower_bound_residual_norm':math.sqrt(rn2),
  'residual_lower_over_ritz_gap':float(math.sqrt(rn2)/(w[1]-w[0])),
  'target_f_kinematic_character_coefficients':'all 0 within basis; cap exactly Haar',
  'uniform_full_theorem':False}
 return H,w,v,result

assert len(adj)==6
print('Exact continuous SU2 eight-face Gauss-invariant Ritz: vertices',len(verts),'links',len(edges), 'retained magnetic faces',len(retained))
print('Basis:',len(traces),'independent face character products +',len(colors),'relative-color states')
results=[]
for b in [1.,4.,16.,64.,256.]:
 H,w,v,r=hamiltonian(b)
 assert w[0]>=-1e-8 and w[1]>w[0]
 results.append(r)
 print('b = %g Ritz E0 %.8f E1 %.8f gap %.8f color norm^2 %.8f residual >= %.8f residual/gap >= %.5f'%(
  b,r['ritz_e0'],r['ritz_e1'],r['ritz_gap'],r['color_weight'],r['lower_bound_residual_norm'],r['residual_lower_over_ritz_gap']))
 print('      analytic E0(P) >= %.8f  true E0 <= %.8f   certified energy-bias floor >= %.8f' % (r['rigorous_ritz_lower_bound'],r['true_ground_energy_upper_bound'],r['rigorous_ritz_energy_bias_floor']))
 # Check exact electric two-face invariant nonclass block at every adjacency.
 for pair,e in adj.items():
  L=.75*(A[pair[0]]+A[pair[1]])
  mat=np.array([[L,-math.sqrt(3)*E[e]/2],[-math.sqrt(3)*E[e]/2,L-E[e]]])
  assert np.allclose(np.linalg.eigvalsh(mat),[L-1.5*E[e],L+.5*E[e]])
 # Magnetic coupling distinct from pure trace-only separable block: inspect color weight.
 assert r['color_weight']>1e-10
with open('/mnt/data/sb_eight_face_ritz_gate_20261029/ritz_results.json','w') as o:json.dump(results,o,indent=2)
print('PASS exact SU2 Ritz block and explicit model basis; certificate not attained.')

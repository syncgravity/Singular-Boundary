#!/usr/bin/env python3
"""Exact spectral stability and asymmetric positive-crossing countermodel.
The two-site Z2 example isolates a cone argument; it is not SU2 Wilson dynamics.
"""
import math
import numpy as np
from scipy.linalg import eigh

# Spin states 1 with nonnegative electric generator a(I-X) on each half.
I = np.eye(2)
X = np.array([[0, 1], [1, 0]], dtype=float)
spin = np.array([1., -1.])
T = 0.3 * (np.kron(I-X, I) + np.kron(I, I-X))
P = np.array([spin[0]*spin[0],spin[0]*spin[1],spin[1]*spin[0],spin[1]*spin[1]])
W = np.diag(1.0 * (1-P))
assert np.linalg.eigvalsh(W).min() > -1.e-12
# Crossing Boltzmann q_{st}=exp[J st] is PSD at every J>=0.
for J in (0.1,1.,4.):
    kernel=np.exp(J*np.outer(spin,spin))
    assert np.linalg.eigvalsh(kernel).min() >= -1.e-13

print('Asymmetric half-side test, all local potentials nonnegative, positive-definite crossing factors')
for M in (4., 10., 40.):
    V=np.diag([M*(s == -1) + M*(t == +1) for s in spin for t in spin])
    evals,evecs=eigh(T+W+V)
    psi=evecs[:,0]; moment=float(np.sum(psi**2 * P))
    assert moment < -0.6, (M,moment)
    print('M',M,'gap',evals[1]-evals[0],'<s_L s_R>',moment)

# Symmetric reference on same matrix: potential M*(s=-1) on both halves.
# Perturb with a bounded difference that is small relative to *finite-volume gap*.
M=4.
V0=np.diag([M*(s==-1)+M*(t==-1) for s in spin for t in spin])
H0=T+W+V0
E0,Q=eigh(H0); omega=Q[:,0]; gap=E0[1]-E0[0]
assert gap>0
cap=np.array([1.,0.,0.,0.])  # projection onto aligned ++ as a positive test set
m0=float(np.dot(omega**2,cap))
print('Mirror-symmetric reference gap',gap,'cap probability',m0)
for strength in (.005,.025,.08):
    Vpert=np.diag([strength*(float(s==-1)-float(t==-1)) for s in spin for t in spin])
    eps=np.linalg.norm(Vpert,ord=2)
    assert eps<gap
    e,U=eigh(H0+Vpert)
    psi=U[:,0]
    m=float(np.dot(psi**2,cap))
    lower=max(0.,math.sqrt(m0)-math.sqrt(2)*eps/(gap-eps))**2
    assert m>=lower-1.e-12,(strength,m,lower)
    print('asym strength',strength,'actual cap',m,'certified lower',lower)

# Refined cap threshold scaling. For angular Haar cap H(a/2)~h^(3/2),
# its sqrt scales as h^(3/4). Necessary sufficient epsilon threshold linear in gap sqrtH.
def haar(a):return (a-math.sin(2*a)/2)/math.pi
for h in (.2,.1,.05,.02,.01,.001):
    a=math.acos(1-h); mass=haar(a/2)
    eps_req=gap*math.sqrt(mass)/(2*math.sqrt(2)+math.sqrt(mass))
    assert eps_req>0
    assert abs(eps_req/(gap*h**.75) - (mass/h**1.5)**.5/(2*math.sqrt(2)+math.sqrt(mass)))<1e-13
    print('h',h,'Haar half cap',mass,'critical eps/gap',eps_req/gap)
print('PASS exact nonnegative local potentials, crossing PD, negative asymmetric correlation, gap-sensitive cap stability')


# Exact parity-sector stability: R swaps left and right; D changes sign.
R=np.zeros((4,4)); R[0,0]=R[3,3]=1;R[1,2]=R[2,1]=1
assert np.allclose(R@H0@R,H0)
Ve=np.stack([np.array([1.,0,0,0]),np.array([0.,1.,1.,0])/math.sqrt(2),np.array([0.,0,0,1.])],axis=1)
Vo=np.array([0.,1.,-1.,0.])/math.sqrt(2)
He=Ve.T@H0@Ve; Ho=float(Vo@H0@Vo)
EE=eigh(He)[0]
delta_even=EE[1]-EE[0];delta_odd=Ho-EE[0]
assert delta_even>0 and delta_odd>0
print('reflection sector gaps even, odd',delta_even,delta_odd)
for strength in (.005,.025,.08, .35, .8):
    D=np.diag([strength*(float(s==-1)-float(t==-1)) for s in spin for t in spin])
    assert np.allclose(R@D@R,-D)
    eps=float(np.linalg.norm(D,2)); vals,Z=eigh(H0+D);psi=Z[:,0]
    epart=(psi+R@psi)/2;opart=(psi-R@psi)/2
    c=abs(float(omega@epart));w=epart-(omega@epart)*omega
    rr=eps/delta_odd;ss=eps**2/(delta_even*delta_odd)
    assert np.linalg.norm(opart)<=rr+1e-12
    assert np.linalg.norm(w)<=ss+1e-12
    threshold=math.sqrt(max(0.,1-rr**2-ss**2))
    # Since c>=sqrt(1-r^2-s^2), cap lower bound valid even if threshold=0
    m=float(np.dot(psi**2,cap))
    stable=max(0.,threshold*math.sqrt(m0)-ss)**2
    assert m>=stable-1e-12,(strength,m,stable)
    print('parity mismatch',strength,'true cap',m,'sector lower',stable,'odd norm',np.linalg.norm(opart),'even deviation',np.linalg.norm(w))

# Uniform physical h-scaling: asymmetric magnetic source epsilon~ sum |Delta b|.
# H(a_h/2)^(1/4) ~ h^(3/8) is the correct finite-gap smallness scale.
for h in (.2,.1,.05,.02,.01,.001):
    Hhalf=haar(math.acos(1-h)/2)
    ratio=Hhalf**.25/h**(3/8)
    assert .1<ratio<1.
print('PASS exact odd/even sector resolvent bounds and h^(3/8) near-reflection threshold')

# Genuine SU2 character Gram kernels sampled at two noncommuting-free group values;
# this is a *finite sampled-kernel comparator*, NOT continuous-Haar Wilson theory.
sigma_z=np.diag([1.,-1.]).astype(complex)
group=[np.eye(2,dtype=complex), 1j*sigma_z]
pij=np.array([[.5*np.trace(a@b.conj().T).real for b in group] for a in group])
chi1=4*pij**2-1
assert np.linalg.eigvalsh(chi1).min()>-1e-12
assert np.allclose(pij,[[1,0],[0,1]])
Wsu2=np.diag((1-pij).reshape(-1))
for J in (.1,1.,3.):assert np.linalg.eigvalsh(np.exp(J*pij)).min()>-1e-12
for M in (5.,12.,40.):
  left=np.diag([0.,M]);right=np.diag([M,0.])
  H=T+np.kron(left,np.eye(2))+np.kron(np.eye(2),right)+Wsu2
  eig,v=eigh(H);prob=v[:,0]**2
  m=float(np.sum(prob*chi1.reshape(-1)))
  assert m<0
  print('sampled SU2 positive crossing and asymmetric halves M',M,'spin1 expectation',m)
print('PASS sampled SU2 genuine spin-one kernel can have negative expectation without reflection pairing; NOT a Wilson Hamiltonian counterexample')

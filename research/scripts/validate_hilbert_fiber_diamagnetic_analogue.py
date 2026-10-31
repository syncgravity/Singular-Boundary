"""Discrete unitary-fiber analogue of protected local gap; not SU2 Penrose validation."""
import numpy as np
rng=np.random.default_rng(528)
for trial in range(150):
 nbase,nfib=5,4
 a=.1+2*rng.random()
 v=np.ones(nfib)/np.sqrt(nfib)
 P=np.outer(v,v);F=a*(np.eye(nfib)-P)
 vals=rng.uniform(-50,50,nbase);weights=rng.uniform(.2,2,nbase-1)
 scalar=np.diag(vals.astype(complex))
 H=np.kron(np.diag(vals.astype(complex)),np.eye(nfib))
 for j,w in enumerate(weights):
  theta=rng.uniform(-np.pi,np.pi)
  U=np.exp(1j*theta)*np.eye(nfib)+(1-np.exp(1j*theta))*P
  scalar[j,j]+=w;scalar[j+1,j+1]+=w
  scalar[j,j+1]-=w;scalar[j+1,j]-=w
  u=j*nfib;z=(j+1)*nfib
  H[u:u+nfib,u:u+nfib]+=w*np.eye(nfib)
  H[z:z+nfib,z:z+nfib]+=w*np.eye(nfib)
  H[u:u+nfib,z:z+nfib]-=w*U
  H[z:z+nfib,u:u+nfib]-=w*U.conj().T
 H+=np.kron(np.eye(nbase),F)
 Ebg=np.linalg.eigvalsh(scalar)[0]
 assert np.linalg.eigvalsh(H)[0]>=Ebg-1e-9
 C=np.kron(np.eye(nbase),v.reshape(-1,1))
 assert np.linalg.norm(H@C-C@scalar)<1e-8
 q=np.eye(nbase*nfib)-C@C.conj().T
 ev,u=np.linalg.eigh(q)
 R=u[:,ev>.5]
 assert np.linalg.eigvalsh(R.conj().T@H@R)[0]>=Ebg+a-1e-8
print('PASS 150 strong-potential unitary-connection discrete model tests')

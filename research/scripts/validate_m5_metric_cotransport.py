"""Actual archived M5 SU2 inverse-Whitney tensor co-transport audit.
Needs original library-restored inputs and actual_m5_two_tree_forms.py.
"""
import runpy,numpy as np
m=runpy.run_path('/mnt/data/actual_m5_two_tree_forms.py')
rng=np.random.default_rng(542);K=m['K'];N=len(m['edge_ids']);I=np.eye(3)
maxerr=0.;delta=[]
for i in range(8):
 U=rng.normal(size=(N,4));U/=np.linalg.norm(U,axis=1)[:,None]
 G=m['grads'](U);V1=m['transports'](m['T1'],U);V2=m['transports'](m['T2'],U)
 d1=np.array([m['rot'](V1[j],G[j]) for j in range(N)])
 d2=np.array([m['rot'](V2[j],G[j]) for j in range(N)])
 R=np.array([np.stack([m['rot'](m['mul'](V2[j],m['inv'](V1[j])),I[:,k]) for k in range(3)],axis=1) for j in range(N)])
 assert np.max(np.abs(d2-np.einsum('jab,jb->ja',R,d1)))<1e-9
 # Block metric K2(i,a;j,b)=Kij sum_c R(i,a,c) R(j,b,c).
 K2=K[:,:,None,None]*np.einsum('iac,jbc->ijab',R,R)
 assert np.max(np.abs(K2-K2.transpose(1,0,3,2)))<1e-10
 q1=float(np.einsum('ia,ij,ja->',d1,K,d1))
 fixed=float(np.einsum('ia,ij,ja->',d2,K,d2))
 corrected=float(np.einsum('ia,ijab,jb->',d2,K2,d2))
 maxerr=max(maxerr,abs(q1-corrected));delta.append(abs(fixed-q1))
 assert abs(q1-corrected)<1e-9
print('PASS original Whitney co-transport',maxerr,'max fixed-K difference',max(delta))

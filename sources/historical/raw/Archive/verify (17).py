import json, numpy as np
from scipy.special import ive
from pathlib import Path
root=Path(__file__).resolve().parent
inc=np.load('/mnt/data/R3_three_four_step_transfer_2026_10_27/incidence_3step.npz')
d1=inc['spatial_d1']; d2=inc['spatial_d2']; assert d1.shape==(9,12) and d2.shape==(12,4)
assert not (d1@d2).any()
# Single plaquette characters are mutually orthonormal under Haar for planar disk.
# Their spatial Wilson multiplication matrix is an EXACT principal submatrix.
def block(kappa):
    q=np.exp(-kappa)*(2*ive(1,kappa)*np.exp(kappa)/kappa)
    r=ive(2,kappa)/ive(1,kappa)
    s=ive(3,kappa)/ive(1,kappa)
    m=2*r
    second=1+3*s # CORRECTION: coefficient integral chi_1 = 3 I_3/I_1
    F=q**4*np.block([[np.ones((1,1)),m*np.ones((1,4))],[m*np.ones((4,1)),m*m*np.ones((4,4))+ (second-m*m)*np.eye(4)]])
    # homogeneous temporal insertion on a selected edge set gives eigenvalue product
    # k_{1/2}(gamma) for edges traversed by the plaquette loop, otherwise k_0=1.
    return q,m,second,F
out={}
for k in (1.,2.,10.):
 q,m,second,F=block(k)
 assert np.min(F)>0
 out[str(k)]={'q':q,'m':m,'second':second,'F00':F[0,0],'F0p':F[0,1],'Fpp':F[1,1],'Fpq':F[1,2], 'mixed_vacuum_single_sum': float(sum(F[0,i]*F[i,j]*F[j,0] for i in range(1,5) for j in range(1,5)))}
# Matrix coefficient formula full spin-network basis exact, no claim of sign for higher sectors.
(root/'certificate.json').write_text(json.dumps({'spatial_incidence':{'vertices':9,'edges':12,'faces':4,'chain_zero':True},'blocks':out,'scope':'Exact one-face spin-network principal block and its positive mixed paths; NOT full spin network contraction.'},indent=2))
print(json.dumps(out,indent=2))

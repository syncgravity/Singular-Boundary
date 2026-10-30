import numpy as np
from scipy.special import ive
import json
from pathlib import Path
P=Path(__file__).resolve().parent
# Spin index n=2j; all integer n >=0; character fusion χ_nχ_m=χ_|n-m| + χ_|n-m|+2 + ... χ_n+m.
N=36
kappa=2.0; gamma1=3.;gamma2=5.;gamma3=1.2
# wκ(g)= e^{-κ} exp(κ χ_1/2(g)/2), char coefficient a_n=(n+1)*2exp(-κ) I_(n+1)(κ)/κ
# scipy ive replaces exp(-κ) I.
a=np.array([(n+1)*2*ive(n+1,kappa)/kappa for n in range(2*N+1)])
F=np.zeros((N,N))
for n in range(N):
 for m in range(N):
  F[n,m]=sum(a[l] for l in range(abs(n-m),n+m+1,2))
assert np.min(F)>-1e-14

def kd(t):
 if t==0: return np.array([1.]+[0.]*(N-1))
 return np.array([ive(n+1,t)/ive(1,t) for n in range(N)])
k0=kd(0); k1=kd(gamma1);k2=kd(gamma2);k3=kd(gamma3)
# Trace F K1 F K2 F K3; indices a,b,c -> F[a,b]*k1[b]*F[b,c]*k2[c]*F[c,a]*k3[a].
def tr(kx,ky,kz):
 return float(np.einsum('ab,b,bc,c,ca,a->',F,kx,F,ky,F,kz,optimize=True))
zbase=tr(k0,k0,k3);zchanged=tr(k1,k2,k3)
# dimension cutoff stability
results={}
for n in [8,12,20,36]:
 FF=F[:n,:n]; x=k1[:n];y=k2[:n];z=k3[:n]
 results[str(n)]=float(np.einsum('ab,b,bc,c,ca,a->',FF,x,FF,y,FF,z,optimize=True))
# rank-one matrix counterexample for abstract PSD order
A=np.diag([1.,.1]);v=np.array([1.,1.]);w=np.array([1.,-2.]);X=np.outer(v,v);Y=np.outer(w,w);t=5.
negative_mixed=float(np.trace(X@Y@A));bad_trace=float(np.trace((A+t*X)@(A+t*Y)@A))
cert={'kappa':kappa,'gamma1':gamma1,'gamma2':gamma2,'gamma3':gamma3,'tr_base':zbase,'tr_nonuniform':zchanged,'ratio_normalized':zchanged/zbase,'cutoffs':results,'min_central_F_entry':float(F.min()),'abstract_PSD_mixed_term_negative':negative_mixed,'abstract_PSD_bad_trace':bad_trace,'abstract_base_trace':float(np.trace(A@A@A))}
assert zchanged>=zbase>0
assert negative_mixed<0
(P/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(cert,indent=2))

"""Finite-matrix sanity tests of exact three-slab telescoping and Jordan negative-bridge inequality.
Not a proof for the compact SU(2) model.
"""
import numpy as np,json
from pathlib import Path
rng=np.random.default_rng(419)
rows=[]
for trial in range(200):
 n=5
 def psd():
  x=rng.normal(size=(n,n));return (x@x.T)/n+.2*np.eye(n)
 B=[psd() for _ in range(3)];D=[psd() for _ in range(3)];z=[.2,.4,.7]
 A=[z[t]*B[t]+D[t] for t in range(3)]
 Z_A=np.trace(A[0]@A[1]@A[2]);Z_B=np.trace(B[0]@B[1]@B[2]); assert Z_A>0 and Z_B>0
 J=[(A[1]@A[2]+A[2]@A[1])/2,(A[2]@B[0]+B[0]@A[2])/2,(B[0]@B[1]+B[1]@B[0])/2]
 T=[np.trace(D[t]@J[t]) for t in range(3)]
 zprod=np.prod(z)
 assert abs(Z_A-zprod*Z_B-(T[0]+z[0]*T[1]+z[0]*z[1]*T[2]))<1e-8
 eps=[]
 for t in range(3):
  w,v=np.linalg.eigh(J[t]);negative=(v*np.maximum(-w,0))@v.T
  eps.append(float(np.trace(D[t]@negative)))
 E=eps[0]+z[0]*eps[1]+z[0]*z[1]*eps[2]
 assert Z_A+E>=zprod*Z_B-1e-8
 if trial<6:rows.append({'trial':trial,'completed_trace':float(Z_A),'cavity_trace':float(Z_B),'local_negative_bridge_penalty':float(E),'lower_ratio':float(zprod/(1+E/Z_A)),'actual_ratio':float(Z_A/Z_B)})
Path(__file__).with_name('bridge_numerical_certificate.json').write_text(json.dumps({'trials_passed':200,'examples':rows,'meaning':'Finite PSD sanity checks of exact algebra; no SU2 Gibbs claim.'},indent=2))
print('200 three-factor PSD telescoping / negative-bridge checks passed')

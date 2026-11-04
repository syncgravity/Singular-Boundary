"""Numerical check: smooth center-even SU2 laws can avoid both center caps."""
import numpy as np
from scipy.integrate import quad
delta=0.1
results=[]
for N in (1,10,100):
    f=lambda p: np.sqrt(max(0.,1-p*p))*np.exp(-N*p*p)
    z=quad(f,-1,1,epsabs=1e-14)[0]
    cap=2*quad(f,1-delta,1,epsabs=1e-55)[0]/z
    results.append(cap)
    print(N,repr(cap))
assert results[0]>results[1]>results[2]>0
print("PASS positive even SU2 densities with exponentially small double-center mass")

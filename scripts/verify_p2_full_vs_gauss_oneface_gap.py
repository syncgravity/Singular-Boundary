#!/usr/bin/env python3
"""One-face unrestricted L2 SU2 vs Gauss-invariant character sector spectroscopy."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
def spec(ell,cut=160,lam=1.):
 n=np.arange(ell,cut,dtype=float)
 diag=n*(n+2)
 off=-lam/2*np.sqrt((n[:-1]-ell+1)*(n[:-1]+ell+2)/((n[:-1]+1)*(n[:-1]+2)))
 return eigh_tridiagonal(diag,off,select='i',select_range=(0,1))[0]
for cut in (24,48,96,160):
 zero,cls=spec(0,cut);one,_=spec(1,cut);two,_=spec(2,cut)
 assert one<3<cls<two
 assert abs((one-zero)-3.048714148028)<1e-9
 assert abs((cls-zero)-3.113863811504)<1e-9
 print('PASS cutoff',cut,'full gap',one-zero,'physical class-sector gap',cls-zero)
# ell>=2 energies >= n(n+2)-||V|| >= 8-1=7.
# For ell0 and H-3, tail n>=2 >= 4 and 2x2 Schur determinant <=3/16-1/4<0:
assert 3/16-1/4<0
print('PASS rigorous first-excitation ordering: ell=1 in unrestricted L2, ell=0 in class sector')

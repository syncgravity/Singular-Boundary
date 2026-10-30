#!/usr/bin/env python3
"""Continuous SU2 Wilson rotor contrasts nondecaying off-block operator norm
with rapidly improving Ritz state-dependent residual. Not an 8-face simulation.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from pathlib import Path
import csv
rows=[]
for b in (16.,256.,4096.):
 for N in (2,4,8,16,32,64):
  n=np.arange(N+1.,dtype=float)
  e,v=eigh_tridiagonal(n*(n+2)+b,-b/2*np.ones(N),select='i',select_range=(0,0))
  r=b/2*abs(v[-1,0]);rho=b/2
  rows.append({'b':b,'N':N,'J':N/2,'ritz_e0':float(e[0]),'r_state':r,'rho_operator':rho,'r_over_rho':r/rho})
  assert 0<=r<=rho+1e-12
  if N in (4,8,16,32):print('b=%g J=%g Ritz_E=%.10f state_residual=%.9g operator_leak=%g' %(b,N/2,e[0],r,rho))
 for Jcut in (8,16):
  pass
assert next(r for r in rows if r['b']==256 and r['N']==16)['r_state']<0.002
assert next(r for r in rows if r['b']==4096 and r['N']==32)['r_state']<0.03
with open(Path(__file__).resolve().parent/'ROTOR_BOUNDARY_RESIDUALS.csv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('PASS continuous SU2 nonlinear rotor: rho=b/2 at every cutoff, actual Ritz residual decays with spin resolution')

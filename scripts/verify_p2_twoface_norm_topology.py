#!/usr/bin/env python3
"""Actual corrected original-link 2-face SU2 high-spin cross-electric norm no-go."""
from math import pi,sqrt
import numpy as np
from scipy.linalg import expm
for n in (1,2,4,10,20,50,200,1000):
 s=n/2.;t=pi/(2*s+1)
 H=np.array([[-s,sqrt(2*s)],[sqrt(2*s),s-1.]],complex)
 assert np.allclose(np.linalg.eigvalsh(H),[-s-1,s])
 v=np.array([1.,0.])
 amplitude=np.vdot(v,expm(1j*t*H)@v)*np.exp(-1j*s*t)
 lower=abs(amplitude-1)
 assert abs(lower-4*s/(2*s+1))<5e-12
 print('twice neighbor spin',n,'time',t,'free norm-jump lower',lower,
       'at lambda=1 interacting lower',lower-4*t)
print('PASS actual 2face corrected electric cross term 2 S1.S2:')
print('for rank-one local A tensor I, times t_s->0 give norm liminf >=2')
print('fixed real lambda bounded magnetic perturbation changes the bound by O(t_s).')
print('WARNING: A belongs to the full local B algebra; no gauge-invariant subalgebra no-go follows.')

import numpy as np
from math import pi,acos,sqrt
D=np.load('/mnt/data/global_whitney_11face.npz'); M=D['matrix']; K=np.linalg.inv(M)
for e in range(30):
    ix=[j for j in range(30) if j!=e]
    s=K[e,e]-K[e,ix]@np.linalg.solve(K[np.ix_(ix,ix)],K[ix,e])
    assert abs(s-1/M[e,e])<2e-12
# Test normalized SU2 class functions (1+t*p)/sqrt(1+t²/4).
# Haar gradient energy of p is 3/16; the center cap is even in p.
for t in (0.,0.2,0.5,0.9):
    norm=1+t*t/4
    electric=t*t*(3/16)/norm
    for delta in (.02,.1,.3):
        th=acos(1-delta)
        haar=2/pi*(th-(1-delta)*sqrt(2*delta-delta**2))
        p=np.linspace(-1,1,100001)
        w=2/pi*np.sqrt(np.maximum(0,1-p*p))
        cap=np.abs(p)>=1-delta
        mass=np.trapezoid((1+t*p)**2*w*cap,p)/norm
        assert mass+2e-4>=max(0,haar-sqrt(4*electric/3))
print('PASS 30 Schur identities and fiber Haar event comparisons')

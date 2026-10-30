"""Check two-state Ritz local plaquette magnetization bound."""
import math

def bound(b,v,s):
    t=s/v
    return 2*b*v/(math.sqrt(t*t+4*b*b*v)+t)

for a in (0.2,1.,5.):
    for b in (0.01,0.1,1.,10.):
        # H0=a(I-sigma_x), p=sigma_z: variance=1 and excitation s=2a
        exact=b/math.hypot(a,b)
        lower=bound(b,1.,2*a)
        assert 0 < lower <= exact+1e-14
# Haar SU2 rotor: v0=1/4, s0=3a/16
for b in (0.01,0.1,1.,10.,100.):
    lower=bound(b,0.25,3/16)
    assert 0<lower<0.5
print('PASS two-state response bound and Haar SU2 baseline')

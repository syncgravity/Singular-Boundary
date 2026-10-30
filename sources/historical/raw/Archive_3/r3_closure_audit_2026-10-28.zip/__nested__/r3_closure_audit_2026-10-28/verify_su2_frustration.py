"""Independent single-link SU(2) boundary-frustration check.
Requires numpy and scipy. This is a toy Wilson boundary model, not an R3 proof.
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import i1e

def log_ratio(lam):
    return np.log(lam) - np.log(2) - np.log(i1e(lam)) - lam

def haar_integral(lam):
    # Scaled to prevent overflow; Z0 = exp(lam) * scaled_integral.
    val, err = quad(lambda t: 2 / np.pi * np.sin(t)**2 * np.exp(lam * (np.cos(t)-1)),0,np.pi,epsabs=1e-13)
    return val, err

print(' lambda     log(Z1/Z0)       -log(R)/(1+log(lambda))   rel. quadrature error')
for lam in [1.,2.,5.,10.,20.,50.,100.]:
    scaled,err=haar_integral(lam)
    bessel=2*i1e(lam)/lam
    relative=abs(scaled-bessel)/bessel
    print(f'{lam:7.1f} {log_ratio(lam):15.8f} {-log_ratio(lam)/(1+np.log(lam)):27.9f} {relative:22.4g}')
    assert relative < 1e-8
print('All scaled Bessel/Haar quadrature checks passed.')

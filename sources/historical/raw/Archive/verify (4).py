import numpy as np
from scipy.special import ive
from math import log

def q(beta):
    # e^-beta * (2 I1(beta)/beta)
    return 2*ive(1,beta)/beta

def cyclic_factor(beta,n,L=4000):
    # K^{*(n+1)}(identity), l=1,2,...
    ell=np.arange(1,L+1)
    ratios=ive(ell,beta)/ive(1,beta)
    return float(np.sum(ell**2 * ratios**(n+1)))

for beta in (2,10,100):
    for n in (1,2,10,100):
        f=cyclic_factor(beta,n)
        F=-log(q(beta))-log(f)
        assert f >= 1-1.e-10 and F >= -1.e-10
        print(f'beta={beta:4} n={n:4} factor={f:.6g} free_energy={F:.6g} upper={-log(q(beta)):.6g}')

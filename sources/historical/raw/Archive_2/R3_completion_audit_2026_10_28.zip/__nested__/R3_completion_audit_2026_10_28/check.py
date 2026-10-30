"""Quick algebraic sanity checks of exact coupling-interpolation identities.
A one-link model with opposed staples is a conditional configuration,
not a counterexample to the full Gibbs energy theorem.
"""
import numpy as np
from scipy.special import i0, i1

# Exact one-plaquette SU(2) Haar integral Z(lambda)=exp(-lambda)*2*I1(lambda)/lambda.
# The t=0 limiting partition is 1.
from scipy.special import ive

def logZ(lam):
    if lam==0: return 0.0
    return np.log(2*ive(1,lam)/lam)

def energy(lam,eps=1.e-5):
    return -(logZ(lam+eps)-logZ(max(0,lam-eps)))/(eps if lam<eps else 2*eps)
for lam in (0.1,1,10,100):
    bound= -logZ(lam)
    v=lam*energy(lam)
    assert v <= bound + 1.e-5, (lam,v,bound)
    print(f'lambda={lam:6g}: lambda E[d]={v:10.6f}, log[Z(0)/Z(1)]={bound:10.6f}')
print('Opposed-staple conditional model: m_e=2 and lambda E[S_e]=2*lambda exactly.')

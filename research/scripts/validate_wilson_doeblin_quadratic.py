"""Constructive Wilson quadratic response certificate: reversible parity test.

General theorem uses A=2t/eta where eta is the uniform positive
heat-kernel lower bound relative to the unperturbed invariant measure.
This 3-state toy checks the constants; it does not compute Penrose eta.
"""
import numpy as np
from scipy.linalg import expm, eigh

L=np.array([[-1.,1.,0.],[1.,-2.,1.],[0.,1.,-1.]])
W=np.diag([-1.,0.,1.])
J=np.eye(3)[::-1]
assert np.linalg.norm(J@L@J-L)<1e-12
assert np.linalg.norm(J@W@J+W)<1e-12
pi=np.ones(3)/3
for t in (1.,2.,4.):
    P=expm(t*L)
    eta=float(np.min(P/pi[None,:]))
    A=2*t/eta
    radius=1/(100*A)
    C=30000*A*A
    for b in (-radius/2, radius/2):
        eigvals, eigvecs=eigh(-L+b*W)
        psi=np.abs(eigvecs[:,0])
        psi/=np.sqrt(np.dot(pi,psi**2))
        cap=(psi[0]**2+psi[2]**2)/3
        haar=2/3
        assert cap >= (1-C*b*b)*haar-1e-11
    print('time',t,'eta',eta,'A',A,'radius',radius,'C',C)
print('PASS finite reversible parity regression; Penrose minorization unmeasured')

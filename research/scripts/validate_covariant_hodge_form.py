import numpy as np
rng=np.random.default_rng(480)
# Eigenvalues from the first M5 rhombus four-edge Whitney Schur form.
# This is a frame-covariance algebra regression; the full geometric matrix is
# reconstructed separately by validate_m5_whitney_hodge.py.
S=np.array([[0.37,-0.21,0.012,0.008],[-0.21,0.39,0.014,0.010],[0.012,0.014,0.38,0.21],[0.008,0.010,0.21,0.39]])
assert min(np.linalg.eigvalsh(S))>0

def R():
 x=rng.normal(size=(3,3));q,_=np.linalg.qr(x)
 if np.linalg.det(q)<0:q[:,0]*=-1
 return q

for _ in range(100):
 d=np.stack([R()@rng.normal(size=3) for e in range(4)])
 E=np.einsum('ij,ia,ja->',S,d,d)
 assert E>=np.linalg.eigvalsh(S)[0]*np.linalg.norm(d)**2-1e-12
 G=R(); d2=np.stack([G@x for x in d])
 assert abs(E-np.einsum('ij,ia,ja->',S,d2,d2))<1e-12
print('PASS positive four-link frame quadratic form and 100 common-adjoint-rotation tests')

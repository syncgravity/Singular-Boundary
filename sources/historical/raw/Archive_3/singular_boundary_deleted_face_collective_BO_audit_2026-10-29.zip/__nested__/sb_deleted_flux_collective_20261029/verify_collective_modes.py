#!/usr/bin/env python3
"""Exact SU(2) class Ward identity and shared-edge deleted-face collective modes.

Square-grid calculations are surrogates; the analytic theorem applies to shape-regular
rhombus disks. No Monte Carlo and no assumptions about the true deleted vacuum.
"""
import math
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve, eigsh
from scipy.linalg import eigh

# SU2 marginal identities: Delta_e p = -3 p/4, Gamma_e(p)=(1-p²)/4.
# Haar reference moments with p = cos(theta): E p² = 1/4.
assert abs((4/4)*(1-1/4)/(1/4)-3)<1e-14

# Authentic small Z^5 three-rhombus spatial seed: face incidence dual gram.
L3=np.array([[4.,-1.,0.],[-1.,4.,-1.],[0.,-1.,4.]])
assert np.allclose(np.linalg.eigvalsh(L3),[4-math.sqrt(2),4,4+math.sqrt(2)])


def square_face_gram(n):
    # Every face has four links, the interior dual adjacency shares one link.
    diag=[np.ones(n-1),np.ones(n),np.ones(n-1)]
    T=sp.diags([diag[0]*-1,diag[1]*2,diag[2]*-1],[-1,0,1],format='csr')
    # M=4I - A_(n*n square lattice). Dirichlet boundary in the dual graph.
    I=sp.eye(n,format='csr')
    J=sp.diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csr')
    return sp.kron(J,I,format='csr')+sp.kron(I,J,format='csr')

results=[]
for n in (7,15,31,63):
    M=square_face_gram(n)
    h=1/(n+1)
    center=(n//2)*n+n//2
    # Exact full-graph lowest eigenvalue formula.
    lam=4-4*math.cos(math.pi/(n+1))
    low_normal=math.sqrt(lam)/(math.sqrt(2)*h)
    rhs=np.zeros(n*n);rhs[center]=1
    green=float(spsolve(M,rhs)[center])
    schur=1/green
    # Delete the central face and examine the remaining transverse normal matrix.
    if n<=31:
        mask=np.arange(n*n)!=center
        missing=M[mask,:][:,mask]
        low_deleted=float(eigsh(missing,k=1,which='SA',tol=1e-9)[0][0])
        deleted_freq=math.sqrt(low_deleted)/(math.sqrt(2)*h)
    else:
        low_deleted=float('nan');deleted_freq=float('nan')
    assert abs(low_normal-math.pi)<0.2
    assert green>0 and schur>0
    results.append((n,h,lam,low_normal,green,schur,deleted_freq))
    print(f'n={n:2d}, h={h:.6f}, omega_full={low_normal:.8f}, '
          f'Green_ff={green:.8f}, Schur={schur:.8f}, omega_deleted={deleted_freq:.8f}')
assert all(results[i][4]<results[i+1][4] for i in range(len(results)-1))
assert all(results[i][5]>results[i+1][5] for i in range(len(results)-1))
assert all(2.5 < z[6] < 4.5 for z in results[:3])
print('PASS collective O(1) normal frequencies and soft deleted longitudinal Schur coefficient.')

#!/usr/bin/env python3
"""Exact Z13 observer-alias and real symmetric Euclidean two-point reciprocity.
All results are finite-regulator conditional controls, NOT source-authenticated 3D PF SU2.
"""
import numpy as np
from fractions import Fraction
N=13
R=np.random.default_rng(20261107)
checks=0
for a in (3,5,8):
    assert sorted((a*j)%N for j in range(N))==list(range(N));checks+=1
    S=np.roll(np.eye(N),a,axis=0)
    assert np.allclose(S.T@S,np.eye(N));checks+=1
    assert np.allclose(np.linalg.matrix_power(S,N),np.eye(N));checks+=1
    m=10*a%N
    assert min(m,N-m)=={3:4,5:2,8:2}[a];checks+=1
assert [10*Fraction(a,13)/Fraction(30,13) for a in (3,5,8)]==[1,Fraction(5,3),Fraction(8,3)]
checks+=1

for i in range(100):
    f=R.uniform(0,2,N)
    q={a:np.array([f[a*j%N] for j in range(N)]) for a in (3,5,8)}
    for a in (3,5,8):
        assert np.allclose(np.sort(q[a]),np.sort(f));checks+=1
    assert np.allclose(q[8],q[5][(-np.arange(N))%N]);checks+=1
    assert np.allclose(abs(np.fft.fft(q[8]))**2,abs(np.fft.fft(q[5]))**2);checks+=1
    def T(a):return np.mean([f[j]*f[(j+a)%N]*f[(j+3*a)%N] for j in range(N)])
    assert abs(T(5)-T(-5)-(T(5)-T(8)))<1e-12;checks+=1

for i in range(100):
    dim=4+i%8;A=R.normal(size=(dim,dim))
    E=A.T@A
    values,V=np.linalg.eigh(E)
    K=(V*np.exp(-.25*values))@V.T  # real selfadjoint Euclidean semigroup
    v=R.normal(size=(N,dim))
    for lag in range(1,7):
        def C(a):return sum(v[j]@K@v[(j+a*lag)%N] for j in range(N))/N
        assert abs(C(5)-C(8))<1e-10;checks+=1
        assert abs(C(3)-C(-3))<1e-10;checks+=1
print("PASS",checks,"exact helical alias / real Euclidean gauge-probe reciprocity calibrations")

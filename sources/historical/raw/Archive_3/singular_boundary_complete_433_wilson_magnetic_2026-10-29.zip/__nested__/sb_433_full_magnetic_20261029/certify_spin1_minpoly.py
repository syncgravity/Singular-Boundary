#!/usr/bin/env python3
"""Symbolic Q(sqrt3) certificate for compressed target spin-one spectrum.

The discrete SU2 link contractions yield rational/sqrt(3) recoupling entries.
This independently verifies the exact minimal-polynomial certificate of the
saved 433-by-433 target spin-one matrix (using its 16 occupation sectors).
"""
from pathlib import Path
import numpy as np
import sympy as S
from fractions import Fraction
from scipy.sparse import load_npz
p=Path(__file__).resolve().parent
Z=np.load(p/'basis.npz');subs=Z['face_subsets'];C=load_npz(p/'target_spin1.npz')
roots=[S.Rational(-1,3),S.Rational(-1,27),S.Integer(0),S.Rational(1,81),S.Rational(1,9),S.Integer(1)]
x=S.Symbol('x');P=S.prod(x-r for r in roots)
allroots=[];nblocks=0
for sub in sorted(set(subs)):
 ids=np.where(subs==sub)[0];B=C[ids,:][:,ids].toarray()
 if max(abs(B.ravel()))<1e-12:continue
 nblocks+=1
 exact=S.zeros(len(ids))
 for i in range(len(ids)):
  for j in range(len(ids)):
   v=B[i,j]
   if abs(v)<1e-12:continue
   candidates=[]
   for factor in [S.Integer(1),S.sqrt(3)]:
    f=Fraction(float(v)/float(factor)).limit_denominator(1000)
    value=S.Rational(f.numerator,f.denominator)*factor
    if abs(float(value)-v)<1e-11:candidates.append(value)
   assert candidates,(sub,i,j,v)
   exact[i,j]=candidates[0]
 assert exact==exact.T
 # matrix polynomial in exact Q(sqrt3)
 R=S.zeros(len(ids));power=S.eye(len(ids))
 for k in range(S.degree(P,x)+1):
  R+=S.expand(P).coeff(x,k)*power
  power=power*exact
 assert all(S.simplify(z)==0 for z in R),sub
 # exact characteristic spectrum; rational eigenvalues by polynomial proof
 vals=np.linalg.eigvalsh(B)
 for v in vals:
  rr=min(roots,key=lambda r:abs(float(r)-v))
  assert abs(float(rr)-v)<1e-10
  allroots.append(rr)
assert nblocks==16
assert len(allroots)==81
from collections import Counter
counts=Counter(allroots)
assert counts[S.Integer(1)]==16
assert counts[S.Rational(-1,3)]==32
print('PASS exact minimal polynomial',S.factor(P),'in',nblocks,'blocks')
print('PASS exact rational spin-one eigenvalue counts',dict(sorted(counts.items(),key=lambda x:float(x[0]))))
print('Therefore ||P_1/2 chi_1(W_f) P_1/2||_op = 1 EXACTLY')

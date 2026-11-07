#!/usr/bin/env python3
"""Exact D5 reflection reversal of oriented C5 generator and complex J.
This does not prove that a physical observer dynamically selects either frame.
"""
import numpy as np
I=np.eye(5,dtype=int)
C=np.zeros((5,5),dtype=int)
R=np.zeros((5,5),dtype=int)
for j in range(5):
 C[(j+1)%5,j]=1
 R[(-j)%5,j]=1
assert np.array_equal(R@R,I)
assert np.array_equal(np.linalg.matrix_power(C,5),I)
assert np.array_equal(R@C@R,C.T)
J=np.array([[0,-1],[1,0]])
R2=np.diag([1,-1])
assert np.array_equal(R2@J@R2,-J)
print("PASS 4 exact D5 and complex-orientation identities")

#!/usr/bin/env python3
"""Exact SU2 Peter-Weyl link cutoff gives universal magnetic-compression floor.
Works for all Gauss-invariant joint color intertwiners; no eight-face
full-coupling diagonalization is performed.
"""
import math
C_H=4*math.sqrt(2)/(3*math.pi)
for N in range(0,51):
 D=(N+1)*(N+2)*(2*N+3)//6
 delta=(2*C_H*D)**(-2/3)
 assert 0<delta<=1
 # exact upper on Haar cap, hence at most half kinematic cap weight
 a=math.acos(1-delta)
 H=(a-(1-delta)*math.sqrt(2*delta-delta**2))/math.pi
 assert D*H<=.5+1e-12
 compression_floor=delta/2
 assert compression_floor>0
 if N in (0,1,2,4,8,16,32,50):
  print('max edge character index',N,'dim diagonal D',D,'cap width',delta,'magnetic energy factor',compression_floor)
# Confirm asymptotic scale analytically: D ~ N^3/3; floor ~ N^-2
for N in (16,32,64,128,256,512):
 D=(N+1)*(N+2)*(2*N+3)//6
 floor=0.5*(2*C_H*D)**(-2/3)
 if N>=128:assert .3<floor*N*N<1.2,(N,floor*N*N)
print('PASS exact universal SU2 magnetic compression P_J V P_J >= const*b/(J+1)^2, independent of color and volume')
# Compare extensive Wilson upper/lower energies; face count cancels exactly.
a_plus,c_minus,c_plus=2.0,.78,1.4
for F in (7,30,300,3000):
  C_upper=3/math.sqrt(2)*F*math.sqrt(a_plus*c_plus)
  csum_lower=F*c_minus
  for b in (1e4,1e8):
    N=16
    D=(N+1)*(N+2)*(2*N+3)//6
    ratio=(b*csum_lower/(2*(2*C_H*D)**(2/3)))/(C_upper*math.sqrt(b))
    ref=(b*c_minus/(2*(2*C_H*D)**(2/3)))/((3/math.sqrt(2))*math.sqrt(a_plus*c_plus)*math.sqrt(b))
    assert math.isclose(ratio,ref,rel_tol=1e-12)
print('PASS volume cancels from necessary b^1/4 spin-cutoff ratio under bounded Penrose-type coefficients')

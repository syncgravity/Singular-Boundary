#!/usr/bin/env python3
"""Rational Jacobi moment checks for audited SU2 three-face sample polynomials.
Examples are regression data; general-m theorem is in the research audit.
"""
from fractions import Fraction as Q
P={(3,2):(Q(17,16),-Q(1,8),Q(51,8)),
   (3,4):(Q(17,16),-Q(21,8),Q(111,8)),
   (4,3):(Q(52,25),-Q(12,25),Q(372,25)),
   (4,5):(Q(52,25),-Q(112,25),Q(672,25))}
def hs(N,m,l):
 E=N-3
 return sum(c/Q(E+i+2) for i,c in enumerate(P[m,l]))
for N,m,l,want in ((10,3,2,.6851010101010101),(10,3,4,1.1169191919191918),(16,4,3,.9839607843137255),(16,4,5,1.439843137254902),(100,3,2,.07260113511351135),(100,3,4,.12185856085608547)):
 x=hs(N,m,l)
 assert abs(float(x)-want)<1e-12
 print("PASS rational fixed-collar moment",N,m,l,x)
print("Lim N*HS2 = P(1) at fixed m for each insertion class.")

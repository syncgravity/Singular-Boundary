#!/usr/bin/env python3
"""SU2 exact two-adjacent-face class-sector leakage: local Wilson skein,
conditional Haar color integration and projected kinetic residual.
Deterministic 6-axis spherical 2-design quadrature; no Monte Carlo.
"""
import math
import numpy as np

def mult(q,r):
    a,u=q[0],q[1:]; b,v=r[0],r[1:]
    return np.r_[a*b-np.dot(u,v), a*v+b*u+np.cross(u,v)]
def inv(q):return q*np.array([1.,-1.,-1.,-1.])
def qrot(theta,axis):return np.r_[math.cos(theta),math.sin(theta)*np.asarray(axis)]
def p(q):return float(q[0])
axes=[np.eye(3)[i]*s for i in range(3) for s in (-1,1)]
P=(-.91,-.54,0.,.32,.8)
maxmean=0.;maxsecond=0.
for x in P:
 for y in P:
  # Two face holonomies U_f, U_g with independent conditional class axes.
  d=[]
  for ax in axes:
   U=qrot(math.acos(x),ax)
   for ay in axes:
    V=qrot(math.acos(y),ay)
    z=p(mult(U,V)) - x*y
    d.append(z)
  mean=sum(d)/len(d)
  square=sum(z*z for z in d)/len(d)
  desired=(1-x*x)*(1-y*y)/3
  maxmean=max(maxmean,abs(mean))
  maxsecond=max(maxsecond,abs(square-desired))
  assert abs(mean)<1e-14
  assert abs(square-desired)<1e-14
print('conditional SU2 color average mean/maxerror:',maxmean,'variance/maxerror:',maxsecond)

# Verify the edge-gradient skein with noncommuting U and V.
for i in range(1,35):
 u=np.array([math.sin(i+.3),math.cos(3*i+.2),math.sin(2*i+.1)]);u/=np.linalg.norm(u)
 v=np.array([math.sin(2*i+.9),math.cos(5*i+.11),math.sin(4*i+.41)]);v/=np.linalg.norm(v)
 U=qrot(.013+.069*i,u)
 V=qrot(.038+.041*i,v)
 # Shared primal edge Z: f holonomy = Z, g holonomy = Z^{-1} V
 g0=mult(inv(U),V)
 def fval(z):return p(z)
 def gval(z):return p(mult(inv(z),V))
 gradf=[];gradg=[];h=2e-6
 for ax in np.eye(3):
  qp=qrot(h/2,ax);qm=qrot(-h/2,ax)
  gradf.append((fval(mult(qp,U))-fval(mult(qm,U)))/(2*h))
  gradg.append((gval(mult(qp,U))-gval(mult(qm,U)))/(2*h))
 empirical=np.dot(gradf,gradg)
 predicted=(p(V)-p(U)*p(g0))/4
 assert abs(empirical-predicted)<4e-9, (i,empirical,predicted)
print('SU2 mixed-gradient six-edge skein: PASS on 34 noncommuting configurations')

# SU2 Haar exact moments for fundamental normalized trace.
p2=1/4;p4=1/8
# For phi=p_f*p_g, its off-class kinetic residual on the shared edge is
# -(a_e/2)*(p_union-p_fp_g); its squared Haar norm equals 3a_e^2/64.
class_leak=(1/4)*((1-p2)**2/3)
assert abs(class_leak-3/64)<1e-14
# Cross-face mixed Gamma square: E(Gamma_e^2) = a_e^2*3/256.
gamma_sq=(1/16)*((1-p2)**2/3)
assert abs(gamma_sq-3/256)<1e-14
print('Haar exact E[Gamma_e(p_f,p_g)^2]/a_e^2 =',gamma_sq)
print('Haar exact ||(I-P_class) [-a_e Delta_e](p_f p_g)||^2/a_e^2 =',class_leak)
# The center-even spin-one x spin-one product has off-class kinetic leakage
# -2 Gamma_e * (8p_f)*(8p_g) = -32 a_e p_f p_g delta.
# Haar E[p^2*(1-p^2)]=1/8, axes E[(n.m)^2]=1/3.
spinone_leak=(32**2)*((p2-p4)**2)/3
assert abs(spinone_leak-16/3)<1e-12
print('Haar exact center-even ||(I-P_class) T[chi_1(f)chi_1(g)]||^2/a_e^2 =',spinone_leak)
# Normalized center-even chi_1(f) * fundamental trace p_g: input 2*chi_1(f)*p_g.
# Its off-class residual is -8 a_e p_f delta; Haar norm^2=2 a_e^2.
relevant_leak=8**2*(p2-p4)*(1-p2)/3
assert abs(relevant_leak-2)<1e-13
print('Haar exact normalized center-even ||(I-P_class) T[2chi_1(f)p_g]||^2/a_e^2 =',relevant_leak)
print('PASS: class compression loses a genuine SU2 center-even electric color channel; not a mass-gap proof')

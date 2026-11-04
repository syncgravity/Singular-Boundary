#!/usr/bin/env python3
"""Exact quaternion and spin-block nested SU(2) original-link regression. Requires SymPy."""
import sympy as s
a0,b0=s.symbols("a0 b0",real=True)
a=s.symbols("a1:4",real=True)
b=s.symbols("b1:4",real=True)
def deriv(f,q0,vec,i,right):
    v=[q0*int(j==i)+sum((s.LeviCivita(j,k,i) if right else s.LeviCivita(j,i,k))*vec[k] for k in range(3)) for j in range(3)]
    return s.expand(-vec[i]*s.diff(f,q0)/2+sum(v[j]*s.diff(f,vec[j])/2 for j in range(3)))
def D(f):
    return s.expand(sum(deriv(deriv(f,a0,a,i,True),b0,b,i,False) for i in range(3)))
def C(f,q0,vec):
    return s.expand(-sum(deriv(deriv(f,q0,vec,i,True),q0,vec,i,True) for i in range(3)))
def K(f):
    return s.expand(4*C(f,a0,a)+4*C(f,b0,b)+2*D(f))
def sphere(f):
    return s.factor(s.expand(f).subs(a[2]**2,1-a0**2-a[0]**2-a[1]**2).subs(b[2]**2,1-b0**2-b[0]**2-b[1]**2))
x,y,u=2*a0,2*b0,4*a0*a0-1
dot=sum(a[i]*b[i] for i in range(3))
T=D(u*y)
F=x*y
G=s.expand((F*K(x)+x*K(F)-K(F*x))/2)
B=y-s.Rational(19,216)*u*y-s.Rational(7,216)*T
identities={
"Kx":K(x)-3*x,"Ky":K(y)-3*y,
"Dxy":D(F)-dot,"T":T-4*a0*dot,
"Kuy":K(u*y)-11*u*y-2*T,"KT":K(T)-u*y-10*T,
"Gamma":G-(3-u)*y+T/2,"inverse":K(B)-G,
"minimal polynomial":D(T)+T/2-u*y/2}
for name,err in identities.items():
    assert sphere(err)==0,(name,sphere(err))
Jz=s.diag(1,0,-1)
Jp=s.Matrix([[0,s.sqrt(2),0],[0,0,s.sqrt(2)],[0,0,0]])
Jph=s.Matrix([[0,1],[0,0]])
Jzh=s.diag(s.Rational(1,2),-s.Rational(1,2))
spinD=s.kronecker_product(Jz,Jzh)+(s.kronecker_product(Jp,Jph.T)+s.kronecker_product(Jp.T,Jph))/2
assert spinD.eigenvals()=={s.Rational(1,2):4,s.Integer(-1):2}
coef=(11*s.eye(6)+2*spinD).inv()*(-s.eye(6)-spinD/2)
assert coef==-s.Rational(19,216)*s.eye(6)-s.Rational(7,216)*spinD
assert coef.eigenvals()=={-s.Rational(5,48):4,-s.Rational(1,18):2}
norm=sum(abs(v)*m for v,m in coef.eigenvals().items())
assert norm==s.Rational(19,36)
assert 4+6*norm==s.Rational(43,6)
assert 2*4+3*6*norm==s.Rational(35,2)
print("PASS: nine exact quaternion identities; coupled-spin inverse, eigenvalues, nuclear PW norm.")

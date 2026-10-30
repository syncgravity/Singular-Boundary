#!/usr/bin/env python3
"""Deterministic SU(2) exponential-coordinate quartic remainder audit.
No stochastic simulation. Exact symbolic Taylor and finite covariance matrices.
"""
import sympy as s
import numpy as np
from scipy.linalg import eigh
from itertools import combinations

h,r,beta,a=s.symbols('h r beta a',positive=True)
z=s.sqrt(h)*r/2
# Exact SU(2) radial Wilson expansion through order six.
taylor=s.series(1-s.cos(z),h,0,4).removeO()
assert s.simplify(taylor-(h*r**2/8-h**2*r**4/384+h**3*r**6/46080))==0
# Fourth-chaos decomposition for n=3 color components.
t1,t2,c=s.symbols('t1 t2 c',positive=True)
# Bivariate quadratic-generating function coefficient u^2 v^2.
u,v=s.symbols('u v')
# det(I-2 diag(u,v) covariance) = 1 - 2t1u - 2t2v +4(t1*t2-c**2)uv.
G=(1-2*t1*u-2*t2*v+4*(t1*t2-c**2)*u*v)**(-s.Rational(3,2))
M22=s.diff(G,u,2,v,2).subs({u:0,v:0})
Cov=s.factor(M22-225*t1**2*t2**2)
assert s.simplify(Cov-(600*t1*t2*c**2+120*c**4))==0
assert s.simplify(Cov.subs({t1:1,t2:1,c:1})-720)==0
# Coercivity constants from uniform a edge coefficient; K=sqrt(M)∘sqrt(M).
minK=s.Rational(105,64)*a
min_t2=4*a/beta
minSigmaHad=2*minK/beta
lower=s.simplify(600*min_t2*minSigmaHad*(beta/s.Integer(384))**2)
upper=s.simplify(s.Integer(46080)*a**2/beta**2*(beta/s.Integer(384))**2)
assert lower==s.Rational(2625,49152)*a**2
assert upper==s.Rational(5,16)*a**2
print('Exact quartic-remainder variance lower coefficient:',lower)
print('Exact quartic-remainder variance upper coefficient:',upper)

# Authentic three-face Z^5 Penrose incidence fixture.
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):
 return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
faces=[edges(face) for face in seed]
E=set.union(*faces)
assert len(E)==10 and max(sum(e in f for f in faces) for e in E)==2

def check_dual(M):
 w,U=eigh(M)
 assert w.min()>1e-9 and w.max()<=8+1e-8
 sqrtM=(U*np.sqrt(w))@U.T
 K=sqrtM**2
 Sigma=np.sqrt(2.)*sqrtM
 ts=np.diag(Sigma)
 Kr=Sigma**2
 cov4=600*np.outer(ts,ts)*Kr+120*(Kr**2)
 for _q in [np.ones(M.shape[0]),np.array([(-1.)**i for i in range(M.shape[0])]),np.linspace(-1,1,M.shape[0])]:
  quad=float(_q@cov4@_q)
  norm2=float(_q@_q)
  assert quad>=7875*norm2-1e-7
  assert quad<=46080*norm2+1e-6
  print('F=',M.shape[0], 'weighted quartic var/norm2=',quad/norm2,'min eigen K=',np.linalg.eigvalsh(K).min())

Mseed=np.diag(np.full(3,4.))-np.diag(np.ones(2),1)-np.diag(np.ones(2),-1)
check_dual(Mseed)
# 2D finite square-lattice face dual is an incidence-class surrogate; not Penrose.
for n in (5,10):
 F=n*n; M=np.eye(F)*4
 for i in range(n):
  for j in range(n):
   k=i*n+j
   if i+1<n:M[k,k+n]=M[k+n,k]=-1
   if j+1<n:M[k,k+1]=M[k+1,k]=-1
 check_dual(M)
print('PASS: exact SU(2) Taylor, 3-color Wick fourth covariance, signed coercivity and spatial incidence.')

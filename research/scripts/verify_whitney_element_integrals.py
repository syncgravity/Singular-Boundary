"""Independent exact polynomial and Gaussian Whitney 1-form element tests."""
import numpy as np
from numpy.polynomial.legendre import leggauss
rng=np.random.default_rng(537)
components=[0,1,0,1]
coefs=[(1.,-1.),(0.,1.),(0.,-1.),(-1.,1.)]
variables=[1,0,1,0]
def exact(J):
 G=np.linalg.inv(J)@np.linalg.inv(J).T
 A=np.zeros((4,4))
 for i in range(4):
  for j in range(4):
   a,b=coefs[i];c,d=coefs[j]
   moment=a*c+(a*d+b*c)/2+b*d/3 if variables[i]==variables[j] else (a+b/2)*(c+d/2)
   A[i,j]=abs(np.linalg.det(J))*G[components[i],components[j]]*moment
 return A
def gauss(J):
 x,w=leggauss(4);x=(x+1)/2;w=w/2;R=np.zeros((4,4))
 for u,wu in zip(x,w):
  for v,wv in zip(x,w):
   B=np.array([[1-v,0],[0,u],[-v,0],[0,u-1]])@np.linalg.inv(J)
   R+=wu*wv*abs(np.linalg.det(J))*(B@B.T)
 return R
for _ in range(300):
 J=rng.normal(size=(2,2))
 if abs(np.linalg.det(J))<.15:continue
 A,B=exact(J),gauss(J)
 assert np.max(np.abs(A-B))<1e-9
 assert np.linalg.eigvalsh(A)[0]>-1e-10
print('PASS independent exact moments versus Gaussian edge mass elements')

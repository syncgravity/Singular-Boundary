#!/usr/bin/env python3
"""Independent mixed-spin trace-class superoperator finite regression, not an all-order proof."""
from itertools import product
from math import sqrt
import numpy as np
from scipy.linalg import svdvals
def spinops(n):
 j=n/2;m=np.arange(j,-j-1,-1)
 plus=np.zeros((n+1,n+1),complex)
 for k in range(n):
  x=m[k+1];plus[k,k+1]=sqrt((j-x)*(j+x+1))
 minus=plus.conj().T
 return (plus+minus)/2,(plus-minus)/(2j),np.diag(m).astype(complex)
def output(p,q,l):
 d=2*(p+1)*(l+1);a,b,c=spinops(p),spinops(l),spinops(1)
 ia=np.eye(p+1);ib=np.eye(l+1);ic=np.eye(2);ident=np.eye(d,dtype=complex)
 A=[np.kron(np.kron(a[i],ib),ic) for i in range(3)]
 B=[np.kron(np.kron(ia,b[i]),ic) for i in range(3)]
 C=[np.kron(np.kron(ia,ib),c[i]) for i in range(3)]
 def D(x):return -sum((A[i]@x@B[i]+B[i]@x@C[i] for i in range(3)),np.zeros_like(x))
 P=p*(p+2);L=l*(l+2);base=P+L+3
 alpha=-q if l==q+1 else q+2
 beta=(-1 if l==q+1 else 1)/(q+1)
 rhs=alpha*ident+beta*D(ident)
 x=np.zeros_like(rhs);term=rhs/base
 for _ in range(80):
  x+=term;term=(-2/base)*D(term)
  if np.linalg.norm(term,'fro')<2e-14:break
 assert np.linalg.norm(base*x+2*D(x)-rhs,'fro')<1e-9
 S=(sqrt(P*L)+sqrt(3*L))/4
 bound=d*(abs(alpha)+S/(q+1))/(base-2*S)
 actual=svdvals(x).sum();assert actual<=bound+1e-8
 return actual,bound
for p,q in product(range(1,6),repeat=2):
 din=2*(p+1)*(q+1);a=b=0
 for l in (q+1,q-1):
  x,y=output(p,q,l);wt=2*(p+1)*(l+1)*(1+max(p,l))
  a+=wt*x;b+=wt*y
 den=16*din**2*(1+max(p,q))
 assert a<=b+1e-8 and b/den<=105/(32*(p+q))+1e-12
print("PASS: 50 original-link Fourier inverse/Schatten checks; 25 mixed-spin ratios")

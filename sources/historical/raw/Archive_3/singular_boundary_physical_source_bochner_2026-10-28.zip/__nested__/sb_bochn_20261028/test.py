import numpy as np
from scipy.linalg import eigh_tridiagonal
for N in [24,36,48]:
 a,b,h=1.,5.,.1
 n=np.arange(N,dtype=float)
 E,c=eigh_tridiagonal(a*n*(n+2)+b,np.full(N-1,-b/2),select='i',select_range=(0,0))
 c=c[:,0]
 k=np.arange(1,1501);p=np.cos(np.pi*k/1501);wt=2/1501*np.sin(np.pi*k/1501)**2
 U=np.zeros((N,len(p))); Up=np.zeros_like(U); Upp=np.zeros_like(U)
 U[0]=1;U[1]=2*p;Up[1]=2
 for j in range(2,N):
  U[j]=2*p*U[j-1]-U[j-2]
  Up[j]=2*U[j-1]+2*p*Up[j-1]-Up[j-2]
  Upp[j]=4*Up[j-1]+2*p*Upp[j-1]-Upp[j-2]
 O=c@U; O1=c@Up; O2=c@Upp
 w1=O1/O;w2=O2/O-w1*w1
 prob=wt*O*O
 expect=lambda x:float(np.dot(prob,x))
 D=3*a*h*p; F=-2*a*h*(1-p*p)*w1
 direct=expect((D+F)**2)
 geom=expect(a*a*h*h*(2+p*p))
 curv=expect(-2*a*a*h*h*((1-p*p)**2*w2-p*(1-p*p)*w1))
 print(N,'E0',float(E[0]),'full',direct,'geom',geom,'score-curv',curv,'res',direct-geom-curv)

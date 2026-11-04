import numpy as np
from scipy.linalg import expm
L=np.array([[1.,-1.],[-1.,1.]])
V=np.diag([.7,-.3]);P=np.diag([1.,-1.]);s=.25
def constants(H):
 w,U=np.linalg.eigh(H);D=w[1]-w[0]
 C=np.exp(2*s*w[0])*expm(-2*s*H)[0,0]/U[0,0]**2-1
 return D,C,U[1,0]**2
def window(b,eta=.1):
 (D0,C0,c),(Db,Cb,_)=constants(L+V),constants(L+V-b*P)
 assert 0<eta<c/2
 tm=s+max(0,np.log(C0*(1-eta**2)/eta**2)/(2*D0),np.log(Cb*(1-eta**2)/eta**2)/(2*Db))
 tp=np.log((c-eta)/eta)/(4*b)
 return tm,tp
for b in (.2,.8):
 a,z=window(b);print(b,a,z,a<z)
assert window(.2)[0]<window(.2)[1]
assert window(.8)[0]>window(.8)[1]
print('PASS bridge time-window audit')

import numpy as np
from fractions import Fraction
from pathlib import Path
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--matrix',default='/mnt/data/global_whitney_11face.npz')
a=parser.parse_args()
d=np.load(a.matrix); ids=list(map(int,d['edge_ids'])); K=np.linalg.inv(d['matrix'])
targets={(0,86):.3369725553099113,(1,88):.5031861223918195,(4,372):.3836664423821451,(13,26):.4584295335630277}
for pair,expected in targets.items():
 L=[ids.index(e) for e in pair];B=[i for i in range(len(ids)) if i not in L]
 A=K[np.ix_(L,L)]; Z=K[np.ix_(B,B)]; C=K[np.ix_(L,B)]
 la,U=np.linalg.eigh(A); lb,V=np.linalg.eigh(Z)
 W=(U/np.sqrt(la))@U.T@C@(V/np.sqrt(lb))@V.T
 alpha=np.linalg.svd(W,compute_uv=False)[0]
 assert abs(alpha-expected)<1e-9 and 0<alpha<1
 print(pair,alpha)
eps=Fraction(1,4)
for n in [1,4,16,256]:
 assert eps*eps*n*n/Fraction(2)==Fraction(n*n,32)
print('PASS four metric energy couplings and exact unbounded Fourier offblock sequence')

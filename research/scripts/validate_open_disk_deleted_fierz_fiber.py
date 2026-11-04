"""Run with penrose_study.zip modules importable; validates deleted-face fiber."""
import numpy as np
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
a=Approximant(M=5);words,sg,E=penrose_faces(a)
assert set(map(int,words[0]))=={0,1,4,13}
assert set(map(int,words[1]))=={0,3,14,86}
rng=np.random.default_rng(99)
I=np.eye(2,dtype=complex)
sig=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
def U():
 q=rng.normal(size=4);q/=np.linalg.norm(q)
 return q[0]*I+1j*sum(q[k+1]*sig[k] for k in range(3))
links={int(e):U() for e in range(E)}
A=[(0,1),(14,1),(86,-1),(3,-1)]
B=[(3,1),(87,1),(89,-1),(88,1),(372,1),(300,-1),(297,-1),(295,-1),(291,1),(16,1),(34,1),(26,-1),(25,-1),(7,-1),(9,1),(11,1),(14,-1),(13,1),(4,-1),(1,-1)]
def p(word):
 m=I
 for e,s in word:m=m@(links[e] if s>0 else links[e].conj().T)
 return np.trace(m).real/2
def smooth(edge):
 def rotate(word,sign):
  j=word.index((edge,sign));return word[j+1:]+word[:j]
 sign=next(s for e,s in A if e==edge)
 return rotate(A,sign)+rotate(B,-sign)
S3,S14=smooth(3),smooth(14)
a0,b0=p(A),p(B);s30=p(S3)
u0,u86,u14=links[0].copy(),links[86].copy(),links[14].copy()
values=[]
for _ in range(100):
 h=U();links[0]=u0@h;links[86]=u86@u14.conj().T@h@u14
 assert abs(p(A)-a0)<1e-11 and abs(p(B)-b0)<1e-11
 assert abs(p(S3)-s30)<1e-11
 values.append(p(S14))
assert np.std(values)>1e-3
print("PASS fiber invariants and varying S14; exact Schur variance=(1-a^2)(1-b^2)/3")

#!/usr/bin/env python3
"""Read-only symbolic audit of the strong-field curvature-density bound."""
import sympy as s
from itertools import combinations
from collections import Counter
import json
k,A,B,a,b,h,g2=s.symbols('k A B a b h g2',positive=True)
sm,sp=s.symbols('sigma_minus sigma_plus',positive=True)
phi=(1+s.sqrt(5))/2
F=3*A*k/8+3*B/k
kopt=s.sqrt(8*B/A)
assert s.simplify(s.diff(F,k).subs(k,kopt))==0
assert s.simplify(F.subs(k,kopt)-3*s.sqrt(A*B)/s.sqrt(2))==0
assert s.simplify(3*s.sqrt(4*a/b)/s.sqrt(2)-3*s.sqrt(2)*s.sqrt(a/b))==0
Amax=4*g2/sm; Bmax=4/(g2*h*h*sm); bmin=4/(g2*h*h*sp)
assert s.simplify(3*s.sqrt(Amax*Bmax)/(s.sqrt(2)*bmin)-3*sp*g2*h/(s.sqrt(2)*sm))==0
assert s.simplify(s.sin(2*s.pi/5)/s.sin(s.pi/5)-phi)==0
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
def dist(x,y):return sum(abs(i-j) for i,j in zip(x,y))
def edges(face):
 z=list(map(tuple,face))
 return {tuple(sorted((x,y))) for x,y in combinations(z,2) if dist(x,y)==1}
faces=[edges(f) for f in seed];inc=Counter(e for f in faces for e in f)
assert len(inc)==10 and sum(v==1 for v in inc.values())==8
print(json.dumps({"trial_bound":"3/sqrt(2) sqrt(A B)","uniform_mean_deficit":"3 sqrt(2) sqrt(a/b)","geometric_mean_deficit":"(3/sqrt(2)) phi g3^2 h","canonical_seed_edges":10,"no_simulation":True},indent=2))

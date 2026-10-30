#!/usr/bin/env python3
"""Sympy exact rational verification of the crossing-preserving obstruction."""
import json,time
import sympy as sp
from pathlib import Path
from direct_cut_project import build
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
P=Path(__file__).resolve().parent

g,_=build(5.,0);W,_=product_collar(g);Q=Q_from_seed(g,seed_support(g));R=set(range(len(W)))-Q
H=sorted({e for q in Q for e,s in W[q]});A=sorted(f for f in R if any(e in H for e,s in W[f]));E=sorted({e for f in A for e,s in W[f]}-set(H));C=sorted(f for f in R if f not in A and any(e in E for e,s in W[f]));
def mat(fs,es):
 ix={e:j for j,e in enumerate(es)};m=sp.zeros(len(fs),len(es))
 for i,f in enumerate(fs):
  for e,s in W[f]:
   if e in ix:m[i,ix[e]]+=s
 return m
DH=mat(A,H);DA=mat(A,E);DC=mat(C,E)
start=time.time();print('matrices built',DH.shape,DA.shape,DC.shape,flush=True)
# Rational nullspace; matrix has only +/-1 so sparse elimination stays tractable
N=DC.nullspace()
print('crossing nullspace',len(N),'time',time.time()-start,flush=True)
assert len(N)==22
M=DH.row_join(DA*sp.Matrix.hstack(*N))
rank0=DH.rank();rank_joint=M.rank();rankcross=DC.rank();rank_full=DH.row_join(DA).rank()
print('exact Q ranks',rank0,rank_joint,rankcross,'allowed rank',rank_joint-rank0,'elapsed',time.time()-start,flush=True)
assert (rank0,rank_joint,rankcross,rank_full)==(35,36,67,59)
(P/'exact_crossing_rank.json').write_text(json.dumps({'field':'Q rationals, exact SymPy elimination','local_rank':rank0,'crossing_rank':rankcross,'crossing_nullity':len(N),'rank_after_crossing_fixed_moves':rank_joint,'extra_exterior_modes_accessible_while_preserving_crossing_faces':rank_joint-rank0,'total_exterior_modes':rank_full-rank0,'rank_full_local_plus_halo':rank_full,'dimensions':{'A_faces':len(A),'H_links':len(H),'E_exterior_links':len(E),'crossing_faces':len(C)}},indent=2))

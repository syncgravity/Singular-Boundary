#!/usr/bin/env python3
"""Certify a nonnegative local-frustration closure matrix.

Input JSON: {"faces":[...], "rows":[{"face":"...","coefficients":{"...":"1/3"},
"proof_word_certificate":"path/to/proof"},...], "incidence_hash":"..."}
Computes numerical screening and rational (if possible) weighted super-solution bounds.
WARNING: matrix inequality m_e<=B*d is a separate mathematical proof obligation.
"""
import json,sys,math
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

def run(path):
 o=json.loads(Path(path).read_text());faces=o['faces']; n=len(faces);idx={f:i for i,f in enumerate(faces)}
 assert len(idx)==n and len(o['rows'])==n
 B=np.zeros((n,n)); proofs=[]
 for i,row in enumerate(o['rows']):
  assert row['face']==faces[i]
  proofs.append(row.get('proof_word_certificate'))
  for k,v in row['coefficients'].items():
   B[i,idx[k]]=float(Fraction(str(v)))
 assert np.isfinite(B).all() and B.min()>=0
 rho=float(np.max(np.abs(np.linalg.eigvals(B))))
 # Certified sufficient test: rationally rounded positive solution h=(I-B)^-1 1.
 if rho<1-1e-10:
  h=np.linalg.solve(np.eye(n)-B,np.ones(n))
  h=np.ceil(h*1000000)/1000000
  margin=float(np.min(h-B@h))
 else:h=None; margin=None
 report={'n':n,'rho_numeric_screen':rho,'row_sum_max':float(B.sum(axis=1).max()),
 'positive_supersolution_rounding_margin':margin,'weighted_bound_on_x_F':None,
 'pointwise_word_proofs_present':all(proofs),'incidence_hash':o.get('incidence_hash'),
 'status':'NOT_CERTIFIED: separate pointwise nonabelian inequality proof and exact interval arithmetic still required'}
 if margin is not None and margin>=1-1e-7:
  report['weighted_bound_on_x_F']=float(1.5*np.sum(h));report['status']='SPECTRAL_SUFFICIENT_CONDITION_VERIFIED_NUMERICALLY; POINTWISE INEQUALITIES UNVERIFIED'
 return report
if __name__=='__main__':
 if len(sys.argv)!=2:raise SystemExit('Usage: python certify_B.py candidate_B.json')
 print(json.dumps(run(sys.argv[1]),indent=2))

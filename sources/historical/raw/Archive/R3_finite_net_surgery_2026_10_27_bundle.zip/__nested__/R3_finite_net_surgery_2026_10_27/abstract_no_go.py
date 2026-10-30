#!/usr/bin/env python3
"""Exact nonabelian abstract-plaquette obstruction; NOT a Penrose prism topology.
Two four-letter Wilson words differ by a frozen center holonomy -I.
"""
import json
from pathlib import Path
import numpy as np
from construct_surgery import qmul,qinv,unit_random
ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(501)
identity=np.array([1.,0.,0.,0.]);minus=-identity
res=[]
for i in range(500):
 U,x=unit_random(rng,2)
 y=qmul(U,x)
 W1=qmul(qmul(qmul(U,x),identity),identity)
 W2=qmul(qmul(qmul(U,x),identity),minus)
 S=2.-W1[0]-W2[0]
 assert abs(S-2)<5e-14
 res.append(S)
# H={U}, K={U,x}; s_H=s_K=2, all allowed transformations preserve full S.
proof={'model':'abstract two-quadrilateral Wilson-word system, NOT certified as a Penrose or embedded prism 2-complex',
       'face_words':['U x a b','U x a c'], 'frozen_background':{'a':'I','b':'I','c':'-I'},
       'identity':'W2=-W1, d(W1)+d(W2)=2 for every U,x',
       'H':['U'],'K':['U','x'],'s_H':2,'s_K':2,'full_action_for_all_Ux':2,
       'trials':500,'max_numerical_action_error':max(abs(x-2) for x in res),
       'consequence':'No universal positive alpha for an absolute-action surgery follows solely from bounded face word length, O(q) adjustable links, and Haar-jacobian control; an exterior compatibility input is necessary.'}
(ROOT/'abstract_no_go_certificate.json').write_text(json.dumps(proof,indent=2));print('PASS',proof['max_numerical_action_error'])

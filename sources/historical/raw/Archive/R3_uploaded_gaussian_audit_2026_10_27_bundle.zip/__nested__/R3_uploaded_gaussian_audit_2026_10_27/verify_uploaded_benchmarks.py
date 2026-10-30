#!/usr/bin/env python3
"""Independent numerical check of supplied compact-Haar one-prism character series.
This is a consistency check, not a proof of the character-expansion formula.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.special import ive
root=Path(__file__).resolve().parent
source=json.loads((root/'uploaded_exact_compact_certificate.json').read_text())
max_error=0.
for row in source['single_prism']['coupling_rows']:
 lam=row['lambda'];q=2.*ive(1,lam)/lam
 ns=np.arange(1,int(max(100,10*math.sqrt(lam))+1))
 ratios=ive(ns+1,lam)/ive(1,lam)
 correction=1+np.sum((ns+1)**2*ratios**6)
 actual=q*correction
 error=abs(actual-row['exact_insertion_ratio']);max_error=max(max_error,error)
 assert error<5e-8,(lam,actual,row['exact_insertion_ratio'])
print('Uploaded single-prism SU2 sphere character-series rows independently consistent; max error=',max_error)

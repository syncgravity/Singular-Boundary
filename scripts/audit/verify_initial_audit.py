#!/usr/bin/env python3
"""Read-only deterministic Stage26 and rational trace-obstruction checks.
Usage: python3 verify_initial_audit.py /path/to/original/archives
Requirements: Python 3, numpy. DOES NOT perform MCMC or spectral fitting.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib, io, json, re, sys, zipfile
import numpy as np

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):
    return sum(a[i][i] for i in range(len(a)))
def sha(b):
    return hashlib.sha256(b).hexdigest()
def rational_counterexample():
    a=[[F(1),F(7,5)],[F(7,5),F(4)]]
    b=[[F(4),F(7,5)],[F(7,5),F(1)]]
    k=[[F(1),F(7,10)],[F(7,10),F(1)]]
    p=[[F(1,2)]*2 for _ in range(2)]
    z=F(17,10)
    cavity=tr(mm(mm(a,p),b))
    complete=tr(mm(mm(a,k),b))
    assert cavity==F(324,25) and complete==F(543,25)
    assert complete-z*cavity==F(-39,125)
    assert k[0][0]*k[1][1]-k[0][1]*k[1][0]>0
    assert a[0][0]*a[1][1]-a[0][1]*a[1][0]>0
    assert b[0][0]*b[1][1]-b[0][1]*b[1][0]>0
    return {'completed_trace':str(complete),'cavity_trace':str(cavity),'defect':str(complete-z*cavity)}
def stage26(directory):
    result=[]
    for path in sorted(directory.glob('*_stage26.zip')):
        with zipfile.ZipFile(path) as archive:
            meta=[x for x in archive.namelist() if x.endswith('/latest.json')]
            assert len(meta)==1
            j=json.loads(archive.read(meta[0]))
            outers=[x for x in archive.namelist() if re.search(r'/outer_\d{8}\.npz$',x)]
            sweeps=sorted(int(re.search(r'outer_(\d{8})',x).group(1)) for x in outers)
            assert sweeps==list(range(10020,12001,20))
            assert j['observations']==100 and j['sweep']==12000
            last=next(x for x in outers if x.endswith('/'+j['record']))
            assert sha(archive.read(last))==j['record_sha256']
            with np.load(io.BytesIO(archive.read(last)),allow_pickle=False) as npz:
                assert npz['direct_timeslice'].shape==(20,4)
                assert npz['conditional'].shape==(2,9,4,4)
            result.append({'archive':path.name,'sha256':sha(path.read_bytes()),'records':100,'record_hash_valid':True})
    assert len(result)==8, 'Expected eight original Stage26 ZIPs'
    return result
if __name__=='__main__':
    root=Path(sys.argv[1] if len(sys.argv)>1 else '/mnt/data')
    print(json.dumps({'rational_counterexample':rational_counterexample(),'stage26':stage26(root)},indent=2))

#!/usr/bin/env python3
"""Exact dense source-graph crosscheck: first 3 sizes; no original source sharing."""
import sys, json, math, argparse
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh
from scipy import sparse
sys.path.insert(0,str(Path(__file__).parent))
from verify_pf_i10_source_spectral import periodic_sparse,source_import,SOURCE_SHA
from verify_pf_i10_multimass import same_graph_uniform
P=Path(__file__).parent
ap=argparse.ArgumentParser()
ap.add_argument('--source-script',type=Path,required=True)
ap.add_argument('--cache',type=Path,default=P/'cache')
ap.add_argument('--output',type=Path,default=P/'PF_I10_EXACT_THREE_SIZES.json')
args=ap.parse_args()
s=source_import(args.source_script)
rows=[]
for ngrid in [7,10,12]:
    z=np.load(args.cache/f'PF_I10_source_{ngrid}.npz',allow_pickle=False)
    L=sparse.csr_matrix((z['data'],z['indices'],z['indptr']),shape=tuple(z['shape']))
    meta=json.loads(str(z['meta'].item()))
    Pm,_=periodic_sparse(meta['n'])
    Um=same_graph_uniform(L)
    spec={name:eigvalsh(M.toarray(),check_finite=False) for name,M in [('source',L),('periodic',Pm),('uniform',Um)]}
    out={'Ngrid':ngrid,'original_source_sha256':SOURCE_SHA,'n':meta['n'],'e':meta['edges'],'source_operator':meta}
    for name,eig in spec.items():
        assert np.min(eig)>-1e-9
        pos=eig[eig>1e-10]
        out[name]={'zero_modes':int(len(eig)-len(pos)), 'smallest_positive':float(min(pos)),
                   'traceL_over_n':float(eig.mean()),'positive_mode_count':len(pos),
                   'masses':{}}
        for m2 in [0.0001,0.01,1.,100.]:
            out[name]['masses'][str(m2)]={
                'sqrt':float(np.sqrt(pos+m2).mean()),
                'zeta_prime':float(-np.log(pos+m2).mean()),
                'relative_logdet':float(np.log1p(pos/m2).mean())}
    out['ratios']={}
    for m2 in ['0.0001','0.01','1.0','100.0']:
        out['ratios'][m2]={}
        for f in ['sqrt','zeta_prime','relative_logdet']:
            qc=out['source']['masses'][m2][f]
            per=out['periodic']['masses'][m2][f]
            uni=out['uniform']['masses'][m2][f]
            out['ratios'][m2][f]={'source_over_periodic':qc/per,
                                    'source_over_uniform':qc/uni,
                                    'uniform_over_periodic':uni/per}
    print('Exact:',ngrid,'mass .0001',out['ratios']['0.0001'],'flow',[out['ratios'][str(m)]['relative_logdet']['source_over_periodic'] for m in [0.0001,0.01,1.,100.]],flush=True)
    rows.append(out)
args.output.write_text(json.dumps({'scope':'exact positive-eigenmode finite scalar spectra; source script SHA-pinned','rows':rows},indent=2,sort_keys=True)+'\n')

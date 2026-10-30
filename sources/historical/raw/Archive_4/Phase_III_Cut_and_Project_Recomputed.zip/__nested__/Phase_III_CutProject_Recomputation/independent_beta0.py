"""Exact beta=0 SU(2) Wilson ensemble: independent product-Haar links.

Compute the lowest eigenvalue with k=1, avoiding Kramers-doublet selection
problems inherent in a k=4 sparse solve. The interacting gap uses complete
dense eigenspectra instead (see replay_dense.py).
"""
from pathlib import Path
import json
import numpy as np
from scipy.sparse.linalg import eigsh
from direct_cut_project import build,validate
from phase2_extended import sparse_laplacian
from haar_sampler import haar_su2


def run():
    rows=[];geometry=[]
    for radius in (5.,6.5,8.,10.):
        for o in range(5):
            g,gamma=build(radius,o)
            di=validate(g,gamma)
            geometry.append({'radius':radius,'offset':o,**di})
            for seed in range(8):
                rng=np.random.default_rng(20261011+int(radius*1000)*101+o*2999+seed*991)
                U={e:haar_su2(rng) for e in g.edges}
                h=sparse_laplacian(g,U)
                ground=float(eigsh(h,k=1,which='SA',tol=1e-11,maxiter=20000,
                                   return_eigenvectors=False,v0=np.ones(h.shape[0],complex))[0])
                rows.append({'radius':radius,'offset':o,'seed':seed,'n':len(g.labels),'lambda0':ground})
            means=[x['lambda0'] for x in rows if x['radius']==radius and x['offset']==o]
            print('R',radius,'offset',o,'n',len(g.labels),'lambda0_mean',round(float(np.mean(means)),6),flush=True)
    output={'description':'Independent beta=0 link-Haar Wilson ensemble on verified direct-window P3 patches',
            'solver':'eigsh k=1 fixed starting vector, tolerance 1e-11',
            'n_link_seeds_per_offset':8,'n_offsets_per_size':5,'rows':rows,'geometry':geometry}
    Path(__file__).with_name('beta0_independent.json').write_text(json.dumps(output,indent=2))
    print('total configs',len(rows))

if __name__=='__main__':run()

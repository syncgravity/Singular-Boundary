#!/usr/bin/env python3
"""Self-contained genuine-Penrose audit of an eta-regularized Gaussian rank-Q update.
No output in this script is a compact Haar or noncommuting SU2 Gibbs theorem.
"""
import json, math
from pathlib import Path
from collections import Counter
import numpy as np
from scipy.sparse import coo_matrix, eye
from scipy.sparse.linalg import splu
from direct_cut_project import build,validate
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
ROOT=Path(__file__).resolve().parent

def measure(g):
    faces,meta=product_collar(g)
    n=3*(len(g.edges)+len(g.labels))
    rr=[];cc=[];vv=[]
    for j,word in enumerate(faces):
        for e,sgn in word:
            rr.append(e);cc.append(j);vv.append(sgn)
    D=coo_matrix((np.array(vv,dtype=float),(rr,cc)),shape=(n,len(faces))).tocsc()
    m=max(Counter(rr).values());p=max(map(len,faces))
    return D,meta,m,p

def rank_update(D,Q,eta,lamb):
    n,m=D.shape
    qids=np.asarray(sorted(Q),dtype=np.int64)
    allidx=np.arange(m)
    ridx=np.setdiff1d(allidx,qids)
    A=D[:,ridx];B=D[:,qids]
    M=(lamb*(A@A.T)+eta*eye(n,format='csc')).tocsc()
    sol=splu(M).solve(B.toarray())
    K=lamb*(B.T@sol)
    K=(K+K.T)*.5
    eig=np.linalg.eigvalsh(K)
    assert eig.min()>-1e-7
    return {'eta':float(eta),'lambda':float(lamb),'rank_Q':len(qids),
       'min_eigenvalue':float(eig.min()),'max_eigenvalue':float(eig.max()),
       'gaussian_free_energy':float(1.5*np.log1p(eig).sum()),
       'global_regularized_bound':float(1.5*len(qids)*np.log1p(lamb*28/eta)),
       'bianchi_regulator_free_bound':float(1.5*len(qids)*math.log(45)),
       'full_list_eigenvalues':eig.tolist()}

def main():
    g0,_=build(5.,0);seed=seed_support(g0)
    rows=[]
    for radius in (5.,6.5,8.,10.):
        g,ga=build(radius,0);validate(g,ga)
        D,meta,nu,p=measure(g);Q=Q_from_seed(g,seed)
        assert len(Q)==14 and p==4 and nu<=7
        diagnostics=[rank_update(D,Q,1.,lamb) for lamb in (1.,10.,300.)]
        diagnostics.extend(rank_update(D,Q,eta,1.) for eta in (1e-2,1e-4))
        for d in diagnostics:
            assert d['gaussian_free_energy']<=d['global_regularized_bound']+1e-6,d
            # Bianchi-fillability gives D_Q D_Q^T <=44 D_R D_R^T
            # hence K <=44 for eta>=0, lambda>=0
            assert d['max_eigenvalue']<=44+1e-6,d
            assert d['gaussian_free_energy']<=d['bianchi_regulator_free_bound']+1e-6,d
        row={'radius':radius,'spatial_rhombi':len(g.faces),'spacetime_links':D.shape[0],
             'spacetime_plaquettes':D.shape[1],'Q_count':len(Q),'max_incidence':nu,
             'experiments':diagnostics}
        rows.append(row)
        print('R',radius,'links',D.shape[0], 'Q',len(Q),
             'eta1 beta300',round(diagnostics[2]['gaussian_free_energy'],8),
             'eta1e-4 beta1',round(diagnostics[-1]['gaussian_free_energy'],8),flush=True)
    out={'model':'identity-tangent three-component real Gaussian gauge-field rank update, eta mass term on ALL links',
        'physical_SU2_theorem':False,'source':'direct Z5 Penrose rhombus disks x three periodic time intervals',
        'theorem_eta':'(3/2) logdet(I+lambda D_Q^T(eta I+lambda D_R D_R^T)^-1 D_Q) <=(3/2)|Q| log(1+lambda p nu/eta)',
        'theorem_fillable':'For Q14 with D_Q D_Q^T<=44 D_R D_R^T, same logdet <=(3/2)|Q|log(45), independent of eta, lambda and volume.',
        'important_caveat':'The uploaded exterior Schur form omits the local Gaussian normalization determinant. Neither it nor the full-link eta-normalized Gaussian determinant proves SU2 conditional Gibbs control.',
        'rows':rows}
    (ROOT/'gaussian_penrose_certificate.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':main()

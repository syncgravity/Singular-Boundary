#!/usr/bin/env python3
"""PF-I10 source graph spectra: sparse original-source matrices and SLQ validation.

Source script paper6_extend_local.py is an UNPUBLISHED USER SOURCE FILE kept private.
Derived code requires an explicitly provided --source-script; no replacements.
Results are finite scalar spectral functionals, NEVER a Yang--Mills gap theorem.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.linalg import eigh_tridiagonal
from scipy.sparse.csgraph import connected_components

SOURCE_SHA='86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da'
PHI=(1+math.sqrt(5))/2
TAVG=(1+PHI**-2)/2
EXPECTED_NS={7:1550,10:3042,12:4324,15:6980,18:9950,20:12207,23:16435,25:19260}
EXPECTED_E={7:None,10:None,12:None,15:None,18:None,20:None,23:None,25:38139}

def source_import(src):
    if hashlib.sha256(src.read_bytes()).hexdigest()!=SOURCE_SHA:
        raise ValueError('Unrecognized source script SHA-256; fail closed')
    sp=importlib.util.spec_from_file_location('source_research_code',str(src))
    x=importlib.util.module_from_spec(sp);sp.loader.exec_module(x);return x

def build_sparse(source,n_grid):
    """Build exactly the original source's retained vertex/edge/weight rules,
    but sparse; compare dense source at smallest n and trace oracle all sizes.
    """
    til=source.build_penrose_tiling(n_grid)
    retained=source.select_interior_vertices(til,.35)
    n=len(retained)
    if n!=EXPECTED_NS[n_grid]:raise AssertionError(('N mismatch',n_grid,n))
    source_labels=[til['multi_indices'][i] for i in retained]
    index={mi:i for i,mi in enumerate(source_labels)}
    if len(index)!=n:raise AssertionError('duplicate labels')
    ie=[];je=[];weight=[]
    for a,mi in enumerate(source_labels):
        for fam in range(5):
            x=list(mi);x[fam]+=1;other=index.get(tuple(x))
            if other is None:continue
            level=mi[fam];t=source.fibonacci_hopping(level)
            ie.append(a);je.append(other);weight.append(t)
    ii=np.asarray(ie,dtype=np.int64);jj=np.asarray(je,dtype=np.int64);ww=np.asarray(weight,dtype=float)
    A=sparse.coo_matrix((np.r_[ww,ww],(np.r_[ii,jj],np.r_[jj,ii])),shape=(n,n)).tocsr()
    L=sparse.diags(np.asarray(A.sum(axis=1)).ravel())-A
    ncomp,lab=connected_components(A,directed=False)
    if n_grid==25:assert len(ww)==38139
    return L, {'n':n,'edges':len(ww),'A_edges':int(np.count_nonzero(ww>.999999)),
        'B_edges':int(np.count_nonzero(ww<.999999)),
        'trace_over_n':float(2*np.sum(ww)/n),
        'components':int(ncomp),'components_sizes':sorted(np.bincount(lab).tolist(),reverse=True),
        'mean_degree':float(2*len(ww)/n),
        'matrix_sparsity_nnz':int(L.nnz),
        'source_sha256':SOURCE_SHA},A

def periodic_sparse(n,tavg=TAVG):
    q=math.isqrt(n); nper=q*q
    ii=[];jj=[]
    def add(a,b):ii.append(a);jj.append(b)
    for i in range(q):
        for j in range(q):
            x=i*q+j
            if j+1<q:add(x,x+1)
            if i+1<q:
                add(x,x+q)
                jj2=j+1 if i%2==0 else j-1
                if 0<=jj2<q:add(x,(i+1)*q+jj2)
    w=np.full(len(ii),tavg)
    A=sparse.coo_matrix((np.r_[w,w],(np.r_[ii,jj],np.r_[jj,ii])),shape=(nper,nper)).tocsr()
    L=sparse.diags(np.asarray(A.sum(axis=1)).ravel())-A
    assert len(ii)==(q-1)*(3*q-1)
    assert connected_components(A,directed=False)[0]==1
    return L,{'n':nper,'q':q,'edges':len(ii),'trace_over_n':float(2*len(ii)*tavg/nper),'components':1,'weight':tavg}


def slq_one(L,probe,steps,m2,source_trace=None,orth='none'):
    """Lanczos-Gauss for probe^T f(L+m²I) probe / N.
    Use localized tridiagonal eigendecomp; no QR reorth (which can produce
    ghost modes at long run). Test against dense and independent step settings.
    """
    n=L.shape[0]
    v=probe.astype(float);norm=float(np.linalg.norm(v));v/=norm
    vprev=np.zeros(n);beta=0.
    diag=[];off=[]
    for i in range(steps):
        q=L@v
        if i: q-=beta*vprev
        alpha=float(v@q)
        q-=alpha*v
        beta1=float(np.linalg.norm(q))
        diag.append(alpha)
        if beta1<1e-12:break
        if i<steps-1:off.append(beta1)
        vprev=v;v=q/beta1;beta=beta1
    d=np.array(diag);e=np.array(off)
    eig,vec=eigh_tridiagonal(d,e,check_finite=False)
    # The exact matrix is semidefinite; Jacobi error may yield numerical
    # eigenvalues slightly below zero (or true zero). Protect log/sqrt.
    if eig.min() < -1e-7:raise AssertionError(('negative quadrature eigenvalue',eig.min()))
    eig=np.maximum(eig,0.)
    w=(vec[0,:]**2); w/=w.sum()
    return {
     'sqrt':float(norm*norm/n*np.dot(w,np.sqrt(eig+m2))),
     'log':float(norm*norm/n*np.dot(w,np.log(eig+m2))),
     'relative_log':float(norm*norm/n*np.dot(w,np.log1p(eig/m2))),
     'first':float(norm*norm/n*np.dot(w,eig)),
     'second':float(norm*norm/n*np.dot(w,eig**2)),
    }


def slq(L,seed,probes=96,steps=130,m2=1e-4):
    rng=np.random.default_rng(seed)
    out=[];t0=time.monotonic()
    for k in range(probes):
        probe=rng.choice(np.array([-1.,1.]),size=L.shape[0])
        out.append(slq_one(L,probe,steps,m2))
    keys=out[0].keys()
    ans={k:{'mean':float(np.mean([x[k] for x in out])),
             'standard_error':float(np.std([x[k] for x in out],ddof=1)/math.sqrt(probes))} for k in keys}
    ans.update({'steps':steps,'probes':probes,'seed':seed,'duration_sec':time.monotonic()-t0})
    return ans

def ratio(a,b,f,nc,np_,ca,cb,m2):
    """Full and strictly-positive mode ratios. Only full-mode stochastic
    sampling is done; remove known zero contributions algebraically.
    """
    va=a[f]['mean'];vb=b[f]['mean'];ea=a[f]['standard_error'];eb=b[f]['standard_error']
    if f=='sqrt':zerocontr=math.sqrt(m2)
    elif f=='log':zerocontr=math.log(m2)
    elif f=='relative_log':zerocontr=0.
    else:zerocontr=m2 if f=='first' else None
    full=va/vb
    pos_a=(va*nc-ca*zerocontr)/(nc-ca)
    pos_b=(vb*np_-cb*zerocontr)/(np_-cb)
    pos=pos_a/pos_b
    semf=abs(full)*math.hypot(ea/va,eb/vb)
    semp=abs(pos)*math.hypot(ea*nc/(nc-ca)/pos_a,eb*np_/(np_-cb)/pos_b)
    return {'full':full,'full_se_independent_probe':semf,'positive_modes':pos,'positive_modes_se_independent_probe':semp}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-script',type=Path,required=True)
    ap.add_argument('--ngrids',type=int,nargs='+',default=[7,10,12,15,18,20,23,25])
    ap.add_argument('--steps',type=int,default=130)
    ap.add_argument('--probes',type=int,default=96)
    ap.add_argument('--m2',type=float,default=1e-4)
    ap.add_argument('--seed',type=int,default=84637)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--cache',type=Path,default=None)
    ap.add_argument('--only-build',action='store_true')
    args=ap.parse_args()
    source=source_import(args.source_script)
    rows=[];start=time.monotonic()
    for ngrid in args.ngrids:
        stamp=time.monotonic()
        if args.cache:
            args.cache.mkdir(parents=True,exist_ok=True)
            p=args.cache/f'PF_I10_source_{ngrid}.npz'
        else:p=None
        if p is not None and p.exists():
            q=np.load(p,allow_pickle=False)
            L=sparse.csr_matrix((q['data'],q['indices'],q['indptr']),shape=tuple(q['shape']))
            info=json.loads(str(q['meta'].item()))
            source_replayed=info['source_sha256']==SOURCE_SHA
            assert source_replayed
        else:
            L,info,A=build_sparse(source,ngrid)
            if p:
                np.savez_compressed(p,data=L.data,indices=L.indices,indptr=L.indptr,shape=np.asarray(L.shape),meta=json.dumps(info,sort_keys=True))
        P,per=periodic_sparse(info['n'])
        if ngrid==7:
            # Dense original source matrix, one time; exact matrix comparison
            til=source.build_penrose_tiling(ngrid)
            iv=source.select_interior_vertices(til,.35)
            dense,N,*_=source.build_coupled_z5_laplacian(til,iv)
            assert N==L.shape[0] and np.allclose(dense,L.toarray(),atol=1e-12)
            pdense,_=source.build_periodic_laplacian(N,TAVG)
            assert np.allclose(pdense,P.toarray(),atol=1e-12)
            del dense,pdense
        assert abs(float(L.diagonal().sum())/L.shape[0]-info['trace_over_n'])<1e-10
        assert abs(float(P.diagonal().sum())/P.shape[0]-per['trace_over_n'])<1e-10
        results={'Ngrid':ngrid,'QC':info,'periodic':per,'source_matrix_asymmetric_nnz':int((L-L.T).nnz),
                 'source_zero_rows':int(np.count_nonzero(np.abs(np.asarray(L.sum(axis=1)).ravel())>1e-10)),
                 'matrix_trace_Rminus1':(args.m2+info['trace_over_n'])/(args.m2+per['trace_over_n'])}
        if not args.only_build:
            qa=slq(L,args.seed+ngrid*10,probes=args.probes,steps=args.steps,m2=args.m2)
            pa=slq(P,args.seed+ngrid*10+1,probes=args.probes,steps=args.steps,m2=args.m2)
            ratios={f:ratio(qa,pa,f,info['n'],per['n'],info['components'],per['components'],args.m2) for f in ['sqrt','log','relative_log']}
            # Zeta prime ratio is ratio of mean logarithms
            # and Gamma relative is ratio of means of log1p(lambda/m2).
            results['slq']={'QC':qa,'periodic':pa,'ratios':ratios,
                'note':'SLQ stochastic, not exact eigenspectra. Errors are probe SE, not a deterministic Lanczos truncation bound.'}
        results['elapsed_s']=time.monotonic()-stamp
        rows.append(results)
        print(json.dumps({'Ngrid':ngrid,'N':info['n'],'E':info['edges'],'R(-1)':results['matrix_trace_Rminus1'],
           'sqrt_r':results.get('slq',{}).get('ratios',{}).get('sqrt',{}).get('positive_modes'),
           'elapsed_s':results['elapsed_s']}),flush=True)
        args.output.write_text(json.dumps({'m2':args.m2,'probes':args.probes,'steps':args.steps,
            'seed':args.seed,'source_sha256':SOURCE_SHA,'models':rows},indent=2,sort_keys=True)+'\n')
    print('done',time.monotonic()-start)

if __name__=='__main__':main()

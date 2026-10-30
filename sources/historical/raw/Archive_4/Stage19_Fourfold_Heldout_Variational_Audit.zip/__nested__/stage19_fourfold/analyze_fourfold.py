import io,json,zipfile,hashlib
from pathlib import Path
import numpy as np
ROOT=Path('/mnt/data'); OUT=ROOT/'stage19_fourfold'; OUT.mkdir(exist_ok=True)
SEEDS=(101,211,307,419); KINDS=('square','penrose'); N=490; T=20; D=4

def load():
    data={}; meta={}
    for geom in KINDS:
        for seed in SEEDS:
            name=f'{geom}_seed{seed}'; zpath=ROOT/f'{name}.zip'
            with zipfile.ZipFile(zpath) as z:
                entries=sorted(x for x in z.namelist() if x.endswith('.npz') and 'observations_' in x)
                assert len(entries)==245,(name,len(entries))
                arr=[]; sw=[]; cat=set(); anchors=set()
                for entry in entries:
                    with np.load(io.BytesIO(z.read(entry)),allow_pickle=False) as f:
                        arr.append(f['scalar'].astype(np.float64)); sw.extend(f['measured_sweeps'].tolist());cat.add(str(f['catalogue_sha256'])); anchors.add((int(f['accepted_anchors']),int(f['all_anchors'])))
                x=np.concatenate(arr,axis=0);sw=np.asarray(sw)
                assert x.shape==(N,T,D) and np.isfinite(x).all()
                assert np.array_equal(sw,np.arange(10110,15001,10))
                assert len(cat)==len(anchors)==1
                data[(geom,seed)]=x
                meta[name]={'observations':N,'sweep_first':int(sw[0]),'sweep_last':int(sw[-1]),'catalogue_sha256':next(iter(cat)),'anchors':list(next(iter(anchors))), 'sha256_zip':hashlib.sha256(zpath.read_bytes()).hexdigest()}
    return data,meta

def covs(x,max_t=7):
    # x:(configs,times,channels); global time- and configuration-average vacuum
    mu=x.mean(axis=(0,1)); xc=x-mu
    return np.array([np.einsum('nti,ntj->ij',xc,np.roll(xc,-t,axis=1))/(len(xc)*T) for t in range(max_t+1)])

def basis(train,method,rank=3):
    c=covs(train,7); c0=(c[0]+c[0].T)/2; eig,v=np.linalg.eigh(c0); order=np.argsort(eig)[::-1];eig=eig[order];v=v[:,order]
    floor=max(eig[0]*1e-8,1e-17)
    if method=='PCA':
        B=v[:,:rank]; selected=eig[:rank]; score=eig
    else:
        # whiten the leading three training C0 directions only; enforce a fixed cut, not determined by validation
        W=v[:,:rank]/np.sqrt(np.maximum(eig[:rank],floor))[None,:]
        g=(W.T@c[1]@W); g=(g+g.T)/2
        score,u=np.linalg.eigh(g); order=np.argsort(score)[::-1];score=score[order];u=u[:,order];B=W@u;selected=score[:rank]
    # standardize signs deterministically, and normalize coefficient vectors for report
    for j in range(B.shape[1]):
        k=np.argmax(np.abs(B[:,j])); B[:,j]*=np.sign(B[k,j]) if B[k,j] else 1
    return B,{'C0_eigenvalues':eig.tolist(),'C0_condition':float(eig[0]/max(eig[-1],floor)),'training_scores':np.asarray(score).tolist(),'coefficients':B.T.tolist()}

def projected_features(x,B,lim=7):
    y=x@B; m=y.mean(axis=1)
    prods=np.stack([np.mean(y*np.roll(y,-t,axis=1),axis=1) for t in range(lim+1)],axis=1)
    return m,prods

def bootstrap(m,p,block=20,reps=320,rng=None):
    n=len(m); k=m.shape[1]; out=np.empty((reps,p.shape[1],k)); offsets=np.arange(block)
    for b in range(reps):
        start=rng.integers(n,size=(n+block-1)//block)
        inds=((start[:,None]+offsets)%n).ravel()[:n]
        mean=m[inds].mean(axis=0); out[b]=p[inds].mean(axis=0)-mean[None,:]**2
    return out

def inspect(x,B,blocks=(10,20,40,80),reps=320,seed=111):
    m,p=projected_features(x,B); avg=p.mean(axis=0)-m.mean(axis=0)[None,:]**2
    result={'heldout_connected':avg.T.tolist(),'blocks':{}}
    for bl in blocks:
        samples=bootstrap(m,p,bl,reps,np.random.default_rng(seed+bl))
        se=samples.std(axis=0,ddof=1).T
        snr=np.divide(avg.T,se,out=np.full_like(se,np.nan),where=se>0)
        accepted=[{'component':j,'starting_t':t,'SNR':snr[j,t:t+3].round(3).tolist()} for j in range(B.shape[1]) for t in range(2,5) if np.all(snr[j,t:t+3]>=2)]
        result['blocks'][str(bl)]={'SE':se.tolist(),'SNR':snr.tolist(),'three_point_positive_2sigma':accepted,'best_snr_t2_6':float(np.nanmax(snr[:,2:7]))}
    return result

def main():
    data,meta=load(); result={'metadata':meta,'method':{'basis_selection':'PCA top 3 or rank-three C0-whitened C1 eigenvectors, fit exclusively on other three chains','validation':'each held-out seed examined individually; no held-out data enter basis selection','connected':'global vacuum subtraction on held-out gauge configurations, with periodic timeslice averaging','uncertainty':'circular moving-block bootstrap within held-out chain; block lengths 10,20,40,80; 320 resamples','scope':'not a physical glueball mass fit, nor independent cross-fold ensemble estimates'},'geometries':{}}
    for geom in KINDS:
        result['geometries'][geom]={}
        for held in SEEDS:
            tr=np.concatenate([data[(geom,s)] for s in SEEDS if s!=held]); te=data[(geom,held)]; fold={}
            for method in ('PCA','GEVP'):
                B,di=basis(tr,method);fold[method]={'training':di,'heldout':inspect(te,B,seed=held)}
            result['geometries'][geom][str(held)]=fold
            print(geom,held, [(meth,{b:len(fold[meth]['heldout']['blocks'][str(b)]['three_point_positive_2sigma']) for b in (10,20,40,80)}) for meth in fold],flush=True)
    (OUT/'RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False))
    summary={}
    for geom,folds in result['geometries'].items():
        summary[geom]={}
        for meth in ('PCA','GEVP'):
            summary[geom][meth]={'folds_passing_all_block_lengths':[], 'fold_block_passes':{}}
            for fold,dt in folds.items():
                blocks=dt[meth]['heldout']['blocks']; pairs={b:set((d['component'],d['starting_t']) for d in blocks[b]['three_point_positive_2sigma']) for b in blocks}
                stable=set.intersection(*pairs.values())
                summary[geom][meth]['fold_block_passes'][fold]={b:len(v) for b,v in pairs.items()}
                if stable: summary[geom][meth]['folds_passing_all_block_lengths'].append({'seed':fold,'stable':sorted(stable)})
    (OUT/'SUMMARY.json').write_text(json.dumps(summary,indent=2))
    print('SUMMARY',json.dumps(summary,indent=2),flush=True)
if __name__=='__main__': main()

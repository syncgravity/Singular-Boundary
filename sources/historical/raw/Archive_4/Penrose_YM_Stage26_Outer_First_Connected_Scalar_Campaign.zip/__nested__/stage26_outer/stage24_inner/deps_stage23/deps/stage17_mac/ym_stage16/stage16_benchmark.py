"""Paired direct-versus-exact SU(2) multihit Wilson benchmarking.

Small genuine interacting reference, different independent seeds. No mass fit.
All measurements use the faithful quaternion Wilson action convention.
"""
from pathlib import Path
import sys,json,time
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from stage16_multihit import catalog_square,multihit_batched,_direct_batched
from stage13_transport import small_square
from corrected_2p1_pilot import run_chain

def direct_batched(links,lat,sp,p,lag):
    return _direct_batched(links,sp['E'],sp['V'],lat['nt'],p['idx'],p['sign'],p['length'],p['u'],p['v'],0,lag,
      np.zeros((sp['V'],lag,4)),np.zeros(sp['V'],np.bool_))[0]

def path_subset(p,n):
    inds=np.unique(np.rint(np.linspace(0,len(p['u'])-1,n)).astype(int))
    return {k:v[inds] for k,v in p.items()}

def bench(n_per_chain=8,burn=300,thin=18,batch_sizes=(16,64,128),lags=(4,10)):
    sp,lat=small_square(nt=20,nx=8,ny=8,beta=3.5)
    paths=catalog_square(sp,nanchors=16)
    warm=np.zeros((lat['L'],4));warm[:,0]=1.
    p16=path_subset(paths,16)
    _=multihit_batched(warm,lat,sp,p16,lag=4)
    _=direct_batched(warm,lat,sp,p16,lag=4)
    # Compile the genuine SU(2) Metropolis kernel before timing outer sampling.
    _=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],999999,1,1,1,.95)
    out=[];timer=time.perf_counter()
    for seed in (101,211,307,419):
        start=time.perf_counter()
        links,_,_,err=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],seed,burn,n_per_chain*thin,thin,.95)
        generation=time.perf_counter()-start
        if err>1e-9:raise ValueError('Metropolis cache residual')
        for cfg,U in enumerate(links):
            for n in batch_sizes:
                p=path_subset(paths,n)
                for lag in lags:
                    t0=time.perf_counter();D=direct_batched(U,lat,sp,p,lag)
                    td=time.perf_counter()-t0
                    t1=time.perf_counter();Dm,M=multihit_batched(U,lat,sp,p,lag=lag)
                    tm=time.perf_counter()-t1
                    if not np.allclose(D,Dm,atol=1e-12):raise AssertionError('direct mismatch')
                    out.append({'seed':seed,'config':cfg,'batch':n,'lag':lag,'r':p['r'].tolist(),
                      'direct':D.tolist(),'multihit':M.tolist(),
                      'direct_seconds':td,'multihit_seconds':tm,
                      'outer_generation_seconds_per_config':generation/n_per_chain})
        print('completed independent chain',seed,'fields',len(links), 'seconds',round(generation,2),flush=True)
    data={'design':{'geometry':'8x8 square Nt20 beta_ref3.5','outer_chains':4,'n_outer_per_chain':n_per_chain,
       'burn':burn,'thin':thin,'batch_sizes':batch_sizes,'lags':lags,'shared_anchor_paths':True,
       'conditional_integration':'exact SU2 link first moments, no inner Markov chain',
       'equilibrium_certified':False,'mass_admitted':False,'string_tension_admitted':False},
       'rows':out,'elapsed_seconds':time.perf_counter()-timer}
    return data

def summarize(z):
    result=[]
    for n in z['design']['batch_sizes']:
     for lag in z['design']['lags']:
      rows=[r for r in z['rows'] if r['batch']==n and r['lag']==lag]
      D=np.array([r['direct'] for r in rows]);M=np.array([r['multihit'] for r in rows]);r=np.array(rows[0]['r'])
      # Primary comparison: equally weighted *complete path batch* observable
      d=D.mean(axis=1);m=M.mean(axis=1);cD=np.mean([v['direct_seconds'] for v in rows]);cM=np.mean([v['multihit_seconds'] for v in rows]);
      cOuter=np.mean([v['outer_generation_seconds_per_config'] for v in rows]);
      stdD=float(d.std(ddof=1));stdM=float(m.std(ddof=1));
      for rr in (1.,2.,3.,4.):
       ix=np.where(np.isclose(r,rr))[0]
       if not len(ix):continue
       di=D[:,ix].mean(axis=1);mi=M[:,ix].mean(axis=1)
       result.append({'batch':n,'lag':lag,'distance':rr,'npaths_distance':int(len(ix)),
        'direct_mean':float(di.mean()),'multihit_mean':float(mi.mean()),
        'direct_sd':float(di.std(ddof=1)),'multihit_sd':float(mi.std(ddof=1)),
        'raw_sd_ratio':float(di.std(ddof=1)/mi.std(ddof=1)) if mi.std(ddof=1)>0 else None,
        'paired_mean_difference':float((mi-di).mean()),
        'naive_paired_SE':float((mi-di).std(ddof=1)/np.sqrt(len(di))),
        'direct_measurement_seconds_all_paths':float(cD),
        'multihit_measurement_seconds_all_paths':float(cM),
        'generation_seconds_per_outer':float(cOuter),
        'measurement_only_variance_time_ratio':float(mi.var(ddof=1)*cM/(di.var(ddof=1)*cD)) if di.var(ddof=1)*cD>0 else None,
        'total_cost_variance_ratio':float(mi.var(ddof=1)*(cM+cOuter)/(di.var(ddof=1)*(cD+cOuter))) if di.var(ddof=1)>0 else None})
    return {'summary_rows':result,'n_outer':len({(r['seed'],r['config']) for r in z['rows']}),
        'decision':'EXPLORATORY: exact link integration validated, outer thermalization and fit plateaus not established'}
if __name__=='__main__':
    dat=bench();dat['summary']=summarize(dat)
    (HERE/'BENCHMARK.json').write_text(json.dumps(dat,indent=2))
    (HERE/'BENCHMARK_SUMMARY.json').write_text(json.dumps(dat['summary'],indent=2))
    print('TIME',dat['elapsed_seconds'])
    print('SUMMARY large batch',json.dumps([x for x in dat['summary']['summary_rows'] if x['batch']==128],indent=2))

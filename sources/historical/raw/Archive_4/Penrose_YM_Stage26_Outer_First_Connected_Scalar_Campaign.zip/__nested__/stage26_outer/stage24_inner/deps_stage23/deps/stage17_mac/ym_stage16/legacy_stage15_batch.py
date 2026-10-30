"""Batch SU(2) temporal transporter pilot; exploratory and NOT equilibrium-certified.

Freeze spatial boundary slices, sample conditional slabs, and share the same updated
field across several spatial paths and inner depths. Each path is contracted with
its own fixed spatial endpoint holonomies; depth results are nested prefixes.
"""
from pathlib import Path
import sys,time,json
import numpy as np
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'ym_stage13'))
from stage13_transport import (small_square, time_line,paired_matrix,spatial_holonomy,
                               contract_paired,direct_rectangle)
from stage6_multilevel import slab_partition,assert_slab_factorization,condition_sweeps,update_sweeps_inplace,plaquettes
from corrected_2p1_pilot import run_chain

DEPTHS=(8,16,32)

def paths_x(sp, lengths=(1,2,3)):
    """Physical straight x paths on unwrapped 5x5 square torus, no winding."""
    edges=np.asarray(sp['edges']);vec=np.asarray(sp['edge_vectors']);out=[]
    for length in lengths:
        start=0;cur=start;path=[];signs=[]
        for _ in range(length):
            choices=[]
            for e,(a,b) in enumerate(edges):
                if a==cur and np.allclose(vec[e],[1,0]):choices.append((e,1,int(b)))
                elif b==cur and np.allclose(-vec[e],[1,0]):choices.append((e,-1,int(a)))
            if len(choices)!=1:raise ValueError(f'nonunique straight x edge at {cur}: {choices}')
            e,s,nxt=choices[0];path.append(e);signs.append(s);cur=nxt
        out.append({'length':length,'u':start,'v':cur,'path':path,'sg':signs,'physical_r':float(length)})
    return out

def batched_measure(outer,lat,sp,paths,depths=DEPTHS,warm=32,spacing=2,slab=5,seed=11):
    depths=tuple(sorted(set(depths)));N=depths[-1]
    E,V,nt=sp['E'],sp['V'],lat['nt'];assert nt>=3*slab and nt%slab==0
    locked,allowed,group,_=slab_partition(nt,E,V,slab)
    assert_slab_factorization(lat,group,locked,nt,E,V,slab)
    init=outer[locked].copy()
    t0=time.perf_counter()
    state,_,init_err=condition_sweeps(outer,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],allowed,warm,.95,seed)
    pf=plaquettes(state,lat['fi'],lat['sg'])
    sumQ=np.zeros((len(paths),2,4,4),complex)
    boundary=[(spatial_holonomy(outer,E,p['path'],p['sg'],0),
               spatial_holonomy(outer,E,p['path'],p['sg'],2*slab)) for p in paths]
    results={};spent={}
    for k in range(1,N+1):
        update_sweeps_inplace(state,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],allowed,spacing,.95)
        for i,p in enumerate(paths):
            for j,t in enumerate((0,slab)):
                A=time_line(state,nt,E,V,p['u'],t,slab)
                B=time_line(state,nt,E,V,p['v'],t,slab)
                sumQ[i,j]+=paired_matrix(B,A)
        if k in depths:
            results[k]=[float(contract_paired(boundary[i][0],(sumQ[i,0]/k)@(sumQ[i,1]/k),boundary[i][1])) for i in range(len(paths))]
            spent[k]=time.perf_counter()-t0
    resid=float(np.max(np.abs(plaquettes(state,lat['fi'],lat['sg'])-pf)))
    assert np.array_equal(init,state[locked])
    assert max(init_err,resid)<1e-9
    return {'values':results,'seconds':spent,'cache_error':resid,'frozen':True}

def benchmark(nouter=6,burn=200,thin=12,depths=DEPTHS):
    sp,lat=small_square();paths=paths_x(sp);rows=[];beg=time.perf_counter()
    for ci,seed in enumerate((101,211,307,419)):
        outer,_,_,err=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],seed,burn,nouter*thin,thin,.95)
        for k,U in enumerate(outer):
            a=time.perf_counter()
            direct=[direct_rectangle(U,lat['nt'],sp['E'],sp['V'],p['u'],p['v'],p['path'],p['sg'],0,10) for p in paths]
            direct_t=time.perf_counter()-a
            b=batched_measure(U,lat,sp,paths,depths=depths,seed=50000+ci*1000+k)
            rows.append({'chain':ci,'seed':seed,'index':k,'direct':direct,'direct_seconds':direct_t,
                         'conditional':{str(d):b['values'][d] for d in depths},
                         'conditional_seconds':{str(d):b['seconds'][d] for d in depths},
                         'cache_error':b['cache_error']})
        print('stage15 chain',seed,'done',flush=True)
    return {'design':{'n_outer_chains':4,'n_outer_per_chain':nouter,'depths':depths,'inner_warm':32,'inner_spacing':2,'paths':paths,'outer_burn':burn,'outer_thin':thin,'physical_admission':False,'conditional_prefixes_shared':True},'rows':rows,'elapsed_seconds':time.perf_counter()-beg}

def summary(data):
    rows=data['rows']; P=len(data['design']['paths']);out={'n_outer':len(rows),'path_results':[]}
    for j in range(P):
        D=np.array([r['direct'][j] for r in rows]);entry={'length':data['design']['paths'][j]['physical_r'],'direct_mean':float(D.mean()),'direct_sd':float(D.std(ddof=1)), 'depths':{}}
        for depth in data['design']['depths']:
            C=np.array([r['conditional'][str(depth)][j] for r in rows]);cost=np.mean([r['conditional_seconds'][str(depth)] for r in rows]);dt=np.mean([r['direct_seconds'] for r in rows]);
            entry['depths'][str(depth)]={'mean':float(C.mean()),'sd':float(C.std(ddof=1)),
               'raw_sd_ratio':float(D.std(ddof=1)/C.std(ddof=1)) if C.std(ddof=1)>0 else None,
               'mean_diff':float((C-D).mean()),'paired_diff_naive_SE':float((C-D).std(ddof=1)/np.sqrt(len(D))),
               'elapsed_seconds_per_outer_for_all_paths':float(cost),
               'cost_ratio_conditional_to_direct_all_paths':float(cost/dt) if dt else None,
               'variance_time_ratio_conditional_to_direct':float(C.var(ddof=1)*cost/(D.var(ddof=1)*dt)) if D.var(ddof=1)>0 else None}
        out['path_results'].append(entry)
    return out

if __name__=='__main__':
    obj=benchmark();obj['summary']=summary(obj)
    (Path(__file__).parent/'BENCHMARK.json').write_text(json.dumps(obj,indent=2))
    print(json.dumps(obj['summary'],indent=2))

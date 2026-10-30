"""Stage14 exploratory paired square-torus transporter benchmark. Not production spectroscopy."""
import json,time,sys,os
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'ym_stage13'))
from stage13_transport import small_square,conditioned_rectangle,direct_rectangle
from corrected_2p1_pilot import run_chain

SEEDS=(101,211,307,419)
DEPTHS=(8,32)

def benchmark(nouter=12,burn=240,thin=12):
    sp,lat=small_square()
    E,V,nt=sp['E'],sp['V'],lat['nt']
    results=[];begin=time.perf_counter();cache=[]
    for ichain,seed in enumerate(SEEDS):
        t0=time.perf_counter()
        outer,_,_,err=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],seed,burn,nouter*thin,thin,.95)
        cache.append(float(err))
        for k,u in enumerate(outer):
            tdirect=time.perf_counter()
            direct=direct_rectangle(u,nt,E,V,0,1,[0],[1],0,10)
            directtime=time.perf_counter()-tdirect
            row={'chain':ichain,'seed':seed,'index':k,'direct':float(direct),'direct_seconds':directtime}
            for d in DEPTHS:
                t=time.perf_counter()
                r=conditioned_rectangle(u,lat,sp,0,1,[0],[1],slab=5,inner=d,warm=32,spacing=2,seed=100000+ichain*10000+k*100+d)
                row[f'conditional_{d}']=float(r['conditional'])
                row[f'inner_direct_{d}']=float(r['inner_direct_mean'])
                row[f'seconds_{d}']=time.perf_counter()-t
                assert r['frozen_exact'] and r['cache_error']<1e-9
            results.append(row)
        print('completed chain',seed,'elapsed',round(time.perf_counter()-t0,2),flush=True)
    return {'design':{'geometry':'5x5 square, Nt15, beta3.5','outer_chains':4,'outer_per_chain':nouter,'burn':burn,'thin':thin,'depths':DEPTHS,'inner_warm':32,'inner_spacing':2,'t_rectangle':10,'physical_admission':False},'rows':results,'max_outer_cache_error':max(cache),'elapsed_seconds':time.perf_counter()-begin}

def describe(data):
    x=data['rows']; d=np.array([r['direct'] for r in x]);summary={'n_outer':len(x),'direct_mean':float(d.mean()),'direct_sd':float(d.std(ddof=1)),'elapsed_seconds':data['elapsed_seconds']}
    for depth in DEPTHS:
        c=np.array([r[f'conditional_{depth}'] for r in x]);times=np.array([r[f'seconds_{depth}'] for r in x]);diff=c-d
        summary[str(depth)]={'conditional_mean':float(c.mean()),'conditional_sd':float(c.std(ddof=1)),
             'raw_sd_ratio':float(d.std(ddof=1)/c.std(ddof=1)),
             'mean_difference':float(diff.mean()),'paired_diff_se_naive':float(diff.std(ddof=1)/np.sqrt(len(diff))),
             'mean_time_seconds':float(times.mean()),'direct_time_seconds':float(np.mean([r['direct_seconds'] for r in x])),
             'cost_adjusted_ratio_excluding_outer_cost':float((d.var(ddof=1)*np.mean([r['direct_seconds'] for r in x]))/(c.var(ddof=1)*times.mean()))}
    return summary

if __name__=='__main__':
    obj=benchmark();obj['summary']=describe(obj)
    (HERE/'BENCHMARK.json').write_text(json.dumps(obj,indent=2))
    print(json.dumps(obj['summary'],indent=2))

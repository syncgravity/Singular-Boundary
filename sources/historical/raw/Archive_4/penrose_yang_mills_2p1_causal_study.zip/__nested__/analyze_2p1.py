"""Aggregates independent chains. Statistical errors conditional on the stated blocks."""
import json, math, pathlib
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parent
files={'M5_geometry':'study_2p1_M5.json','M8_geometry':'study_2p1_M8.json',
       'M5_uniform':'study_2p1_M5_uniform.json','M8_uniform':'study_2p1_M8_uniform.json',
       'M5_shuffled':'study_2p1_M5_shuffled.json'}

def avg(vals):
    xs=np.array([x[0] for x in vals],float)
    s=np.array([x[1] for x in vals],float)
    m=float(xs.mean());se=float(np.sqrt(np.sum(s*s))/len(xs))
    return {'mean':m,'blocked_se':se,'between_chain_se':float(xs.std(ddof=1)/np.sqrt(len(xs))) if len(xs)>1 else None}

def scalar_corr(r,k):return [r['correlator'][k],r['correlator_se_jackknife'][k]]

def combine(j):
    out={'M':j['M'],'physical_area':j['physical_area'],'time_spacing':j['time_spacing'],
         'nt':j['nt'],'weight_mode':j.get('weight_mode','geometric'),
         'normalize_mean_couplings':j.get('normalize_mean_couplings'),
         'geometry':j['geometry'],'betas':{}}
    for beta in sorted(set(x['beta_ref'] for x in j['results'])):
        dat={}
        for geom in ['penrose','square']:
            rs=[r for r in j['results'] if r['geometry']==geom and r['beta_ref']==beta]
            if not rs:continue
            d={k:avg([r[k] for r in rs]) for k in ['spatial_plaquette','temporal_plaquette','action_per_plaquette']}
            d['rectangles']=[avg([r['rectangular_wilson_loops'][k] for r in rs]) for k in range(j['nt']//2)]
            d['scalar_connected_correlators']=[avg([scalar_corr(r,k) for r in rs]) for k in range(j['nt']//2+1)]
            # For the earliest run, jackknife ratios were not archived; the point estimate
            # can still be calculated but the covariance-aware standard error is unknown.
            energies=[]
            for k in range(j['nt']//2-1):
                x=d['rectangles'][k]['mean'];y=d['rectangles'][k+1]['mean']
                energy=-math.log(y/x)/j['time_spacing'] if x>0 and y>0 else None
                if all('rectangle_effective_static_energies' in r for r in rs):
                    e=avg([r['rectangle_effective_static_energies'][k] for r in rs])
                else:
                    e={'mean':energy,'blocked_se':None,'between_chain_se':None}
                energies.append(e)
            d['effective_static_energies']=energies
            d['n_chains']=len(rs)
            d['seed_list']=[r['seed'] for r in rs]
            d['acceptance_mean']=float(np.mean([r['acceptance'] for r in rs]))
            d['max_cache_error']=float(max(r['max_cache_error'] for r in rs))
            if all('autocorrelation' in r for r in rs):
                d['autocorrelation_each_chain']=[r['autocorrelation'] for r in rs]
            dat[geom]=d
        if 'penrose' in dat and 'square' in dat:
            diffs={}
            for key in ['spatial_plaquette','temporal_plaquette','action_per_plaquette']:
                p=dat['penrose'][key];s=dat['square'][key]
                delta=p['mean']-s['mean'];se=math.hypot(p['blocked_se'],s['blocked_se'])
                diffs[key]={'difference':float(delta),'blocked_se':se,'z_naive':float(delta/se)}
            for k in range(j['nt']//2):
                p=dat['penrose']['rectangles'][k];s=dat['square']['rectangles'][k]
                delta=p['mean']-s['mean'];se=math.hypot(p['blocked_se'],s['blocked_se'])
                diffs[f'rectangle_lag_{k+1}']={'difference':float(delta),'blocked_se':se,'z_naive':float(delta/se)}
            dat['penrose_minus_square']=diffs
        out['betas'][str(beta)]=dat
    return out

def main():
    agg={}
    for key,name in files.items():
        path=ROOT/name
        if path.exists():agg[key]=combine(json.loads(path.read_text()))
    (ROOT/'study_2p1_aggregate.json').write_text(json.dumps(agg,indent=2))
    for key,j in agg.items():
        print(key)
        for beta,run in j['betas'].items():
            d=run.get('penrose_minus_square',{})
            print('  beta',beta,' '.join('%s %+0.6f ± %.6f (%+.1f sigma)'%(k,x['difference'],x['blocked_se'],x['z_naive']) for k,x in d.items() if k in ['spatial_plaquette','temporal_plaquette','rectangle_lag_2']))
            for geom in ['penrose','square']:
                if geom in run:
                    energies=run[geom]['effective_static_energies']
                    print('   ',geom,'Eτ1:2',energies[0], 'Eτ2:3',energies[1],
                          'C1',run[geom]['scalar_connected_correlators'][1])
if __name__=='__main__':main()

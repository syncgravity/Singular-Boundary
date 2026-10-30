"""Stage 5: longer-time square SU(2) gauge ensemble with fail-closed spectroscopy.

The square torus is a reference/regression target. No M5 geometry claim is made.
Saved configurations retain all SU(2) links in (spatial times, temporal times) order.
Run generator with --generate, analyze with --analyze (or both).
"""
import argparse, json, time, hashlib
from pathlib import Path
import numpy as np
from stage3_periodic_pilot import square_torus, periodic_paths
from stage2_ym_calibration import assemble
from corrected_2p1_pilot import run_chain, measure_wilson_paths
from stage4_smearing_flux import (staple_structure,ape_spatial,winding_paths,measure_winding,
 measure_scalar_groups,square_scalar_basis,connected_corr,gevp_diagnostics)

AREA=61.70899448216604
REFERENCE_FACES=188
SEEDS=(101,211,307,419)
LEVELS=(0,2,6)
ALPHA=.4

def setup(nt=20,beta=3.5):
    sp=square_torus(13,14,AREA)
    a=(AREA/REFERENCE_FACES)**.5
    lat,cal=assemble(sp,nt,beta,a,a)
    paths=periodic_paths(sp,max_steps=4,per_size=20)
    flux=winding_paths(sp,nanchors=24,max_steps=85)
    scalar=square_scalar_basis(sp)
    staple=staple_structure(sp,'inverse_area')
    return sp,lat,cal,paths,flux,scalar,staple

def generator(out,nt=20,beta=3.5,burn=300,steps=1200,thin=5):
    if nt<16 or steps%thin: raise ValueError('nt must be >=16 and steps divisible by thin')
    out=Path(out);out.mkdir(exist_ok=True,parents=True)
    sp,lat,cal,paths,flux,scalar,staple=setup(nt,beta)
    metadata={'study':'square reference spectroscopy pilot, NOT Penrose causal comparison',
       'geometry':'square 13x14 torus','nt':nt,'beta_ref':beta,'area':AREA,
       'a_ref':float((AREA/REFERENCE_FACES)**.5),'physical_T':float(nt*(AREA/REFERENCE_FACES)**.5),
       'nx':13,'ny':14,'V':sp['V'],'E':sp['E'],'F':sp['F'],'spatial_kind':sp['spatial_kind'],
       'graph_hash':sp['graph_hash'],'spatial_beta_range':cal['spatial_beta_range'],
       'temporal_beta_range':cal['temporal_beta_range'],'tree_level_response_eigenvalues':cal['eig'].tolist(),
       'seeds':SEEDS,'burn':burn,'steps':steps,'thin':thin,'n_saved_per_chain':steps//thin,
       'angle':.95,'smearing_levels':LEVELS,'smearing_alpha':ALPHA,
       'W_max_lag':nt//2,'n_paths':len(paths['length']),
       'winding_paths':len(flux['length']),'basis_names':['plaquette','rectangle_1x2','square_2x2'],
       'diagnostic_policy':'No mass or sigma without 4-chain Rhat<1.01, ESS>=400, stable >=3-time fit with covariance and volume controls.'}
    (out/'settings.json').write_text(json.dumps(metadata,indent=2))
    (out/'paths.json').write_text(json.dumps(paths['meta'],indent=2))
    (out/'winding_paths.json').write_text(json.dumps(flux['meta'],indent=2))
    for seed in SEEDS:
        t0=time.monotonic()
        print(f'GENERATE chain {seed}: nt={nt}, {steps//thin} frames, {lat["L"]} links',flush=True)
        links,actions,accept,err=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],
                      seed,burn,steps,thin,.95)
        if err>1e-9:raise AssertionError(f'Plaquette cache error={err}')
        path=out/f'configs_seed{seed}.npz'
        np.savez_compressed(path,links=links,actions=actions)
        log={'seed':seed,'frames':len(links),'acceptance':float(accept),'action_mean':float(actions.mean()),
          'action_std':float(actions.std(ddof=1)),'cache_error':float(err),
          'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
          'elapsed_seconds':float(time.monotonic()-t0)}
        (out/f'chain_seed{seed}.json').write_text(json.dumps(log,indent=2))
        print(f'RECORDED seed {seed}, acc {accept:.3f}, elapsed {log["elapsed_seconds"]:.1f}s',flush=True)

def measure(out,nt=None,levels=LEVELS):
    out=Path(out)
    meta=json.loads((out/'settings.json').read_text())
    if nt is None:nt=int(meta['nt'])
    sp,lat,cal,paths,flux,scalar,staple=setup(nt,meta['beta_ref'])
    for seed in SEEDS:
        file=out/f'configs_seed{seed}.npz'
        if not file.is_file():raise FileNotFoundError(file)
        z=np.load(file);links=z['links']
        if links.shape!=(meta['n_saved_per_chain'],nt*(sp['E']+sp['V']),4):
            raise ValueError(f'Invalid saved gauge shape for seed {seed}: {links.shape}')
        obs=np.empty((len(links),nt,len(levels)*3))
        torelon=np.empty((len(links),nt,len(levels)*2))
        rect=np.empty((len(links),len(levels),len(paths['length']),nt//2))
        for i,u in enumerate(links):
            for j,l in enumerate(levels):
                v=u if l==0 else ape_spatial(u,nt,sp['E'],*staple,ALPHA,l)
                obs[i,:,3*j:3*j+3]=measure_scalar_groups(v,nt,sp['E'],scalar['idx'],scalar['sign'],scalar['length'],scalar['kind'])
                torelon[i,:,2*j:2*j+2]=measure_winding(v,nt,sp['E'],flux['idx'],flux['sign'],flux['length'],flux['direction'])
                rect[i,j,:,:]=measure_wilson_paths(v,nt,sp['E'],sp['V'],paths['idx'],paths['sign'],paths['length'],
                                        paths['u'],paths['v'],nt//2)
            if (i+1)%60==0:print('MEASURE',seed,i+1,'/',len(links),flush=True)
        np.savez_compressed(out/f'obs_seed{seed}.npz',operators=obs,flux=torelon,wilson=rect)
        print('MEASURED',seed,flush=True)

def block_indices(nchains,per,block,B,seed=20261011):
    if per%block:raise ValueError('block must divide frames per chain')
    ids=np.arange(nchains*per).reshape(nchains,per//block,block)
    rng=np.random.default_rng(seed)
    for _ in range(B):
        kk=rng.integers(0,per//block,(nchains,per//block))
        yield ids[np.arange(nchains)[:,None],kk].reshape(-1)

def bootstrap_correlators(arr,block=10,B=250):
    """Cache per-config raw time products; resample whole gauge frames in chains.

    This exactly matches connected_corr for each resample (sample-mean VEV
    subtraction) but avoids recomputing all time-lag products B times.
    """
    arr=np.asarray(arr,np.float64)
    n,nt,nop=arr.shape;per=n//4
    if n!=per*4:raise ValueError('expected four chains')
    raw=np.empty((n,nt//2+1,nop,nop),float)
    for tau in range(nt//2+1):
        z=np.einsum('bti,btj->bij',arr,np.roll(arr,-tau,axis=1))/nt
        raw[:,tau]=(z+z.transpose(0,2,1))/2
    means=arr.mean(axis=1)
    C=raw.mean(axis=0)-np.outer(means.mean(axis=0),means.mean(axis=0))[None,:,:]
    samples=[]
    for ii in block_indices(4,per,block,B):
        mu=means[ii].mean(axis=0)
        samples.append(raw[ii].mean(axis=0)-np.outer(mu,mu)[None,:,:])
    return C,np.array(samples)

def diagnostic_az(data):
    # Four chains, columns represent separate scalars; check mixing and bulk/tail sample size.
    import arviz as az
    vals=np.asarray(data)
    assert vals.shape[0]==4
    tab=[]
    for j in range(vals.shape[-1]):
        a=vals[:,:,j]
        try:
            r=float(az.rhat(a));be=float(az.ess(a,method='bulk'))
            te=float(az.ess(a,method='tail',prob=(.05,.95)))
        except Exception:
            r=be=te=float('nan')
        tab.append({'index':j,'rhat':r if np.isfinite(r) else None,
                    'ess_bulk':be if np.isfinite(be) else None,
                    'ess_tail':te if np.isfinite(te) else None,
                    'pass':bool(np.isfinite(r) and r<1.01 and min(be,te)>=400)})
    return tab

def analyze(out,block=10,B=250):
    out=Path(out);meta=json.loads((out/'settings.json').read_text());nt=meta['nt']
    obs=[];flux=[];wilson=[];actions=[]
    for seed in SEEDS:
        k=np.load(out/f'obs_seed{seed}.npz')
        obs.append(k['operators']);flux.append(k['flux']);wilson.append(k['wilson'])
        actions.append(np.load(out/f'configs_seed{seed}.npz')['actions'])
    ops=np.concatenate(obs);flo=np.concatenate(flux);w=np.concatenate(wilson)
    nper=ops.shape[0]//4
    if not(nper%block==0 and ops.shape[1]==nt):raise ValueError('wrong block or data shapes')
    C,bootC=bootstrap_correlators(ops,block,B)
    F,bootF=bootstrap_correlators(flo,block,B)
    seC=bootC.std(axis=0,ddof=1);seF=bootF.std(axis=0,ddof=1)
    cc=np.diag(C[2]);sce=np.diag(seC[2]);ff=np.diag(F[2]);sfe=np.diag(seF[2])
    scalar_snr=np.divide(cc,sce,out=np.full(len(cc),np.nan),where=sce>0)
    flux_snr=np.divide(ff,sfe,out=np.full(len(ff),np.nan),where=sfe>0)
    from scipy.linalg import eigvalsh
    percent_c2=float(np.mean(np.all(np.linalg.eigvalsh(bootC[:,2,:,:])>0,axis=1)))
    scalar_diag={'C2':cc.tolist(),'C2_bootstrap_SE':sce.tolist(), 'C2_SNR':scalar_snr.tolist(),
         'C2_min_eigen':float(eigvalsh(C[2]).min()),'C1_min_eigen':float(eigvalsh(C[1]).min()),
         'bootstrap_fraction_C2_full_positive':percent_c2,'gevp':gevp_diagnostics(C)}
    ref={}
    paths=json.loads((out/'paths.json').read_text())
    pr=np.array([x['physical_r'] for x in paths]);edges=np.array([x['edges'] for x in paths])
    bins=np.arange(.5,4.6,.5)
    for lo,hi in zip(bins[:-1],bins[1:]):
        take=np.where((pr>=lo)&(pr<hi))[0]
        if len(take)==0:continue
        # The path-mean covariance is preserved within each gauge config.
        pair=w[:,:,take,:].mean(axis=2)
        boot=np.array([pair[ii].mean(axis=0) for ii in block_indices(4,nper,block,B)])
        means=pair.mean(axis=0);errors=boot.std(axis=0,ddof=1)
        ref[f'{lo:g}-{hi:g}']={'r':float(pr[take].mean()),'n_paths':len(take),
                'mean_by_smearing':means.tolist(),'bootstrap_SE':errors.tolist(),
                'W_t4_SNR_by_smearing':(means[:,3]/np.maximum(errors[:,3],1e-30)).tolist(),
                'physical_potential_fit_admitted':False}
    # Action, volume-averaged scalar channels, and W(t=1) monitor autocorrelation.
    act=np.array(actions)[:,:,None];opchain=np.array([o.mean(axis=1) for o in obs]);
    wmon=np.stack([np.mean(x[:,:,:,0],axis=2) for x in wilson])
    scalar_byt=np.stack(obs)
    flux_byt=np.stack(flux)
    scalar_g2=np.mean(scalar_byt*np.roll(scalar_byt,-2,axis=2),axis=2)
    flux_g2=np.mean(flux_byt*np.roll(flux_byt,-2,axis=2),axis=2)
    monitored=np.concatenate((act,opchain,wmon,scalar_g2,flux_g2),axis=2)
    diag=diagnostic_az(monitored)
    # A loop-average has no definite physical continuum meaning without mass extraction,
    # so correlations and weak-field calibration stay diagnostic only.
    summary={'source':'Stage 5 square reference nt=20 measured at fixed beta; no modelset comparison',
       'settings':meta,'n_configs':len(ops),'blocked_bootstrap_replicates':B,'block_size':block,
       'monitoring':{'n_observables':len(diag),'all_pass':bool(all(a['pass'] for a in diag)),
                     'observables':diag,'explanation':'index 0=action; 1:10=9 scalar means; 10:13=3 W(t=1) smearing averages; 13:22=9 raw scalar G(2) diagonal products; 22:28=6 raw flux G(2) diagonal products'},
       'scalar':scalar_diag,
       'winding':{'C2':ff.tolist(),'C2_bootstrap_SE':sfe.tolist(),'C2_SNR':flux_snr.tolist(),
                   'C2_min_eigen':float(eigvalsh(F[2]).min()),
                   'separate_source_length_m':None,'winding_period_lengths':[float(np.linalg.norm(np.array([[1,0],[0,1]])[:,j])) for j in range(2)],
                   'energy_fit_admitted':False,'sigma_fit_admitted':False},
       'physical_W_bins':ref,
       'admission':{'mass':'REJECT: no validated >=3-separation correlated multi-exponential plateau and full precision gate',
                    'string_tension':'REJECT: no stable torelon energy and finite-length string corrections / long-range potential',
                    'ratio':'REJECT: numerator or denominator not admitted',
                    'continuum':'REJECT: one beta only; no continuum trajectory',
                    'Penrose_causal':'REJECT: square only; M5 fails geometry admission'}}
    # Correct period lengths from stage3 builder instead of template placeholder.
    sp,*_=setup(nt,meta['beta_ref'])
    summary['winding']['winding_period_lengths']=[float(np.linalg.norm(sp['periods'][:,j])) for j in range(2)]
    (out/'stage5_analysis.json').write_text(json.dumps(summary,indent=2,allow_nan=False))
    np.savez_compressed(out/'stage5_correlator_matrices.npz',C_scalar=C,C_flux=F,SE_scalar=seC,SE_flux=seF,
             bootstrap_C_scalar=bootC,bootstrap_C_flux=bootF)
    print('ANALYZED',len(ops),'frames, mixing pass=',summary['monitoring']['all_pass'],
          'scalar C2 SNR:',np.round(scalar_snr,2),'flux C2 SNR:',np.round(flux_snr,2),flush=True)
    return summary

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',default='outputs');ap.add_argument('--generate',action='store_true')
    ap.add_argument('--measure',action='store_true');ap.add_argument('--analyze',action='store_true')
    ap.add_argument('--nt',type=int,default=20);ap.add_argument('--beta',type=float,default=3.5)
    ap.add_argument('--burn',type=int,default=300);ap.add_argument('--steps',type=int,default=1200)
    ap.add_argument('--thin',type=int,default=5);ap.add_argument('--block',type=int,default=10)
    ap.add_argument('--bootstrap',type=int,default=220)
    a=ap.parse_args()
    if not (a.generate or a.measure or a.analyze):ap.error('select a phase')
    if a.generate:generator(a.out,a.nt,a.beta,a.burn,a.steps,a.thin)
    if a.measure:measure(a.out)
    if a.analyze:analyze(a.out,a.block,a.bootstrap)
if __name__=='__main__':main()

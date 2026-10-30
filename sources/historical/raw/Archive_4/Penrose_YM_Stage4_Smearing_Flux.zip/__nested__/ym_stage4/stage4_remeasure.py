"""Deterministic Stage 4 remeasurement on unmodified Stage 3 gauge configurations.

Usage: OPENBLAS_NUM_THREADS=1 python stage4_remeasure.py \
 --stage3 /mnt/data/ym_stage3/outputs --out outputs --per-chain 50
The interpretation is explicitly fail-closed; no m0++, sigma or continuum ratio fits.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np
from stage3_periodic_pilot import square_torus,_basis,periodic_paths
from stage2_rational_torus import build_torus
from stage4_smearing_flux import (staple_structure,ape_spatial,winding_paths,
   measure_winding,measure_scalar_groups,connected_corr,centered_flux_corr,gevp_diagnostics,square_scalar_basis)
from corrected_2p1_pilot import measure_wilson_paths


def resample_blocks(nchains,per_chain,block,B,seed=20261011):
    if per_chain%block:raise ValueError('block must divide per-chain samples')
    rng=np.random.default_rng(seed); inds=np.arange(nchains*per_chain).reshape(nchains,per_chain//block,block)
    for _ in range(B):
        pick=rng.integers(0,per_chain//block,(nchains,per_chain//block))
        yield inds[np.arange(nchains)[:,None],pick].reshape(-1)


def _finite_stat(obs,B=250,block=5):
    C=connected_corr(obs)
    boot=np.array([connected_corr(obs[ii]) for ii in resample_blocks(4,len(obs)//4,block,B)])
    se=np.std(boot,axis=0,ddof=1)
    snr=np.diag(C[2])/np.maximum(np.diag(se[2]),1e-30)
    pos=np.mean([np.min(np.linalg.eigvalsh(c[2]))>0 for c in boot])
    return C,boot,dict(diagonal_t2=np.diag(C[2]).tolist(),diagonal_t2_SE=np.diag(se[2]).tolist(),
                       diagonal_t2_SNR=snr.tolist(),
                       C1_min_eigen=float(np.linalg.eigvalsh(C[1]).min()),
                       C2_min_eigen=float(np.linalg.eigvalsh(C[2]).min()),
                       bootstrap_fraction_positive_C2=float(pos),
                       gevp=gevp_diagnostics(C),
                       three_point_plateau=False, mass_admitted=False)


def run(name,sp,src,out,per_chain,levels,alpha=.4,block=5,B=250):
    p=Path(src)/f'{name}_configs.npz';z=np.load(p)
    seeds=sorted(z.files,key=lambda s:int(s.split('_')[-1]))
    if len(seeds)!=4:raise ValueError('expected 4 independent Stage3 chains')
    links=np.concatenate([z[k][:per_chain] for k in seeds])
    nt=8;E=sp['E'];V=sp['V'];n=len(links)
    if n!=4*per_chain:raise ValueError('missing Stage3 configurations')
    if links.shape[1] != nt*(E+V):raise ValueError('geometry mismatch')
    staple=staple_structure(sp,'inverse_area')
    winding=winding_paths(sp,nanchors=8,max_steps=80)
    if sp.get('spatial_kind')=='square_torus':
        loops=square_scalar_basis(sp)
        names=['plaquette','rectangle_1x2','square_2x2']
    else:
        loops,names=_basis(sp)
    paths=periodic_paths(sp,max_steps=3,per_size=12)
    op=np.zeros((n,nt,len(levels)*3))
    tor=np.zeros((n,nt,len(levels)*2))
    rect=np.zeros((n,len(levels),len(paths['length']),nt//2))
    for i,link in enumerate(links):
        for j,l in enumerate(levels):
            u=link if l==0 else ape_spatial(link,nt,E,*staple,alpha,l)
            op[i,:,3*j:3*j+3]=measure_scalar_groups(u,nt,E,loops['idx'],loops['sign'],loops['length'],loops['kind'])
            tor[i,:,2*j:2*j+2]=measure_winding(u,nt,E,winding['idx'],winding['sign'],winding['length'],winding['direction'])
            rect[i,j]=measure_wilson_paths(u,nt,E,V,paths['idx'],paths['sign'],paths['length'],paths['u'],paths['v'],nt//2)
        if (i+1)%25==0:print(name,'measured',i+1,'/',n,flush=True)
    c,bc,scalar=_finite_stat(op,B,block)
    flux,fb,flux_summary=_finite_stat(tor,B,block)
    # Physically binned path correlators; same bins for both geometries.
    pr=np.array([x['physical_r'] for x in paths['meta']]);
    bins=np.arange(.5,3.5,.5)
    binned=[]
    for lo,hi in zip(bins[:-1],bins[1:]):
        ix=np.where((pr>=lo)&(pr<hi))[0]
        if not len(ix):continue
        w=rect[:,:,ix,:].mean(axis=2) # configuration, smearing-level, time-lag
        wb=np.array([w[ii].mean(axis=0) for ii in resample_blocks(4,per_chain,block,B)])
        wm=w.mean(axis=0);se=wb.std(axis=0,ddof=1)
        binned.append({'physical_distance_bin':[float(lo),float(hi)],'r_mean':float(pr[ix].mean()),
                       'n_paths':int(len(ix)),'W_by_smear_level':wm.tolist(),
                       'W_bootstrap_se':se.tolist(),
                       'admitted_as_potential':False})
    summary={'source':name,'source_config_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
       'reference_geometry_hash':sp['graph_hash'],'geometry':sp['spatial_kind'],
       'spatial_vertices':int(V),'spatial_faces':int(sp['F']),
       'n_chains':4,'per_chain':per_chain,'n_configs':n,'nt':nt,
       'spatial_smearing':{'method':'SU2-projected APE with inverse physical face-area staples',
          'alpha':alpha,'levels':levels,'temporal_links':'unchanged',
          'not_equivalent_to_renormalized_scale_or_anisotropy_matching':True},
       'scalar_operator_names':[f'{label}_APE{l}' for l in levels for label in names],
       'scalar':scalar,'winding':{'deck_residual':winding['deck_residual'],
          'paths':winding['meta'],'directions':[
           {'winding':[1,0],'physical_length':float(np.linalg.norm(sp['periods'][:,0]))},
           {'winding':[0,1],'physical_length':float(np.linalg.norm(sp['periods'][:,1]))}],
          'correlator_t2_SNR':flux_summary['diagonal_t2_SNR'],
          'correlator_t2_SE':flux_summary['diagonal_t2_SE'],
          'bootstrap_fraction_positive_C2':flux_summary['bootstrap_fraction_positive_C2'],
          'string_tension_admitted':False},
       'physical_distance_bins':binned,
       'analysis':{'block':block,'bootstrap_replicates':B,'sources_are_Stage3_exploratory':True,
          'max_loop_time_steps':int(nt//2),'nonperturbative_matching':'not determined',
          'local_motif_admission':'M5 control fails','mass_fit':'REJECT',
          'string_tension_fit':'REJECT','continuum_ratio':'REJECT'}}
    Path(out).mkdir(parents=True,exist_ok=True)
    (Path(out)/f'{name}_stage4.json').write_text(json.dumps(summary,indent=2))
    np.savez_compressed(Path(out)/f'{name}_stage4_measurements.npz',operators=op,flux=tor,
                        wilson_rectangles=rect,scalar_connected_C=c,winding_connected_C=flux)
    print(name,'C2_SNR',scalar['diagonal_t2_SNR'],'flux2_SNR',flux_summary['diagonal_t2_SNR'],flush=True)
    return summary


def main():
    a=argparse.ArgumentParser()
    a.add_argument('--stage3',default='/mnt/data/ym_stage3/outputs')
    a.add_argument('--out',default='outputs')
    a.add_argument('--per-chain',type=int,default=50)
    a.add_argument('--block',type=int,default=5)
    a.add_argument('--bootstrap',type=int,default=200)
    a.add_argument('--only',choices=['square','modelset','both'],default='both')
    x=a.parse_args()
    sp=build_torus(5)
    if x.only in ('both','square'):
        run('square_13x14',square_torus(13,14,sp['physical_area']),x.stage3,x.out,x.per_chain,[0,2,6],block=x.block,B=x.bootstrap)
    if x.only in ('both','modelset'):
        run('rational_M5',sp,x.stage3,x.out,x.per_chain,[0,2,6],block=x.block,B=x.bootstrap)
if __name__=='__main__':main()

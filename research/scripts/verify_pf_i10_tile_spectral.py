#!/usr/bin/env python3
"""PF-I10 direct same-source tile-cap versus basis-edge finite spectral controls."""
import argparse,json,sys,math
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh
from verify_pf_i10_source_spectral import source_import,periodic_sparse
from verify_pf_i10_tile_cutoff import source_tile_sparse
from verify_pf_i10_multimass import slq_mass,ratios

def exact(L,m2):
 eig=eigvalsh(L.toarray(),check_finite=False)
 if eig.min()<-1e-8:raise ValueError('nonPSD')
 pos=eig[eig>1e-10]
 return {'full_sqrt':float(np.sqrt(np.maximum(eig,0)+m2).mean()),
         'positive_sqrt':float(np.sqrt(pos+m2).mean()),
         'positive_log':float(np.log(pos+m2).mean()),
         'positive_relative_log':float(np.log1p(pos/m2).mean()),
         'zero_modes':int(len(eig)-len(pos))}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source-script',type=Path,required=True);ap.add_argument('--ngrids',nargs='+',type=int,default=[7,10,12,25]);ap.add_argument('--output',type=Path,required=True)
 ap.add_argument('--steps',type=int,default=180);ap.add_argument('--probes',type=int,default=128);ap.add_argument('--seed',type=int,default=1981)
 args=ap.parse_args();s=source_import(args.source_script);rows=[]
 for ng in args.ngrids:
  L,meta,_=source_tile_sparse(s,ng)
  P,pm=periodic_sparse(meta['n'])
  ta=slq_mass(L,args.seed+ng*19,args.steps,args.probes)
  pmass=slq_mass(P,args.seed+ng*19+1,args.steps,args.probes)
  q={'n':meta['n'],'components':meta['tile_components']};v=ratios(q,pm,ta,pmass)['0.0001'];
  row={'Ngrid':ng,'source_tile_N':meta['n'],'source_tile_edges':meta['tile_edges'],'source_tile_components':meta['tile_components'],
       'source_tile_positive_sqrt_R':v['sqrt']['trace_control']['positive'],
       'source_tile_full_sqrt_R':v['sqrt']['trace_control']['full'],
       'source_tile_zeta_prime_R':v['log']['trace_control']['positive'],
       'source_tile_Gamma_R':v['relative_log']['trace_control']['positive'],
       'SLQ_probe_SE_sqrt':v['sqrt']['trace_control']['positive_SE_independent']}
  if ng in [7,10,12]:
   row['exact_tile_eigenvalues']=exact(L,1e-4)
   row['exact_periodic_eigenvalues']=exact(P,1e-4)
   row['exact_positive_ratio_sqrt']=row['exact_tile_eigenvalues']['positive_sqrt']/row['exact_periodic_eigenvalues']['positive_sqrt']
   row['exact_full_ratio_sqrt']=row['exact_tile_eigenvalues']['full_sqrt']/row['exact_periodic_eigenvalues']['full_sqrt']
  rows.append(row)
  print(json.dumps({'ngrid':ng,'n':meta['n'],'components':meta['tile_components'],
       'R_source_tile_pos':row['source_tile_positive_sqrt_R'],'R_source_tile_full':row['source_tile_full_sqrt_R'],
       'exact_ratio':row.get('exact_positive_ratio_sqrt')}),flush=True)
  args.output.write_text(json.dumps({'scope':'author original tile-cap operator versus periodic, NOT completed basis graph','source_sha256':__import__('verify_pf_i10_source_spectral').SOURCE_SHA,'rows':rows},indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()

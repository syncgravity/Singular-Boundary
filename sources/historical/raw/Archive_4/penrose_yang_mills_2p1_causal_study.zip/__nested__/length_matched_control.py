"""Alternative square comparators matching the mean Penrose physical edge length.
Penrose ensemble itself is unchanged from the main geometry-weighted comparison;
bare square mean couplings are held equal to the *original density-matched* trial.
This is a sensitivity diagnostic, not a simultaneously area+cell-density match.
"""
import json,math
import numpy as np
from penrose_2p1_study import paired_spatial,spatial_square,run_once

def run(M,betas,params):
    p,sd=paired_spatial(M)
    edge_mean=float(np.mean(p['edge_lengths']))
    nx,ny=params
    sa=spatial_square(nx,ny,p['area'])
    a_ref=math.sqrt(p['area']/p['F']);dt=a_ref;nt=10
    meta={'M':M,'betas':betas,'comparison':'square mean source separation matched',
          'area':p['area'],'Penrose_edge_length_mean':edge_mean,
          'density_control_square_edge_length':float(sd['edge_lengths'][0]),
          'length_control_square_edge_length':float(sa['edge_lengths'][0]),
          'density_control_square_F':sd['F'],'length_control_square_F':sa['F'],
          'nt':nt,'time_spacing':dt,'results':[]}
    for beta in betas:
        # Same mean bare coupling as original Penrose/density-square pairing
        targets=(beta*sd['F']/p['F'],beta)
        for seed in [109,211]:
            r=run_once(sa,nt,beta,seed,240,900,4,10,dt,a_ref,mean_targets=targets)
            meta['results'].append(r)
            print(json.dumps({'M':M,'beta':beta,'seed':seed,'sp':r['spatial_plaquette'],
                   'tm':r['temporal_plaquette'],'R2':r['rectangular_wilson_loops'][1],
                   'Eeff12':r['rectangle_effective_static_energies'][0],
                   'elapsed_s':round(r['seconds'],2)}),flush=True)
    with open(f'/mnt/data/study_2p1_M{M}_lengthsquare.json','w') as f:json.dump(meta,f,indent=2)

if __name__=='__main__':
    run(5,[2.5,3.5],(12,13))
    run(8,[2.5],(20,20))

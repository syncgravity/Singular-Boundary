#!/usr/bin/env python3
"""PF-I3 source-model discriminator: trace identities and *controlled*, not original, spectra.

Authentic printed Paper1 P3 pentagrid equations are reconstructed by PF-I2.
The Paper2 coupled numerical generator is unavailable; do not claim reproduction.
Only finite scalar graph operators, never a Yang-Mills mass-gap test.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, math, sys
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.linalg import eigh
from scipy.spatial import ConvexHull

HERE=Path(__file__).resolve().parent
PFI2=next((x for x in (HERE, HERE.parent/'pf_i2_checkpoint') if (x/'verify_pf_i2_pentagrid.py').is_file()),None)
if PFI2 is None:
    raise RuntimeError('PF-I2 generator not found: keep verify_pf_i2_pentagrid.py beside this script')
sys.path.insert(0,str(PFI2))
from verify_pf_i2_pentagrid import generate, PHI

SOURCE_PAPER2_RATIO_M1=0.7371
SOURCE_PAPER2_RATIO_MHALF=0.8332
SOURCE_PAPER1_IR_M2=1e-4


def p3_matrices(radius, nmax):
    q=generate(radius,nmax)
    vertices=sorted(q['vertices']); iv={v:i for i,v in enumerate(vertices)}
    edges=list(q['edges'].items())
    n=len(vertices)
    ii=[];jj=[];ww=[];deg_w=np.zeros(n);deg_c=np.zeros(n)
    for (a,b),(_,_,_,w) in edges:
        i=iv[a];j=iv[b];deg_w[i]+=w;deg_w[j]+=w;deg_c[i]+=1;deg_c[j]+=1
        ii.extend([i,j]);jj.extend([j,i]);ww.extend([-w,-w])
    W=sparse.coo_matrix((ww,(ii,jj)),shape=(n,n)).toarray()
    mean_w=float(np.mean([x[-1] for _,x in edges]))
    A=W/(-1) # positive weighted adjacency
    A_c=(A>0).astype(float)
    lap_w=np.diag(deg_w)-A
    lap_c=np.diag(deg_c)-A
    lap_uniform=mean_w * (np.diag(deg_c)-A_c)
    return {
        'name':'Paper1-P3-reconstructed', 'n':n,'e':len(edges),'r':radius,'grid_levels':nmax,
        'mean_count_degree':float(deg_c.mean()),'mean_weighted_degree':float(deg_w.mean()),
        'mean_edge_weight':mean_w,'B_fraction':float(np.mean([x[2]=='B' for _,x in edges])),
        'weighted_strength':lap_w,'count_minus_weight':lap_c,'same_graph_uniform_mean_weight':lap_uniform,
        'coords': np.array(vertices,dtype=float)@np.stack((np.cos(2*np.pi*np.arange(5)/5),np.sin(2*np.pi*np.arange(5)/5)),axis=1),
        'edges':edges
    }


def control_patch(n,kind):
    size=math.ceil(math.sqrt(n)*1.5)+5
    integer=[]
    b1=np.array([1.,0.]);b2=np.array([.5,math.sqrt(3)/2]) if kind=='triangle' else np.array([0.,1.])
    for i in range(-size,size+1):
        for j in range(-size,size+1):
            pos=i*b1+j*b2
            integer.append((float(pos@pos),i,j))
    pts=sorted(integer)[:n]
    verts=[(i,j) for _,i,j in pts];iv={v:i for i,v in enumerate(verts)}
    steps=[(1,0),(0,1)] + ([(1,-1)] if kind=='triangle' else [])
    edges=[];deg=np.zeros(n)
    for a,idx in iv.items():
        for di,dj in steps:
            b=(a[0]+di,a[1]+dj)
            if b in iv:
                jdx=iv[b];edges.append((idx,jdx));deg[idx]+=1;deg[jdx]+=1
    lap=np.diag(deg)
    for i,j in edges:lap[i,j]=-1;lap[j,i]=-1
    assert np.max(np.abs(lap-lap.T))<1e-12
    assert abs(lap.sum())<1e-10
    coords=np.array([i*b1+j*b2 for i,j in verts])
    return {'name':kind, 'n':n,'e':len(edges),'mean_degree':float(deg.mean()),'lap':lap,'coords':coords}


def spectral(L,m2):
    e=eigh(L, eigvals_only=True,check_finite=False,driver='evr')
    assert e[0]>-1e-8, e[0]
    e=np.maximum(e,0)
    z={str(s):float(np.mean((e+m2)**(-s))) for s in [-2,-1,-.5,0,.5]}
    return {'zeta':z,'minimum_eigenvalue':float(e[0]),'first_positive':float(e[1]),
        'mean_L':float(np.mean(e)),'mean_L2':float(np.mean(e**2)),
        'mean_log_L_plus_m2':float(np.mean(np.log(e+m2))),
        'eigenvalues':e}


def check_trace(L,n,mu,weighted=False,edges=None):
    # Exact finite trace identities; for any zero-diagonal adjacency W,
    # Tr(L)=sum D and Tr(L^2)=sum D^2 + 2 sum_edge w_e^2.
    diagonal=np.diag(L);off=L-np.diag(diagonal)
    tr1=float(diagonal.mean()); tr2=float((np.sum(diagonal**2)+np.sum(off**2))/n)
    assert abs(tr1-np.trace(L)/n) < 5e-12
    assert abs(tr2-np.trace(L@L)/n) < 5e-10
    return tr1,tr2


def sample(radius,nmax,m2):
    pen=p3_matrices(radius,nmax)
    controls={k:control_patch(pen['n'],k) for k in ('triangle','square')}
    candidates={'P3_weighted_strength':pen['weighted_strength'],
                'P3_count_degree_minus_weighted':pen['count_minus_weight'],
                'P3_same_graph_uniform_edge_mean':pen['same_graph_uniform_mean_weight'],
                'triangle_unit_edges':controls['triangle']['lap'],
                'square_unit_edges':controls['square']['lap']}
    for name,L in list(candidates.items()):
        assert np.max(np.abs(L-L.T))<1e-10
        tr1,tr2=check_trace(L,len(L),m2)
        sp=spectral(L,m2)
        assert abs(sp['mean_L']-tr1)<1e-8
        assert abs(sp['mean_L2']-tr2)<1e-7
        sp['trace1']=tr1;sp['trace2']=tr2
        sp.pop('eigenvalues')
        candidates[name]=sp
    qc_area=float(ConvexHull(pen['coords']).volume)
    periodic_areas={k:float(ConvexHull(controls[k]['coords']).volume) for k in ('triangle','square')}
    ratios={}
    for model in ('P3_weighted_strength','P3_count_degree_minus_weighted','P3_same_graph_uniform_edge_mean'):
        ratios[model]={}
        for control in ('triangle_unit_edges','square_unit_edges'):
            a=candidates[model];b=candidates[control]
            ratios[model][control]={
                'raw':{s:a['zeta'][s]/b['zeta'][s] for s in ('-2','-1','-0.5','0','0.5')},
                'match_mean_eigenvalue_scale':None,
                'match_vertex_hull_area':None,
                'single_point_calibration_to_Paper2_R_minus1':None
            }
            alpha=a['mean_L']/b['mean_L']; cc=controls['triangle']['lap'] if control=='triangle_unit_edges' else controls['square']['lap']
            matched=spectral(alpha*cc,m2)
            ratios[model][control]['match_mean_eigenvalue_scale']={
                'periodic_operator_scale':float(alpha),
                'R':{s:a['zeta'][s]/matched['zeta'][s] for s in ('-2','-1','-0.5','0','0.5')},
            }
            assert abs(ratios[model][control]['match_mean_eigenvalue_scale']['R']['-1']-1)<1e-11
            # A deliberate one-parameter calibration (not a source reproduction):
            # select periodic conductance to match the source-reported R(-1)
            # EXACTLY via the trace identity, then independently predict R(-.5).
            beta=(a['zeta']['-1']/SOURCE_PAPER2_RATIO_M1 - m2)/b['mean_L']
            assert beta>0
            calibrated=spectral(beta*cc,m2)
            predicted={s:a['zeta'][s]/calibrated['zeta'][s] for s in ('-2','-1','-0.5','0','0.5')}
            assert abs(predicted['-1']-SOURCE_PAPER2_RATIO_M1)<1e-10
            ratios[model][control]['single_point_calibration_to_Paper2_R_minus1']={
                'periodic_operator_scale_selected_to_fit_s_minus1':float(beta),
                'resulting_ratio_at_s_minus_half_without_another_fit':float(predicted['-0.5']),
                'difference_from_Paper2_s_minus_half':float(predicted['-0.5']-SOURCE_PAPER2_RATIO_MHALF),
                'ratios':predicted,
                'is_original_reproduction':False
            }
            # Additional descriptive control: equal N and convex-hull area.
            # P3 source bonds have unit projected length; scale periodic
            # spatial coordinates by h, then the physical Laplacian by h^-2.
            kind='triangle' if control.startswith('triangle') else 'square'
            periodic_h2=qc_area/periodic_areas[kind]
            area_scaled=spectral(cc/periodic_h2,m2)
            ratios[model][control]['match_vertex_hull_area']={
                'QC_vertex_hull_area':qc_area,
                'periodic_unit_edge_hull_area':periodic_areas[kind],
                'periodic_edge_length_scale':math.sqrt(periodic_h2),
                'R':{s:a['zeta'][s]/area_scaled['zeta'][s] for s in ('-2','-1','-0.5','0','0.5')}
            }
    return {
        'radius':radius,'nmax':nmax,'n':pen['n'],
        'p3':{k:v for k,v in pen.items() if k not in ('coords','weighted_strength','count_minus_weight','same_graph_uniform_mean_weight','edges')},
        'controls':{k:{z:v for z,v in y.items() if z not in ('lap','coords')} for k,y in controls.items()},
        'QC_convex_hull_area':qc_area,'periodic_unit_edge_convex_hull_areas':periodic_areas,
        'operators':candidates,
        'ratios':ratios,
        'source_code_reproduction':False,
        'same_normalization_as_paper2':False,
        'dimensional_YM_gap_test':False,
    }


def exact_source_constraints(m2):
    dqc=3.9;dtri=6.;r=SOURCE_PAPER2_RATIO_M1
    ratio=(dqc+m2)/(dtri+m2)
    inferred_mass=(r*dtri-dqc)/(1-r)
    # If QC diag = mean count degree, periodic diag = c * 6, and m2 fixed,
    # the required periodic edge conductance c is determined exactly.
    required_periodic=(dqc+m2)/r-m2
    c=required_periodic/dtri
    # Two exactly identical negative-half zetas, different log determinant:
    # a=(1,9), b=(4,4) with m2=0
    s_a=(1+3)/2;s_b=(2+2)/2
    log_a=(math.log(1)+math.log(9))/2
    log_b=(math.log(4)+math.log(4))/2
    assert s_a==s_b and abs(log_a-log_b)>0.25
    # Mass-regulated numerical sanity test: use positive mode eigenvalues
    for s in (-2,-1,-.5,0,.5):
        assert abs(sum((v+m2)**(-s) for v in [1,9])/2 -np.mean((np.array([1.,9.])+m2)**(-s)))<1e-12
    return {'paper2_s_minus1':r,'paper2_s_minus_half':SOURCE_PAPER2_RATIO_MHALF,
        'paper2_reported_degree_qc':dqc,'paper2_reported_degree_triangular':dtri,
        'paper1_explicit_m2_not_certain_paper2':m2,
        'strict_count_degree_triangular_unit_edges_predicted_ratio_s_minus1':ratio,
        'source_report_minus_prediction':r-ratio,
        'mass_squared_needed_to_force_0_7371_under_count_degree_unit_triangle':inferred_mass,
        'periodic_mean_conductance_needed_at_fixed_m2_and_count_qc':c,
        'at_s_zero_all_regulated_full_spectra_normalized_zeta_equal_one':True,
        'two_mode_counterexample_zeta_minus_half_same':s_a,
        'two_mode_counterexample_mean_logdet_a':log_a,
        'two_mode_counterexample_mean_logdet_b':log_b,
        'one_loop_determinant_not_equal_negative_half_zeta':True}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--m2',type=float,default=SOURCE_PAPER1_IR_M2)
    ap.add_argument('--summary-output',type=Path,default=None)
    args=ap.parse_args()
    results={'report':'PF-I3 exact trace and one-loop audit; new finite controls are illustrative, NOT Paper2 numerical generator',
             'm2':args.m2,'source_exact_constraints':exact_source_constraints(args.m2),
             'samples':[]}
    for radius,nmax in [(6.5,11),(12.0,12)]:
        smp=sample(radius,nmax,args.m2)
        results['samples'].append(smp)
    txt=json.dumps(results,indent=2,sort_keys=True)+'\n'
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(txt)
    if args.summary_output:
        summary={'schema':'singular-boundary.pf-i3-spectral-controls.v1',
                 'date':'2026-11-07','source_original_Paper2_reproduced':False,
                 'continuous_Yang_Mills_gap_proved':False,
                 'm2_borrowed_from_Paper1':args.m2,
                 'conditional_source_constraints':results['source_exact_constraints'],
                 'samples':[]}
        for smpi in results['samples']:
            compact={'n':smpi['n'],'edges':smpi['p3']['e'],
                     'P3_mean_count_degree':smpi['p3']['mean_count_degree'],
                     'P3_mean_weighted_strength':smpi['p3']['mean_weighted_degree'],
                     'triangular_edges':smpi['controls']['triangle']['e'],
                     'square_edges':smpi['controls']['square']['e'],
                     'models':{}}
            for model in ('P3_weighted_strength','P3_count_degree_minus_weighted',
                          'P3_same_graph_uniform_edge_mean'):
                obj=smpi['ratios'][model]['triangle_unit_edges']
                compact['models'][model]={
                    'raw_ratios':{k:obj['raw'][k] for k in ('-2','-1','-0.5')},
                    'same_first_moment_ratios':{k:obj['match_mean_eigenvalue_scale']['R'][k] for k in ('-1','-0.5')},
                    'one_ratio_fit_scale':obj['single_point_calibration_to_Paper2_R_minus1']['periodic_operator_scale_selected_to_fit_s_minus1'],
                    'prediction_at_s_minus_half':obj['single_point_calibration_to_Paper2_R_minus1']['resulting_ratio_at_s_minus_half_without_another_fit']}
            summary['samples'].append(compact)
        args.summary_output.parent.mkdir(parents=True,exist_ok=True)
        args.summary_output.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'source_constraints':results['source_exact_constraints'],
        'samples':[{'n':s['n'],'edges':s['p3']['e'],
           'triangle_n_edges':s['controls']['triangle']['e'],
           'triangle_mean_degree':s['controls']['triangle']['mean_degree'],
           'weighted_vs_triangle_R(-0.5)':s['ratios']['P3_weighted_strength']['triangle_unit_edges']['raw']['-0.5'],
           'matched_R(-0.5)':s['ratios']['P3_weighted_strength']['triangle_unit_edges']['match_mean_eigenvalue_scale']['R']['-0.5']
          } for s in results['samples']]},indent=2))

if __name__=='__main__': main()

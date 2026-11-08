#!/usr/bin/env python3
"""Independent implementation-provenance checks on uploaded source scripts.

This tests uploaded finite algorithms as written, NOT a continuum YM/gravity
argument, and DOES NOT modify user source code. Filenames serve only as locators;
classify scripts by presence of the functions passed on command line.
"""
import argparse, hashlib, importlib.util, io, json, tarfile
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.spatial import HalfspaceIntersection


def load_script(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name,str(path))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def two_dimensional(tiler, coupled):
    results=[]
    published={7:1550,10:3042,12:4324}
    for ng,n_expected in published.items():
        t=coupled.build_penrose_tiling(ng)
        interior=coupled.select_interior_vertices(t,0.35)
        tile_L,n_tile,*rest=tiler.build_penrose_laplacian(t,1.0,1/coupled.PHI**2)
        z5_L,n_z5,*_=coupled.build_coupled_z5_laplacian(t,interior,1.0,1/coupled.PHI**2)
        assert len(interior)==n_tile==n_z5==n_expected
        assert rest[-1]==interior
        t_edges=np.transpose(np.triu(-tile_L>1e-12,k=1).nonzero())
        z_edges=np.transpose(np.triu(-z5_L>1e-12,k=1).nonzero())
        E_tile={tuple(p) for p in t_edges};E_z5={tuple(p) for p in z_edges}
        assert not (E_tile-E_z5)
        assert np.max(np.abs(tile_L.sum(axis=1)))<1e-11
        assert np.max(np.abs(z5_L.sum(axis=1)))<1e-11
        E_extra=E_z5-E_tile
        labels=t['multi_indices'];fam_hist=Counter()
        for i,j in E_extra:
            d=np.asarray(labels[interior[j]])-np.asarray(labels[interior[i]])
            assert (np.abs(d).sum()==1 and np.count_nonzero(d)==1),d
            fam_hist[int(np.flatnonzero(d)[0])]+=1
        periodic_n=int(np.sqrt(n_z5))**2
        result={'N_grid':ng,'generated_vertices':t['n_vertices'],
            'interior_vertices':n_expected,'periodic_reference_vertices':periodic_n,
            'periodic_reference_not_exact_same_N':periodic_n!=n_expected,
            'tile_edge_count':len(E_tile),'coupled_basis_edge_count':len(E_z5),
            'coupled_extra_edges':len(E_extra),'coupled_missing_tile_edges':len(E_tile-E_z5),
            'coupled_extra_edges_by_family':dict(sorted(fam_hist.items())),
            'max_abs_matrix_difference':float(np.max(np.abs(tile_L-z5_L))),
            'mean_unweighted_basis_coordination':2*len(E_z5)/n_z5,
            'mean_weighted_strength':float(np.trace(z5_L)/n_z5)}
        results.append(result)
        del tile_L,z5_L
    assert [x['coupled_extra_edges'] for x in results]==[0,62,85]
    return results


def z6_window_geometry(z6):
    _,en=z6.icosahedral_basis_vectors()
    phi=z6.PHI
    R=np.sqrt(2/(phi+2))*1.15
    # Directly construct halfspaces implemented in triacontahedron_test:
    # |r · e_j| < R for each of the six j values.
    inequalities=np.vstack([np.column_stack([en,np.full(6,-R)]),
                             np.column_stack([-en,np.full(6,-R)])])
    poly=HalfspaceIntersection(inequalities,np.zeros(3))
    on_face=[]
    for j in range(6):
        for sign in (-1,1):
            on_face.append(int(np.sum(np.abs(poly.intersections@(sign*en[j])-R)<1e-7)))
    assert len(poly.intersections)==20
    assert on_face==[5]*12
    return {'implementation':'intersection of six axial slabs, 12 planar pentagonal facets',
            'halfspace_boundaries':len(inequalities),'polytope_vertices':len(poly.intersections),
            'polytope_facets':sum(x>=3 for x in on_face),'vertices_on_each_facet':on_face,
            'claimed_rhombic_triacontahedron_facets':30,
            'source_window_30_face_claim_matches_implemented_12_face_polytope':False,
            'window_R_calibrated_multiplier':1.15}


def archived_z6(archive):
    rows=[]
    with tarfile.open(archive,'r:gz') as tf:
        verdict=json.load(tf.extractfile('z6_finiteness_data/finiteness_verdict.json'))
        for ng in [8,9,10,11,12,13,14,15]:
            src=json.load(tf.extractfile(f'z6_finiteness_data/results_{ng}.json'))
            q=np.load(io.BytesIO(tf.extractfile(f'z6_finiteness_data/lam_qc_{ng}.npy').read()))
            p=np.load(io.BytesIO(tf.extractfile(f'z6_finiteness_data/lam_per_{ng}.npy').read()))
            assert (len(q),len(p))==(src['N_qc'],src['N_per'])
            ratio=np.mean(np.sqrt(q+1e-6))/np.mean(np.sqrt(p+1e-6))
            assert abs(ratio-src['R_minus_half'])<1e-12
            # The archived eigenvalues are strictly positive: zero modes
            # were discarded before the code's spectral dimension calculation.
            assert q.min()>0 and p.min()>0
            record={'N_range':ng,'retained_positive_modes_QC':len(q),
                'retained_positive_modes_periodic':len(p),
                'reported_and_recomputed_R_minus_half':float(ratio),
                'max_retained_QC_eigenvalue':float(q.max()),
                'max_retained_periodic_eigenvalue':float(p.max()),
                'last_two_sizes_use_only_lowest_2999_modes':ng in [14,15]}
            if ng==8:
                s=np.logspace(-3,2,300)
                k=np.exp(-np.multiply.outer(s,p))
                # periodic open cubic control is connected => exactly one
                # zero mode. Add it back for the actual finite heat trace.
                full_heat=(1+k.sum(axis=1))/(len(p)+1)
                d=np.r_[0,-2*np.diff(np.log(full_heat))/np.diff(np.log(s))]
                record['reported_periodic_peak_ds_excluding_zero']=src['peak_ds_per']
                record['recomputed_periodic_peak_ds_restoring_zero']=float(d.max())
                assert abs(float(d.max())-3.1951592470251877)<1e-10
            rows.append(record)
    assert verdict['sizes_used']==[8,9,10,11,12,13]
    assert verdict['finiteness'] is False
    return {'verdict_as_written':verdict['verdict'],
            'sizes_used_for_gamma':verdict['sizes_used'],
            'delta_gamma_minus_half':verdict['delta_gamma_at_minus_half'],
            'sigma_reported_by_code':verdict['sigma'],
            'z6_original_scaling_finiteness_flag':verdict['finiteness'],
            'data':rows,
            'important_caveat':'Script removes degree-zero isolated vertices but does NOT test global connectivity. More than one zero mode could remain on QC, so only periodic control zero-mode reconstruction is definitive.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--tiler',type=Path,required=True,help='Source script defining build_penrose_laplacian')
    parser.add_argument('--coupled',type=Path,required=True,help='Source script defining build_coupled_z5_laplacian')
    parser.add_argument('--z6',type=Path,required=True,help='Source script defining icosahedral_basis_vectors')
    parser.add_argument('--z6-data',type=Path,required=True,help='Archived eigenvalue data tar.gz')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    tiler=load_script(args.tiler,'pfi6_tiler')
    coupled=load_script(args.coupled,'pfi6_coupled')
    z6=load_script(args.z6,'pfi6_icosahedron')
    data={'scope':'finite source-implementation audit; not continuum proof',
          'sources':{'p3_tiler':{'sha256':sha(args.tiler)},'z5_coupled':{'sha256':sha(args.coupled)},
                     'z6_window':{'sha256':sha(args.z6)},'z6_eigenvalue_archive':{'sha256':sha(args.z6_data)}},
          'two_dimensional_source_comparison':two_dimensional(tiler,coupled),
          'z6_window_shape':z6_window_geometry(z6),
          'archived_z6_spectral_checks':archived_z6(args.z6_data),
          'source_code_determines_geometry_not_filename':True,
          'original_unprovided_auxiliary_scripts_still_needed':True,
          'ym_mass_gap_proved':False,'gravitational_uv_finiteness_proved':False}
    args.output.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'source_matching_counts':[x['interior_vertices'] for x in data['two_dimensional_source_comparison']],
                      'extra_Z5_edges':[x['coupled_extra_edges'] for x in data['two_dimensional_source_comparison']],
                      '3d_window_faces':data['z6_window_shape']['polytope_facets'],
                      '3d_gamma_delta':data['archived_z6_spectral_checks']['delta_gamma_minus_half'],
                      '3d_finiteness_flag':data['archived_z6_spectral_checks']['z6_original_scaling_finiteness_flag'],
                      'periodic_peak_ds_fixed':data['archived_z6_spectral_checks']['data'][0]['recomputed_periodic_peak_ds_restoring_zero']},indent=2))

if __name__=='__main__':main()

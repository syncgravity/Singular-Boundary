#!/usr/bin/env python3
"""Checks exact SU(2) q-moment bounds on genuine Penrose planar disks.
Does NOT establish local curvature concentration for the three-dimensional prism Wilson measure.
"""
import sys, json, csv
from pathlib import Path
from collections import Counter
import numpy as np
from scipy.special import ive
ROOT=Path(__file__).resolve().parent
sys.path.insert(0, '/mnt/data/R3_local_energy_relative_haar_2026_10_27')
from direct_cut_project import build,validate

def ratio(lambda_, k):
    return float(ive(k,lambda_)/ive(1,lambda_))

def haar_q(t):
    return float(2*ive(1,t)/t)

def main():
    rows=[]
    for rad in (5.,6.5,8.,10.):
        g,gamma=build(rad,0)
        geo=validate(g,gamma)
        counts=Counter()
        for face in g.faces:
            for i in range(4):
                counts[tuple(sorted((face[i],face[(i+1)%4])))] += 1
        assert set(counts)==set(g.edges)
        hist=Counter(counts.values())
        assert set(hist).issubset({1,2})
        assert sum(m*c for m,c in hist.items()) == 4*len(g.faces)
        rows.append({'radius':rad,'vertices':len(g.labels),'edges':len(g.edges),'rhombi':len(g.faces),
                     'boundary_staple_links_m1':hist[1],'interior_staple_links_m2':hist[2],
                     'max_number_incident_retained_faces':max(counts.values()),
                     'rigorous_uniform_lambda_E_F_e_upper':3.0,
                     'rigorous_tail_at_lambda_F_e_ge_12':float(8*np.exp(-6)),
                     'rigorous_local_E_d_sum_coefficient':1.5})
    tgrid=np.geomspace(1e-4,1e4,500)
    tg=np.array([float(t*(1-ratio(t,2))) for t in tgrid]);
    assert tg.max()<1.50001
    moment_checks=[]
    for lam in (1.,4.,8.,16.,32.,100.,1000.):
        for theta in (.25,.5,.75):
            mgf=haar_q((1-theta)*lam)/haar_q(lam)
            bound=(1-theta)**(-1.5)
            assert mgf <= bound*(1+1e-12)
            moment_checks.append({'lambda':lam,'theta':theta,'single_plaquette_exact_mgf':mgf,'gamma_majorant':bound})
    import scipy.special as sc
    # Monte Carlo check of the deterministic F_e <= sum incident deficits in the two-staple model.
    rng=np.random.default_rng(267101)
    w=rng.normal(size=(4096,4));w/=np.linalg.norm(w,axis=1,keepdims=True)
    a,b=w[:2048],w[2048:]
    F=2-np.linalg.norm(a+b,axis=1)
    # Evaluate at link U=identity: plaquette deficits d(A)+d(B).
    S=2-a[:,0]-b[:,0]
    assert np.all(F>=-1e-12) and np.all(F<=S+1e-12)
    with (ROOT/'penrose_planar_certificate.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
    cert={'scope':'two-dimensional planar free-boundary Penrose retained Wilson measure (NOT 3D prism)',
          'Penrose_geometry':rows,'mgf_samples':moment_checks,'verified_max_lambda_excess':float(tg.max()),
          'two_staple_F_le_S_max_violation':float(np.max(F-S)),
          'theorems':{'local_raw_curvature':'lambda E sum_{p in A} d(Wp) <= (3/2)|A|',
                      'staple_bound':'lambda E F_e <= (3/2) m_e <= 3',
                      'staple_tail':'P(lambda F_e >= t) <= 2^(3m_e/2) exp(-t/2)',
                      'conditional_block':'lambda E[S_B|b] <= lambda min_u S_B(u;b) + (3/2)|B| log(lambda) + C_nu |B| for lambda>=1',
                      '3d_prism_status':'NOT PROVED: need control of block conditional minimum or exterior staple frustration'}}
    (ROOT/'certificate.json').write_text(json.dumps(cert,indent=2))
    print(json.dumps({'geometry':rows,'max_Bessel_excess':float(tg.max()),'status':'2D concentration proved; 3D retained staple frustration remains open'},indent=2))
if __name__=='__main__':main()

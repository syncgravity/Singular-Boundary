#!/usr/bin/env python3
"""Descriptive same-field channel-overlap pilot. No temporal correlation or mass fits."""
import json
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
seeds=[101,211,307,419]
for geo in ('square','penrose'):
    with np.load(P/'results'/f'{geo}_projection_pilot.npz') as f:
        new=f['observables'][:,-1,:,:] # four independently initiated snapshots, 20 timeslices, 3 clusters
    old=[]
    for seed in seeds:
        with np.load(Path('/mnt/data')/f'{geo}_nt20_seed{seed}.npz') as z:
            assert int(z['measured_sweeps'][-1]) == int(z['sweeps']) == 10000
            old.append(z['observables_scalar'][-1,:,:])
    old=np.asarray(old)
    # Within snapshot demean timeslices. Correlation only probes same-field operator redundancy,
    # NOT overlap with states of transfer matrix. The rank across snapshots is limited to four.
    x=(new-new.mean(axis=1,keepdims=True)).reshape(-1,3)
    y=(old-old.mean(axis=1,keepdims=True)).reshape(-1,9)
    cross=np.corrcoef(x.T,y.T)[:3,3:]
    # Caution: high correlation here does not imply good ground-state overlap.
    summary={'geometry':geo,'cross_operator_corr_per_new_channel':cross.tolist(),
             'maximum_abs_corr_with_any_legacy_channel':np.max(abs(cross),axis=1).tolist(),
             'description':'Same-field, timeslice-centered cross-channel correlations, four final gauge fields; no temporal mass estimate'}
    (P/'results'/f'{geo}_legacy_overlap.json').write_text(json.dumps(summary,indent=2))
    print(geo,np.round(summary['maximum_abs_corr_with_any_legacy_channel'],3))

"""Empirical MCMC and correlator gate (no automatic physics claim).

Calculation requires complete post-burn-in samples on at least four independent
chains. Rank Rhat and bulk/tail ESS are computed channel-by-channel. The
output is a diagnostic report, not a mass or string-tension estimator.
"""
from pathlib import Path
import numpy as np

def correlation_per_configuration(x,mean=None,tmax=None):
    """C_i(dt)=mean_t[(O_i(t)-mu)(O_i(t+dt)-mu)] for channel arrays.

    Explicit global ensemble centering is essential for the scalar channel;
    centering individually on each gauge configuration induces finite-T bias.
    """
    x=np.asarray(x,dtype=float)
    if x.ndim!=3:raise ValueError('Expected configurations by time by channel')
    n,T,k=x.shape
    mu=np.mean(x,axis=(0,1),keepdims=True) if mean is None else np.reshape(mean,(1,1,k))
    centered=x-mu
    tmax=T//2 if tmax is None else tmax
    return np.stack([np.mean(centered*np.roll(centered,-t,axis=1),axis=1)
                     for t in range(tmax+1)],axis=1)

def audit_chains(checkpoint_root,kind,seeds=(101,211,307,419),min_ess=400,max_rhat=1.01):
    import arviz as az
    arrays=[];starts=[];diagnostics=[]
    for seed in seeds:
        filename=Path(checkpoint_root)/f'{kind}_nt20_seed{seed}.npz'
        if not filename.exists():return {'admitted':False,'reason':'missing chain','seed':seed}
        with np.load(filename,allow_pickle=False) as z:
            starts.append(np.array(z['measured_sweeps']))
            arrays.append({'scalar':np.array(z['observables_scalar']),
                           'flux':np.array(z['observables_flux']),
                           'wilson':np.array(z['observables_wilson'])})
    n=min(a['scalar'].shape[0] for a in arrays)
    if n < 100:return {'admitted':False,'reason':'insufficient post-burn samples for reliable chain diagnostics',
                      'minimum_samples_per_chain':n}
    for name in ('scalar','flux'):
        X=np.stack([a[name][:n].mean(axis=1) for a in arrays])
        # Autocorrelation of bulk/mean operator signal. Must also assess
        # individual per-configuration connected correlation estimates.
        if np.any(~np.isfinite(X)):return {'admitted':False,'reason':'nonfinite data'}
        for k in range(X.shape[-1]):
            chain=X[:,:,k]
            rh=np.asarray(az.rhat(chain,method='rank')).item()
            eb=np.asarray(az.ess(chain,method='bulk')).item()
            et=np.asarray(az.ess(chain,method='tail')).item()
            diagnostics.append({'kind':name,'channel':k,'rank_rhat':float(rh),
                 'bulk_ess':float(eb),'tail_ess':float(et),
                 'passed':bool(rh<max_rhat and eb>=min_ess and et>=min_ess)})
    return {'admitted':bool(all(d['passed'] for d in diagnostics)),
            'minimum_samples_per_chain':n,'diagnostics':diagnostics,
            'note':'Additional autocorrelation diagnostics of connected correlator channels and multi-time fit gates required.'}

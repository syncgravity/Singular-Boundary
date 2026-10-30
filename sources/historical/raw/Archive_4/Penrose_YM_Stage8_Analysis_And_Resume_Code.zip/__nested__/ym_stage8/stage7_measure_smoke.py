import json,time,sys
from pathlib import Path
import numpy as np
from stage7_large_torus import pair
from stage7_measurement import build_measurement_plan,measure_configuration

def main():
    out=Path('/mnt/data/ym_stage7')
    spair=pair()
    for name,sp in zip(('penrose','square'),spair):
        start=time.monotonic()
        ck=out/'checkpoints'/f'{name}_nt20_seed101.npz'
        with np.load(ck,allow_pickle=False) as z:
            u=z['links'];n=int(z['sweeps'].item())
            assert n==2
        plan=build_measurement_plan(sp)
        O,F,W=measure_configuration(u,20,sp,plan)
        assert O.shape==(20,9) and F.shape==(20,6) and W.shape==(3,100,10)
        assert np.isfinite(O).all() and np.isfinite(F).all() and np.isfinite(W).all()
        np.savez_compressed(out/(name+'_warmup_observable_smoke.npz'),scalar=O,flux=F,wilson=W)
        result={'geometry':name,'sweep':n,'n_scalar_observables':O.shape[1],
          'n_winding_observables':F.shape[1],'n_wilson_paths':W.shape[1],
          'nt':20,'full_measurement_seconds':time.monotonic()-start,
          'finite_values':True,'physical_use':'PROHIBITED: unequilibrated hot start, 1 config; implementation smoke only'}
        (out/(name+'_measurement_smoke.json')).write_text(json.dumps(result,indent=2))
        print(name,'smoke seconds',round(result['full_measurement_seconds'],2),'arrays',O.shape,F.shape,W.shape,flush=True)

if __name__=='__main__': main()

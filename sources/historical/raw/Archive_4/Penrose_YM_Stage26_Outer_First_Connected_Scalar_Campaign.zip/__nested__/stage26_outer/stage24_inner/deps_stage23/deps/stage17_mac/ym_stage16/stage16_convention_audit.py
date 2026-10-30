"""Independent gauge test for the legacy Stage 13 matrix orientation convention."""
from pathlib import Path
import json
import numpy as np
from stage16_multihit import catalog_square,multihit_batched
from stage13_transport import small_square,direct_rectangle
from wilson_torus import mul

def audit():
 sp,lat=small_square(nt=15,nx=8,ny=8);E,V,nt=sp['E'],sp['V'],lat['nt']
 paths=catalog_square(sp,nanchors=16)
 U=np.zeros((lat['L'],4));U[:,0]=1.
 rng=np.random.default_rng(91);g=rng.normal(size=(nt,V,4));g/=np.linalg.norm(g,axis=2,keepdims=True)
 new=U.copy()
 for t in range(nt):
  for e,(a,b) in enumerate(sp['edges']):
   qb=g[t,b].copy();qb[1:]*=-1
   new[t*E+e]=mul(mul(g[t,a],U[t*E+e]),qb)
  for v in range(V):
   qb=g[(t+1)%nt,v].copy();qb[1:]*=-1
   new[nt*E+t*V+v]=mul(mul(g[t,v],U[nt*E+t*V+v]),qb)
 d0,m0=multihit_batched(U,lat,sp,paths,lag=4)
 d1,m1=multihit_batched(new,lat,sp,paths,lag=4)
 legacy=[]
 for i in range(len(paths['u'])):
  val=direct_rectangle(new,nt,E,V,int(paths['u'][i]),int(paths['v'][i]),
    paths['idx'][i,:paths['length'][i]].tolist(),paths['sign'][i,:paths['length'][i]].tolist(),0,4)
  legacy.append(val)
 res={'gauge_type':'random local SU2 gauge rotation of the flat identity field',
     'npaths':len(paths['u']),
     'corrected_direct_max_gauge_residual':float(np.max(np.abs(d0-d1))),
     'corrected_multihit_max_gauge_residual':float(np.max(np.abs(m0-m1))),
     'legacy_stage13_direct_max_deviation_from_flat_unity':float(np.max(np.abs(np.array(legacy)-1.))),
     'legacy_stage13_direct_mean_deviation_from_flat_unity':float(np.mean(np.abs(np.array(legacy)-1.))),
     'interpretation':'Stage13-15 legacy matrix mapping is not gauge-covariant with the original Wilson-action quaternion group law; transporter claims require correction.'}
 if res['corrected_direct_max_gauge_residual']>1e-11:raise AssertionError('new physical Wilson loop fails gauge test')
 if res['corrected_multihit_max_gauge_residual']>1e-11:raise AssertionError('new multihit fails gauge test')
 if res['legacy_stage13_direct_max_deviation_from_flat_unity']<.1:raise AssertionError('legacy warning not reproduced')
 (Path(__file__).resolve().parent/'CONVENTION_AUDIT.json').write_text(json.dumps(res,indent=2))
 return res
if __name__=='__main__': print(json.dumps(audit(),indent=2))

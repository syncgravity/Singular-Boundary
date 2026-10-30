"""Small numeric checks of exact opposite-staple obstruction and constants.
Not a proof of exterior Gibbs tail or a Penrose surgery map.
"""
import numpy as np,math,json
rng=np.random.default_rng(20261027)
q=rng.normal(size=(10000,4)); q/=np.linalg.norm(q,axis=1)[:,None]
dp=1-q[:,0];dm=1+q[:,0]
assert np.max(abs(dp+dm-2))<1e-14
ch=8/(3*math.pi**3)
cnu=14-math.log(ch)
assert abs(cnu-16.4533604045365)<1e-9
result={"opposite_staple_max_action_deviation":float(np.max(abs(dp+dm-2))),"Haar_ball_c":ch,"C_nu7":cnu,"status":"Verified obstruction and constants; absolute 3D Penrose exterior Gibbs tail NOT established"}
with open('/mnt/data/R3_exterior_surgery_2026_10_27/CHECK.json','w') as f:json.dump(result,f,indent=2)
print(result)

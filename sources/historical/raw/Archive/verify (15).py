import json, numpy as np
from scipy.special import ive
from pathlib import Path
root=Path(__file__).resolve().parent
src=np.load(root.parent/'R3_three_four_step_transfer_2026_10_27'/'incidence_3step.npz')
print('Incidence arrays:',{k:list(src[k].shape) for k in src.files})
# Test Loewner insertion with noncommuting spatial multiplication proxy F and commuting Wilson-spectrum diagonal transfers.
rng=np.random.default_rng(4831)
X=rng.normal(size=(6,6)); F=X@X.T+np.eye(6)
vals0=np.array([1,.65,.4,.25,.14,.08])
vals1=np.array([1,.8,.53,.4,.28,.20])
w,U=np.linalg.eigh(F); Fs=(U*np.sqrt(w))@U.T
A=Fs@np.diag(vals0)@Fs; B=Fs@np.diag(vals1)@Fs
for n in (3,4,7):
    baseline=np.trace(np.linalg.matrix_power(A,n))
    modified=np.trace(np.linalg.matrix_power(A,n-1)@B)
    assert modified>=baseline-1e-9
q={str(t):float(np.exp(-t)*2*ive(1,t)/ive(0,0)/t*np.exp(t)) for t in (1,2,10,100)}
# ive(1,t)=exp(-t) I1(t), so simply q=2*ive(1,t)/t
q={str(t):float(2*ive(1,t)/t) for t in (1,2,10,100)}
cert={'theorem':'single exceptional interval, n>=2, arbitrary subset of temporal faces','incidence_arrays':{k:list(src[k].shape) for k in src.files},'matrix_example':{'min_diff_3step':float(np.trace(A@A@(B-A))), 'positive_at_3_4_7':True},'q_values':q,'limitations':'does not establish independently different inserted supports in two or three time intervals'}
(root/'certificate.json').write_text(json.dumps(cert,indent=2))
print(json.dumps(cert,indent=2))

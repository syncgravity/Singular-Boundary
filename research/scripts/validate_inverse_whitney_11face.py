"""Check inverse Whitney geometry for the previously verified 11-face disk."""
import numpy as np
from pathlib import Path
p=Path(__file__).resolve().parent
candidates=[p/"global_whitney_11face.npz",Path("/mnt/data/global_whitney_11face.npz")]
match=next((x for x in candidates if x.is_file()),None)
if match is None:
 raise SystemExit("Provide global_whitney_11face.npz beside the script or under /mnt/data")
M=np.load(match)["matrix"]
assert M.shape==(30,30) and np.allclose(M,M.T)
w=np.linalg.eigvalsh(M)
assert w[0]>0
inv=np.linalg.inv(M)
wi=np.linalg.eigvalsh(inv)
assert np.allclose(wi,np.sort(1/w))
assert np.allclose(M@inv,np.eye(30),atol=1e-11)
assert np.count_nonzero(abs(M-np.diag(np.diag(M)))>1e-10)==132
assert np.count_nonzero(abs(inv-np.diag(np.diag(inv)))>1e-10)==870
print("PASS inverse Whitney SPD, spectral reciprocity and dense inverse",w[0],w[-1],wi[0],wi[-1])

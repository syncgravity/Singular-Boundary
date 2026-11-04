"""Audit whether global scalar normalization reconciles the M5 Whitney matrices."""
import numpy as np
from pathlib import Path
here=Path(__file__).resolve().parent
z=np.load(here/'m5_whitney_candidate_2026-10-30.npz')
M=z['matrix'];ids=list(map(int,z['edge_ids']));w=np.linalg.eigvalsh(M)
factors={
 'minimum_eigenvalue':.143174148694/w[0],
 'maximum_eigenvalue':1.104659344162/w[-1],
 'edge13_diagonal':.777859028095/M[ids.index(13),ids.index(13)],
}
for name,value in factors.items():print(name,'requires uniform scalar',value)
assert max(factors.values())-min(factors.values())>.5
print('PASS no uniform scalar reconciles three reported historical diagnostics')

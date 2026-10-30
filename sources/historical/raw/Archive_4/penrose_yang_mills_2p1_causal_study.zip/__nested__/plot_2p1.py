import json, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
root=Path(__file__).resolve().parent
j=json.load(open(root/'study_2p1_aggregate.json'))
fig,ax=plt.subplots(figsize=(8.3,5.2))
for M in (5,8):
    d=j[f'M{M}_geometry']['betas']['2.5']
    for geom in ('penrose','square'):
        rr=d[geom]['rectangles']
        t=np.arange(1,len(rr)+1)
        w=[v['mean'] for v in rr]
        se=[v['blocked_se'] for v in rr]
        ax.errorbar(t,w,yerr=se,marker='o',capsize=2,label=f'M={M}, {geom}')
ax.set_yscale('log')
ax.set_xlabel('Euclidean temporal separation (lattice steps)')
ax.set_ylabel('Gauge-invariant temporal Wilson rectangle')
ax.set_title(r'$SU(2)$ 2+1D Wilson loops, $\beta_\mathrm{ref}=2.5$')
ax.legend(frameon=False,fontsize=9)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(root/'temporal_wilson_rectangles.png',dpi=185)
plt.close(fig)

fig,ax=plt.subplots(figsize=(9,5))
keys=[('M5_geometry','M5 geometry, β=2.5','2.5'),('M5_uniform','M5 uniform, β=2.5','2.5'),('M5_shuffled','M5 shuffled, β=2.5','2.5'),('M8_geometry','M8 geometry, β=2.5','2.5'),('M8_uniform','M8 uniform, β=2.5','2.5'),('M5_geometry','M5 geometry, β=3.5','3.5'),('M5_uniform','M5 uniform, β=3.5','3.5'),('M8_geometry','M8 geometry, β=3.5','3.5')]
labels=[];means=[];se=[]
for key,label,beta in keys:
    x=j[key]['betas'][beta]['penrose_minus_square']['spatial_plaquette']
    labels.append(label);means.append(x['difference']);se.append(x['blocked_se'])
y=np.arange(len(keys))
ax.errorbar(means,y,xerr=se,fmt='o',capsize=3)
ax.axvline(0,linestyle='--',linewidth=1)
ax.set_yticks(y,labels)
ax.invert_yaxis()
ax.set_xlabel('Penrose − square mean spatial plaquette (blocked SE)')
ax.set_title('Incidence control versus geometric-coupling effects')
ax.grid(axis='x',alpha=.25)
fig.tight_layout()
fig.savefig(root/'causal_control_comparisons.png',dpi=185)
plt.close(fig)

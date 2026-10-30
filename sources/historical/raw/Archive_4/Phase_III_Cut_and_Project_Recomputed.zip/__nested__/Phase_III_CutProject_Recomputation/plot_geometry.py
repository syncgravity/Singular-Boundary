"""Draw the exact acceptance-window rhombi, not a generated impression."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import numpy as np
from direct_cut_project import build
fig,axes=plt.subplots(1,2,figsize=(12,6),layout='constrained')
for ax,o in zip(axes,(0,2)):
 g,gm=build(8.,o)
 polys=[g.xy[list(face)] for face in g.faces]
 area=[abs(np.linalg.det(np.vstack([p[1]-p[0],p[3]-p[0]]))) for p in polys]
 colors=['#a9cdc1' if a>0.77 else '#e7c998' for a in area]
 ax.add_collection(PolyCollection(polys,facecolors=colors,edgecolors='#273b44',linewidths=.47))
 ax.autoscale();ax.set_aspect('equal');ax.set_axis_off()
 ax.set_title(f'Z⁵ cut-and-project · offset {o}\n{len(g.labels)} vertices, {len(g.faces)} rhombi')
fig.suptitle('Verified finite Penrose P3 patches — direct acceptance-window construction',fontsize=13)
fig.savefig(Path(__file__).with_name('verified_penrose_patches.png'),dpi=170,bbox_inches='tight')

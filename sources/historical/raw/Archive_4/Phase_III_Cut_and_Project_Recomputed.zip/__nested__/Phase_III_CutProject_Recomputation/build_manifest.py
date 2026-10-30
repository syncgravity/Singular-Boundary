import json
from pathlib import Path
from direct_cut_project import build,validate
from checkpoint_wilson import fingerprint
rows=[]
for R in (5.,6.5,8.,10.):
 for o in range(5):
  g,gm=build(R,o)
  rows.append({'physical_cutoff':R,'offset':o,'graph_sha256':fingerprint(g,gm),
               'gamma':gm.tolist(),**validate(g,gm)})
Path(__file__).with_name('geometry_manifest.json').write_text(json.dumps(rows,indent=2))
print('independently validated graphs',len(rows))

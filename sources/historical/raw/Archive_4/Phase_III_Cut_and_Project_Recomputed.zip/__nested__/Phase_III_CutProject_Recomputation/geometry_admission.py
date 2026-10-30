"""Run the *unchanged prespecified* admission gate on direct-window Penrose inputs.

Periodic rationalized directions are provisional, not canonical Penrose
substitution supercells; no passing or failing result is a causal claim.
"""
import json
from pathlib import Path
from direct_cut_project import build,validate
from provisional_periodic import periodic
from admission_metrics import ball,profile,cmp,admitted,THRESHOLDS
base=Path(__file__).parent
ps=[(o,build(14.,o)[0]) for o in range(4)]
qs=[(q,o,periodic(q,o)[0]) for q in (6,8,10,13) for o in range(2)]
rows=[]
for n in (100,180,260):
 for po,p in ps:
  z=profile(p,ball(p,n))
  for q,qo,h in qs:
   r={'size':n,'penrose_offset':po,'q':q,'periodic_offset':qo,**cmp(z,profile(h,ball(h,n)))}
   r['admitted']=admitted(r);rows.append(r)
 vals=[x for x in rows if x['size']==n]
 print('N',n,'pairs',len(vals),'pass',sum(x['admitted'] for x in vals),
       'best_r1',min(x['radius1_tv'] for x in vals),'best_r2',min(x['radius2_tv'] for x in vals),flush=True)
out={'description':'Independent window-first Penrose versus provisional rational-grid torus controls',
     'thresholds':THRESHOLDS,'rows':rows}
(base/'admission_results.json').write_text(json.dumps(out,indent=2))

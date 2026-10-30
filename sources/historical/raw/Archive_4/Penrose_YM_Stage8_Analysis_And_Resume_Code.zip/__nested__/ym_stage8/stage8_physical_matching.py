"""A source-distance matching *screen*, not physical scale calibration.

Uses the 100-path Stage 7 geometry plans (distinct physical separations only).
No Wilson-loop potential or renormalized physics is inferred from geometry alone.
"""
import argparse,csv,json
from pathlib import Path
import numpy as np

def evaluate(penrose_plan,square_plan,threshold=.05):
    p=json.loads(Path(penrose_plan).read_text());s=json.loads(Path(square_plan).read_text())
    a=np.sort(np.unique(np.asarray(p['path_lengths_m'],float)))
    b=np.sort(np.unique(np.asarray(s['path_lengths_m'],float)))
    rows=[]
    for r in b:
        x=float(a[np.argmin(np.abs(a-r))])
        relative=abs(x-r)/((x+r)/2)
        rows.append({'square_r':float(r),'penrose_r':x,'relative_mismatch':float(relative),
                     'matched_within_5pct':bool(relative<=threshold)})
    return {'source':'Stage 7 deterministic 100-source spatial path plans',
            'threshold':threshold,'matched_distinct_r':sum(int(x['matched_within_5pct']) for x in rows),
            'total_distinct_square_r':len(rows),'pairs':rows,
            'not_established':['same path orientation distribution','same long-distance static potential',
                              'renormalized coupling/anisotropy matching','matched continuum theory']}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--penrose',default='penrose_measurement_plan.json');ap.add_argument('--square',default='square_measurement_plan.json');ap.add_argument('--out',default='stage8_physical_matching.json');args=ap.parse_args()
 obj=evaluate(args.penrose,args.square)
 Path(args.out).write_text(json.dumps(obj,indent=2))
 print('physical geometry bins within 5%:',obj['matched_distinct_r'],'/',obj['total_distinct_square_r'])

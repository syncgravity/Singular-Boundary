#!/usr/bin/env python3
"""Full Penrose-anchor strict-threshold enhanced catalogue screening."""
import json,time,argparse
from pathlib import Path
import numpy as np
from stage19_full import setup_geometry
from diagnose_missing import screen,summary

def main():
 p=argparse.ArgumentParser();p.add_argument('--variants',type=int,default=4);p.add_argument('--output',default='/mnt/data/stage19_target_diagnostic');a=p.parse_args()
 sp,_=setup_geometry('penrose',20,3.5);roots=np.arange(int(sp['F']),dtype=np.int64);thresholds=(1.5,1.65,1.8,2.0,2.25)
 start=time.perf_counter();sizes=(2,3,4,5,6,7,8,9,10,12,15);data=screen(sp,roots,sizes,a.variants,thresholds)
 out=Path(a.output);out.mkdir(exist_ok=True,parents=True);r=summary(data,thresholds);r.update({'total_roots':len(roots),'sizes':sizes,'variants':a.variants,'threshold_used_for_admission':1.5,'seconds':time.perf_counter()-start,'geometry_hash':sp['graph_hash']})
 (out/'FULL_EXPANDED_REPORT.json').write_text(json.dumps(r,indent=2));np.savez_compressed(out/'full_expanded_per_anchor.npz',anchors=roots,min_distance=data['min_distance'],best_size=data['size'],best_target=data['target'],candidate_counts=data['candidate_counts'],features=data['feature'])
 print(json.dumps(r,indent=2),flush=True)
if __name__=='__main__':main()

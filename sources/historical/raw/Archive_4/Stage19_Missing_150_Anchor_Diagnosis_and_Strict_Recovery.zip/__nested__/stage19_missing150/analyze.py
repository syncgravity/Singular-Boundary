import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.stats import ks_2samp,mannwhitneyu
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components,shortest_path
BASE=Path('/mnt/data/stage19_target_first');sys.path.insert(0,str(BASE))
from stage19_full import setup_geometry,neighbors
from diagnose_missing import screen
OUT=Path('/mnt/data/stage19_missing150');OUT.mkdir(exist_ok=True)
f=np.load('/mnt/data/stage19_strict_expanded/all_anchors_strict_min_distance.npz');sp,_=setup_geometry('penrose',20,3.5)
F=int(sp['F']);missing=np.flatnonzero(~f['covered']);accepted=np.flatnonzero(f['covered']);adj=neighbors(sp)
areas=np.asarray(sp['face_areas']);degree=np.array([len(a) for a in adj]);nbrmean=np.array([np.mean(areas[list(a)]) if a else np.nan for a in adj]);nbrdeg=np.array([np.mean(degree[list(a)]) if a else np.nan for a in adj])
rows=[];cols=[]
for i,a in enumerate(adj):
 for j in a:rows.append(i);cols.append(j)
G=csr_matrix((np.ones(len(rows),dtype=np.int8),(rows,cols)),shape=(F,F));missG=G[missing,:][:,missing];cc,lab=connected_components(missG,directed=False); sizes=np.bincount(lab); local=np.array(G[missing,:][:,missing].sum(axis=1)).ravel()
# minimum edge-hop separation between different missing roots, via first 2 hops
is_missing=np.zeros(F,bool);is_missing[missing]=True
near_missing=np.array([sum(is_missing[list(adj[i])]) for i in range(F)])
stats={}
for label,vals in [('face_area',areas),('adjacent_face_count',degree),('mean_neighbor_area',nbrmean),('mean_neighbor_degree',nbrdeg)]:
 a=vals[missing];b=vals[accepted];stats[label]={'missing_mean':float(np.mean(a)),'covered_mean':float(np.mean(b)),'missing_median':float(np.median(a)),'covered_median':float(np.median(b)),'ks_statistic':float(ks_2samp(a,b).statistic),'ks_pvalue_descriptive_spatial_dependence':float(ks_2samp(a,b).pvalue),'missing_unique_values':{str(round(v,7)):int(n) for v,n in zip(*np.unique(np.round(a,7),return_counts=True))} if label in ('face_area','adjacent_face_count') else None}
# Distances and face-count failure composition: original best features for already scanned
failure={'minimum_distance_quantiles':np.quantile(f['minimum_distance'][missing],[0,.1,.25,.5,.75,.9,1]).tolist(),'best_size_distribution':{str(int(v)):int(n) for v,n in zip(*np.unique(f['best_size'][missing],return_counts=True))},'best_target_distribution':{str(int(v)):int(n) for v,n in zip(*np.unique(f['best_target'][missing],return_counts=True))}}
# probe wider variants on the same 150 roots (strict criterion preserved). Existing deterministic grow has 4 variants; test 8, and extra sizes up to 19. 
start=time.monotonic();sc=screen(sp,missing,(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19),8,(1.5,));elapsed=time.monotonic()-start
recover=sc['min_distance']<=1.5
stats2={'anchors':F,'missing':len(missing),'covered':len(accepted),'graph_hash':sp['graph_hash'],'missing_anchor_ids_sha256':hashlib.sha256(missing.astype('<i8').tobytes()).hexdigest(),'missing_neighbor_edges':int(missG.nnz//2),'isolated_missing_anchors':int(np.sum(local==0)),'missing_connected_components':int(cc),'largest_missing_component':int(sizes.max()),'missing_component_size_histogram':{str(int(v)):int(n) for v,n in zip(*np.unique(sizes,return_counts=True))},'local_geometry':stats,'previous_best_failures':failure,'extended_search':{'sizes':list(range(2,20)),'variants':8,'threshold_unchanged':1.5,'additional_recovered':int(recover.sum()),'still_missing':int((~recover).sum()),'elapsed_seconds':elapsed,'newly_recovered_anchor_ids':missing[recover].tolist(),'remaining_anchor_ids':missing[~recover].tolist(),'new_minimum_distance_quantiles':np.quantile(sc['min_distance'],[0,.25,.5,.75,1]).tolist()},'caveats':['Candidate enumeration is deterministic and finite, not an exhaustive search over all face clusters.','KS p-values treat spatially correlated anchors as independent and should not be used as formal significance tests.','Full-volume scalar control is unchanged; no mass measurement performed.']}
(OUT/'REPORT.json').write_text(json.dumps(stats2,indent=2))
np.savez_compressed(OUT/'missing_anchor_diagnostics.npz',missing_anchor_ids=missing,accepted_anchor_ids=accepted,face_area=areas,face_neighbor_count=degree,mean_neighbor_area=nbrmean,neighbor_missing_count=near_missing,previous_best_distance=f['minimum_distance'],previous_best_size=f['best_size'],previous_best_target=f['best_target'],new_search_distance=sc['min_distance'],new_search_size=sc['size'],new_search_target=sc['target'],newly_recovered=missing[recover],remaining_missing=missing[~recover])
print(json.dumps({k:v for k,v in stats2.items() if k not in ('local_geometry',)},indent=2),flush=True)
print('local',json.dumps(stats,indent=2),flush=True)

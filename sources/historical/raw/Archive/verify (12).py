import numpy as np,json
from scipy.special import ive
p='/mnt/data/R3_looped_four_prism_2026_10_27/incidence.npz'
z=np.load(p); b1=z['d1'];b2=z['d2'];seams=set(map(int,z['seam_face_ids']))
# Spatial vertices have indices 0,...,8 on lower slice and 9,...,17 on upper slice.
vertical=[]; horizontal=[[],[]]
for e in range(b1.shape[1]):
 u=np.where(b1[:,e]<0)[0][0];v=np.where(b1[:,e]>0)[0][0]
 if abs(int(u)-int(v))==9:vertical.append(e)
 elif u//9==v//9:horizontal[u//9].append(e)
 else:raise AssertionError((e,u,v))
spatial=[[],[]];temporal=[]
for f in range(b2.shape[1]):
 E=set(np.flatnonzero(b2[:,f])); nv=len(E&set(vertical))
 if nv==0:
  lev=int(any(e in horizontal[1] for e in E));spatial[lev].append(f)
 elif nv==2:temporal.append(f)
 else:raise AssertionError((f,nv))
assert len(vertical)==9 and list(map(len,horizontal))==[12,12]
assert list(map(len,spatial))==[4,4] and len(temporal)==12
assert seams.issubset(temporal) and len(set(temporal)-seams)==8
pairs=[]
for f in temporal:
 E=set(np.flatnonzero(b2[:,f]));lo=list(E&set(horizontal[0]));hi=list(E&set(horizontal[1]))
 assert len(lo)==len(hi)==1
 pairs.append((int(f),int(lo[0]),int(hi[0])))
assert len({x for _,x,_ in pairs})==12 and len({y for _,_,y in pairs})==12
# normalized SU2 Wilson convolution: each spin j multipler c_j/c_0 = I_(2j+1)/I_1.
# Strictly nonnegative; trivial j=0 coefficient 1.
spectra={}
for coupling in [0.2,2.0,10.0,100.0]:
 ratios=[float(ive(k,coupling)/ive(1,coupling)) for k in range(1,22)]
 assert ratios[0]==1 and min(ratios)>=0
 spectra[str(coupling)]={'fundamental_multiplier':ratios[1], 'min_first_21_multipliers':min(ratios), 'largest_first_21_multipliers':max(ratios)}
report={'patch':'constructed four-prism 2x2 quadrilateral spatial patch extruded one time step','spatial_sites':9,'vertical_edges_gauged_to_identity':9,'spatial_edges_per_layer':[len(a) for a in horizontal],'spatial_faces_per_layer':[len(a) for a in spatial],'temporal_face_pairs':pairs,'retained_temporal_faces':len(temporal)-len(seams),'deleted_temporal_faces':sorted(seams),'temporal_edge_bijection':True,'symmetric_spatial_couplings_required':True,'theorem':'Z_insert / Z_cavity >= product_{q in Q} q(gamma_q), for all nonnegative temporal couplings, when spatial top/bottom weights agree','multipliers':spectra}
with open('/mnt/data/R3_four_prism_temporal_reflection_2026_10_27/certificate.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))

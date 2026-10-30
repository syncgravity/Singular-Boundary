"""Stage 7: exact vectorized 2+1D SU(2) Wilson action on large 5-grid torus.
Build validated modelset torus and area-matched square reference; no spectroscopic claims.
Adjacent lists are built without Python's O(nt*links) loops.
"""
import json,hashlib,time
from pathlib import Path
import numpy as np
from stage2_rational_torus import build_torus
from stage3_periodic_pilot import square_torus
from stage2_ym_calibration import quadratic_weights

SCALE=55; NX=151;NY=151;NT=20;BETA=3.5

def pair():
    q=build_torus(SCALE)
    r=square_torus(NX,NY,q['physical_area'])
    return q,r

def assemble_vectorized(sp,nt,beta_ref,a_ref):
    E=int(sp['E']);V=int(sp['V']);F=int(sp['F'])
    assert nt>=4
    L=nt*(E+V);P=nt*(F+E)
    face=np.asarray(sp['face_idx'],np.int32)
    sgsp=np.asarray(sp['face_sign'],np.int8)
    edges=np.asarray(sp['edges'],np.int32)
    ts=np.arange(nt,dtype=np.int32)
    fsp=ts[:,None,None]*E+face[None,:,:]
    tedge=ts[:,None]*E+np.arange(E,dtype=np.int32)[None,:]
    nxtedge=((ts+1)%nt)[:,None]*E+np.arange(E,dtype=np.int32)[None,:]
    temporal=nt*E+ts[:,None]*V
    ft=np.stack([tedge,temporal+edges[None,:,1],nxtedge,temporal+edges[None,:,0]],axis=2)
    fi=np.empty((nt,F+E,4),np.int32)
    fi[:,:F,:]=fsp;fi[:,F:,:]=ft
    fi=fi.reshape(P,4)
    sg=np.empty((nt,F+E,4),np.int8)
    sg[:,:F,:]=sgsp[None,:,:]
    sg[:,F:,:]=[1,1,-1,-1]
    sg=sg.reshape(P,4)
    ids=fi.ravel();cnt=np.bincount(ids,minlength=L)
    if np.min(cnt)!=3 and sp['spatial_kind']=='rational_modelset_torus':
        raise ValueError('expected torus spatial links 4 incident plaquettes, no boundary')
    if np.any(cnt<=0):raise ValueError('unused gauge links')
    order=np.argsort(ids,kind='stable')
    start=np.zeros(L+1,np.int64);start[1:]=np.cumsum(cnt)
    slot=np.arange(len(ids),dtype=np.int64)-start[ids[order]]
    adj=np.full((L,int(cnt.max())),-1,dtype=np.int32)
    adj[ids[order],slot]=(order//4).astype(np.int32)
    calibration=quadratic_weights(sp,a_ref,a_ref,beta_ref)
    beta=np.tile(np.concatenate([calibration['beta_s'],calibration['beta_t']]),nt)
    return {'fi':fi,'sg':sg,'adj':adj,'degree':cnt.astype(np.int32),'beta':beta,
        'nt':nt,'V':V,'E':E,'F':F,'L':L,'P':P,'calibration':calibration}

def exact_checks(sp,lat):
    fi=lat['fi'];sg=lat['sg'];nt=lat['nt'];E=lat['E'];V=lat['V'];F=lat['F']
    face_usage=np.bincount(sp['face_idx'].ravel(),minlength=E)
    assert np.all(face_usage==2)
    assert np.all(lat['degree'][:nt*E].reshape(nt,E)==4)
    degree=np.bincount(np.asarray(sp['edges']).ravel(),minlength=V)
    assert np.array_equal(lat['degree'][nt*E:].reshape(nt,V),np.broadcast_to(degree,(nt,V)))
    assert np.array_equal(lat['adj'][fi.ravel(),np.zeros(fi.size,dtype=np.int32)].shape, (fi.size,))
    # Face chain boundary closure via oriented source/dest vertex arrays; handles seam winding.
    n=nt*V
    spatial_end=np.empty((nt,E,2),np.int32)
    spatial_end[:,:,0]=np.arange(nt)[:,None]*V+sp['edges'][None,:,0]
    spatial_end[:,:,1]=np.arange(nt)[:,None]*V+sp['edges'][None,:,1]
    temporal_end=np.empty((nt,V,2),np.int32)
    temporal_end[:,:,0]=np.arange(nt)[:,None]*V+np.arange(V)[None,:]
    temporal_end[:,:,1]=((np.arange(nt)+1)%nt)[:,None]*V+np.arange(V)[None,:]
    end=np.concatenate([spatial_end.reshape(nt*E,2),temporal_end.reshape(nt*V,2)])
    a=np.where(sg==1,end[fi,0],end[fi,1]);b=np.where(sg==1,end[fi,1],end[fi,0])
    if not np.array_equal(b,np.roll(a,-1,axis=1)):
        raise AssertionError('plaquette orientations not closed')
    return {'n_spatial_face_incidence':int(face_usage.size), 'all_spatial_degree_four':True,
            'time_link_incidence_max':int(degree.max()),'closure':True}

def audit(outdir):
    t=time.monotonic();P,W=pair()
    area=P['physical_area'];a=(area/P['F'])**.5
    reports={}
    for name,sp in [('Penrose_M55',P),('square_151x151',W)]:
        lat=assemble_vectorized(sp,NT,BETA,a)
        chk=exact_checks(sp,lat)
        result={'V':sp['V'],'E':sp['E'],'F':sp['F'],'L':lat['L'],'P':lat['P'],'nt':NT,'area':sp['physical_area'],
           'periods':sp['periods'].tolist(),'ref_spacing':a,'tree_level_eigs':lat['calibration']['eig'].tolist(),
           'calibrated_beta_spatial_range':lat['calibration']['spatial_beta_range'],
           'calibrated_beta_temporal_range':lat['calibration']['temporal_beta_range'],
           'checks':chk,'graph_hash':sp['graph_hash'],'source':'corrected model-set for Penrose; square with matched area'}
        reports[name]=result
        print(name,'V E F',sp['V'],sp['E'],sp['F'],'spacetime links',lat['L'],'plaquettes',lat['P'],flush=True)
    reports['conditions']={'local_motif_gate_M55':'previous Stage 2 radius-2 TV=.0821 threshold=.15; toroidal bulk',
       'reference_beta':BETA, 'physical_volume_scale':'area is fixed between pair only; no continuum or renormalized tuning',
       'production_status':'NOT RUN: ensemble / scalar mass / flux signal unavailable',
       'elapsed_seconds':time.monotonic()-t}
    outdir=Path(outdir);outdir.mkdir(exist_ok=True,parents=True)
    (outdir/'stage7_action_audit.json').write_text(json.dumps(reports,indent=2))
    return reports

if __name__=='__main__': audit(Path(__file__).resolve().parent)

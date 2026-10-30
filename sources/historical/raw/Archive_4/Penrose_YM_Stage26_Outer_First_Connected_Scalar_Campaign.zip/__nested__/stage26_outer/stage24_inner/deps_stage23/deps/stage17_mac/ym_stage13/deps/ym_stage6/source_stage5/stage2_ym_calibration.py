"""2+1D SU(2) corrected Penrose: tree-level quadratic response calibration and comparison pilots.

Never identifies calibrated quadratic response with nonperturbative scale setting.
Uses direct-cut/project *open* disks, plus a square *open* rectangle for a
necessary software reference. The square is NOT a locally matched periodic
Penrose approximant. All simulations are exploratory unless separately certified.
"""
from __future__ import annotations
import json, argparse, hashlib
from pathlib import Path
import numpy as np
from corrected_2p1_pilot import (geometry,extrude_open,run_chain,face_cluster_loops,
                                 make_paths,summarize,rect_path)
from direct_cut_project import Complex


def square_rectangle(nx,ny,physical_area):
    if nx<3 or ny<3: raise ValueError('square grid needs >=3 cells per direction')
    a=float(np.sqrt(physical_area/(nx*ny)))
    xy=np.array([((i-nx/2)*a,(j-ny/2)*a) for j in range(ny+1) for i in range(nx+1)],float)
    node=lambda i,j:j*(nx+1)+i
    faces=[(node(i,j),node(i+1,j),node(i+1,j+1),node(i,j+1))
           for j in range(ny) for i in range(nx)]
    edges=sorted({tuple(sorted((face[k],face[(k+1)%4]))) for face in faces for k in range(4)})
    edge_ids={e:k for k,e in enumerate(edges)}
    fidx=[];fsg=[]
    for face in faces:
        ids=[];sg=[]
        for k in range(4):
            u,v=face[k],face[(k+1)%4]
            ids.append(edge_ids[min(u,v),max(u,v)]); sg.append(1 if u<v else -1)
        fidx.append(ids); fsg.append(sg)
    graph_hash=hashlib.sha256(json.dumps([nx,ny,physical_area],sort_keys=True).encode()).hexdigest()
    return dict(V=len(xy),E=len(edges),F=len(faces),xy=xy,
                edges=np.asarray(edges,np.int64),face_idx=np.asarray(fidx,np.int64),
                face_sign=np.asarray(fsg,np.int64),face_areas=np.full(nx*ny,a*a),
                graph_hash=graph_hash,stats={'vertices':len(xy),'edges':len(edges),
                'faces':len(faces),'euler':1,'boundary_edges':2*(nx+ny)},
                g=Complex([],xy,faces,edges),spatial_kind='square_open_rectangle',
                nx=nx,ny=ny,spacing=a)


def quadratic_weights(sp,a_ref,a_time,beta_ref=2.):
    """Positive geometric diagonal Hodge *candidate*, derived by homogeneous weak-field response.

    Spatial: beta_f=beta_ref*a_ref*a_time/A_f.
    Temporal: beta_e=beta_ref*a_ref/a_time*(sum_{f incident e} A_f/2)/|edge|^2.

    Boundary weights are *half-face* for an edge incident to one face.
    The tensor T=at^2*sum beta_e dx_e dx_e^T should approximate S*I,
    S=sum beta_f A_f^2. This averages the continuum weak-field action
    and does not establish its local correctness or physical renormalized scale.
    """
    areas=np.asarray(sp['face_areas'],float)
    d=np.asarray(sp['edge_vectors'] if 'edge_vectors' in sp else (np.asarray(sp['xy'])[sp['edges'][:,1]]-np.asarray(sp['xy'])[sp['edges'][:,0]]))
    lengths2=np.einsum('ij,ij->i',d,d)
    if min(lengths2)<=0:raise ValueError('zero-length spatial edge')
    dual=np.zeros(sp['E'])
    use=np.zeros(sp['E'],np.int64)
    for i,faces in enumerate(sp['face_idx']):
        for e in faces:
            dual[e]+=areas[i]/2
            use[e]+=1
    if not np.all(np.isin(use,(1,2))): raise ValueError('invalid face adjacency')
    bfs=beta_ref*a_ref*a_time/areas
    bte=beta_ref*a_ref/a_time*dual/lengths2
    S=np.dot(bfs,areas**2)
    T=a_time**2*np.einsum('e,ei,ej->ij',bte,d,d)
    eig=np.linalg.eigvalsh(T/S)
    residual=float(np.linalg.norm(T/S-np.eye(2),'fro'))
    anisotropy=float((max(eig)-min(eig))/np.mean(eig))
    # Gauge-independent, purely geometric coefficients
    return {'beta_s':bfs,'beta_t':bte,'edge_incidence':use,'dual_area':dual,
            'edge_lengths':np.sqrt(lengths2),'a_ref':float(a_ref),'a_time':float(a_time),
            'S':float(S),'T':T,'eig':eig,'response_residual':residual,
            'directional_anisotropy':anisotropy,
            'spatial_beta_range':[float(min(bfs)),float(max(bfs))],
            'temporal_beta_range':[float(min(bte)),float(max(bte))],
            'boundary_beta_t_over_interior_mean':float(np.mean(bte[use==1])/np.mean(bte[use==2])) if np.any(use==1) else None}


def assemble(sp,nt,beta_ref,a_ref,a_time):
    lat=extrude_open(sp,nt,float(beta_ref))
    cal=quadratic_weights(sp,a_ref,a_time,beta_ref)
    for t in range(nt):
        lat['beta'][t*(sp['F']+sp['E']):t*(sp['F']+sp['E'])+sp['F']]=cal['beta_s']
        lat['beta'][t*(sp['F']+sp['E'])+sp['F']:(t+1)*(sp['F']+sp['E'])]=cal['beta_t']
    return lat,cal


def geometric_screen(radii=(3.5,5.,6.5,8.), offsets=(0,1,2,3), nx=8,ny=9):
    out=[]
    for r in radii:
        for off in offsets:
            sp=geometry(r,off)
            a_ref=np.sqrt(sp['face_areas'].mean())
            ca=quadratic_weights(sp,a_ref,a_ref)
            out.append({'kind':'Penrose_open', 'radius':r,'offset':off,'V':sp['V'],'E':sp['E'],
                        'F':sp['F'],'physical_area':float(sum(sp['face_areas'])),
                        'quadratic_response_eigs':ca['eig'].tolist(),
                        'directional_anisotropy':ca['directional_anisotropy'],
                        'frobenius_residual':ca['response_residual'],
                        'trace_response':float(np.trace(ca['T'])/ca['S']),
                        'spatial_beta_range':ca['spatial_beta_range'],
                        'temporal_beta_range':ca['temporal_beta_range']})
    return out


def pilot(sp,nt,beta_ref,area_ref,reference_faces,seeds,burn,steps,thin,maxpath=3,per_size=10):
    a_ref=float(np.sqrt(area_ref/reference_faces)) # common mean Penrose face-area length for both geometries
    lat,ca=assemble(sp,nt,beta_ref,a_ref,a_ref)
    # Square faces all have equal physical area: create a checkerboard split for
    # the *operator basis only*, while keeping real geometry/action untouched.
    if sp.get('spatial_kind')=='square_open_rectangle':
        op_sp=dict(sp)
        op_sp['face_areas']=np.where(np.arange(sp['F'])%2==0,1.,2.)
        basis=face_cluster_loops(op_sp)
        operator_names=['checkerboard_even','checkerboard_odd','adjacent_pair']
    else:
        basis=face_cluster_loops(sp)
        operator_names=['thin','thick','adjacent_pair']
    paths=make_paths(sp,max_steps=maxpath,per_size=per_size)
    if len(paths['length'])==0: raise ValueError('no interior Wilson paths')
    snaps={};chain_stats={}
    for seed in seeds:
        links,actions,acc,err=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],
                                         int(seed),burn,steps,thin,.95)
        if err>1e-9:raise AssertionError('plaquette cache mismatch')
        snaps[str(seed)]=links
        chain_stats[str(seed)]={'action_mean':float(actions.mean()),'acceptance_rate':float(acc),
                                'cache_error':float(err),'configurations':len(links)}
    sm=summarize(snaps,nt,sp['E'],sp['V'],basis,paths,B=200)
    sm['scalar_operator_names']=operator_names
    return {'calibration':{'reference_faces':reference_faces,'a_ref':ca['a_ref'],'a_time':ca['a_time'],
                           'quadratic_response_eigs':ca['eig'].tolist(),
                           'directional_anisotropy':ca['directional_anisotropy'],
                           'spatial_beta_range':ca['spatial_beta_range'],
                           'temporal_beta_range':ca['temporal_beta_range']},
            'geometry':{'V':sp['V'],'E':sp['E'],'F':sp['F'],
                        'physical_area':float(np.sum(sp['face_areas'])),'hash':sp['graph_hash']},
            'lattice':{'nt':nt,'L':lat['L'],'P':lat['P'],'spatial_boundary':'open','time':'periodic'},
            'sampling':{'beta_ref':beta_ref,'seeds':list(seeds),'burn':burn,'steps':steps,'thin':thin},
            'chain_stats':chain_stats,'observables':sm,
            'admission':{'mass':'NO: t>=2 signal/fit plateau and multichain diagnostics missing',
                         'sigma':'NO: large-R/T potential plateau and reliable physical-R bins missing',
                         'continuum':'NO: neither continuum spacings nor renormalized scale matching'}},snaps,paths


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--screen',action='store_true')
    ap.add_argument('--pilot',action='store_true')
    ap.add_argument('--only',choices=['penrose','square','both'],default='both')
    ap.add_argument('--outdir',default=str(Path(__file__).resolve().parent/'outputs'))
    ap.add_argument('--radius',type=float,default=5.)
    ap.add_argument('--beta',type=float,default=2.)
    ap.add_argument('--nt',type=int,default=8)
    ap.add_argument('--burn',type=int,default=60)
    ap.add_argument('--steps',type=int,default=120)
    ap.add_argument('--thin',type=int,default=4)
    ap.add_argument('--seeds',type=int,nargs='+',default=[101,211])
    a=ap.parse_args()
    out=Path(a.outdir);out.mkdir(parents=True,exist_ok=True)
    if a.screen:
        screen=geometric_screen()
        (out/'quadratic_calibration_screen.json').write_text(json.dumps(screen,indent=2))
        for r in sorted({x['radius'] for x in screen}):
            v=[x for x in screen if x['radius']==r]
            print('radius',r,'anisotropy range',round(min(x['directional_anisotropy'] for x in v),6),
                  round(max(x['directional_anisotropy'] for x in v),6),flush=True)
    if a.pilot:
        sp=geometry(a.radius,0)
        area=float(sum(sp['face_areas']))
        nx=max(3,int(np.floor(np.sqrt(sp['F']))))
        ny=max(3,int(np.round(sp['F']/nx)))
        sq=square_rectangle(nx,ny,area)
        for name,g in [('penrose',sp),('square',sq)]:
            if a.only not in ('both',name):continue
            print('RUNNING',name,'links',a.nt*(g['V']+g['E']),flush=True)
            r,s,p=pilot(g,a.nt,a.beta,area,sp['F'],a.seeds,a.burn,a.steps,a.thin)
            (out/f'{name}_pilot.json').write_text(json.dumps(r,indent=2))
            (out/f'{name}_paths.json').write_text(json.dumps(p['meta'],indent=2))
            np.savez_compressed(out/f'{name}_configs.npz',**{'seed_'+k:v for k,v in s.items()})
            print(name,'n',r['observables']['n_configs'],'t2 SNR',r['observables']['scalar_diag_signal_to_noise_t2'],flush=True)

if __name__=='__main__':main()

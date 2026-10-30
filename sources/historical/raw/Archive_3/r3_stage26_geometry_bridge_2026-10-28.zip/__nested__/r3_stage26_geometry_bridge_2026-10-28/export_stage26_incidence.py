#!/usr/bin/env python3
"""Export the *actual Stage26 simulation plaquette-edge incidence*.

Run in the stage26_outer directory with upstream stage24_inner/deps_stage23 on disk.
Provide explicit insertion face IDs and fixed link indices to make an R3 partition.
This does NOT identify the original historical 12-prism R3 geometry by itself.
"""
import argparse, hashlib, json, pathlib, sys
import numpy as np


def read_ids(path):
    if path is None: return None
    x=json.loads(pathlib.Path(path).read_text())
    if not isinstance(x,list) or not all(isinstance(v,int) and not isinstance(v,bool) and v>=0 for v in x):
        raise ValueError('Index file must be JSON list of nonnegative integer indices')
    if len(set(x))!=len(x): raise ValueError('Repeated index')
    return x


def extract(lat, g, kind, beta, q_indices=None, fixed_indices=None):
    if 'fi' not in lat or 'sg' not in lat:
        raise ValueError('Missing lat[fi] or lat[sg]')
    fi=np.asarray(lat['fi']); sg=np.asarray(lat['sg'])
    if fi.ndim!=2 or fi.shape!=sg.shape:
        raise ValueError(f'Expected matching 2D fi and sg arrays, got {fi.shape} vs {sg.shape}; inspect stage22 representation')
    if fi.dtype.kind not in 'iu' or sg.dtype.kind not in 'iu':
        raise ValueError('fi and sg must be integer arrays')
    # Stage26 get_plaquettes() may use different packing conventions. Fail closed.
    if np.any(fi<0) or not np.all(np.isin(sg,[-1,1])):
        raise ValueError('fi contains negative padding or sg contains non-±1 values; inspect get_plaquettes() packing before export')
    face_count=int(fi.shape[0]); edge_count=int(fi.max())+1
    if len(np.unique(fi))!=edge_count:
        raise ValueError('Edge indices are not contiguous 0..max: inspect underlying representation')
    fixed_indices=fixed_indices or []
    q_indices=q_indices or []
    if any(i>=face_count for i in q_indices): raise ValueError('Insertion face index out of range')
    if any(i>=edge_count for i in fixed_indices): raise ValueError('Fixed edge index out of range')
    if any(len(set(int(e) for e in row))!=len(row) for row in fi):
        raise ValueError('A face repeats an edge index: incidence export supports this, but audit needs occurrence-aware review')
    faces={f'f:{i}':[[f'e:{int(e)}',int(s)] for e,s in zip(fi[i],sg[i])] for i in range(face_count)}
    fixed={f'e:{i}' for i in fixed_indices}
    q={f'f:{i}' for i in q_indices}
    payload={
      'schema':'stage26-simulation-incidence-v1',
      'warning':'Simulation face list, not a certified historical R3 12-prism subcomplex. Q and fixed edges explicitly supplied by operator, not inferred.',
      'kind':kind, 'nt':20,'beta':beta,'spatial_graph_hash':str(g.get('graph_hash','')),
      'source_array_sha256':hashlib.sha256(fi.tobytes()+sg.tobytes()).hexdigest(),
      'source_array_shapes':{'fi':list(fi.shape),'sg':list(sg.shape)},
      'edges':{f'e:{i}':None for i in range(edge_count)},
      'faces':faces,
      'inserted_faces':sorted(q,key=lambda x:int(x.split(':')[1])),
      'cavity_faces':[f'f:{i}' for i in range(face_count) if f'f:{i}' not in q],
      'excluded_faces':[],
      'fixed_edges':sorted(fixed,key=lambda x:int(x.split(':')[1])),
      'integrated_edges':[f'e:{i}' for i in range(edge_count) if f'e:{i}' not in fixed],
      'partition_certified':bool(q_indices is not None and fixed_indices is not None),
      'note':'Without --q and --fixed, audit treats all faces as cavity and all edges integrated for exploratory inventory only; not an R3 insertion estimate.'
    }
    return payload

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--kind',choices=['penrose','square'],default='penrose')
    ap.add_argument('--nt',type=int,default=20)
    ap.add_argument('--beta',type=float,default=3.5)
    ap.add_argument('--q',help='JSON list of zero-based Stage26 plaquette indices to insert')
    ap.add_argument('--fixed',help='JSON list of zero-based Stage26 link indices fixed by the relevant boundary condition')
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    root=pathlib.Path(__file__).resolve().parent
    # resolve upstream modules from invocation cwd first, then script parent
    candidates=[pathlib.Path.cwd()/'stage24_inner'/'deps_stage23',root/'stage24_inner'/'deps_stage23',pathlib.Path.cwd()/'stage24_inner']
    for c in candidates:
        if c.exists():sys.path.insert(0,str(c))
    try:from stage22_shifted import setup_geometry
    except ImportError as e:raise SystemExit('Cannot import stage22_shifted: run from stage26_outer directory, ensuring stage24_inner/deps_stage23 exists') from e
    g,lat=setup_geometry(args.kind,args.nt,args.beta)
    data=extract(lat,g,args.kind,args.beta,read_ids(args.q),read_ids(args.fixed))
    data['nt']=args.nt
    pathlib.Path(args.out).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'out':args.out,'face_count':len(data['faces']),'edge_count':len(data['edges']),
      'q_count':len(data['inserted_faces']),'fixed_count':len(data['fixed_edges']),
      'graph_hash':data['spatial_graph_hash'],'partition_certified':data['partition_certified']},indent=2))

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Build auditable 3-step SU(2) prism incidence from an EXPLICIT oriented spatial cell complex.
No inference from path catalogues. Python >=3.9; standard library only.
Input schema: {vertices:[id,...], edges:[{id,u,v},...], faces:[{id,boundary:[[edge_id,+1|-1],...]}],
  fixed_spatial_edges:[id,...] (optional), fixed_temporal_vertices:[id,...] (optional),
  fixed_boundary_edges:[full_extruded_edge_id,...] (optional),
  q:[full_extruded_face_id,...] (optional),
  cavity_excluded_faces:[full_extruded_face_id,...] (optional),
  boundary_policy:'explicit' (required)}.
Temporal and spatial edges oriented toward +t and along supplied edges.
Face orientations: spatial inherited; temporal word spatial(t),time(v),spatial(t+1)^-1,time(u)^-1.
"""
import argparse,json,collections,hashlib,pathlib

def parity_rank(rows):
    basis={}
    for bits in rows:
        x=bits
        while x:
            p=x.bit_length()-1
            if p in basis: x^=basis[p]
            else: basis[p]=x;break
    return len(basis)

def build(d):
    if d.get('boundary_policy')!='explicit':raise ValueError('boundary_policy must be explicit')
    verts=[str(v) for v in d['vertices']]
    if len(set(verts))!=len(verts):raise ValueError('duplicate vertex')
    edges={str(e['id']):(str(e['u']),str(e['v'])) for e in d['edges']}
    if len(edges)!=len(d['edges']):raise ValueError('duplicate edge id')
    for eid,(u,v) in edges.items():
        if u not in verts or v not in verts or u==v:raise ValueError('invalid edge '+eid)
    spatial_faces={str(f['id']):[(str(e),int(s)) for e,s in f['boundary']] for f in d['faces']}
    if len(spatial_faces)!=len(d['faces']):raise ValueError('duplicate face id')
    for fid,word in spatial_faces.items():
        if not word:raise ValueError('empty face '+fid)
        chain=[]
        for e,s in word:
            if e not in edges or s not in (-1,1):raise ValueError('bad face word '+fid)
            u,v=edges[e];chain.append((u,v) if s==1 else (v,u))
        if any(chain[i][1]!=chain[(i+1)%len(chain)][0] for i in range(len(chain))):raise ValueError('face boundary not closed: '+fid)
    E={};F={}
    for t in range(4):
        for e,(u,v) in edges.items():E[f's:{t}:{e}']=[f'{t}:{u}',f'{t}:{v}']
        for f,word in spatial_faces.items():F[f'p:{t}:{f}']=[[f's:{t}:{e}',s] for e,s in word]
    for t in range(3):
        for v in verts:E[f't:{t}:{v}']=[f'{t}:{v}',f'{t+1}:{v}']
        for e,(u,v) in edges.items():F[f'r:{t}:{e}']=[[f's:{t}:{e}',1],[f't:{t}:{v}',1],[f's:{t+1}:{e}',-1],[f't:{t}:{u}',-1]]
    fixed=set(map(str,d.get('fixed_boundary_edges',[])))
    for e in d.get('fixed_spatial_edges',[]):
        for t in (0,3):fixed.add(f's:{t}:{e}')
    for v in d.get('fixed_temporal_vertices',[]):
        for t in range(3):fixed.add(f't:{t}:{v}')
    if not fixed<=E.keys():raise ValueError('unknown fixed edges: '+str(sorted(fixed-set(E))))
    q=set(map(str,d.get('q',[]))); excluded=set(map(str,d.get('cavity_excluded_faces',[])))
    if not q:raise ValueError('q must explicitly list inserted face IDs; no default insertion convention')
    if not q<=F.keys() or not excluded<=F.keys():raise ValueError('unknown face in Q/exclusions')
    if q&excluded:raise ValueError('q must be separate from cavity_excluded_faces')
    cavity=set(F)-q-excluded
    degrees=collections.Counter(e for f in cavity for e,s in F[f])
    touches=collections.Counter(e for f in q for e,s in F[f])
    strict={f:[e for e,s in F[f] if e not in fixed and degrees[e]==0 and touches[e]==1] for f in q}
    # Linearized mod-2 central Z2 problem on *integrated* edges: assigned central -I plaquettes.
    # Constraints A x = b. For a requested central plaquette assignment b, feasibility
    # is checked against fixed edges assumed +I; actual arbitrary fixed SU(2) links are NOT covered.
    free=sorted(set(E)-fixed);idx={e:i for i,e in enumerate(free)}
    rows={}
    for f in F:
        bit=0
        for e,s in F[f]:
            if e in idx:bit^=1<<idx[e]
        rows[f]=bit
    # Cavity all +I, inserted all -I: incompatible if rank augmented increases.
    selected=sorted(cavity|q)
    base=[rows[f] for f in selected]
    aug=[rows[f] | ((1<<len(free)) if f in q else 0) for f in selected]
    central_frustration=parity_rank(aug)>parity_rank(base)
    out={'schema':'r3-explicit-prism-v1','source_sha256':hashlib.sha256(json.dumps(d,sort_keys=True).encode()).hexdigest(),
         'spatial':{'vertices':verts,'edges':edges,'faces':spatial_faces},'vertices':[f'{t}:{v}' for t in range(4) for v in verts],
         'edges':E,'faces':F,'inserted_faces':sorted(q),'cavity_faces':sorted(cavity),
         'excluded_faces':sorted(excluded),'fixed_edges':sorted(fixed),'integrated_edges':free,
         'audit':{'n_vertices':4*len(verts),'n_edges':len(E),'n_faces':len(F),
           'n_cavity_faces':len(cavity),'n_inserted_faces':len(q),
           'strict_exclusive_edges_by_insertion':strict,
           'cavity_touching_edges':sorted(e for e in touches if degrees[e]>0),
           'max_cavity_edge_degree':max(degrees.values(),default=0),
           'mod2_all_cavity_flat_all_inserted_central_minus_inconsistent':central_frustration,
           'mod2_test_scope':'central +/-I assignments, all fixed edges assigned +I; necessary-only obstruction to simultaneous flat cavity and -I inserted targets; not a proof of Gibbs exponential cost'}}
    return out

def main():
    p=argparse.ArgumentParser();p.add_argument('spatial_json');p.add_argument('-o','--output',required=True);a=p.parse_args()
    d=json.loads(pathlib.Path(a.spatial_json).read_text());out=build(d)
    pathlib.Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out['audit'],indent=2))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""PF-I6 independent audit of the AUTHOR-UPLOADED predecessor-paper source bundle.
Usage: python verify_pf_i6_predecessor_scripts.py '/path/to/Archive(1).zip' [results.json]

This imports no uploaded code as a main module: it compiles selected original
function AST nodes in a controlled namespace. It does NOT claim to replicate
all eight publication datasets, their external .npy files, or continuum physics.
"""
import ast, hashlib, itertools, json, sys, zipfile
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
PHI=(1+np.sqrt(5))/2
PAR=np.column_stack((np.cos(2*np.pi*np.arange(5)/5),np.sin(2*np.pi*np.arange(5)/5)))
PERP=np.column_stack((np.cos(4*np.pi*np.arange(5)/5),np.sin(4*np.pi*np.arange(5)/5)))
HULL={h:ConvexHull([PERP[list(c)].sum(axis=0) for c in itertools.combinations(range(5),h)]) for h in range(1,5)}

def load_functions(raw,source):
    tree=ast.parse(raw.decode('utf-8'),filename=source)
    ns={'np':np,'defaultdict':defaultdict,'PHI':PHI,'E_NORMALS':PAR,
        'ZETA':PAR.copy(),'ZETA_VECS':PAR.copy(),'OMEGA':np.exp(2j*np.pi/5),
        't_A':1.0,'t_B':1/PHI**2}
    nodes=[x for x in tree.body if isinstance(x,ast.FunctionDef)]
    exec(compile(ast.Module(body=nodes,type_ignores=[]),source,'exec'),ns)
    ns['GAMMA_GENERIC']=ns['make_generic_gamma']()
    return ns

def accepted(k,gamma):
    h=sum(k)
    if h not in HULL:return False
    y=(np.asarray(k,dtype=float)+gamma)@PERP
    e=HULL[h].equations
    return bool(np.max(e[:,:2]@y+e[:,2]) < -1e-9)

def window_patch(R,gamma):
    bound=(R+2)**2
    seeds={tuple(k) for k in itertools.product(range(-1,2),repeat=5)
           if accepted(k,gamma) and np.linalg.norm(np.asarray(k)@PAR)**2<=bound}
    explored=set(seeds);queue=list(seeds)
    for k in queue:
        for axis in range(5):
            for delta in [-1,1]:
                m=list(k);m[axis]+=delta;m=tuple(m)
                if m in explored or np.linalg.norm(np.asarray(m)@PAR)**2>bound or not accepted(m,gamma):continue
                explored.add(m);queue.append(m)
    kept={m for m in explored if np.linalg.norm(np.asarray(m)@PAR)**2<=R*R}
    edges=set()
    for m in kept:
        for j in range(5):
            n=tuple(m[i]+int(i==j) for i in range(5))
            if n in kept:edges.add(tuple(sorted((m,n))))
    return kept,edges

def edge_sets(graph,interior):
    iv=set(interior);ls=graph['multi_indices'];index=graph['mi_to_idx']
    tiled={(a,b) for a in iv for b in graph['adjacency'].get(a,()) if a<b and b in iv}
    basis=set()
    for a in iv:
        m=ls[a]
        for j in range(5):
            for delta in [-1,1]:
                z=list(m);z[j]+=delta;b=index.get(tuple(z))
                if b is not None and b in iv and a<b:basis.add((a,b))
    return tiled,basis

def ncomponents(verts,edges):
    parent={u:u for u in verts}
    def root(u):
        while parent[u]!=u:
            parent[u]=parent[parent[u]];u=parent[u]
        return u
    for a,b in edges:parent[root(a)]=root(b)
    return len({root(u) for u in verts})

def characterize(graph,interior,tile,basis,gamma,ng):
    ls=graph['multi_indices'];extra=basis-tile;hist=Counter();deg=Counter()
    weight=0
    for a,b in extra:
        m,n=ls[a],ls[b];diff=[j for j in range(5) if m[j]!=n[j]]
        assert len(diff)==1 and abs(m[diff[0]]-n[diff[0]])==1
        level=min(m[diff[0]],n[diff[0]])
        val=1 if int(np.floor((level+1)/PHI))!=int(np.floor(level/PHI)) else 1/PHI**2
        weight+=val
    for a,b in tile:deg[a]+=1;deg[b]+=1
    hist=Counter(deg.get(v,0) for v in interior)
    return {'N_grid':ng,'n_raw_vertices':graph['n_vertices'],'n_tiles':graph['n_tiles'],
            'n_interior':len(interior),'tile_edge_count':len(tile),'basis_edge_count':len(basis),
            'extra_basis_edges':len(extra),'extra_tile_edges':len(tile-basis),
            'tile_components':ncomponents(interior,tile),'basis_components':ncomponents(interior,basis),
            'tile_degree_histogram':dict(sorted(hist.items())),
            'additional_edge_weight_sum':float(weight),
            'laplacian_trace_increase_from_additional_edges':float(2*weight),
            'extra_basis_label_pairs':[[list(ls[a]),list(ls[b])] for a,b in sorted(extra)[:8]]}

def run(archive):
    with zipfile.ZipFile(archive) as z:
        code_names=sorted(n for n in z.namelist() if n.endswith('.py') and not n.startswith('__MACOSX'))
        docs=sorted(n for n in z.namelist() if n.lower().endswith('.pdf') and not n.startswith('__MACOSX'))
        summaries=sorted(n for n in z.namelist() if (n.endswith('.json') or n.endswith('.md')) and not n.startswith('__MACOSX'))
        assert len(code_names)==9 and len(docs)==9 and len(summaries)==3
        bytes_map={n:hashlib.sha256(z.read(n)).hexdigest() for n in code_names+docs+summaries}
        p6=load_functions(z.read('paper6_convergence_compute.py'),'paper6_convergence_compute.py')
        p3=load_functions(z.read('paper3_compute.py'),'paper3_compute.py')
        p3c=load_functions(z.read('paper3_coupled_compute.py'),'paper3_coupled_compute.py')
        gamma=p6['GAMMA_GENERIC'];source={}
        paired=[];pairs_by_ng={};graph_by_ng={}
        for ng in [3,4,5,7,10,12,14]:
            g=p6['build_penrose_tiling'](ng)
            iv=p6['select_interior_vertices'](g)
            tile,basis=edge_sets(g,iv)
            if ng<=12:
                rec=characterize(g,iv,tile,basis,gamma,ng)
                paired.append(rec);pairs_by_ng[ng]=rec
            graph_by_ng[ng]=g
        assert [pairs_by_ng[x]['n_interior'] for x in (7,10,12)]==[1550,3042,4324]
        assert all(pairs_by_ng[x]['extra_basis_edges']==0 for x in [3,4,5,7])
        assert [pairs_by_ng[x]['extra_basis_edges'] for x in [10,12]]==[62,85]
        assert all(row['extra_tile_edges']==0 for row in paired)
        recovered=[]
        for ng,upper in [(10,12),(12,14)]:
            g=graph_by_ng[ng];iv=p6['select_interior_vertices'](g);tile,basis=edge_sets(g,iv)
            extra=basis-tile;ls=g['multi_indices'];extra_label={frozenset([ls[a],ls[b]]) for a,b in extra}
            h=graph_by_ng[upper];ml=h['multi_indices']
            grown_label={frozenset([ml[a],ml[b]]) for a,neigh in h['adjacency'].items() for b in neigh if a<b}
            found=len(extra_label & grown_label)
            assert found==len(extra_label)
            recovered.append({'N_grid':ng,'extension_to':upper,'extra_edges':len(extra_label),'restored_as_tile_edges':found})
        disk=[];g=graph_by_ng[7];labels=g['multi_indices'];g_edges={frozenset([labels[a],labels[b]]) for a,neigh in g['adjacency'].items() for b in neigh if a<b}
        for R in [3,5,7,9]:
            dv,de=window_patch(R,gamma)
            gv={m for m in labels if np.linalg.norm(np.asarray(m)@PAR)**2<=R*R}
            ge={frozenset([a,b]) for a,b in g_edges if a in gv and b in gv}
            assert dv==gv and {frozenset(x) for x in de}==ge
            disk.append({'R':R,'source_vertices':len(gv),'direct_window_vertices':len(dv),'source_edges':len(ge),'direct_window_edges':len(de),'identical':True})
        ns=[x['N_grid'] for x in paired];
        return {'archive_name':Path(archive).name,'archive_sha256':hashlib.sha256(Path(archive).read_bytes()).hexdigest(),
                'draft_python_count':len(code_names),'paper_pdfs_count':len(docs),'summaries_count':len(summaries),
                'files_sha256':bytes_map,'gamma':gamma.tolist(),'gamma_sum':float(np.sum(gamma)),
                'source_function_interpretation':{'tile_graph':'graph edges from de Bruijn pentagrid rhombi','coupled_graph':'on identical indexed vertices, all +/- one-basis Z5 neighbours, same Fibonacci weight and D=sumW'},
                'paired_graphs':paired,'missing_tile_edges_restored_at_larger_grid':recovered,
                'direct_cut_project_matched_central_disks':disk,'paper3_and_paper6_generated_same_labels':(p3['build_penrose_tiling'](3)['multi_indices']==graph_by_ng[3]['multi_indices']),
                'source_comparator_size_rule':'N_periodic=floor(sqrt(N_int))^2; triangular t_avg=(1+phi^-2)/2',
                'source_zero_mode_threshold':'lambda>1e-10 before computing source reported zeta ratios',
                'note':'Source code tests only; not independent reproduction of original all-eight-size eigenspectra or continuum gauge/gravity claims.'}
if __name__=='__main__':
    if len(sys.argv)<2:raise SystemExit('usage: verify_pf_i6_predecessor_scripts.py archive.zip [results.json]')
    result=run(Path(sys.argv[1])); out=json.dumps(result,indent=2,sort_keys=True,default=int)+'\n'
    if len(sys.argv)>2:Path(sys.argv[2]).write_text(out)
    else:print(out)
    print('PF-I6 PASS: nine scripts inventoried; matched direct windows; finite source graph-pair diagnostics complete.',file=sys.stderr)

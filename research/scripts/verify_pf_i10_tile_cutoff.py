#!/usr/bin/env python3
"""PF-I10 exact finite source tile/coupled comparison, not physical-geometry inference.

The original source tiled adjacency can omit true C&P faces because it is
line-level capped. The author-defined coupled basis edge graph uses same labels.
Both graphs/crops stay distinct; this checks no new edge physics is assumed.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.csgraph import connected_components
from verify_pf_i10_source_spectral import source_import,build_sparse,SOURCE_SHA
EXTRA_COUNTS={7:0,10:62,12:85,15:290,18:444,20:593,23:889,25:1066}

def source_tile_sparse(source,ngrid):
    til=source.build_penrose_tiling(ngrid)
    selection=source.select_interior_vertices(til,.35)
    ni=len(selection);imap={v:i for i,v in enumerate(selection)}
    labels=til['multi_indices']
    pairs=set()
    for old in selection:
        for old2 in til['adjacency'].get(old,set()):
            if old2 not in imap:continue
            a,b=sorted((imap[old],imap[old2]))
            if a!=b:pairs.add((a,b))
    ie=[];je=[];ww=[]
    for a,b in sorted(pairs):
        k=labels[selection[a]];m=labels[selection[b]]
        diffs=[j for j in range(5) if abs(k[j]-m[j])==1]
        if len(diffs)!=1:raise AssertionError('source tile edge not basis difference')
        j=diffs[0]; assert sum(abs(k[z]-m[z]) for z in range(5))==1
        ie.append(a);je.append(b);ww.append(source.fibonacci_hopping(min(k[j],m[j])))
    W=np.asarray(ww);I=np.asarray(ie,dtype=int);J=np.asarray(je,dtype=int)
    A=sparse.coo_matrix((np.r_[W,W],(np.r_[I,J],np.r_[J,I])),shape=(ni,ni)).tocsr()
    L=sparse.diags(np.asarray(A.sum(axis=1)).ravel())-A
    nc,grp=connected_components(A,directed=False)
    return L,{'Ngrid':ngrid,'n':ni,'tile_edges':len(pairs),'tile_components':int(nc),
             'tile_component_sizes':sorted(np.bincount(grp).tolist(),reverse=True),
             'tile_mean_strength':float(2*np.sum(W)/ni),
             'tile_edge_weight_sum':float(np.sum(W))},pairs

def one_case(source,ngrid):
    tile,meta,edges=source_tile_sparse(source,ngrid)
    coupled,cm,_=build_sparse(source,ngrid)
    assert tile.shape==coupled.shape
    # M_coupled - M_tile = sum omitted weighted edge Laplacians PSD.
    difference=(coupled-tile).tocsr()
    diag=difference.diagonal()
    coo=difference.tocoo()
    extra_weights=-np.asarray(coo.data)[(coo.row<coo.col)&(coo.data<0)]
    # subset condition for original tile graph
    cooT=tile.tocoo();tile_neg={(int(i),int(j)) for i,j,v in zip(cooT.row,cooT.col,cooT.data) if i<j and v<0}
    cooC=coupled.tocoo();basis_neg={(int(i),int(j)) for i,j,v in zip(cooC.row,cooC.col,cooC.data) if i<j and v<0}
    assert tile_neg<=basis_neg and len(basis_neg-tile_neg)==EXTRA_COUNTS[ngrid]
    assert np.all(diag>=-1e-10) and np.all(extra_weights>0)
    assert abs(float(diag.sum())-2*float(extra_weights.sum()))<1e-7
    assert np.max(np.abs(np.asarray(difference.sum(axis=1)).ravel()))<1e-10
    return {'Ngrid':ngrid,'N':cm['n'],'tile_edges':meta['tile_edges'],
       'coupled_edges':cm['edges'],'source_coupled_minus_tile_edges':len(basis_neg-tile_neg),
       'components_tile':meta['tile_components'],'components_coupled':cm['components'],
       'coupled_minus_tile_positive_edge_weights_sum':float(extra_weights.sum()),
       'trace_Delta_L_over_N':float(diag.sum()/cm['n']),
       'source_coupled_traceL_over_N':cm['trace_over_n'],
       'source_tile_traceL_over_N':meta['tile_mean_strength'],
       'finite_PSD_edge_sum_verified':True,
       'strictly_positive_mean_spectral_shift_when_extra_edges':bool(len(extra_weights)>0)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-script',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--ngrids',nargs='+',type=int,default=[7,10,12,15,18,20,23,25])
    args=ap.parse_args();s=source_import(args.source_script)
    out=[]
    for ng in args.ngrids:
        a=one_case(s,ng);out.append(a);print(a,flush=True)
        args.output.write_text(json.dumps({'source_sha256':SOURCE_SHA,'scope':'exact finite source operator difference; continuum proof open','rows':out},indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()

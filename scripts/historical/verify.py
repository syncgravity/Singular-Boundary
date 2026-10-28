#!/usr/bin/env python3
"""Read-only verification of archived Singular Boundary source/data evidence.

Never imports modules from the archives, invokes Monte Carlo, estimates spectral
masses, or changes original artifacts. Machine-readable output is optional and
must be outside the supplied historical input tree unless explicitly selected.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, re, sys, zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
import numpy as np

HERE=Path(__file__).resolve().parent

def sha256_file(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for part in iter(lambda:f.read(1024*1024), b''): h.update(part)
    return h.hexdigest()

def run(root,lock):
    checks=[]; failures=[]
    def check(label,condition,evidence):
        checks.append({'check':label,'passed':bool(condition),'evidence':evidence})
        if not condition: failures.append(label)
    rows=list(csv.DictReader(lock.open(newline='')))
    hashes={}
    for row in rows:
        name=row['filename'];path=root/name
        exists=path.is_file()
        actual=sha256_file(path) if exists else None
        hashes[name]=actual
        check(f'checksum:{name}', exists and actual==row['sha256'] and path.stat().st_size==int(row['size_bytes']),
              {'expected_sha256':row['sha256'],'actual_sha256':actual,'expected_bytes':int(row['size_bytes'])})
        if not exists or actual!=row['sha256']:
            continue
        if path.suffix.lower()=='.zip':
            with zipfile.ZipFile(path) as z:
                members=[x for x in z.infolist() if not x.is_dir()]
                dangerous=[x.filename for x in members if PurePosixPath(x.filename).is_absolute() or '..' in PurePosixPath(x.filename).parts or '\\' in x.filename or ((x.external_attr >> 16)&0o170000)==0o120000]
                check(f'archive-integrity:{name}', z.testzip() is None and not dangerous,
                      {'members':len(members),'bad_paths':dangerous[:3]})
    # Do not silently compare derived findings when a needed original is missing.
    if failures:
        return {'status':'FAIL','pinned_files':len(rows),'checks':checks,'failures':failures,
                'note':'At least one source differs from the pinned manifest; derived checks were not attempted.'}

    def zjson(name,member):
        with zipfile.ZipFile(root/name) as z:return json.loads(z.read(member))
    def znpz(name,member):
        with zipfile.ZipFile(root/name) as z:
            buf=io.BytesIO(z.read(member))
        return np.load(buf,allow_pickle=False)
    def close_float(a,b,tol=1e-12): return abs(a-b)<=tol

    # Stage 19 strict anchor recovery is a coverage/existence test, not spectroscopy.
    early=zjson('Stage19_Strict_Expanded_Anchor_Recovery_and_Symmetry_Audit(1).zip','stage19_strict_expanded/REPORT.json')
    last=zjson('Stage19_Missing_150_Anchor_Diagnosis_and_Strict_Recovery.zip','stage19_missing150/REPORT.json')
    with znpz('Stage19_Missing_150_Anchor_Diagnosis_and_Strict_Recovery.zip','stage19_missing150/missing_anchor_diagnostics.npz') as a:
        orig=a['missing_anchor_ids'];covered=a['accepted_anchor_ids'];rec=a['newly_recovered'];rem=a['remaining_missing']
        validity=(len(orig)==150 and len(covered)==22658 and len(rec)==149
                  and np.intersect1d(orig,covered).size==0 and np.union1d(orig,covered).size==22808
                  and np.isin(rec,orig).all() and rem.tolist()==[10550])
    check('stage19-strict-anchor-candidate-existence',validity and early['original_covered']==22055 and early['now_covered']==22658
          and last['combined_strict_recovery']['matched_total']==22808
          and last['last_anchor_followup']['best_distance']<1.5,
          {'early':22055,'expanded':22658,'later':22808,'last_anchor':10550,
           'last_anchor_distance':last['last_anchor_followup']['best_distance'],
           'scope':'Candidate loop coverage, not production catalogue certification.'})

    # Stage 19 held-out reports: 64 screens are NOT 64 independent simulations.
    held=zjson('Stage19_Fourfold_Heldout_Variational_Audit.zip','stage19_fourfold/SUMMARY.json')
    vals=[int(v) for geometry in held.values() for method in geometry.values()
          for seed in method['fold_block_passes'].values() for v in seed.values()]
    check('stage19-fourfold-heldout-screen',len(vals)==64 and sum(vals)==0,
          {'screen_combinations':len(vals),'accepted':sum(vals),'independent_chains':8})

    # Stage 20: verify saved vacuum subtraction shift is constant across times.
    stage20=zjson('Stage20_Scalar_Vacuum_Estimator_Benchmark(1).zip','stage20_scalar_variance/RESULTS.json')
    shift_drift=[]; no_windows=True
    for g in ('penrose','square'):
        v=stage20['geometries'][g]
        plugin=np.asarray(v['observed']['plugin'],dtype=np.float64)
        cross=np.asarray(v['observed']['cross_chain'],dtype=np.float64)
        drift=float(np.max(np.ptp(cross-plugin,axis=0)))
        shift_drift.append(drift)
        no_windows &= all(not any(block[method]['three_consecutive_t2_6'])
                          for block in v['bootstrap'].values() for method in ('plugin','cross_chain'))
    check('stage20-lag-invariant-vacuum-subtraction',max(shift_drift)<1e-19 and no_windows,
          {'max_time_shift_drift':max(shift_drift),'positive_3time_windows':0})

    # Stage 29 saved matched diagnostic, not a rerun of bootstrap.
    stats={}
    for b in (5,10,20):
        obj=zjson('Singular_Boundary_Stage29_Matched_Covariance_and_Source_Audit.zip',f'stage29/STAGE26_MATCHED_BLOCK{b}.json')
        stats[b]={g:obj[g]['max_abs_standardized_difference_diagonal'] for g in ('square','penrose')}
    check('stage29-matched-saved-standardized-differences',close_float(stats[20]['square'],2.357098314204506)
          and close_float(stats[20]['penrose'],2.2830995328326558),
          {'block20':stats[20],'scope':'Saved diagnostic, not independently recomputed covariance.'})

    # Stage 33 source code fix is a source-diff check; do not run original code.
    old='Stage33_Per_Anchor_Production_Equivalence_Gate.zip'
    new='Stage33_Per_Anchor_Production_Equivalence_Gate_FIXED.zip'
    with zipfile.ZipFile(root/old) as z: oldsrc=z.read('stage33_exact/stage33_audit.py').decode()
    with zipfile.ZipFile(root/new) as z: newsrc=z.read('stage33_exact/stage33_audit.py').decode()
    check('stage33-transpose-correction', 'unweighted=raw.mean(axis=-1).T' in oldsrc and
          'unweighted=raw.mean(axis=-1)' in newsrc,
          {'original_has_transpose':True,'fixed_omits_transpose':True})

    # Stage34 same-field production observable equivalence is genuinely reproducible.
    with znpz('Stage34_Exact_Per_Anchor_Equivalence.zip','stage34_exact/stage34_output/stage34_verified_per_anchor.npz') as a:
        anchors=a['per_anchor']; reference=a['production_reference']; reconstructed=a['production_reconstructed']; ids=a['anchor_ids']
        err=float(np.max(np.abs(np.mean(anchors,axis=-1)-reference)))
        recon_err=float(np.max(np.abs(reconstructed-reference)))
        shapes=(anchors.shape==(20,4,22808) and reference.shape==(20,4) and
                np.array_equal(ids,np.arange(22808)) and np.isfinite(anchors).all())
    check('stage34-one-field-per-anchor-reconstruction',shapes and err<2e-13 and recon_err<2e-13,
          {'shape':[20,4,22808],'max_abs_mean_error':err,'max_abs_reconstructed_error':recon_err,
           'scope':'One saved gauge field; not helical ensemble spectroscopy.'})

    with zipfile.ZipFile(root/'Stage35_C5_Production_Helical_Ensemble.zip') as z:
        measured=[n for n in z.namelist() if n.lower().endswith(('.npz','.npy','.h5','.hdf5'))]
    check('stage35-absence-of-measured-arrays',len(measured)==0,
          {'saved_array_members':measured,'scope':'Absence of arrays is not evidence no experiment occurred elsewhere.'})

    # Stage26 8-chain saved outer records, never treat inner replicas as independent.
    total_outer=0; chain_summaries={}; original_catalogue={
        'penrose':'d08e157f1b6fe258f4214e834f80508ef6278cae2f672b378188e8f138c00e2d',
        'square':'c81bff473a8418b141b23d8f6547aceb9f569d4dc9c352f7f2920b0373580ff8'}
    for g in ('penrose','square'):
        for seed in (101,211,307,419):
            n=f'{g}_seed{seed}_stage26.zip';d=f'{g}_seed{seed}'
            with zipfile.ZipFile(root/n) as z:
                meta=json.loads(z.read(f'{d}/latest.json'))
                entries=sorted([x for x in z.namelist() if re.search(r'/outer_\d{8}\.npz$',x)])
                steps=[int(re.search(r'outer_(\d{8})',x).group(1)) for x in entries]
                ok=(len(entries)==100 and steps==list(range(10020,12001,20)) and
                    meta['observations']==100 and meta['sweep']==12000 and meta['seed']==seed and
                    meta['kind']==g and meta['catalogue_sha256']==original_catalogue[g])
                for member in (entries[0],entries[-1]):
                    with np.load(io.BytesIO(z.read(member)),allow_pickle=False) as a:
                        ok=ok and (a['direct_timeslice'].shape==(20,4) and
                                  a['conditional'].shape==(2,9,4,4) and a['pair_counts'].shape==(9,)
                                  and str(a['catalogue_sha256'])==original_catalogue[g] and
                                  int(a['chain_seed'])==seed)
                # Last saved payload checksum vs archived latest.json.
                ok=ok and hashlib.sha256(z.read(f'{d}/outer_00012000.npz')).hexdigest()==meta['record_sha256']
                chain_summaries[d]={'saved_outer':len(entries),'first_sweep':steps[0],
                                    'last_sweep':steps[-1],'record_integrity':bool(ok)}
                total_outer+=len(entries)
                check(f'stage26-chain:{d}',ok,chain_summaries[d])
    check('stage26-eight-chain-saved-outer-total',total_outer==800 and len(chain_summaries)==8,
          {'chains':8,'outer_records':total_outer,'not_independent':'Inner replicas and shifts.'})

    return {'status':'PASS' if not failures else 'FAIL', 'pinned_files':len(rows),
            'checks':checks,'failures':failures,
            'scope':'Read-only saved artifacts; not independent proof, spectral fit or simulation.'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,required=True,help='directory containing original ZIP/NPZ archives')
    p.add_argument('--lock',type=Path,default=HERE/'MANIFEST_LOCK.csv')
    p.add_argument('--output',type=Path,help='optional JSON result path; never modifies source artifacts')
    a=p.parse_args()
    result=run(a.root,a.lock)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        src={(a.root / row['filename']).resolve() for row in csv.DictReader(a.lock.open(newline=''))}
        if a.output.resolve() in src or a.output.resolve()==a.lock.resolve():
            raise ValueError('Refusing to overwrite any pinned source or lock manifest')
        a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'source_files':result['pinned_files'],
                      'checks':len(result['checks']),'failed':result['failures'],
                      'stage34':next((i['evidence'] for i in result['checks'] if i['check'].startswith('stage34-')),None)},indent=2))
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__': sys.exit(main())

#!/usr/bin/env python3
"""Continuum analysis of dimensionless 2+1D Yang--Mills scalar glueball ratios.

Input: joint bootstrap replicates of *fitted* mass and string tension per ensemble.
This program does not generate SU(N) gauge fields or extract raw correlator masses.

The longitudinal anisotropy convention is xi=a_t/a_s.  Input am_t=a_t*m and
asqrt_sigma=a_s*sqrt(sigma); the dimensionless continuum ratio is
R=am_t / (xi * asqrt_sigma).  The cutoff covariate x=(asqrt_sigma)**power.

All ensembles must include matching bootstrap indices (which may independently
resample each ensemble), allowing mass-string-tension covariance within each
ensemble to be propagated through each continuum fit.
"""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
import numpy as np

REQUIRED = ('geometry', 'ensemble', 'replica', 'am_t', 'asqrt_sigma', 'xi')


def read_bootstraps(path):
    series = defaultdict(dict)
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or not set(REQUIRED).issubset(set(reader.fieldnames)):
            raise ValueError('CSV must contain columns: ' + ', '.join(REQUIRED))
        for row in reader:
            geo = row['geometry'].strip().lower()
            ens = row['ensemble'].strip()
            if not geo or not ens:
                raise ValueError('Every row must contain geometry and ensemble')
            b = int(row['replica'])
            vals = tuple(float(row[c]) for c in ('am_t', 'asqrt_sigma', 'xi'))
            if min(vals) <= 0 or not np.all(np.isfinite(vals)):
                raise ValueError('am_t, asqrt_sigma and xi must be finite and positive')
            k = (geo, ens)
            if b in series[k]:
                raise ValueError(f'Duplicate bootstrap {b} in {k}')
            series[k][b] = vals
    if not series:
        raise ValueError('No measurements found: supply joint bootstrap samples')
    return series


def model(series, geometric_labels, power, exclude_coarse=0):
    keys = [key for key in series if key[0] in geometric_labels]
    if len({k[0] for k in keys}) != 2:
        raise ValueError('Both specified geometry labels must occur in input')
    common = set.intersection(*(set(series[k]) for k in keys))
    b_ids = sorted(common)
    if len(b_ids) < 50:
        raise ValueError('Need at least 50 common bootstrap indices across ensembles; 1000+ recommended')
    data = {}
    for key in keys:
        a = np.array([series[key][b] for b in b_ids])
        # M and tension were estimated on the SAME resampled Monte Carlo blocks.
        r = a[:, 0] / (a[:, 2] * a[:, 1])
        x = a[:, 1] ** power
        data[key] = {'r': r, 'x': x, 'mean_x': float(np.mean(x)),
                     'sd_r': float(np.std(r, ddof=1))}
    by_geom = {}
    for geom in geometric_labels:
        subset = [(key, data[key]) for key in keys if key[0] == geom]
        subset.sort(key=lambda kv: kv[1]['mean_x'], reverse=True)  # coarsest first
        subset = subset[exclude_coarse:]
        if len(subset) < 3:
            raise ValueError(f'{geom} needs >=3 distinct spacings after cutoff (has {len(subset)})')
        x_means = np.array([v['mean_x'] for _, v in subset])
        if len(np.unique(np.round(x_means, 10))) < 3:
            raise ValueError(f'{geom} needs >=3 *distinct* cutoff scales')
        sd = np.array([max(v['sd_r'], 1e-12) for _, v in subset])
        inv_sd = 1.0 / sd
        A = np.column_stack([np.ones(len(subset)), x_means])
        central_y = np.array([float(np.mean(v['r'])) for _, v in subset])
        central_coeff, *_ = np.linalg.lstsq(A * inv_sd[:, None], central_y * inv_sd, rcond=None)
        chi2 = float(np.sum(((central_y - A @ central_coeff) * inv_sd)**2))
        sampled = np.empty((len(b_ids), 2))
        for ib in range(len(b_ids)):
            this_x = np.array([v['x'][ib] for _, v in subset])
            this_y = np.array([v['r'][ib] for _, v in subset])
            this_A = np.column_stack([np.ones(len(subset)), this_x])
            sampled[ib], *_ = np.linalg.lstsq(this_A * inv_sd[:, None], this_y * inv_sd,
                                               rcond=None)
        by_geom[geom] = {'R0': float(central_coeff[0]), 'R0_se': float(np.std(sampled[:,0], ddof=1)),
                         'R0_ci95': np.quantile(sampled[:,0], [0.025,0.975]).tolist(),
                         'slope': float(central_coeff[1]), 'chi2': chi2,
                         'ndof': len(subset)-2, 'ensembles': [k[1] for k, _ in subset],
                         'samples_R0': sampled[:, 0]}
    pen, control = geometric_labels
    delta_boot = by_geom[pen]['samples_R0'] - by_geom[control]['samples_R0']
    delta = by_geom[pen]['R0'] - by_geom[control]['R0']
    for obj in by_geom.values():
        del obj['samples_R0']
    return {'geometry_fit': by_geom,
            'Delta_R0': float(delta),
            'Delta_R0_bootstrap_se': float(np.std(delta_boot, ddof=1)),
            'Delta_R0_CI95': np.quantile(delta_boot, [0.025, 0.975]).tolist(),
            'bootstrap_replicates': len(b_ids), 'cutoff_x': f'(a_s sqrt(sigma))^{power}',
            'exclude_coarsest_each': exclude_coarse,
            'caution': 'Statistical interval conditional on chosen fitting model, input observable fits, '
                       'lattice action, finite volume, and Penrose approximant. It is not a total uncertainty.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input_csv')
    p.add_argument('--penrose-label', default='penrose')
    p.add_argument('--control-label', default='wilson')
    p.add_argument('--power', type=int, choices=(1,2), default=2,
                   help='continuum correction model R=R0+c*(a sqrt(sigma))**power')
    p.add_argument('--exclude-coarsest', type=int, default=0)
    p.add_argument('--output-prefix', default='continuum_fit')
    args = p.parse_args()
    result = model(read_bootstraps(args.input_csv),
                   (args.penrose_label.lower(), args.control_label.lower()),
                   args.power, args.exclude_coarsest)
    prefix = Path(args.output_prefix)
    prefix.parent.mkdir(parents=True, exist_ok=True)
    (prefix.with_suffix('.json')).write_text(json.dumps(result, indent=2) + '\n')
    print('Model:', result['cutoff_x'])
    for name, obj in result['geometry_fit'].items():
        print(f'{name}: R0={obj["R0"]:.5f} +- {obj["R0_se"]:.5f} (bootstrap statistical); '
              f'chi2/dof={obj["chi2"]:.2f}/{obj["ndof"]}')
    print(f'Delta_R0={result["Delta_R0"]:.5f} '
          f'+- {result["Delta_R0_bootstrap_se"]:.5f}; '
          f'bootstrap 95% interval={result["Delta_R0_CI95"]}')
    print('WARNING: Must run additional cutoff models, leave-one-spacing-out, volume, '
          'and Penrose approximant tests before interpreting a shift.')


if __name__ == '__main__':
    main()

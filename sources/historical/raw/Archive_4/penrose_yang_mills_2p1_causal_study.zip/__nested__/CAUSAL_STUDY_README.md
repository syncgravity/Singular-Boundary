# Corrected Penrose geometry × interacting SU(2) Wilson comparison

This is an **independent research prototype**, not the code from the previous Yang–Mills and Graph Method conversation. The uploaded `Sharpe_dissertation_v10.7.tar.gz` archive contains the dissertation and paper PDFs, not the earlier tested generator/Monte Carlo ZIP. The six passing tests listed below are **new tests**.

## Contents

- `penrose_causal_study.py`: integer-period rational-plane approximants to the direct 5D cut-and-project model; four pentagonal acceptance windows; torus vertex/edge/face incidence; orientation, acceptance and local-convergence diagnostics. Also supports `primitive_periods=True` to saturate the integer period lattice; the 1360-face default is a fourfold, near-square supercell of the 340-face primitive M=13 torus.
- `wilson_torus.py`: local-link Metropolis SU(2) Wilson simulation on periodic quadrangulations, and an equal-plaquette-count square-torus control.
- `test_penrose_causal.py`: six independent pytest tests, including gauge invariance, oriented incidence, exact face-area coverage, four acceptance windows, and local convergence.
- `geometry_audit.json`: seven scale geometry diagnostics and radius-by-radius model-set agreement.
- `wilson_comparison_results.json`: initial matched SU(2) Wilson results at beta=2 and beta=4.
- `wilson_beta4_recheck.json`: independent longer beta=4 check with fresh seeds.
- `wilson_primitive_results.json`: independent M=13 primitive 340-face-cell comparison against the 17×20 square torus.
- `CAUSAL_STUDY_NOTE.md`: derivation, conclusions, limitations, and follow-up experiment.

## Requirements and commands

Python 3.11+ with `numpy`, `scipy`, `numba`, and `pytest` installed. Commands, from the extracted directory:

```bash
python penrose_causal_study.py
pytest -q test_penrose_causal.py
python wilson_torus.py
```

`python wilson_torus.py` runs three independent random-seed chains at each of beta=2 and 4 (250 equilibration and 750 measurement sweeps per chain) on the 1360-face Penrose torus and a 34×40 square torus. It replaces `wilson_comparison_results.json` with its new results.

To reproduce the additional primitive benchmark, run `python -c "from wilson_torus import run_comparison; print(run_comparison(M=13,nx=17,ny=20,primitive_periods=True, seeds=(59,79,97)))"` (or use the supplied JSON).

The exact 2D Wilson result is **not a numerical hypothesis**: on a closed orientable surface, the homogeneous pure lattice-gauge partition function is a topological/face-count invariant; the SU(2) bulk mean plaquette is `I_2(beta)/I_1(beta)`. Agreement of simulation on two different tilings tests the code and is *not* evidence for a geometry-driven Yang–Mills effect.

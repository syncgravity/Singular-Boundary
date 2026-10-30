# 433-state complete first-shell SU(2) Wilson audit

Run in Python with `numpy`, `scipy`, `sympy`, `opt_einsum` installed:

```bash
python target_spin1_433.py           # regenerates all 8 matrices and target spin-1 matrix; ~seconds
python verify_saved_433_matrices.py  # independent Haar, parity, sparse and Ritz checks
python certify_spin1_minpoly.py      # exact symbolic Q(sqrt(3)) spectrum
```

`build_433_exact.py` is imported by `target_spin1_433.py` and can be run alone. Both write NPZ outputs next to the script. Magnetic matrices `magnetic_0.npz`–`magnetic_7.npz` include the *deleted* target matrix for diagnostic purposes; only seven others enter the Hamiltonian. `basis.npz` contains the 433-state occupation masks and electric coefficients. `ritz_b_*` stores normalized Ritz vectors, spectra, out-of-shell **lower** bounds, and target projected quantities. The `PROOF_REPORT.md` fully documents the scope, exact algebra and limitations.

All files are local research artifacts. They do **not** prove a continuum Yang–Mills mass gap or a certified eight-face physical ground-state cap probability. No GitHub write is claimed.

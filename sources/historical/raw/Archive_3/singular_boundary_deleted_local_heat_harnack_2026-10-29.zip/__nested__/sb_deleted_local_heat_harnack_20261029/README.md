# Local SU2 heat-kernel Harnack, deleted-face probability minorization

- `PROOF_REPORT.md`: finite interacting Wilson theorem, volume-independent all-bulk lower bound, exact center-even rotor obstruction, unresolved bulk conditions.
- `verify_deleted_local_heat_harnack.py`: deterministic symbolic and numeric SU2 checks. Run `python verify_deleted_local_heat_harnack.py` with Python, NumPy, SymPy and SciPy.
- `VERIFY_LOG.txt`: direct output of deterministic verifier.
- `SHA256SUMS.txt`: per-file hashes.

The theorem proves an unconditional `h^(3/2) exp(-C/h)` **lower** bound for the deleted-vacuum center-cap probability, but not the desired polynomial bound; no Yang–Mills mass-gap claim is made. The separate rotor is **not** the Penrose Wilson Hamiltonian.

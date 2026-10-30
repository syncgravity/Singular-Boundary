# Eight-face complete-shell: winding response and exact magnetic leakage

This archive continues the R3 independent-reconstruction proof program at the next concrete eight-face spin-network gate. It is independent of GitHub authorization and does **not** claim a continuum mass gap.

## Results
- Exact full 433-state fundamental-shell electric spectrum and target-center parity splitting.
- An explicit admissible center-even fundamental-shell state with target marginal `4 p_f^2 * Haar`, spin-one character expectation exactly 1, and near-center cap enhancement asymptotically fourfold. This is a *kinematic state*, not the interacting vacuum.
- Seven exact omitted SU(2) spin channels have matrix `-diag(b_q/2)` for every complete original-link cutoff `J>=1/2`, hence the global magnetic off-block norm never decreases below `max(b_q)/2` with cutoff.
- An exact nonlinear one-face SU(2) rotor demonstrates that the *Ritz eigenvector* residual may nonetheless decay strongly with cutoff.

## Run
```
python verify_fundamental_shell_winding.py
python verify_exact_magnetic_edge_leakage.py
python verify_state_dependent_rotor_residual.py
```

All checkers are deterministic. No eight-face 433x433 magnetic matrix, true Wilson cap certificate, or physical mass-gap theorem is claimed.

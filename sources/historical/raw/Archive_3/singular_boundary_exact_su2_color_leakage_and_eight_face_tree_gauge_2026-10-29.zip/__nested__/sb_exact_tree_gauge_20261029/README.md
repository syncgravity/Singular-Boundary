# Exact class-sector leakage and connected eight-face gauge reduction

Proof report: `PROOF_REPORT.md`.

Verification: 

```bash
python verify_su2_class_leakage.py
python verify_exact_tree_gauge_q8.py
```

- The SU(2) gradient and kinematic Haar identities are analytic; the quadrature checker validates algebra and constants.
- The nonabelian Q8 checker validates spanning-tree gauge reduction and all 22 primal-edge actions on the 8-face patch. It is not an approximation to the continuous SU(2) spectrum.
- No connected eight-face full-coupling low-energy response has been bounded; no continuum Yang–Mills mass-gap proof is claimed.
- `COL4` is the compressed operator on individual-plaquette class functions, **not** the original interacting Hamiltonian.
- `COL5`–`COL7` quantify the physical color modes that the class compression omits.

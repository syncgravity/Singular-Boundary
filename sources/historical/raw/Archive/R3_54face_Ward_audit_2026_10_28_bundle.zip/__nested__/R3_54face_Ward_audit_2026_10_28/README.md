# R3 54-face Wilson-energy Ward audit

This is a **partial mathematical result**, not a proof of the requested uniform 54-face bound.

- `FORMAL_NOTE.md`: analytic statements, proofs, precise remaining gap.
- `verify_heatbath.py`: independently verifies the SU(2) heatbath Bessel formula and pairwise staple identity; requires NumPy and SciPy.
- `verification.json`: recorded results from the script.

Run: `python verify_heatbath.py`.

The local-cover specialization assumes the previously reported incidence inclusion `A_fill subset A(H)`. The uploaded catalogue arrays are not an explicit 54-by-36 face-link incidence certificate, so this inclusion has not been independently re-audited in this package.

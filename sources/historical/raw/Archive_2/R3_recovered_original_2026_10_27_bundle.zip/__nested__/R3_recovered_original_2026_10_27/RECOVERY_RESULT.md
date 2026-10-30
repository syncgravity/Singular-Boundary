# Historical R3 Q14 source recovered and executed

The uploaded `R3_uploaded_gaussian_audit_2026_10_27_bundle.zip` **contains** original `cavity_audit.py`, `construct_surgery.py` and `verify_bianchi.py`. Earlier searches overlooked these files.

`python cavity_audit.py` returns Q=14, H=36, affected retained faces=62 on all four disk radii 5, 6.5, 8, 10. `python verify_bianchi.py` returns Q=14, retained fill=54, longest reduced expansion 17, coefficient 44. The exact original canonical endpoint face labels are written in `HISTORICAL_Q14_CANONICAL.json`.

This recovers the historical **support-generation** source and the Bianchi certificate. `construct_surgery.py` contains a finite-net Haar-translation shell construction, but is not by itself evidence that the separately reported 59-pivot repair implementation has been recovered. No contraction matrix or volume-uniform nonlinear energy bound has been proved.

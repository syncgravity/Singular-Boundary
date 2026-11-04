"""Reproducibility entrypoint for R3-IR-563.

The full executed numerical audit resides in ChatGPT Library:
 /The Singular Boundary/Source/audit_prism_gauge_covariance.py
Restore the original archived complete source there alongside archived 3D
mass and incidence NPZ data. The exact gauge-covariance proof is given in:
 research/theorems/R3_PRISM3D_GAUGE_COVARIANCE_GAUSS_DOMAIN_2026-10-31.md

This file intentionally makes no unverified pass claims if data are missing.
"""
from pathlib import Path
import runpy
source=Path("audit_prism_gauge_covariance.py")
if source.resolve()==Path(__file__).resolve():
 raise RuntimeError("Restore the full Library audit into a separate working directory")
if not source.exists():
 raise FileNotFoundError("Restore audit_prism_gauge_covariance.py from Library into the current directory")
runpy.run_path(str(source),run_name="__main__")

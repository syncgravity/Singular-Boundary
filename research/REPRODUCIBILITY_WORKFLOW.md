# Reproducible research handoff — canonical workflow

Original historic branch document: `fix/reproducible-research-handoff-2026-10-30:research/REPRODUCIBILITY_WORKFLOW.md`, Git blob `4834fa55b048168daab2560c131a467732118f98`. The original remains readable on its branch; this file updates its procedures without rewriting the earlier account.

## Standard

1. The reviewed historical record lives on `main`. Retire obsolete branches only after confirming that their distinct evidence has been preserved on `main`; do not force-push or silently delete conflicting mathematical assertions.
2. Couple a claim with its complete assumptions, source commit, scripts, verified input hashes, expected outputs, explicit status, correction chain and regression results. A citation or script path is not proof of availability or mathematical truth.
3. Upload immutable original binaries to verified durable storage (Git LFS or content-addressed object storage). Record SHA-256, byte length, producer, source and retrieval URI. Recover them and rehash the returned **bytes**. Do not substitute a regenerated candidate for a historical original.
4. Build **bundle-specific** `FILE_MANIFEST.json` files. The verifier deliberately ignores any original absolute `base` field. A global inventory is not a suitable manifest for a subset.
5. Verify a handoff ZIP or directory with:

```bash
python research/scripts/verify_research_handoff.py /path/to/package.zip
python research/scripts/verify_research_handoff.py /path/to/extracted-package
python -m unittest discover -s research/tests -v
```

6. All 11 bundled verifier fixtures passed on the local integration candidate on 2026-11-01; the installed runner's full CI and actual historical science calculations have not thereby been certified. Reexecute against the exact Git commit in a fresh checkout before promoting evidence status.
7. The historical `global_whitney_11face.npz` and `m5_whitney_candidate_2026-10-30.npz` are distinct. A consistent recomputed eigenvalue of an uploaded NPZ proves internal consistency, **not** original-byte provenance.
8. Source-missing claims, disputed IDs, unreproduced experiments and unvalidated continuum steps remain blocked. The acceptance gate is [here](../docs/research/HISTORICAL_RECORD_ACCEPTANCE_GATE_2026-11-01.md).

No workflow, input checker or finite Ritz calculation on its own establishes a uniform Penrose center-cap bound or continuum Yang–Mills mass gap.

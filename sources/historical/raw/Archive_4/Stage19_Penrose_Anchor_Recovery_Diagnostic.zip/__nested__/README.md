# Stage 19 — Penrose missing-anchor diagnosis

**Geometry-only research screen.** Not a scalar mass extraction, a proven point-group scalar operator, or a production-admitted matched observable.

## What is fully measured

The original Penrose target-first screen used cluster sizes (3,5,8,10), two deterministic growth variants, five predeclared physical (area,perimeter) targets, scales (.25,.25,.12), and a standardized descriptor-distance threshold of 1.5. It misses **3,254 / 22,808** spatial anchors (**85.7331% covered**).

With the **same targets, scale, sizes and 1.5 threshold**, but **four** variants, a complete rerun on all 22,808 Penrose anchors found **22,055 covered and 753 missing (96.6985% coverage)**. Thus **2,501 missing anchors were recovered without relaxing matching**. Every anchor has at least one valid boundary candidate; missing anchors failed the descriptor threshold, not the boundary existence test.

The baseline full run has **8,771** invalid candidate boundaries; the four-variant full run has **17,113** invalid candidate boundaries, but these candidate-level rejections do not mean an anchor is unmeasurable. The broader variant search also increases boundary tests.

For the four-variant full run a looser threshold of 1.65 would cover **22,764/22,808** and 2.0 would cover **22,806/22,808**. Those are sensitivity screens, **not** a justified change of physical matching tolerance.

## Expanded face-count sample, not full-lattice result

A deterministic 1,024-anchor sample (`np.linspace(0,F-1,1024,dtype=int)`) gave strict-threshold 1.5 coverage:

| Candidate family | Covered | Missing |
|---|---:|---:|
| Sizes 3,5,8,10; 2 variants | 882 | 142 |
| Sizes 3,5,8,10; 4 variants | 985 | 39 |
| Sizes 2,3,4,5,6,7,8,9,10,12,15; 2 variants | 974 | 50 |
| Sizes 2,3,4,5,6,7,8,9,10,12,15; 4 variants | 1,019 | 5 |

The expanded all-anchor screen was attempted but exceeded the execution budget. **Do not extrapolate the sampled 99.5% into a claim of full-lattice admission.**

## Symmetry admission is separate

Area, perimeter and compactness are invariant under coordinate rotations/reflections but matching them does not construct an orbit-averaged scalar operator. Penrose finite rational approximant symmetry may be only approximate; exact rotation operations must be verified as graph automorphisms before applying orbit averaging. Root-normalized weights must be retained and unmatched roots explicitly audited. The original unrestricted full-volume loop operator remains an independent control.

## Files

- `DIAGNOSTIC_REPORT.json`: summarized full Penrose + sampled growth results.
- `variants4_per_anchor.npz`: full Penrose per-root nearest distance, best target, face count and candidate availability at four growth variants.
- `sample_*_per_anchor.npz`: same diagnostics on the 1,024-anchor extension sample.
- `diagnose_missing.py` and `full_expanded_screen.py`: reproducible code; must be placed alongside Stage19 target-first package dependencies.

Run from `stage19_target_first` with dependency modules present:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python diagnose_missing.py --roots 1024 --variants 4 --output ./sample_audit
```

A full 2–15 face expansion can be costly; pre-budget computation before using it to define production operators.

# PF-I6 source-identity erratum — manuscript titles, not file numbers

**Date:** 2026-11-07 · **User correction:** disregard numbering in paper archive filenames.

The source analysis below is indexed by **printed title, SHA-256, implemented algorithm, and verified inputs/outputs**. Number-like filename suffixes are preserved solely to locate raw archive members. They are **not** evidence of chronology, a revision chain, or one-to-one script↔manuscript ownership.

## Manuscripts identified by content

| Content title | Raw archive member (locator only) | SHA-256 prefix |
|---|---|---|
| Spectral Dimension Flow and Gravitational Finiteness on the Fibonacci Lattice | `paper1.pdf` | `a6afe544146711eb` |
| Spectral Dimension Flow on the Penrose Tiling: From Two-Dimensional Quasicrystalline Structure to the Kaluza-Klein Bridge | `paper2.pdf` | `5971445e733db264` |
| The Gravitational Path Integral on the Penrose Lattice: From Z5 to Minkowski’s World via Lapidus Complex Dimensions | `paper3.pdf` | `9d883e07004e0688` |
| The Complex Structure of Quasicrystalline Spacetime: The J-Operator and the Hidden Domain | `paper4.pdf` | `50fbe6da8d6e0c83` |
| Spectral Identity on the Penrose Lattice: The Heat Kernel as Locational Observable and the Constitutive Hypothesis of Position | `paper5.pdf` | `9ec26715091c1c09` |
| Appendix to Paper 5: Experimental Design for Detection of Quasicrystalline Spectral Signatures | `paper5_appendix.pdf` | `07f16f659656a185` |
| The Conformal Boundary of Quasicrystalline Spacetime: Λ as a Function on Perpendicular Space | `paper6.pdf` | `27d78024501a317f` |
| The Analytic Structure of Spectral Suppression on the Penrose Lattice: Failure Bands, the Complementary Pair Identity, and the Cosmological Constant | `paper7.pdf` | `14fc592f00dfe57b` |
| The Walker’s Path: Neural Coherence, Synchronicity, and Failure Correction on the Quasicrystalline Lattice | `paper8.pdf` | `2932b41e8a36f3c3` |

## Executables identified by code behavior

| Code behavior or outputs | Raw archive member (locator only) | SHA-256 prefix |
|---|---|---|
| Fibonacci-chain Hamiltonian and regular/Fibonacci Laplacians; heat-kernel spectral-flow diagnostics | `paper1_compute.py` | `876104b01aa385f6` |
| Robinson-triangle subdivision, Delaunay/filter graph and spectral computation (one implementation) | `paper2_computation.py` | `7849cc2dcda14393` |
| de Bruijn pentagrid P3 tiles, Fibonacci hopping, Conway-worm and spectral-dimension calculations (distinct implementation) | `paper2_compute.py` | `a8e73bb783471bed` |
| P3 integer labels, scalar Laplacian and Z5 coordinate/compact-direction and spectral-zeta diagnostics | `paper3_compute.py` | `f253f4036dfb6a7e` |
| P3 indexed vertices and all accepted original-basis nearest neighbors; coupled-named scalar Laplacian, comparator and zeta ratios | `paper3_coupled_compute.py` | `ad074fc4fbbbb5dc` |
| position-resolved heat kernel/identity/phason and spectral-temperature computations | `paper5_compute.py` | `85416b0ec4303207` |
| finite P3/basis incidence, scalar zeta and conformal/gradient diagnostics across cutoffs | `paper6_convergence_compute.py` | `a758befa9bbbe27a` |
| finite-graph observables, corrected mass-relative log determinant and figures | `paper6_figures.py` | `63315de666d593f9` |
| zeta-prime/relative determinant validation and comparison of multiple finite model operators | `zeta_prime_validation.py` | `fc15434334223368` |

## Corrected research interpretation

The finite PF-I6 test compared **two specific algorithms and their actual integer-labeled vertex/edge sets**, not successive numbered papers. A de Bruijn grid-intersection P3 constructor and an independent accepted-window cut-and-project constructor matched on four central disks **when their offsets, selection and crop were matched**. Two named Laplacians (tile-edge enumeration and all accepted-basis-neighbor enumeration) differed at some larger *finite* grid cutoffs because the tile enumerator omitted ordinary boundary rhombi; that difference is verified at the level of the concrete source functions. These facts do **not** establish chronology, an independent second physical dimension, the source identity of the merged-final dissertation, or the quantum mass gap.

The old PF-I6 report is preserved with a visible addendum pointing here. The Observatory must not use filename numbering to infer computational dependencies or research lineage. Dependencies are asserted only when an actual code import, function call, data read, explicit source claim, or mathematical equality supports them. Where an input is absent, mark that dependency **unverified**.

**Verification boundary:** Nine script files AST-parsed, nine manuscript/appendix titles read from extracted title pages, all file hashes independently calculated from original ZIP members. This is not a claim to have independently executed every script end-to-end or recovered the large eigenspectrum input arrays.

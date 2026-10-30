# R3 original-cavity incidence: forensic audit, 2026-10-28

## Outcome
The specific 14-face cavity has **not** been reconstructed from the available files. There is no defensible exact 54-face peeling verdict, nor a derived Gibbs estimate for any nonpeelable residue. The test suite verifies the certificate *algorithm*, not its application to the original Penrose support.

## Files inspected
- `/mnt/data/penrose_complete_catalogue.npz`: 22,808 records with fields `idx,sign,length,roots,distance,target,faces,cidx,csign,clength,ckind,F,graph_hash,threshold,coverage_version`; 68,424 auxiliary `cidx` rows. These are indexed loops/cycles and metadata, not a mapping of the specified 14 deleted prism faces to 54 fill faces.
- `/mnt/data/penrose_yang_mills_2p1_causal_study.zip`: `geometry_audit.json` and prism-construction code, but no labelled identification of the original R3 cavity Q14.
- Existing R3 bundles and formal notes: proof reductions and a peeling checker; no `Q14` labelled support or complete retained-face-to-edge incidence file.
- Dissertation tar archive listing: PDF papers and dissertation; not a machine-readable R3 face-incidence certificate. No evidence that a unique 14-face cavity can be inferred from the catalogue alone.

## What a valid peeling certificate needs
1. The 14 deleted temporal faces, identified by explicit spatial-edge and time-slab labels or by oriented four-edge cycles.
2. The exact 54 retained Bianchi-fill faces (or an exact Bianchi algorithm that deterministically derives them).
3. Every retained face incident to any candidate elimination edge, including exterior faces not in the 54-fill set.

The checker `audit.py` uses the full retained face set and tests that the edge is private at the moment of integration. It is conservative: failing peeling does not imply failure of the energy estimate.

## Coupled remainder
If a verified incidence file permits peeling a subset P of fill faces, then the exact identity is

    Z_R = (product_{p in P} z(lambda_p)) Z_{R\P}

and

    lambda E_R S_F = |P| lambda (-d/dlambda log z(lambda)) + lambda E_{R\P} S_{F\P}

for uniform couplings. This rigorously isolates the coupled remainder; it does not bound that remainder without further analysis.

## A structural warning
For an interior temporal plaquette of a complete three-periodic prism, a spatial edge is incident to temporal plaquettes in both neighboring slabs, and a temporal link at a spatial vertex is incident to all temporal faces meeting that vertex. Consequently, private edges are not generally available in the complete interior. Deleting 14 plaquettes can change the incidence locally; only the exact labelled support can decide which edges become private.

## Verification
`python -m unittest -v test_audit.py` passes four tests (positive, exterior-blocked, full-rank-without-peeling, partial peeling). `inventory.json` contains exact catalogue shapes and a SHA-256 hash.

## Proof status
The original-cavity peeling verdict and the volume-uniform energy estimate are **not proved** by these materials. A reconstructed *different* cavity must not be passed off as the original.

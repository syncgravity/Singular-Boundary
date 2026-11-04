# Original Whitney 11-face matrix: verified source

File: `global_whitney_11face.npz` supplied in project Source and mounted as `/mnt/data/global_whitney_11face.npz` in verification session.

SHA256: `d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf`
Bytes: `8448`
Members: `matrix` float64 (30,30), `edge_ids` int64 (30,), `eigenvalues` float64 (30,).
Computed eigvalsh min/max: `0.14317414869400802`, `1.1046593441618966`. Edge ID 13 matrix diagonal: `0.7778590280946629`. Stored eigenvalues match eigvalsh results exactly in numpy double precision.

The later `m5_whitney_candidate_2026-10-30.npz` is NOT the original: lambda range 0.196155044395 to 2.277516706271; edge13 diagonal 0.694741426782.

New chats: consult this file and Project Source; verify checksum before calculations. Do not ask for re-upload without checking Source and mounted files. Do not replace original with candidate. The binary itself is in Project Source; this repository file is the manifest, not a binary backup.

Outstanding: recover the exact historic matrix assembly rule; use original K=M^-1 with the two actual M5 spanning trees and gauge-invariant multiloop observables; test tree equivalence, then refinement scaling and relative center-cap. Open: continuum Yang-Mills mass gap.

# Certified eleven-face open Penrose disk extracted from M5 local incidence
Date: 2026-10-30
Status: Verified finite cell complex and product-Haar based-face kinematics. SU(2) smoothing Q_f not yet evaluated.

SOURCE: user-supplied penrose_study.zip, Approximant(M=5), penrose_faces. Extract exactly the face set D={0,1,3,2,4,154,150,11,10,7,8}, preserving original oriented edges and vertices, BUT DISCARD every other periodic face and treat each singly incident local edge as a FREE BOUNDARY EDGE. This defines a NEW OPEN DISK lattice; it is not a gauge-fixed sector of the periodic torus Hamiltonian.

EXECUTED TEST: 11 faces, 30 distinct primal links, 20 distinct vertices, Euler V-E+F=1, 14 two-face internal edges, 16 single-face boundary edges. Every internal shared link has opposite oriented face signs, all faces form a connected dual graph, the 16 boundary vertices have degree two within the boundary graph, and that graph is connected (one simple boundary). Target face 0 has edges {0,1,4,13}, all interior to D. Topologically, this is a connected orientable cellulated disk (assuming standard nondegenerate 2-cell embedding inherited locally). The boundary edge IDs are [7,9,11,16,25,26,34,86,87,88,89,291,295,297,300,372].

A maximal primal tree has V-1=19 links; thus E-(V-1)=11 independent link Haar variables. On the simply connected disk, choose rooted face words so they generate all 11 fundamental cycles without a torus surface relation; change of variables from product link Haar to product face Haar is triangular by selecting dual paths and uses Haar invariance. The remaining global conjugation gives the physical gauge-invariant Hilbert. In particular face 0 is a legitimate independent Haar variable at fixed remaining ten based-face holonomies, defining P_0 and Q_0=1-P_0.

This validates transferring the M5 *local oriented link incidence* and Fierz contraction identities to an open finite disk with its OWN electric and magnetic Hamiltonian, after retaining all 30 local edges with their specified positive a_e. Earlier M5 torus Q_f statements cannot be retroactively promoted without re-checking their precise observables and domain. The two smoothing words S3 and S14 from R3_M5_TEN_FACE_ORIENTED_TWO_LINK_FIERZ_2026-10-30.md remain to be expanded in these 11 based-face coordinates and conditionally Haar-projected. No nonzero or zero projection is claimed, nor a refinement-uniform cap theorem or continuum mass gap.

Executable geometry regression: research/scripts/validate_m5_open_disk.py.

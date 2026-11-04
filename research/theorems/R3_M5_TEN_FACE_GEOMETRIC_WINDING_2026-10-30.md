# Geometric winding of the M5 ten-face retained dual cycle
Date: 2026-10-30. Finite periodic Penrose approximant geometry CERTIFIED numerically with a wide nondegenerate margin. No non-Haar or continuum mass gap claim.

Source: supplied penrose_study.zip, penrose_causal_study.Approximant(M=5), wilson_torus.penrose_faces. Indexed ten-face closed dual walk [1,3,2,4,154,150,11,10,7,8,1], shared-link IDs [3,2,5,19,296,17,18,12,8,14], with opposite orientations verified in earlier incidence test.

For each face tuple (u,ua,uab,ub,i,j) in approximant.faces, define a lifted center in the physical projection as Qpar @ (nodes[u]+(e_i+e_j)/2), where e_i is a standard Z5 basis vector. Physical periodic translations Qpar@t1 and Qpar@t2 are respectively approximately [0,7.48331477] and [8.24621125,0]. Lift the consecutive dual centers to their nearest translated images. Only face centers 154 and 150 require the shift minus t1 for this cycle, and the walk closes with EXACT zero net period displacement (within numerical tolerance).

The lifted polygon has signed shoelace area approximately +1.8068678794016582 and standard atan2 total turning/winding about the center of deleted face 0 equal to +1 (within floating-point accuracy). The face-0 projected center is approximately [0.48507125,0.40089186]. Therefore the dual walk is a CONTRACTIBLE positively wound geometric loop surrounding face 0 in the periodic embedding. This is more specific than abstract graph cyclomatic rank or a noncontractible toroidal winding.

This geometric certificate does not show that any squarefree or repeated-insertion SU2 electric-resolvent coefficient is nonzero, nor prove all-orders non-Haar behavior, a Penrose disk bound, or the continuum Yang-Mills mass gap. The test must be transferred to an open-disk incidence and evaluated in the physical gauge-invariant Wilson Hilbert space. Executable regression at research/scripts/validate_m5_ten_face_winding.py.

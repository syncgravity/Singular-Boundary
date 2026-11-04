# Exact connected four-face Wilson electric resolvent on M5 chain 1-3-2-4
Date 2026-10-30. PROVED fixed finite periodic SU2 rational regression; no nonzero Q response yet.

Use periodic Penrose Approximant(M=5), face sequence [1,3,2,4], sharing consecutive edge IDs [3,2,5]. Nonconsecutive faces share no edges. Every connected face block B has a simple union boundary of length 2|B|+2. Let O_P be product of fundamental half-trace Wilson loops around each block of a partition P of the four faces into chain-connected blocks. There are 2^3=8 possible partitions. Under equal unit link electric weights and physical SU2 Casimir j(j+1), the exact electric action is T O_P = d_P O_P -(1/2) sum_{cuts c of P} O_(P merged across c), with d_P=(3/4)sum_B(2|B|+2)+(number of cuts)/2 = 11/2+2(number of blocks). SU2 Fierz gives the cross-edge term. For each nonempty subset J of chain faces, use F_empty=1 and F_J=T_perp^-1 sum_(g in J) p_g F_(J minus g), solved on connected-block partitions of its induced forest.

The final squarefree four-face coefficient has exact coefficients:
[1][3][2][4]:154/15795
[1][3,2][4]:227/223560
[1,3][2][4]:6103/5812560
[1][3][2,4]:6103/5812560
[1,3,2][4]:37189/220877280
[1][3,2,4]:37189/220877280
[1,3][2,4]:6103/55219320
[1,3,2,4]:3293/110438640.

Independent Python Fraction arithmetic checked all 15 nonempty subset electric residual equations exactly, using real archived M5 incidence and no link Casimir beyond the required SU2 fundamental trace fusion. Results: PASS exact four-face chain, all 15 subsets, eight final basis terms. The original electric source and four-face intermediate states are made solely of retained-loop observables; this does not imply an interacting deleted-holonomy Q response. No seventh-order coefficient or continuum gap proved.

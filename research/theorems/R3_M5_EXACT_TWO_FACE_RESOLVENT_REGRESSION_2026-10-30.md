# Exact M5 seven-face two-plaquette electric-resolvent regression
Date 2026-10-30. Verified symbolic SU(2) rational calculation; full seven-face amplitude OPEN.

From the supplied M5 periodic Penrose archive, the active seven-face set S={1,2,3,4,7,8,10} uses 22 links, with six links in two active plaquettes [2,3,5,8,12,14]. Faces 2 and 4 share link 5 with opposite oriented signs. Take every link electric coefficient a_e=1, physical Casimir j(j+1) and fundamental half trace p.

Let G=p_2 p_4 and U=p_(2 union 4), normalized half trace around six-edge union. SU2 Fierz identity and electric product formula give T G=(13/2)G-(1/2)U and T U=(9/2)U. Thus R G=(2/13)G+(2/117)U, where R=T_perp^-1. Since T p_2=T p_4=3p_2, the exact squarefree two-face coefficient from F(J)=R sum_g p_g F(J\g) is
F_{2,4}=(4/39)G+(4/351)U.
Substitution recovers T F_{2,4}=(2/3)G exactly. The rational coefficients were checked with fractions in an independent Python run against the archived face incidence and link signs. This is an exact analytical regression target for a spin-network solver and verifies correct j(j+1) normalization.

This computation DOES NOT evaluate the seventh-order 127-subset response, its conditioned spin-one probe amplitude, an open-disk Penrose vacuum, or the continuum gap. The two-face subblock cannot be substituted for the full seven-face response.

Executable source saved in /mnt/data/validate_m5_two_face.py during this session, and should be copied to scripts/ if maintained with repository CI.

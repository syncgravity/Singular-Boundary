# M5 ten-face exact oriented two-link Fierz smoothings
Date 2026-10-30. PROVED SU2 algebraic identity and tested against explicit fundamental matrices. Q_f PROJECTION NOT EVALUATED.

Reconstructed from user-supplied penrose_study.zip with Approximant(M=5), penrose_faces and actual directed edge endpoints (i,z,j) from a.edges. Face 1 word A=[(0,+),(14,+),(86,-),(3,-)]. The nine-face boundary word B, starting at edge 3, is:
[(3,+),(87,+),(89,-),(88,+),(372,+),(300,-),(297,-),(295,-),(291,+),(16,+),(34,+),(26,-),(25,-),(7,-),(9,+),(11,+),(14,-),(13,+),(4,-),(1,-)].
Here each tuple means a link ID and exponent sign; tracing these cyclic words is gauge-invariant.

For shared edge 3, smooth the opposite-oriented word occurrences by deleting (3,-) from A and (3,+) from B and concatenating the resulting cyclic remainders. The 22-edge smoothing word S3 is
[(0,+),(14,+),(86,-),(87,+),(89,-),(88,+),(372,+),(300,-),(297,-),(295,-),(291,+),(16,+),(34,+),(26,-),(25,-),(7,-),(9,+),(11,+),(14,-),(13,+),(4,-),(1,-)].
For shared edge 14, the analogous 22-edge smoothing S14 is
[(86,-),(3,-),(0,+),(13,+),(4,-),(1,-),(3,+),(87,+),(89,-),(88,+),(372,+),(300,-),(297,-),(295,-),(291,+),(16,+),(34,+),(26,-),(25,-),(7,-),(9,+),(11,+)].

With p_W=(1/2)Tr W, unit electric weights and Lie generators X_a=i sigma_a/2, the exact shared-edge identity is Gamma_e(p_A,p_B)=1/4(p_Se-p_A p_B), hence Gamma_T(p_A,p_B)=1/4(p_S3+p_S14-2p_A p_B). Independent explicit random SU2 matrix multiplication with inserted link right generators gave direct derivatives and Fierz values:
edge 3: -0.14646419513398 vs -0.14646419513397999,
edge 14: -0.20249183025320308 vs -0.2024918302532031.
These are algebraic regression test samples, not physical vacuum expectations or certified rational interval enclosures.

Critical: BOTH smoothing words are 22-step walks containing one repeated/shared link, not merely the 16-edge outer and 4-edge inner traces separately. Their joint Haar-conditional Q_f projection is NOT computed in this note. No claim that it is nonzero or zero. No bulk cap or mass gap established.

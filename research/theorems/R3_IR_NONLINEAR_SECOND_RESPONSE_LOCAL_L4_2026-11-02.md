# Local L4 Hessian control of first and second coupling responses (2026-11-02)

Conditional on the archived dressed weighted W2,4 resolvent certificate with C4=127.90141971854507 and geometric original-link bounds B=120/11, G=sqrt(21)*67/13824, q=5/6, the exact zero-coupling responses u1=-RQW and u2=2RQ|grad u1|^2 satisfy per original link e, uniformly in N:

||grad_e u1||infinity <= 13 B G = 3.1497975302;
||Hess_(e,*) u1||_(L4(ell2)) <= 13 C4 G = 36.9291611280;
||grad_e |grad u1|^2||4 <= 2(13BG)(C4G)(841) = 15049.938309651758;
||Hess_(e,*) u2||_(L4(ell2)) <= 2 C4 sqrt(161/11)*15049.938309651758 = 14728437.49653106.

The geometric majorants are sum_j q^d(e,S_j)<=13, sum_d q^(2d(e,d))<=161/11 and sum_j,d q^max(d(e,S_j),d(d,S_j))<=841. Mixed Hessian components use symmetry plus increasing source-distance weights. The globally supported quadratic source uses decreasing target-link weights. All estimates are conditional and only at lambda=0; the huge constant does not imply pointwise ground-state curvature or the interacting lambda=1 gap. Neither a continuum Yang-Mills gap nor a full independent geometric verification is claimed. Full proof, verifier, log, hashes in project Library Proof Audits.
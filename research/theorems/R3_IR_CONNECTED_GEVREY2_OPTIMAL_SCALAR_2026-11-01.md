# Gevrey-2 sharpening and positive scalar optimality — 2026-11-01

Reviewed all 415 rows of the canonical claims ledger (392 R3-IR, 11 R3-PRISM, 11 R2, 1 D1), including historical duplicate claim identifiers R3-IR-378/379/380. This theorem sharpens the *existing* formal connected-score recurrence from R3_IR_FORMAL_CONNECTED_GEVREY8_2026-11-01.md, not a new SU(2) recurrence proof. See the complete report and checker in the matching Library Proof Audits ZIP.

Inherited recurrence (q=2^(5/2), rho>=0, A_1=1/3):
[
A_n le (e^ho/2)(n+4)sum_{j=1}^{n-1}sqrt{j(j+2)(n-j)(n-j+2)}q^{min(j,n-j)}A_jA_{n-j}.
]
**Theorem:** With (alpha=q/16=2^{-3/2}) and (M_2=144sum_{hge1}h^3[1+(2h+1)^2]alpha^h<67574), for all n>=1,
[
oxed{A_n(ho)lerac13left(rac{M_2e^ho}{3}ight)^{n-1}(n!)^2.}
]
Uniform in finite chain length, assuming the original linked interval recurrence and its original-link operator hypotheses.

**Proof:** Factorial-normalize the convolution and set h=min(j,n-j), B=binom(n,j). By (n+4)/2<=3n/2, sqrt[j(j+2)k(k+2)]<=3jk<=3hn and two orientations, normalized kernel <=9 sum_{h<=n/2}n² h q^h/B². For h<=n/4, B>=(n/h)^h gives n²h/B²<=16h³/16^h. For h>n/4, n<4h and B>=binom(2h,h)>=4^h/(2h+1) give n²h/B²<=16h³(2h+1)²/16^h. Sum gives M2; factorial induction finishes.

**Optimality of the *positive scalar equality* recurrence only:** Its one-leaf term satisfies a_n>=c_rho n²a_{n-1} for n>=3, giving a_n>=a_2 c_rho^(n-2)(n!/2!)². Thus no Gevrey-s bound with s<2 holds for that scalar majorant. Not a lower bound on signed SU(2) coefficients.

**Verification:** executable Python verifier checked normalized exact kernel through n=150, maximum approximately 70.14393 at n=8; analytic inequalities prove the all-order result. Library ZIP includes complete Markdown, script, log and SHA-256 manifest.

**Research verdict:** Gevrey-2 is proved from the previously established finite open straight SU(2) formal connected recurrence and is optimal for the associated positive equality majorant. True signed coefficients may have cancellations. Ordinary convergence, Borel summability, lambda=1 interacting gap, Penrose signed current, and continuum Yang–Mills mass gap remain unproved.

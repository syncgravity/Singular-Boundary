# Gevrey-3 sharpening of the connected-score activity majorant (2026-11-01)

**Depends on:** earlier `R3_IR_FORMAL_CONNECTED_GEVREY8_2026-11-01.md` formal SU(2) connected-score recurrence. All hypotheses, root-weighted activities and `S=log Omega^2` normalization are inherited; this is not a fresh proof of that recurrence.

The previously proved recurrence states `A_1(rho)=1/3` and
[
A_n(ho)le {e^hoover2}(n+4)sum_{j=1}^{n-1}
sqrt{j(j+2)(n-j)(n-j+2)}q^{min(j,n-j)}A_j(ho)A_{n-j}(ho),
quad q=2^{5/2}.
]
Define `L(x)=x(1+4x+x^2)/(1-x)^4`, `M=144[L(q/8)+L(q/64)]<59914`.
**Theorem** (sharpening): for all n≥1 and rho≥0,
[
oxed{A_n(ho)lerac13left(rac{Me^ho}{3}ight)^{n-1}(n!)^3.}
]
Uniform in chain length.

**Proof:** Normalize the convolution by `(n!)^3` and write h=min(j,n-j), B=binom(n,j). Because (n+4)/2≤3n/2 and sqrt[j(j+2)k(k+2)]≤3jk≤3hn, the normalized kernel is at most `9 sum_{h≤n/2}n² h q^h/B³`. For h≤n/4, `B≥(n/h)^h` and `n²h/B³≤16h³/64^h`. For n/4<h≤n/2, `B≥2^h` and `n²h/B³≤16h³/8^h`. The normalized kernel is therefore bounded by `M=144∑h³[(q/64)^h+(q/8)^h]`. Since q/8=1/√2<1, M is finite. Factorial induction proves the displayed activity bound.

The conservative global M is approximately 59913.16224; finite independent checks through order 150 found maximum normalized kernel approximately 9.48415723 at n=4. Verification scripts and detailed report are retained in Library Proof Audits as `R3_IR_CONNECTED_GEVREY3_SHARPENING_2026-11-01.zip`.

**Scope boundary:** This is an all-orders bound on *formal coefficients*, not ordinary convergence, not Gevrey optimality, and not a lambda=1 gap. The newer `S=log Omega` tree convention has a different Riccati factor and should not be conflated with this inherited `S=log Omega²` recurrence. The physical gauge-fixed embedding assumptions of the earlier theorem remain necessary. Penrose signed-current and continuum mass gap remain open.

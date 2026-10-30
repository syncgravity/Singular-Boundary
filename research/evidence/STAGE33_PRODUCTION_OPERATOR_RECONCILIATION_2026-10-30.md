# Stage 33/34 production operator convention reconciliation

Date: 2026-10-30. This is an **aggregate numerical operator reconciliation**, not a continuum or physical mass-gap theorem.

Stage 33 raw archive records four trace-like channels R0,R1,R2,R3, whereas production reports controls 1,2,3 and then auxiliary, with a 1-minus-trace convention. The mapping checked against the recovered Stage 19 weighted_observe implementation and Stage 34 exact-equivalence tests is

\[P=(1-R_1,1-R_2,1-R_3,1-R_0).\]

At t=0 the recorded raw means are R=(0.0782949577087022,0.30355705308477476,0.14283401391872197,0.047255028400825815). Mapped production values are P=(0.6964429469152252,0.8571659860812780,0.9527449715991742,0.9217050422912978), matching the stage33_report production_t0 within floating-point precision (max discrepancy ~4.3e-15 in the prior direct array audit).

Stage 34 reports max aggregate discrepancy ~1.13e-14 over 4 channels x 20 time slices. Stage 32 source probe explains why earlier signed one-based indexing could not directly substitute for production zero-based index plus separate orientation sign. The earlier raw-versus-production *unmapped* discrepancy is **superseded, not erased**.

Scope limits: equality of aggregated observables and unit tests does not independently prove per-path implementation identity, Markov-chain mixing, correctness of Wilson-action normalization, a spectral mass, or regulator-uniformity. Stage 35 remains a production measurement pipeline, not a completed ensemble proof.

# Evidence and independent review protocol

**A future researcher or AI must not conflate the following verbs.**

| Level | Meaning | Required evidence |
|---|---|---|
| Located | A path, filename or archive pointer is known | Stable locator |
| Retrieved | Actual full bytes or full text obtained | Exact source and byte/line completeness check |
| Read | Every line/section of the specified item examined in context | Review log identifying range, version, exclusions and ambiguities |
| Reconciled | Later corrections and earlier dependencies mapped | Change/correction crosswalk |
| Mathematically audited | Each asserted implication and equation independently checked | Proof audit report, assumptions, countercases, reviewer |
| Reproduced | Actual executable code run against authentic inputs | Environment, command, hashes, stdout, residuals |
| Publication-ready | Independent auditors sign off on all essential lemmas, computation and provenance | Versioned release gate and peer-review plan |

No prior conversation statement of “read” counts as reproducibility evidence. An indexed theorem is not an audited theorem. A reconstructed experiment is not an original simulation. A date does not indicate mathematical supersession.

## Session startup

1. Record exact branch and commit, repository tree state and applicable scope.
2. Read [current checkpoint](CURRENT_CHECKPOINT.md), [dependencies](PROOF_DEPENDENCIES.md), claim ledger and source theorem(s) **in full** before extending them.
3. Trace each correction backwards; never compute an already certified coefficient because it appears unresolved in an older report.
4. Check whether scripts, original inputs and companion ZIPs were **actually retrieved**, not merely linked.
5. Define the *new* obligation and explicitly exclude settled work.

## Session finish

Record: exact sources examined; results previously known versus newly proved; assumptions; equations verified; tests run and skipped; source hashes; commit; library/raw preservation; open dependencies; next noncircular task. “No new result” is a valid audit outcome.

## Publication gate

Until independent equation-by-equation and script-by-script audit, this is a **research navigation system**. Do not claim a Yang–Mills continuum gap, or elevate finite 2+1D reference results to 3+1D statements.

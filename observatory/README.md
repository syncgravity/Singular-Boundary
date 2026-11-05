# Research Observatory v2.25-draft integration supplement

Open `index.html` together with `catalog.js`, `audit.js`, and `proofpaths.js` in the same folder (works without a server). The **740-record catalog** is generated from the immutable source Git tree `fd1c1c1c8db078f8ec9d591d182059bd1635b164` and records paths, Git blob identifiers and source sizes. Only 12 selected theorem bodies have editorial annotations; all remaining records explicitly say `Indexed path and Git blob only`.

The site includes a P0–P5 dependency navigator, searchable 740-file theorem catalog, four candidate proof routes, exact missing implications, the supplied historical archive audit, and evidence controls.

**Do not publish publicly before privacy and source-publication review.** Source links refer to the private GitHub repository. No secrets or binary data are embedded. The continuum mass gap is open.

See `HISTORICAL_DOUBLE_AUDIT_2026-11-04.md` for source-level findings and limitations.

To replay the mounted archive checks: `python observatory/tools/verify_stage26.py /path/to/uploads` (NumPy required). The checker makes no changes to inputs. The original archives must be supplied separately; this repository does not automatically contain them.


## New P0–P5 theorem integration (private draft)

[`integration.html`](integration.html) presents the quantified common-regulator theorem, conditional positive-time spectral-support lemma, six interactive gate interfaces, a geometric-versus-quantum-versus-double-uniform acceptance table, explicit Z5/prism/cubic model distinctions, and an incremental dissertation publication plan. This view is **proposed in a review branch only**; it is not a new certified theorem, not a change to the 740-path baseline catalog, and not deployed on GitHub Pages. Supporting drafts are in `docs/research/UNIFORM_INTERACTING_THEOREM_BRIDGE_2026-11-04.md` and `docs/research/DISSERTATION_EVOLUTION_AND_PUBLICATION_PLAN_2026-11-04.md` (both source paths relative to the repository root). The structural validator is `observatory/tools/verify_uniform_integration_contract.py` and checks presentation/contracts only, not mathematical truth.

# Publishing the Research Observatory

Public URL after GitHub Pages activation: https://syncgravity.github.io/singular-boundary/

This repository is **private**; GitHub Pages static deployments can nevertheless be **public** depending on account and plan. Only `observatory/` is uploaded by the workflow. The static site exposes 761 source-linked theorem filenames (740 historical baseline plus 21 later sources), curated proof-status records, historical audit summaries and repository URLs; it does **not** include private source bodies, uploaded binaries, or credentials. Private GitHub links require authenticated access.

1. Open **Settings → Pages** for `syncgravity/singular-boundary`.
2. Under **Build and deployment**, choose **GitHub Actions**.
3. Inspect the workflow at **Actions → Research Observatory · GitHub Pages**; use **Run workflow** if needed. The workflow deploys automatically when a commit lands on `main` that changes `observatory/**` or this workflow; manual `workflow_dispatch` remains available.
4. Inspect the verified Pages URL and publication status. Do not infer success from a prepared workflow alone.

If the Pages controls are unavailable for the private repository, check the repository owner's plan or organization policy. Do not make the whole research repository public merely to publish this site.

The public site does not certify historical claims or prove the Yang–Mills mass gap.

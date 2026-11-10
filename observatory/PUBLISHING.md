# Publishing the Research Observatory

**Public site:** https://syncgravity.github.io/singular-boundary/  
**Source repository:** https://github.com/syncgravity/singular-boundary

The source repository is public. Its tracked research, documentation, code, and history are therefore publicly accessible on GitHub; GitHub Pages is a separate, curated static publication of the Observatory interface.

## What the Pages workflow publishes

The workflow assembles a site artifact from the browser-facing Observatory assets:

- HTML pages, JavaScript, CSS, and the graph/overlay JSON data required by the interface;
- the concept-index JSON used by the conceptual atlas;
- the three linked research guides: the mathematical-physics guide, historical double audit, and proof-path discovery note.

It deliberately excludes the `observatory/tools/` verification scripts and `data-manifest.json` from the Pages artifact. It does not upload the original ZIP/NPZ research archives or other repository files as part of the site artifact. The interface links to source records in the public GitHub repository. Indexing and publication do not certify a theorem or close a continuum proof gate.

## Enable and verify publication

1. Open **Settings → Pages** for `syncgravity/singular-boundary`.
2. Under **Build and deployment**, set **Source** to **GitHub Actions** before merging, if the selector is available.
3. Merge the Pages-readiness change to `main`. The workflow then runs automatically on commits affecting `observatory/**` or the workflow itself. If Pages was enabled only after the merge, start the workflow manually from **Actions → Research Observatory · GitHub Pages → Run workflow**.
4. Wait for the deployment job to complete, then verify the environment URL and the public site URL above. A configured workflow or a public repository alone does not mean the site has been deployed.

If Pages is not available in Settings, the repository owner must resolve the account or organization policy that prevents Pages activation.

The public site states the research limitations explicitly: continuum Yang–Mills existence and the physical mass-gap gates remain OPEN.

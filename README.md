# FrameShift Lab

**A private, evidence-first research workbench for games and software.**

FrameShift brings together the agent workflow ideas behind [Craft Anything](https://github.com/storytold/craft-anything) and [REA](https://github.com/morluto/rea), and the compatibility research focus of [AnyPS5](https://github.com/boykopovar/AnyPS5), with a broader directory of tools for binaries, runtimes, managed code, mobile apps, formats, graphics, networking and compatibility.

## What makes this hub useful

- Search and compare tools by specialty, platform and license.
- Follow question-led playbooks for native binaries, managed code, Android, formats, runtime behavior, graphics, networking and compatibility.
- Keep a local notebook with separate observation, verified fact, hypothesis and interpretation labels.
- Record source links and authorization scope; export a portable JSON project or Markdown report.
- Calculate a SHA-256 digest for a selected local file in the browser. File bytes are never uploaded by the site.
- Review upstream changes through proposed metadata-only merge requests, never automatic merges.

FrameShift coordinates research around independent projects; it does not replace their specialist analysis engines or claim their capabilities as its own. It contains original site code and metadata only. It does not redistribute upstream source, game files, firmware, keys, copyrighted assets, or third-party binaries. Each upstream project keeps its own license and terms.

## Scope

Use the catalog and workbench with software and devices you own or have permission to examine, and follow applicable law and platform terms. Supported research topics include learning, interoperability, preservation, accessibility, authorized modding, debugging, graphics development and defensive security. This project does not provide instructions or features for bypassing DRM, defeating anti-cheat, evading access controls, manipulating third-party services, or obtaining paid content without authorization.

Do not put passwords, private keys, account information, personal data, copyrighted asset files, firmware or game binaries in the notebook. Notebook entries are saved in browser storage on the device and browser origin where the site is open; use the export function to back them up or move them. Local browser storage is not encrypted by FrameShift.

## Host it

GitLab is the intended canonical home. Import this repository into a GitLab project named `frameshift-lab`, set it as the source of truth, and enable **Settings → Pages**. The included `.gitlab-ci.yml` publishes `site/` and `catalog.json`. GitHub Pages is currently a live discovery copy.

The site is static and has no external JavaScript dependencies. The GitHub Actions workflow publishes `site/` plus the catalog JSON.

## Reviewed upstream updates

The scheduled GitLab pipeline checks the public GitHub repositories listed in `upstream-lock.json` for new commit IDs. If any move, it creates a branch and merge request that changes only the pointer file. It never imports or merges upstream source. On GitLab, add a masked project access token variable named `GITLAB_UPDATE_TOKEN` with API permission to create branches, commits and merge requests. Then create a weekly pipeline schedule on the default branch. Protect the variable and default branch according to your GitLab settings.

A reviewer should inspect upstream releases, license changes, project activity, and catalog accuracy before merging. The initial scheduled run proposes a baseline commit map; review and merge that baseline first. No merge automation is configured.

## Contributing

Suggest tools by opening an issue or merge request. Include canonical project URL, purpose, supported platforms, license source, maintenance status, inputs/outputs, and a lawful-use note. Do not submit copyrighted game assets, firmware, keys, personal data, or circumvention instructions. License labels should be checked against each project’s own current terms.

## License

Original site code and documentation are MIT licensed. Catalog entries are factual pointers to independent projects; their licenses are not changed by inclusion. See `LICENSE` and each upstream project's own license.

# FrameShift Lab

**A field guide to understanding how games and software work.**

FrameShift Lab is a curated, link-first research hub for games, applications, runtimes, formats, and the tools used to study them. It brings together the workflow ideas behind [Craft Anything](https://github.com/storytold/craft-anything), [REA](https://github.com/morluto/rea), and [AnyPS5](https://github.com/boykopovar/AnyPS5), alongside widely useful reverse-engineering tools.

This repository contains original site text and metadata only. It does not redistribute upstream source, game files, firmware, keys, copyrighted assets, or third-party binaries. Each upstream project keeps its own license and terms.

## Scope

Use these resources with software and devices you own or have permission to examine, and follow applicable law and platform terms. Suitable topics include learning, interoperability, preservation, accessibility, authorized modding, debugging, and defensive security. The hub does not provide instructions or features for bypassing DRM, defeating anti-cheat, evading access controls, or obtaining paid content without authorization.

## Host it

GitLab is the intended canonical home. Create a GitLab project named `frameshift-lab`, push this repository, and enable **Settings → Pages**. The included `.gitlab-ci.yml` builds the static site into `public/`. A GitHub Pages copy is a discovery mirror; keep GitLab as the source of truth.

The `site/` directory is a dependency-free static site. It can also be published with GitHub Pages using the included Actions workflow.

## Reviewed upstream updates

The scheduled GitLab pipeline checks the catalog's upstream repositories for new commits. When it finds changes, it updates only `upstream-lock.json` and opens a GitLab merge request for review. It never imports or merges upstream code. Configure a masked, protected project variable named `GITLAB_UPDATE_TOKEN` with permission to push a branch and create merge requests; then create a weekly pipeline schedule for the default branch. Without that variable the job reports that no update credential is configured and exits safely.

Review a proposed update by checking the upstream diff, release notes, license, project health, and whether the catalog description remains accurate. Merge manually only after review.

## Contributing

Suggest tools by opening an issue or merge request. Include the canonical project URL, purpose, supported platforms, license link, maintenance status, and a concise lawful-use note. Do not submit copyrighted game assets, firmware, keys, account data, or circumvention instructions.

## License

Original site code and documentation in this repository are MIT licensed. Catalog entries are factual pointers to independent projects; their licenses are not changed by inclusion. See `LICENSE` and each upstream project's own license.

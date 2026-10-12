# Gemini Notebook Workshop — Participant Companion

Participant reference for HKMA K S Lo College Tech in Ed Task Force, 13 Oct 2026. The web companion contains 33 sequenced workshop pages, including eight supplied Studio-output comparison pages and four video-comparison pages, plus ten bilingual prompt detail pages. The downloadable PowerPoint is the matching 33-slide export.

## Structure

- `content/slides.json`: faithful, structured slide-page content.
- `content/prompt-texts.json`: latest concise bilingual examples and reusable templates.
- `content/prompt-examples-source.md`: situations and source-selection guidance for all ten examples.
- `src/styles.css` and `src/app.js`: responsive Swiss Minimal design and progressive enhancements.
- `scripts/build.py`: dependency-free static HTML generator, producing `site/`.
- `public/assets/`: supplied logos, screenshots, local video posters and compressed WebP/JPEG Studio display images.
- `public/downloads/`: supplied Blueprint PDFs, presentation, bilingual prompt handouts and byte-preserved original Studio outputs.

## Build and preview

```sh
python3 scripts/build.py
python3 -m http.server 3000 --bind 0.0.0.0 --directory site
```

Python 3.10+ is sufficient. No Node packages, database, AI service or login are needed. Page contents are delivered as static HTML and remain readable without JavaScript. JavaScript enhances the contents dialog, filtering, copying, keyboard shortcuts, deferred YouTube playback and printing. The video pages show local posters until a participant explicitly selects playback; a prominent YouTube link remains available without JavaScript.

## GitHub Pages

The destination is `https://hkmakslo.github.io/tie-261013/`. Source code lives on `main`; GitHub Pages serves the static-only `gh-pages` branch from its root. Every internal link and asset reference is relative, so nested pages work at `/tie-261013` without a client-side fallback or rewriting rules. `.nojekyll` is supplied. No custom GitHub Actions workflow is required.

After reviewing source changes, rebuild and run the checks, commit them on `main`, and push `main`. Then update the publishing branch without rewriting history:

```sh
git subtree split --prefix=site -b gh-pages
git push origin gh-pages:refs/heads/gh-pages
python3 scripts/verify_live.py
```

The public site includes only the approved workshop content and supplied public documents, not a private Notebook link, student work or sign-in credentials. Official reference links direct participants to the applicable documents; teachers must add their own subject notes where indicated.

The original PPT is not modified by this project. The supplied Studio outputs are AI-generated drafts for comparison, not independently verified policy: figures, dates, mandates, strategies, funding and curriculum claims within them must be checked against original sources. Prompt examples are source-aware workshop adaptations, not official EDB or HKEAA instructions or a guarantee of AI accuracy.

## Independent publication

This repository is the independent hkmakslo copy requested by the owner. The previous ksloenglish repository and its Pages site are unchanged. The Manus website project is still linked to the previous repository; updates to this copy must be committed and pushed here explicitly.

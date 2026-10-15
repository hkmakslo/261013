# Gemini Notebook Workshop — Participant Companion

Participant reference for **Gemini Notebook Workshop (Advanced Level)**, HKMA K S Lo College Tech in Ed Task Force, 13 Oct 2026. The companion contains **35 sequenced workshop pages**, ten bilingual prompt pages and a resource page. Its downloadable PowerPoint is the matching 35-slide editable export.

## Structure

- `content/slides.json`: authoritative slide-page content and ordering.
- `content/prompt-texts.json`: concise bilingual examples and reusable templates.
- `content/prompt-examples-source.md`: situations and source-selection guidance.
- `src/styles.css` and `src/app.js`: responsive Swiss Minimal styling and progressive enhancements.
- `scripts/build.py`: static HTML generator, producing `site/`.
- `public/assets/`: supplied branding, screenshots, video posters and Studio display images.
- `public/downloads/`: Blueprint PDFs, presentation, bilingual handouts and original Studio outputs.

## Build and checks

```sh
python3 scripts/build.py
python3 scripts/check_site.py
python3 -m py_compile scripts/build.py scripts/check_site.py scripts/verify_live.py
node --check src/app.js
```

The builder needs Python 3.10+ and the standard library. The optional validation script additionally uses Beautiful Soup and Pillow. No application dependencies, database, AI service or participant login are required. HTML content and navigation remain usable without JavaScript; JavaScript enhances menus, filtering, copying, keyboard navigation and participant-controlled YouTube playback.

For local preview:

```sh
python3 -m http.server 3000 --bind 0.0.0.0 --directory site
```

## GitHub Pages

The publication repository is **hkmakslo/261013** and the intended public URL is **https://hkmakslo.github.io/261013/**. Source lives on `main`; GitHub Pages serves `gh-pages` from the branch root. Internal navigation and asset paths are relative, including nested pages. `.nojekyll` is supplied, and no custom GitHub Actions workflow is required.

After checking intended source changes and integrating any remote changes without overwriting work:

```sh
python3 scripts/build.py
python3 scripts/check_site.py
git add README.md TODO.md content scripts src public site
git commit -m "Update workshop companion"
git push origin main
PAGES_COMMIT=$(git subtree split --prefix=site HEAD)
git push origin "$PAGES_COMMIT":refs/heads/gh-pages
python3 scripts/verify_live.py
```

Use normal pushes, never force-push. The bounded verifier waits for the expected homepage and then checks the published pages, assets and downloads against local bytes.

## Account and organisation access

The authenticated personal account remains **ksloenglish**. The **Manus Connector** GitHub App is installed on both ksloenglish and **hkmakslo**, with the organisation installation approved for all current and future repositories on 15 Oct 2026. Choose the appropriate repository owner when publishing; no account switch is needed for these authorised destinations. Repository administration and write access were verified through the existing connection. Organisation-wide OAuth restrictions were retained, and Pipedream was not granted organisation access.

Repository creation and code pushes succeeded. The Pages-creation API request returned HTTP 403, but the owner settings screen already showed the required `gh-pages` / root publishing source, and all 92 public files were subsequently verified live. For a future repository, a one-time Pages source setting may need to be enabled in GitHub’s owner interface; that is separate from switching the connected personal account. Subsequent updates to an already configured site use the normal branch pushes above.

This is an **independent GitHub Pages copy**. The former website under the renamed **hkmakslo-admin** personal account was not modified. The managed website connection was not switched; future changes to this organisation copy must be pushed explicitly to **hkmakslo/261013**.

## Content boundaries

Only approved workshop content and supplied public documents are included—not private Notebook links, identifiable student work or credentials. Teachers must add their own authorised subject notes where indicated. Original Studio outputs remain AI-generated drafts for comparison, not independently verified policy. Check embedded figures, dates, mandates and curriculum claims against original sources before use. Prompts are workshop adaptations, not official EDB/HKEAA instructions or guarantees of accuracy.

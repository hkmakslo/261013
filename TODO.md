# Participant companion outcomes

- [x] Faithful slide companion: Create 19 distinct web-optimised pages preserving all information and the sequence of the latest PowerPoint, one page for each slide. Do not alter the PPT.
- [x] Responsive Swiss Minimal design: off-white, near-black, orange, Arial-compatible typography, supplied discreet Task Force and Gemini Notebook logos; phone, tablet and desktop layouts with wrapped content, accessible typography, touch targets and keyboard navigation.
- [x] Navigation: previous, next, home/contents and direct page links with clear current-page context; searchable contents and prompt index.
- [x] Clickable resources: school access page on page 4, both supplied Blueprint PDF downloads on page 8, workshop Padlet on page 14, clickable ten-prompt titles on page 15; optional PowerPoint and handout downloads.
- [x] Ten dedicated prompt pages: title, situation, sources to add to Notebook, concise year-free English and Traditional Chinese prompts from the latest examples, in wrapping Markdown-style code boxes with copy buttons. Retain required answer-language instructions in those prompts.
- [x] GitHub hosting: prepare static output with repository-relative paths for K S Lo English GitHub at /tie-261013; confirm any new public repository/publication choices, then verify live pages and downloads. Do not deploy to an alternative public domain instead.
- [x] Independent review: read-only implementation review against these outcomes; resolve confirmed defects before publication.

## Evidence

`python3 scripts/check_site.py` passes all 30 pages, relative links, copy targets, slide-point parity, exact bilingual examples, original PDF checksums and the 19-slide PowerPoint. All 35 preview page/download URLs return HTTP 200. Mobile views were inspected for the cover, format page and prompt example; desktop views were inspected for the Studio and prompt-index pages. Independent review identified small-label contrast and no-JavaScript direct-navigation issues; both are corrected and verified in the generated site. The user approved the public repository and publication. Repository connection completed, and the live site at https://ksloenglish.github.io/tie-261013/ passed exact-byte checks for 42 pages/assets/downloads. Page 8 now uses prominent Download Chinese version and Download English version action labels; the publishing update is verified with scripts/verify_live.py.

## Navigation prominence update

- [x] Make Previous and Next controls prominent on every slide, prompt and resource page, with large eye-catching arrow icons, clear button boundaries, accessible contrast and responsive touch-friendly sizing. Preserve all existing destinations and keyboard navigation, and publish the update to the established GitHub Pages site.

The controls use bold SVG arrows in circular badges, a bordered white Previous button and a high-contrast orange Next button. Buttons stack on smaller phones and remain side by side on wider screens. All 30 pages retain their original link destinations and pass the existing content checks. Mobile page 8 and a desktop prompt-detail page were inspected for wrapping and button prominence. The stylesheet URL is content-versioned for returning visitors; live publication is checked with the existing verification script.

## Independent hkmakslo publication

- [x] Publish the current site to public hkmakslo/tie-261013 and verify all live pages and downloads. Preserve the old ksloenglish repository, site and Manus binding. Future updates must be pushed to this independent repository explicitly.

Source and static website branches were successfully pushed to hkmakslo/tie-261013. GitHub Pages creation returned HTTP 403 Resource not accessible by integration; publication remains pending owner enablement in Repository Settings → Pages. No changes were pushed to the ksloenglish repository.

GitHub Pages was enabled by the owner and returned HTTP 200. Navigation now uses compact padding, 38px arrow badges and 72px desktop / 68px mobile minimum heights (down from 116px / 94px), while preserving labels, wrapping and all destinations. Live exact-file checks are run after publishing this update.

## Prompt-page navigation update

- [x] All ten prompt pages have a compact Previous button returning to the all-ten-prompts page, no sequential Next button, and a top-right dropdown listing all ten prompt titles with the current prompt indicated. Preserve the slide-page navigation and bilingual prompt content, support keyboard and mobile use, and publish to hkmakslo GitHub Pages.

Prompt navigation passed HTTP-based Chromium checks at 375, 768 and 1440px, including all-ten dropdown options, current-page indication, Escape/outside dismissal, prompt switching, index return and operation without JavaScript. Complete existing content checks also passed. Live publishing is verified with scripts/verify_live.py.

## Examples before prompt overview

- [x] Move the ten-prompt overview from slide/page 15 to slide/page 18 immediately before conclusion 19. Situation, English example and Chinese example become slides/pages 15–17; change their headings from Example 1 to Example. Update the website navigation, prompt-index return links and downloadable PowerPoint to match, preserving the prompt dropdown and bilingual text.

Verified reordered PowerPoint text, all nineteen slide numbers, matching web pages, ten prompt-index return links and responsive dropdown navigation. The latest exported PPT is included in public/downloads.

## Social-preview card update

- [x] Use the supplied HKMA K S Lo College / Tech in Ed artwork as the homepage social-preview image. Preserve the complete 3:2 artwork in a 1200 × 630 px letterboxed JPEG; do not crop its logos. Add public absolute `og:image` and matching Twitter image metadata, plus image dimensions and alt text. Publish the new image filename and verify raw live metadata and image dimensions.

## Supplied social-preview artwork refresh

- [x] Replace the WhatsApp/Open Graph image with the newly supplied HKMA K S Lo College / Tech in Ed artwork. Preserve the full artwork within a fresh 1200 × 630 px card, publish it at a new public filename to encourage social-preview refresh, and update matching Open Graph and Twitter metadata.

## Full-bleed WhatsApp preview crop

- [x] Crop the newly supplied 3:2 artwork centrally to the 1.91:1 WhatsApp/Open Graph ratio, so no white letterbox bars appear at the sides. Keep both logos intact, publish the cropped card at a fresh filename, and update all social-image metadata.

## Slide 14 wording update

- [x] Match the supplied Slide 14 reference: “Post your Studio output” on the black first line and “on Padlet.” on the orange second line. Keep the first upload point as “Upload the output or screenshot.” Mirror the page on the website and refresh the downloadable editable PowerPoint.

## Workshop links simplification

- [x] On the Workshop downloads & useful links page, keep only the School Notebook access and Workshop Padlet buttons; remove the four small supplementary links beneath them.

## Footer action cleanup

- [x] Remove the Downloads & links and Print this page actions from the footer of every slide, resource and prompt page.

## Cover label update

- [x] Replace the cover label “CONTINUING PROFESSIONAL DEVELOPMENT” with “HKMA K S LO COLLEGE” in both the workshop PowerPoint and the matching participant website cover.

## Presenter and Studio examples

- [x] Add “Presented by Ken Kum” discreetly below the cover subtitle, preserving the established title hierarchy and branding.
- [x] Insert eight website pages after Slide 13: infographic default, exact custom prompt/settings, customised output, readable close-up; followed by slide-deck default, exact custom prompt, customised output, readable content-page example. Retain the supplied generated outputs as examples, not independently verified policy statements.
- [x] Renumber subsequent website pages; keep the conclusion last. Provide responsive full-size visuals and byte-preserved original output downloads. Update prompt-index returns and data-driven navigation/count checks, while preserving social metadata and footer cleanup.
- [x] Replace the downloadable PowerPoint with the matching exported 27-slide file; the automated check derives and verifies its count from slide data.
- [ ] Parent follow-up: publish and verify the final exported presentation/site version.

## School crest branding

- [x] Replace the Tech in Ed logo with the supplied school crest on all slides and website header/favicon/branding, retaining the Task Force name and Gemini Notebook wordmark. Remove the obsolete orange rounded slide-logo frame. Preserve the latest presenter-credit spacing and the eight new Studio example pages. Use school-only sharing artwork so the removed logo is not the website preview image.

## Presenter-credit typography

- [x] Make the website’s “Presented by Ken Kum” larger and responsive, with subtle emphasis on the name, while preserving its secondary hierarchy, muted colour and clear gap below it. Publish to the existing hkmakslo GitHub Pages site; do not alter the PowerPoint.

## Video overview examples

- [x] Add four slides after the slide-deck examples: default YouTube video, exact supplied custom prompt, custom output with the observed Mandarin-versus-Cantonese limitation, and the supplied HeyGen Cantonese workaround. Preserve all school branding and existing presenter typography. Use brief excerpts rather than whole videos to retain hands-on and Q&A time.
- [x] Match the website to the expanded deck, with responsive playable YouTube videos, external playback fallbacks, the supplied screenshots, updated sequential navigation, prompt-index links and the current PowerPoint download. Show that the language limitation is observed in this sample, not a universal product claim. Explain HeyGen as a separate service and avoid sending sensitive material without approval.

## Cantonese workflow introduction

- [x] Replace Slide 25’s introductory sentence with “To create a video in Cantonese:” and match website page 25 and its downloadable PowerPoint, retaining the existing workflow and video links.

## Studio retail comparison

- [x] Insert a screenshot-based comparison after Slide 3: school deployment shows eight Studio tools; the supplied retail screenshot shows the same eight plus Data table. Do not generalise this screenshot to all accounts. Preserve the Swiss Minimal design and school branding. Renumber subsequent slides, sync the website and prompt-index links, refresh the PowerPoint download and verify publication.

## Retail-interface caption

- [x] Change the Slide 4 screenshot caption to “The interface of the retail version.”, mirror it on page 4 and refresh the website PowerPoint download.

## Grounding, Studio spacing and access order

- [x] Add a qualified hallucination-reduction point to Slide 2; leave clear breathing space below Flashcards, Quizzes on Slide 3; move Use our school route after Why do versions feel different. Mirror content and ordering on the participant website, refresh the PowerPoint download, and verify the publication.

## Slide 2 clean four-point layout

- [x] Remove the remark beneath point 04 on Slide 2 and redistribute the four points with balanced line heights and spacing. Mirror the removal on website page 2 and refresh the downloadable PowerPoint.

## Participant action cues

- [x] Add a consistent orange “Try it Out!” badge with a computer icon and “On your computer” helper to Slides 8, 9, 11, 14 and 27 (school access, notebook creation, Explore, Studio comparison and Padlet posting). Keep existing slide titles, logos, content and ordering intact. Mirror the cue on the corresponding responsive website pages and refresh the PowerPoint download; do not label demonstration-only examples as hands-on steps.

## Blueprint table-format practice

- [x] Insert a Try it Out! activity immediately after Slide 13 (new Slide 14): use the selected English and Chinese Digital Education Blueprint PDFs to summarise the Four Key Focuses and Ten Strategies in a four-column table, with one row per strategy. Columns: Key focus; Strategy; Suggested teacher action; Citation. Show concise English followed by Traditional Chinese on the same slide, distinguish document facts from teacher suggestions, and preserve the established action badge, logos, fonts and layout. Mirror the copyable bilingual activity on the website, renumber subsequent slides/pages and navigation, retain the ten-prompt library, refresh the PowerPoint download and verify live publication.

## Simplified Ten Strategies exercise

- [x] Respect the user’s three-column revision to Slide 14: Strategy, Suggested teacher action, Citation. Remove Four Key Focuses and grouping from the activity title and prompts, use ten simple strategy rows, tidy bilingual typography with a clear bottom gap, and synchronize website page 14 and its PowerPoint download.

## Blueprint strategies prompt and sample output

- [x] Replace Slide 14’s English prompt with the exact user-provided wording, translate it into Traditional Chinese, and mirror both prompts on website page 14. Use Strategy, Suggested teacher action, Examples as the three columns, with 'not mentioned' / '未提及' for missing information. Insert one new sample-output slide immediately after Slide 14 using the supplied screenshot, add its matching responsive web page with an enlargeable image, renumber all subsequent slides and navigation, and publish the refreshed PowerPoint download.

## Caption, HeyGen home link and Padlet prompt description

- [x] Remove the photo caption from Slide 15 and matching website page, while retaining the enlargeable sample image. Add the visible, clickable HeyGen home URL https://www.heygen.com to Slide 28 and its website page, retaining the existing translation link. Replace Slide 29’s second point with “Briefly describe the prompt you used to customise this output.” in both formats. Preserve the 34-slide sequence and existing branding, refresh the PowerPoint download, and publish and verify the hkmakslo GitHub Pages site.

The 34-slide deck passed Slides validation and exported PowerPoint text/hyperlink checks. All 45 website pages passed content, navigation and download checks; live verification confirmed exact bytes for 73 pages/assets/downloads, including pages 15, 28, 29 and the refreshed PowerPoint. Published source commit: e99feff; Pages commit: 3e0d2ad.

## Page 27 neutral sample wording

- [x] Sync website Page 27’s introduction to Slide 27: “In this sample, the narration is still Mandarin.” Remove the separate quote “AI識寫文，仲使乜中文老師？” from the web page, preserve the existing video/screenshot and language limitation, and publish to the established hkmakslo GitHub Pages site. No PowerPoint change is requested.

All site checks passed. Live verification confirmed Page 27 and 73 pages/assets/downloads exactly match the published files. Source commit: 4379c9c; Pages commit: 0c7c78d.

## Explore before Studio hands-on

- [x] Move the former Slides 11 and 12, in that order, immediately before the hands-on Slide 16. The resulting sequence is 11 Chat format, 12 Blueprint prompt, 13 sample output, 14 Try Explore, 15 specific source searches, 16 hands-on. Add “Choose a Studio tool and customise its output for your teaching needs.” as a prominent instruction on Slide 16 and its matching website page. Preserve all 34 slides, prior revisions and branding; synchronize page order, navigation, footer numbers, route titles and the exported PowerPoint download, then publish and verify the website.

Slides validation, all 34 exported footer numbers, reordered slide content and website content/navigation checks passed. Slide 16 was visually checked for spacing. Live verification confirmed 73 pages/assets/downloads exactly match the approved files, including the refreshed PowerPoint. Source commit: dccafb7; Pages commit: 432c920.

## Save a response and reuse it as a source

- [x] Add one Try it Out! slide immediately after Slide 14, titled “Save a response. Reuse it as a source.” Use three concise instructions: “Under the chat response, click Save to note.”; “On the saved note, open ⋮.”; “Select Convert to source.” Include both supplied screenshots unchanged, with the interface labels 儲存至記事 and 轉換為來源資料. Do not reopen the attached images with a viewing tool. Preserve the established branding, update all subsequent numbers for 35 slides, mirror the new page and responsive screenshot links on the website, update global navigation and prompt-index returns, refresh the downloadable PowerPoint, then publish and verify the live site.

## Prompt overview immediately after Padlet

- [x] Move the ten-prompts overview (Slide 34 after the new activity insertion) immediately after Slide 30, Post your Studio output on Padlet. It becomes Slide 31; the three worked-example pages become 32–34 and Q&A remains 35. Mirror this ordering, all global navigation and the prompt-page return links on the website and refresh the matching PowerPoint download.

## Advanced Level workshop title

- [x] Rename the current workshop to “Gemini Notebook Workshop (Advanced Level)”. Replace the old level wording across the editable deck title/cover, website cover and page footers, browser/social titles, current workshop plan, activity brief and downloadable prompt materials. Preserve functioning link destinations, including the existing Padlet slug, and stable resource IDs; retain historical QA/baseline snapshots unchanged. Export a clearly named Advanced Level PowerPoint and publish the final website/downloads after completing the new activity and prompt-overview reorder.

The final Advanced Level deck passed Slides validation, all 35 exported footer-number and sequence checks, and exact three-step instruction checks. Both screenshots were copied unchanged and were not reopened with an image-viewing tool. All 46 website pages passed content, links, navigation, title and download checks. Live verification confirmed exact bytes for 76 pages/assets/downloads, including the new screenshot files and Advanced PowerPoint. Source commit: de18f42; Pages commit: 52041ed. Five current workshop Markdown documents were synchronized and verified in the Advanced Materials ZIP.

## Slide 15 screenshot replacement and aligned layout

- [x] Replace Slide 15’s Save to note screenshot with pasted_file_VwTj3g_image.png, preserve the existing Convert to source screenshot, and arrange both more aesthetically. Use a coherent right-hand screenshot column with shared outer and image edges, proportional image sizing, matching white frames and border treatment, and consistent spacing. Keep the three concise instructions, branding, Advanced Level title and all 35 slides unchanged. Synchronize the new asset and responsive image presentation on the website, refresh the PowerPoint download, publish and verify the live page and files.

Slide 15 was validated, exported and visually checked as a complete slide. The two screenshots share a 492px display width and common left edge inside matching 540px white frames, separated by 16px. The replacement asset is byte-identical to the supplied image. Website checks passed, and live verification confirmed 77 exact pages/assets/downloads, including the replacement image and refreshed Advanced Level PPTX. Source commit: e90b954; Pages commit: a67f800.

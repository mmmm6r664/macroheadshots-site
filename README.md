# Macro Headshots website

Redesign of macroheadshots.com in a clean, modern style (floating pill navigation, soft gradient hero,
stacked gradient service cards, purple accents, black footer). All 19 pages: Home, Pricing,
Appointments and 16 "Headshots in …" local pages, with the original copy, photos and SEO titles.

- The appointment form is the live HighLevel form embed, so submissions still reach the CRM.
- Google reviews (Elfsight) and the Instagram feed are kept.
- Static site, no build step. Deploys on Vercel.

## Regenerating

`tools/redesign/generate.py` builds the pages from content captured from the original site:

    python3 tools/redesign/generate.py capture/content.json <original-assets-dir> tools/brand out/

Styles live in `tools/redesign/styles.css` (copied to `css/styles.css`).

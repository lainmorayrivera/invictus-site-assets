# Invictus site assets

Shared CSS and JavaScript for **invictus-global.net** (Webflow), served through the jsDelivr CDN. These files are too large for Webflow's custom-code fields.

| File | What it is | Size |
|---|---|---|
| `dist/figures.min.css` | The four SFOM diagram modules (wheel, phases, diagnostic, force multiplier) | ~30 KB |
| `dist/site.min.js` | Site behaviour: mobile menu, media headers, scroll reveals, rotators, carousels, sub-nav highlight, phone navbar hide/show | ~14 KB |

This repository contains only styling and behaviour code. Page content, diagram wording and book material live in Webflow, not here.

## Use in Webflow
In **Site settings → Custom code**, pin a release tag:

Head code:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lainmorayrivera/invictus-site-assets@v1.0.0/dist/figures.min.css">
```

Footer code (before `</body>`):
```html
<script src="https://cdn.jsdelivr.net/gh/lainmorayrivera/invictus-site-assets@v1.0.0/dist/site.min.js" defer></script>
```

## Releasing a change
1. In the prototype, edit `prototype/modules/fig-*.css`, `fig-shared.css` or `prototype/script.js`.
2. From the project root, run `python site-assets/build.py`. It rebuilds the combined CSS and minifies both files into `site-assets/dist/`.
3. Commit, then tag the next version: `git tag v1.0.1 && git push && git push --tags`.
4. In Webflow, change `@v1.0.0` to `@v1.0.1` in both lines and publish.

Rollback means changing the tag back. Each tag is a fixed snapshot that jsDelivr caches permanently, so visitors never see a half-updated mix.

Never point Webflow at `@main` or `@latest`: those can change without warning and are cached unpredictably.

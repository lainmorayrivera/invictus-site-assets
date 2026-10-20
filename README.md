# Invictus site assets

Shared CSS and JavaScript for **invictus-global.net** (Webflow), served through the jsDelivr CDN. These files are too large for Webflow's custom-code fields.

| File | What it is | Size |
|---|---|---|
| `dist/figures.min.css` | The four SFOM diagram modules (wheel, phases, diagnostic, force multiplier) | ~30 KB |
| `dist/site.min.css` | Rules Webflow's Designer can't author: menu scroll lock, `text-link` arrow, header logo shrink on scroll, media-header fades/video/toggle icons/scroll drift. Source: `src/site.css` | ~2 KB |
| `dist/site.min.js` | Site behaviour: mobile menu, media headers, scroll reveals, rotators, carousels, sub-nav highlight, phone navbar hide/show, Space key on `role="button"` links | ~14 KB |

This repository contains only styling and behaviour code. Page content, diagram wording and book material live in Webflow, not here.

## Use in Webflow
In **Site settings → Custom code**, pin a release tag:

Head code:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lainmorayrivera/invictus-site-assets@v1.0.3/dist/figures.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lainmorayrivera/invictus-site-assets@v1.0.3/dist/site.min.css">
```

Footer code (before `</body>`):
```html
<script src="https://cdn.jsdelivr.net/gh/lainmorayrivera/invictus-site-assets@v1.0.3/dist/site.min.js" defer></script>
```

## Releasing a change
1. Edit `prototype/modules/fig-*.css`, `fig-shared.css`, `prototype/script.js` or `src/site.css`.
2. From the project root, run `python site-assets/build.py`. It rebuilds the combined CSS and minifies both files into `site-assets/dist/`.
3. Commit, then tag the next version: `git tag v1.0.4 && git push && git push --tags`.
4. In Webflow, change the version in every line (e.g. `@v1.0.3` to `@v1.0.4`) and publish.

Rollback means changing the tag back. Each tag is a fixed snapshot that jsDelivr caches permanently, so visitors never see a half-updated mix.

Never point Webflow at `@main` or `@latest`: those can change without warning and are cached unpredictably.

## Changelog
- **v1.0.3:** `site.min.js`: the media header can no longer stay hidden. The first poster is forced to eager (Webflow marks images lazy), and `is-loaded` is added after 2.5 s regardless of image load events.
- **v1.0.2:** `site.min.css` adds the media header rules: poster/video cover, fade-in on `is-loaded`/`is-playing` (only under `.js-motion`, so the header stays visible without JS), staggered content reveal, pause/play icon swap on `aria-pressed`, and the scroll-linked drift.
- **v1.0.1:** added `site.min.css` (menu scroll lock, `text-link` arrow, logo shrink on scroll). `site.min.js`: Space activates `<a role="button">` links (Webflow renders `<button>` as `<a href="#">`), and those links no longer follow `#`.
- **v1.0.0:** first release. Diagram CSS and site behaviour JS.

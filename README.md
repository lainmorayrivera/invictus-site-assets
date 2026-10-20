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
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lainmorayrivera/invictus-site-assets@v1.0.7/dist/figures.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lainmorayrivera/invictus-site-assets@v1.0.7/dist/site.min.css">
```

Footer code (before `</body>`):
```html
<script src="https://cdn.jsdelivr.net/gh/lainmorayrivera/invictus-site-assets@v1.0.7/dist/site.min.js" defer></script>
```

## Releasing a change
1. Edit `prototype/modules/fig-*.css`, `fig-shared.css`, `prototype/script.js` or `src/site.css`.
2. From the project root, run `python site-assets/build.py`. It rebuilds the combined CSS and minifies both files into `site-assets/dist/`.
3. Commit, then tag the next version: `git tag v1.0.8 && git push && git push --tags`.
4. In Webflow, change the version in every line (e.g. `@v1.0.7` to `@v1.0.8`) and publish.

Rollback means changing the tag back. Each tag is a fixed snapshot that jsDelivr caches permanently, so visitors never see a half-updated mix.

Never point Webflow at `@main` or `@latest`: those can change without warning and are cached unpredictably.

## Changelog
- **v1.0.17:** `site.min.css`: visible two-tone keyboard focus ring (gold on a navy halo) for buttons, nav and footer links, insight cards and text links that had none.
- **v1.0.16:** `site.min.js`: clear Webflow's "Example Text" placeholders case-insensitively (inputs and textareas); external `rel="noopener"` links open in a new tab (the Webflow API drops `target`).
- **v1.0.15:** `site.min.js`: Contact form on Webflow (Topic options from `data-options`, `?topic=` pre-select and topic cards; Webflow handles the submit), clears Webflow's default "Example text" placeholders. `site.min.css`: Education (card hovers, figure margins), Contact (hero compass, topic states, textarea/select, next-step links), Privacy/Terms typography and compasses, text-side compass on the About bio, academic intro and contact intro.
- **v1.0.14:** `site.min.js`: CMS-fed rotators (`data-rotator-cms`): flatten the Advisors tab and panel lists into the rotator, order by the bound Sort order (blank last), set ids/ARIA, split Roles into tags. `site.min.css`: Advisory Board tab photos, active ring, quote marks, empty-field hiding, alternating panel sides on desktop.
- **v1.0.13:** `site.min.css`: insight title cards read "Article · Substack" (Type from a `data-kind` attribute ahead of the bound Source).
- **v1.0.12:** `site.min.js`: Media & Insights archive on CMS markup (merge the Insights and Press lists with the Book card, newest first; type filter with aria-pressed and a live count; Show more by 12). `site.min.css`: archive grid without wrappers, filter pressed/focus states, featured card hover.
- **v1.0.11:** `site.min.css`: Book page: flip book in the carousel header (placement by breakpoint, mirrored angle, navy halo, phone badge), compass on Parts I/III/V only, no margin on figure embeds.
- **v1.0.10:** `site.min.css`: Solutions page: carousel page header (slide crossfade and drift, 4:3 phone frame), sticky sub-nav (gold hairline, current pill, phone edge fade), inline video fill, text-side compass on light solution sections.
- **v1.0.9:** `site.min.css`: press release template (CMS): the Brand field switches the logo and boilerplate; an empty lead image or PDF hides its frame or button; dateline spacing.
- **v1.0.8:** `site.min.js`: carousels fed by a Webflow CMS list get their per-slide state on load (first slide active, others hidden and inert, every second slide reversed, "n of N" labels), and the dots are rebuilt to match the number of slides.
- **v1.0.7:** `site.min.css`: insight card hover (gold title underline, slight image zoom, deeper shadow) and focus ring.
- **v1.0.6:** `site.min.css`: scroll reveals (`[data-reveal]` fade-up, photo settle) and the thesis band's reveal; carousel dot focus ring. `site.min.js`: decorative images (`alt=""`, e.g. watermarks; Webflow drops `aria-hidden` on images) are no longer revealed to full opacity.
- **v1.0.5:** `site.min.css`: 3D flip book (custom-property sizing, container units, sheens, spine, pages) and rotator state rules (progress line, active icon, phone tab strip). `site.min.js`: the `#`/Space handling also covers `role="tab"` links; the rotator's pause label is derived from its own text.
- **v1.0.4:** `site.min.js`: the scroll behaviour (`is-scrolled` shadow and logo shrink, phone navbar hide/show) targets `.navbar_component`; Webflow's navbar has no `.is-dark`, so it never ran there.
- **v1.0.3:** `site.min.js`: the media header can no longer stay hidden. The first poster is forced to eager (Webflow marks images lazy), and `is-loaded` is added after 2.5 s regardless of image load events.
- **v1.0.2:** `site.min.css` adds the media header rules: poster/video cover, fade-in on `is-loaded`/`is-playing` (only under `.js-motion`, so the header stays visible without JS), staggered content reveal, pause/play icon swap on `aria-pressed`, and the scroll-linked drift.
- **v1.0.1:** added `site.min.css` (menu scroll lock, `text-link` arrow, logo shrink on scroll). `site.min.js`: Space activates `<a role="button">` links (Webflow renders `<button>` as `<a href="#">`), and those links no longer follow `#`.
- **v1.0.0:** first release. Diagram CSS and site behaviour JS.

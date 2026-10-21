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
- **v1.0.43:** Home figures band: pause button moved to the top-right, centred on the row of labels.
- **v1.0.42:** newsletter panel: Subscribe button and benefits row share one width (button full width, ticks spread edge to edge), block centred against the copy.
- **v1.0.41:** alliance panel: split treatment (B) is live (NEXUS path on a BizNuvo mint card); reviewer switcher and the unused A/C treatments removed.
- **v1.0.40:** featured alliance panel (Solutions): modernized NEXUS path (connecting line that draws and lights each step on scroll-in, hover lift, gold top bar, compass watermark) plus three BizNuvo brand treatments for review via ?alliance=a|b|c (teal accent, split mint card, co-branded gradient with wave) and a reviewer switcher.
- **v1.0.39:** rotating stats (Home figures band ripples through two figures per slot; Solutions stat box rebuilt in the band's style with label, compass, hairlines, progress line and pause); SFOM spider chart builds on scroll-in (rings, spokes, current then target shape, numbers, list) and links list rows to chart spokes/points/numbers both ways; Substack buttons in Substack orange with the bookmark mark and one label; newsletter panel watermark, benefits row and latest article.
- **v1.0.38:** podcast band restyled to match the site's navy bands (flat navy, compass watermark, gold bar and play circle on the photo, hairline platforms note) plus a row of the three latest episodes copied from the Insights CMS video cards.
- **v1.0.37:** framed graphics: article images that aren't photos (diagrams, charts, covers) show whole inside the navy title-card frame instead of being cropped; Substack photos listed in `PHOTOS` keep the full-bleed crop.
- **v1.0.36:** Contact hero text measured against the window less its scrollbar (`--sbw`), so it lines up with the page column.
- **v1.0.35:** polish follow-up: Contact hero text on the page column (scrollbar-safe), Education highlights Solutions in the menu with its own class (Webflow resets w--current).
- **v1.0.34:** polish pass (docs/polish-review-2026-10-20.md, all 37 items): advisor avatars, Book phone hero, one scroll offset, card meta rows, legal reading column, balanced headings, one focus style, header spacing and headline scale, thesis band, sequential carousel fades, rotators resume in step and pause on phones/off screen, Advisory Board phone panels, Contact select/checkbox/headings, footer grid, Solutions mirror grid, tap targets, curly apostrophes, responsive header slides, book cover ratio and Tap hint, weight 600, brand deep navy, Education nav highlight.
- **v1.0.33:** `site.min.css`: motion polish follow-up: cards that also fade in on scroll (Education, Contact topics, Solutions help items, Insights cards) keep the reveal timing and add smooth hover shadow/border; rotator play/pause circles use the house timing instead of Webflow's 0.2s.
- **v1.0.32:** `site.min.css`: motion polish. A site-wide audit found ~25 hover effects that snapped or ran in 0.2s (nav, footer and text links, sub-nav, rotator tabs, play buttons, carousel dots, form fields, Insights/Education/Contact/Solutions cards). All now share one timing: 0.3s ease for colour and underlines, ~0.45s ease-out for lifts and shadows; underlines fade in (transparent until hover); carousel dots animate via a registered colour property.
- **v1.0.31:** `site.min.css`: one smooth hover for every button (0.35s ease): filled buttons deepen in their own colour, outline buttons take a faint tint, all lift 2px with a soft shadow and press down on click; YouTube button eases instead of snapping. Social, filter and carousel-arrow buttons share the timing.
- **v1.0.30:** `figures.min.css`: a consistent "pop" across all four book figures. On scroll-in the centre (wheel hub, AI engine) appears first, then the cards pop in one by one with a slight overshoot (CSS animations with backwards fill, so hover still works); on hover (pointer devices) wheel cards, phase cards, force pillars and diagnostic key items lift and scale slightly with a soft shadow. No motion for reduced-motion users.
- **v1.0.29:** `site.min.css`: footer credit links (photographer, website developer) styled as quiet text links with a gold underline; spacing between adjacent links.
- **v1.0.28:** `site.min.css`: header slideshows vary their motion (zoom out, pan right, gentle zoom in, pan left, repeating) instead of every slide zooming out the same way. Reduced-motion users still get no motion.
- **v1.0.27:** photo refinement. Cards: lighter, bluer duotone so the photo reads (closer to the Bucknell reference). Bands: photo softened (1.5px blur) and darkened only behind the text, watermark lighter. Solutions, About and Insights bands swapped to photos without signage (towers under cloud, Lower Manhattan across the water, glass tower); sign photos removed from the rotation pool.
- **v1.0.26:** `site.min.css`: play/pause circles centre their icon (Webflow's 15px button padding pushed it 2.8px right); CTA band photo wash uses the brand navy (#0F2A4A) so bands match the footer.
- **v1.0.25:** `site.min.js` + `site.min.css`: navy photo backgrounds (Bucknell-style). Article title cards with no image of their own get a matched greyscale FiDi / Wall Street photo under a navy wash (new articles rotate through the pool by a hash of their link); the closing CTA band on each page gets its own photo and the compass watermark. Logo, label and watermark stay on top. Photos: Unsplash License, in Webflow Assets (`stock-*`).
- **v1.0.24:** `site.min.js`: the full-width `sizes` fix applies only to the header photo/slides (`.header-media_media`), not the 3D book cover beside them on the Book page.
- **v1.0.23:** `site.min.js`: sharp images. Header-media slides get `sizes="100vw"` (Webflow had written "360px" or "1152px" from the Designer, so the Book and Media & Insights heroes loaded 500-1152px files stretched to full width), and any image rendering wider than its fixed-pixel `sizes` hint gets its real width so the browser picks a large enough file.
- **v1.0.22:** `site.min.css` + `site.min.js`: scrolling from the prototype (section 41) that never reached Webflow: smooth in-page jumps offset below the navbar, the gold reading-progress line on every page but Home, and the phone navbar sliding away on scroll down. "Watch on YouTube" buttons are YouTube red (#CC0000, AA contrast) with the play logo.
- **v1.0.21:** `site.min.js` + `site.min.css`: Insight cards show their CMS Tags (New / Popular / Most discussed pills), Topics and "N min read", expanded from `[data-meta]` spans in the card meta row, as in the prototype.
- **v1.0.20:** `site.min.js`: header and inline videos set `muted` + `loop` before playing (Webflow strips the attributes, so the hero froze after one pass and iOS would not autoplay); a "Skip to content" link is inserted on every page (styles in `site.min.css`); Insights filter clicks update `?filter=` in the address bar.
- **v1.0.19:** `site.min.js` + `site.min.css`: Media & Insights archive shows a friendly note (with a Substack link) when a filter has no items yet, e.g. Press before the first release.
- **v1.0.18:** `site.min.css`: define the design tokens the book figures use (colours, fonts, spacing, gold bars) on the figure roots; on Webflow the figure icons, rules and gold bars had no colour.
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

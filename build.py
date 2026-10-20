"""Build the CDN files from the prototype sources. Run from the project root:
    python site-assets/build.py
Concatenates the diagram module CSS (fig-shared.css last), then minifies it, src/site.css and
script.js with esbuild (via npx)."""
import pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MOD = ROOT / "prototype" / "modules"
DIST = ROOT / "site-assets" / "dist"
DIST.mkdir(parents=True, exist_ok=True)

parts = []
for n in ["fig-wheel", "fig-phases", "fig-diagnostic", "fig-force", "fig-shared"]:
    parts.append(f"/* ===== {n} ===== */\n" + (MOD / f"{n}.css").read_text(encoding="utf-8"))
combined = MOD / "figures.css"
combined.write_text("/* Diagram modules, combined (fig-shared.css last). Built by site-assets/build.py. */\n\n" + "\n\n".join(parts), encoding="utf-8")

def minify(src, out):
    cmd = ["npx", "--yes", "esbuild", str(src), "--minify", f"--outfile={out}", "--log-level=warning"]
    subprocess.run(cmd, check=True, shell=sys.platform == "win32")

minify(combined, DIST / "figures.min.css")
minify(ROOT / "site-assets" / "src" / "site.css", DIST / "site.min.css")
minify(ROOT / "prototype" / "script.js", DIST / "site.min.js")
for f in sorted(DIST.iterdir()):
    print(f"{f.name}: {f.stat().st_size / 1024:.1f} KB")

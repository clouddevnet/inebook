import html
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "python_network_automation_crash_course_book.md"
OUT = ROOT / "book_site"


@dataclass
class Page:
    title: str
    filename: str
    markdown: str
    nav_title: str
    group: str = "Chapters"


def slugify(text):
    text = text.lower()
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "section"


def split_h1_sections(text):
    sections = []
    current_title = None
    current = []
    in_code = False

    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("# "):
            if current_title is not None:
                sections.append((current_title, "\n".join(current).strip()))
            current_title = line[2:].strip()
            current = [line]
        else:
            current.append(line)

    if current_title is not None:
        sections.append((current_title, "\n".join(current).strip()))
    return sections


def split_lab_tracks(section_markdown):
    intro = []
    tracks = []
    current_title = None
    current = []
    in_code = False

    for line in section_markdown.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("## Lab Track "):
            if current_title is not None:
                tracks.append((current_title, "\n".join(current).strip()))
            else:
                intro = current[:]
            current_title = line[3:].strip()
            current = [line]
        else:
            current.append(line)

    if current_title is not None:
        tracks.append((current_title, "\n".join(current).strip()))
    elif current:
        intro = current

    return "\n".join(intro).strip(), tracks


def build_pages(text):
    pages = []
    sections = split_h1_sections(text)

    chapter_count = 0
    for title, body in sections:
        if title == "Python Network Automation Crash Course":
            pages.append(Page(title, "index.html", body, "Home", "Start"))
            continue

        if title == "Introduction: The Evolution You Cannot Ignore":
            pages.append(Page(title, "introduction.html", body, "Introduction", "Start"))
            continue

        if title == "Part II: Applying Python to Network Automation":
            pages.append(Page(title, "part-ii-network-automation.html", body, "Part II", "Chapters"))
            continue

        if title == "Part III: Twin-Bridges Mastery Lab Workbook":
            intro, tracks = split_lab_tracks(body)
            pages.append(Page(title, "part-iii-labs.html", intro, "Part III Labs", "Labs"))
            for index, (track_title, track_body) in enumerate(tracks, start=1):
                pages.append(
                    Page(
                        track_title,
                        f"lab-track-{index:02d}.html",
                        f"# {track_title}\n\n{track_body}",
                        f"Lab Track {index}",
                        "Labs",
                    )
                )
            continue

        if title == "References":
            pages.append(Page(title, "references.html", body, "References", "Back Matter"))
            continue

        chapter_count += 1
        prefix = f"ch{chapter_count:02d}"
        pages.append(Page(title, f"{prefix}-{slugify(title)[:54]}.html", body, f"Ch {chapter_count}", "Chapters"))

    return pages


def preprocess_markdown(md_text):
    # Mermaid-style text arrows and network diagrams should remain plain code.
    return md_text


def markdown_to_html(md_text):
    return markdown.markdown(
        preprocess_markdown(md_text),
        extensions=["fenced_code", "codehilite", "tables", "toc", "sane_lists"],
        extension_configs={
            "codehilite": {
                "css_class": "highlight",
                "guess_lang": False,
                "linenums": False,
                "noclasses": False,
                "use_pygments": True,
            }
        },
        output_format="html5",
    )


def extract_headings(rendered_html):
    pattern = re.compile(r"<h([23]) id=\"([^\"]+)\">(.+?)</h[23]>", re.S)
    headings = []
    for level, ident, raw in pattern.findall(rendered_html):
        label = re.sub(r"<.*?>", "", raw)
        headings.append((int(level), ident, html.unescape(label)))
    return headings


def grouped_nav(pages, current):
    groups = []
    for page in pages:
        if not groups or groups[-1][0] != page.group:
            groups.append((page.group, []))
        groups[-1][1].append(page)

    chunks = []
    for group, items in groups:
        chunks.append(f'<div class="toc-label">{html.escape(group)}</div>')
        chunks.append("<ol class=\"chapter-list\">")
        for page in items:
            active = " active" if page.filename == current.filename else ""
            chunks.append(
                f'<li><a class="{active.strip()}" href="{page.filename}">'
                f'<span>{html.escape(page.nav_title)}</span>'
                f'<small>{html.escape(page.title)}</small>'
                "</a></li>"
            )
        chunks.append("</ol>")
    return "\n".join(chunks)


def local_toc(headings):
    if not headings:
        return '<p class="muted">No sections on this page.</p>'
    rows = ['<div class="toc-label">On This Page</div>', '<ol class="page-toc">']
    for level, ident, label in headings:
        cls = "sub" if level == 3 else ""
        rows.append(f'<li class="{cls}"><a href="#{ident}">{html.escape(label)}</a></li>')
    rows.append("</ol>")
    return "\n".join(rows)


def previous_next(pages, index):
    prev_page = pages[index - 1] if index > 0 else None
    next_page = pages[index + 1] if index + 1 < len(pages) else None
    left = (
        f'<a class="nav-btn prev" href="{prev_page.filename}">← {html.escape(prev_page.nav_title)}</a>'
        if prev_page
        else '<span></span>'
    )
    right = (
        f'<a class="nav-btn next" href="{next_page.filename}">{html.escape(next_page.nav_title)} →</a>'
        if next_page
        else '<span></span>'
    )
    return f'<div class="chapter-nav-footer">{left}{right}</div>'


CSS = r"""
*, *::before, *::after { box-sizing: border-box; }
:root {
  --bg: #f8fafc;
  --bg-card: #ffffff;
  --bg-code: #11120d;
  --code-border: #34352d;
  --code-text: #f8f8f2;
  --bg-note: #eff6ff;
  --text: #334155;
  --text-heading: #0f172a;
  --text-muted: #64748b;
  --text-light: #94a3b8;
  --accent: #0069ff;
  --accent-2: #0284c7;
  --border: #e2e8f0;
  --nav-hover: #f1f5f9;
  --shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
  --sidebar-width: 280px;
  --content-max: 900px;
  --font-body: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: "Fira Code", "Cascadia Code", Consolas, monospace;
}
[data-theme="dark"] {
  --bg: #0b1120;
  --bg-card: #111827;
  --bg-code: #11120d;
  --code-border: #34352d;
  --code-text: #f8f8f2;
  --bg-note: #0c223a;
  --text: #cbd5e1;
  --text-heading: #f8fafc;
  --text-muted: #94a3b8;
  --text-light: #64748b;
  --accent: #60a5fa;
  --accent-2: #38bdf8;
  --border: #243244;
  --nav-hover: #172033;
  --shadow: none;
}
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: var(--font-body);
  background: var(--bg);
  color: var(--text);
  line-height: 1.72;
  font-size: 16px;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.site-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  height: 58px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 0 1.5rem;
  background: color-mix(in srgb, var(--bg-card) 94%, transparent);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(14px);
}
.nav-logo {
  font-weight: 800;
  color: var(--text-heading);
  display: flex;
  align-items: center;
  gap: .55rem;
}
.logo-badge {
  background: var(--accent);
  color: white;
  font-size: .68rem;
  border-radius: 4px;
  padding: .1rem .45rem;
  letter-spacing: .06em;
}
.nav-actions { display: flex; align-items: center; gap: .75rem; }
.nav-actions a { color: var(--text-muted); font-size: .9rem; font-weight: 600; }
.theme-toggle {
  border: 1px solid var(--border);
  background: var(--bg-card);
  color: var(--text-heading);
  border-radius: 999px;
  padding: .42rem .7rem;
  font-weight: 700;
  cursor: pointer;
}
.page-layout {
  max-width: 1460px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: var(--sidebar-width) minmax(0, 1fr) var(--sidebar-width);
  gap: 1.25rem;
  padding: 0 1rem;
}
.sidebar-left, .sidebar-right {
  position: sticky;
  top: 58px;
  height: calc(100vh - 58px);
  overflow: auto;
  padding: 1.5rem .5rem;
}
.toc-label {
  margin: 1rem .55rem .5rem;
  color: var(--text-light);
  font-size: .72rem;
  text-transform: uppercase;
  letter-spacing: .08em;
  font-weight: 800;
}
.chapter-list, .page-toc { list-style: none; margin: 0; padding: 0; }
.chapter-list li, .page-toc li { margin: .18rem 0; }
.chapter-list a {
  display: block;
  padding: .55rem .65rem;
  border-radius: 8px;
  color: var(--text-muted);
}
.chapter-list a span {
  display: block;
  font-size: .74rem;
  text-transform: uppercase;
  letter-spacing: .06em;
  font-weight: 800;
  color: var(--accent-2);
}
.chapter-list a small {
  display: block;
  color: inherit;
  font-size: .82rem;
  line-height: 1.35;
}
.chapter-list a.active, .chapter-list a:hover, .page-toc a:hover {
  background: var(--nav-hover);
  text-decoration: none;
  color: var(--text-heading);
}
.page-toc a {
  display: block;
  padding: .38rem .65rem;
  border-left: 2px solid transparent;
  color: var(--text-muted);
  font-size: .86rem;
}
.page-toc li.sub a { padding-left: 1.35rem; font-size: .8rem; }
.main-content {
  min-width: 0;
  max-width: var(--content-max);
  width: 100%;
  margin: 0 auto;
  padding: 3rem 1rem 5rem;
}
.article-shell {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 14px;
  box-shadow: var(--shadow);
  padding: clamp(1.35rem, 4vw, 3rem);
}
.article-meta {
  color: var(--text-muted);
  font-size: .84rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .06em;
  margin-bottom: .8rem;
}
h1, h2, h3, h4 { color: var(--text-heading); line-height: 1.18; }
h1 { font-size: clamp(2rem, 5vw, 3.6rem); letter-spacing: -0.02em; margin: 0 0 1rem; }
h2 { font-size: clamp(1.45rem, 3vw, 2rem); margin: 2.5rem 0 .8rem; border-top: 1px solid var(--border); padding-top: 1.6rem; }
h3 { font-size: 1.22rem; margin: 1.8rem 0 .55rem; }
h4 { font-size: 1.05rem; margin: 1.4rem 0 .4rem; }
p, ul, ol, blockquote, table, pre { margin-top: 0; margin-bottom: 1.05rem; }
ul, ol { padding-left: 1.45rem; }
li + li { margin-top: .28rem; }
blockquote {
  border-left: 4px solid var(--accent);
  background: var(--bg-note);
  padding: .9rem 1rem;
  border-radius: 0 8px 8px 0;
  color: var(--text);
}
code {
  font-family: var(--font-mono);
  background: var(--nav-hover);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: .08rem .28rem;
  font-size: .9em;
}
.highlight,
pre {
  overflow: auto;
  background: var(--bg-code);
  color: var(--code-text);
  border-radius: 10px;
  border: 1px solid var(--code-border);
}
.highlight {
  margin: 0 0 1.05rem;
}
.highlight pre,
pre {
  padding: 1rem;
}
.highlight pre {
  margin: 0;
  border: 0;
}
.highlight code,
pre code {
  background: transparent;
  border: 0;
  padding: 0;
  color: inherit;
  font-size: .86rem;
  line-height: 1.55;
}
.highlight .hll { background-color: #49483e; }
.highlight .c, .highlight .ch, .highlight .cm, .highlight .cpf, .highlight .c1, .highlight .cs { color: #75715e; font-style: italic; }
.highlight .k, .highlight .kc, .highlight .kd, .highlight .kn, .highlight .kp, .highlight .kr, .highlight .kt { color: #f92672; }
.highlight .o, .highlight .ow { color: #f92672; }
.highlight .m, .highlight .mb, .highlight .mf, .highlight .mh, .highlight .mi, .highlight .mo, .highlight .il { color: #ae81ff; }
.highlight .s, .highlight .sa, .highlight .sb, .highlight .sc, .highlight .dl, .highlight .sd, .highlight .s2, .highlight .se, .highlight .sh, .highlight .si, .highlight .sx, .highlight .sr, .highlight .s1, .highlight .ss { color: #e6db74; }
.highlight .na, .highlight .nc, .highlight .nd, .highlight .ne, .highlight .nf, .highlight .fm { color: #a6e22e; }
.highlight .nb, .highlight .bp, .highlight .vc, .highlight .vg, .highlight .vi, .highlight .vm { color: #66d9ef; font-style: italic; }
.highlight .n, .highlight .p { color: #f8f8f2; }
.highlight .nt { color: #f92672; }
.highlight .nv { color: #66d9ef; }
.highlight .w { color: #f8f8f2; }
.highlight .gd { color: #f92672; }
.highlight .gi { color: #a6e22e; }
.highlight .ge { font-style: italic; }
.highlight .gs { font-weight: 700; }
.highlight .err { color: #ff5555; }
table {
  width: 100%;
  border-collapse: collapse;
  overflow: hidden;
  border: 1px solid var(--border);
  border-radius: 8px;
  display: block;
  max-width: 100%;
  overflow-x: auto;
}
th, td { border: 1px solid var(--border); padding: .65rem .75rem; text-align: left; }
th { color: var(--text-heading); background: var(--nav-hover); }
.chapter-nav-footer {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  margin-top: 2.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
}
.nav-btn {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: .65rem .85rem;
  background: var(--bg-card);
  font-weight: 700;
}
.muted { color: var(--text-muted); }
@media (max-width: 1180px) {
  .page-layout { grid-template-columns: 240px minmax(0, 1fr); }
  .sidebar-right { display: none; }
}
@media (max-width: 760px) {
  .site-nav { padding: 0 .8rem; }
  .nav-actions a { display: none; }
  .page-layout { display: block; padding: 0; }
  .sidebar-left { position: static; height: auto; max-height: 42vh; border-bottom: 1px solid var(--border); padding: .75rem; background: var(--bg-card); }
  .main-content { padding: 1rem .75rem 3rem; }
  .article-shell { border-radius: 0; border-left: 0; border-right: 0; }
}
"""


JS = r"""
(function () {
  const root = document.documentElement;
  const saved = localStorage.getItem("book-theme");
  if (saved) root.setAttribute("data-theme", saved);
  const btn = document.querySelector("[data-theme-toggle]");
  function label() {
    const dark = root.getAttribute("data-theme") === "dark";
    if (btn) btn.textContent = dark ? "Light" : "Dark";
  }
  label();
  if (btn) {
    btn.addEventListener("click", function () {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      localStorage.setItem("book-theme", next);
      label();
    });
  }
})();
"""


def render_page(page, pages, index):
    html_body = markdown_to_html(page.markdown)
    headings = extract_headings(html_body)
    title = html.escape(page.title)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | Python Network Automation Crash Course</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/book.css">
</head>
<body>
  <nav class="site-nav">
    <a class="nav-logo" href="index.html">Python Network Automation <span class="logo-badge">Book</span></a>
    <div class="nav-actions">
      <a href="part-iii-labs.html">Labs</a>
      <a href="references.html">References</a>
      <button class="theme-toggle" data-theme-toggle type="button">Dark</button>
    </div>
  </nav>
  <div class="page-layout">
    <aside class="sidebar-left">
      {grouped_nav(pages, page)}
    </aside>
    <main class="main-content">
      <article class="article-shell">
        <div class="article-meta">{html.escape(page.group)} · {html.escape(page.nav_title)}</div>
        {html_body}
        {previous_next(pages, index)}
      </article>
    </main>
    <aside class="sidebar-right">
      {local_toc(headings)}
    </aside>
  </div>
  <script src="assets/book.js"></script>
</body>
</html>
"""


def main():
    if not SOURCE.exists():
        raise SystemExit(f"Missing source manuscript: {SOURCE}")

    text = SOURCE.read_text(encoding="utf-8")
    pages = build_pages(text)

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    (OUT / "assets" / "book.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (OUT / "assets" / "book.js").write_text(JS.strip() + "\n", encoding="utf-8")

    for index, page in enumerate(pages):
        (OUT / page.filename).write_text(render_page(page, pages, index), encoding="utf-8")

    print(f"Wrote {len(pages)} pages to {OUT}")
    print(OUT / "index.html")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Baut aus src/pages/*.md eine einzige, vollständig eigenständige HTML-Datei.

- Formeln ($…$ / $$…$$) werden mit MathJax vorgerendert (SVG, kein JavaScript nötig)
- Bilder werden als data:-URI eingebettet
- Ohne JavaScript: alle Seiten stehen untereinander, Navigation über Sprungmarken
- Mit JavaScript: Seitenumschaltung, gemerkte Checklisten (localStorage), Fortschritt
"""
import base64, json, mimetypes, os, re, subprocess, sys, html, datetime
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'src')
OUT = os.path.join(HERE, '..', 'build', 'Nuklearmedizin.html')

# ---------- Formeln --------------------------------------------------------
_math_items = []          # (tex, display)
_math_cache = {}

def _extract_math(text):
    """Ersetzt $$…$$ und $…$ durch Platzhalter."""
    def repl_display(m):
        _math_items.append((m.group(1).strip(), True)); return f'\x00MATH{len(_math_items)-1}\x00'
    def repl_inline(m):
        _math_items.append((m.group(1).strip(), False)); return f'\x00MATH{len(_math_items)-1}\x00'
    text = re.sub(r'\$\$(.+?)\$\$', repl_display, text, flags=re.S)
    text = re.sub(r'(?<![\\$\w])\$(?!\s)(.+?)(?<!\s)\$(?!\w)', repl_inline, text)
    return text

def _render_math():
    todo = [{'tex': t, 'display': d} for t, d in _math_items if (t, d) not in _math_cache]
    if todo:
        res = subprocess.run(['node', os.path.join(HERE, 'tex2svg.js')], input=json.dumps(todo),
                             capture_output=True, text=True, check=True)
        for item, svg in zip(todo, json.loads(res.stdout)):
            _math_cache[(item['tex'], item['display'])] = svg

def _insert_math(htmltext):
    def repl(m):
        tex, disp = _math_items[int(m.group(1))]
        svg = _math_cache[(tex, disp)]
        cls = 'math-display' if disp else 'math-inline'
        return f'<span class="{cls}">{svg}</span>'
    return re.sub('\x00MATH(\\d+)\x00', repl, htmltext)

# ---------- Bilder ---------------------------------------------------------
def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or 'application/octet-stream'
    with open(path, 'rb') as f:
        return f'data:{mime};base64,{base64.b64encode(f.read()).decode()}'

def embed_images(htmltext):
    def repl(m):
        before, src, after = m.group(1), m.group(2), m.group(3)
        p = os.path.join(SRC, src)
        if os.path.exists(p):
            return f'<img{before}src="{data_uri(p)}"{after} loading="lazy">'
        print('  ! Bild fehlt:', src, file=sys.stderr)
        return m.group(0)
    return re.sub(r'<img([^>]*?)src="([^"]+)"([^>]*)>', repl, htmltext)

# Bilder mit Titel -> <figure>
def figures(htmltext):
    def repl(m):
        attrs, title, rest = m.group(1), m.group(2), m.group(3)
        return f'<figure><img{attrs}{rest}><figcaption>{title}</figcaption></figure>'
    htmltext = re.sub(r'<p><img([^>]*?) title="([^"]*)"([^>]*)></p>', repl, htmltext)
    return htmltext

# ---------- Seiten ---------------------------------------------------------
def parse_page(path):
    raw = open(path, encoding='utf-8').read()
    meta = {}
    if raw.startswith('---'):
        _, fm, body = raw.split('---', 2)
        for line in fm.strip().splitlines():
            k, _, v = line.partition(':'); meta[k.strip()] = v.strip()
    else:
        body = raw
    meta['id'] = meta.get('id') or os.path.splitext(os.path.basename(path))[0]
    return meta, body

MD_EXT = ['tables', 'attr_list', 'md_in_html', 'admonition', 'footnotes', 'sane_lists',
          'pymdownx.tasklist', 'pymdownx.superfences', 'pymdownx.details']
MD_CFG = {'pymdownx.tasklist': {'custom_checkbox': True, 'clickable_checkbox': True}}

def strip_comments(body):
    """Zeilen, die mit %% beginnen, sind Redaktionskommentare und werden nicht gebaut."""
    return re.sub(r'^[ \t]*%%.*$', '', body, flags=re.M)

def render_md(body):
    body = strip_comments(body)
    body = _extract_math(body)
    md = markdown.Markdown(extensions=MD_EXT, extension_configs=MD_CFG)
    out = md.convert(body)
    return out

def main():
    pages = []
    for fn in sorted(os.listdir(os.path.join(SRC, 'pages'))):
        if fn.endswith('.md'):
            meta, body = parse_page(os.path.join(SRC, 'pages', fn))
            pages.append((meta, body))
    pages.sort(key=lambda p: float(p[0].get('order', 999)))

    rendered = []
    for meta, body in pages:
        rendered.append(render_md(body))
    _render_math()

    # Navigation: Gruppen aus meta['group']
    groups = {}
    order = []
    for meta, _ in pages:
        g = meta.get('group', 'Sonstiges')
        if g not in groups: groups[g] = []; order.append(g)
        groups[g].append(meta)
    nav = ['<nav class="sitenav" aria-label="Seitennavigation">']
    for g in order:
        items = groups[g]
        head = items[0]
        nav.append(f'<div class="navgroup" data-group="{html.escape(g)}">')
        nav.append(f'<a class="navhead" href="#{head["id"]}">{html.escape(head.get("nav", head["title"]))}</a>')
        if len(items) > 1:
            nav.append('<ul>')
            for m in items[1:]:
                nav.append(f'<li><a href="#{m["id"]}">{html.escape(m.get("nav", m["title"]))}</a></li>')
            nav.append('</ul>')
        nav.append('</div>')
    nav.append('</nav>')
    nav_html = '\n'.join(nav)

    body_parts = []
    for (meta, _), h in zip(pages, rendered):
        h = _insert_math(h)
        h = figures(h)
        h = embed_images(h)
        badge = meta.get('badge', '')
        modcls = f' m{meta["mod"]}' if meta.get('mod') else ''
        badge_html = f'<span class="badge{modcls}">{html.escape(badge)}</span>' if badge else ''
        body_parts.append(
            f'<article class="page{" raster" if meta["id"].startswith("raster-") else ""}" id="{meta["id"]}" data-title="{html.escape(meta["title"])}">\n'
            f'<header class="pagehead">{badge_html}<h1>{html.escape(meta["title"])}</h1></header>\n'
            f'{h}\n<footer class="pagefoot"><a href="#start">↑ Zur Übersicht</a></footer>\n</article>')

    css = open(os.path.join(SRC, 'style.css'), encoding='utf-8').read()
    js = open(os.path.join(SRC, 'app.js'), encoding='utf-8').read()
    stamp = datetime.date.today().strftime('%d.%m.%Y')

    doc = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nuklearmedizin – Lerneinheit Physik 9/10</title>
<meta name="description" content="Selbstständige Teamarbeit: Kernphysik im Kontext Nuklearmedizin (Physik, Doppeljahrgang 9/10, Gymnasium Niedersachsen)">
<style>
{css}
</style>
</head>
<body>
<a class="skip" href="#start">Zum Inhalt</a>
<div class="layout">
<aside class="sidebar">
<div class="brand"><a href="#start"><span class="brandmark">☢</span> Nuklearmedizin</a><span class="sub">Physik · Jahrgang 9/10</span></div>
<div class="navwide">
{nav_html}
</div>
<details class="navtoggle"><summary>Menü</summary>
{nav_html}
</details>
</aside>
<main class="content">
{chr(10).join(body_parts)}
</main>
</div>
<footer class="sitefoot">Lerneinheit Nuklearmedizin · Stand {stamp} · Diese Datei ist vollständig eigenständig (Bilder und Formeln sind eingebettet).</footer>
<script>
{js}
</script>
</body>
</html>'''
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(doc)
    print(f'geschrieben: {OUT} ({os.path.getsize(OUT)/1024/1024:.2f} MB, {len(pages)} Seiten, {len(_math_cache)} Formeln)')

if __name__ == '__main__':
    main()

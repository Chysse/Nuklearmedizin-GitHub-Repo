#!/usr/bin/env python3
"""Erzeugt aus denselben Quellen eine EPUB-3-Datei (für Apple Books u. a.)."""
import os, re, zipfile, uuid, datetime, html, shutil
import lxml.html, lxml.etree as ET
import build as B

OUT = os.path.join(B.HERE, '..', 'build', 'Nuklearmedizin.epub')

def to_xhtml(fragment):
    """HTML-Fragment -> wohlgeformtes XHTML (als String, ohne Wurzelelement)."""
    root = lxml.html.fragment_fromstring(fragment, create_parent='div')
    # Checkboxen -> Zeichen, Buttons/Formulare entfernen
    for inp in root.xpath('.//input'):
        span = ET.Element('span'); span.text = '☐ '
        inp.getparent().replace(inp, span)
    for el in root.xpath('.//button | .//label'):
        if el.tag == 'button': el.getparent().remove(el)
        else: el.tag = 'span'
    for el in root.xpath('.//*[@loading]'): del el.attrib['loading']
    for el in root.xpath('.//*[@focusable]'): del el.attrib['focusable']
    for el in root.xpath('.//*[@data-mml-node or @data-c or @data-mjx-texclass]'):
        for k in list(el.attrib):
            if k.startswith('data-'): del el.attrib[k]
    # Links #id -> id.xhtml
    for a in root.xpath('.//a[@href]'):
        h = a.get('href')
        if h.startswith('#'):
            a.set('href', h[1:] + '.xhtml' if h[1:] in PAGE_IDS else h)
    # SVG-Namensraum sicherstellen
    for svg in root.xpath('.//svg'):
        svg.set('xmlns', 'http://www.w3.org/2000/svg')
    s = ET.tostring(root, method='xml', encoding='unicode')
    s = re.sub(r'^<div[^>]*>', '', s); s = re.sub(r'</div>$', '', s)
    return s

PAGE_IDS = set()

def main():
    pages = []
    for fn in sorted(os.listdir(os.path.join(B.SRC, 'pages'))):
        if fn.endswith('.md'):
            meta, body = B.parse_page(os.path.join(B.SRC, 'pages', fn)); pages.append((meta, body))
    pages.sort(key=lambda p: float(p[0].get('order', 999)))
    PAGE_IDS.update(m['id'] for m, _ in pages)
    rendered = [B.render_md(b) for _, b in pages]
    B._render_math()

    css = open(os.path.join(B.SRC, 'style.css'), encoding='utf-8').read()
    # Layout-Regeln entfernen, nur Inhaltsstile behalten
    css = css.split('/* ---------- Layout ---------- */')[0]
    css += '\nbody{padding:0 .5em} .nojs-note{display:none} .pagefoot{display:none}\n'

    z = zipfile.ZipFile(OUT, 'w')
    z.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
    z.writestr('META-INF/container.xml', '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>''')
    z.writestr('OEBPS/style.css', css)
    manifest = ['<item id="css" href="style.css" media-type="text/css"/>',
                '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>']
    spine = []
    used_assets = set()
    for (meta, _), h in zip(pages, rendered):
        h = B._insert_math(h); h = B.figures(h)
        for m in re.finditer(r'src="(assets/[^"]+)"', h): used_assets.add(m.group(1))
        badge = meta.get('badge', '')
        body = to_xhtml(f'<p class="badge">{html.escape(badge)}</p><h1>{html.escape(meta["title"])}</h1>' + h)
        props = ' properties="svg"' if '<svg' in body else ''
        doc = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="de" lang="de">
<head><meta charset="utf-8"/><title>{html.escape(meta["title"])}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>{body}</body></html>'''
        # Wohlgeformtheit prüfen
        ET.fromstring(doc.encode('utf-8'))
        z.writestr(f'OEBPS/{meta["id"]}.xhtml', doc)
        manifest.append(f'<item id="p-{meta["id"]}" href="{meta["id"]}.xhtml" media-type="application/xhtml+xml"{props}/>')
        spine.append(f'<itemref idref="p-{meta["id"]}"/>')
    for i, a in enumerate(sorted(used_assets)):
        mime = 'image/png' if a.endswith('.png') else 'image/jpeg'
        z.write(os.path.join(B.SRC, a), f'OEBPS/{a}')
        manifest.append(f'<item id="img{i}" href="{a}" media-type="{mime}"/>')
    # Navigation
    groups, order = {}, []
    for meta, _ in pages:
        g = meta.get('group', 'Sonstiges')
        if g not in groups: groups[g] = []; order.append(g)
        groups[g].append(meta)
    nav = []
    for g in order:
        items = groups[g]; head = items[0]
        li = f'<li><a href="{head["id"]}.xhtml">{html.escape(head.get("nav", head["title"]))}</a>'
        if len(items) > 1:
            li += '<ol>' + ''.join(f'<li><a href="{m["id"]}.xhtml">{html.escape(m.get("nav", m["title"]))}</a></li>' for m in items[1:]) + '</ol>'
        nav.append(li + '</li>')
    z.writestr('OEBPS/nav.xhtml', f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="de" lang="de">
<head><meta charset="utf-8"/><title>Inhalt</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body><nav epub:type="toc" id="toc"><h1>Inhalt</h1><ol>{''.join(nav)}</ol></nav></body></html>''')
    uid = 'urn:uuid:' + str(uuid.uuid5(uuid.NAMESPACE_URL, 'radioaktivitaet-lerneinheit'))
    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    z.writestr('OEBPS/content.opf', f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="de">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">{uid}</dc:identifier>
<dc:title>Nuklearmedizin – Lerneinheit Physik 9/10</dc:title>
<dc:language>de</dc:language>
<dc:creator>Physik-Fachschaft</dc:creator>
<meta property="dcterms:modified">{now}</meta>
</metadata>
<manifest>{''.join(manifest)}</manifest>
<spine>{''.join(spine)}</spine>
</package>''')
    z.close()
    print(f'geschrieben: {OUT} ({os.path.getsize(OUT)/1024/1024:.2f} MB)')

if __name__ == '__main__':
    main()

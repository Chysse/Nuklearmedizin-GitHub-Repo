#!/usr/bin/env python3
"""Prüft die gebaute HTML-Datei: alle Sprungziele vorhanden, keine Formelfehler."""
import re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(HERE, '..', 'build', 'Nuklearmedizin.html'), encoding='utf-8').read()
links = set(re.findall(r'href="#([^"]+)"', html))
ids = set(re.findall(r'id="([^"]+)"', html))
missing = sorted(l for l in links if l not in ids and "'" not in l)
bad_math = re.findall(r'<code>[^<]*\\[^<]*</code>', html)
ok = True
if missing:
    print('FEHLER – Sprungziele fehlen:', ', '.join(missing)); ok = False
if bad_math:
    print('FEHLER – Formeln konnten nicht gerendert werden:', bad_math[:5]); ok = False
print('Größe: %.2f MB, Seiten: %d' % (len(html.encode())/1024/1024, html.count('<article class="page')))
sys.exit(0 if ok else 1)

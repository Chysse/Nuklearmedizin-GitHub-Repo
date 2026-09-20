#!/usr/bin/env python3
"""Erzeugt build/Nuklearmedizin.pdf aus der gebauten HTML-Datei (Druckansicht, A4)."""
import asyncio, os
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.abspath(os.path.join(HERE, '..', 'build', 'Nuklearmedizin.html'))
PDF = os.path.abspath(os.path.join(HERE, '..', 'build', 'Nuklearmedizin.pdf'))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto('file://' + HTML)
        await pg.wait_for_timeout(500)
        await pg.emulate_media(media='print')
        # Bilder sind mit loading="lazy" eingebettet; für den Druck alle laden
        await pg.evaluate('''async () => {
            const imgs = [...document.images];
            imgs.forEach(i => { i.loading = 'eager'; });
            await Promise.all(imgs.map(i => i.complete && i.naturalWidth ? null :
                new Promise(r => { i.addEventListener('load', r, {once: true}); i.addEventListener('error', r, {once: true}); })));
            await new Promise(r => setTimeout(r, 300));
        }''')
        await pg.pdf(path=PDF, format='A4', print_background=True,
                     margin={'top': '15mm', 'bottom': '15mm', 'left': '15mm', 'right': '15mm'})
        await b.close()
    print(f'geschrieben: {PDF} ({os.path.getsize(PDF)/1024/1024:.2f} MB)')

asyncio.run(main())

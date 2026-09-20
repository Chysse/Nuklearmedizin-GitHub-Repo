// Liest JSON-Array [{tex, display}] von stdin, gibt JSON-Array mit SVG-Strings aus.
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({packages: AllPackages});
const svg = new SVG({fontCache: 'none'});
const html = mathjax.document('', {InputJax: tex, OutputJax: svg});

let input = '';
process.stdin.on('data', d => input += d);
process.stdin.on('end', () => {
  const items = JSON.parse(input);
  const out = items.map(({tex: t, display}) => {
    try {
      const node = html.convert(t, {display: !!display, em: 16, ex: 8, containerWidth: 600});
      let s = adaptor.innerHTML(node);
      // Titel für Screenreader
      s = s.replace('<svg ', `<svg aria-label="${t.replace(/"/g, '&quot;').replace(/</g,'&lt;')}" `);
      return s;
    } catch (e) { return `<code>${t}</code>`; }
  });
  process.stdout.write(JSON.stringify(out));
});

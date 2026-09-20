/* Optionale Verbesserungen – die Seite funktioniert auch ohne dieses Skript
   (z. B. in der Vorschau der Dateien-App, in der kein JavaScript läuft). */
(function () {
  'use strict';
  var pages = Array.prototype.slice.call(document.querySelectorAll('article.page'));
  if (!pages.length) return;
  document.body.classList.add('js');

  var store = null;
  try { store = window.localStorage; store.setItem('__t', '1'); store.removeItem('__t'); } catch (e) { store = null; }
  var KEY = 'nuklearmedizin:';

  /* --- Seitenumschaltung über #id --- */
  function show(id, scroll) {
    var target = document.getElementById(id);
    if (!target || !target.classList.contains('page')) {
      // Sprungmarke innerhalb einer Seite? -> deren Seite anzeigen
      var el = id && document.getElementById(id);
      var host = el && el.closest && el.closest('article.page');
      if (host) { activate(host); if (scroll !== false) el.scrollIntoView(); return; }
      target = document.getElementById('start');
    }
    activate(target);
    if (scroll !== false) window.scrollTo(0, 0);
  }
  function activate(page) {
    pages.forEach(function (p) { p.classList.toggle('active', p === page); });
    document.querySelectorAll('.sitenav a').forEach(function (a) {
      a.classList.toggle('active', a.getAttribute('href') === '#' + page.id);
    });
    document.title = page.getAttribute('data-title') + ' – Radioaktivität';
    var nt = document.querySelector('.navtoggle');
    if (nt && window.innerWidth <= 900) nt.removeAttribute('open');
    if (store) { try { store.setItem(KEY + 'last', page.id); } catch (e) {} }
  }
  window.addEventListener('hashchange', function () { show(location.hash.slice(1)); });

  /* Vor/Zurück-Navigation je Seite */
  pages.forEach(function (p, i) {
    var nav = document.createElement('div'); nav.className = 'pagenav';
    var prev = pages[i - 1], next = pages[i + 1];
    nav.innerHTML = (prev ? '<a href="#' + prev.id + '">← ' + prev.getAttribute('data-title') + '</a>' : '<span></span>') +
                    (next ? '<a href="#' + next.id + '">' + next.getAttribute('data-title') + ' →</a>' : '<span></span>');
    p.appendChild(nav);
  });

  /* --- Checklisten merken --- */
  var boxes = document.querySelectorAll('input[type=checkbox].task-list-item-checkbox, .task-list-item input[type=checkbox]');
  Array.prototype.forEach.call(boxes, function (box, i) {
    var page = box.closest('article.page');
    var id = (page ? page.id : 'x') + ':' + i;
    box.disabled = false;
    if (store) {
      try { if (store.getItem(KEY + 'chk:' + id) === '1') box.checked = true; } catch (e) {}
    }
    var li = box.closest('li'); if (li) li.classList.toggle('done', box.checked);
    box.addEventListener('change', function () {
      if (li) li.classList.toggle('done', box.checked);
      if (store) { try { store.setItem(KEY + 'chk:' + id, box.checked ? '1' : '0'); } catch (e) {} }
      updateProgress(page);
    });
  });
  function updateProgress(page) {
    if (!page) return;
    var all = page.querySelectorAll('.task-list-item input[type=checkbox]');
    var bar = page.querySelector('.progress');
    if (!all.length) return;
    var done = 0; Array.prototype.forEach.call(all, function (b) { if (b.checked) done++; });
    if (!bar) { bar = document.createElement('div'); bar.className = 'progress'; page.querySelector('.pagehead').appendChild(bar); }
    var pct = Math.round(100 * done / all.length);
    bar.innerHTML = 'Checkliste: ' + done + ' von ' + all.length + ' erledigt &nbsp;<span style="width:' + pct + 'px"></span>';
  }
  pages.forEach(updateProgress);

  /* --- Zurücksetzen-Knopf (Lehrkräfte-Seite) --- */
  var reset = document.getElementById('reset-storage');
  if (reset) reset.addEventListener('click', function () {
    if (!store) return;
    var keys = []; for (var k = 0; k < store.length; k++) { if (store.key(k).indexOf(KEY) === 0) keys.push(store.key(k)); }
    keys.forEach(function (k) { store.removeItem(k); });
    location.reload();
  });

  /* Start: Hash, sonst zuletzt besuchte Seite, sonst Startseite */
  var first = location.hash ? location.hash.slice(1) : null;
  if (!first && store) { try { first = store.getItem(KEY + 'last'); } catch (e) {} }
  show(first || 'start', false);
})();

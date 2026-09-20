# Lerneinheit Nuklearmedizin (Physik, Jahrgang 9/10)

Dieses Repository enthält die Texte der Lerneinheit „Nuklearmedizin – Strahlung, die heilt?“ (Kernphysik im Kontext Nuklearmedizin, nach dem NUN-Material) und die Werkzeuge, mit denen daraus automatisch die Schülerfassung entsteht: eine einzige HTML-Datei für das iPad (`Nuklearmedizin.html`), dazu PDF und EPUB.

**Bei jeder Änderung an einem Text baut GitHub die drei Dateien neu.** Niemand muss dafür etwas installieren.

---

## Für alle: So änderst du einen Text

1. Ordner **`src/pages`** öffnen. Jede Seite der Lerneinheit ist dort eine Datei, z. B. `20-modul1.md` (Modul I) oder `41-info-strahlungsarten.md` (Infotext Strahlungsarten). Die Nummer bestimmt nur die Reihenfolge.
2. Datei anklicken, dann oben rechts auf das **Stift-Symbol** („Edit this file“).
3. Text ändern – wie in einem einfachen Texteditor. Ein Satz ist ein Satz; du musst nichts „programmieren“.
4. Oben rechts **„Commit changes…“** klicken, in das Feld kurz schreiben, was du geändert hast (z. B. „Modul I: Aufgabe B4 vereinfacht“), dann **„Commit changes“**.

Das war's. Nach ein bis zwei Minuten liegt die neue Fassung unter **Actions → letzter Lauf → Artifacts** zum Herunterladen (ZIP mit HTML, PDF, EPUB).

**Tipp:** Die Taste **`.`** (Punkt) im Repository öffnet einen komfortableren Editor mit Vorschau (funktioniert auch im Safari auf dem iPad). Dort links die Datei wählen, rechts oben das Vorschau-Symbol. Speichern geht dort über das Symbol „Source Control“ (Zweig-Symbol) → Nachricht eintippen → Häkchen.

### Wenn mehrere gleichzeitig arbeiten

GitHub kann **nicht** zwei Leute gleichzeitig in derselben Datei tippen lassen. Deshalb: **Jede Seite hat auf der Tagung eine verantwortliche Person.** Wer etwas an einer fremden Seite ändern möchte, schreibt ein *Issue* (siehe unten) oder spricht die Person an. Innerhalb verschiedener Dateien kann jeder jederzeit arbeiten.

### Etwas diskutieren statt sofort ändern

Oben auf **Issues → New issue** klicken und eine der Vorlagen wählen („Fachlicher Fehler“, „Formulierung“, „Ergänzung / Streichung“). Ein Issue ist ein Diskussionsfaden mit Ort, Problem und Vorschlag; wenn es erledigt ist, wird es geschlossen.

### Kommentare direkt im Text

Eine Zeile, die mit `%%` beginnt, erscheint **nicht** in der Schülerfassung. So könnt ihr Anmerkungen direkt an die Stelle setzen:

```
%% Kommentar (Anna): Ist „Nukleon“ hier schon eingeführt? Sonst Fußnote.
```

---

## Schreibregeln (Stilkarte)

| Regel | So | Nicht so |
| --- | --- | --- |
| Anrede auf Modulseiten: das Team | „Lest den Infotext …“, „Erstellt …“ | „Lies …“ |
| Anrede auf Arbeitsblättern: die Person | „Baue den Versuch auf …“ | „Baut …“ |
| Operatoren wie im Abitur | beschreiben, erklären, begründen, beurteilen, vergleichen | „Schreibt etwas zu …“ |
| Fachsprache | Äquivalentdosis, Netto-Zählrate, Schwellenwert | Äquivalentsdosis, Grenzwert |
| Zahlen | 2,1 mSv (Komma, geschütztes Leerzeichen vor der Einheit) | 2.1mSv |
| Kernreaktionen | `$^{226}_{88}\mathrm{Ra} \rightarrow\ ^{222}_{86}\mathrm{Rn} +\ ^{4}_{2}\mathrm{He}$` | He²⁺ |

**Was in einer Modulseite immer vorkommt (in dieser Reihenfolge):** Einleitung · `!!! warum` · Arbeitspakete mit Kriterien · `!!! lernprodukt` · ggf. `!!! video` · Sprint-Plan · `!!! info "So wird bewertet"` · Scrumboard-Checkliste.

---

## Die wichtigsten Schreibweisen in den Dateien

| Was | Schreibweise |
| --- | --- |
| Überschrift | `## Überschrift` (zwei Rauten = Abschnitt, drei = Unterabschnitt) |
| fett / kursiv | `**fett**`, `*kursiv*` |
| Aufzählung | `- Punkt` |
| Checkliste | `- [ ] Aufgabe` |
| Link auf eine andere Seite | `[Infotext Zählraten](#info-zaehlraten)` – das Ziel ist die `id` aus dem Kopf der Zieldatei |
| Formel im Text / eigene Zeile | `$R = \frac{N}{\Delta t}$` / `$$ … $$` |
| Bild mit Unterschrift | `![Beschreibung](assets/bild.jpg "Bildunterschrift")` |
| Kasten | `!!! aufgabe "Titel"` und darunter den Inhalt um **vier Leerzeichen** eingerückt. Kastentypen: `aufgabe`, `info`, `tipp`, `warnung`, `video`, `lernprodukt`, `sprint`, `zusatz`, `warum`, `lehrkraft` |
| Farbmarker | `<span class="ap">A1</span>` (Arbeitspaket), `<span class="kr">Kriterien:</span>`, `<span class="warumtag">Warum</span>` |
| Tabelle | Zeilen mit `|` trennen; zweite Zeile `| --- | --- |`; leere Zellen werden zu Ausfüllfeldern |

**Bitte nicht anfassen:** die Zeilen zwischen den beiden `---` ganz oben in jeder Datei (`id`, `title`, `nav`, `group`, `order`, `badge`, `mod`). Sie steuern Menü und Reihenfolge.

Neue Seite anlegen: eine vorhandene Datei kopieren, Kopfzeilen anpassen (`id` muss eindeutig sein, `order` bestimmt die Position, `group` die Menügruppe).

---

## Für die technische Betreuung

```
src/pages/        eine Markdown-Datei je Seite
src/assets/       Bilder (verkleinert, max. ca. 1400 px)
src/style.css     Gestaltung
src/app.js        optionale Funktionen (Seitenumschaltung, gemerkte Checklisten)
tools/build.py    Markdown → Nuklearmedizin.html (Formeln als SVG, Bilder eingebettet)
tools/tex2svg.js  Formel-Renderer (MathJax, Node.js)
tools/build_epub.py, tools/build_pdf.py, tools/check.py
.github/workflows/build.yml   baut bei jedem Commit HTML, PDF, EPUB (Artifact, 90 Tage)
```

Lokal bauen (macOS mit Homebrew):

```
brew install python node
pip3 install -r tools/requirements.txt && python3 -m playwright install chromium
cd tools && npm install && cd ..
python3 tools/build.py && python3 tools/check.py
cd tools && python3 build_epub.py && cd .. && python3 tools/build_pdf.py
```

Ergebnis in `build/`. Die Schülerfassung ohne Lehrkräfte-Seiten entsteht, indem die Dateien `9*-lehrkraft*.md` vor dem Bauen aus `src/pages` entfernt werden (z. B. in einem eigenen Branch `schuelerfassung`).

**Videos** liegen nicht im Repository (zu groß), sondern im IServ-/Nextcloud-Ordner neben der HTML-Datei: `Experiment zur Wirkung radioaktiver Strahlung.mp4`, `Einführungsvideo - Verwendung des Zählrohrs.mp4`.

**Veröffentlichung (GitHub Pages)** ist in `build.yml` vorbereitet, aber auskommentiert. Vor dem Aktivieren: Schulbuchfoto (`beispiel_magnetismus.jpg`) ersetzen und die Lizenz der LEIFIphysik-Abbildungen prüfen; Repository muss dafür öffentlich sein oder ein bezahlter Tarif vorliegen.

## Lizenz- und Quellenhinweise

Texte: eigene Erstellung bzw. Bearbeitung von NUN-Material (Naturwissenschaftlicher Unterricht in Niedersachsen), teils KI-gestützt erstellt und fachlich geprüft. Abbildungen: LEIFIphysik (Joachim Herz Stiftung), M. Täschner (IRS Hannover, bearbeitet), BfS-Daten, LD Didactic (Gerätefotos). Scrum-Elemente nach „Scrum in der Schule“ (Hopp Foundation / Mindshift.One). Nur zur schulinternen Nutzung, solange die Bildrechte nicht abschließend geklärt sind.

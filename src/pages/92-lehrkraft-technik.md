---
id: lehrkraft-technik
title: Technik – Verteilen, Öffnen, Weiterbearbeiten
nav: Für Lehrkräfte · Technik & Verteilung
group: Für Lehrkräfte
order: 92
badge: Lehrkräfte
---

## Was diese Datei ist

`Nuklearmedizin.html` ist eine **einzige, vollständig eigenständige HTML-Datei**: Alle Bilder sind als Daten eingebettet, alle Formeln sind vorab in Vektorgrafiken (SVG) umgewandelt, Schrift und Layout kommen ohne externe Dateien aus. Sie braucht **kein Internet und keinen Webspace**. Nach außen führen nur die Links zu den GeoGebra-Simulationen, zur AR-App, zu den StrahlenschutzKOMPAKT-Broschüren, zur Online-Nuklidkarte, zu den Videos und zu LEIFIphysik/BfS – die Simulationen und die AR-App werden in Modul I gebraucht, alles andere ist entbehrlich.

Die Datei funktioniert auf zwei Stufen:

| | ohne JavaScript (z. B. Vorschau der Dateien-App) | mit JavaScript (Safari über IServ, Browser-Apps) |
| --- | --- | --- |
| Inhalte, Bilder, Formeln | ✔ vollständig | ✔ vollständig |
| Navigation | Menü mit Sprungmarken; alle Seiten stehen untereinander | jede Seite einzeln, Vor/Zurück, Menü |
| Checklisten | anzeigbar, Häkchen nicht gespeichert | antippbar, werden pro iPad gemerkt |

## Wege auf das iPad – mit Bordmitteln

**1. IServ → Dateien → „Öffnen“ (empfohlen für den Unterricht).**
Die Datei in den Gruppenordner der Klasse legen (z. B. *Dateien → Gruppen → Klasse 10x → Physik → Nuklearmedizin*). Die Schülerinnen und Schüler öffnen sie in der IServ-App oder im Safari-Browser über *Öffnen* („Öffnet die Datei direkt im Browser“). Damit läuft die Seite als echte Webseite in Safari inklusive JavaScript und gemerkter Checklisten. Voraussetzung: Schul-WLAN und IServ-Login.

!!! warnung "Einmal testen"
    Ob IServ HTML-Dateien tatsächlich als Webseite anzeigt oder als Download behandelt, hängt von der IServ-Version und den Einstellungen der Schule ab. Bitte **vor der ersten Stunde einmal mit einem Schüler-iPad prüfen**: Datei antippen → erscheint die Seite mit Menü und Startseite? Erscheint stattdessen Quelltext oder ein Download, hilft Weg 2 oder 3.

**2. Dateien-App (iCloud Drive, „Auf meinem iPad“, IServ-Ordner in der Dateien-App) → Vorschau.**
Tippt man die Datei in der Dateien-App an, zeigt iPadOS sie in der **Schnellansicht** an. Dort werden Text, Bilder und Formeln vollständig dargestellt, aber **ohne JavaScript**: Alle Seiten stehen untereinander, das Menü funktioniert über Sprungmarken (auf manchen Systemversionen sind Links in der Schnellansicht nicht antippbar; dann hilft Scrollen und die Suche). Checklisten werden nicht gespeichert. Funktioniert auch **offline** und ohne Login – ideal zum Nachlesen zu Hause.

**3. PDF-Fassung.**
Im Quellordner liegt zusätzlich `Nuklearmedizin.pdf` (aus der Druckansicht erzeugt). PDFs öffnen sich überall zuverlässig (Dateien, Bücher, IServ-Vorschau), lassen sich mit Markierungen versehen und ausdrucken – ohne Navigation und Checklisten.

**4. E-Book-Fassung (Apple Books).**
`Nuklearmedizin.epub` öffnet sich über *Teilen → Bücher* in der vorinstallierten App **Bücher** – mit Inhaltsverzeichnis, anpassbarer Schriftgröße, Lesezeichen und Notizen, offline, ohne Login. Ebenfalls ohne Checklisten-Speicherung.

**5. Weitere Möglichkeiten (nicht Bordmittel).**
Browser-fähige Datei-Apps wie *Documents (Readdle)* zeigen lokale HTML-Dateien inklusive JavaScript an. Eine Lernplattform (Moodle, IServ-Kursmodul, falls vorhanden) kann die Datei als Webseite einbinden. Beides ist optional.

!!! tipp "Empfehlung"
    Im Unterricht **Weg 1** (IServ → Safari) nutzen, weil dort die Checklisten pro iPad gemerkt werden. Zusätzlich HTML und PDF in denselben Ordner legen, damit zu Hause und ohne WLAN alles lesbar bleibt. Die vier StrahlenschutzKOMPAKT-Broschüren (PDF) und die Bildmarker der AR-App ebenfalls in diesen Ordner legen; Videos sind als Links eingebunden und bewusst **nicht** eingebettet, um die Datei klein zu halten.

## Datei ändern und neu bauen

Alle Inhalte liegen als **Markdown-Dateien** im Quellordner `Nuklearmedizin-Webseite (Quelle)`:

```
src/pages/       eine .md-Datei je Seite (Kopfzeilen: id, title, nav, group, order, badge, mod)
src/assets/      Bilder (verkleinert)
src/style.css    Gestaltung
src/app.js       optionale Funktionen (Seitenumschaltung, Checklisten)
tools/build.py   Bauskript (Python 3, benötigt: markdown, pymdown-extensions)
tools/tex2svg.js Formelrenderer (Node.js, benötigt: mathjax-full)
build/           Ergebnis: Nuklearmedizin.html
```

Bauen auf dem Mac (einmalig `pip3 install markdown pymdown-extensions` und `cd tools && npm install mathjax-full`):

```
python3 tools/build.py
```

Seiten entfernen (z. B. die Lehrkräfte-Seiten für die Schülerfassung): die entsprechenden `.md`-Dateien aus `src/pages` verschieben und neu bauen. Formeln werden in den Markdown-Dateien wie gewohnt mit `$…$` und `$$…$$` geschrieben; Hinweiskästen mit `!!! aufgabe "Titel"`, `!!! info`, `!!! tipp`, `!!! warnung`, `!!! video`, `!!! lernprodukt`, `!!! sprint`, `!!! zusatz`, `!!! warum`, `!!! lehrkraft`.

## Lizenz- und Quellenhinweise

- Texte: Bearbeitung der NUN-Unterrichtseinheit „Kernphysik im Kontext Nuklearmedizin“ (Naturwissenschaftlicher Unterricht in Niedersachsen, Stand 23.06.2026); mehrere Infotexte (biologische Strahlenwirkung, Strahlungsarten, Abstandsgesetz, Aktivität/Halbwertszeit) aus der Lerneinheit Radioaktivität übernommen; Ergänzungen teilweise KI-gestützt erstellt und fachlich geprüft – wie in den Quellenangaben der Seiten vermerkt. Die Informationsblätter für Frau A. und Frau B. sind Unterrichtsmaterial und keine ärztliche Aufklärung.
- Abbildungen: Gammakamera-Foto Bionerd (CC BY-SA 3.0, Wikimedia Commons); Gammakamera-Schema nach quizlet.com; Szintigramm Schilddrüse praxis-nuramed.de; Tc-99m-Diagramm MSB NRW (Beispielaufgabe Abitur Physik GK); Nuklidkarten-Ausschnitt periodensystem-online.de; Kugelmodelle der Zerfallsarten, Skelettszintigramm, Radon-Zerfallskette und Radonstollen-Foto aus dem NUN-Material (Herkunft dort nicht vollständig angegeben – vor einer Weitergabe außerhalb der Schule prüfen); Übersichtstabelle Strahlungsarten und Abstandsgesetz-Grafiken aus LEIFIphysik (Joachim Herz Stiftung); Wirkungskette nach M. Täschner (IRS, Leibniz Universität Hannover); Expositionsgrafik nach BfS-Daten.
- Simulationen: GeoGebra-Materialien kz97spk2, mffspduv, adnzwgbq (NUN); AR-App „Radiation Protection“ der Strahlenschutzkurse (Leibniz Universität Hannover).
- Scrum-Elemente nach „Scrum in der Schule“ (Hopp Foundation / Mindshift.One).

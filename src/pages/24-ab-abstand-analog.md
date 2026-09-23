---
id: ab-abstand-analog
title: Experiment – Abstandsgesetz mit Licht (Analogexperiment)
nav: Arbeitsblatt · Abstandsgesetz mit Licht
group: Modul I
order: 24
badge: Modul I · Arbeitsblatt
mod: 1
---

Ihr untersucht, wie die Zählrate vom **Abstand** zur Quelle eines radioaktiven Präparats abhängt. Ihr habt gelernt, dass Gammastrahlung dieselbe Natur wie sichtbares Licht hat. Deshalb können wir die Frage mit dem gewöhnlichen Licht einer **Halogenlampe** untersuchen und auf ein echtes radioaktives Präparat verzichten.

Im Experiment wird eine **Solarzelle** mit dem Licht der Lampe bestrahlt. Der Abstand $d$ wird schrittweise vergrößert. Mit dem Multimeter wird jeweils der Fotostrom $I$ der Solarzelle gemessen – er steht für die Intensität der Strahlung an der Solarzelle. Zur Messung wird der Raum verdunkelt.

!!! tipp "Protokoll"
    Ein gutes Protokoll dieser Aufgaben hat für jeden Versuch: Aufbau (Foto/Screenshot), Durchführung (was wurde verändert?), Messwerte (Tabelle), Auswertung (Diagramm, Rechnung), Deutung (was folgt daraus für den Strahlenschutz?).

## Aufbau

![Solarzelle mit aufgesetzter Blende](assets/Analogexperiment.jpg "Die Solarzelle wird mit einer Blende abgedeckt"){: width=420 }

!!! warnung "Bitte vorsichtig"
    Geht mit den Experimentiermaterialien pfleglich um. Die Halogenlampe wird im Betrieb heiß.

- Decke die Solarzelle mit der Blende ab (Blende aus dem vorbereiteten Bogen ausschneiden).
- Schließe die Kabel der Solarzelle so an das Multimeter an, dass du eine **Stromstärke** ablesen kannst.
- Positioniere die Solarzelle ganz links auf der Schiene. Sie bleibt für die gesamte Messung dort stehen – **verschoben wird die Lampe, nicht der Sensor** (dann bleibt der Nulleffekt konstant).
- Miss den Fotostrom $I_0$, der durch das Restlicht im Raum erzeugt wird (**Nulleffekt**). Warte damit, bis der Raum verdunkelt ist.
- Stelle rechts neben der Solarzelle die Halogenlampe auf. Der Abstand zwischen den weißen Strichen an den Reiterfüßen soll 6,7 cm betragen – dann beträgt der Abstand zwischen Solarzelle und Lampe genau 4,0 cm.
- Netzteil: im ausgeschalteten Zustand die beiden linken Regler ganz nach rechts, die beiden rechten ganz nach links drehen. Einschalten, mit den rechten Reglern 9,0 V einstellen, dann die Lampe anschließen.

## Durchführung

1. Notiere den Nulleffekt $I_0$.
2. Beginne mit dem Abstand 4,0 cm. Miss den Fotostrom $I$, trage das Wertepaar ein, ziehe die Lampe ein Stück von der Solarzelle weg und wiederhole die Messung – bis zum Ende der Schiene.

**Nulleffekt:** $I_0 =$ ________ mA

| $d$ in cm | $I$ in mA | $I_{\text{korrigiert}} = I-I_0$ in mA |
| --- | --- | --- |
| 4,0 | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

## Auswertung

3. Stelle die Messwerte grafisch dar ($x$-Achse: Abstand, $y$-Achse: Netto-Zählrate) und zeichne eine Ausgleichskurve ein. Beschreibe den Verlauf des Graphen auch für sehr große Abstände.

!!! info "Info"
    Die folgende Abbildung zeigt: Bei doppeltem Abstand hat sich die Fläche, auf die sich die Strahlung verteilt, also vervierfacht. An einem Punkt der Oberfläche – vergleichbar mit dem Ort des Zählrohrs – kommt jetzt nur noch ein Viertel der Strahlung an.
    Allgemein gilt: Die Netto-Zählrate $R_{\text{Netto}}$ ist **antiproportional zum Quadrat des Abstands** $r$[^1]:
    $$R_{\text{Netto}} \sim \frac{1}{r^2}$$

![Abstandsquadratgesetz](assets/abstandsquadratgesetz.jpg "Abstandsquadratgesetz (Quelle: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) Borb)"){: .img-small }

4. Überprüfe an mehreren Beispielen, ob für deine Messreihe gilt: 2-facher Abstand → $\frac{1}{4}$ der Intensität, 3-facher Abstand → $\frac{1}{9}$, 4-facher Abstand → $\frac{1}{16}$.
5. In einem Gedankenexperiment nimmt ein Forscher eine kleine Menge radioaktives Präparat direkt in die Hand (Abstand vom Mittpunkt 0,5 cm). Alternativ kann er eine 10 cm lange Pinzette benutzen. Erkläre den Einfluss der Pinzette auf die Höhe der Intensität und damit Strahlendosis.
6. Eine Regel des Strahlenschutzes lautet: „**A**bstand so groß wie möglich.“ Begründe diese Regel vor dem Hintergrund deines Experiments.


!! info [^1]"Voraussetzungen des Modells"
    Das Abstandsgesetz gilt streng nur für eine punktförmige Quelle, geradlinige Ausbreitung und ohne Absorption in der Luft. Für Alphastrahlung, die in Luft schon nach wenigen Zentimetern verschluckt wird, weicht die Messung deshalb deutlich vom Gesetz ab – ein Beispiel dafür, dass Modelle Grenzen haben. Für Licht einer kleinen Lampe gilt das Gesetz dagegen sehr gut – deshalb funktioniert das Analogexperiment.
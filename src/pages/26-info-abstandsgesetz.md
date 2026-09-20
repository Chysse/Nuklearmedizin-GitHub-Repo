---
id: info-abstandsgesetz
title: Infotext – Das Abstandsgesetz
nav: Infotext · Abstandsgesetz
group: Modul I
order: 26
badge: Modul I · Infotext
mod: 1
---

## Herleitung

Nehmen wir an, dass die radioaktive Strahlung von einer kleinen Quelle **geradlinig in alle Raumrichtungen** ausgesendet wird. Im Abstand $r_1$ verteilt sich die Strahlung dann auf einer Kugeloberfläche mit dem Radius $r_1$.

![Kugel mit Radius r: Die Strahlung verteilt sich auf der Kugeloberfläche](assets/kugel.jpg "Die Strahlung verteilt sich auf einer Kugeloberfläche mit dem Radius r"){: .img-small }

Die Oberfläche $A_1$ dieser Kugel beträgt:

$$A_1 = 4 \pi r_1^2$$

Verdoppeln wir nun den Abstand zur Quelle ($r_2 = 2 r_1$), verdoppelt sich der Radius der Kugel. Damit wächst auch die Fläche, auf die sich die Strahlung verteilt:

$$A_2 = 4 \pi r_2^2 = 4 \pi (2 r_1)^2 = 4 \pi \cdot 4 r_1^2 = 4 \cdot A_1$$

Bei doppeltem Abstand hat sich die Fläche, auf die sich die Strahlung verteilt, also **vervierfacht**. An einem Punkt der Oberfläche – vergleichbar mit dem Ort des Zählrohrs – kommt jetzt nur noch **ein Viertel** der Strahlung an. Die Zählrate **viertelt** sich daher bei Verdopplung des Abstands.

![Strahlung trifft in 5 cm Abstand auf 1 cm², in 10 cm auf 4 cm², in 15 cm auf 9 cm², in 20 cm auf 16 cm²](assets/abstandsgesetz.jpg "Bei doppeltem Abstand verteilt sich dieselbe Strahlung auf die vierfache Fläche (Quelle: LEIFIphysik)")

Wird der Abstand verdreifacht, verneunfacht sich die Fläche – die Zählrate sinkt auf ein Neuntel. Allgemein gilt: Die Netto-Zählrate $R_{\text{Netto}}$ ist **antiproportional zum Quadrat des Abstands** $r$:

$$R_{\text{Netto}} \sim \frac{1}{r^2}$$

!!! info "Voraussetzungen des Modells"
    Das Abstandsgesetz gilt streng nur für eine punktförmige Quelle, geradlinige Ausbreitung und ohne Absorption in der Luft. Für Alphastrahlung, die in Luft schon nach wenigen Zentimetern verschluckt wird, weicht die Messung deshalb deutlich vom Gesetz ab – ein Beispiel dafür, dass Modelle Grenzen haben. Für Licht einer kleinen Lampe gilt das Gesetz dagegen sehr gut – deshalb funktioniert das Analogexperiment.

## Einhaltung eines Sicherheitsabstandes

Ein wirksamer Schutz gegen ionisierende Strahlung besteht darin, einen genügend großen Abstand zur Strahlenquelle einzuhalten. Ist die Quelle punktartig und sendet sie ihre Strahlung gleichmäßig nach allen Seiten aus (isotrope Quelle), gilt das quadratische Abstandsgesetz: Die Intensität nimmt mit dem Quadrat der Entfernung ab. In der Praxis kann eine Quelle als punktartig angesehen werden, wenn der Abstand mindestens fünfmal so groß ist wie ihre Ausdehnung.

<div class="img-row" markdown="1">
![Strahlung verteilt sich in doppeltem Abstand auf die vierfache Fläche](assets/abstand_flaeche.jpg "In doppeltem Abstand verteilt sich die Strahlung auf die vierfache Fläche"){: .img-small }
![Kugel mit Finger angefasst (0,5 cm) und mit Pinzette gehalten (10 cm)](assets/abstand_pinzette.jpg "Mit der Pinzette ist die Hand 20-mal weiter entfernt – die Intensität sinkt auf 1/400"){: .img-small }
</div>

Wird zum Beispiel eine kleine Menge radioaktiver Substanz, die in einer Kugel mit 0,5 cm Durchmesser eingeschlossen ist, mit den Fingern angefasst, so ist die Haut des Fingers 0,5 cm vom Mittelpunkt der Kugel entfernt. Packt man die Kugel dagegen mit einer Pinzette, ist die Hand etwa 10 cm vom Kugelmittelpunkt entfernt. Durch die 20-fache Entfernung beträgt die Intensität nur noch $(1/20)^2 = 1/400$ des ursprünglichen Wertes. In Laboratorien werden deshalb Werkzeuge mit langen Griffen verwendet; bei einem Meter langen Griffen sinkt die Dosisleistung um den Faktor $10^4$.

Zu bedenken ist: Luft absorbiert einen Teil der Strahlung, und Strahlung kann an Körpern gestreut werden – an manchen Stellen kann die Intensität deshalb höher sein, als das Abstandsgesetz erwarten lässt.

<small>Nach: Informationskreis KernEnergie (Hg.), M. Volkmer: „Radioaktivität und Strahlenschutz“, 2007, S. 69.</small>

## Überprüfung anhand von Messwerten

Es gibt mehrere Möglichkeiten, das Abstandsgesetz mit Messwerten zu überprüfen.

### 1. Produktgleichheit (Proportionalitätskonstante)

Ist $R$ antiproportional zu $r^2$, dann gilt **Produktgleichheit**: Das Produkt aus Zählrate und Abstandsquadrat ist eine Konstante $K$:

$$K = R_{\text{Netto}} \cdot r^2$$

Berechnet für jedes Messwertpaar den Wert $K$. Ist er – unter Berücksichtigung von Messunsicherheiten – bei allen Paaren (ungefähr) gleich, ist der Zusammenhang bestätigt.

### 2. Diagramm und Regression

Tragt die Messwerte in ein $r$-$R$-Diagramm ein. Liegen sie auf einer hyperbelähnlichen Kurve, ist das ein erster Hinweis. Als zweites Kriterium könnt ihr mit dem Taschenrechner (z. B. TI-Nspire CAS), in GeoGebra oder Numbers eine **Regression** des Typs $y = a \cdot x^{-2}$ durchführen. Liegt die erhaltene Kurve auf den Messwerten, ist der Zusammenhang sachgerecht überprüft.

### 3. Linearisierung

Trägt man $R$ nicht gegen $r$, sondern gegen $\frac{1}{r^2}$ auf, müssten die Messwerte auf einer **Geraden durch den Ursprung** liegen. Dieses Verfahren (Linearisierung) übersteigt den Unterrichtsinhalt der 10. Klasse und wird ab Jahrgang 11 verwendet – wer möchte, darf es aber gern ausprobieren.

!!! tipp "Messunsicherheiten beachten"
    Kleine Abstände lassen sich schwer genau einstellen, und die Impulszahl schwankt zufällig. Überlegt, wie groß die Abweichung von $K$ sein darf, damit ihr noch von „konstant“ sprechen könnt – und wie ihr die Messung verbessern könntet (längere Messzeit, mehrere Messungen mitteln).

<small>Quelle: NUN – Naturwissenschaftlicher Unterricht in Niedersachsen (bearbeitet); Abbildung Abstandsgesetz: LEIFIphysik.</small>

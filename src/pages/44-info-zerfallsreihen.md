---
id: info-zerfallsreihen
title: Infotext – Kernumwandlungen, Zerfallsreihen und Nuklidkarte
nav: Infotext · Zerfallsreihen und Nuklidkarte
group: Modul II
order: 44
badge: Modul II · Infotext · beide Pfade
mod: 2
---

## Die Schreibweise eines Nuklids

Ein Atomkern besteht aus **Protonen** (positiv geladen) und **Neutronen** (ungeladen). Die Anzahl der Protonen $Z$ (Kernladungszahl) legt fest, um welches Element es sich handelt; die **Massenzahl** $A$ ist die Summe aus Protonen und Neutronen. Ein bestimmter Kern – ein **Nuklid** – wird so geschrieben:

$${}^{A}_{Z}\mathrm{X} \qquad \text{zum Beispiel} \qquad {}^{131}_{53}\mathrm{I}, \quad {}^{99}_{42}\mathrm{Mo}, \quad {}^{222}_{86}\mathrm{Rn}$$

Die Neutronenzahl ist $N = A - Z$: Iod-131 hat 53 Protonen und $131 - 53 = 78$ Neutronen. Kerne mit gleicher Protonenzahl, aber verschiedener Neutronenzahl heißen **Isotope** desselben Elements (Iod-127 ist stabil, Iod-131 radioaktiv). Im Text schreibt man kurz „I-131“ oder „Iod-131“.

## Die Zerfallsarten als Kernumwandlungen

Ob ein Kern stabil ist, hängt vom Verhältnis von Neutronen zu Protonen ab. Instabile Kerne wandeln sich um und senden dabei Strahlung aus ([Infotext Strahlungsarten](#info-strahlungsarten)). Für die Zerfallsreihe ist wichtig, *was aus dem Kern wird*:

![Übersicht: Alpha-, Beta-minus-, Beta-plus- und Gamma-Zerfall als Kernumwandlung](assets/zerfallsarten_uebersicht.jpg "Die vier Zerfallsarten als Kernumwandlung (Modelldarstellung)"){: width=520 }

| Zerfall | Was passiert im Kern? | Neues Nuklid? | Beispiel |
| --- | --- | --- | --- |
| **α** (Alpha) | Ein Heliumkern (2 p + 2 n) verlässt den Kern. | ja: $Z - 2$, $A - 4$ | ${}^{222}_{86}\mathrm{Rn} \rightarrow {}^{218}_{84}\mathrm{Po} + {}^{4}_{2}\mathrm{He}$ |
| **β⁻** (Beta minus) | Ein Neutron wandelt sich in ein Proton und ein Elektron um; das Elektron wird ausgesandt. | ja: $Z + 1$, $A$ gleich | ${}^{131}_{53}\mathrm{I} \rightarrow {}^{131}_{54}\mathrm{Xe} + \mathrm{e}^-$ |
| **β⁺** (Beta plus) | Ein Proton wandelt sich in ein Neutron und ein Positron um; das Positron wird ausgesandt. | ja: $Z - 1$, $A$ gleich | ${}^{18}_{9}\mathrm{F} \rightarrow {}^{18}_{8}\mathrm{O} + \mathrm{e}^+$ (PET) |
| **γ** (Gamma) | Der Kern gibt überschüssige Energie als elektromagnetische Strahlung ab. | **nein** – gleiches Nuklid, nur „abgeregt“ | ${}^{99\mathrm{m}}_{43}\mathrm{Tc} \rightarrow {}^{99}_{43}\mathrm{Tc} + \gamma$ |

<div class="img-row" markdown="1">
![Alpha-Zerfall: Kern gibt Heliumkern ab](assets/zerfall_alpha.jpg "α-Zerfall im Kugelmodell")

![Beta-minus-Zerfall: Neutron wird zu Proton, Elektron wird ausgesandt](assets/zerfall_betaminus.jpg "β⁻-Zerfall im Kugelmodell")
</div>

Gammastrahlung tritt meist *zusammen* mit einem Alpha- oder Betazerfall auf: Der neue Kern entsteht in einem angeregten Zustand und gibt die Energie sofort (oder – wie bei Tc-99m – mit Verzögerung, „metastabil“) als Gammaquant ab. Deshalb ist I-131 ein Beta- **und** Gammastrahler.

## Zerfallsreihen

Ist das Tochternuklid selbst wieder radioaktiv, zerfällt es weiter – so entsteht eine **Zerfallsreihe**, die erst bei einem stabilen Nuklid endet. Jedes Glied hat seine eigene Halbwertszeit und Strahlungsart.

- **Pfad A:** ${}^{99}\mathrm{Mo} \xrightarrow{\beta^-,\ 66\ \mathrm{h}} {}^{99\mathrm{m}}\mathrm{Tc} \xrightarrow{\gamma,\ 6\ \mathrm{h}} {}^{99}\mathrm{Tc} \xrightarrow{\beta^-,\ 2{,}1\cdot 10^{5}\ \mathrm{a}} {}^{99}\mathrm{Ru}$ (stabil)
- **Pfad B:** ${}^{131}\mathrm{Te} \xrightarrow{\beta^-,\ 25\ \mathrm{min}} {}^{131}\mathrm{I} \xrightarrow{\beta^-\!+\gamma,\ 8\ \mathrm{d}} {}^{131}\mathrm{Xe}$ (stabil)
- **Modul IV:** die lange Uran-Radium-Reihe von ${}^{238}\mathrm{U}$ über ${}^{226}\mathrm{Ra}$ und ${}^{222}\mathrm{Rn}$ bis zum stabilen ${}^{206}\mathrm{Pb}$ – mit 14 Zerfällen.

## Die Nuklidkarte lesen

In der **Nuklidkarte** hat jedes Nuklid ein Feld. Waagerecht (Spalten) ist die **Protonenzahl** $Z$ aufgetragen, senkrecht (Zeilen) die **Neutronenzahl** $N$. Alle Isotope eines Elements stehen also in *einer Spalte* übereinander. Die Farbe zeigt die Zerfallsart:

| Farbe (in M2, Pfad B) | Bedeutung | Schritt in der Karte |
| --- | --- | --- |
| lila / schwarz | stabil | – |
| türkis / blau | β⁻-Zerfall | eine Spalte nach **rechts**, eine Zeile nach **unten** |
| rot | β⁺-Zerfall oder Elektroneneinfang | eine Spalte nach **links**, eine Zeile nach **oben** |
| gelb (Karlsruher Karte) | α-Zerfall | zwei Spalten nach **links**, zwei Zeilen nach **unten** |

Mit diesen „Zügen“ könnt ihr jede Zerfallsreihe in der Karte nachverfolgen – wie Figuren auf einem Spielbrett. Achtung: In der **Karlsruher Nuklidkarte** (und der Online-Karte unten) sind die Achsen vertauscht – Protonenzahl senkrecht, Neutronenzahl waagerecht. Die Regel bleibt dieselbe, nur die Richtungen drehen sich mit.

!!! info "Online-Nuklidkarte"
    [physik.gym-wst.de – Nuklidkarte](https://www.physik.gym-wst.de/apps/kp/03_nuklidkarte/index.html): Nuklid anklicken, Zerfallsart und Halbwertszeit ablesen, Zerfallsreihe verfolgen. Die gedruckte **Karlsruher Nuklidkarte** liegt in vielen Physiksammlungen aus.

!!! zusatz "Vertiefung: Was wird bei β⁻ noch ausgesandt?"
    Beim β⁻-Zerfall entsteht neben dem Elektron ein weiteres, fast masseloses und ungeladenes Teilchen – ein **Antineutrino**. Es verlässt den Körper (und die Erde) praktisch ohne Wechselwirkung und spielt für den Strahlenschutz keine Rolle. In der Schule lässt man es in der Reaktionsgleichung oft weg.

<small>Quellen: LEIFIphysik (Kernumwandlungen, Nuklidkarte); Karlsruher Nuklidkarte; Abbildungen aus dem NUN-Material (13b). Text mit KI-Unterstützung erstellt und anschließend fachlich geprüft.</small>

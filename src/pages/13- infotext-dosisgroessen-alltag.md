---
id: infotext-dosisgroessen-alltag
title: Infotext – Energiedosis, Äquivalentdosis und effektive Dosis
nav: C - Infotext · Dosisgrößen
group: Modul 0
order: 14
badge: Modul 0 · Infotext
---

%% Hinweis für die Redaktion: order/group ggf. an eure bestehende Seitenreihenfolge anpassen.
%% Diese Zeile wird beim Bauen automatisch entfernt.

Im Strahlenschutz werden nicht eine, sondern drei verschiedene Dosisgrößen verwendet, denn nicht jede Strahlung wirkt im Körper gleich stark, und nicht jedes Organ reagiert gleich empfindlich auf Strahlung. Eine rein physikalische Messung der absorbierten Energie sagt deshalb noch nichts darüber aus, wie groß das gesundheitliche Risiko tatsächlich ist. Die drei Dosisgrößen bauen aufeinander auf. 
Dieser Infotext erklärt, was sich hinter **Energiedosis**, **Äquivalentdosis** und **effektiver Dosis** verbirgt, warum man alle drei braucht – und wie groß typische Dosen im Alltag tatsächlich sind.


## Energiedosis $D$

!!! info "Definition"
    Die **Energiedosis** $D$ gibt an, wie viel Strahlungsenergie $E$ pro Kilogramm bestrahlter Masse $m$ absorbiert wird:
    $$D = \frac{E}{m}$$
    Einheit: $[D] = 1\ \mathrm{Gy} = 1\ \dfrac{\mathrm{J}}{\mathrm{kg}}$ (Gray)

    Die Energiedosis ist eine rein physikalische Messgröße. Sie ist unabhängig davon, um welche Strahlungsart es sich handelt und welches Gewebe getroffen wird.

## Äquivalentdosis $H$

Unterschiedliche Strahlungsarten richten bei gleicher Energiedosis unterschiedlich viel biologischen Schaden an. Alphastrahlung ist zum Beispiel auf kurzer Strecke im Gewebe viel dichter ionisierend als Beta- oder Gammastrahlung. Das wird mit einem Strahlungs-Wichtungsfaktor  bzw. Qualitätsfaktor $q$ berücksichtigt.

!!! info "Definition"
    $$H = q \cdot D$$
    Einheit: $[H] = 1\ \mathrm{Sv}$ (Sievert)

    | Strahlungsart | $q$ |
    |---|---|
    | Röntgen-, Gammastrahlung, Betastrahlung | 1 |
    | Alphastrahlung | 20 |

    Alphastrahlung richtet also bei gleicher Energiedosis das 20-fache an biologischem Schaden an wie Gamma- oder Betastrahlung.

!!! warnung "Vorsicht bei der Einheit"
    Gray und Sievert sind formal dieselbe SI-Einheit $\dfrac{\mathrm{J}}{\mathrm{kg}}$, stehen aber für unterschiedliche Dinge: Gray misst die physikalisch absorbierte Energie, Sievert die biologische Wirkung. Deshalb gibt es zwei unterschiedliche Namen für dieselbe Einheit.

## Effektive Dosis $E$

Auch nicht jedes Organ ist gleich strahlenempfindlich – Knochenmark und Keimdrüsen reagieren zum Beispiel empfindlicher als die Haut. Deshalb wird die Äquivalentdosis $H$ jedes betroffenen Organs bzw. Gewebes zusätzlich mit einem Gewebe-Wichtungsfaktor $w$ multipliziert und über alle betroffenen Organe aufsummiert.

!!! info "Definition"
    $$E = w_1 \cdot H_1 + w_2 \cdot H_2 + ...$$
    Einheit: $[E] = 1\ \mathrm{Sv}$ (Sievert)

    Die Summe aller Gewebe-Wichtungsfaktoren $w$ ergibt 1. Einige Beispiele (Angaben nach ICRP 103):

    | Organ/Gewebe | $w$ |
    |---|---|
    | Rotes Knochenmark, Lunge, Magen, Dickdarm, Brust | je 0,12 |
    | Keimdrüsen (Gonaden) | 0,08 |
    | Schilddrüse, Leber, Speiseröhre, Blase | je 0,04 |
    | Haut, Knochenoberfläche, Gehirn | je 0,01 |

    Die effektive Dosis erlaubt es, ganz unterschiedliche Bestrahlungssituationen – etwa eine Ganzkörperbestrahlung und eine lokale Röntgenaufnahme – hinsichtlich ihres gesundheitlichen Risikos miteinander zu vergleichen.

## Die drei Größen im Überblick

| Größe | Symbol | Formel | Einheit | Berücksichtigt zusätzlich |
|---|---|---|---|---|
| Energiedosis | $D$ | $D = \dfrac{E}{m}$ | Gray (Gy) | – |
| Äquivalentdosis | $H$ | $H = q \cdot D$ | Sievert (Sv) | Strahlungsart |
| Effektive Dosis | $E$ | $E = w_1 \cdot H_1 + w_2 \cdot H_2 + ...$ | Sievert (Sv) | Empfindlichkeit des Organs |

!!! tipp "Merkhilfe"
    Energiedosis → **wie viel** Energie ankommt. Äquivalentdosis → **wie gefährlich** die Strahlungsart ist. Effektive Dosis → **wie empfindlich** der getroffene Körperteil ist. Von links nach rechts wird aus einer rein physikalischen Größe eine strahlenbiologisch bzw. medizinisch aussagekräftige Größe.


## Wie groß sind typische Dosen im Alltag?
Es handelt sich um gerundete Richtwerte – die tatsächliche Dosis hängt von Gerät, Untersuchung, Flugroute, Wohnort und weiteren Faktoren ab. (Angaben nach Bundesamt für Strahlenschutz (BfS) und Strahlenschutzgesetz/-verordnung)

| Quelle | ungefähre effektive Dosis |
|---|---|
| Natürliche Strahlenexposition in Deutschland (Mittel pro Jahr) | ca. 2,1 mSv/Jahr *(davon Radon ca. 1,1 mSv, Nahrung ca. 0,3 mSv, kosmische und terrestrische Strahlung ca. 0,7 mSv)* |
| Medizinische Diagnostik in Deutschland (Mittel pro Kopf und Jahr) | ca. 1,5–2 mSv/Jahr |
| Röntgenaufnahme Brustkorb (Thorax) | ca. 0,05–0,1 mSv |
| Computertomographie (CT) des Bauchraums | ca. 10–20 mSv |
| Transatlantikflug (Hin- und Rückflug) | ca. 0,1 mSv |
| Gesetzlicher Grenzwert für beruflich strahlenexponierte Personen | 20 mSv/Jahr |
| Gesetzlicher Grenzwert für die allgemeine Bevölkerung (genehmigungspflichtige Anlagen) | 1 mSv/Jahr |



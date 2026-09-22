---
id: infotext-dosisgroessen-alltag
title: Infotext – Energiedosis, Äquivalentdosis und effektive Dosis
nav: Infotext · Dosisgrößen (mit Beispielen)
group: Infotexte
order: 13
badge: Infotext · Strahlenschutz
---

%% Hinweis für die Redaktion: order/group ggf. an eure bestehende Seitenreihenfolge anpassen.
%% Diese Zeile wird beim Bauen automatisch entfernt.

Im Strahlenschutz werden nicht eine, sondern drei verschiedene Dosisgrößen verwendet. Dieser Infotext erklärt, was sich hinter **Energiedosis**, **Äquivalentdosis** und **effektiver Dosis** verbirgt, warum man alle drei braucht – und wie groß typische Dosen im Alltag tatsächlich sind.

!!! warum "Warum reicht eine einzige Dosisgröße nicht aus?"
    Nicht jede Strahlung wirkt im Körper gleich stark, und nicht jedes Organ reagiert gleich empfindlich auf Strahlung. Eine rein physikalische Messung der absorbierten Energie sagt deshalb noch nichts darüber aus, wie groß das gesundheitliche Risiko tatsächlich ist. Die drei Dosisgrößen bauen aufeinander auf und berücksichtigen Schritt für Schritt mehr davon.

## Energiedosis $D$

!!! info "Definition"
    Die **Energiedosis** $D$ gibt an, wie viel Strahlungsenergie $E$ pro Kilogramm bestrahlter Masse $m$ absorbiert wird:
    $$D = \frac{E}{m}$$
    Einheit: $[D] = 1\ \mathrm{Gy} = 1\ \dfrac{\mathrm{J}}{\mathrm{kg}}$ (Gray)

    Die Energiedosis ist eine rein physikalische Messgröße. Sie ist unabhängig davon, um welche Strahlungsart es sich handelt und welches Gewebe getroffen wird.

## Äquivalentdosis $H_T$

Unterschiedliche Strahlungsarten richten bei gleicher Energiedosis unterschiedlich viel biologischen Schaden an. Alphastrahlung ist zum Beispiel auf kurzer Strecke im Gewebe viel dichter ionisierend als Beta- oder Gammastrahlung. Das wird mit einem Strahlungs-Wichtungsfaktor $w_R$ berücksichtigt.

!!! info "Definition"
    $$H_T = w_R \cdot D$$
    Einheit: $[H_T] = 1\ \mathrm{Sv}$ (Sievert)

    | Strahlungsart | $w_R$ |
    |---|---|
    | Röntgen-, Gammastrahlung, Beta-/Elektronenstrahlung | 1 |
    | Protonen | 2 |
    | Neutronen | 2,5 bis 20 (abhängig von der Energie) |
    | Alphastrahlung, Spaltfragmente | 20 |

    Alphastrahlung richtet also bei gleicher Energiedosis das 20-fache an biologischem Schaden an wie Gamma- oder Betastrahlung.

!!! warnung "Vorsicht bei der Einheit"
    Gray und Sievert sind formal dieselbe SI-Einheit ($\mathrm{J/kg}$), stehen aber für unterschiedliche Dinge: Gray misst die physikalisch absorbierte Energie, Sievert die biologische Wirkung. Deshalb gibt es zwei unterschiedliche Namen für dieselbe Einheit.

## Effektive Dosis $E$

Auch nicht jedes Organ ist gleich strahlenempfindlich – Knochenmark und Keimdrüsen reagieren zum Beispiel empfindlicher als die Haut. Deshalb wird die Äquivalentdosis $H_T$ jedes betroffenen Organs bzw. Gewebes $T$ zusätzlich mit einem Gewebe-Wichtungsfaktor $w_T$ multipliziert und über alle betroffenen Organe aufsummiert.

!!! info "Definition"
    $$E = \sum_T w_T \cdot H_T$$
    Einheit: $[E] = 1\ \mathrm{Sv}$ (Sievert)

    Die Summe aller Gewebe-Wichtungsfaktoren $w_T$ ergibt 1. Einige Beispiele (Auszug nach ICRP 103):

    | Organ/Gewebe | $w_T$ |
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
| Äquivalentdosis | $H_T$ | $H_T = w_R \cdot D$ | Sievert (Sv) | Strahlungsart ($w_R$) |
| Effektive Dosis | $E$ | $E = \sum_T w_T \cdot H_T$ | Sievert (Sv) | + Empfindlichkeit des Organs ($w_T$) |

!!! tipp "Merkhilfe"
    Energiedosis → **wie viel** Energie ankommt. Äquivalentdosis → **wie gefährlich** die Strahlungsart ist. Effektive Dosis → **wie empfindlich** der getroffene Körperteil ist. Von links nach rechts wird aus einer rein physikalischen Größe eine strahlenbiologisch bzw. medizinisch aussagekräftige Größe.

## Rechenbeispiel

!!! aufgabe "Vereinfachtes Beispiel: Von der Energiedosis zur effektiven Dosis"
    Bei einer Röntgenuntersuchung nimmt die Lunge eine Energiedosis von $D = 0{,}5\ \mathrm{mGy}$ Röntgenstrahlung auf.

    <span class="ap">1</span> **Äquivalentdosis:** Röntgenstrahlung hat $w_R = 1$, also
    $$H_T = w_R \cdot D = 1 \cdot 0{,}5\ \mathrm{mGy} = 0{,}5\ \mathrm{mSv}$$

    <span class="ap">2</span> **Beitrag zur effektiven Dosis:** Die Lunge hat $w_T = 0{,}12$, ihr Beitrag beträgt somit
    $$w_T \cdot H_T = 0{,}12 \cdot 0{,}5\ \mathrm{mSv} = 0{,}06\ \mathrm{mSv}$$

    <span class="ap">3</span> Da bei einer echten Röntgenaufnahme meist mehrere Organe mitbestrahlt werden, addieren sich deren Beiträge zur gesamten effektiven Dosis $E$ der Untersuchung. Reale Thoraxaufnahmen liegen deshalb insgesamt bei ca. 0,05–0,1 mSv effektiver Dosis (siehe Tabelle unten) – dieses Beispiel zeigt nur den Rechenweg für ein einzelnes Organ.

## Wie groß sind typische Dosen im Alltag?

| Quelle | ungefähre effektive Dosis |
|---|---|
| Natürliche Strahlenexposition in Deutschland (Mittel pro Jahr) | ca. 2,1 mSv/Jahr *(davon Radon ca. 1,1 mSv, Nahrung ca. 0,3 mSv, kosmische und terrestrische Strahlung ca. 0,7 mSv)* |
| Medizinische Diagnostik in Deutschland (Mittel pro Kopf und Jahr) | ca. 1,5–2 mSv/Jahr |
| Zahnröntgen | < 0,01 mSv |
| Röntgenaufnahme Brustkorb (Thorax) | ca. 0,05–0,1 mSv |
| Computertomographie (CT) des Bauchraums | ca. 10–20 mSv |
| Transatlantikflug (Hin- und Rückflug) | ca. 0,1 mSv |
| Gesetzlicher Grenzwert für beruflich strahlenexponierte Personen | 20 mSv/Jahr |
| Gesetzlicher Grenzwert für die allgemeine Bevölkerung (genehmigungspflichtige Anlagen) | 1 mSv/Jahr |

!!! info "Quelle und Genauigkeit"
    Werte nach Bundesamt für Strahlenschutz (BfS) und Strahlenschutzgesetz/-verordnung, Stand 2026. Es handelt sich um gerundete Richtwerte – die tatsächliche Dosis hängt von Gerät, Untersuchung, Flugroute, Wohnort und weiteren Faktoren ab.

!!! zusatz "Zum Weiterdenken (optional)"
    Vergleicht die natürliche Jahresdosis mit der Dosis einer einzelnen CT-Untersuchung. Was bedeutet das für die Abwägung von Nutzen und Risiko bei einer medizinisch notwendigen Untersuchung?

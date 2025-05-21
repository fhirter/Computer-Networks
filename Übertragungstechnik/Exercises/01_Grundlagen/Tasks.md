# Übung Grundlagen

Belege alle deine Antworten mit **Quellen**!

Visualisiere wenn möglich deine Antworten!

## Überblick

Lies folgenden Artikel aufmerksam durch. Halte den Inhalt stichwortartig fest und notiere dir Punkte, die du nicht
verstehst: [Wenn die Nachbarn früher jubeln: Die Fussball-TV-Hölle](https://blog.init7.net/de/wenn-die-nachbarn-frueher-jubeln-die-fussball-tv-hoelle/)

Versuche anschliessend in der Gruppe die nicht bekannten Punkte zu klären und bearbeite folgende Fragen:

- Skizziere den Weg des Signals vom Stadion bis zum heimischen TV.
- Was bedeutet Encoding bzw Codierung?
- Wie unterscheiden sich Ethernet und WLAN bezüglich Übertragungsstörungen? Wieso?
- Wozu dient Komprimierung?
- Der Artikel spricht von "Bandbreite". Welcher Fachbegriff wäre hier korrekt? Und was ist die eigentliche Bedeutung von
  Bandbreite?
- Was sind die Eigenschaften von Koaxialkabel?
- Wieso wird immer mehr IP basierte Übertragung genutzt? Welche Vor- und Nachteile hat das?

## Zeit- und Frequenzbereich

### Bandbreite

Erstelle eine Tabelle, in der du verschiedene Protokolle nach der verfügbaren Bandbreite ordnest.

Halte ebenfalls den Übertragungskanal fest (Funk, Twisted Pair, Koaxial, Glasfaser)

Viele Protokolle teilen den verfügbaren Frequenzbereich in Kanäle auf. Gib sowohl die verfügbare Bandbreite wie auch die
Kanalbandbreite an.

Die Zuweisung der Funkfrequenzen ist pro Land unterschiedlich. Gib die Situation in der Schweiz
an ([zugewiesenen Frequenzbereich](https://www.bakom.admin.
ch/bakom/de/home/frequenzen-antennen/nationaler-frequenzzuweisungsplan.html)).

- DVB-T
- WLAN IEEE 802.11a
- WLAN IEEE 802.11ac
- ADSL2+
- DOCSIS
- Gigabit Ethernet 1000BASE-T
- 10G Ethernet 10GBASE-LR

Also z.B.:

| Protokoll        | Frequenzbereich(e)       | Kanalbandbreite(n) | Übertragungskanal |
|------------------|--------------------------|--------------------|-------------------|
| DAB  (Pro Kanal) | 174-230MHz, 1452-1492MHz | 7 MHz              | Funk              |

### Fourier

Versuche mit [Geogebra](https://www.geogebra.org/calculator) ein Rechtecksignal zu approximieren.
Notiere, die Frequenzen und Amplituden der einzelnen Sinusschwingungen.

### Frequenzspektrum

Arbeite mit dem Script [`frequency_spectrums.py`](../../Examples/frequency_spectrums.py).

Untersuche den Einfluss der verschiedenen Grössen auf die Darstellung:
- Filterfrequenzen (Hoch- und Tiefpass)
- Verhältnis von Signal zu Rausch-Pegel

Notiere deine Erkenntnisse.

### Oszilloskop

Mach dich mit Oszilloskop und Frequenzgenerator vertraut.
- Bestimme oder Überprüfe mit dem Oszilloskop Frequenz, Periode, Amplitude, Effektivwert, Gleichanteil des Signals. 
- Bestimme mit einer Frequenzanalyse Störabstand und Bandbreite des Signals.





## Nachrichtenquader

Erstelle drei Diagramme für die drei wichtigen Übertragungsmedien Kupfer, Glasfaser und Funk. Die X-Achse bezeichnet die
den Frequenzbereich, die Y-Achse den Störabstand des Kanals:
![SNR_vs_Frequency.png](SNR_vs_Frequency.png))
Zeichne in diese drei Diagramme nun jeweils eine Fläche ein, die den verfügbaren Störabstand und Frequenzbereich des
Übertragungskanals darstellt. Die exakten numerischen Werte sind dabei zweitrangig, wichtig ist das Verhältnis der drei
Kanäle.

## Digitale und Analoge Signale

Digitalisiere folgendes Signal mit einer Abtastrate von 200Hz und einer Bittiefe von 2Bit:

![Zeitbereich.png](Zeitbereich.png)

Skizziere die digitalen Abtastpunkte.
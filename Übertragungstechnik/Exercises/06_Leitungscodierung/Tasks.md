# Übung Leitungscodierung

## Grundlagen

Recherchiere die Funktionsweise folgender Leitungscodes:

- NRZ
- Manchester
- 8b/10b

Skizziere die Funktionsweise!

## Modulation

Arbeite mit dem Script [`modulation.py`](../../Examples/modulation.py).

- Analysiere die drei Plots in den Grundeinstellungen.
- Analysiere den Einfluss der folgenden Grössen: `carrier_frequency`, `signal_frequency`, `modulation_index`
- Filtere das modulierte Signal, indem du `bandpass_frequencies` näher an die Trägerfrequenz setzt. Welche Bandbreite
  benötigt das Signal um korrekt empfangen werden zu können?

## Leitungscodes

Codiere folgenden String mit dem 4b5b Leitungscode:
`Hello World`

Wähle ein geeignetes Werkzeug für diese Aufgabe.

1. Wandle die Buchstaben mit der ASCII-Tabelle in Hex-Zahlen um.
2. Notiere die Zahlen als Binärzahlen.
3. Encodiere diese Zahlenfolge mit dem 4b5b Leitungscode.
4. Zähle die aufeinanderfolgenden 0 und 1 vor und nach dem Codieren.
5. Berechne den Mittelwert des Signals vor und nach dem Codieren.

## Moderne Technologien

Lies einen der drei Artikel (5G auf gebündeltem Millimeterwellen-Speed, PCI Express 6.0 erlaubt neue Architekturen,
Schnelleres WLAN mit Wi-Fi 7) aufmerksam durch.
Recherchiere, wenn du Dinge nicht verstehst. Setze den Artikel in Kontext zu den in den im Unterricht behandelten Themen.
Erarbeite ein Handout mit den wichtigsten Punkten aus dem Artikel und den Ergebnissen der Recherche.

### 5G auf gebündeltem Millimeterwellen-Speed

- Wieso sind 26GHz Netze nur für lokale Anwendungen vorgesehen und überhaupt sinnvoll?
- Wieso ist es für industrielle Anwendungen von Vorteil, dass das 26GHz Frequenzband nur auf Antrag genutzt werden kann?
- Welche Vorteile hat 5G gegenüber Wi-Fi?

### PCI Express 6.0 erlaubt neue Architekturen

- Was ist der Unterschied zwischen PAM und QAM?
- Was ist Gray-Code?
- Die Abbildung entspricht nicht Gray-Code. Wieso?
- Wieso ist PAM4 gegenüber einer Übertragung mit 2 Pegeln störanfälliger? Was ist Forwärtsfehlerkorrektur?

### Schnelleres WLAN mit Wi-Fi 7

- Wie wird die Erhöhung der Datenübertragungsrate erreicht?
- Wie wird die Reduktion der Latenz erreicht?
- Was ist 4K-QAM?
- Was ist MLO?
- Was ist 16x16 MU-MIMO?
- Was ist OFDMA?
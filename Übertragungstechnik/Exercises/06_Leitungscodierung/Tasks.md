# Übung Leitungscodierung

## Modulation

Arbeite mit dem Script [`modulation.py`](../../Examples/modulation.py).

- Analysiere die drei Plots in den Grundeinstellungen.
- Analysiere den Einfluss der folgenden Grössen: `carrier_frequency`, `signal_frequency`, `modulation_index`
- Filtere das modulierte Signal, indem du `bandpass_frequencies` näher an die Trägerfrequenz setzt. Welche 
  Bandbreite benötigt das Signal um korrekt empfangen werden zu können?


## Leitungscodes
Codiere folgenden String mit dem 4b5b Leitungscode:
`Hello World`

Wähle ein geeignetes Werkzeug für diese Aufgabe.

1. Wandle die Buchstaben mit der ASCII-Tabelle in Hex-Zahlen um.
2. Notiere die Zahlen als Binärzahlen.
3. Encodiere diese Zahlenfolge mit dem 4b5b Leitungscode.
4. Zähle die aufeinanderfolgenden 0 und 1 vor und nach dem Codieren.
5. Berechne den Mittelwert des Signals vor und nach dem Codieren.
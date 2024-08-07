# Übung Störabstand

## Übung 1
Mach dich mit Oszilloskop und Frequenzgenerator vertraut.
Beobachte das Signal am Oszilloskop bei verschiedenen Einstellungen am Frequenzgenerator.
Bestimme oder Überprüfe mit dem Oszilloskop Frequenz, Periode, Amplitude, Effektivwert, Gleichanteil des Signals.

Generiere mit dem Frequenzgenerator ein Signal mit einer Amplitude von 0dBu. 
Überprüfe das Signal mit dem Oszilloskop.
Überprüfe, ob das Mischpult den Signalpegel korrekt anzeigt.
Beobachte den Einfluss des Mischpults auf das Signal bei verschiedenen Einstellungen am Mischpult.
Versuche den Störabstand des Mischpults (am Ausgang) zu bestimmen.

Notiere deine Erkenntnisse.

## Übung 2
Untersuche das Rauschen einer Fotokamera.
Halte in einem Dokument fest, wie sich das Rauschen in Abhängigkeit der gewählten ISO Stufe verhält.
Hinweis: Bei Bildern zeigt sich das Rauschen in dunklen Bildteilen als farbige Pixel.

Notiere deine Erkenntnisse.

## Übung 3
Arbeite mit dem Script `frequency_spectrums.py` in Github Repository.

Untersuche den Einfluss der verschiedenen Grössen auf das Augendiagramm:
- Filterfrequenzen (Hoch- und Tiefpass)
- Verhältnis von Signal zu Rausch-Pegel

Notiere deine Erkenntnisse.

## Übung 4
Die beiden wichtigsten Kennwerte der Digital-Analog-Wandlung sind Bit-Rate und Abtastrate (engl. sampling rate).
Die Abtastrate bestimmt nach dem Nyquist-Shannon-Abtasttheorem die maximal im Signal vorkommende Frequenz.
Die Bit-Rate hingegen bestimmt den möglichen Störabstand, da die Quantisierung Rauschen verursacht.
Der resultierende Störabstand ist proportional zur verwendeten Bit-Tiefe n:

`Q_SNR = n*6.02dB+10.78dB`

Beschreibe, wie durch die Quantisierung Rauschen verursacht wird.

Überprüfe anhand der in verschiedenen Bitraten vorliegenden Audiodateien, wie sich das Signal mit verschiedenen Abtast- und Bit-Raten verändert.

Notiere deine Erkenntnisse.


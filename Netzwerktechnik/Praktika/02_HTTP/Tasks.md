# Praktikum HTTP
## Lernziele
Die Studierenden kennen das HTTP Protokoll und dessen Funktionsweise.

Die Studierenden sind in der Lage, Netzwerkanalysen mit entsprechenden Tools durchzuführen, die Ergebnisse zu analysieren und einfache Netzwerkfehler zu beheben. 

## Aufgabenstellung
Die aufgeführten Fragen und Aufgaben sollen dem Erreichen der Lernziele dienen. 
Zusätzliche Experimente und Recherchen sind ausdrücklich erwünscht.

Haltet die Antworten zu den Fragen und Aufgaben sowie zusätzliche Erkenntnisse in einem kurzen Bericht fest.
Dieser Bericht ist am Schluss einzureichen.
Er wird nicht bewertet und es werden keine formellen Anforderungen gestellt.

## Browsertools
### Vorbereitungen
- Öffne einen Browser (Chrome oder Firefox)
- Öffne die Netzwerk-Entwicklertools
- Öffne die [erste Webseite](http://info.cern.ch/hypertext/WWW/TheProject.html).

### Fragen und Aufgaben
- Welche HTTP Methode wurde verwendet?
- Mit welchem HTTP Statuscode hat der Server geantwortet? Was bedeutet dieser?
- Wie kann ein Statuscode >=400 provoziert werden? Was bedeutet dies?
- Wird die TCP Verbindung offen gehalten oder geschlossen?
- Welche Datentypen akzeptiert der Browser?

## Wireshark
### Vorbereitungen
- Öffne Wireshark und starte eine Aufzeichnung
- Öffne in einem Browser die [erste Webseite](http://info.cern.ch/hypertext/WWW/TheProject.html).
- Eruiere die IP-Adresse des Servers: `ping info.cern.ch`
- Filtere in Wireshark anhand dieser Adresse

### Fragen und Aufgaben
- Untersuche die Request und Response Header. Erkläre die einzelnen Bestandteile der Header und deren Bedeutung.
- Über welche Sockets läuft die Verbindung?
- Skizziere die TCP Verbindung der ersten HTTP-Anfrage.
- Was Ändert sich in der Wireshark Aufzeichnungm, wenn eine Seite über HTTPS aufgerufen wird?

## cURL, wget
- Erstelle dieselbe HTTP Anfrage auch mit den CLI Programmen `cURL` und `Wget`.
- Speichere die Website in einer Datei.
- Experimentiere mit den Header Feldern. Welche Werte können gesetzt werden? Wie reagiert der Server?


## HTTP/2, Cache und Cookies
### Vorbereitung
- Öffne einen Browser (Chrome oder Firefox)
- Öffne die Netzwerk-Entwicklertools und starte eine Netzwerkaufzeichnung.
- Öffne die [Webseite der Schule](https://www.teko.ch) oder eine andere Webseite deiner Wahl.

### Fragen und Aufgaben
- Untersuche die Kommunikation bei ein- bzw. ausgeschaltetem Cache. Siehst du einen Unterschied?
- HTTP/2 verspricht höhere Geschwindigkeiten im Vergleich zu HTTP/1.1. HTTP/3 soll diese weiter steigern. Erstelle eine kleine Statistik, um dies zu überprüfen.
- Untersuche die gespeicherten Cookies. Versuche herauszufinden, wozu diese dienen.
- Cookies werden oft genutzt, um den Login Zustand zu speichern. Untersuche, was passiert, wenn du die Cookies löscht. Mit welchem Cookie wird der Login-Zustand gespeichert? Wie funktioniert dies?


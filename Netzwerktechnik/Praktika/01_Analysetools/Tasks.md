# Praktikum Analysetools

## Lernziele

Die Studierenden sind in der Lage, Netzwerkanalysen mit entsprechenden Tools durchzuführen, die Ergebnisse zu analysieren und einfache Netzwerkfehler zu beheben. 

## Aufgabenstellung
Die aufgeführten Fragen und Aufgaben sollen dem Erreichen der Lernziele dienen.
Zusätzliche Experimente und Recherchen sind ausdrücklich erwünscht.
Die Aufgaben sind bewusst eher umfangreich.
Es ist wichtiger, dass die Aufgaben gründlich gemacht werden, als dass alle Aufgaben erledigt werden.

Die Antworten zu den Fragen und Aufgaben sowie zusätzliche Erkenntnisse sollen in einem kurzen Bericht festgehalten werden.
Dieser Bericht ist am Schluss per E-Mail an den Dozenten einzureichen.
Er wird nicht bewertet, es werden jedoch folgende formellen Anforderungen gestellt:
- Dateiformat: [Markdown](https://www.markdownguide.org/) und daraus [generiertes PDF](https://pandoc.org/).
- Diagramme: [PlantUML](https://plantuml.com/de/), [Mermaid](https://mermaid.js.org/) o.ä.

## Browsertools
### Vorbereitungen
- Öffne einen Browser (Chrome oder Firefox)
- Öffne die Netzwerk-Entwicklertools
- Öffne die [erste Webseite](http://info.cern.ch/hypertext/WWW/TheProject.html).

### Fragen und Aufgaben
- Untersuche und Dokumentiere die Netzwerk-Analysemöglichkeiten, die der Browser bietet.
- Vergleiche die Anfrage und Antwort der oben genannten Website mit einer modernen Website.

## Wireshark
### Vorbereitungen
- Öffne Wireshark und starte eine Aufzeichnung

### Fragen und Aufgaben
- Untersuche und Dokumentiere die Netzwerk-Analysemöglichkeiten, die Wireshark bietet.
- Wie können Pakete gefiltert werden?
- Untersuche von verschiedenen Nachrichten die Header der unterschiedlichen Layer.
  - Welche Protokolle werden verwendet?
  - Zu welchem Layer gehören die Protokolle?
  - Welche Adressen und Ports sind gesetzt?

## cURL, wget
- Erstelle dieselbe HTTP Anfrage an die [erste Webseite](http://info.cern.ch/hypertext/WWW/TheProject.html) auch mit den CLI Programmen `cURL` und `Wget`.
- Welche Möglichkeiten bieten die beiden Tools?
- Speichere die Website in einer Datei.

## PyCharm HTTP Client
- Erstelle dieselbe HTTP Anfrage an die [erste Webseite](http://info.cern.ch/hypertext/WWW/TheProject.html) mit dem HTTP Client von PyCharm.
- Welche Möglichkeiten bietet dieses Tool?
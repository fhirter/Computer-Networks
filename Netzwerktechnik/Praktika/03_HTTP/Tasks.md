# Praktikum HTTP
## Lernziele
Die Studierenden kennen das HTTP Protokoll und dessen Funktionsweise.

Die Studierenden sind in der Lage, Netzwerkanalysen mit entsprechenden Tools durchzuführen, die Ergebnisse zu analysieren und einfache Netzwerkfehler zu beheben. 

## Aufgabenstellung
Die aufgeführten Fragen und Aufgaben sollen dem Erreichen der Lernziele dienen. 
Zusätzliche Experimente und Recherchen sind ausdrücklich erwünscht.
Es ist wichtiger, dass die Aufgaben gründlich bearbeitet und dokumentiert werden, als dass alle Aufgaben erledigt werden.

Das Vorgehen, die Antworten und Erkenntnisse sollen in einem kurzen Bericht festgehalten werden.
Dieser Bericht ist am Schluss per E-Mail an den Dozenten einzureichen.
Er wird nicht bewertet, es werden jedoch folgende formellen Anforderungen gestellt:
- Dateiformat: [Markdown](https://www.markdownguide.org/) oder daraus [generiertes PDF](https://pandoc.org/).
- Diagramme: [PlantUML](https://plantuml.com/de/), [Mermaid](https://mermaid.js.org/) o.ä.

## HTTP Allgemein
Untersuche den HTTP Aufruf auf die [erste Webseite](http://info.cern.ch/hypertext/WWW/TheProject.html).
Nutze für die Beantwortung der Fragen geeignete Tools (Browser, Wireshark, PyCharm, cURL, wget).

### HTTP Methoden und Statuscodes
- Welche HTTP Methode wurde verwendet?
- Mit welchem HTTP Statuscode hat der Server geantwortet? Was bedeutet dieser?
- Wie kann ein Statuscode >=400 provoziert werden? Was bedeutet dies?
- Was ändert sich in der Abfrage, wenn eine Seite über HTTPS aufgerufen wird?
- Speichere die Website in einer Datei.

### Transport Protocol
- Wird die TCP Verbindung offen gehalten oder geschlossen?
- Skizziere die TCP Verbindung der ersten HTTP-Anfrage.
- Über welche Sockets läuft die Verbindung?

### Header
- Welche Dateitypen akzeptiert der Browser?
- Untersuche die Request und Response Header. Erkläre die einzelnen Bestandteile der Header und deren Bedeutung.
- Experimentiere mit den Header Feldern des Requests. Welche Werte können gesetzt werden? Wie reagiert der Server?

### Cache
- Untersuche die Kommunikation bei ein- bzw. ausgeschaltetem Cache. Siehst du einen Unterschied?

### Cookies
- Untersuche die gespeicherten Cookies von einem Webshob (z.B. [digitec.ch](https://www.digitec.ch)) Versuche herauszufinden, wozu diese dienen.
- Cookies werden oft genutzt, um den Login Zustand oder einen Warenkorb zu speichern. 
  Untersuche, was passiert, wenn du die Cookies löscht.
  Mit welchem Cookie wird der Login-Zustand gespeichert? Wie funktioniert dies?

### HTTP/2 und HTTP/3
- HTTP/2 verspricht höhere Geschwindigkeiten im Vergleich zu HTTP/1.1. HTTP/3 soll diese weiter steigern. Erstelle eine kleine Statistik, um dies zu überprüfen.
- Untersuche mit verschiedenen Websites, wie viele TCP Verbindungen ein Browser bei HTTP/1.1 und HTTP/2 Verbindungen öffnet.
- Untersuche, wie bei HTTP/3 UDP verwendet wird.
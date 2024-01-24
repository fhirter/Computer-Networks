# Video Streaming

## Lernziele

* Die Studierenden kennen die Internetprotokolle DNS, [...] und verstehen deren Funktionsweise.
* Die Studierenden wissen, wie Video Streaming funktioniert und wozu Content Delivery Networks dienen
* Die Studierenden sind in der Lage, die im Kurs erlernten Techniken und Konzepte in realen Netzwerkumgebungen
  umzusetzen.
* Die Studierenden Können mit geeigneten Werkzeugen die HTTP Kommunikation analysieren und auswerten.

## Aufgabenstellung

Zum Erreichen der Lernziele sollten die Aufgaben für einen Streaming-Anbieter vollständig gelöst werden.

Die Antworten sollen in einem kurzen Bericht festgehalten werden.
Dieser Bericht ist am Schluss per E-Mail an den Dozenten einzureichen.
**Die Abgabe ist zwingend**, wird jedoch nicht bewertet.
Es werden folgende formellen Anforderungen gestellt:

- Dateiformat: [Markdown](https://www.markdownguide.org/) oder daraus [generiertes PDF](https://pandoc.org/).
- Diagramme: [PlantUML](https://plantuml.com/de/), [Mermaid](https://mermaid.js.org/) o.ä.

Untersuche, wie Youtube und Netflix Videos streamen.
Falls du kein Netflix Abo hast, untersuche einen Streaming-Anbieter deiner Wahl oder eine alternative Videoplattform.

Die Aufgabe soll frei gelöst werden unter Verwendung der bisher erlernten Techniken und Werkzeuge (**Netzwerkanalyse im
Browser, Wireshark, dig**, etc).
Die aufgeführten Fragen können als Orientierung dienen.
Ziel ist, die Fragen durch eigene Untersuchungen zu beantworten und nicht im Internet zu recherchieren.

### Video Streaming

- Welche Protokolle werden für die Datenübertragung verwendet?
- Welchen Einfluss hat die Videoqualität auf die Übertragung?
  Versuche, die Reduktion der Datenrate zu erfassen und grafisch darzustellen!
- Was passiert, wenn du die Übertragungsgeschwindigkeit im Browser drosselst?

### Content Delivery Networks
Untersuche, wie Youtube und Netflix den geeigneten Server für die Bereitstellung der Videodaten auswählen.

- Welche Server liefern die Videodaten?
- Wie funktioniert die Auswahl des Videoservers?
- Wo befinden sich diese Server?
- Wird beim gleichen Video immer derselbe Server ausgewählt?
- Findest du ein Video, das von einem weiter entfernten Server geliefert wird?

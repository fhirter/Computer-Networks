# Praktikum Einstieg Application Layer

## Lernziele

Die Studierenden können Netzwerktechnologien und -trends kritisch bewerten und ihre Relevanz für verschiedene Anwendungsfälle einschätzen.
Die Studierenden kennen die Funktionen und Unterschiede von TCP/IP und ISO/OSI Modellen sowie die zugehörigen Protokolle wie HTTP [...].

## Aufgabenstellung
Die Aufgaben sind bewusst eher umfangreich.
Es ist wichtiger, dass die Aufgaben gründlich gemacht werden, als dass alle Aufgaben erledigt werden.

Die Antworten sollen in einem kurzen Bericht festgehalten werden.
Dieser Bericht ist am Schluss per E-Mail an den Dozenten einzureichen.
Er wird nicht bewertet, es werden jedoch folgende formellen Anforderungen gestellt:
- Dateiformat: [Markdown](https://www.markdownguide.org/) und daraus [generiertes PDF](https://pandoc.org/).
- Diagramme: [PlantUML](https://plantuml.com/de/), [Mermaid](https://mermaid.js.org/) o.ä.

### no data loss & time sensitive

Abbildung 2.4 im Buch zeigt keine Applikation, die sowohl keinen Datenverlust toleriert als auch zeitkritisch ist.
Findest du ein Beispiel für eine solche Applikation?

### Bankautomat

Entwerfe ein Protokoll für die Kommunikation zwischen einem Bankautomaten und dem zentralen Server der Bank.
Das Protokoll soll es ermöglichen, dass Kontonummer und PIN überprüft werden können, der Kontostand abgefragt werden
kann und Geld bezogen werden kann. Das Protokoll soll den Fall unterstützen, wenn zu wenig Geld für einen Bezug auf dem Konto
vorhanden ist.
Spezifiziere das Protokoll, indem du die Nachrichten, die ausgetauscht werden, auflistest, die Felder erläuterst
und jeweils beschreibst, was der Bankautomat bzw der zentrale Server nach der jeweiligen Nachricht machen.
Skizziere die Kommunikation analog der Abbildung 1.2 im Buch.
Begründe und erläutere deine Überlegungen und halte fest, welche Anforderungen an das Transport-Layer-Protokoll gestellt werden.

### Messaging

SMS, iMessage, Signal, WhatsApp und Matrix sind alles Echtzeit Messaging Dienste fürs Smartphone.
Untersuche deren Funktionsweise, recherchiere welche Protokolle sie verwenden und vergleiche sie.
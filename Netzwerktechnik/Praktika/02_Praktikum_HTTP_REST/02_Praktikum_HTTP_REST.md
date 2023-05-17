# Praktikum HTTP und REST

## Lernziele
Die Studierenden kennen das HTTP Protokoll und dessen Funktionsweise.

Die Studierenden sind in der Lage, Netzwerkanalysen mit entsprechenden Tools durchzuführen, die Ergebnisse zu analysieren und einfache Netzwerkfehler zu beheben. 

## Aufgabenstellung
Die aufgeführten Fragen und Aufgaben sollen dem Erreichen der Lernziele dienen. 
Zusätzliche Experimente und Recherchen sind ausdrücklich erwünscht.

Haltet die Antworten zu den Fragen und Aufgaben sowie zusätzliche Erkenntnisse in einem kurzen Bericht fest.
Dieser Bericht ist am Schluss einzureichen.
Er wird nicht bewertet und es werden keine formellen Anforderungen gestellt.

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


## REST
### Vorbereitung
Wähle eine der folgenden APIs aus und mache eine Anfrage mit cURL und Insomnia.
* [IMDB](https://imdb-api.com/API)
* [SBB](https://data.sbb.ch/pages/home/)
* [Open-Data-Plattform Mobilität](https://opentransportdata.swiss/de/)
* [Weather](https://openweathermap.org/api)
* [Openrouteservice](https://openrouteservice.org/dev/#/api-docs)
* [Google Maps](https://developers.google.com/maps/documentation/maps-static)
* [Youtube](https://developers.google.com/youtube/v3/getting-started?hl=de)
* [Openai](https://platform.openai.com/docs/api-reference)

Bei einigen der APIs muss zuerst ein API Key erstellt werden.

### Fragen und Aufgaben
- Untersuche die Antwort und wie du mit der Anfrage die Antwort beeinflussen kannst.
- Vergleiche die Endpunkte und die Antwort mit der REST Theorie. Wo entspricht die API den REST Prinzipien, wo nicht?


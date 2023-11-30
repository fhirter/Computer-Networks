# Praktikum Webserver

## Lernziele

Die Studierenden können einfache REST Schnittstellen serverseitig implementieren.

Die Studierenden können für die verschiedenen CRUD Operationen die geeignete HTTP Methode (GET, POST, PUT, DELETE) und
HTTP Statuscodes wählen. Sie können für eine gegebene Ressource geeignete URL Pfade wählen.

## Aufgabenstellung

Für viele Web-Applikationen bietet es sich an, das Frontend über eine REST-API anzubinden.
So ist die Applikation von Anfang an offen für Erweiterungen.

Schreibe eine einfache CRUD (Create, Read, Update, Delete) Applikation für "User"-Objekte.
Nutze alternativ ein einfaches Datenschema deiner Wahl.

Schreibe die Applikation in einer Sprache deiner Wahl. Die Lösungen sind in JavaScript verfügbar.

Für einige Endpunkte stehen Tests zur Verfügung.
Mit folgenden Befehlen kannst du diese ausführen:

```shell
npm install
npm run test
```

Das Vorgehen, die Antworten und Erkenntnisse sollen in einem kurzen Bericht festgehalten werden.
Dieser Bericht ist am Schluss zusammen mit dem Code per E-Mail an den Dozenten einzureichen.
Er wird nicht bewertet, es werden jedoch folgende formellen Anforderungen gestellt:
- Dateiformat: [Markdown](https://www.markdownguide.org/) oder daraus [generiertes PDF](https://pandoc.org/).
- Diagramme: [PlantUML](https://plantuml.com/de/), [Mermaid](https://mermaid.js.org/) o.ä.

### Weiterführende Aufgaben

Erweitere die API mit einem Cache.

Erweitere die API mit URL Referenzen (`_links`) auf die verfügbaren Ressourcen (HATEOAS).

## Informationen

### OpenAPI

Die [OpenAPI Specification](https://de.wikipedia.org/wiki/OpenAPI) ist ein weit verbreiteter Standard zur Dokumentation von REST-APIs.
Mit [SwaggerUI](https://swagger.io/tools/swagger-ui/) kann die Spezifikation intuitiv als Webseite dargestellt werden.
Mit [Swagger JS Doc](https://github.com/Surnet/swagger-jsdoc) kann die OpenAPI Spezifikation anhand des Express Code generiert werden.
So wird sichergestellt, dass Dokumentation und Code synchron sind.

### Tech-Stack der Lösungen

- Backendsprache: Node.JS
- Backend-Framework: [Express.js](http://expressjs.com/)
- Unit-Test-Framework: [Jest](https://jestjs.io/)
- API-Test-Framework: [Supertest](https://www.npmjs.com/package/supertest)

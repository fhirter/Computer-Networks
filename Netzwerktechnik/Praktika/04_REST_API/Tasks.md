# Praktikum Webserver

## Lernziele

Die Studierenden können einfache REST Schnittstellen serverseitig implementieren und gemäss der OpenAPI Spezifikation
dokumentieren.

## Aufgabenstellung

Schreibe eine einfache CRUD (Create, Read, Update, Delete) Applikation.
Nutze ein einfaches Datenschema deiner Wahl, z.B. Personaldaten oder Wetterdaten aus der vorgängigen Übung.

### REST API

Für viele Web-Applikationen bietet es sich an, das Frontend über eine REST-API anzubinden.
So ist die Applikation von Anfang an offen für Erweiterungen.
Die [OpenAPI Specification](https://de.wikipedia.org/wiki/OpenAPI) ist ein weit verbreiteter Standart zur Dokumentation
von REST-APIs.
Mit [SwaggerUI](https://swagger.io/tools/swagger-ui/) kann die Spezifikation intuitiv als Webseite dargestellt werden.
Mit [Swagger JS Doc](https://github.com/Surnet/swagger-jsdoc) kann die OpenAPI Spezifikation anhand des Express Code
generiert werden.
So wird sichergestellt, dass Dokumentation und Code synchron sind.

### Tech-Stack

- Backendsprache: Node.JS
- Backend-Framework: [Express.js](http://expressjs.com/)
- Unit-Test-Framework: [Jest](https://jestjs.io/)
- API-Test-Framework: [Supertest](https://www.npmjs.com/package/supertest)

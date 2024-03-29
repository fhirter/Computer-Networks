# DNS - The Internet Directory Service

## Lernziele

* Die Studierenden kennen die Internetprotokolle DNS, [...] und verstehen deren Funktionsweise.
* Die Studierenden können Netzwerkprobleme identifizieren, analysieren und geeignete Lösungsstrategien entwickeln.
* Die Studierenden sind in der Lage, die im Kurs erlernten Techniken und Konzepte in realen Netzwerkumgebungen
  umzusetzen.

## Aufgabenstellung

Die Aufgaben sind bewusst eher umfangreich.
Es ist wichtiger, dass die Aufgaben gründlich gemacht werden, als dass alle Aufgaben erledigt werden.

Zum Erreichen der Lernziele sollten die Aufgaben "Whois Datenbanken", "dig" und "Wireshark" vollständig gelöst werden.

Die Antworten sollen in einem kurzen Bericht festgehalten werden.
**Dieser Bericht ist am Schluss per E-Mail an den Dozenten einzureichen.**
Er wird nicht bewertet, es werden jedoch folgende formellen Anforderungen gestellt:

- Dateiformat: [Markdown](https://www.markdownguide.org/) und daraus [generiertes PDF](https://pandoc.org/).
- Diagramme: [PlantUML](https://plantuml.com/de/), [Mermaid](https://mermaid.js.org/) o.ä.

### Whois Datenbanken

1. Verwende verschiedene Whois-Datenbanken im Internet, um die Namen von zwei DNS-Servern zu ermitteln. Gib an,
   welche Whois-Datenbanken du verwendet hast.
2. Führe mit nslookup auf deinem lokalen Host DNS-Abfragen für drei DNS-Server durch: Den lokalen DNS-Server und
   die zwei DNS-Server, die du in Teil (1) gefunden hast. Versuche Abfragen für Typ A, NS und MX-Einträge. Fasse
   die Ergebnisse zusammen.
3. Verwende die [RIPE-Whois-Datenbank](https://apps.db.ripe.net/db-web-ui/query), um den IP-Adressbereich zu
   ermitteln, der vom Provider der Schulwebsite verwendet wird.

### dig

In dieser Aufgabe verwenden wir das nützliche Werkzeug `dig`, das auf Unix- und Linux-Hosts verfügbar ist, um die
Hierarchie der DNS-Server zu erkunden. Unter Windows kann
ein [Online-Interface](https://toolbox.googleapps.com/apps/dig/) für dig genutzt werden.

Denke daran, dass in Abbildung 2.19 ein DNS-Server eine DNS-Anfrage an einen
DNS-Server weiter unten in der Hierarchie delegiert, indem er dem DNS-Client den Namen dieses untergeordneten
DNS-Servers zurücksendet. Lies zuerst die [Handbuchseite für `dig`](https://linux.die.net/man/1/dig) und beantworte
dann die folgenden Fragen.

1. Beginne mit einem Root-DNS-Server ([[a-m].root-servers.net)](http://a.root-servers.net/).
   Schicke eine Abfrage für die IP-Adresse des Webservers der Schule mit dig. Iteriere durch die Nameserver, bis du
   die IP-Adresse des Webhosts der Webseite der Schule hast.
2. Wiederhole Teil (1) für mehrere beliebte Webseiten, wie google.com, yahoo.com oder amazon.com.

### Wireshark

Untersuche mit Wireshark eine DNS Kommunikation und beantworte folgende Fragen.
DNS Auflösungen werden im Client zwischengespeichert, stelle deshalb sicher, dass die Aufzeichnung mindestens 10min
läuft.

- Welcher DNS-Server hat geantwortet? Wer betreibt diesen Server?
- Welchen Typ hat die DNS Nachricht?
- Welche IP hat der Host?
- Kannst du den DNS-Server für deinen Client auf einen öffentlichen ändern (z.B. 1.1.1.1 (cloudflare), 8.8.8.8 (
  google))?

### DNS Caching

Nehmen wir an, dass unsere Schule einen lokalen DNS-Server für alle Computer, die mit dem Schul-Netzwerk verbinden sind,
hat. Kann ohne spezielle Rechte (Netzwerk-/Systemadministrator) festgestellt werden, ob eine externe Webseite
wahrscheinlich von einem Computer im Netzwerk vor ein paar Sekunden aufgerufen wurde?
Erkläre und schreibe ein Script, um dies festzustellen!

### Angriffe

1. Wie kann DNS verwendet werden, um einen Person-in-the-Middle Angriff durchzuführen?
2. Wie können DNS Angriffe vermieden werden?
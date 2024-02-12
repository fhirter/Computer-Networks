# Übung Transport Layer

## Lernziele

Die Studierenden verstehen den Unterschied zwischen verbindungsloser (UDP) und verbindungsorientierter (TCP)
Kommunikation sowie die Konzepte Fluss- und Staukontrolle.

## Aufgabenstellung

Zum Erreichen der Lernziele sollten beide Aufgaben vollständig gelöst werden.

Die Antworten sollen in einem kurzen Bericht festgehalten werden.
Dieser Bericht ist am Schluss per E-Mail an den Dozenten einzureichen.
**Die Abgabe ist zwingend**, wird jedoch nicht bewertet.
Es werden folgende formellen Anforderungen gestellt:

- Dateiformat: [Markdown](https://www.markdownguide.org/) oder daraus [generiertes PDF](https://pandoc.org/).
- Diagramme: [PlantUML](https://plantuml.com/de/), [Mermaid](https://mermaid.js.org/) o.ä.

Nutze eine dir geläufige Sprache oder nutze die Gelegenheit, um eine neue Sprache auszuprobieren.
Python, JavaScript, C, C#, Go, Rust etc. dürften allesamt gut dafür geeignet sein.

Hardwarenahe Sprachen wie C und [Rust](https://www.rust-lang.org/) werden für derartige, zumeist in Betriebssystemen zu
findende Funktionalität aufgrund der hohen Performance häufig verwendet.

[Go](https://go.dev/) bietet einen guten Mittelweg aus Einfachheit bei der Entwicklung und hoher Performance.

### UDP Kommunikation

Schreibe einen einfachen Client und Server, die Daten per UDP austauschen können.

Der Client soll dem Server einen [UUID](https://de.wikipedia.org/wiki/Universally_Unique_Identifier) schicken können,
worauf der Server eine Textdatei zurückliefert.

Um ein korrektes Funktionieren sicherzustellen, sollen Unit-Tests geschrieben werden.
Ein Vorgehen nach [TDD](https://de.wikipedia.org/wiki/Testgetriebene_Entwicklung) wird empfohlen.

- Zeichne die Kommunikation mit Wireshark auf.
- Messe die Geschwindigkeit der Übertragung und vergleiche diese mit einer TCP-basierten Übertragung.
- Untersuche, wie gross die maximale Paketgrösse ist, die zuverlässig Übertragen werden kann.
  Verschicke mehrere Pakete, wenn diese überschritten wird.
  Setze die Nachricht beim Empfänger wieder zusammen.

### Zuverlässiges Transportprotokoll

Erweitere die UDP Kommunikation um eine zuverlässige Übertragung. 
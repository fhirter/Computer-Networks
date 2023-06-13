# Praktikum Konfiguration
## Lernziele
- Die Studierenden können Konfigurations- und Anwenderdienste in einem eigens geplanten, aufgebauten und konfigurierten Netzwerk einrichten und Netzwerkanalysen durchführen.
- Die Studierenden können die Funktionsweise der Konfigurationsdienste beschreiben und die Protokolle für die Konfiguration eines Netzwerks einsetzen.
- Die Studierenden können selbstständig ein Netzwerk aufbauen, installieren und nach Kundenwunsch konfigurieren.

## Vorbereitung
Starte eine Aufzeichnung mit Wireshark auf deinem default Ethernet Interface.

## Aufgabenstellung
### DHCP und NAT
Untersuche mit Wireshark eine DHCP Kommunikation und beantworte folgende Fragen:
- Welche IP-Adresse wurde vergeben?
- In welchem Subnetz befindet sich die IP? Ist dies ein privates oder öffentliches Netz?
- Welches Default Gateway wurde konfiguriert?
- Welche DNS-Server wurden konfiguriert? Wieso werden oft mehrere DNS-Server konfiguriert?
- Wie ist deine öffentliche IP-Adresse?

Untersuche die Netzwerkkonfiguration von deinem Gerät mit `ifconfig` (macOS, Linux), `ipconfig` (Windows):
- Über welche Netzwerkinterfaces verfügt dein Gerät? Identifiziere die Hardware- sowie WLAN-Schnittstelle.
- Welche MAC Adresse haben die Schnittstellen?
- Welche IPv4 und IPv6 ist auf diesen Schnittstellen konfiguriert?
- Welches Subnetz ist konfiguriert?
- Kannst du die IPv4 und IPv6 Adresse manuell ändern? Was musst du berücksichtigen, dass du noch Internetzugriff hast?

### DNS
Untersuche mit Wireshark eine DNS Kommunikation und beantworte folgende Fragen.
DNS Auflösungen werden im Client zwischengespeichert, stelle deshalb sicher, dass die Aufzeichnung mindestens 10min läuft.
- Welcher DNS-Server hat geantwortet? Wer betreibt diesen Server?
- Welchen Typ hat die DNS Nachricht?
- Welche IP hat der Host?
- Kannst du den DNS-Server für deinen Client auf einen öffentlichen ändern (z.B. 1.1.1.1 (cloudflare), 8.8.8.8 (google))?
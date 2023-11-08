# Praktikum Konfiguration

## Lernziele

- Die Studierenden können selbstständig ein Netzwerk aufbauen, installieren und nach Kundenwunsch konfigurieren.

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

### Netzwerkkonfiguration
Konfiguriere ein Netzwerk gemäss den folgenden Anforderungen.

Organisiert euch selbstständig, analysiert zuerst die Aufgabenstellung zusammen in der Klasse.
Stellt Folgendes sicher:
- Festhalten des Gelernten in einem einfachen Bericht der am Schluss mit allen geteilt wird.
- Regelmässiger Austausch mit den anderen (ca alle 30min)

#### Fragen
- Was sind Vor- und Nachteile von der statischen IP Konfiguration auf dem Host gegenüber einem Mapping mit DHCP?
- Wieso soll die Firewall im `192.168.0.0/23` Netz grundsätzlich allen Traffic blockieren?
- Wieso sind zusätzlich zu NAT Firewall-Regeln nötig?
- Wieso sollen im DHCP-Range keine eingehenden Verbindungen akzeptiert werden?
- Wieso wird der DHCP-Range nur für einen Teil der Adressen genutzt?
- Wieso verwenden wir bei IPv4 NAT?

#### Router
- `192.168.0.0/23` Netzwerk an eth0
- `192.168.10.0/24` Netzwerk an eth1
- DHCP Client (WAN) an eth2
- NAT mit Weiterleitung von Port 80 an `192.168.10.10/24`

#### Hosts
- Python Webserver aus Übung 03 auf Raspberry PI 
  - fixe IP `192.168.10.10/24` konfiguriert auf dem Host
  - Optional: automatischer Start beim Boot
  - Optional: Applikation containerisieren
- 3 Raspberry PI als DHCP Clients

#### DHCP
- DHCP Server nur im `192.168.0.0/23` Netz
- DHCP Range: `192.168.0.100` - `192.168.1.200`
- Ein Raspberry PI mit statisch gemappter IP `192.168.0.100/23`

#### Firewall
- Keinen eingehenden Verbindungsaufbau im `192.168.0.0/23` Netz
- Blockiert im `192.168.10.0/24` Netz sämtliche Verbindungen bis folgende Ausnahme:
  - `192.168.10.10` lässt TCP Verbindungen auf Port 80 zu

## Default-Einstellungen

### Raspberry PI
- IP: DHCP
- user: pi
- password: password

### EdgeRouter
- IP: 192.168.1.1
- user: ubnt
- password: ubnt
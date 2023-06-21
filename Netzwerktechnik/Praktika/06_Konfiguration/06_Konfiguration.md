# Praktikum Konfiguration

## Lernziele

- Die Studierenden können selbstständig ein Netzwerk aufbauen, installieren und nach Kundenwunsch konfigurieren.

## Anforderungen an das Netzwerk

### Router
- `192.168.0.0/23` Netzwerk an eth0
- `192.168.10.0/24` Netzwerk an eth1
- DHCP Client (WAN) an eth2
- NAT mit Weiterleitung von Port 80 an `192.168.10.10/24`

### Hosts
- Python Webserver aus Übung 03 auf Raspberry PI 
  - fixe IP `192.168.10.10/24` konfiguriert auf dem Host
  - Optional: automatischer Start beim Boot
  - Optional: Applikation containerisieren
- 3 Raspberry PI als DHCP Clients

### DHCP
- DHCP Server nur im `192.168.0.0/23` Netz
- DHCP Range: `192.168.0.100` - `192.168.1.200`
- Ein Raspberry PI mit statisch gemappter IP `192.168.0.20/23`

### Firewall
- Keinen eingehenden Verbindungsaufbau im `192.168.0.0/23` Netz
- Blockiert im `192.168.0.0/24` Netz sämtliche Verbindungen bis folgende Ausnahme:
  - `192.168.0.10` lässt TCP Verbindungen auf Port 80 zu

## Default-Einstellungen

### Raspberry PI
- IP: DHCP
- user: PI
- password: password

### EdgeRouter
- IP: 192.168.1.1
- user: ubnt
- password: ubnt

## Vorgehen

Organisiert euch selbstständig, analysiert zuerst die Aufgabenstellung zusammen in der Klasse.
Stellt Folgendes sicher:
- Festhalten des Gelernten in einem einfachen Bericht der am Schluss mit allen geteilt wird.
- Regelmässiger Austausch mit den anderen (ca alle 30min)

## Fragen
- Was sind Vor- und Nachteile von der statischen IP Konfiguration auf dem Host gegenüber einem Mapping mit DHCP?
- Wieso soll die Firewall im `192.168.0.0/23` Netz grundsätzlich allen Traffic blockieren?
- Wieso sind zusätzlich zu NAT Firewall-Regeln nötig?
- Wieso sollen im DHCP-Range keine eingehenden Verbindungen akzeptiert werden?
- Wieso wird der DHCP-Range nur für einen Teil der Adressen genutzt?
- Wieso verwenden wir bei IPv4 NAT?
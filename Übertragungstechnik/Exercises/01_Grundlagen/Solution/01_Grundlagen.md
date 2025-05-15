# Übung Bandbreite - Lösung

## Überblick

> Skizziere den Weg des Signals vom Stadion bis zum heimischen TV.

```mermaid
flowchart LR
    Videokamera -- SDI --> mobile
    mobile[Mobile Bildregie] -- Radio/Fibre --> SRF
    SRF -- Fibre --> ISP
    ISP -- Fibre --> router[Customer Router]
    router -- Copper --> TV

```

> Was bedeutet Encoding bzw Codierung?

Das Signal wird für die Übertragung aufbereitet indem die Datenrate reduziert wird, das Signal also komprimiert wird.

> Wie unterscheiden sich Ethernet und WLAN bezüglich Übertragungsstörungen? Wieso?

Ethernet ist weniger störungsanfällig, weil es kabelgebunden ist und der Kanal, also das Kabel, nicht mit anderen
Übertragungen geteilt wird. Funkübertragung ist immer ein geteilter Kanal.

> Wozu dient Komprimierung?

Reduktion der zu Übertragenden Datenmenge.

 
> Der Artikel spricht von "Bandbreite". Welcher Fachbegriff wäre hier korrekt? Und was ist die eigentliche Bedeutung von
> Bandbreite?

Der korrekte Fachbegriff ist "Datenübertragungsrate". Bandbreite bezeichnet den Frequenzbereich, den eine 
Übertragung nutzen kann. Eine hohe Bandbreite korreliert in der Regel mit einer hoher Datenübertragungsrate.


> Was sind die Eigenschaften von Koaxialkabel?

- Hohe Bandbreite
- Geringere Störanfälligkeit als Twisted Pair
- Teuerer als Twisted Pair
- Schwieriger zu installieren
 
> Wieso wird immer mehr IP basierte Übertragung genutzt? Welche Vor- und Nachteile hat das?

Mit IP-basierter Übertragung kann für Video oder Tonübertragung dieselbe Infrastruktur genutzt werden wie für 
Internet/Datenübertragung. Dies führt zu grossen Kosteneinsparungen.

## Zeit- und Frequenzbereich

### Fourier

$$
y(t) = \frac{\hat{y}}{2}+\frac{2\hat{y}}{\pi}(sin(\omega t)+\frac{1}{3}sin(3\omega t)+\frac{1}{5}sin(5\omega t))
$$

### Bandbreite

- DAB
    - 174-230MHz, 1452-1492MHz / 1.536MHz pro Kanal
- DVB-T
    - 177.5-226.5MHz / 7MHz pro Kanal
    - 474-786MHz / 8MHz pro Kanal
- WLAN
    - 2.4-2.4835GHz / 20MHZ, 40MHz pro Kanal
    - 5.15-5.35GHz / 20MHZ, 40MHz, 80MHz, 160MHz pro Kanal
    - 5.47-5.725GHz / 20MHZ, 40MHz, 80MHz, 160MHz pro Kanal
- ADSL2+
    - 138 - 2208 kHz / 4.3125kHZ pro Kanal
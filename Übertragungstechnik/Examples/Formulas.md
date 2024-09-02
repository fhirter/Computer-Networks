# Übertragungstechnik Formeln

## Modulation eines sinusförmigen Trägers

$$
s(t) = A(t)sin(\omega(t)t+\varphi(t))
$$

### Quadraturamplituden Modulation

Phase und Amplitude werden unabhängig moduliert:
$$
s(t) = A(t)sin(\omega t+\varphi(t))
$$

Mit Vektorgeomietrie können die Polarkoordinaten Amplitude und Phase wie folgt in Kartesische Koordinaten 
umgerechnet werden:

Dies ergibt für Amplitude und Phase des Signals:
$$
A(t) = \sqrt{I(t)^2+Q(t)^2}
$$

$$
\varphi(t) = arctan(\frac{Q(t)}{I(t})
$$

Damit kann die erste Formel in folgenden Ausdruck umgeformt werden:

$$
s(t) = I(t)cos(\omega t)-Q(t)sin(\omega t)
$$

Zwei phasenverschobene Träger (sin und cos), die separat moduliert (I und Q) und anschliessend voneinander subtrahiert 
werden.
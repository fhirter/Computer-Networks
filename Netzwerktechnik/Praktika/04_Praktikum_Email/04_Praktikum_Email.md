# Praktikum E-Mail

## Lernziele
Die Studierenden können die Anwenderdienste für das Senden und Empfangen von Mails mit ihren Merkmalen  charakterisieren und einen Mailclient in der Praxis konfigurieren. 

Die Studierenden sind in der Lage, Netzwerkanalysen mit entsprechenden Tools durchzuführen, die Ergebnisse zu analysieren und einfache Netzwerkfehler zu beheben. 

Die Studierenden können die Aufgaben von HTTP nennen und den Ablauf der wichtigsten Funktionen beschreiben.


## Vorbereitung
Erstelle ein Login und einen API Key bei folgendem Dienst: 
* [Openrouteservice](https://openrouteservice.org/dev/#/api-docs)

## Aufgabenstellung
Schreib ein Python eine kleine Applikation, die per E-Mail Routen-Informationen liefert.
Es soll eine verschlüsselte Mail geschickt werden können welche zwei Adressen enthält:
```
Bundesplatz 3, 3005 Bern
Freiburgstrasse 20, 3010 Bern
```
Anhand von diesen Informationen soll die Applikation eine Route erstellen und per verschlüsselter E-Mail zurückschicken.

Nutze einen eigenen Mailserver oder den zur Verfügung gestellten. 
Dessen Verbindungsangaben findest du hier:
https://docs.immerda.ch/de/services/email/clients/

Der Erkenntnisgewinn ist wichtiger als eine vollständige Lösung. Halte deine Erkenntnisse fest!

**Vorsicht: Secrets (Passwörter, Private Keys) dürfen nie in der Versionsverwaltung erfasst werden!** Falls dies trotzdem passiert müssen die Passwörter und Keys sofort geändert werden.

## E-Mail Empfangen
- Empfange die neuste ungelesene Mail und den Absender mit IMAP:
- Entschlüssle die Nachricht mit dem PGP Public Key.

```python
import email
import imaplib

def get_latest_new_email():
    with imaplib.IMAP4_SSL(imap_server) as server:
        server.login(account_email, password)
        server.select(mailbox)

        response, data = server.search(None, '(UNSEEN)')

        # get the latest
        data = data[0].split()
        latest = data[-1]

        # mark the email as read
        server.store(latest, '+FLAGS', '\Seen')

        # fetch the email (RFC822) for the ID (latest)
        result, email_data = server.fetch(latest, "(BODY[])")
        raw_email = email_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)

        # Get the 'From' field
        from_field = email_message['From']

        # print the email body
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                return from_field, body
            else:
                continue
```

## E-Mail Senden
- Nutze folgende Befehle der smtplib um E-Mails zu versenden. Konfiguriere die verwendeten Variablen entsprechend.
- Verschlüssele die Nachricht mit einem PGP Public Key. Erstelle dazu ein persönliches Public/Private Key-Paar online oder mit gpg in der Konsole.

```python
import smtplib
import ssl
def send_mail(message, receiver_email):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(account_email, password)
        server.sendmail(account_email, receiver_email, message)
```



## REST API Abfragen
- Erstelle eine Anfrage mit Insomnia oder cURL um die Koordinaten für eine Adresse zu erhalten ([openrouteservice.org/dev/#/api-docs/geocode](https://openrouteservice.org/dev/#/api-docs/geocode/search/get)). 
- Erstelle eine Anfrage mit Insomnia oder cURL um die Route zwischen diesen beiden Koordinaten zu erhalten. ([openrouteservice.org/dev/#/api-docs/v2/directions](https://openrouteservice.org/dev/#/api-docs/v2/directions/{profile}/get)).
- Übertrage die beiden API Anfragen in Python nach folgendem Code Beispiel.

```python
import requests

def get_coordinates(address):
    url = f"<endpoint>?<parameter>={<value>}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["features"][0]["geometry"]["coordinates"]
    else:
        print(f"Request failed with status code {response.status_code}")
```

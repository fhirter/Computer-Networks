# Praktikum E-Mail

## Lernziele

- Die Studierenden können die Anwenderdienste für das Senden und Empfangen von Mails mit ihren Merkmalen
  charakterisieren
  und einen Mailclient in der Praxis konfigurieren.
- Die Studierenden sind in der Lage, Netzwerkanalysen mit entsprechenden Tools durchzuführen, die Ergebnisse zu
  analysieren und einfache Netzwerkfehler zu beheben.
- Die Studierenden können die Aufgaben von HTTP nennen und den Ablauf der wichtigsten Funktionen beschreiben.
- Die Studierenden kennen das Matrix Protokoll und können einen einfachen Client selber implementieren.

## Vorbereitung

Erstelle ein Login und einen API Key bei folgendem Dienst:

* [Openrouteservice](https://openrouteservice.org/dev/#/api-docs)

## Aufgabenstellung

Schreib in Python eine kleine Applikation, die per E-Mail eine Adresse in Koordinaten auflöst.
Es soll eine E-Mail geschickt werden können, welche eine Adresse enthält:

```
Freiburgstrasse 20, 3010 Bern
```

Anhand von diesen Informationen soll die Applikation die Koordinaten abfragen und per E-Mail zurückschicken.

Nutze einen eigenen Mailserver oder den zur Verfügung gestellten. Dessen Verbindungsangaben findest du hier:
https://docs.immerda.ch/de/services/email/clients/

Erstelle die REST Anfragen mit Insomnia oder cURL und übertrage die Anfragen anschliessend in Python gemäss dem Beispiel
weiter unten.
Nutze folgende Endpoints:

- ([openrouteservice.org/dev/#/api-docs/geocode](https://openrouteservice.org/dev/#/api-docs/geocode/search/get)).
- ([openrouteservice.org/dev/#/api-docs/v2/directions](https://openrouteservice.org/dev/#/api-docs/v2/directions/{profile}/get)).

Der Erkenntnisgewinn ist wichtiger als eine vollständige Lösung.
Das Vorgehen, die Antworten und Erkenntnisse sollen in einem kurzen Bericht festgehalten werden.
Dieser Bericht ist am Schluss zusammen mit dem Code **per E-Mail an den Dozenten** einzureichen.
Er wird nicht bewertet, es werden jedoch folgende formellen Anforderungen gestellt:

- Dateiformat: [Markdown](https://www.markdownguide.org/) oder daraus [generiertes PDF](https://pandoc.org/).
- Diagramme: [PlantUML](https://plantuml.com/de/), [Mermaid](https://mermaid.js.org/) o.ä.

**Vorsicht: Secrets (Passwörter, Private Keys) dürfen nie in der Versionsverwaltung erfasst werden!**
Falls dies trotzdem passiert, muss das betroffene Secret sofort geändert werden.

### Erweiterungen

#### PGP-Verschlüsselung

Implementiere eine mit PGP verschlüsselte Kommunikation.

- Verschlüssle die Antwort-Nachricht mit einem PGP Public Key. Erstelle dazu ein persönliches Public/Private Key-Paar
  online oder mit gpg in der Konsole und hänge diesen der E-Mail an. Lade und verwende diesen Schlüssel in der
  Applikation.
- Entschlüssle die Anfrage-Nachricht mit dem PGP Private Key.

### Matrix

Erweitere die Applikation mit einer [Matrix](https://matrix.org/)-Anbindung:

- Löse Nachrichten in diesem Kanal analog der E-Mail Funktionalität in Koordinaten auf.
- Aktivieren den Bot, indem du die Nachrichten mit `@coordinates` o.ä. beginnst.

Informiere dich über die Funktionsweise in der [Dokumentation](https://matrix.org/docs/).

Erstelle zuerst einen [Matrix-Account](https://matrix.org/docs/chat_basics/matrix-for-im/#creating-a-matrix-account) und
einen öffentlichen [Space und Raum](https://matrix.org/docs/communities/getting-started/).

Nutze z.B. die Library ["nio"](https://github.com/poljar/matrix-nio).

## Code Beispiele

### E-Mail Empfangen

Empfange die neuste ungelesene Mail mit IMAP.
Folgende Variablen musst du vorgängig konfigurieren:

- `imap_server`: Die URL des IMAP Servers
- `account_email`, `password`: E-Mail-Adresse und Passwort des Accounts auf dem IMAP Server
- `mailbox`: Der Name des Postfachs, das abgerufen werden soll

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

### E-Mail Senden

Folgende Variablen musst du vorgängig konfigurieren:

- `smtp_server`: URL des SMTP-Servers
- `smtp_port`: Port des SMTP-Servers
- `account_email`, `password`: E-Mail-Adresse und Passwort des Accounts auf dem SMTP Server

```python
import smtplib
import ssl


def send_mail(message, receiver_email):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(account_email, password)
        server.sendmail(account_email, receiver_email, message)
```

### REST API Abfragen

```python
import requests


def get_coordinates(address):
    url = f"<endpoint>?<parameter>={< value >}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["features"][0]["geometry"]["coordinates"]
    else:
        print(f"Request failed with status code {response.status_code}")
```

## Verschlüsselung

```python
import subprocess
import os


def encrypt_message(recipient_mail, message):
    """
    Encrypts data using key.
    """

    temp_message_path = "./tmp.txt"
    temp_message = open(temp_message_path, "w")
    temp_message.writelines(message)

    # gpg --recipient 6B0AC064EA829F61F730447DEF62CA8C485DEE52 --batch -o- --encrypt <(printf "foo")
    status = subprocess.check_call([
        "gpg",
        "--recipient", recipient_mail,
        "--batch",
        "--encrypt", temp_message_path
    ])

    temp_message_path_encrypted = f"{temp_message_path}.gpg"

    if status == 0:
        with open(temp_message_path_encrypted, mode='rb') as file:
            encrypted_message = file.read()

        os.remove(temp_message_path)
        os.remove(temp_message_path_encrypted)

        return encrypted_message
```
